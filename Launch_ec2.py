import boto3

def launch_instances():
    # Specify the region
    region = 'us-east-1'

    # Create the EC2 client
    ec2 = boto3.client('ec2', region_name=region)
    
    # Specify the instance type
    instance_type = 't2.micro'

    # Specify the AMI ID for t2.micro instances
    ami_id = 'ami-079db87dc4c10ac91'

    # Specify the number of instances to launch
    num_instances = 3

    # Launch instances
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=num_instances,
        MaxCount=num_instances,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Development server'},
                    {'Key': 'Env', 'Value': 'Dev'}
                ]
            }
        ]
    )

    # Extract instance IDs from the response
    instance_ids = [instance['InstanceId'] for instance in response['Instances']]

    return instance_ids

if __name__ == "__main__":
    # Launch instances and get instance IDs
    instance_ids = launch_instances()

    # Print instance IDs
    print("Launched Instances:")
    for instance_id in instance_ids:
        print(instance_id)
