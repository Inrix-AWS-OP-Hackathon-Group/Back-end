import boto3
from dotenv import load_dotenv
import os

load_dotenv()

# Put your AWS credentials in a .env file
access_key_id_S3 = os.getenv("AWS_ACCESS_KEY_S3_ID")
secret_access_key_S3 = os.getenv("AWS_SECRET_ACCESS_KEY_S3")


s3_client = boto3.client('s3')
bucket_name = os.getenv("S3_BUCKET_NAME")

file_keys = []

response = s3_client.list_objects_v2(Bucket=bucket_name)

if 'Contents' in response:
  for obj in response['Contents']:
    file_keys.append(obj['Key'])

for i in range(len(file_keys)):
  print(file_keys[i])

print(len(file_keys))