from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.api.book import  book_handlers
from app.domain_types.schemas.schemas import BookResponse ,BookCreate

book_router = APIRouter()
@book_router.post("/books/", response_model=BookResponse)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    return book_handlers.create_book(db, data)

@book_router.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book= book_handlers.get_publisher(db=db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book





# app/api/book/book_handlers.py
