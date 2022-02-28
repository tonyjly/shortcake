import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB = os.environ.get('POSTGRES_DB')
HOST = os.environ.get('POSTGRES_HOST')
PORT = os.environ.get('POSTGRES_PORT')

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
