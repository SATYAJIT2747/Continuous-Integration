import pytest

def square(x):
    return x * x
def cube(x):
    return x * x * x
def fifth_power(x):
    return x * x * x * x * x
def test_square():
    assert square(2) == 4 , "Test failed: square(2) should be 4"
def test_cube():
    assert cube(2) == 8 , "Test failed: cube(2) should be 8"
def test_fifth_power():
    assert fifth_power(2) == 32 , "Test failed: fifth_power(2) should be 32"
    # Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")