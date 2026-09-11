import pytest
from calculus.functions.function_engine import FunctionEngine
from calculus.applications.critical_points import find_critical_points
from calculus.applications.extrema import classify_local_extrema, find_absolute_extrema
from numerical.root_finding import newton_raphson

def test_critical_points():
    engine = FunctionEngine("x^2")
    pts = find_critical_points(engine)
    assert len(pts) == 1
    assert pytest.approx(pts[0], 0.01) == 0.0

def test_local_extrema():
    engine = FunctionEngine("x^2")
    res = classify_local_extrema(engine)
    assert list(res.values())[0] == "Local Minimum"

def test_absolute_extrema():
    engine = FunctionEngine("x^2")
    res = find_absolute_extrema(engine, -2, 3)
    assert res["Absolute Maximum"]["x"] == 3
    assert res["Absolute Minimum"]["x"] == 0

def test_newtons_method():
    engine = FunctionEngine("x^2 - 4")
    res = newton_raphson(engine, x0=3.0)
    assert res["Status"] == "Converged"
    assert pytest.approx(res["Root"], 0.001) == 2.0
