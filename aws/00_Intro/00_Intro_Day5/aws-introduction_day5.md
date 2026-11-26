# Introduction to AWS

## What is AWS?

**AWS (Amazon Web Services)** is Amazon's cloud platform. Instead of buying and running your own servers, you rent computing, storage and other services over the internet and pay for what you use.

## What is cloud computing?

Cloud computing means using computers, storage and software that live in someone else's data centre, through the internet, on demand.

| Own servers (on-premises) | Cloud (AWS) |
|---------------------------|-------------|
| Buy hardware up front | Pay as you go |
| Slow to set up | Ready in minutes |
| You maintain everything | AWS maintains the hardware |
| Hard to scale | Scale up or down easily |

## Why use AWS?

- **Pay as you go**: no big upfront cost.
- **Scalable**: grow or shrink as needed.
- **Global**: data centres around the world.
- **Reliable**: built for high availability.
- **Secure**: strong security tools, shared responsibility.
- **Many services**: 200+ services.

## Global infrastructure

- **Region**: a geographic area, for example Mumbai (`ap-south-1`).
- **Availability Zone (AZ)**: one or more data centres inside a region. Each region has several AZs.
- **Edge locations**: used by CloudFront to deliver content closer to users.

Pick the region nearest to you or your users. Resources are created in one region (IAM is global).

## Common services

| Category | Service | Use |
|----------|---------|-----|
| Compute | EC2 | Virtual servers |
| Storage | S3 | Store files (objects) in buckets |
| Security | IAM | Users, permissions, policies |
| Database | RDS, DynamoDB | Managed databases |
| Networking | VPC | Your private network in AWS |
| Serverless | Lambda | Run code without managing servers |

## Ways to use AWS

1. **Management Console**: the web interface.
2. **AWS CLI**: commands in the terminal.
3. **SDK**: use AWS from code. For Python it is **boto3**.

## Getting started

1. Create an AWS account (needs an email, card and phone).
2. Secure the root user with MFA.
3. Create an IAM user for daily work (see `iam-basics.md`).
4. Create access keys and configure them with `aws configure`.
5. Try S3: make a bucket and upload a file, first in the console, then with boto3.

## Free tier and cost

AWS has a free tier for new accounts with limits on many services. Set a **billing alarm / budget** and delete resources you are not using, so you are not charged by mistake.

## Shared responsibility

- **AWS** is responsible for the security **of** the cloud (hardware, data centres).
- **You** are responsible for security **in** the cloud (your data, users, permissions, keys).

## Quick summary

- AWS = rent computing and storage from Amazon, pay for what you use.
- Regions and Availability Zones make it global and reliable.
- Main early services: IAM, S3, EC2.
- Use the console, CLI or boto3.
