use reqwest::header::{HeaderMap, HeaderValue};
use std::collections::HashMap;
use serde_json::Value;
use reqwest::header::HeaderName;
use serde_json::json;


pub(crate) fn flatten_records(records: &Value) -> Vec<Value> {
    records.as_array().unwrap().iter().map(|record| {
        let mut flattened_record = serde_json::Map::new();
        flatten_object(record, &mut flattened_record, "");
        Value::Object(flattened_record)
    }).collect()
}

fn flatten_object(obj: &Value, result: &mut serde_json::Map<String, Value>, prefix: &str) {
    match obj {
        Value::Object(obj) => {
            for (key, value) in obj {
                match value {
                    Value::Object(_inner_obj) => {
                        let new_prefix = if prefix.is_empty() {
                            key.clone()
                        } else {
                            format!("{}.{}", prefix, key)
                        };
                        flatten_object(value, result, &new_prefix);
                    }
                    _ => {
                        let key_str = if prefix.is_empty() {
                            key.clone()
                        } else {
                            format!("{}.{}", prefix, key)
                        };
                        result.insert(key_str, value.clone());
                    }
                }
            }
        }
        _ => {}
    }
}

fn json_to_hashmap(json_obj: Value) -> HashMap<String, Value> {
    let mut hashmap = HashMap::new();
    let obj = json_obj.as_object().unwrap();
    for (key, value) in obj {
        match value {
            Value::Array(arr) => {
                let vec: Vec<String> = arr
                    .clone()
                    .into_iter()
                    .map(|v| match v {
                        Value::String(s) => s.clone(),
                        _ => panic!("Unsupported value type"),
                    })
                    .collect();
                hashmap.insert(key.clone(), Value::String(format!("{:?}", vec)));
            }
            _ => {
                hashmap.insert(key.clone(), value.clone());
            }
        }
    }
    hashmap
}

pub enum Response {
    Text(String),
    Json(Value),
}

pub(crate) struct Requests<'a> {
    pub url: &'a str,
    pub params: Value,
    pub headers: Value,
    pub client: reqwest::Client,
    pub timeout: u64,
}

impl<'a> Default for Requests<'a> {
    fn default() -> Self {
        Self {
            url: "",
            params: json!({}),
            headers: json!({}),
            client: reqwest::Client::new(),
            timeout: 60,
        }
    }
}

impl<'a> Requests<'a> {
    pub(crate) async fn get(self) -> Result<Response, Box<dyn std::error::Error>> {
        let mut headers_map = HeaderMap::new();
        let headers_temp = &json_to_hashmap(self.headers.clone());
        for (k, v) in headers_temp.iter() {
            let header_name = HeaderName::from_bytes(k.as_bytes()).unwrap();
            headers_map.insert(header_name, HeaderValue::from_str(v.as_str().unwrap()).unwrap());
        }

        let response = self.client
            .get(self.url)
            .query(&json_to_hashmap(self.params.clone()))
            .headers(headers_map.clone())
            .timeout(std::time::Duration::from_secs(self.timeout))
            .send().await?;

        // println!("[{:?}] {} \n{:?}", response.status(), response.url(), headers_map);

        let content_type = response.headers().get("Content-Type").unwrap().to_str().unwrap();
        if content_type.starts_with("application/json") {
            let json: Value = response.json().await?;
            Ok(Response::Json(json))
        } else {
            let text = response.text().await?;
            Ok(Response::Text(text))
        }
    }
}