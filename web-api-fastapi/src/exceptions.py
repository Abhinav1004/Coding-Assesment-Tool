from src.setup import LOGGER


class CustomException(Exception):
    """
    Custom Exception for Learning Phase API
    :param msg: error message
    """

    def __init__(self, msg: str):
        LOGGER.error(f"CustomException: {msg}")
        self.msg = msg
