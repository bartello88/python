import logging
import logging.handlers
from source.logger import create_logger


def frontend_function(frontedn_logger) -> None:
    new_session = "New session"
    frontedn_logger.info(f"{new_session:_^40}")
    frontedn_logger.info("This is frontend")
    frontedn_logger.warning("This is frontend")
    frontedn_logger.debug("This is frontend\n\n")
