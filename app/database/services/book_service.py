from fastapi import HTTPException, Query, Body
from app.common.utils import print_colorized_json
from app.database.models.book_model import Book
from app.domain_types.schemas.schemas import BookCreate, BookResponse
from sqlalchemy.orm import Session
from app.domain_types.miscellaneous.exceptions import Conflict, NotFound
from sqlalchemy import asc, desc, func
import datetime as dt


def create_book(session: Session, model: BookCreate) -> BookResponse:
    model_dict = model.dict()
    db_model = Book(**model_dict)
    db_model.UpdatedAt = dt.datetime.now()
    session.add(db_model)
    session.commit()
    temp = session.refresh(db_model)
    book = db_model

    print_colorized_json(book)
    return book.__dict__