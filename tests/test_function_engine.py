import pytest
import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from numerical.validation import calculate_absolute_error, calculate_relative_error

def test_polynomial_evaluation():
    engine = FunctionEngine("x^2 + 2*x + 1")
    exact, num = engine.evaluate(3)
    assert num == 16.0

def test_trigonometric_evaluation():
    engine = FunctionEngine("sin(x)")
    exact, num = engine.evaluate(0)
    assert num == 0.0

def test_invalid_expression():
    with pytest.raises(ValueError):
        FunctionEngine("x^2 + +")

def test_division_by_zero():
    engine = FunctionEngine("1/x")
    exact, num = engine.evaluate(0)
    assert num == "Undefined/Infinity"

def test_symbolic_simplification():
    engine = FunctionEngine("x^2 + 2*x + 1")
    forms = engine.get_symbolic_representations()
    assert str(forms["Factorized"]) == "(x + 1)**2"

def test_numerical_validation():
    exact = 10.0
    approx = 9.9
    abs_err = calculate_absolute_error(exact, approx)
    rel_err = calculate_relative_error(exact, approx)
    
    assert pytest.approx(abs_err, 0.001) == 0.1
    assert pytest.approx(rel_err, 0.001) == 0.01
