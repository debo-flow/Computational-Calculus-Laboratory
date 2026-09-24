import pytest
import numpy as np
import sympy as sp
from calculus.differential_equations.ode_analysis import classify_single_ode, parameter_sweep_equilibria
from calculus.differential_equations.numerical_solvers import run_convergence_study
from calculus.differential_equations.phase_space import compute_nullclines

def test_ode_classification_details():
    res = classify_single_ode("y'' + 4*y = 0", 'y', 'x')
    assert res["Order"] == 2
    assert res["Linear"] is True
    assert res["Homogeneous"] is True

def test_convergence_study():
    # y' = y. Exact y(1) = e^1. Check RK4 p~4
    f = lambda x, y: y
    exact = lambda x: np.exp(x)
    study = run_convergence_study(f, exact, 0.0, np.array([1.0]), 1.0, 0.2, 'RK4')
    
    assert len(study) == 4
    p_last = study[-1]["Observed Order (p)"]
    if isinstance(p_last, float):
        assert pytest.approx(p_last, 0.5) == 4.0 # RK4 is O(h^4)

def test_parameter_sweep():
    # dx/dt = mu*x - x^3
    sys = ["mu*x - x**3"]
    sweep = parameter_sweep_equilibria(sys, "x", "mu", [-1.0, 1.0])
    
    # For mu=-1, x=0 is only real equilibrium
    assert len(sweep[0]["Equilibria"]) == 1
    # For mu=1, x=0, 1, -1
    assert len(sweep[1]["Equilibria"]) == 3
