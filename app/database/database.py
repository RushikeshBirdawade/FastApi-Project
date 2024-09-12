#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
#from app.config.config import Settings

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:RR2602_1999@127.0.0.1:3306/passdb"

#engine = create_engine(SQLALCHEMY_DATABASE_URL)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()
#settings = Settings()

#def get_db_session():
    #db = SessionLocal()
   # try:
  #      yield db
 #   finally:
#        db.close()  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config.config import get_settings
from app.database.base import Base

from app.database.models.book_model import Book 
from app.database.models.author_model import Author
from app.database.models.publisher_model import Publisher
settings = get_settings()
print(settings.DATABASE_URL)
engine = create_engine(settings.DATABASE_URL, echo=False)
# or
# engine = create_engine(
#     settings.DB_DIALECT,
#     username=settings.DB_USER_NAME,
#     password=settings.DB_USER_PASSWORD,
#     host=settings.DB_HOST,
#     port=settings.DB_PORT,
#     database=settings.DB_NAME,
#     pool_size=settings.DB_POOL_SIZE,
#     pool_recycle=settings.DB_POOL_RECYCLE,
#     drivername=settings.DB_DRIVER,
#     echo=True,
# )

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    



