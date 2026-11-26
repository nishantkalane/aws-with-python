
import boto3
import os

# Connect to S3
s3 = boto3.client(
    's3',
    region_name='ap-southeast-2'
)

# Existing S3 bucket
bucket_name = 'nk-task04-paginator-2026'

# Get the current project directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Locate duplicate_files folder
folder_name = os.path.join(base_dir, "duplicate_files")

# Upload all files to S3
for file_name in os.listdir(folder_name):

    file_path = os.path.join(folder_name, file_name)

    if os.path.isfile(file_path):

        s3.upload_file(
            file_path,
            bucket_name,
            file_name
        )

        print(f"Uploaded: {file_name}")

print("\nAll Task 05 files uploaded successfully!")
