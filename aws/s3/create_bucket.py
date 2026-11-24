"""Create an S3 bucket using boto3.

Credentials come from `aws configure` or from a local .env file
(see .env.example). Bucket names are globally unique, so change BUCKET_NAME.
"""

import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = "my-unique-bucket-name-12345"  # change this
REGION = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")


def create_bucket(bucket_name: str, region: str) -> None:
    s3 = boto3.client("s3", region_name=region)
    try:
        # us-east-1 must NOT pass a LocationConstraint; every other region must.
        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print(f"Bucket '{bucket_name}' created in {region}")
    except ClientError as err:
        print(f"Could not create bucket: {err}")


if __name__ == "__main__":
    create_bucket(BUCKET_NAME, REGION)
