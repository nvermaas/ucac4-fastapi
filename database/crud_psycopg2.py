from sqlalchemy.orm import Session

from .models import Star
from utils import timeit

@timeit
def get_stars(db: Session, skip: int = 0, limit: int = 1000):
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
