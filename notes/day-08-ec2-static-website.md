# Day 8: Amazon EC2 and static website deployment

Date: 2026-11-26

## Done in class

1. Learnt what **EC2** is and how it differs from S3.
2. Launched an Ubuntu EC2 instance and connected to it with **SSH**.
3. Configured **Security Groups** (SSH and HTTP).
4. Installed **Nginx**, copied the website files with **SCP** and served my resume website.
5. Troubleshot SSH and website connection problems.

Project write-up: [`aws/ec2/ec2-static-resume-website/README.md`](../aws/ec2/ec2-static-resume-website/README.md)

Handwritten notes: [handwritten/day-08/](handwritten/day-08/)

> Real addresses are replaced by placeholders such as `<EC2_PUBLIC_IP>`.

---

## PART 1: What is AWS EC2?

### 1. Understanding EC2

EC2 stands for **Elastic Compute Cloud**.

It is an AWS service that provides virtual servers in the cloud.

Imagine that you want to host a website.

Traditionally, you would need:

- A physical computer.
- An operating system.
- RAM and CPU.
- Storage.
- Internet connectivity.
- A web server.

AWS EC2 allows you to rent a virtual computer from Amazon instead of purchasing and maintaining physical hardware.

You can configure this virtual computer according to your requirements.

For example:

- Choose Ubuntu or Windows.
- Select RAM and CPU.
- Configure storage.
- Install software.
- Run applications.
- Host websites.
- Run Python scripts.

**In simple terms: EC2 is a computer that runs in AWS data centres and that you can access remotely.**

### 2. Why is EC2 called Elastic?

Elastic means that resources can be adjusted according to requirements.

For example:

Suppose your application initially requires:

- 1 CPU.
- 1 GB RAM.

Later, your application grows and needs:

- 4 CPUs.
- 16 GB RAM.

You can change the instance configuration to support increased requirements, subject to AWS instance and configuration options.

EC2 also allows you to launch additional instances.

### 3. Understanding Cloud Computing

Cloud computing means accessing computing resources over the internet instead of managing all the physical infrastructure yourself.

Examples:

| Requirement             | AWS Service |
| ----------------------- | ----------- |
| Virtual computer        | EC2         |
| File and object storage | S3          |
| Relational database     | RDS         |
| Serverless functions    | Lambda      |
| Content delivery        | CloudFront  |
| Monitoring              | CloudWatch  |

### 4. EC2 vs S3

This is an important distinction.

| Feature          | EC2                        | S3                      |
| ---------------- | -------------------------- | ----------------------- |
| Full form        | Elastic Compute Cloud      | Simple Storage Service  |
| Main purpose     | Computing                  | Object storage          |
| What it provides | Virtual server             | Storage bucket          |
| Operating system | Can run Linux or Windows   | No user-managed OS      |
| Applications     | Can run applications       | Stores objects          |
| Website hosting  | Through a web server       | Static website hosting  |
| SSH access       | Supported                  | Not applicable          |
| Example          | Running Python application | Storing images and PDFs |

#### Example

Suppose you have a resume website.

With S3:

- Upload HTML, CSS, JavaScript and PDF files.
- S3 stores the objects.
- Static website hosting can serve the website.

With EC2:

- Launch an Ubuntu server.
- Install Nginx.
- Upload website files.
- Configure Nginx.
- Serve the website through the server.

**Remember: EC2 is primarily a computing service. S3 is primarily a storage service.**

---

## PART 2: Understanding EC2 Components

### 5. What is an EC2 Instance?

An instance is an individual virtual server running on AWS infrastructure.

Think of an instance as one computer.

Our instance had:

| Property         | Value          |
| ---------------- | -------------- |
| Operating system | Ubuntu         |
| Public IP        | <EC2_PUBLIC_IP> |
| Private IP       | 172.31.36.4    |
| Username         | ubuntu         |
| Architecture     | x86_64         |

### 6. What is an Operating System?

An operating system manages the computer's hardware and software resources.

Examples:

- Windows.
- Linux.
- macOS.
- Ubuntu.

We used Ubuntu Linux on our EC2 instance.

Ubuntu allowed us to:

- Install Nginx.
- Create directories.
- Manage files.
- Configure services.
- Execute Linux commands.

### 7. What is a Public IP?

A public IP address allows your EC2 instance to be reached over the internet, subject to network and security configuration.

Our EC2 public IP:

