from sqlalchemy.orm import Session

from .models import Star, HygData
from utils import timeit

@timeit
def get_stars(db: Session, skip: int = 0, limit: int = 1000):
    # example: http://127.0.0.1:8000/stars/?skip=100&limit=100
    return db.query(Star).offset(skip).limit(limit).all()

@timeit
def get_rectangle(db: Session, ra_min: float = 0.0, ra_max: float = 1.0, dec_min: float = 0.0, dec_max: float = 1.0, j_mag: int = 10000, limit: int = 1000):
    list = db.query(Star).filter(
        Star.ra > ra_min,
        Star.ra < ra_max,
        Star.dec > dec_min,
        Star.dec < dec_max,
        Star.j_mag < j_mag
    ).limit(limit).all()
    print("retrieved "+str(len(list)) + ' stars')
    return list

@timeit
def get_hygdata(db: Session, skip: int = 0, limit: int = 1000):
    # example: http://127.0.0.1:8000/stars/?skip=100&limit=100
    return db.query(HygData).offset(skip).limit(limit).all()

@timeit
def get_hygdata_rectangle(db: Session, ra_min: float = 0.0, ra_max: float = 1.0, dec_min: float = 0.0, dec_max: float = 1.0, j_mag: int = 10000, limit: int = 1000):
    list = db.query(HygData).filter(
        HygData.RightAscension > ra_min,
        HygData.RightAscension < ra_max,
        HygData.Declination > dec_min,
        HygData.Declination < dec_max,
        HygData.Magnitude < j_mag / 1000
    ).limit(limit).all()
    print("retrieved "+str(len(list)) + ' stars')
    return list