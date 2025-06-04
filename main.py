import ast
import requests
import os
from dotenv import load_dotenv

from app.dbs.get_rtsp import get_rtsp_link
from app.dbs.insert_body import insert_detection_log

from app.utils.download_image import download_img
from app.utils.convertToBase64 import convert_image_to_base64

from app.schemas.iv_cameras_schemas import IVCameras

# Main
load_dotenv()
rtsp_link = get_rtsp_link("Helmet Camera") #input camera_name_display

if not rtsp_link:
    print("RTSP link not found.")
    exit()
else:
    print(rtsp_link)

data = {"video_path": rtsp_link}

HOST_API = os.getenv('API_HOST')
print(HOST_API)

if not HOST_API:
    print("API host not set in environment variables.")
    exit()
    
with requests.post(f'{HOST_API}/api/detect/stream', json=data, stream=True) as response:
    print("waiting for data from {} . . . ")
    for line in response.iter_lines():
        if line and line.decode().startswith("data: "):
            try:
                data_dict = ast.literal_eval(line.decode()[len("data: "):])
                print(f"receive : {data_dict} \n")

                schema_data = IVCameras(**data_dict)

                snp_path = download_img("/".join(schema_data.snapshot_image.split("/")[4:])) # get just after bucket

                snapshot_base64 = convert_image_to_base64(snp_path)
                os.remove(snp_path)

                insert_detection_log(schema_data, rtsp_link, snapshot_base64 )

            except Exception as e:
                print("Error parsing data:", e)
