import boto3
import time

# Connect to Amazon S3
s3 = boto3.client('s3')

# Existing bucket name
bucket_name = 'nishant-day6-se-practical-2026'

#first uploaded object's key
object_name = 'fourth.txt'

#Generate a presigned URL
url = s3.generate_presigned_url(
    'get_object',
    Params={
        'Bucket': bucket_name,
        'Key': object_name
    },
    ExpiresIn=60
)

print("Presigned URL:")
print(url)

#deleting the object after the file access time expires

print("Waiting for 1 minutes...")

time.sleep(60)

s3.delete_object(
    Bucket= bucket_name,
    Key = object_name
)

print("Object deleted from S3!")