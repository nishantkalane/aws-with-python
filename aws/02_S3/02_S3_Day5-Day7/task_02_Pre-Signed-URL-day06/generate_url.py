import boto3
import time

# Connect to Amazon S3
s3 = boto3.client('s3')

# Existing bucket name
bucket_name = 'nishant-day6-se-practical-2026'

#first uploaded object's key
object_name = 'fourth.txt'
URL_EXPIRY_SECONDS = 300

#Generate a presigned URL
url = s3.generate_presigned_url(
    'get_object',
    Params={
        'Bucket': bucket_name,
        'Key': object_name
    },
    ExpiresIn=URL_EXPIRY_SECONDS
)

print("Presigned URL:")
print(url)

#deleting the object after the file access time expires

print(f"Waiting for {URL_EXPIRY_SECONDS // 60} minutes...")

time.sleep(URL_EXPIRY_SECONDS)

s3.delete_object(
    Bucket= bucket_name,
    Key = object_name
)

print("Object deleted from S3!")