import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def upload_file(folder, blob_client, container_name):
    for file in os.listdir(folder):
        upload_client=blob_client.get_blob_client(container=container_name, blob=file)
        with open(folder+"/"+file, "rb") as data:
            upload_client.upload_blob(data)
            
def do_containers_exist(list):
    cont1300 = False
    cont3110 = False
    cont4010 = False
    for i in list:
        if i['name'] == 'manavcis1300':
            cont1300 = True
        elif i['name'] == 'manavcis3110':
            cont3110 = True
        elif i['name'] == 'manavcis4010':
            cont4010 = True

    if cont1300 and cont3110 and cont4010:
        return True
    else:
        return False

def main():
    try:
        print("Azure Blob storage v12 - Python quickstart sample")
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        # check to see if the containers exis
        possible_containers = blob_service_client.list_containers(name_starts_with=None, include_metadata=False)

        if do_containers_exist(possible_containers):
            print('containers already exist exitting')
            exit(0)
        print("creating container manavcis1300")
        container_client = blob_service_client.create_container('manavcis1300')
        print("created container now uploading files to container: manavcis1300")
        upload_file('./files/1300', blob_service_client, 'manavcis1300')

        print("creating container manavcis3110")
        container_client = blob_service_client.create_container('manavcis3110')
        print("created container now uploading files to container: manavcis3110")
        upload_file('./files/3110', blob_service_client, 'manavcis3110')

        print("creating container manavcis4010")
        container_client = blob_service_client.create_container('manavcis4010')
        print("created container now uploading files to container: manavcis4010")
        upload_file('./files/4010', blob_service_client, 'manavcis4010')



        
        
            # Quick start code goes here
    except Exception as ex:
        print('Exception:')
        print(ex)

main()