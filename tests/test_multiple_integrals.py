import pytest
import sympy as sp
from calculus.multivariable.multivariable_engine import MultivariableEngine
from calculus.multiple_integrals.double_integrals import compute_double_integral, change_integration_order
from calculus.multiple_integrals.triple_integrals import compute_triple_integral
from calculus.multiple_integrals.jacobian_integration import apply_coordinate_transformation
from calculus.multiple_integrals.coordinate_transformations import get_polar_transformation
from calculus.multiple_integrals.applications import compute_lamina_properties
from calculus.multiple_integrals.multiple_integral_analysis import monte_carlo_double_integral

def test_double_integral_rectangular():
    eng = MultivariableEngine("x * y", "x, y")
    res = compute_double_integral(eng, (0, 1), (0, 1))
    assert res["Status"] == "Success"
    assert pytest.approx(res["Numerical Result"], 1e-5) == 0.25

def test_change_of_order():
    eng = MultivariableEngine("x^2 + y", "x, y")
    res = change_integration_order(eng, (0, 2), (1, 3))
    assert res["Fubini Theorem Holds"] is True

def test_triple_integral():
    eng = MultivariableEngine("x * y * z", "x, y, z")
    res = compute_triple_integral(eng, (0, 1), (0, 1), (0, 1))
    assert res["Status"] == "Success"
    assert pytest.approx(res["Numerical Result"], 1e-5) == 0.125

def test_polar_jacobian():
    eng = MultivariableEngine("x^2 + y^2", "x, y")
    trans = get_polar_transformation()
    res = apply_coordinate_transformation(eng.expression, trans)
    # x^2 + y^2 -> r^2. Jacobian = r. Integrand -> r^3
    assert sp.simplify(res["Final Integrand f(u,v)|J|"] - sp.sympify("r^3")) == 0

def test_lamina_properties():
    # Uniform density rho=1 over [0,1]x[0,1]. Mass should be 1. Centroid (0.5, 0.5)
    res = compute_lamina_properties("1", (0, 1), (0, 1))
    assert res["Status"] == "Success"
    assert res["Mass (M)"] == 1
    assert res["Centroid (x_bar, y_bar)"] == (0.5, 0.5)

def test_monte_carlo():
    eng = MultivariableEngine("x * y", "x, y")
    res = monte_carlo_double_integral(eng, (0, 1), (0, 1), N=10000)
    assert res["Status"] == "Success"
    # Estimate should be close to 0.25
    assert abs(res["Estimate"] - 0.25) < 0.05
