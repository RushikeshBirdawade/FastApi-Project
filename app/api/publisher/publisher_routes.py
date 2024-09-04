from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database_accessor import get_db_session
from app.api.publisher import publisher_handlers
from app.domain_types.schemas.schemas import PublisherCreate, PublisherResponse

publisher_router = APIRouter()

@publisher_router.post("/publishers/", response_model=PublisherResponse)
def create_publisher(data: PublisherCreate, db: Session = Depends(get_db_session)):
    return publisher_handlers.create_publisher(db, data)

@publisher_router.get("/publishers/{publisher_id}", response_model=PublisherResponse)
def get_publisher(publisher_id: int, db: Session = Depends(get_db_session)):
    db_publisher= publisher_handlers.get_publisher(db=db, publisher_id=publisher_id)
    if not db_publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return db_publisher



