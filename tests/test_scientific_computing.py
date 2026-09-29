import pytest
import numpy as np
from numerical.scientific.precision import compare_precision
from numerical.scientific.linear_algebra import analyze_svd
from numerical.scientific.differentiation import richardson_extrapolation
from numerical.scientific.numerical_engine import solve_1d_heat_pde

def test_precision_comparison():
    res = compare_precision("exp(x)", 1.0, dps=50)
    assert "Standard Float (64-bit)" in res
    assert "High Precision (50 dps)" in res

def test_svd_analysis():
    A = [[1, 2], [3, 4]]
    res = analyze_svd(A)
    assert res["Rank Estimate"] == 2
    assert res["Reconstruction Error"] < 1e-10

def test_richardson_extrapolation():
    # f(x) = x^3. f'(2) = 12.
    f = lambda x: x**3
    res = richardson_extrapolation(f, 2.0, 0.1)
    assert abs(res["Richardson Extrapolation"] - 12.0) < 1e-10

def test_pde_cfl_stability():
    # Stable case
    res_stable = solve_1d_heat_pde(1.0, 0.1, 10, 100, 0.1)
    assert res_stable["Stable"] is True
    # Unstable case
    res_unstable = solve_1d_heat_pde(1.0, 0.1, 10, 10, 1.0)
    assert res_unstable["Stable"] is False
