from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db_session
from app.api.book.book_handlers import (
    get_book,
    create_book
)
from app.domain_types.schemas.schemas import BookResponse ,BookCreate

book_router = APIRouter()
@book_router.post("/books", response_model=BookResponse)
def create_book_(data: BookCreate, db: Session = Depends(get_db_session)):
    return create_book(db, data)

@book_router.get("/books/{book_id}", response_model=BookResponse)
def get_book_(book_id: int, db: Session = Depends(get_db_session)):
    return get_book(db, book_id)
