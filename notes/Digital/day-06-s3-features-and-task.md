# Day 6: S3 features and Task 01

Date: 2026-11-24

## Done in class

1. Learnt the benefits and main features of S3: storage limits, S3 Glacier, versioning, pre-signed URLs and static website hosting.
2. Did **Task 01** (bucket, uploads, listing, a 5-minute pre-signed URL, download and delete) and saved my solution in `aws/s3/`.

## Key points

### 1. Benefits of S3

- **Virtually unlimited storage.** You pay only for what you use (pay as per usage).
- A single object can be very large: the maximum size of one object is **5 TB**. (My handwritten page says 50 TB; the AWS limit is 5 TB. Objects over 5 GB must be uploaded in parts with *multipart upload*; boto3's `upload_file` does this automatically.)

### 2. Sub-service: S3 Glacier

- S3 Glacier is for **data that is not needed often or soon**, such as old backups and archives.
- It costs much less to store than normal S3, but getting the data back is slower and can cost extra.
- It comes as storage classes:

| Class | Retrieval | Use for |
|-------|-----------|---------|
| S3 Glacier Instant Retrieval | milliseconds | rarely used data you still need quickly |
| S3 Glacier Flexible Retrieval | minutes to hours | archives |
| S3 Glacier Deep Archive | hours | long-term archive, cheapest |

- Normal S3 storage (S3 Standard) is for data you use often.

### 3. Versioning

- Versioning lets you keep the **same file name with different versions**.
- It is a bucket-level setting and is **off by default**. Once turned on it can only be suspended, not removed.
- Uploading the same key again creates a new version with a new version ID instead of overwriting the old one. You can get back an older version.
- Deleting a versioned object adds a *delete marker*; the old versions are still stored (and still cost money).

### 4. Pre-signed URL

- A pre-signed URL is a **temporary link to a private object**. Anyone with the link can access the object until it expires, without needing AWS credentials.
- The link carries the permissions of the user who created it, so that user must be allowed to read the object.
- You set the lifetime in seconds (`ExpiresIn`). 5 minutes = `300`. With IAM user keys the maximum is 7 days.

```python
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": "my-bucket", "Key": "file1.txt"},
    ExpiresIn=300,
)
```

### 5. Static website hosting

- S3 can host a **static website** (HTML, CSS, JavaScript, images; no server-side code).
- Turn it on in the bucket properties and set an index document (for example `index.html`).
- The site must be publicly readable (Block Public Access off and a bucket policy that allows reads). For HTTPS or better speed, put CloudFront in front.

## Task 01

**Task:** Create a new bucket of your choice and upload a text file created by you. Then upload 3 more text files with different names. List all the objects in the bucket. Create a URL of the first file so a friend can download it only within the next 5 minutes. Download the object and delete it after.

**Steps**

1. Create the bucket (a unique name; use the `LocationConstraint` outside `us-east-1`).
2. Create 4 text files with different names and upload them.
3. List the objects in the bucket.
4. Create a pre-signed URL for the first file with `ExpiresIn=300`.
5. Download the first file, then delete it from the bucket.

**Reference solution (boto3)**

```python
import boto3

BUCKET_NAME = "my-unique-bucket-name-12345"  # change this
REGION = "ap-south-1"
FILES = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

s3 = boto3.client("s3", region_name=REGION)

# 1. create the bucket
s3.create_bucket(
    Bucket=BUCKET_NAME,
    CreateBucketConfiguration={"LocationConstraint": REGION},
)

# 2. create and upload four text files
for name in FILES:
    with open(name, "w") as f:
        f.write(f"This is {name}\n")
    s3.upload_file(name, BUCKET_NAME, name)

# 3. list all objects in the bucket
response = s3.list_objects_v2(Bucket=BUCKET_NAME)
for obj in response.get("Contents", []):
    print(obj["Key"], obj["Size"])

# 4. pre-signed URL for the first file, valid for 5 minutes
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": BUCKET_NAME, "Key": FILES[0]},
    ExpiresIn=300,
)
print(url)

# 5. download the first file, then delete it from the bucket
s3.download_file(BUCKET_NAME, FILES[0], "downloaded_" + FILES[0])
s3.delete_object(Bucket=BUCKET_NAME, Key=FILES[0])
```

This reference version was checked against a mocked S3 (not the real AWS). My own solution is in [`aws/s3/`](../aws/s3/).

**Things to remember**

- `list_objects_v2` returns at most 1000 objects per call; use a paginator for more.
- After the 5 minutes the pre-signed URL stops working (`AccessDenied`).
- `delete_object` on a bucket with versioning turned on adds a delete marker instead of removing the data.
- Delete the bucket and test objects when you are done, so you are not charged for them.

## Scripts written

- [`aws/s3/`](../aws/s3/): my Task 01 solution (edit: add the file name here)

## Handwritten notes

- [page-01.jpg](handwritten/day-06/page-01.jpg): benefits of S3, Glacier, versioning, pre-signed URL, static website hosting
- [page-02.jpg](handwritten/day-06/page-02.jpg): Task 01

## Doubts / to revise

- Difference between S3 Standard and the Glacier storage classes, and when to use each.
- What happens to old versions when versioning is on and you delete an object.
- How to make a bucket public for static website hosting, and why it is risky.
- Pre-signed URL: what happens if the signing user's permissions change before the link expires.
