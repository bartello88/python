import pytest


@pytest.fixture
def variable(autouse=True) -> int:
    return 10


@pytest.mark.parametrize("item, number", [("A", 1), ("B", 2), ("C", 3)])
def test_parametrize(item, number):
    assert item in ["A", "B", "C"]
    assert number < 4


@pytest.fixture
def list_comp():
    words = ["name", "banana", "nice"]
    return [i for i in words if len(i) < 5]
