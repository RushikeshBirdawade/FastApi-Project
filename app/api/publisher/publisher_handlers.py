from sqlalchemy.orm import Session
from app.common.utils import print_colorized_json
from app.database.models.publisher_model import Publisher
from app.domain_types.schemas.schemas import PublisherCreate
from app.database.services import publisher_service
from app.domain_types.miscellaneous.response_model import ResponseModel
from app.domain_types.schemas.schemas import PublisherResponse

def create_publisher(db: Session, model: PublisherCreate):
    try:
        publisher = publisher_service.create_publisher(db, model)
        message = "Publisher record created successfully"
        resp = ResponseModel[PublisherResponse](
            Message=message, Data=publisher)
        # logger.info(resp)
        print_colorized_json(resp)
        return resp
    except Exception as e:
        print(e)
        db.rollback()
        raise e
    finally:
        db.close()

def get_publisher(db_session: Session, publisher_id: int):
    try:
        publisher = publisher_service.get_publisher_by_id(db_session, publisher_id)
        message = "Publisher retrieved successfully"
        resp = ResponseModel[PublisherResponse](
            Message=message, Data=publisher)
        # logger.info(resp)
        print_colorized_json(resp)
        return resp
    except Exception as e:
        print(e)
        db_session.rollback()
        raise e
    finally:
        db_session.close()
