# AWS S3 & Azure Blob Store
These scripts are used to interact with Amazon Web Services Simple Storage Service (S3) and Microsoft Azure's Blob Storage. 

The AWS scripts `awsS3Client.py` and `awsS3Uploader.py` makes use of the `Boto3` SDK provided by Amazon to create S3 buckets and upload/download files to respective buckets. 

The `azureBlobStoreClient.py` and `azureBlobStoreUploader.py` scripts are used to interact with Azure's Blob Storage. The scripts will create containers within Azure's cloud and allow uploads/download of blobs (files) from the created containers. 