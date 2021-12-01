from random_cli_framework import __version__
from random_cli_framework.logic import sum_of_xy


def test_version():
    assert __version__ == '0.1.0'


def test_sum_xy():
    result = sum_of_xy(10, 15)
    assert result == 25
