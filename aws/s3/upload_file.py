"""Upload a local file to an S3 bucket."""

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = "my-unique-bucket-name-12345"  # change this
LOCAL_FILE = "sample.txt"                    # file to upload
S3_KEY = "sample.txt"                        # name inside the bucket

s3 = boto3.client("s3")

try:
    s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_KEY)
    print(f"Uploaded {LOCAL_FILE} to s3://{BUCKET_NAME}/{S3_KEY}")
except (ClientError, FileNotFoundError) as err:
    print(f"Upload failed: {err}")
