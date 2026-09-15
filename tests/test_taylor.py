import pytest
import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.taylor.taylor_engine import TaylorEngine

def test_maclaurin_exp():
    engine = FunctionEngine("exp(x)")
    taylor = TaylorEngine(engine, a=0)
    T_3 = taylor.get_polynomial(3)
    assert sp.simplify(T_3 - sp.sympify("1 + x + x^2/2 + x^3/6")) == 0

def test_taylor_arbitrary_point():
    engine = FunctionEngine("ln(x)")
    taylor = TaylorEngine(engine, a=1)
    T_2 = taylor.get_polynomial(2)
    assert sp.simplify(T_2 - sp.sympify("(x-1) - (x-1)^2/2")) == 0

def test_symbolic_verification():
    engine = FunctionEngine("sin(x)")
    taylor = TaylorEngine(engine, a=0)
    ver = taylor.verify_polynomial(3)
    assert ver["All Verified"] is True

def test_radius_of_convergence():
    engine = FunctionEngine("1/(1-x)")
    taylor = TaylorEngine(engine, a=0)
    roc = taylor.get_convergence()
    assert roc["R"] == 1

def test_lagrange_remainder():
    engine = FunctionEngine("cos(x)")
    taylor = TaylorEngine(engine, a=0)
    res = taylor.get_remainder_analysis(0.5, 2)
    assert res["Status"] == "Success"
    assert res["Actual Error"] < res["Lagrange Error Bound"]

def test_target_order_estimation():
    engine = FunctionEngine("exp(x)")
    taylor = TaylorEngine(engine, a=0)
    res = taylor.find_target_order(1.0, 1e-4) # Target e^1 to 4 decimals
    assert res["Status"] == "Success"
    assert res["Target Order"] <= 10 # e^1 usually converges around n=7 or 8 for 1e-4
