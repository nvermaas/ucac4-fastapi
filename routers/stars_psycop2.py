from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils import timeit
from database import schemas
from database import crud_psycopg2 as crud
from database.database_psycopg2 import SessionLocal
from database.models import Star

router = APIRouter(tags=["stars"],)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# http://127.0.0.1:8000/stars/
# http://127.0.0.1:8000/stars/?skip=100&limit=100
@router.get("/stars/", tags=["stars"], response_model=List[schemas.Star])
async def get_stars(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    items = crud.get_stars(db, skip=skip, limit=limit)
    return items

@router.get("/stars_rectangle/", tags=["stars"], response_model=List[schemas.Star])
async def get_stars_rectangle(ra_min: float = 0.0, ra_max: float = 1.0,
                              dec_min: float = 0.0, dec_max: float = 1.0,
                              j_mag: int = 10000, limit: int = 1000, db: Session = Depends(get_db)):
    items = crud.get_rectangle(db, ra_min=ra_min, ra_max=ra_max, dec_min=dec_min, dec_max=dec_max, j_mag=j_mag, limit=limit)
    return items

@router.get("/stars_cone/", tags=["stars"], response_model=List[schemas.Star])
async def get_stars_cone(ra: float = 0.0, dec: float = 0.0, radius: float = 1.0,
                        j_mag: int = 10000, limit: int = 1000, db: Session = Depends(get_db)):

    items = crud.get_cone(db, ra=ra, dec=dec, radius=radius, j_mag=j_mag, limit=limit)
    return items

@router.get("/hygdata/", tags=["hygdata"], response_model=List[schemas.HygData])
async def get_hygdata(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    # http://127.0.0.1:8000/hygdata/?skip=100&limit=100
    items = crud.get_hygdata(db, skip=skip, limit=limit)
    return items

@router.get("/hygdata_rectangle/", tags=["hygdata"], response_model=List[schemas.HygData])
async def get_hygdata_rectangle(ra_min: float = 0.0, ra_max: float = 1.0,
                              dec_min: float = 0.0, dec_max: float = 1.0,
                              magnitude: float = 10.0, limit: int = 1000, db: Session = Depends(get_db)):
    items = crud.get_hygdata_rectangle(db, ra_min=ra_min, ra_max=ra_max, dec_min=dec_min, dec_max=dec_max, magnitude=magnitude, limit=limit)
    return items