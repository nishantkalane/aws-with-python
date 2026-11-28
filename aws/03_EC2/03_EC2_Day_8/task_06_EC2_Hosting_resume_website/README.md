# AWS EC2 Static Resume Website Deployment

> Real addresses are replaced by placeholders such as `<EC2_PUBLIC_IP>` and `<EC2_PUBLIC_DNS>`. Never commit the `.pem` key file.

## 1. Project Overview

This project demonstrates how to deploy and host a static personal resume website on an AWS EC2 instance using Ubuntu Linux and the Nginx web server.

The website contains:

- `index.html`: Main resume website.
- `error.html`: Custom error page.
- `Nishant_Kalane_Resume.pdf`: Downloadable resume.

The website files are stored on an EC2 instance and served to visitors through Nginx.

## 2. Technologies Used

| Technology          | Purpose                    |
| ------------------- | -------------------------- |
| AWS EC2             | Cloud-based virtual server |
| Ubuntu              | Operating system           |
| Nginx               | Web server                 |
| HTML                | Website structure          |
| SSH                 | Remote server access       |
| SCP                 | File transfer              |
| AWS Security Groups | Network access control     |

## 3. Project Architecture

```
                  USER
                    |
                    |
              Web Browser
                    |
                    | HTTP (Port 80)
                    |
             AWS EC2 Instance
             Public IP: <EC2_PUBLIC_IP>
                    |
                  Ubuntu
                    |
                  Nginx
                    |
             /var/www/resume/
                    |
          +---------+----------+
          |         |          |
       index.html error.html  Resume.pdf
```

## 4. EC2 Instance Information

| Property         | Value                 |
| ---------------- | --------------------- |
| Cloud Provider   | AWS                   |
| Service          | EC2                   |
| Operating System | Ubuntu 26.04.1 LTS    |
| Architecture     | x86_64                |
| Login Username   | ubuntu                |
| Public IPv4      | <EC2_PUBLIC_IP>        |
| Private IPv4     | <EC2_PRIVATE_IP>      |
| Region           | Asia Pacific (Sydney) |
| Web Server       | Nginx                 |
| Web Root         | /var/www/resume/      |

## 5. Project Files

The project directory:

```
aws-with-python/
└── aws/
    └── 03_EC2/
        └── 03_EC2_Day_8/
            └── task_06_EC2_Hosting_resume_website/
                ├── index.html
                ├── error.html
                └── Nishant_Kalane_Resume.pdf
```

The destination directory on EC2:

```
/var/www/resume/
├── index.html
├── error.html
└── Nishant_Kalane_Resume.pdf
```

## 6. Deployment Process

### Step 1: Launch EC2

Launch an EC2 instance using Ubuntu.

Obtain the following:

- Public IPv4 address
- Public DNS
- Private key (.pem)
- Security Group

### Step 2: Configure Security Group

Configure the inbound rules:

| Type | Protocol | Port | Source            |
| ---- | -------- | ---- | ----------------- |
| SSH  | TCP      | 22   | Your public IP/32 |
| HTTP | TCP      | 80   | 0.0.0.0/0         |

SSH provides remote terminal access.

HTTP allows visitors to access the website.

### Step 3: Connect to EC2

From Windows CMD or PowerShell:

```
ssh -i "C:\Users\user\my-new-key.pem" ubuntu@<EC2_PUBLIC_DNS>
```

### Step 4: Install Nginx

```
sudo apt update
sudo apt install nginx -y
```

Check the service:

```
sudo systemctl status nginx
```

### Step 5: Create Website Directory

```
sudo mkdir -p /var/www/resume
sudo chown -R ubuntu:ubuntu /var/www/resume
```

### Step 6: Upload Website Files

From PowerShell, change to this project directory and run SCP (replace the key path and public DNS):

```
scp -i "C:\path\to\my-key.pem" .\index.html .\error.html .\Nishant_Kalane_Resume.pdf ubuntu@<EC2_PUBLIC_DNS>:/var/www/resume/
```

Verify the files:

```
ls -lh /var/www/resume/
```

### Step 7: Configure Nginx

Open the default configuration:

```
sudo nano /etc/nginx/sites-available/default
```

Change the document root:

```
root /var/www/resume;
```

Save the file.

### Step 8: Test Nginx Configuration

```
sudo nginx -t
```

Expected result:

```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

### Step 9: Reload Nginx

```
sudo systemctl reload nginx
```

### Step 10: Access the Website

Open:

http://<EC2_PUBLIC_IP>

The website should now be accessible through the EC2 public IP.

## 7. Verification Commands

Check Nginx:

```
sudo systemctl status nginx
```

Check uploaded files:

```
ls -lh /var/www/resume/
```

Check HTTP locally:

```
curl -I http://localhost
```

Check listening ports:

```
sudo ss -tlnp | grep ':80'
```

Check Ubuntu firewall:

```
sudo ufw status
```

Check EC2 public IP:

```
curl -4 https://checkip.amazonaws.com
```

From Windows PowerShell, test port 80:

```
Test-NetConnection <EC2_PUBLIC_IP> -Port 80
```

Test the HTTP response:

```
curl.exe -I http://<EC2_PUBLIC_IP>
```

## 8. Troubleshooting

### Problem 1: SSH Connection Timed Out

Cause: The public IP address of the local computer changed, but the SSH Security Group rule still contained the old IP.

Solution:

Check the current public IP:

```
(Invoke-RestMethod -Uri "https://checkip.amazonaws.com").Trim()
```

Update the SSH inbound rule to:

```
YOUR_CURRENT_PUBLIC_IP/32
```

### Problem 2: Website Connection Timed Out

Checks performed:

1. EC2 instance was running.
2. HTTP inbound rule allowed port 80.
3. Nginx was active.
4. Nginx listened on 0.0.0.0:80.
5. Ubuntu UFW was inactive.
6. Windows could connect to port 80.

The final HTTP test returned:

```
HTTP/1.1 200 OK
Server: nginx/1.28.3 (Ubuntu)
```

This confirmed that the website was responding successfully over HTTP.

### Problem 3: HTTPS vs HTTP

The deployment was configured for HTTP.

Correct URL:

```
http://<EC2_PUBLIC_IP>
```

HTTPS was not configured in this project.

## 9. Important Learning Outcomes

- Understanding AWS EC2 and virtual machines.
- Connecting to a remote Ubuntu server using SSH.
- Understanding PEM private keys.
- Configuring Security Groups.
- Understanding public and private IP addresses.
- Installing and managing Nginx.
- Transferring files using SCP.
- Configuring Nginx document roots.
- Deploying a static website.
- Testing HTTP connectivity.
- Troubleshooting network and server issues.

## 10. Future Improvements

- Configure HTTPS using a domain name and SSL certificate.
- Complete custom 404 error page configuration.
- Configure a custom domain.
- Explore CloudFront for content delivery.
- Add monitoring using Amazon CloudWatch.
- Automate deployment using Python and Boto3.

## 11. Cost Considerations

EC2 resources may incur charges while running, depending on the instance type, usage, and AWS pricing.

Remember to check the instance state and AWS Billing dashboard when the project is not in use.

---

**Project:** AWS EC2 Static Resume Website\
**Web Server:** Nginx\
**Deployment Method:** SSH + SCP\
**Status:** HTTP deployment verified successfully.
