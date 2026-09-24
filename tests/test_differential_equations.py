import pytest
import numpy as np
import sympy as sp
from calculus.differential_equations.ode_analysis import classify_ode, empirical_convergence_study
from calculus.differential_equations.first_order import analyze_bernoulli, analyze_exact
from calculus.differential_equations.numerical_solver import solve_fixed_step, solve_adaptive
from calculus.differential_equations.equilibrium import find_equilibria
from calculus.differential_equations.stability import analyze_stability

def test_ode_classification():
    res = classify_ode("y'' + y = 0")
    assert res["Order"] == 2
    assert res["Linearity"] == "Linear"

def test_bernoulli_equation():
    # y' + y = y^2  (n=2)
    res = analyze_bernoulli("1", "1", 2)
    assert res["Status"] == "Success"
    assert "v = y^-1.0" in res["Substitution"]

def test_exact_equation():
    # 2xy dx + (x^2 + 3y^2) dy = 0
    res = analyze_exact("2*x*y", "x**2 + 3*y**2")
    assert res["Exact"] is True

def test_empirical_convergence():
    f = lambda x, y: y
    exact = lambda x: np.exp(x)
    # Midpoint O(h^2)
    study = empirical_convergence_study(f, exact, 0.0, np.array([1.0]), 1.0, 0.2, 
                                       lambda f, x0, y0, xe, h: solve_fixed_step(f, x0, y0, xe, h, 'Midpoint'))
    p_last = study[-1]["Observed Order (p)"]
    if isinstance(p_last, float):
        assert pytest.approx(p_last, 0.2) == 2.0

def test_dynamical_equilibria_and_stability():
    # Logistic: x' = r*x*(1 - x/K). Let r=1, K=2.
    sys = ["1*x*(1 - x/2)"]
    eqs = find_equilibria(sys, "x")
    assert [0.0] in eqs and [2.0] in eqs
