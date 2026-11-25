
import boto3
import os
import tempfile

# Connect to S3
s3 = boto3.client(
    's3',
    region_name='ap-southeast-2'
)

# S3 bucket name
bucket_name = 'nk-task04-paginator-2026'

# Create a paginator
paginator = s3.get_paginator('list_objects_v2')

# Store file contents and their filenames
content_map = {}

# Create a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:

    # Retrieve all objects from S3
    pages = paginator.paginate(Bucket=bucket_name)

    file_count = 0

    for page in pages:

        objects = page.get('Contents', [])

        for obj in objects:

            file_key = obj['Key']

            # Download only text files
            if not file_key.endswith('.txt'):
                continue

            file_count += 1

            # Create a temporary local path
            local_path = os.path.join(
                temp_dir,
                f"file_{file_count}.txt"
            )

            # Download object from S3
            s3.download_file(
                bucket_name,
                file_key,
                local_path
            )

            # Read the downloaded file contents
            with open(local_path, 'rb') as file:
                content = file.read()

            # Group filenames by their exact contents
            content_map.setdefault(content, []).append(file_key)

# Print duplicate files
print("\nDuplicate files found:")

duplicate_count = 0

for content, file_names in content_map.items():

    if len(file_names) > 1:

        duplicate_count += 1

        print("\nDuplicate Group:")

        for name in file_names:
            print(name)

print("\nTotal duplicate groups:", duplicate_count)