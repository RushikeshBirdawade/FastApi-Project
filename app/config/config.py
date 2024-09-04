from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:RR2602_1999@localhost:3306/passdb" #link add saturday

    class Config:
        env_file = ".env"

settings = Settings()

def get_settings():
    return Settings()