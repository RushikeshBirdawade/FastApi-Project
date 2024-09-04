
from fastapi import APIRouter, Depends, HTTPException, status
from app.api.api_router import router as api_router

router = APIRouter()

@router.get('/health-check', status_code=200)
def perform_healthcheck():
    return "OK"

# Add API outer here...
router.include_router(api_router)


