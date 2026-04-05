from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://asyncqueue:asyncqueue@localhost:5432/asyncqueue"
    redis_url: str = "redis://localhost:6379"
    app_name: str = "AsyncQueue"
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()