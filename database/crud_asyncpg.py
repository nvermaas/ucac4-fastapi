from sqlalchemy.orm import Session

from .models import Star, HygData
from utils import timeit

@timeit
def get_star_query(stars,  skip: int = 0, limit: int = 1000):
    query = stars.select().offset(skip).limit(limit)
    return query

@timeit
def get_rectangle_query(stars, ra_min: float = 0.0, ra_max: float = 1.0, dec_min: float = 0.0, dec_max: float = 1.0, j_mag: int = 10000, limit: int = 1000):
    query = stars.select().where(
        Star.ra > ra_min,
        Star.ra < ra_max,
        Star.dec > dec_min,
        Star.dec < dec_max,
        Star.j_mag < j_mag
    ).limit(limit)
    return query

def get_hygdata_query(hygdata,  skip: int = 0, limit: int = 1000):
    query = hygdata.select().offset(skip).limit(limit)
    return query


@timeit
def get_hygdata_rectangle(hygdata, ra_min: float = 0.0, ra_max: float = 1.0, dec_min: float = 0.0, dec_max: float = 1.0, magnitude: float = 10.0, limit: int = 1000):
    query = hygdata.select().where(
        HygData.RightAscension > ra_min,
        HygData.RightAscension < ra_max,
        HygData.Declination > dec_min,
        HygData.Declination < dec_max,
        HygData.Magnitude < magnitude
    ).limit(limit)
    return query