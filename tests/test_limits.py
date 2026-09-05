import pytest
import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.limits.limit_engine import LimitEngine
from calculus.limits.numerical_limits import NumericalLimitEngine

def get_limits(expr_str: str, point: float):
    engine = FunctionEngine(expr_str)
    lim_engine = LimitEngine(engine)
    return lim_engine.evaluate_limits(point)

def test_polynomial_limit():
    res = get_limits("x^2 + 2*x", 3)
    assert res['Two-Sided Limit'] == 15

def test_rational_removable_limit():
    res = get_limits("(x^2 - 1)/(x - 1)", 1)
    assert res['Two-Sided Limit'] == 2

def test_sin_x_over_x():
    res = get_limits("sin(x)/x", 0)
    assert res['Two-Sided Limit'] == 1

def test_left_and_right_hand_limits():
    res = get_limits("Abs(x)/x", 0)
    assert res['Left-Hand Limit'] == -1
    assert res['Right-Hand Limit'] == 1
    assert res['Two-Sided Limit'] == "Does Not Exist"

def test_limit_at_infinity():
    res = get_limits("1/x", 'oo')
    assert res['Two-Sided Limit'] == 0

def test_limit_at_negative_infinity():
    res = get_limits("x/(x+1)", '-oo')
    assert res['Two-Sided Limit'] == 1

def test_infinite_behavior():
    res = get_limits("1/(x-1)^2", 1)
    assert res['Two-Sided Limit'] == sp.oo

def test_oscillatory_behavior():
    res = get_limits("sin(1/x)", 0)
    assert "AccumulationBounds" in str(res['Two-Sided Limit'])

def test_numerical_convergence_generation():
    engine = FunctionEngine("(1 + 1/x)^x")
    num_eng = NumericalLimitEngine(engine)
    table = num_eng.generate_infinity_table(positive_infinity=True, steps=2)
    
    assert len(table) == 2
    assert table[0]['x'] == 10
    assert table[1]['x'] == 100
    assert table[0]['f(x)'] < table[1]['f(x)'] # Approaching e
