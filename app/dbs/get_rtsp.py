from app.dbs.database import get_connection

def get_rtsp_link(camera_name_display):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT rtsp FROM metthier.iv_cameras WHERE camera_name_display = %s", (camera_name_display,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error during SQL: {e}")
        return None
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()