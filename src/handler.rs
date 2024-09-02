#[path = "rust_libs/requests_async.rs"] mod requests_async;
use requests_async::*;
use polars::prelude::*;
use serde_json::json;
use std::io::Cursor;   
use polars::io::json::JsonWriter;
use std::fs::File;

pub(crate) async fn handler() -> Result<(), Box<dyn std::error::Error>> {

    let request = Requests {
            url: "https://api.orats.io/datav2/snapshot/strikes15",
            params: json!({
              "token": "{YOUR_ORATS_KEY}",
              "tradeDate": "202008201130",
            }),
        ..Requests::default()
    };
    
    let response = request.get().await.unwrap();
    match response {
        Response::Text(text) => {
            println!("Text response: {}", text)
        },
        Response::Json(json) => {
            // println!("JSON response: {}", json);
            let new_json = flatten_records(&json);
            let json_str = serde_json::to_string(&new_json).unwrap();
            let cursor = Cursor::new(json_str);
            let mut df = JsonReader::new(cursor).finish().unwrap();
            println!("{}", df);

            let file = File::create("__data__/output.json")?;
            let mut writer = JsonWriter::new(file).with_json_format(JsonFormat::Json);
            writer.finish(&mut df)?;

            let file: File = File::create("__data__/output.csv")?;
            let mut writer = CsvWriter::new(file);
            writer.finish(&mut df)?;

            let file: File = File::create("__data__/output.parquet")?;
            let writer = ParquetWriter::new(file);
            writer.finish(&mut df)?;            
        },
    }
    Ok(())
}