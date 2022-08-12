from sqlalchemy.orm import Session

from . import models, schemas
from .models import Star

def get_asteroids(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Asteroid).offset(skip).limit(limit).all()

def get_stars(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Star).offset(skip).limit(limit).all()

def get_rectangle(db: Session, ra_min: float = 0.0, ra_max: float = 1.0, dec_min: float = 0.0, dec_max: float = 1.0, limit: int = 1000):
    list = db.query(Star).filter(
        Star.ra > ra_min,
        Star.ra < ra_max,
        Star.dec > dec_min,
        Star.dec < dec_max,
    ).limit(limit).all()
    return list