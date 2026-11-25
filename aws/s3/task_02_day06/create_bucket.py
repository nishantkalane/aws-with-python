import boto3

#connect to Amazon S3
s3 = boto3.client('s3')

#choose a unique bucket name
bucket_name = 'nishant-day6-se-practical-2026'

#create the bucket
response = s3.create_bucket(
    Bucket = bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-2'
    }
)

print("Bucket created successfully!")
print(response)

