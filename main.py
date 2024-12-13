import logging
from logging.handlers import SysLogHandler
import datetime
import os

from dotenv import load_dotenv, dotenv_values

from source.frontend import frontend_function
from source.frontend import create_logger


load_dotenv()
config_variables = dotenv_values(".env")


date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%SZ")

logging.basicConfig(filename="logs.log", level=logging.INFO)
logger = logging.getLogger("app")


def show_error(a: int) -> int:
    if a < 4:
        raise Exception("Not working")
    else:
        return a


LOGIN = config_variables["LOGIN"]
PASSWORD = config_variables["PASSWORD"]


def login_azure(login, password) -> None:
    if login and password:
        print("logged successfully")
    else:
        print("Missing credencials")


def login_to_azure(login: str, password: str) -> None:
    print("Login has benn logged")


login_to_azure(LOGIN, PASSWORD)


def logging_examples() -> None:

    logger = create_logger("Test_Loger", "logger.log", "INFO")
    logger.info("asdasd")
    console_logger = create_logger(
        "Test_console", "frontend.log", "INFO", handler=logging.StreamHandler
    )
    console_logger.info("asdasdasd")


logging_examples()
frontnd_logger = create_logger("Frontend_App", "frontend.log", "DEBUG")
frontend_function(frontnd_logger)

a = 10
b = 20
c = 10
sdfsdfsf = 234
