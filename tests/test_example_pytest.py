import pytest
from py_utils_knaier.core.classes import Dog


@pytest.fixture
def basic_dog():
    """Returns a Wallet instance with a zero balance"""
    return Dog('willie', 2)


def test_dog_age(basic_dog):
    assert basic_dog.age == 2


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
