# Task 05: Find duplicate files in an S3 bucket

Day 7 (2026-11-25)

## Task

Find duplicate files inside a bucket: files with exactly the same content but different file names. The program should download the objects temporarily, compare their contents and print the duplicates.

Create 25 files (or use the past ones), upload them, compare them, and print which files have the same contents.

## Files

- `generate_files.py`: prepare files including duplicates.
- `upload_files.py`: upload the files.
- `find_duplicates.py`: download text objects temporarily and group matching contents.

## Requirements

- Python 3 and `boto3`.
- AWS credentials configured locally. Never commit keys.
- A bucket that holds the files (use the one from Task 04 or create a new one).

## Approach

1. List all objects in the bucket (with a paginator, so none are missed).
2. Download each object to a temporary location.
3. Work out a fingerprint of the content for each file (for example a hash such as SHA-256).
4. Group file names by fingerprint.
5. Print every group that has more than one file name.
6. Delete the temporary downloads.

## How to test

- Make sure the 25 files include a few that share the same content but have different names, for example `file_03.txt` and `file_17.txt` with the same text.
- Include at least one file that is unique, and ideally one empty file.

## Expected output

- A list of groups of duplicate file names, for example: `file_03.txt, file_17.txt`.
- A clear message when no duplicates are found.

## Notes

- Compare the **content**, not the names or sizes. Two files can have the same size and different content.
- Comparing hashes is better than comparing whole files against each other, because it needs one pass over each file.
- Temporary files must be cleaned up even if the program stops with an error.
- Without downloading, the ETag of an object is an MD5 hash for simple uploads, but not for multipart or encrypted uploads, so downloading is the safe method.
