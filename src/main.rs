use polars::prelude::*;
use std::io::Cursor;
use reqwest::blocking::Client;

fn main() {
    
    let url = "https://theunitedstates.io/congress-legislators/legislators-historical.csv";
    
    let mut schema = Schema::new();
    schema.with_column(
        "first_name".into(),
        DataType::Categorical(None, Default::default()),
    );
    schema.with_column(
        "gender".into(),
        DataType::Categorical(None, Default::default()),
    );
    schema.with_column(
        "type".into(),
        DataType::Categorical(None, Default::default()),
    );
    schema.with_column(
        "state".into(),
        DataType::Categorical(None, Default::default()),
    );
    schema.with_column(
        "party".into(),
        DataType::Categorical(None, Default::default()),
    );
    schema.with_column("birthday".into(), DataType::Date);
    
    let data: Vec<u8> = Client::new()
        .get(url)
            .send().expect("msg")
            .text().expect("msg")
            .bytes()
        .collect();
    // print!("{:?}", data);
    
    let dataset = CsvReadOptions::default()
        .with_has_header(true)
        // .with_schema(Some(Arc::new(schema)))
        .map_parse_options(|parse_options| parse_options.with_try_parse_dates(true))
        .into_reader_with_file_handle(Cursor::new(data))
        .finish()
        .unwrap();
    
    println!("{}", &dataset);
}