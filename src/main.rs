
#[path = "handler.rs"] mod handler;
use crate::handler::handler;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {

    let _ = handler().await;
    Ok(())
}