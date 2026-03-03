from utils import add_numbers,multiply_numbers

def test_add():
    assert add_numbers(2, 3) == 5

def test_add_negative():
    assert add_numbers(-1, -1) == -2

def test_multiply():
    assert multiply_numbers(3, 4) == 12