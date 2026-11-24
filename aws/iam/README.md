# IAM (Identity and Access Management)

- **User**: an identity for a person or application, with its own credentials.
- **Group**: a collection of users; attach permissions once and every member gets them.
- **Policy**: a JSON document that allows or denies actions on resources.
- **Access key / secret key**: credentials a user (or script) uses to call AWS from code or the CLI.

## What I did (Day 5)

1. Created a new IAM user.
2. Generated an access key and secret key for it (stored locally, never in Git).
3. Gave the user permissions (S3 access) so boto3 can work with buckets.

## Rules

- Never commit keys. If one leaks, delete it in IAM and create a new one.
- Give only the permissions that are needed (least privilege).

Full class notes: [`notes/day-05-iam-s3.md`](../../notes/day-05-iam-s3.md)
