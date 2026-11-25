import boto3

s3= boto3.client('s3')

bucket_name = 'nishant-day6-se-practical-2026'

#list all the objects in the bucket

response = s3.list_objects_v2(
    Bucket = bucket_name
)

print(response)

#display all object names

if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("Bucket is empty!")
