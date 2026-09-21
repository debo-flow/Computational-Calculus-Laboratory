import numpy as np

def heun_step(f, x, y, h):
    """Improved Euler (Heun's Method)"""
    k1 = f(x, y)
    k2 = f(x + h, y + h * k1)
    return y + (h / 2.0) * (k1 + k2)
