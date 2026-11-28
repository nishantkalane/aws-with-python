# EC2 Day 9 practice

## Task 08: EC2 management console

[`task_08_Python_console_to_create_instance/ec2_console.py`](task_08_Python_console_to_create_instance/ec2_console.py) is an interactive boto3 script for creating, selecting, starting, stopping, and terminating EC2 instances.

Before running it:

- Configure AWS credentials with `aws configure`.
- Check the `REGION`, `AMI_ID`, and `KEY_NAME` constants in the script. The AMI and key pair must be available in that region.
- Make sure the configured AWS identity has the required EC2 permissions.

Run from the task directory:

```bash
python ec2_console.py
```

This script operates on real AWS resources. Creating an instance can incur charges; stopping an instance may not stop all storage charges. Terminating an instance is destructive, so verify the selected instance ID before confirming.

## Task 07 directory

The file in [`task_07_reating_instances_using_cmd/`](task_07_reating_instances_using_cmd/) is currently an HTML page about a separate Python DSA project, not an EC2 command-line exercise. Check whether that file belongs in this folder.