```
<EC2_PUBLIC_IP>
```

We used it to open our website:

```
http://<EC2_PUBLIC_IP>
```

### 8. What is a Private IP?

A private IP is used for communication within private networks, such as an AWS VPC.

Our private IP:

```
172.31.36.4
```

It is not normally directly reachable from the public internet.

#### Public IP vs Private IP

| Public IP                       | Private IP                   |
| ------------------------------- | ---------------------------- |
| Used for internet communication | Used within private networks |
| Publicly routable               | Not publicly routable        |
| Example: <EC2_PUBLIC_IP>         | Example: 172.31.36.4         |

---

## PART 3: Connecting to EC2

### 9. What is SSH?

SSH stands for **Secure Shell**.

SSH is a network protocol that allows you to securely connect to and control a remote computer.

For example, our Windows computer connected to Ubuntu running on EC2.

Command:

```
ssh -i "C:\Users\user\my-new-key.pem" ubuntu@<EC2_PUBLIC_DNS>
```

Understanding the command:

| Component      | Meaning                           |
| -------------- | --------------------------------- |
| ssh            | Connect using Secure Shell        |
| -i             | Specify identity/private key file |
| my-new-key.pem | Private key                       |
| ubuntu         | Remote Linux username             |
| @              | Separates username and host       |
| Public DNS     | Address of the EC2 instance       |

After successful connection, we saw:

```
ubuntu@ip-172-31-36-4:~$
```

This indicated that we were working inside the Ubuntu server.

### 10. What is a PEM File?

PEM stands for Privacy-Enhanced Mail.

In our project, the `.pem` file contained the private key used to authenticate our SSH connection.

Think of it as a digital key to your server.

Important:

- Never share your private key.
- Do not upload it to GitHub.
- Keep it in a secure location.
- Restrict access to the file.

### 11. Understanding the Terminal Prompts

We used two different terminals.

Windows:

```
C:\Users\user>
```

Ubuntu:

```
ubuntu@ip-172-31-36-4:~$
```

These are different environments.

| Windows CMD/PowerShell    | Ubuntu                   |
| ------------------------- | ------------------------ |
| Local computer            | Remote EC2 server        |
| Uses Windows paths        | Uses Linux paths         |
| Runs SSH and SCP commands | Runs Linux commands      |
| Example: C:\Users\user    | Example: /var/www/resume |

This distinction was especially important when transferring files.

---

## PART 4: Security Groups and Ports

### 12. What is an AWS Security Group?

A Security Group acts as a virtual firewall for an EC2 instance.

It controls which inbound and outbound network connections are permitted.

For example, our instance needed:

- SSH access for administration.
- HTTP access for website visitors.

### 13. What is a Port?

A port is a logical communication endpoint used by network services.

Different services commonly use different ports.

Important ports:

| Port | Protocol/Service | Purpose               |
| ---- | ---------------- | --------------------- |
| 22   | SSH              | Remote server access  |
| 80   | HTTP             | Website access        |
| 443  | HTTPS            | Secure website access |
| 3306 | MySQL            | Database connections  |

### 14. Our Security Group Rules

| Type | Port | Source           | Purpose                     |
| ---- | ---- | ---------------- | --------------------------- |
| SSH  | 22   | Our public IP/32 | Connect to Ubuntu           |
| HTTP | 80   | 0.0.0.0/0        | Allow public website access |

Why did we restrict SSH?

Because SSH provides administrative access to the server. Allowing it only from our current public IP reduces unnecessary exposure.

Why did we allow HTTP from 0.0.0.0/0?

Because website visitors can come from different public IP addresses.

### 15. What does /32 mean?

Example:

```
203.0.113.25/32
```

The `/32` CIDR notation represents one specific IPv4 address.

It restricts the rule to that address.

---

## PART 5: Linux and Nginx

### 16. What is Linux?

Linux is an open-source operating system kernel.

Ubuntu is a Linux distribution.

We used Ubuntu as the operating system for our EC2 virtual machine.

Some commands we learned:

```
pwd
```

Displays the current directory.

```
ls
```

Lists files and directories.

```
cd
```

Changes directories.

```
mkdir
```

Creates directories.

```
sudo
```

Runs a command with elevated privileges.

```
nano
```

Opens a terminal-based text editor.

### 17. What is Nginx?

Nginx is a web server.

A web server receives HTTP requests from browsers and returns responses.

In our project:

