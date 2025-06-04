import cv2
import base64

def convert_image_to_base64(img_path):

    img = cv2.imread(img_path)

    if img is None:
        raise ValueError(f"Could not read image from path: {img_path}")

    _, buffer = cv2.imencode('.jpg', img)

    img_base64 = base64.b64encode(buffer).decode('utf-8')

    return img_base64


