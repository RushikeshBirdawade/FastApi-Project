from sqlalchemy.orm import Session
from app.database.models.author_model import Author
from app.domain_types.schemas.schemas import AuthorCreate

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name, email=author.email, phone_number=author.phone_number)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()