1. A visitor opens our EC2 public IP.
2. The request reaches Nginx.
3. Nginx looks for the requested website file.
4. Nginx returns the file to the browser.

### 18. Installing Nginx

First, we updated the Ubuntu package information:

```
sudo apt update
```

Then installed Nginx:

```
sudo apt install nginx -y
```

Check its status:

```
sudo systemctl status nginx
```

Expected status:

```
Active: active (running)
```

### 19. What is systemctl?

`systemctl` is a Linux command used to manage system services.

Examples:

Check service status:

```
sudo systemctl status nginx
```

Start Nginx:

```
sudo systemctl start nginx
```

Stop Nginx:

```
sudo systemctl stop nginx
```

Restart Nginx:

```
sudo systemctl restart nginx
```

Reload Nginx:

```
sudo systemctl reload nginx
```

#### Restart vs Reload

- Restart stops and starts the service.
- Reload asks the service to apply updated configuration without a full restart, when supported.

---

## PART 6: Website Deployment

### 20. What is a Web Root or Document Root?

The document root is the directory from which a web server serves website files.

Our website directory:

```
/var/www/resume/
```

It contained:

```
index.html
error.html
Nishant_Kalane_Resume.pdf
```

When someone visited the website, Nginx looked inside this directory for the requested files.

### 21. Creating the Website Directory

```
sudo mkdir -p /var/www/resume
```

Explanation:

- `sudo`: Administrative permission.
- `mkdir`: Create a directory.
- `-p`: Create parent directories if needed.
- `/var/www/resume`: Destination path.

We then changed ownership:

```
sudo chown -R ubuntu:ubuntu /var/www/resume
```

This assigned ownership of the directory and its contents to the Ubuntu user.

### 22. What is SCP?

SCP stands for **Secure Copy Protocol**.

It allows files to be transferred securely between computers using SSH.

We used SCP to transfer files from Windows to EC2.

General structure:

```
scp -i KEY_FILE SOURCE_FILES USERNAME@SERVER:DESTINATION
```

Our destination:

```
ubuntu@<EC2_PUBLIC_DNS>:/var/www/resume/
```

Important distinction:

- SSH gives us remote terminal access.
- SCP transfers files between computers.

Both use SSH-based secure communication.

### 23. Configuring Nginx

We opened:

```
sudo nano /etc/nginx/sites-available/default
```

We changed the document root:

```
root /var/www/resume;
```

This told Nginx to serve website files from our project directory instead of the original default directory.

We saved the configuration and tested it:

```
sudo nginx -t
```

After a successful test, we applied the changes:

```
sudo systemctl reload nginx
```

---

## PART 7: HTTP, HTTPS and Website Testing

### 24. What is HTTP?

HTTP stands for Hypertext Transfer Protocol.

It is used for communication between web browsers and web servers.

Our website was accessible through:

```
http://<EC2_PUBLIC_IP>
```

### 25. What is HTTPS?

HTTPS is HTTP secured using TLS encryption.

It helps protect information exchanged between browsers and servers.

Our EC2 deployment was tested successfully using HTTP.

HTTPS was not configured in this project.

### 26. What is a Firewall?

A firewall controls network traffic based on rules.

We examined two firewall-related layers:

1. AWS Security Groups.
2. Ubuntu UFW firewall.

We checked Ubuntu's firewall using:

```
sudo ufw status
```

Our result:

```
Status: inactive
```

This meant UFW was not actively filtering incoming traffic.

### 27. Understanding HTTP Status Codes

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | OK                    |
| 301         | Moved Permanently     |
| 403         | Forbidden             |
| 404         | Not Found             |
| 500         | Internal Server Error |
| 502         | Bad Gateway           |

Our website returned:

```
HTTP/1.1 200 OK
```

This indicated that the server successfully handled the request.

---

## PART 8: Troubleshooting Lessons

### 28. SSH Connection Timed Out

We encountered:

```
port 22: Connection timed out
```

The reason was that our public IP address had changed.

Earlier SSH rule:

```
<OLD_PUBLIC_IP>/32
```

New public IP:

```
<NEW_PUBLIC_IP>
```

We checked the new IP using PowerShell:

```
(Invoke-RestMethod -Uri "https://checkip.amazonaws.com").Trim()
```

We updated the Security Group SSH source to:

```
203.0.113.25/32
```

After that, SSH worked again.

**Lesson:** A changing public IP can prevent SSH access when the Security Group allows only the previous IP.

