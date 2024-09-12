from fastapi import HTTPException, Query, Body
from app.common.utils import print_colorized_json
from app.database.models.author_model import Author
from app.domain_types.schemas.schemas import AuthorCreate, AuthorResponse
from sqlalchemy.orm import Session
from app.domain_types.miscellaneous.exceptions import Conflict, NotFound
from sqlalchemy import asc, desc, func
import datetime as dt


def create_author(session: Session, model: AuthorCreate) -> AuthorResponse:
    model_dict = model.dict()
    db_model = Author(**model_dict)
    db_model.UpdatedAt = dt.datetime.now()
    session.add(db_model)
    session.commit()
    temp = session.refresh(db_model)
    author = db_model

    print_colorized_json(author)
    return author.__dict__
