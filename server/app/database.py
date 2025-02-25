import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_CONNECTION = "postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_HOST}".format(
    DB_USER=os.getenv("DB_USER"),
    DB_PASSWORD=os.getenv("DB_PASSWORD"),
    DB_HOST=os.getenv("DB_HOST"),
)

engine = create_engine(DB_CONNECTION, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    with SessionLocal() as session:
        return session
