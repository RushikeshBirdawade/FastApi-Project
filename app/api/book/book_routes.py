from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database_accessor import get_db_session
from app.api.book.book_handler import (
    get_book,
    create_book
)
from app.domain_types.schemas.schemas import BookResponse ,BookCreate

book_router = APIRouter()
@book_router.post("/", response_model=BookResponse)
def create_book_(data: BookCreate, db: Session = Depends(get_db_session)):
    return create_book(db, data)

@book_router.get("/{book_id}", response_model=BookResponse)
def get_book_(book_id: int, db: Session = Depends(get_db_session)):
    return get_book(db, book_id)





# app/api/book/book_handlers.py
