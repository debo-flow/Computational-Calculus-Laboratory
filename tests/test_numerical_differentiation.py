import pytest
from calculus.functions.function_engine import FunctionEngine
from numerical.differentiation.finite_difference import STENCILS
from numerical.differentiation.derivative_approximations import apply_stencil, differentiate_discrete_data
from numerical.differentiation.convergence_analysis import richardson_extrapolation
from numerical.differentiation.differentiation_engine import NumericalDifferentiationEngine

def test_finite_difference_stencils():
    engine = FunctionEngine("x^2")
    # Central difference f'(2) for x^2 should be 4
    res = apply_stencil(engine, 2.0, 0.01, STENCILS["Central (2nd Order)"])
    assert pytest.approx(res, 0.0001) == 4.0
    
    # 2nd Derivative Central f''(2) for x^2 should be 2
    res2 = apply_stencil(engine, 2.0, 0.01, STENCILS["Central 2nd Derivative"])
    assert pytest.approx(res2, 0.0001) == 2.0

def test_richardson_extrapolation():
    engine = FunctionEngine("exp(x)")
    res = richardson_extrapolation(engine, 1.0, 0.1)
    assert res["Status"] == "Success"
    # Extrapolated should be extremely close to e^1
    import math
    assert abs(res["Extrapolated (O(h^4))"] - math.exp(1)) < 1e-6

def test_discrete_data_differentiation():
    x_data = [0.0, 1.0, 2.0]
    y_data = [0.0, 1.0, 4.0] # y = x^2
    derivs = differentiate_discrete_data(x_data, y_data)
    
    assert pytest.approx(derivs[0], 0.1) == 1.0 # Edge forward
    assert pytest.approx(derivs[1], 0.1) == 2.0 # Interior central
    assert pytest.approx(derivs[2], 0.1) == 3.0 # Edge backward

def test_adaptive_step_size():
    engine = FunctionEngine("sin(x)")
    num_eng = NumericalDifferentiationEngine(engine)
    res = num_eng.adaptive_step_size(0.0)
    assert res["Status"] == "Converged"
    assert pytest.approx(res["Approximation"], 1e-4) == 1.0
