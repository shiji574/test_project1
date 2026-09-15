import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_divide():
    assert divide(10, 2) == 5

def test_divide_zero_numerator():
    assert divide(0, 7) == 0

def test_divide_negative_operands():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5

def test_divide_fractional_result():
    assert divide(1, 2) == 0.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_by_negative_zero():
    with pytest.raises(ValueError):
        divide(10, -0.0)