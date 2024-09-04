
from msilib.schema import AppId
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.api.author import author_handlers
from app.domain_types.schemas.schemas import AuthorCreate, AuthorResponse  


author_router = APIRouter()

@author_router.post("/authors/", response_model=AuthorResponse)
def create_author(data: AuthorCreate, db: Session = Depends(get_db)):
    return author_handlers.create_author(db, data)

@author_router.get("/authors/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    db_author= author_handlers.get_publisher(db=db, author_id=author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author
