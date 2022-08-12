from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime

from .database import Base

class Asteroid(Base):
    __tablename__ = "transients_app_asteroid"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String)
    absolute_magnitude = Column(Float)
    visual_magnitude = Column(Float)
    timestamp = Column(DateTime)
    ra = Column(Float)
    dec = Column(Float)


# sql alchemy model
class Star(Base):
    __tablename__ = "stars"
    zone = Column(Integer, index=True)
    mpos1 = Column(Integer, primary_key=True, index=True)
    ra = Column(Float, index=True)
    dec = Column(Float, index=True)
    j_mag = Column(Integer, index=True)
    v_mag = Column(Integer, index=True)

