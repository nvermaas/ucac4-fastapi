from datetime import datetime

from pydantic import BaseModel
from typing import Optional

# Pydantic models help you define request payload models
# and response models in Python Class object notation

class Star(BaseModel):
    zone: int
    mpos1: int
    ra: float
    dec: float
    j_mag : Optional[float]
    v_mag : Optional[float]

    class Config:
        orm_mode = True

class HygData(BaseModel):
    id: int
    HipparcosID: str
    HenryDraperID: str
    HarvardRevisedID: str
    GlieseID: str
    BayerFlamsteed: str
    ProperName: str
    RightAscension: float
    Declination: float
    DistanceInParsecs: float
    Magnitude: float
    AbsoluteMagnitude: float
    SpectralType: str
    ColorIndex: str
    Bayer: str
    Flamsteed: str
    Constellation: str
    Luminosity: float

    class Config:
        orm_mode = True