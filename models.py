from beanie import Document
from pydantic import BaseModel


class PredictionModel(Document):
    image_id: str
    label: str
    confidence: float

    class Settings:
        name = 'prediction'


class PredictionRequest(BaseModel):
    title: bytes

