import boto3
import argparse
import os
from dotenv import load_dotenv

def upload_data(bucket_name, key, file_path):
    load_dotenv()
    s3 = boto3.client(
        's3',
        endpoint_url='http://127.0.0.1:9000',
        aws_access_key_id=os.getenv('MINIO_ROOT_USER'),
        aws_secret_access_key=os.getenv('MINIO_ROOT_PASSWORD')
    )
    s3.upload_file(file_path, bucket_name, key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", required=True)
    parser.add_argument("--key", required=True)
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    upload_data(args.bucket, args.key, args.file)
