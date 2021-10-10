from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from random import randint
import os
from dotenv import load_dotenv
load_dotenv()


engine = create_engine(
    os.environ.get('SQLALCHEMY_DATABASE_URL'), connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