### 29. Website Connection Timed Out

We investigated the issue systematically instead of reinstalling everything.

#### Test 1: Nginx status

```
sudo systemctl status nginx
```

Result: Nginx was active.

#### Test 2: Local HTTP request

```
curl -I http://localhost
```

Result:

```
HTTP/1.1 200 OK
```

This showed that Nginx could serve requests locally.

#### Test 3: Public IP

```
curl -4 https://checkip.amazonaws.com
```

Result:

```
<EC2_PUBLIC_IP>
```

The public IP was unchanged.

#### Test 4: Listening port

```
sudo ss -tlnp | grep ':80'
```

Result:

```
LISTEN 0 511 0.0.0.0:80
LISTEN 0 511 [::]:80
```

This confirmed that Nginx was listening on all IPv4 and IPv6 interfaces.

#### Test 5: Ubuntu firewall

```
sudo ufw status
```

Result:

```
Status: inactive
```

#### Test 6: Windows connectivity

```
Test-NetConnection <EC2_PUBLIC_IP> -Port 80
```

Result:

```
TcpTestSucceeded : True
```

This confirmed that Windows could establish a TCP connection to EC2 on port 80.

#### Test 7: External HTTP request

```
curl.exe -I http://<EC2_PUBLIC_IP>
```

Result:

```
HTTP/1.1 200 OK
Server: nginx/1.28.3 (Ubuntu)
Content-Type: text/html
Content-Length: 18856
```

**Final lesson:** Troubleshooting should be performed layer by layer:

1. Check whether the EC2 instance is running.
2. Check Security Groups.
3. Check whether the web server is running.
4. Check whether the service is listening on the correct port.
5. Check local firewall rules.
6. Test network connectivity from your computer.
7. Test the actual HTTP response.

---

## PART 9: Important Commands Cheat Sheet

| Task                 | Command                                        |
| -------------------- | ---------------------------------------------- |
| Connect to EC2       | `ssh -i KEY.pem ubuntu@PUBLIC_DNS`             |
| Transfer files       | `scp -i KEY.pem FILE ubuntu@PUBLIC_DNS:/path/` |
| Update packages      | `sudo apt update`                              |
| Install Nginx        | `sudo apt install nginx -y`                    |
| Check Nginx          | `sudo systemctl status nginx`                  |
| Reload Nginx         | `sudo systemctl reload nginx`                  |
| Test configuration   | `sudo nginx -t`                                |
| List files           | `ls -lh`                                       |
| Create directory     | `sudo mkdir -p /var/www/resume`                |
| Edit configuration   | `sudo nano /etc/nginx/sites-available/default` |
| Check local HTTP     | `curl -I http://localhost`                     |
| Check listening port | `sudo ss -tlnp \| grep ':80'`                  |
| Check firewall       | `sudo ufw status`                              |

---

## PART 10: What I Learned Today

By completing this task, I learned:

1. What Amazon EC2 is and why it is used.
2. How cloud computing differs from using a local computer.
3. The difference between EC2 and S3.
4. What an EC2 instance represents.
5. The difference between public and private IP addresses.
6. How to connect to Ubuntu using SSH.
7. What a PEM private key does.
8. How AWS Security Groups control inbound traffic.
9. Why SSH uses port 22 and HTTP uses port 80.
10. How to work with Ubuntu terminal commands.
11. How to install and manage Nginx.
12. What a web server does.
13. What a document root is.
14. How to transfer files using SCP.
15. How to configure Nginx to serve a website from a custom directory.
16. How to test Nginx configuration before reloading.
17. How to check HTTP responses using curl.
18. How to troubleshoot SSH and website connectivity problems.
19. Why HTTP and HTTPS are different.
20. How multiple AWS and Linux components work together to host a website.

### Final Understanding

The most important concept I learned today:

**EC2 gives me a virtual computer in the cloud. Ubuntu is its operating system. Nginx acts as its web server. SCP transfers my website files to it. SSH lets me control it remotely. AWS Security Groups control who can connect to it.**

Together, these components allow me to host and manage my own website on AWS.

---

## Next learning goals

- Finish configuring the custom 404 error page.
- Understand Nginx server blocks.
- Learn how to configure HTTPS using TLS certificates.
- Explore EC2 monitoring through CloudWatch.
- Automate deployment using Python and Boto3.
- Compare EC2 and S3 website hosting in practice.
