import json 
from app.dbs.database import get_connection
from app.services.request_body_attributes import request_body_attributes

def insert_detection_log(schema_data, rtsp_link, imageBase64):

    json_body_attributes = request_body_attributes(imageBase64)
    if json_body_attributes is not None:
        json_body_attributes = json.dumps(json_body_attributes)

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO metthier.body_detection_logs
            (body_det_id, device_id, snapshot_image, overview_image, overview_image_roi, timestamp, body_attributes) 
            VALUES (
                %s,
                (SELECT device_id FROM metthier.iv_cameras WHERE rtsp = %s),
                %s, %s, %s, %s, %s
            )
        """, (
            schema_data.body_det_id,
            rtsp_link,
            schema_data.snapshot_image,
            schema_data.overview_image,
            schema_data.overview_image_roi,
            schema_data.timestamp,
            json_body_attributes,
        ))
        conn.commit()
        print(f"Insert Finish....{schema_data.snapshot_image}")
    except Exception as e:
        print(f"Error inserting body_log: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()
