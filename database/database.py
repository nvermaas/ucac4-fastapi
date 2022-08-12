import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Note that we are using databases package as it uses asyncpg
# as an interface to talk to PostgreSQL database
#import databases


#DATABASE_URL = "postgresql://postgres:postgres@localhost/ucac4"
# dev machine on SURFSara
DATABASE_URL = "postgresql://postgres:secret@145.38.187.31/ucac4"
#database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
engine = create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
#metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()