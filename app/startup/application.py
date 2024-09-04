#from fastapi import FastAPI
#from app.api.author import author_routes
#from app.api.book import book_routes
#from app.api.publisher import publisher_routes



#app = FastAPI()


#app.include_router(author_routes)
#app.include_router(publisher_routes)
#app.include_router(book_routes)
    
from fastapi import FastAPI
from app.api import api_router
from app.database.models.author_model import Base
from app.database.models.book_model import Base
from app.database.models.publisher_model import Base
from app.database.database import engine

def create_app() -> FastAPI:
    app = FastAPI()

    # Create all database tables
    Base.metadata.create_all(bind=engine)

    # Include all routers
    app.include_router(api_router)

    return app



