from pydantic_settings import BaseSettings
from pydantic import ConfigDict

from pathlib import Path

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    LOG_LEVEL: str = "INFO"
    BACKEND_CORS_ORIGINS: list[str] = []
    
    FRONTEND_DIR: Path = Path(__file__).parent.parent.parent / "frontend"
    TEMPLATES_DIR: Path = FRONTEND_DIR / "templates"
    STATIC_DIR: Path = FRONTEND_DIR / "static"
    
    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")
    
settings = Settings()
