#!/usr/bin/python3

import boto3
import os
from botocore.exceptions import ClientError


def print_help():
    print('Commands:\n1) all\n2) container <name>\n3) file <name>\n4) download <name>\n5) quit')
def clear():
    os.system('clear')

def get_all_buckets():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

def get_container(bucket_name):
    try:
        s3_client = boto3.client('s3')
        resp = s3_client.list_objects(Bucket=bucket_name)
        for obj in resp['Contents']: 
            print(obj['Key'])
    except ClientError as e:
        print ("Error:\n"+str(e))
    
def find_file(filename):
    s3 = boto3.client('s3')
    resp = s3.list_buckets()
    for bucket in resp['Buckets']:
        try:
            found=s3.get_object(Bucket=bucket['Name'], Key=filename)
            if found:
                print('found '+ filename + ' in bucket ' + bucket['Name'])
                return
        except ClientError as e:
            continue
    print('File '+ filename +' does not exist')

def download_file(filename, downloadpath):
    s3_client = boto3.client('s3')
    resp = s3_client.list_buckets()
    for bucket in resp['Buckets']:
        try:
            with open(downloadpath, 'wb') as data:
                s3_client.download_fileobj(bucket['Name'], filename, data)
            print('Downloaded...')
            return
        except ClientError as e:
            continue
    print('the file you requested:'+filename+' does not exist')
def main():
    clear()
    print_help()
    user_command = input(">>> Enter a command: ").split()
    command = ''
    command = user_command[0]
    if len(user_command) > 1:
        filename = user_command[1]
    while command != 'quit':
        if command == 'all':
            get_all_buckets()
        if command == 'container':
            get_container(filename)
        if command == 'file':
            find_file(filename)
        if command == 'download':
            download_file(filename, './downloads/aws/'+filename)

        user_command = input(">>> Enter a command: ").split()
        command = user_command[0]
        if len(user_command) > 1:
            filename = user_command[1]



main()



