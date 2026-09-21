import pytest
import sympy as sp
import numpy as np
from calculus.differential_equations.ode_analysis import classify_single_ode
from calculus.differential_equations.symbolic_solutions import solve_symbolic_ode
from calculus.differential_equations.systems import convert_second_order_to_system
from calculus.differential_equations.equilibrium import find_equilibria
from calculus.differential_equations.stability import analyze_stability
from numerical.ode.rk4 import rk4_step, solve_fixed_step
from numerical.ode.adaptive import solve_adaptive_rk45

def test_ode_classification():
    res = classify_single_ode("y'' + 4*y = 0", 'y', 'x')
    assert res["Order"] == 2
    assert res["Is Autonomous"] is True

def test_symbolic_ivp():
    # y' = y, y(0) = 2 -> y = 2e^x
    res = solve_symbolic_ode("y' = y", ivp={"y(0)": 2})
    assert res["Status"] == "Success"
    assert res["Verified"] is True

def test_numerical_rk4():
    # dy/dx = y. Exact y(1) = e
    f = lambda x, y: y
    x, y, status = solve_fixed_step(f, 0, np.array([1.0]), 1.0, 0.01, 'RK4')
    assert status == "SUCCESS"
    assert pytest.approx(y[-1][0], 1e-4) == np.exp(1)

def test_adaptive_rk45():
    f = lambda x, y: y
    t, y, status = solve_adaptive_rk45(f, 0, np.array([1.0]), 1.0)
    assert status == "SUCCESS"
    assert pytest.approx(y[-1][0], 1e-4) == np.exp(1)

def test_higher_order_conversion():
    res = convert_second_order_to_system("-omega**2 * y")
    assert str(res["u1'"]) == "u2"
    assert str(res["u2'"]) == "-omega**2*u1"

def test_equilibrium_and_stability():
    # Predator-Prey (Lotka-Volterra)
    eqs = ["x - x*y", "x*y - y"]
    eqs_pts = find_equilibria(eqs, "x, y")
    assert [0.0, 0.0] in eqs_pts
    assert [1.0, 1.0] in eqs_pts
    
    stab = analyze_stability(eqs, "x, y", [0.0, 0.0])
    assert stab["Classification"] == "Saddle Point (Unstable)"
