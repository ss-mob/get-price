import boto3
import os


def lambda_handler(event, context):
    db_host = os.environ['db_host']
    client = boto3.resource('dynamodb')
    table = client.Table(db_host)
    response = table.get_item(
        Key={
            'productId': event['productId']
        }
    )

    if 'Item' in response:
        return response['Item']
    else:
        return {
            'statusCode': '404',
            'body': 'Product not found'
        }