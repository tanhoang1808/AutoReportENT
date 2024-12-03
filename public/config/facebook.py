from dotenv import load_dotenv
import boto3
import os
import json

s3_client = boto3.client('s3')
def get_access_token():
    bucket_name = "enternetvn"
    file_name = "package.json"
    print("bucket name : ",bucket_name)
    print("file_name : ",file_name)
    s3_response = s3_client.get_object(Bucket=bucket_name,Key=file_name)
    file_data = s3_response['Body'].read().decode('utf-8')
    json_data = json.loads(file_data)
    token_data = json_data
    return token_data
