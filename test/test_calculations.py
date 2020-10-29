import pytest

try:
    from calculations.add_numbers import add_numbers
except ImportError:
    print("Fix imports to project style!")


def test_add_numbers():

    assert add_numbers(2, 4) == 6




