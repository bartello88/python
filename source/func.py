import logging
import datetime


date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%SZ")

logging.basicConfig(filename="logs.log", level=logging.INFO)
logger = logging.getLogger("app")

#%%#
def show_error(a: int) -> int:
    """
    Docstring: A new function
    :param a: Number
    : return: a
    """
    if a < 4:
        raise Exception("Not working")
    else:
        return a


def devide_by_zero(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError()

    try:
        logger.info(f"\n{date} Calculating the result: {a/b=}")
        logger.info("Everything went fine")
        return a / b
    except ZeroDivisionError as e:
        print(e)
    finally:
        logger.info("Done")
        print("Job done")


devide_by_zero()


# %%
