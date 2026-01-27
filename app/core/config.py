from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "rag-docs-api"
    environment: str = "development"
    log_level: str = "INFO"

    #Database settings
    DATABASE_URL: str

    # Gemini LLM settings
    GEMINI_API_KEY: str
    GEMINI_API_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
