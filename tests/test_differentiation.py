import pytest
import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine
from calculus.differentiation.numerical_derivative import NumericalDerivativeEngine
from calculus.differentiation.derivative_analysis import analyze_differentiability

def test_first_derivative():
    engine = FunctionEngine("x^3")
    dev_eng = DerivativeEngine(engine)
    assert dev_eng.get_derivative(1) == sp.sympify("3*x^2")
    assert dev_eng.evaluate_derivative(2, 1) == 12.0

def test_higher_order_derivative():
    engine = FunctionEngine("sin(x)")
    dev_eng = DerivativeEngine(engine)
    assert dev_eng.get_derivative(2) == sp.sympify("-sin(x)")

def test_implicit_differentiation():
    res = DerivativeEngine.implicit_differentiation("x^2 + y^2 = 25")
    # Result is -x/y
    assert str(res) == "-x/y"

def test_parametric_differentiation():
    res = DerivativeEngine.parametric_differentiation("cos(t)", "sin(t)")
    assert str(res["dx/dt"]) == "-sin(t)"
    assert str(res["dy/dx"]) == "-cos(t)/sin(t)"

def test_numerical_differentiation():
    engine = FunctionEngine("x^2")
    num_eng = NumericalDerivativeEngine(engine)
    res = num_eng.evaluate_all(2.0, h=0.01)
    assert pytest.approx(res["Central"], 0.0001) == 4.0

def test_differentiability_vs_continuity():
    # f(x) = |x| at x=0
    engine = FunctionEngine("Abs(x)")
    res = analyze_differentiability(engine, 0)
    assert res["Continuous"] == True
    assert res["Differentiable"] == False
    assert res["Classification"] == "Corner/Cusp"
