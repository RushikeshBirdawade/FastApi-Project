# main.py

from fastapi import FastAPI
from app.startup.application import app
import uvicorn

#from app.startup.application import create_app

#app=create_app
#app = FastAPI(debug=True)

# Create FastAPI app
#def create_app():
#    app = FastAPI() 
#    return app
@app.get("/")
def read_root():
    return {"message": "Hello World"}

#app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
