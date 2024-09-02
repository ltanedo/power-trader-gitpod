import json, sys, os

import pandas
import polars
import requests

def lambda_handler(event, context):

    resp = requests.get("https://api.orats.io/datav2/snapshot/strikes15",
        params={
            "token": "{YOUR_ORATS_KEY}",
            "tradeDate": "202008201130"
        }
    )
    
    snapshot = pd.read_csv(StringIO(resp.text))
    print(snapshot)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            "key": "hello from lambda"
        })
    }
        
        
  