import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Note that we are using databases package as it uses asyncpg
# as an interface to talk to PostgreSQL database
import databases

# dev machine on SURFSara
# DATABASE_URL = "postgresql://postgres:secret@145.38.187.31/ucac4"

# mintbox docker
# DATABASE_URL = "postgresql://postgres:secret@postgres-ucac4/ucac4"

# mintbox
# DATABASE_URL = "postgresql://postgres:secret@192.168.178.37/ucac4"

# localhost
# DATABASE_URL = "postgresql://postgres:postgres@localhost/ucac4"

# read from environment
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost/ucac4')
print('DATABASE_URL = '+DATABASE_URL)

my_database = databases.Database(DATABASE_URL) # asyncpg
metadata = sqlalchemy.MetaData()            # asyncpg

engine = create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)

metadata.create_all(engine)                 # asyncpg

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

