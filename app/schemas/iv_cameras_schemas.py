from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class Point(BaseModel):
    x: int
    y: int

class Rectangle(BaseModel):
    vertices: List[Point]

class ClassificationAttribute(BaseModel):
    type: str
    category: str
    value: float
    roi: Optional[Any]  #ืnot sure

class Pedestrian(BaseModel):
    quality: float
    rectangle: Rectangle
    track_id: str
    attributes_with_score: Dict[str, ClassificationAttribute]
    pedestrian_score: float

class ObjectInfo(BaseModel):
    type: str
    face: Optional[Any]
    pedestrian: Optional[Pedestrian]
    object_id: str
    associations: List
    

class Feature(BaseModel):
    type: str
    version: int
    blob: str

class DetectedObject(BaseModel):
    object_info: ObjectInfo
    feature: Feature

class Response(BaseModel):
    objects: List[DetectedObject]

class Result(BaseModel):
    code: int
    error: str
    status: str

class BodyAttributes(BaseModel):
    results: List[Result]
    responses: List[Response]

class IVCameras(BaseModel):
    body_det_id: str
    device_id: str = None
    timestamp: str = None
    created_at: str = None
    snapshot_image: Optional[str] = None
    overview_image_roi: Optional[str] = None 
    overview_image: Optional[str] = None
    body_attributes: Optional[BodyAttributes] = None

class GETRTSP(BaseModel):
    rtsp :str = None
