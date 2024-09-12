from fastapi import HTTPException, Query, Body
from app.common.utils import print_colorized_json
from app.database.models.publisher_model import Publisher
from app.domain_types.schemas.schemas import PublisherCreate, PublisherResponse
from sqlalchemy.orm import Session
from app.domain_types.miscellaneous.exceptions import Conflict, NotFound
from sqlalchemy import asc, desc, func
import datetime as dt


def create_publisher(session: Session, model: PublisherCreate) -> PublisherResponse:
    model_dict = model.dict()
    db_model = Publisher(**model_dict)
    db_model.UpdatedAt = dt.datetime.now()
    session.add(db_model)
    session.commit()
    temp = session.refresh(db_model)
    publisher = db_model

    print_colorized_json(publisher)
    return publisher.__dict__
