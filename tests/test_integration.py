import pytest
import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.integration.integral_engine import IntegralEngine
from calculus.integration.indefinite_integrals import compute_indefinite_integral
from calculus.integration.definite_integrals import compute_definite_integral
from calculus.integration.improper_integrals import evaluate_improper_integral
from calculus.integration.integral_analysis import (
    compute_riemann_sum,
    riemann_convergence_series,
    verify_fundamental_theorem_part1,
    verify_fundamental_theorem_part2,
    area_between_curves,
    integration_by_parts,
    partial_fractions_decomposition
)

def test_polynomial_indefinite_integral():
    engine = FunctionEngine("x^2 + 3*x")
    res = compute_indefinite_integral(engine)
    assert res["Verified"] is True
    assert sp.simplify(res["Antiderivative"] - (sp.sympify("x**3/3 + 3*x**2/2"))) == 0
    assert "+ C" in str(res["FullWithConstant"])

def test_constant_integral():
    engine = FunctionEngine("5")
    res = compute_indefinite_integral(engine)
    assert res["Verified"] is True
    assert sp.simplify(res["Antiderivative"] - sp.sympify("5*x")) == 0

def test_trigonometric_integral():
    engine = FunctionEngine("cos(x)")
    res = compute_indefinite_integral(engine)
    assert res["Verified"] is True
    assert sp.simplify(res["Antiderivative"] - sp.sin(engine.x)) == 0

def test_exponential_integral():
    engine = FunctionEngine("exp(x)")
    res = compute_indefinite_integral(engine)
    assert res["Verified"] is True
    assert sp.simplify(res["Antiderivative"] - sp.exp(engine.x)) == 0

def test_logarithmic_integral():
    engine = FunctionEngine("ln(x)")
    res = compute_indefinite_integral(engine)
    assert res["Verified"] is True
    assert sp.simplify(res["Antiderivative"] - sp.sympify("x*ln(x) - x")) == 0

def test_definite_integral():
    engine = FunctionEngine("sin(x)")
    res = compute_definite_integral(engine, 0, sp.pi)
    assert pytest.approx(res["Numerical"], 1e-6) == 2.0

def test_reversed_bounds():
    engine = FunctionEngine("x")
    res = compute_definite_integral(engine, 2, 0)
    assert res["ReversedBounds"] is True
    assert pytest.approx(res["Numerical"], 1e-6) == -2.0

def test_area_under_curve():
    engine = FunctionEngine("x")
    res = compute_definite_integral(engine, -1, 1)
    assert pytest.approx(res["SignedArea"], 1e-6) == 0.0
    assert pytest.approx(res["GeometricArea"], 1e-6) == 1.0

def test_area_between_curves():
    e1 = FunctionEngine("x")
    e2 = FunctionEngine("x^2")
    res = area_between_curves(e1, e2, 0, 1)
    assert pytest.approx(res["GeometricArea"], 1e-6) == 1/6

def test_left_riemann_sum():
    engine = FunctionEngine("x")
    res = compute_riemann_sum(engine, 0, 2, 2, method='left')
    assert pytest.approx(res["Approximation"], 1e-6) == 1.0

def test_right_riemann_sum():
    engine = FunctionEngine("x")
    res = compute_riemann_sum(engine, 0, 2, 2, method='right')
    assert pytest.approx(res["Approximation"], 1e-6) == 3.0

def test_midpoint_riemann_sum():
    engine = FunctionEngine("x")
    res = compute_riemann_sum(engine, 0, 2, 2, method='midpoint')
    assert pytest.approx(res["Approximation"], 1e-6) == 2.0

def test_riemann_convergence():
    engine = FunctionEngine("x^2")
    series = riemann_convergence_series(engine, 0, 1, [4, 16, 64])
    assert series[0]["Absolute Error"] > series[-1]["Absolute Error"]

def test_fundamental_theorem_part1():
    engine = FunctionEngine("x^3")
    res = verify_fundamental_theorem_part1(engine, 0)
    assert res["IdentityHolds"] is True

def test_fundamental_theorem_part2():
    engine = FunctionEngine("x^2")
    res = verify_fundamental_theorem_part2(engine, 0, 3)
    assert res["IdentityHolds"] is True
    assert pytest.approx(res["DefiniteIntegral"], 1e-6) == 9.0

def test_substitution():
    # ∫ 2x * exp(x^2) dx = exp(x^2)
    engine = FunctionEngine("2*x*exp(x^2)")
    res = compute_indefinite_integral(engine)
    assert res["Verified"] is True

def test_integration_by_parts():
    res = integration_by_parts("x", "exp(x)")
    assert sp.simplify(res["Result"] - sp.sympify("x*exp(x) - exp(x)")) == 0

def test_partial_fractions():
    res = partial_fractions_decomposition("1/(x^2 - 1)")
    assert sp.simplify(res["Decomposition"] - sp.sympify("1/(2*(x-1)) - 1/(2*(x+1))")) == 0

def test_trigonometric_integration():
    engine = FunctionEngine("sin(x)*cos(x)")
    res = compute_indefinite_integral(engine)
    assert res["Verified"] is True

def test_improper_integral():
    res = evaluate_improper_integral("1/x^2", 1, "oo")
    assert res["Classification"] == "Convergent"
    assert pytest.approx(float(res["Numerical"]), 1e-6) == 1.0

def test_piecewise_integration():
    x = sp.Symbol('x')
    pw = sp.Piecewise((x, x < 1), (1, True))
    integral_val = sp.integrate(pw, (x, 0, 2))
    assert pytest.approx(float(integral_val), 1e-6) == 1.5

def test_invalid_input():
    with pytest.raises(Exception):
        FunctionEngine("x^2 +")
