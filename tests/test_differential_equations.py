import pytest
import numpy as np
import sympy as sp
from calculus.differential_equations.second_order import analyze_constant_coeff_linear
from calculus.differential_equations.systems import analyze_matrix_system
from calculus.differential_equations.ode_analysis import verify_conservation
from numerical.ode_solvers import solve_fixed_step, solve_adaptive

def test_characteristic_equation():
    # y'' + 3y' + 2y = 0 => r^2 + 3r + 2 = 0. Roots -1, -2.
    res = analyze_constant_coeff_linear(1, 3, 2)
    assert res["Root Classification"] == "Distinct Real Roots"
    assert set(res["Roots"]) == {-1, -2}

def test_matrix_system():
    # Simple Harmonic Oscillator as matrix: [0, 1; -1, 0]
    A = [[0, 1], [-1, 0]]
    res = analyze_matrix_system(A)
    assert res["Classification"] == "Center (Marginally Stable)"
    assert res["Trace"] == 0
    assert res["Determinant"] == 1

def test_conservation_verification():
    # Pendulum: x' = y, y' = -sin(x). Energy: E = 0.5*y^2 - cos(x)
    sys = ["y", "-sin(x)"]
    res = verify_conservation(sys, "x, y", "0.5*y**2 - cos(x)")
    assert res["Is Conserved"] is True

def test_stiff_solver():
    # Stiff test scalar: y' = -1000y, y(0)=1
    f = lambda t, y: -1000 * y
    t, y, status = solve_adaptive(f, 0, np.array([1.0]), 0.1, stiff=True)
    assert "BDF" in status
    assert pytest.approx(y[-1][0], 1e-2) == 0.0 # Should decay instantly
