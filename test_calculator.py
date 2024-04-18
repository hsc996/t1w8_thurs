from calculator import add, subtract, division
import pytest

def test_basic():
    assert "hello" == "hello"

def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(2, 0) == 2
    assert add(5, -7) == -2

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(6, 2) == 4

def test_division():
    assert division(6, 2) == 3
    assert division(8, 2) == 4

def test_raise_error():
    with pytest.raises(Exception):
        division(2, 0)
        # To avoid throwing a ZeroDivisionError