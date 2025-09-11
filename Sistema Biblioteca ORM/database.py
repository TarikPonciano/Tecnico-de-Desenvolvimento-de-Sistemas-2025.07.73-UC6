from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#DATABASE_URL = "postgresql+psycopg2://usuario:senha@localhost:5432/meuBanco"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()