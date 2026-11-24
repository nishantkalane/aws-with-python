# AWS with Python

Course work for **AWS with Python**, offered by SDLC Pune and Capgemini.

This repo holds my Python practice (programs, code snippets, viva questions), my AWS hands-on work with `boto3`, and my class notes (digital and handwritten).

## Repository structure

```
aws-with-python/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── python-practice/               # fixed course resources, organised by type
│   ├── programs/                  # 10 programs
│   ├── code-snippets/             # 50 code snippets
│   └── viva-questions/            # 40 viva questions + answers
│       └── handwritten/           # photos/scans of handwritten viva notes
├── aws/                           # hands-on AWS code, organised by service
│   ├── iam/                       # IAM notes (users, groups, policies)
│   └── s3/                        # boto3 scripts for S3
└── notes/                         # organised by day
    ├── _template.md               # copy this for each new day
    ├── day-05-iam-s3.md
    └── handwritten/               # day-05/, day-06/, ... photos or PDFs
```

## Progress

| Area | Total | Done |
|------|-------|------|
| Programs | 10 | 10 |
| Code snippets | 50 | 50 |
| Viva questions (answers written, plus extra Q23.1) | 40 | 40 |

## Day-wise log

| Day | Topic | Notes | Code |
|-----|-------|-------|------|
| 1-4 | Python practice (programs, snippets, viva questions) | | [`python-practice/`](python-practice/) |
| 5 | AWS account, IAM (users, groups, policies, access keys), S3 basics, first `boto3` script | [day-05](notes/day-05-iam-s3.md) | [`aws/s3/`](aws/s3/) |

## Daily routine

1. Copy `notes/_template.md` to `notes/day-XX-topic.md` and fill it in.
2. Save scripts into `aws/<service>/`.
3. Add handwritten notes to `notes/handwritten/day-XX/`.
4. Update the progress table and day-wise log here.
5. Commit, for example `Day 6: EC2 basics`.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Configure AWS credentials locally (never commit them):

```bash
aws configure
```

or copy `.env.example` to `.env` and fill in your values.

## Security note

Access keys and secret keys must **never** be pushed to GitHub. `.gitignore` excludes `.env` and AWS credential files. If a key is ever committed, delete it in IAM immediately and create a new one. Keep handwritten-note photos free of keys and personal details.
