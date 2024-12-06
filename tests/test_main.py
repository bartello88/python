import pytest

from source.func import show_error
from source.func import devide_by_zero


@pytest.mark.test
def test_var(variable) -> None:
    assert variable == 10


def test_test(variable) -> None:
    assert variable == 10


# %%
def add_numbers(a: int, b: int) -> int:
    return a + b


# %%


def test_add_numbers():
    assert add_numbers(1, 4) == 5


def test_list_comp(list_comp):
    assert list_comp == ["name", "nice"]


def test_check_lenght():
    with pytest.raises(Exception):
        show_error(2)


def test_devide_by_zero():
    with pytest.raises(ValueError):
        devide_by_zero(5, -1)
