import json
import boto3
import botocore

def lambda_handler(event, context):
    client = boto3.client('s3', 'us-east-2', config=botocore.config.Config(s3={'addressing_style':'path'}))
    

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
