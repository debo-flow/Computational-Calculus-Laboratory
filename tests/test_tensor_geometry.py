import pytest
import sympy as sp
from calculus.tensor_geometry.metric import compute_metric_properties, raise_lower_index
from calculus.tensor_geometry.christoffel import compute_christoffel_symbols
from calculus.tensor_geometry.curvature import compute_riemann_tensor, compute_ricci_tensor, compute_scalar_curvature
from calculus.tensor_geometry.differential_geometry import compute_surface_geometry
from calculus.tensor_geometry.geometry_analysis import compute_exterior_derivative_1form

def test_euclidean_metric():
    g = sp.Matrix([[1, 0], [0, 1]])
    res = compute_metric_properties(g)
    assert res["Determinant (g)"] == 1
    assert res["g^ij"] == g

def test_polar_christoffel():
    # g = diag(1, r^2)
    r, th = sp.symbols('r theta')
    g = sp.Matrix([[1, 0], [0, r**2]])
    g_inv = g.inv()
    
    Gamma = compute_christoffel_symbols(g, g_inv, [r, th])
    # Gamma^r_{theta, theta} = -r
    assert sp.simplify(Gamma[0][1][1] - (-r)) == 0
    # Gamma^theta_{r, theta} = 1/r
    assert sp.simplify(Gamma[1][0][1] - (1/r)) == 0

def test_sphere_curvature():
    # Sphere of radius R
    # x = R cos(u) sin(v), y = R sin(u) sin(v), z = R cos(v)
    R_sym = sp.Symbol('R')
    x = R_sym * sp.cos(sp.Symbol('u')) * sp.sin(sp.Symbol('v'))
    y = R_sym * sp.sin(sp.Symbol('u')) * sp.sin(sp.Symbol('v'))
    z = R_sym * sp.cos(sp.Symbol('v'))
    
    res = compute_surface_geometry(str(x), str(y), str(z), "u, v")
    assert res["Status"] == "Success"
    # Gaussian curvature of sphere is 1/R^2
    assert sp.simplify(res["Gaussian Curvature (K)"] - (1 / R_sym**2)) == 0

def test_exterior_derivative():
    # omega = y dx + x dy + 0 dz
    res = compute_exterior_derivative_1form("y", "x", "0", "x, y, z")
    assert res["dx ∧ dy"] == 0 # Closed form d(omega) = 0
