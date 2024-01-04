from .logger import Logger
from .settings import Settings

SETTINGS = Settings()
LOGGER = Logger(SETTINGS.LOG_LEVEL).setup_logger()

__all__ = ["SETTINGS", "LOGGER"]
