# Task 03: Host my resume as a static website on S3

Day 7 (2026-11-25)

## Task

Create a static website of my resume as an `index.html` file and host it on AWS S3.

## Files

- `index.html`: website home page.
- `error.html`: custom error page.
- `Nishant_Kalane_Resume.pdf`: downloadable resume.

## Steps

1. Build the resume as a single `index.html`.
2. Create a bucket for the website (a separate bucket, with a globally unique name).
3. Upload `index.html` to the bucket.
4. Properties tab -> **Static website hosting**: enable it and set the index document to `index.html`.
5. Permissions tab -> **Block Public Access**: turn it off for this bucket.
6. Add a **bucket policy** that allows public `s3:GetObject` on `arn:aws:s3:::<bucket-name>/*`.
7. Open the **website endpoint** from the Static website hosting section and check the page loads.

## Result

The website endpoint is not recorded in this repository.

## Notes

- A 403 Forbidden error means Block Public Access is still on or the bucket policy is missing or wrong.
- The S3 website endpoint is HTTP only. HTTPS needs CloudFront.
- The page is public, so keep personal details such as phone number and address out unless you want them visible.
- Delete the bucket or make it private again when you no longer need the site.
