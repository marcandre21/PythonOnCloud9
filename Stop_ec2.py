import json
import boto3

def stop_instances_by_tag(tag_key, tag_value):
    # Specify the region
    region = 'us-east-1'

    # Create EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Describe instances with the specified tag
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:' + tag_key, 'Values': [tag_value]}
        ]
    )

    # Extract instance IDs from the response
    instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

    # Stop instances
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopping Instances with tag {tag_key}={tag_value}:")
        print(instance_ids)
    else:
        print(f"No instances found with tag {tag_key}={tag_value}")

# Lambda handler
def lambda_handler(event, context):
    # Specify the tag key and value for identifying instances
    tag_key = 'Env'
    tag_value = 'Dev'

    # Stop instances with the specified tag
    stop_instances_by_tag(tag_key, tag_value)