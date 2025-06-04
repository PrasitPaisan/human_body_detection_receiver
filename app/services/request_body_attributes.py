import requests
import os
from dotenv import load_dotenv

load_dotenv()

def request_body_attributes(image_path):

    data ={
    "image_path" : image_path
    }
    try:
        response = requests.post(f"{os.getenv('API_HOST')}/get/tk_API/body_attributes", json=data, timeout=10) 
        response.raise_for_status()
        return response.json()
    except Exception as e :
        print(f" Error in request : {e}")
        return None