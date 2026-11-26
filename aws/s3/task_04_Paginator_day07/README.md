# Task 04: Upload 25 generated files and list them with a paginator

Day 7 (2026-11-25)

## Task

1. Create a new bucket.
2. Generate 25 text files dynamically.
3. Upload all of them to the S3 bucket using boto3 code.
4. Use a paginator to list all the objects in the terminal.
5. For each object, print the file name, file size and last modified time.
6. Count the total number of objects uploaded.

## Files

- `<script name>.py`: my solution (edit: add the file name)

## Requirements

- Python 3 and `boto3` (`pip install -r requirements.txt` from the repo root).
- AWS credentials configured locally (`aws configure` or `.env`). Never commit keys.
- Change the bucket name in the script to a globally unique one.

## How to run

```bash
python <script name>.py
```

## Expected output

- One line per object with its name, size in bytes and last modified time (25 lines).
- A final line with the total count: **25**.

## Concepts

- **Paginator:** one `list_objects_v2` call returns at most 1000 objects. A paginator keeps asking for the next page using the continuation token, so you get every object.
- Each page holds its objects under `Contents`; an empty bucket has no `Contents`.
- With 25 files you get a single page. To see several pages, use a small page size in the pagination settings.

## Notes

- Delete the test files and the bucket afterwards so you are not charged.
