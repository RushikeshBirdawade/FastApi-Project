
# app/startup/router.py

from fastapi import APIRouter, Depends, HTTPException, status
from app.api.api_router import  api_router




router= APIRouter()

@router.get('/health-check', status_code=200)
def perform_healthcheck():
   return "OK"

router.include_router(api_router)


# app/startup/router.py
#from fastapi import APIRouter
#from app.api.book.book_routes import book_router
#from app.api.author.author_routes import author_router
#from app.api.publisher.publisher_routes import publisher_router

# Create a master router that aggregates all the sub-routers
#router = APIRouter()

# Register each sub-router with its respective prefix and tags
#router.include_router(book_router, prefix="/books", tags=["Books"])
#router.include_router(author_router, prefix="/authors", tags=["Authors"])
#router.include_router(publisher_router, prefix="/publishers", tags=["Publishers"])

