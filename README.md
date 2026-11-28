# AWS with Python

Coursework for AWS with Python: Python practice, AWS hands-on exercises, and class notes.

## Repository contents

| Area | Contents |
|---|---|
| [Python practice](python-practice/python_practice_day1-day4/) | 10 programs, 50 code snippets, and viva questions |
| [AWS exercises](aws/) | Intro and IAM notes, S3 exercises, and EC2 projects |
| [Class notes](notes/) | Digital notes and handwritten scans, organised by day and topic |

### AWS exercises

- [Introduction](aws/00_Intro/00_Intro_Day5/aws-introduction_day5.md)
- [IAM](aws/01_IAM/01_IAM_Day5/iam-basicsz_day5.md)
- [S3 tasks](aws/02_S3/02_S3_Day5-Day7/)
- [EC2 Day 8: resume website](aws/03_EC2/03_EC2_Day_8/task_06_EC2_Hosting_resume_website/)
- [EC2 Day 9: instance console](aws/03_EC2/03_EC2_Day_9/)

### Python practice

- [Programs](python-practice/python_practice_day1-day4/programs/)
- [Code snippets](python-practice/python_practice_day1-day4/code-snippets/)
- [Viva questions](python-practice/python_practice_day1-day4/viva-questions/)

## Progress

| Area | Total | Done |
|---|---:|---:|
| Programs | 10 | 10 |
| Code snippets | 50 | 50 |
| Viva questions | 40 | 40 |

## Setup

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Install dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

For AWS scripts, configure credentials using the AWS CLI:

```bash
aws configure
```

The scripts use boto3's default credential chain. A `.env` file is not loaded automatically; scripts that need one must explicitly load it. Never put real credentials in source control.

## Before running AWS exercises

- Review and change the bucket names, region, AMI ID, and key-pair name in each exercise as needed.
- AWS resource operations can incur charges. Stop or terminate resources and remove test data when finished.
- The EC2 console exercise can create, stop, start, or terminate instances. Check the selected instance carefully before using its management options.
- Never commit AWS keys or private `.pem` files. If a key is exposed, revoke it and create a replacement.
