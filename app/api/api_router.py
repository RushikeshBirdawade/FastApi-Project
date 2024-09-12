from fastapi import APIRouter, FastAPI
from app.api.book.book_routes import  book_router
from app.api.author.author_routes import author_router
from app.api.publisher.publisher_routes import  publisher_router

# Create an instance of APIRouter
app=FastAPI()
api_router= APIRouter()


# Include the routes from the individual modules
app.include_router(book_router, prefix="/books", tags=["books"])
app.include_router(author_router, prefix="/authors", tags=["authors"])
app.include_router(publisher_router, prefix="/publishers", tags=["publishers"])
# app/api/api_router.py
#from fastapi import APIRouter
#from app.startup.router import router as registered_router

# Create the main API router
#api_router = APIRouter()

# Include all registered routers from `router.py`
#api_router.include_router(registered_router)

