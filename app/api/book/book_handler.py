# app/api/book/book_handlers.py
from sqlalchemy.orm import Session
from app.database.models.book_model import Book
from app.domain_types.schemas.schemas import BookCreate
from app.database.services import book_service
from app.domain_types.miscellaneous.response_model import ResponseModel
from app.domain_types.schemas.schemas import BookResponse


def create_book(db: Session, model: BookCreate):
    try:
        book = book_service.create_book(db, model)
        message = "Book record created successfully"
        resp = ResponseModel[BookResponse](
            Message=message, Data=book)
        # logger.info(resp)
        return resp
    except Exception as e:
        print(e)
        db.rollback()
        raise e
    finally:
        db.close()

def get_book(db_session: Session, book_id: int):
    try:
        book = book_service.get_address_by_id(db_session, book_id)
        message = "Book retrieved successfully"
        resp = ResponseModel[BookResponse](
            Message=message, Data=book)
        # logger.info(resp)
        return resp
    except Exception as e:
        print(e)
        db_session.rollback()
        raise e
    finally:
        db_session.close()

