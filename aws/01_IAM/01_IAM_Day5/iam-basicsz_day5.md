# IAM Basics

IAM = **Identity and Access Management**.

## What is IAM?

IAM is the AWS service that controls **who** can use your AWS account and **what** they are allowed to do.

- **Who** = users, groups, roles (identities)
- **What** = permissions, written as policies

IAM is global. It is not tied to one region, and it is free.

## Key terms

| Term | Meaning |
|------|---------|
| Root user | The account owner (the email used to sign up). Has full access. Use it only for setup. |
| IAM user | A person or application with its own sign-in or access keys. |
| Group | A collection of users. Attach a policy to the group and every user in it gets it. |
| Policy | A JSON document that says what is allowed or denied. |
| Role | An identity for AWS services or temporary access. It has no password or keys. |
| Access key | Access key ID + secret access key. Used by code (boto3) and the CLI. |

## Why not use the root user?

The root user can do everything, including closing the account. If its keys leak, the whole account is at risk. So create an IAM user for daily work and keep root locked away (with MFA).

## How to create an IAM user (console)

1. Sign in to the AWS console and open **IAM**.
2. Click **Users** > **Create user**.
3. Enter a user name (for example `python-user`).
4. Tick **Provide user access to the AWS Management Console** if the user needs to sign in to the console, and set a password.
5. Click **Next** to go to the permissions step.
6. Choose **Attach policies directly** (or add the user to a group).
7. Search for the policy you need, for example `AmazonS3FullAccess`, and tick it.
8. Click **Next**, then **Create user**.

## How to create access keys (for Python / CLI)

1. IAM > **Users** > click your user.
2. Open the **Security credentials** tab.
3. Under **Access keys**, click **Create access key**.
4. Choose the use case (for example **Command Line Interface** or **Local code**).
5. Click **Create**, then **download the `.csv` file**. The secret key is shown only once.

Then configure it on your computer:

```bash
aws configure
```

It asks for: Access key ID, Secret access key, default region (for example `ap-south-1`), output format.

## Permissions and policies

A policy has four main parts:

| Part | Meaning | Example |
|------|---------|---------|
| Effect | Allow or Deny | `Allow` |
| Action | What can be done | `s3:ListBucket` |
| Resource | On what | `arn:aws:s3:::my-bucket` |
| Condition | Optional extra rule | only from a certain IP |

A simple policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket", "s3:GetObject"],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ]
    }
  ]
}
```

Types of policies:

- **AWS managed**: ready-made by AWS (for example `AmazonS3FullAccess`). Good for learning.
- **Customer managed**: written by you, for exact permissions.
- **Inline**: attached to one user only.

By default a new user has **no permissions**. An explicit **Deny** always beats an Allow.

## Best practices

- Never use root for daily work. Turn on MFA for root.
- Give **least privilege**: only the permissions needed.
- Use groups instead of attaching policies to each user.
- Never put access keys in code or on GitHub. Use `aws configure` or environment variables. Boto3 does not load a `.env` file automatically.
- Rotate or delete keys you do not use.

## Quick summary

- IAM decides who can do what in AWS.
- Create a user, give it a policy, create access keys, use them in Python.
- Start with least privilege and keep keys secret.
