import pytest
from calculus.functions.function_engine import FunctionEngine
from numerical.integration.quadrature_engine import NumericalIntegrationEngine

def test_trapezoidal_rule():
    engine = FunctionEngine("x^2")
    num_int = NumericalIntegrationEngine(engine)
    res = num_int.execute_method("Trapezoidal", 0, 2, n=100)
    assert res["Status"] == "Success"
    assert pytest.approx(res["Approximation"], 1e-3) == 8/3

def test_simpson_13_rule():
    engine = FunctionEngine("sin(x)")
    num_int = NumericalIntegrationEngine(engine)
    res = num_int.execute_method("Simpson 1/3", 0, 3.14159265, n=10)
    assert res["Status"] == "Success"
    assert pytest.approx(res["Approximation"], 1e-4) == 2.0

def test_simpson_13_odd_n_fails():
    engine = FunctionEngine("x")
    num_int = NumericalIntegrationEngine(engine)
    res = num_int.execute_method("Simpson 1/3", 0, 1, n=5)
    assert res["Status"] == "Failed"
    assert "EVEN" in res["Reason"]

def test_simpson_38_rule():
    engine = FunctionEngine("exp(x)")
    num_int = NumericalIntegrationEngine(engine)
    res = num_int.execute_method("Simpson 3/8", 0, 1, n=6)
    assert res["Status"] == "Success"

def test_gaussian_quadrature():
    engine = FunctionEngine("x^3")
    num_int = NumericalIntegrationEngine(engine)
    # 2-point Gauss should integrate cubic exactly
    res = num_int.execute_method("Gauss-Legendre", 0, 2, n=2)
    assert pytest.approx(res["Approximation"], 1e-7) == 4.0

def test_adaptive_simpson():
    # Peaked function
    engine = FunctionEngine("exp(-100*x^2)")
    num_int = NumericalIntegrationEngine(engine)
    res = num_int.execute_method("Adaptive Simpson", -1, 1, tol=1e-5)
    assert res["Status"] == "Success"
    assert len(res["Subdivisions"]) > 0

def test_data_integration():
    engine = FunctionEngine("x")
    num_int = NumericalIntegrationEngine(engine)
    # y = x from 0 to 2
    res = num_int.data_integration([0, 1, 2], [0, 1, 2])
    assert pytest.approx(res) == 2.0
