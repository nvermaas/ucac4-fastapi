from typing import List
from enum import Enum
from datetime import datetime
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from database import crud, models, schemas
from database.database import SessionLocal, engine

router = APIRouter(tags=["minor planets"],)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === demo stuff ======================================================================

class MinorPlanetType(str, Enum):
    asteroid = "asteroid"
    comet = "comet"

# http://127.0.0.1:8000/minorplanets/comet
@router.get("/minorplanets/{type}", tags=["minor planets"])
async def get_minor_planet(type: MinorPlanetType):
    if type == MinorPlanetType.asteroid:
        return {"type": type, "asteroid": "calculate asteroids"}
    return {"type": type, "comet": "don't look up!"}


# http://127.0.0.1:8000/asteroid/
# http://127.0.0.1:8000/asteroid/?name=vesta
@router.get("/asteroid/", tags=["minor planets"])
async def get_asteroid(name: str = 'Ceres' ):
    return {"asteroid": name}


# example of parameter metadata
# http://127.0.0.1:8000/comet/
# http://127.0.0.1:8000/comet/?comet-name=atlas
@router.get("/comet/", tags=["minor planets"])
async def get_comet(name: str = Query(
    'Neowise',
    alias="comet-name",
    title="comet name",
    description="Enter the name of the comet",
    max_length=30),
    datetime: datetime = datetime.utcnow()):
    return {"comet": name, "datetime" : datetime}


# === real stuff ======================================================================

# http://127.0.0.1:8000/asteroids/
# http://127.0.0.1:8000/asteroids/?skip=100&limit=100
@router.get("/asteroids/", tags=["minor planets"], response_model=List[schemas.Asteroid])
async def get_astroids(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    items = crud.get_asteroids(db, skip=skip, limit=limit)
    return items