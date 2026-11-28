# Task 01: Create an S3 bucket

Day 5 (2026-11-23) and Day 6 (2026-11-24)

## Task

1. Create a new bucket of your choice (first with the console, then with boto3).
2. Upload a text file created by you.
3. Upload 3 more text files with different names.
4. List all the objects in the bucket.

## Files

- [`create_s3_bucket.py`](create_s3_bucket.py): creates the bucket. It does not upload files or list objects.
- The upload, listing and pre-signed URL scripts are in [Task 02](../task_02_Pre-Signed-URL-day06/).

## Requirements

- Python 3 and `boto3` (`pip install -r requirements.txt` from the repo root).
- AWS credentials configured locally with `aws configure`. Never commit keys.
- A globally unique bucket name.

## How to run

```bash
python create_s3_bucket.py
```

The bucket name is set in the script and may need to be changed to a globally unique name before running.

## Task objective

The class exercise also included uploading four text files and listing the objects. Those steps are not implemented by `create_s3_bucket.py`; use the Task 02 scripts for the related upload and listing practice.

## Concepts

- Bucket names are **globally unique**: lowercase, 3 to 63 characters, no underscores.
- Outside `us-east-1`, `create_bucket` needs the region as a `LocationConstraint` (for example `ap-south-1`).
- Object key = the file name inside the bucket. Uploading the same key again replaces the object (unless versioning is on).
- One `list_objects_v2` call returns at most 1000 objects. For more, use a paginator (see Task 04).

## Common errors

| Error | Meaning |
|-------|---------|
| `BucketAlreadyExists` | Someone else already uses that name. Choose another. |
| `BucketAlreadyOwnedByYou` | You already created this bucket. |
| `IllegalLocationConstraintException` | The region and the `LocationConstraint` do not match. |
| `AccessDenied` | The IAM user lacks the S3 permission. |
| `InvalidAccessKeyId` / `SignatureDoesNotMatch` | Wrong or mistyped credentials. |

## Notes

- Delete the test files and the bucket when you are done, so you are not charged.
