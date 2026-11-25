import boto3

#connect to Amazon S3
s3 = boto3.client('s3')

#choose a unique bucket name
bucket_name = 'nishant-day6-se-practical-2026'



# task_02 upload a file 

file_name= 'first.txt'

with open(file_name,'w') as file:
    file.write("Hello! This is my first AWS S3 practical using Boto3.")

print("Text file created successfully")

object_name = 'first_one'
s3.upload_file(file_name, bucket_name, object_name)

#task_03 upload 3 more files 

files = {
    'second.txt': 'This is my second file.',
    'third.txt': 'This is my third file.',
    'fourth.txt': 'This is my fourth file.'
}

# Iterate through the dictionary
for file_n, content in files.items():

    #create the local text file
    with open(file_n, 'w') as file:
        file.write(content)

    #upload to s3 with the same object name
    s3.upload_file(file_n, bucket_name, file_n)


