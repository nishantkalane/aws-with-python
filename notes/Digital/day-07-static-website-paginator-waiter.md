# Day 7: Static website hosting, paginator and waiter

Date: 2026-11-25

## Done in class

1. Learnt how to host a **static website on S3** (bucket properties and bucket policy).
2. Learnt what a **paginator** is.
3. Learnt what a **waiter** is.
4. Tasks 03, 04 and 05 (below).

## 1. Hosting a static website on S3

A static website is made of fixed files (HTML, CSS, JavaScript, images). S3 can serve them directly, with no server.

**What to set up**

- **Properties tab -> Static website hosting:** enable it and set the **index document** (`index.html`). An error document (for example `error.html`) is optional.
- **Permissions tab -> Block Public Access:** turn it off for this bucket, otherwise nobody outside your account can open the site.
- **Bucket policy:** allow the public to read the objects. The policy needs `Effect: Allow`, `Principal: *`, `Action: s3:GetObject` and `Resource: arn:aws:s3:::<bucket-name>/*`.
- Upload `index.html` (and any other files) to the bucket.
- Open the **website endpoint** shown at the bottom of the Static website hosting section.

**Things to remember**

- Without the public-read policy the site shows 403 Forbidden.
- The S3 website endpoint is **HTTP only**. For HTTPS or a custom domain, put CloudFront in front.
- S3 serves static files only. No Python, PHP or database code runs there.
- Use a **separate bucket** for the website. Public access applies to everything the policy covers.
- A resume has personal details (phone, email). Once the site is public, anyone can read it, so share only what you are happy to be public.
- Delete the bucket when you no longer need it.

## 2. Paginator (divide, spread and retrieve)

- Many AWS list calls return only a **limited number of results per call**. For S3 `list_objects_v2`, the maximum is **1000 objects** per response.
- If a bucket has more, the response says it is truncated and gives a **continuation token** to fetch the next part.
- A **paginator** does this for you. It calls the API again and again, passing the token each time, and gives you the results **page by page** until everything is retrieved.
- **Example:** a bucket has 2500 objects. The paginator returns 3 pages: 1000, 1000 and 500 objects. You loop over the pages and the objects in each page, without handling the token yourself.
- Why use it: without it you would only see the first 1000 objects and think the bucket is smaller than it is.
- In boto3: `client.get_paginator("list_objects_v2")`, then `paginate(Bucket=...)`. Each page has its objects under `Contents`, and a page for an empty bucket has no `Contents` key.

## 3. Waiter

- A **waiter** makes your code **pause until a resource reaches a certain state**, by checking again and again at fixed intervals.
- It is useful because AWS actions are not always instant. For example, you should not upload to a bucket before it exists.
- S3 waiters in boto3: `bucket_exists`, `bucket_not_exists`, `object_exists`, `object_not_exists`.
- Use it with `client.get_waiter("bucket_exists")` and then `wait(Bucket=...)`.
- It checks about every 5 seconds and gives up after about 20 attempts. If the state is never reached, it raises a `WaiterError`.

## Tasks

**Task 03:** Create a static website of my resume as an `index.html` file and host it on AWS S3. Work through the steps one at a time, finishing each step before the next.

**Task 04**

1. Create a new bucket.
2. Generate 25 text files dynamically.
3. Upload all of them to the S3 bucket using boto3 code.
4. Use a paginator to list all the objects in the terminal.
5. For each object, print the file name, file size and last modified time.
6. Count the total number of objects uploaded.

**Task 05**

- Find duplicate files inside the bucket: files with exactly the same content but different file names.
- The program should download the objects temporarily, compare their contents and print the duplicates.
- Create 25 files (or use the past ones), upload and compare them, then print which files have the same contents.

## Scripts written

- [Task 03 static website files](../../aws/02_S3/02_S3_Day5-Day7/task_03_Static_Website_day07/)
- [Task 04 paginator scripts](../../aws/02_S3/02_S3_Day5-Day7/task_04_Paginator_day07/)
- [Task 05 duplicate-file scripts](../../aws/02_S3/02_S3_Day5-Day7/task_05_DuplicateFiles_day07/)

## Handwritten notes

- [Day 7 handwritten notes](../handwritten/Day-wise/day-07/S3-Static-Website-Paginator-task-duplicate-files-task.pdf)

## Doubts / to revise

- Exact steps and order for enabling a public static website (Block Public Access, bucket policy, endpoint).
- Why the S3 website endpoint is HTTP and how CloudFront adds HTTPS.
- Difference between a paginator and a plain `list_objects_v2` call.
- When to use a waiter, and what the default wait time is.
- My page has a class analogy for the waiter (something about removing benches one by one while waiting). Rewrite it in my own words here.
- Task 05: ways to compare file contents without downloading them (hashing).
