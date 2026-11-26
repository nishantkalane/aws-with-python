
import boto3
import os

# Connect to S3
s3 = boto3.client('s3', region_name='ap-southeast-2')

# S3 bucket name
bucket_name = 'nk-task04-paginator-2026'

# Get the text_files folder path
base_dir = os.path.dirname(os.path.abspath(__file__))
folder_name = os.path.join(base_dir, "text_files")

# Upload all text files to S3
for file_name in os.listdir(folder_name):

    if file_name.endswith(".txt"):

        file_path = os.path.join(folder_name, file_name)

        s3.upload_file(
            file_path,
            bucket_name,
            file_name
        )

        print(f"Uploaded: {file_name}")

print("\nAll files uploaded successfully!")
