# test_calculator.py

import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(10, 10) == 0
    assert calculator.subtract(-3, -7) == 4

def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10
    assert calculator.multiply(0, 100) == 0

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(1, 1) == 1
    with pytest.raises(ValueError):  # Check for division by zero
        calculator.divide(5, 0)

# Logging results of test cases
if __name__ == "__main__":
    result = pytest.main(["-v", "--tb=short", "--result-log=test_results.log"])
    print(f"Test run completed with exit code {result}")
