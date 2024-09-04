from h11 import Data
from sqlalchemy.orm import Session
from app.database.models.publisher_model import Publisher
from app.domain_types.schemas.schemas import PublisherCreate

def create_publisher(db: Session, publisher: PublisherCreate):
    db_publisher = Publisher(name=publisher.name, email=publisher.email, phone_number=publisher.phone_number)
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def get_publisher(db: Session, publisher_id: int):
    return db.query(Publisher).filter(Publisher.id == publisher_id).first()