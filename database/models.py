from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

# sql alchemy model
Base = declarative_base()

class Star(Base):
    __tablename__ = "stars"
    zone = Column(Integer, index=True)
    mpos1 = Column(Integer, primary_key=True, index=True)
    ra = Column(Float, index=True)
    dec = Column(Float, index=True)
    j_mag = Column(Integer, index=True)
    v_mag = Column(Integer, index=True)

class HygData(Base):
    __tablename__ = "hygdata"
    id = Column(Integer, primary_key=True, index=True)
    HipparcosID = Column(String)
    HenryDraperID = Column(String)
    HarvardRevisedID = Column(String)
    GlieseID = Column(String)
    BayerFlamsteed = Column(String)
    ProperName = Column(String)
    RightAscension = Column(Float, index=True)
    Declination = Column(Float, index=True)
    DistanceInParsecs = Column(Float)
    Magnitude = Column(Float)
    AbsoluteMagnitude = Column(Float)
    SpectralType = Column(String)
    ColorIndex = Column(String)
    Bayer = Column(String)
    Flamsteed = Column(String)
    Constellation = Column(String)
    Luminosity = Column(Float)