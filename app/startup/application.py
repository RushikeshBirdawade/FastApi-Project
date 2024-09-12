#from fastapi import FastAPI
#from app.api.author import author_routes
#from app.api.book import book_routes
#from app.api.publisher import publisher_routes



#app = FastAPI()


#app.include_router(author_routes)
#app.include_router(publisher_routes)
#app.include_router(book_routes)

from fastapi import FastAPI
#from app.api import api_router
#from app.database import models
#from app.database.models.author_model import Base
#from app.database.models.book_model import Base
#from app.database.models.publisher_model import Base
from app.database.database import engine
from app.startup.router import router
from app.database.base import Base
from fastapi.middleware.cors import CORSMiddleware

def create_app():

    server = FastAPI()

    # Add CORS middleware
    server.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    server.include_router(router)

    return server
app=create_app()


