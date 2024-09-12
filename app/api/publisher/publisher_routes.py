from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db_session
from app.api.publisher.publisher_handlers import (
    get_publisher,
    create_publisher
)
from app.domain_types.schemas.schemas import PublisherResponse, PublisherCreate

publisher_router = APIRouter()

@publisher_router.post("/publishers", response_model=PublisherResponse)
def create_publisher_(data: PublisherCreate, db: Session = Depends(get_db_session)):
    return create_publisher(db, data)

@publisher_router.get("/publishers/{publisher_id}", response_model=PublisherResponse)
def get_publisher_(publisher_id: int, db: Session = Depends(get_db_session)):
    return get_publisher(db, publisher_id)
