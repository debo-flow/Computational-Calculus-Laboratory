import sympy as sp
from typing import Dict, Any

def get_polar_transformation() -> Dict[str, Any]:
    r, theta = sp.symbols('r theta')
    x_eq, y_eq = r * sp.cos(theta), r * sp.sin(theta)
    return {"Old": [sp.Symbol('x'), sp.Symbol('y')], "New": [r, theta], "Equations": [x_eq, y_eq], "Name": "Polar"}

def get_cylindrical_transformation() -> Dict[str, Any]:
    r, theta, z = sp.symbols('r theta z')
    x_eq, y_eq, z_eq = r * sp.cos(theta), r * sp.sin(theta), z
    return {"Old": [sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')], "New": [r, theta, z], "Equations": [x_eq, y_eq, z_eq], "Name": "Cylindrical"}

def get_spherical_transformation() -> Dict[str, Any]:
    rho, phi, theta = sp.symbols('rho phi theta') # Physics convention: phi = polar angle, theta = azimuthal
    x_eq = rho * sp.sin(phi) * sp.cos(theta)
    y_eq = rho * sp.sin(phi) * sp.sin(theta)
    z_eq = rho * sp.cos(phi)
    return {"Old": [sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')], "New": [rho, phi, theta], "Equations": [x_eq, y_eq, z_eq], "Name": "Spherical"}
