import pytest
import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.continuity.continuity_engine import ContinuityEngine
from calculus.continuity.discontinuity import classify_discontinuity

def get_continuity(expr_str: str, point: float):
    engine = FunctionEngine(expr_str)
    cont_engine = ContinuityEngine(engine)
    return cont_engine.evaluate_point_continuity(str(point))

def test_continuous_polynomial():
    res = get_continuity("x^2 + 2", 2)
    assert res["Continuous"] == True
    assert res["f(a)"] == 6

def test_removable_discontinuity():
    res = get_continuity("(x^2 - 4)/(x - 2)", 2)
    assert res["Continuous"] == False
    assert res["f(a)"] == "Undefined"
    assert res["Limit"] == 4
    assert classify_discontinuity(res) == "Removable Discontinuity"

def test_jump_piecewise_discontinuity():
    # Use SymPy piecewise syntax
    res = get_continuity("Piecewise((x^2, x < 1), (x + 3, True))", 1)
    assert res["Continuous"] == False
    assert res["LHL"] == 1
    assert res["RHL"] == 4
    assert classify_discontinuity(res) == "Jump Discontinuity"

def test_infinite_discontinuity():
    res = get_continuity("1/(x-1)", 1)
    assert res["Continuous"] == False
    assert classify_discontinuity(res) == "Infinite Discontinuity"

def test_oscillatory_discontinuity():
    res = get_continuity("sin(1/x)", 0)
    assert res["Continuous"] == False
    assert classify_discontinuity(res) == "Oscillatory Discontinuity"

def test_left_right_continuity():
    res = get_continuity("Piecewise((x^2, x <= 1), (x + 3, True))", 1)
    # LHL is 1, f(1) is 1. RHL is 4.
    assert res["Left Continuous"] == True
    assert res["Right Continuous"] == False
