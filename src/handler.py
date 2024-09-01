import json, sys, os

import pandas
import polars
import requests

def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            "key": "hello from lambda"
        })
    }
        
        
  