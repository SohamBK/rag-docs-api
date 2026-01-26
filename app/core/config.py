from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "rag-docs-api"
    environment: str = "development"
    log_level: str = "INFO"

    #Database settings
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
