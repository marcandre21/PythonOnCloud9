import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='mpl-boto3-122423'    
)

print(response)
