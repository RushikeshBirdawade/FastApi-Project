# main.py
from fastapi import FastAPI 
#from app.database.database import Base, engine ,SessionLocal 
#from app.startup.application import create_app


from app.startup import router



app=FastAPI

#Base.metadata.create_all(bind=engine)

# Create FastAPI app
#app = create_app()

#app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
