import pytest
from calculus.core.classifier import classify_problem
from calculus.core.pipeline import master_calculus_workflow
from calculus.core.calculus_engine import CalculusEngine

def test_auto_classifier():
    assert classify_problem("y'' + y = 0")["Engine"] == "ode"
    assert classify_problem("lim(sin(x)/x, x, 0)")["Engine"] == "limit"
    assert classify_problem("curl([x, y, z])")["Engine"] == "vector_calculus"

def test_master_workflow():
    report = master_calculus_workflow("x**2 + 2*x + 1")
    assert report["Detected Problem Type"] == "Expression / Function"
    assert "EXACT SYMBOLIC" in report["Result Classification"]

def test_calculus_engine_api():
    engine = CalculusEngine()
    diff_res = engine.differentiate("x**3", "x")
    assert str(diff_res) == "3*x**2"
    
    int_res = engine.integrate("2*x", "x")
    assert str(int_res) == "x**2"
    
    ver_res = engine.validate("x*x", "x^2")
    assert "VERIFIED" in ver_res["Status"]
