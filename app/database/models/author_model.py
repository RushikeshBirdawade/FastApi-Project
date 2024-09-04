from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database.base import Base
from sqlalchemy.sql import func


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(15))
    created_at = Column(DateTime, default=func.now())
    books = relationship("Book",back_populates="author")
