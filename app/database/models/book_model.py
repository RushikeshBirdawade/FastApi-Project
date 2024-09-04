from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    created_at = Column(DateTime, default=func.now())

    author = relationship('Author', back_populates='books')
    publisher = relationship('Publisher', back_populates='books')



   # author = relationship("Author", back_populates="books")
   # publisher = relationship("Publisher", back_populates="books")