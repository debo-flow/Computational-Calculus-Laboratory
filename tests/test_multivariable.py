import pytest
import sympy as sp
from calculus.multivariable.multivariable_engine import MultivariableEngine
from calculus.multivariable.partial_derivatives import compute_partial, compare_mixed_partials
from calculus.multivariable.gradient import compute_gradient, evaluate_gradient
from calculus.multivariable.tangent_plane import compute_tangent_plane
from calculus.multivariable.jacobian import compute_jacobian
from calculus.multivariable.critical_points import find_multivariable_critical_points
from calculus.multivariable.multiple_integrals import double_integral_rectangular

def test_multivariable_evaluation():
    eng = MultivariableEngine("x^2 + y^2", "x, y")
    assert eng.evaluate([2, 3]) == 13.0

def test_partial_derivatives():
    eng = MultivariableEngine("x^2 * y", "x, y")
    x, y = eng.vars
    assert sp.simplify(compute_partial(eng, [x]) - sp.sympify("2*x*y")) == 0

def test_gradient():
    eng = MultivariableEngine("x*y", "x,y")
    grad = evaluate_gradient(eng, [2, 3])
    assert grad["Gradient Vector"] == [3.0, 2.0]

def test_tangent_plane():
    eng = MultivariableEngine("x^2 + y^2", "x, y")
    res = compute_tangent_plane(eng, [1, 1])
    # z = 2 + 2(x-1) + 2(y-1) = 2x + 2y - 2
    assert sp.simplify(res["Tangent Plane Equation"] - sp.sympify("2*x + 2*y - 2")) == 0

def test_jacobian():
    res = compute_jacobian(["r*cos(theta)", "r*sin(theta)"], "r, theta")
    assert sp.simplify(res["Determinant"] - sp.sympify("r")) == 0

def test_critical_points():
    eng = MultivariableEngine("x^2 + y^2", "x, y")
    crits = find_multivariable_critical_points(eng)
    assert len(crits) == 1
    assert crits[0]["Point"] == [0.0, 0.0]
    assert crits[0]["Classification"]["Result"] == "Local Minimum"

def test_double_integral():
    eng = MultivariableEngine("x*y", "x, y")
    res = double_integral_rectangular(eng, (0, 1), (0, 1))
    assert res["Numerical Value"] == 0.25
