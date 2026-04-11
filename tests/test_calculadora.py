import pytest

from Calculadora import add, divide, factorial, multiply, power, subtract


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 3.5, 6.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (0, 7, -7),
        (-5, -2, -3),
        (10.5, 0.5, 10.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (0, 10, 0),
        (-4, 2, -8),
        (1.5, 2, 3.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (7, 2, 3.5),
        (-9, 3, -3),
        (5.0, 2.0, 2.5),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (9, 0.5, 3.0),
        (-2, 2, 4),
    ],
)
def test_power(a, b, expected):
    assert power(a, b) == expected


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
        factorial(-1)
