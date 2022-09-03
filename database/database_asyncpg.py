import os
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

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
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql+asyncpg://postgres:postgres@localhost/ucac4')
print('DATABASE_URL = '+DATABASE_URL)

my_database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = create_async_engine(DATABASE_URL,echo=True,)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

