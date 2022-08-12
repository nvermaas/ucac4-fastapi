from typing import List
from enum import Enum
from datetime import datetime
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from database import crud, models, schemas
from database.database import SessionLocal, engine

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
                              limit: int = 1000, db: Session = Depends(get_db)):
    items = crud.get_rectangle(db, ra_min=ra_min, ra_max=ra_max, dec_min=dec_min, dec_max=dec_max, limit=limit)
    return items