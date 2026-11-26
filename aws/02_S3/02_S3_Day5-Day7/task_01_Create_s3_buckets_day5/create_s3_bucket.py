import boto3

# Create an S3 client
s3 = boto3.client('s3', region_name='ap-southeast-2')

# Create bucket
response = s3.create_bucket(
    Bucket='nishant-aws-s3-practice-2026',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-2'
    }
)

print("Bucket created successfully!")
print(response)