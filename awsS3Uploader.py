import boto3
import os
from botocore.exceptions import ClientError


def upload_file(folder, bucket, s3_client):
    for file in os.listdir(folder):
        print("Uploading:" + folder+"/"+file)
        s3_client.upload_file(folder+'/'+file, bucket, file)

def create_buckets(names, s3_client):
    try:
        for name in names:
            s3_client.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint': 'ca-central-1'} )
        return True
    except Exception as e:
        print(e)
        return False

client = boto3.client('s3')
bucket_names = set(['manavcis1300', 'manavcis3110', 'manavcis4010'])
resp = set(client.list_buckets())
for name in bucket_names:
    try:
        print("Creating bucket " + name)
        resp = client.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint': 'ca-central-1'})
    except ClientError as e:
        if e.response['Error']['Code'] == 'BuckerAlreadyExists' or e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print("Bucket already exists")
            continue
        else:
            print("Unexpected error" + e)

upload_file('./files/1300', 'manavcis1300', client)
upload_file('./files/3110', 'manavcis3110', client)
upload_file('./files/4010', 'manavcis4010', client)

