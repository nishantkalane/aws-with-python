"""List all S3 buckets in the account."""

import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client("s3")

for bucket in s3.list_buckets()["Buckets"]:
    print(bucket["Name"])
