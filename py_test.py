import pytest


@pytest.mark.usefixtures("add_numbers")
def test_compare_numbers():
    """ Testing"""
    x = 5
    y = 15

    assert x < y, "X is not less then Y"

@pytest.fixture
def add_numbers():
    """Adding two numbers"""
    print("Now adding two numbers:")

# pytest -sv /Users/qaisahmadi/Python/catagory.py -k "test"