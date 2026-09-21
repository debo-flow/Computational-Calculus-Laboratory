import numpy as np

def midpoint_step(f, x, y, h):
    """Midpoint Method (RK2)"""
    k1 = f(x, y)
    k2 = f(x + h/2.0, y + (h/2.0) * k1)
    return y + h * k2
