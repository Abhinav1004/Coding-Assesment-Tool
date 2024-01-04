import logging


class Logger:
    """Logger Setup"""

    def __init__(self, log_level: str = "DEV"):
        # Initializing the log level from settings file
        if log_level == "DEV":
            self.log_level = logging.DEBUG
        elif log_level == "STAGING":
            self.log_level = logging.WARNING
        else:
            self.log_level = logging.ERROR

    def setup_logger(self):
        """Setup Logger for the application"""
        # creating the logger
        logger = logging.getLogger("distance-engine")
        logger.setLevel(self.log_level)

        # Adding basic logging format for easier reading
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=self.log_level,
        )

        return logger
