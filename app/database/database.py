
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.config import Settings

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:RR2602_1999@127.0.0.1:3306/passdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
settings = Settings()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()   
