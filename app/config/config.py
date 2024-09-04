from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://priya:password@localhost:3306/book_service_db" #link add saturday

    class Config:
        env_file = ".env"

settings = Settings()

def get_settings():
    return Settings()