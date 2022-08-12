from datetime import datetime

from pydantic import BaseModel

# Pydantic models help you define request payload models
# and response models in Python Class object notation

class Asteroid(BaseModel):
    designation: str
    absolute_magnitude : float

    timestamp : datetime
    visual_magnitude: float
    ra: float
    dec: float

    class Config:
        orm_mode = True

class Star(BaseModel):
    zone: int
    mpos1: int
    ra: float
    dec: float
    j_mag : float


    class Config:
        orm_mode = True