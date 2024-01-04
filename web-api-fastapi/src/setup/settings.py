import os
from typing import Literal

from pydantic import BaseModel, BaseSettings


class Settings(BaseSettings):
    """Settings Setup"""

    # Script Logger
    LOG_LEVEL: Literal["DEV", "STAGING", "PROD"] = "DEV"

    class Config:
        app_env = os.environ["app_env"]
        env_file = f"config/.{app_env}"
        # env_file = ".env"
        env_file_encoding = "utf-8"
