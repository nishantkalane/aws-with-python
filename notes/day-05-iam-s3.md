# Day 5: AWS, IAM, S3 and first boto3 script

Date: 2026-11-23

## Done in class

1. Created a free AWS account.
2. Learnt what **IAM** is: permissions, policies and groups.
3. Created an **IAM user**, generated an **access key and secret key** for it, and gave the user permissions.
4. Learnt what **S3** is.
5. Created an S3 **bucket manually** in the console and uploaded files to it.
6. Opened Python and **configured the IAM user** so code can use it.
7. Tried to **create a bucket using boto3**.

## 1. What is AWS?

- **Amazon Web Services (AWS)** is a cloud platform. Instead of buying and running your own servers, you rent computing, storage, databases and networking over the internet and pay for what you use.
- Services are grouped by job: compute (EC2, Lambda), storage (S3), databases (RDS, DynamoDB), networking (VPC), security (IAM) and more.
- **Region** = a geographic area with AWS data centres, for example `ap-south-1` (Mumbai). **Availability Zone** = one or more data centres inside a region. Pick the region closest to you and use it consistently.
- A **free tier** account has limited free usage. Check the Billing page regularly and delete resources you no longer need.
- You use AWS in three ways: the web console (clicking), the AWS CLI (commands) and SDKs such as **boto3** (Python code).

## 2. IAM (Identity and Access Management)

IAM controls **who** can do **what** in your AWS account. It is global (not tied to one region).

| Term | Meaning |
|------|---------|
| Root user | The email you signed up with. It can do everything. Do not use it for daily work. |
| IAM user | An identity for one person or one application, with its own credentials. |
| Group | A collection of users. Attach permissions to the group once and every member gets them. |
| Permission | Permission to perform one action, for example read an S3 object. |
| Policy | A JSON document that lists the permissions (allow or deny). Attached to a user or group. |
| Access key ID + secret access key | Credentials for programs (CLI, boto3). The secret key is shown **only once** when you create it. |

A policy has three main parts: **Effect** (Allow or Deny), **Action** (what), **Resource** (on what).

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket", "s3:GetObject"],
      "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"]
    }
  ]
}
```

**Principle of least privilege:** give a user only the permissions it needs, nothing more.

### What I did

1. Opened IAM and created a new user.
2. Created an access key for the user and saved the key ID and secret key somewhere safe (outside Git).
3. Attached permissions (an S3 policy) to the user, directly or through a group.

## 3. S3 (Simple Storage Service)

S3 is **object storage**: you store files (objects) inside containers (buckets) and access them over the internet.

- **Bucket**: the container. The name must be **globally unique** across all AWS accounts, lowercase, 3 to 63 characters, no underscores. A bucket lives in one region.
- **Object**: a file plus its metadata. Its **key** is its name or path inside the bucket, for example `photos/2026/cat.jpg`.
- S3 has no real folders; slashes in the key just look like folders in the console.
- Typical uses: backups, website files, images and videos, data for analytics.
- New buckets are private by default. Do not make a bucket public unless you really need to.
- Related features to explore later: versioning, storage classes, lifecycle rules, bucket policies.

### What I did

1. Created a bucket manually in the console (chose a unique name and the region).
2. Uploaded files into the bucket and checked that they appeared.

## 4. Using AWS from Python with boto3

**boto3** is the AWS SDK for Python. It uses the credentials of the IAM user.

```bash
pip install boto3 python-dotenv
aws configure        # asks for access key ID, secret key, region, output format
```

Credentials can also come from environment variables or a local `.env` file (see `.env.example`). **Never hard-code keys in a script and never push them to GitHub.**

```python
import boto3

s3 = boto3.client("s3", region_name="ap-south-1")

# Outside us-east-1 you must pass the region as LocationConstraint
s3.create_bucket(
    Bucket="my-unique-bucket-name-12345",
    CreateBucketConfiguration={"LocationConstraint": "ap-south-1"},
)
```

Common reasons `create_bucket` fails:

- `BucketAlreadyExists`: the name is taken by someone else, so choose a more unique name.
- `BucketAlreadyOwnedByYou`: you already created a bucket with this name.
- `IllegalLocationConstraintException`: the region in the client and the `LocationConstraint` do not match, or the constraint is missing outside `us-east-1`.
- `AccessDenied`: the IAM user does not have an S3 permission such as `s3:CreateBucket`.
- `InvalidAccessKeyId` or `SignatureDoesNotMatch`: wrong or mistyped credentials.

(Edit: write here what happened when you ran it in class and how you configured the user.)

## Scripts

See [`aws/s3/`](../aws/s3/):

- [`create_bucket.py`](../aws/s3/create_bucket.py): create a bucket
- [`list_buckets.py`](../aws/s3/list_buckets.py): list buckets
- [`upload_file.py`](../aws/s3/upload_file.py): upload a file

IAM summary: [`aws/iam/README.md`](../aws/iam/README.md)

## Handwritten notes

- [handwritten/day-05/](handwritten/day-05/)

## Doubts / to revise

- Difference between an IAM user, group, role and policy (roles will come later).
- Why the secret key can be seen only once, and what to do if it is lost (create a new key).
- Why bucket names must be globally unique.
- What the region setting changes for S3.
