from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost"]
    KEY: str = 'THmnCii5thUzdDYsAsrmClw_P9rA4ReIJozLlHUqehE'

    DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
