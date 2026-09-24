import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker,declarative_base

# Load values from the .env file
load_dotenv()



test = os.getenv("TEST")

engine = create_engine(os.getenv("DATABASE_URL"))
# Create an sqlalchemy engine
# An Engine is a factory for connection objects.It encapsulates a connection pool
# that minimizes the cost of connecting to the database by reusing existing connections
# and provides a consistent API for working with transactions.

metadata_obj = MetaData() # create a SQLAlchemy metadata object
# uses for organizing and managing database schema objects


SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) # create a SQLAlchemy session factory
# uses for managing database sessions in a FastAPI application


Base = declarative_base() # create a SQLAlchemy base class
# uses for defining database tables and their relationships

