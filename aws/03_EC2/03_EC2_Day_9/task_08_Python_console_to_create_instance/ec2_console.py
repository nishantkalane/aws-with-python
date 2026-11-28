import boto3

# AWS Configuration
REGION = "ap-southeast-2"

AMI_ID = "ami-0331e43da0c1f186e"

KEY_NAME = "second-server-key"

INSTANCE_TYPE = "t3.micro"


# Establish AWS EC2 connection
ec2 = boto3.resource(
    "ec2",
    region_name=REGION
)

print("EC2 resource initialized for region:", REGION)

instance_id = None

def create_instance():

    global instance_id

    instance_name = input("\nEnter a name for your EC2 instance: ")

    print("\nCreating a new EC2 instance...")

    instances = ec2.create_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": instance_name
                    }
                ]
            }
        ]
    )

    instance = instances[0]
    instance_id = instance.id

    print("\nEC2 Instance Created Successfully!")
    print("Instance Name:", instance_name)
    print("Instance ID:", instance_id)

    return instance_id

def wait_until_running():

    global instance_id

    if instance_id is None:
        print("No instance selected!")
        return

    instance = ec2.Instance(instance_id)

    print("\nWaiting for instance to become running...")

    instance.wait_until_running()

    instance.reload()

    print("\nInstance is now RUNNING!")
    print("Instance ID:", instance_id)
    print("Instance State:", instance.state["Name"])


def get_public_ip():

    global instance_id

    if instance_id is None:
        print("No instance selected!")
        return

    instance = ec2.Instance(instance_id)

    instance.reload()

    public_ip = instance.public_ip_address

    if public_ip:
        print("\nPublic IP Address:", public_ip)
    else:
        print("\nNo public IP address assigned!")
def stop_instance():

    global instance_id

    if instance_id is None:
        print("No instance selected!")
        return

    print("\nStopping EC2 instance...")

    instance = ec2.Instance(instance_id)

    instance.stop()

    print("Waiting for instance to stop...")

    instance.wait_until_stopped()
    instance.reload()

    print("\nInstance stopped successfully!")
    print("Instance ID:", instance_id)
    print("Instance State:", instance.state["Name"])

def start_instance():

    global instance_id

    if instance_id is None:
        print("No instance selected!")
        return

    print("\nStarting EC2 instance...")

    instance = ec2.Instance(instance_id)

    instance.start()

    print("Waiting for instance to start...")

    instance.wait_until_running()

    instance.reload()

    print("\nInstance started successfully!")
    print("Instance ID:", instance_id)
    print("Instance State:", instance.state["Name"])

def terminate_instance():

    global instance_id

    if instance_id is None:
        print("No instance selected!")
        return

    print("\nWARNING: You are about to terminate this EC2 instance.")
    print("Instance ID:", instance_id)

    confirmation = input("Are you sure? (yes/no): ")

    if confirmation.lower() == "yes":

        instance = ec2.Instance(instance_id)

        instance.terminate()

        print("\nWaiting for instance termination...")

        instance.wait_until_terminated()

        print("Instance terminated successfully!")

        instance_id = None

    else:
        print("Termination cancelled.")

def main():

    global instance_id

    while True:

        print("\n================================")
        print("       EC2 MANAGEMENT CONSOLE")
        print("================================")

        print("1. Create a NEW EC2 Instance")
        print("2. Select an EXISTING EC2 Instance")
        print("3. Check Instance Status")
        print("4. Get Public IP Address")
        print("5. Stop EC2 Instance")
        print("6. Start EC2 Instance")
        print("7. Terminate EC2 Instance")
        print("8. Exit")

        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            create_instance()
            wait_until_running()
            get_public_ip()

        elif choice == "2":

            instance_id = input("Enter existing Instance ID: ")
            print("Selected Instance:", instance_id)

        elif choice == "3":

            if instance_id is None:
                print("Please select an instance first!")
            else:
                instance = ec2.Instance(instance_id)
                instance.reload()
                print("Instance State:", instance.state["Name"])

        elif choice == "4":

            get_public_ip()

        elif choice == "5":

            stop_instance()

        elif choice == "6":

            start_instance()
            get_public_ip()

        elif choice == "7":

            terminate_instance()

        elif choice == "8":

            print("Exiting EC2 Management Console...")
            break

        else:

            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()