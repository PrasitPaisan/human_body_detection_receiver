from dotenv import load_dotenv
import os 
from google.cloud import storage

load_dotenv()
bucket_name = os.getenv("BUCKET_PATH")
secret_key = os.getenv("PRIVATE_KEY")

def download_img(source_blob_name):
    # Use the JSON key to create the client
    storage_client = storage.Client.from_service_account_json(secret_key)

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    destination_file_name = f"{source_blob_name.split("/")[-1]}.jpg"
    blob.download_to_filename(destination_file_name)


    return destination_file_name
