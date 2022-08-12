from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

router = APIRouter(tags=["cutouts"])

class Cutout(BaseModel):
    name: str
    ra: float
    dec: float
    fov: Optional[float] = 2
    timestamp : Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "name": "Lambda Orionis",
                "ra": 84.9,
                "dec" : 9.5,
                "fov" : 1.0,
                "timestamp" : "2022-02-06T08:37:37.701815"
            }
        }

cutouts_data = {
    1: {"name": "Orion", "ra": 90.0, "dec": 0.0, "fov": 45.0},
    2: {"name": "Lambda Orionis", "ra": 84.9, "dec": 9.5, "fov": 1.0},
}

@router.get("/")
async def root():
    return {"message": "Hello World"}


# http://127.0.0.1:8000/items/3
@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.post("/cutouts/new", tags=["cutouts"])
async def create_cutout(cutout: Cutout):
    print(cutout.name)
    return cutout

# http://127.0.0.1:8000/cutouts/1
# http://127.0.0.1:8000/cutouts/3
@router.get("/cutouts/{cutout_id}", response_model=Cutout, tags=["cutouts"])
async def get_cutout(cutout_id: int):
    if cutout_id not in cutouts_data:
        raise HTTPException(status_code=404, detail="Cutout not found")
    cutout = cutouts_data[cutout_id]
    print(cutout)
    return cutout