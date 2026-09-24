import pytest
import numpy as np
import sympy as sp
from calculus.differential_equations.ode_analysis import classify_ode, compute_error_metrics, step_size_convergence_study
from calculus.differential_equations.numerical_solver import solve_fixed_step, solve_adaptive
from calculus.differential_equations.systems import create_numerical_system
from calculus.differential_equations.equilibrium import find_equilibria
from calculus.differential_equations.stability import analyze_stability

def test_ode_classification():
    res = classify_ode("y'' + 4*y = 0", 'y', 'x')
    assert res["Order"] == 2
    assert res["Linearity"] == "Linear"
    assert res["Homogeneity"] == "Homogeneous"
    assert res["Autonomous"] == "Autonomous"

def test_numerical_rk3_rk4():
    # y' = y. Exact y(1) = e
    f = lambda x, y: y
    x, y3, s3 = solve_fixed_step(f, 0, np.array([1.0]), 1.0, 0.1, 'RK3')
    x, y4, s4 = solve_fixed_step(f, 0, np.array([1.0]), 1.0, 0.1, 'RK4')
    
    assert s3 == "SUCCESS" and s4 == "SUCCESS"
    assert abs(y4[-1][0] - np.exp(1)) < abs(y3[-1][0] - np.exp(1)) # RK4 more accurate than RK3

def test_convergence_order():
    f = lambda x, y: y
    exact = lambda x: np.exp(x)
    # Midpoint should be O(h^2)
    study = step_size_convergence_study(f, exact, 0.0, np.array([1.0]), 1.0, 0.2, 'RK2 (Midpoint)')
    p_last = study[-1]["Experimental Order (p)"]
    if isinstance(p_last, float):
        assert pytest.approx(p_last, 0.2) == 2.0

def test_equilibrium_and_stability():
    # Lotka-Volterra
    sys = ["x - x*y", "x*y - y"]
    eq_pts = find_equilibria(sys, "x, y")
    assert [1.0, 1.0] in eq_pts
    stab = analyze_stability(sys, "x, y", [1.0, 1.0])
    assert "Center" in stab["Classification"]

def test_stiff_solver_adaptive():
    f = lambda t, y: -1000 * y
    t, y, status = solve_adaptive(f, 0, np.array([1.0]), 0.1, stiff=True)
    assert "SUCCESS" in status["Status"]
    assert "BDF" in status["Method"]
    assert pytest.approx(y[-1][0], 1e-2) == 0.0
