import logging
import logging.config
from logging.handlers import RotatingFileHandler

# logging_config = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formaters": {
#         "default": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
#     },
#     "handlers": {
#         "console": {"class": "loging.StreamHandler", "formatter": "default"},
#         "file": {
#             "class": "logging.FileHandler",
#             "filename": "logs.log",
#             "formatter": "default",
#         },
#         "rotation_file": {
#             "class": "logging.RotationFileHandler",
#             "formatter": "default",
#             "filename": "db_logs.log",
#         },
#     },
#     "loggers": {
#         "my_app": {"level": "INFO", "handlers": ["file"], "propagate": False},
#         "my_app_database": {"level": "DEBUG", "handlers": "rotation_file"},
#     },
# }

# logging.config.dictConfig(logging_config)


def create_logger(
    name: str, filename: str, level=logging.INFO, handler=RotatingFileHandler
) -> object:

    logger = logging.getLogger(name)
    logger.setLevel(level)
    formtter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    if handler == logging.StreamHandler:
        logger_handler = handler()
    else:
        logger_handler = handler(filename, maxBytes=10000, backupCount=3)
    logger_handler.setFormatter(formtter)
    logger.addHandler(logger_handler)

    return logger
