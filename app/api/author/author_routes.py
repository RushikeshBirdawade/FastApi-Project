from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db_session
from app.api.author.author_handlers import (
    get_author,
    create_author
)
from app.domain_types.schemas.schemas import AuthorResponse, AuthorCreate

author_router = APIRouter()

@author_router.post("/authors", response_model=AuthorResponse)
def create_author_(data: AuthorCreate, db: Session = Depends(get_db_session)):
    return create_author(db, data)

@author_router.get("/authors/{author_id}", response_model=AuthorResponse)
def get_author_(author_id: int, db: Session = Depends(get_db_session)):
    return get_author(db, author_id)
