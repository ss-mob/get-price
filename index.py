import boto3
import os
import json

def lambda_handler(event, context):
    db_host = os.environ['db_host']
    client = boto3.resource('dynamodb')
    table = client.Table(db_host)
    response = table.get_item(
        Key={
            'productId': event['queryStringParameters']['productId']
        }
    )

    if 'Item' in response:
        return {
            'statusCode': '200',
            'body': json.dumps(response['Item'])
            }
        
    else:
        return {
            'statusCode': '404',
            'body': 'Product not found'
        }
