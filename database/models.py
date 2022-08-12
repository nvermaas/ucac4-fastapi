from sqlalchemy import Column, Integer, String, Float, DateTime

from .database import Base

# sql alchemy model
class Star(Base):
    __tablename__ = "stars"
    zone = Column(Integer, index=True)
    mpos1 = Column(Integer, primary_key=True, index=True)
    ra = Column(Float, index=True)
    dec = Column(Float, index=True)
    j_mag = Column(Integer, index=True)
    v_mag = Column(Integer, index=True)

