from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from utils import timeit
from database import crud, models, schemas
from database.database import SessionLocal, engine
from database.database import my_database
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

@timeit
@router.get("/stars_rectangle_async/", tags=["stars"], response_model=List[schemas.Star])
async def get_stars_rectangle(ra_min: float = 0.0, ra_max: float = 1.0,
                              dec_min: float = 0.0, dec_max: float = 1.0,
                              j_mag: int = 10000, limit: int = 1000, db: Session = Depends(get_db)):

    stars = Star.__table__
    query = crud.get_rectangle_query(stars, ra_min=ra_min, ra_max=ra_max, dec_min=dec_min, dec_max=dec_max, j_mag=j_mag, limit=limit)
    print(query)
    return await my_database.fetch_all(query)