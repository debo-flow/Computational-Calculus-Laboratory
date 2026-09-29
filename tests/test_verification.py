import pytest
import sympy as sp
from calculus.verification.symbolic_verification import verify_symbolic_identity
from calculus.verification.numerical_verification import search_counterexample
from calculus.verification.theorem_verification import verify_greens_theorem
from calculus.verification.error_analysis import calculate_errors

def test_symbolic_identity():
    res = verify_symbolic_identity("sin(x)**2 + cos(x)**2", "1")
    assert res["Status"] == "SYMBOLICALLY VERIFIED"
    
    res2 = verify_symbolic_identity("x^2", "x")
    assert "NOT VERIFIED" in res2["Status"]

def test_counterexample_search():
    # False claim: (x+y)^2 = x^2 + y^2
    res = search_counterexample("(x+y)**2", "x**2 + y**2", "x, y", [(1, 5), (1, 5)])
    assert res["Status"] == "COUNTEREXAMPLE FOUND"

def test_greens_theorem_verification():
    # P = -y, Q = x. Curl = 2. Area of [0,1]x[0,1] is 1. LHS = RHS = 2.
    res = verify_greens_theorem("-y", "x", (0, 1), (0, 1))
    assert res["Status"] == "SYMBOLICALLY VERIFIED"
    assert res["Difference"] == 0

def test_error_analysis():
    err = calculate_errors([1.01], [1.00])
    assert pytest.approx(err["Max Absolute Error"], 1e-7) == 0.01
    assert pytest.approx(err["Max Relative Error"], 1e-7) == 0.01
