import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_serv_client = BlobServiceClient.from_connection_string(connect_str)
except Exception as ex:
    print("Eexception:")
    print(ex)
    exit(0)


def print_help():
    print('Commands:\n1) all\n2) container <name>\n3) file <name>\n4) download <name>\n5) quit')


def get_all_files():
    containers = blob_serv_client.list_containers(name_starts_with=None, include_metadata=False)
    for container in containers:
        container_client = blob_serv_client.get_container_client(container)
        files = container_client.list_blobs(name_starts_with=None, include=None)
        print("In container: "+ container['name'])
        for f in files:
            print('\t'+f['name'])


def get_blob_in_container(container_name):
    try:
        container = blob_serv_client.get_container_client(container_name)
        files = container.list_blobs()
        print('files in container: '+ container_name)
        for f in files:
            print("\t" + f['name'])
    except Exception as e:
        print('failed to get blobs in ' + container_name)
        print(e)

def find_file(file_name):
    containers = blob_serv_client.list_containers()
    for container in containers:
        container_client = blob_serv_client.get_container_client(container)
        blobs = container_client.list_blobs()
        for file in blobs:
            if file['name'] == file_name:
                print("Found file "+ file_name+" in container " + container['name'])
                return
    
    print("Could not find "+file_name+" in any containers")

def download_blob(filename, download_path):
    containers = blob_serv_client.list_containers()
    for container in containers:
        container_client = blob_serv_client.get_container_client(container)
        blobs = container_client.list_blobs()
        for b in blobs:
            if b['name'] == filename:
                #Found file download the blob
                print('found '+ filename)
                try:
                    print("downloading...")
                    with open(download_path, 'wb') as data:
                        container_client.download_blob(filename).download_to_stream(data)
                        print("finished")
                        return
                except Exception as e:
                    print('Failed to download ' + filename + " " + e)

    print("Could not find file "+ filename)

def main():
    os.system('clear')
    print_help()
    user_command = input(">>> Enter a command: ").split()
    command = ''
    command = user_command[0]
    if len(user_command) > 1:
        filename = user_command[1]
    while command != 'quit':
        if command == 'all':
            get_all_files()
        if command == 'container':
            get_blob_in_container(filename)
        if command == 'file':
            find_file(filename)
        if command == 'download':
            download_blob(filename, './downloads/azure/'+filename)
        user_command = input(">>> Enter a command: ").split()
        command = user_command[0]
        if len(user_command) > 1:
            filename = user_command[1]


main()