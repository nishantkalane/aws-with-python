# Task 02: Pre-signed URL (5-minute download link)

Day 6 (2026-11-24)

## Task

Create a URL for the first file in the bucket so a friend can download the file only within the next 5 minutes. Then download the object and delete it afterwards.

## Files

- `<script name>.py`: my solution (edit: add the file name)

## Requirements

- Python 3 and `boto3`.
- AWS credentials configured locally. Never commit keys.
- A bucket with at least one uploaded text file (from Task 01).

## How to run

```bash
python <script name>.py
```

## Steps

1. Create a pre-signed URL for the first file, valid for 5 minutes (300 seconds).
2. Print the URL.
3. Open it in a browser or send it to a friend and check that the file downloads.
4. Download the object with boto3.
5. Delete the object from the bucket.

## How to test

- Open the URL straight away: the file should download.
- Open it again after 5 minutes: it should fail with `AccessDenied` (request has expired).
- After step 5, list the bucket and check that the object is gone.

## Concepts

- A **pre-signed URL** gives temporary access to a **private** object, without making the bucket or object public.
- The lifetime is set with `ExpiresIn` in seconds. 5 minutes = 300. With IAM user keys the maximum is 7 days.
- The URL carries the permissions of the user who created it, so that user must be allowed to read the object.
- Anyone who has the link can use it until it expires.

## Notes

- Do not post the URL publicly. It contains your access key ID and a signature.
- If versioning is on, deleting adds a delete marker and the old version is still stored.
- Delete the test objects and the bucket when you are done.
