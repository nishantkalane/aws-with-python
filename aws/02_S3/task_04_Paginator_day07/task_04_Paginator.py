
import boto3

# Connect to S3
s3 = boto3.client('s3', region_name='ap-southeast-2')

# Bucket name (must be globally unique)
bucket_name = 'nk-task04-paginator-2026'

# Create the bucket
response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-2'
    }
)

print("Bucket created successfully!")
print("Bucket Name:", bucket_name)
print("Response:", response)
