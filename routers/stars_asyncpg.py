from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from utils import timeit
from database import crud_asyncpg, models, schemas
from database.database_asyncpg import SessionLocal, engine
from database.database_asyncpg import my_database
from database.models import Star

router = APIRouter(tags=["stars"],)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@timeit
@router.get("/stars/", tags=["stars"], response_model=List[schemas.Star])
async def get_stars_async(skip: int = 0, limit: int = 1000):
    query = crud_asyncpg.get_star_query(Star.__table__, skip=skip, limit=limit)
    return await my_database.fetch_all(query)

@timeit
@router.get("/stars_rectangle/", tags=["stars"], response_model=List[schemas.Star])
async def get_stars_rectangle_async(ra_min: float = 0.0, ra_max: float = 1.0,
                              dec_min: float = 0.0, dec_max: float = 1.0,
                              j_mag: int = 10000, limit: int = 1000):

    query = crud_asyncpg.get_rectangle_query(Star.__table__, ra_min=ra_min, ra_max=ra_max, dec_min=dec_min, dec_max=dec_max, j_mag=j_mag, limit=limit)
    return await my_database.fetch_all(query)