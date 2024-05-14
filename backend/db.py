from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

class Database:
    def __init__(self):
        self.POSTGRES_HOST = os.getenv("POSTGRES_HOST")
        self.POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
        self.POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
        self.POSTGRES_PORT = os.getenv("POSTGRES_PORT")
        self.POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

        self.DATABASE_URL = f"postgresql://{self.POSTGRES_USERNAME}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}"

        self.engine = create_engine(self.DATABASE_URL)
        self.Base = declarative_base()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
