import boto3
import os
from dotenv import load_dotenv
import argparse

def download_data(bucket_name, key, download_path):
    load_dotenv()
    access_key = os.getenv('MINIO_ROOT_USER')
    secret_key = os.getenv('MINIO_ROOT_PASSWORD')
    
    s3 = boto3.client(
        's3',
        endpoint_url='http://127.0.0.1:9000',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    
    s3.download_file(bucket_name, key, download_path)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", required=True)
    parser.add_argument("--key", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    download_data(args.bucket, args.key, args.output)