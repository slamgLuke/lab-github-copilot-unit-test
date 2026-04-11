import pytest

from math_utils import factorial, generate_fibonacci


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (8, [0, 1, 1, 2, 3, 5, 8, 13]),
    ],
)
def test_generate_fibonacci(n, expected):
    assert generate_fibonacci(n) == expected


def test_generate_fibonacci_negative_raises_value_error():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci(-1)


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ],
)
def test_factorial(n, expected):
    assert factorial(n) == expected


def test_factorial_negative_raises_value_error():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        factorial(-3)
