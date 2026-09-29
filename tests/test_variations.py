import pytest
import sympy as sp
import numpy as np
from calculus.variations.functional import Functional
from calculus.variations.euler_lagrange import derive_euler_lagrange
from calculus.variations.variational_derivatives import compute_first_variation
from calculus.variations.numerical_variations import numerical_functional_optimization

def test_functional_evaluation():
    fnc = Functional("y^2 + yp^2")
    res = fnc.evaluate_trial_function("x^2", 0, 1)
    assert pytest.approx(res["Numerical J"], 1e-4) == (1/5 + 4/3)

def test_euler_lagrange_shortest_path():
    # J = int sqrt(1 + y'^2) dx. EL should be y'' = 0.
    fnc = Functional("sqrt(1 + yp**2)")
    el_data = derive_euler_lagrange(fnc)
    lhs = el_data["EL Equation"].lhs
    # Note: d/dx(yp / sqrt(1+yp^2)) simplifies to y'' / (yp^2+1)^(3/2). Numerator must be 0.
    assert "ypp" in str(lhs)

def test_first_variation():
    fnc = Functional("yp**2")
    var = compute_first_variation(fnc)
    assert "eta" in str(var["First Variation δF"])

def test_numerical_optimization():
    # Shortest path between (0,0) and (1,1). Should be y=x. J = sqrt(2)
    fnc = Functional("sqrt(1 + yp**2)")
    res = numerical_functional_optimization(fnc, 0, 1, 0, 1, N=20)
    assert res["Status"] == "Converged"
    assert pytest.approx(res["J_min"], 1e-2) == np.sqrt(2)
    # Midpoint should be 0.5
    mid_idx = len(res["y"]) // 2
    assert pytest.approx(res["y"][mid_idx], 1e-2) == 0.5
