from sqlalchemy.orm import Session
from app.database.models.author_model import Author
from app.database.services import author_service
from app.domain_types.miscellaneous.response_model import ResponseModel
from app.domain_types.schemas.schemas import AuthorResponse ,AuthorCreate
from app.common.utils import print_colorized_json

def create_author(db: Session, model: AuthorCreate):
    try:
        author = author_service.create_author(db, model)
        message = "Author record created successfully"

        resp = ResponseModel[AuthorResponse](
            Message=message, Data=author)
        
        # logger.info(resp)
        print_colorized_json(resp)
        return resp
    except Exception as e:
        print(e)
        db.rollback()
        raise e
    finally:
        db.close()

def get_author(db_session: Session, author_id: int):
    try:
        author = author_service.get_author_by_id(db_session, author_id)
        message = "Author retrieved successfully"
        resp = ResponseModel[AuthorResponse](
            Message=message, Data=author)
        # logger.info(resp)
        print_colorized_json(resp)
        return resp
    except Exception as e:
        print(e)
        db_session.rollback()
        raise e
    finally:
        db_session.close()
