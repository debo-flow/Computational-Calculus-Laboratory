import pytest
import sympy as sp
from calculus.vector_calculus.vector_engine import VectorFunctionEngine
from calculus.vector_calculus.vector_fields import VectorFieldEngine
from calculus.vector_calculus.vector_functions import compute_kinematics, compute_arc_length
from calculus.vector_calculus.divergence import compute_divergence
from calculus.vector_calculus.curl import compute_curl
from calculus.vector_calculus.line_integrals import vector_line_integral
from calculus.vector_calculus.flux import compute_flux

def test_kinematics():
    eng = VectorFunctionEngine(["t", "t^2", "t^3"])
    kin = compute_kinematics(eng)
    assert kin["Velocity (v)"] == [sp.sympify("1"), sp.sympify("2*t"), sp.sympify("3*t^2")]

def test_divergence():
    eng = VectorFieldEngine(["x^2", "y^2", "z^2"])
    div = compute_divergence(eng)
    assert sp.simplify(div - sp.sympify("2*x + 2*y + 2*z")) == 0

def test_curl():
    eng = VectorFieldEngine(["-y", "x", "0"])
    curl = compute_curl(eng)
    assert curl == [sp.S.Zero, sp.S.Zero, sp.sympify("2")]

def test_line_integral():
    field = VectorFieldEngine(["y", "x", "0"])
    curve = VectorFunctionEngine(["t", "t^2", "0"])
    res = vector_line_integral(field, curve, 0, 1)
    assert res["Status"] != "Failed"
    assert pytest.approx(res["Numerical"], 1e-4) == 1.0

def test_flux():
    field = VectorFieldEngine(["x", "y", "z"])
    # Surface of cylinder
    param = ["cos(u)", "sin(u)", "v"]
    res = compute_flux(field, param, "u, v", (0, 2*sp.pi), (0, 1))
    assert res["Status"] != "Failed"
    assert pytest.approx(res["Numerical"], 1e-4) == 6.2831853 # 2*pi

