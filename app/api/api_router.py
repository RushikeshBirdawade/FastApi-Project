from fastapi import APIRouter
from app.api.book.book_routes import book_router
from app.api.author.author_routes import author_router
from app.api.publisher.publisher_routes import  publisher_router

# Create an instance of APIRouter
api_router = APIRouter()

# Include the routes from the individual modules
api_router.include_router(book_router, prefix="/books", tags=["books"])
api_router.include_router(author_router, prefix="/authors", tags=["authors"])
api_router.include_router(publisher_router, prefix="/publishers", tags=["publishers"])

