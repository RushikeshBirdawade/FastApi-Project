
from fastapi import FastAPI
from app.startup.application import create_app
from app.api.api_router import api_router

#app = create_app()

#app.include_router(api_router)

#@app.get("/")
#def read_root():
#    return {"message": "Welcome to the FastAPI application!"}

#app.include_router(router)

#from fastapi import FastAPI
#from app.api.api_router import api_router

def include_routers(app: FastAPI) -> None:
    app.include_router(api_router)


