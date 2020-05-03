import boto3
import json

s3_client = boto3.client('s3')

'''
    :returns: list of buckets
'''


def lambda_handler(event, context):
    response = s3_client.list_buckets()['Buckets']

    bucket_names = [x['Name'] for x in response]
    return {
        "statusCode": 200,
        "body": json.dumps({
            "list_buckets": bucket_names
        })
    }