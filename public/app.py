import os
import json
import sys
from datetime import datetime
import boto3

# Import processHandler từ package handler
from handler import processHandler


s3_client = boto3.client('s3')


def lambda_handler(event, context):
    main()


def save_employee_data_to_file(data, bucket_name, file_name):
    json_data = json.dumps(data,indent=4)
    try:
        # Lưu trữ JSON vào S3
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=json_data)
        print(f"Successfully uploaded data to {bucket_name}/{file_name}")
    except Exception as e:
        print(f"Failed to upload data: {str(e)}")


def load_employee_data_from_file(bucket_name, file_name):
    employee_data = {}
    s3_response = s3_client.get_object(Bucket=bucket_name,Key=file_name)
    file_data = s3_response['Body'].read().decode('utf-8')
    json_data = json.loads(file_data)
    employee_data = json_data
    return employee_data


def run(employee_data):
    for employee, data in employee_data.items():
        processHandler.process_employee_data(employee, data, employee_data)


def main():
    # Lấy dữ liệu từ S3 Bucket
    employee_data = load_employee_data_from_file(bucket_name="enternetvn",file_name="agency_data.json")
    print("employee_data : ",employee_data)
    # Chạy chương trình
    run(employee_data)
    # print("employee_data final",employee_data)
    # Lưu dữ liệu từ S3 Bucket dưới dạng Json object
    save_employee_data_to_file(employee_data,bucket_name="enternetvn",file_name="agency_data.json")
    


