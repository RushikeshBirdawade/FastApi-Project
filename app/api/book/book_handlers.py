# app/api/book/book_handlers.py
from sqlalchemy.orm import Session
from app.database.models.book_model import Book
from app.domain_types.schemas.schemas import BookCreate 


def create_book(db: Session, book: BookCreate):
    db_book = Book(title=book.title, author_id=book.author_id, publisher_id=book.publisher_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

