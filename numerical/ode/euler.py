import numpy as np

def euler_step(f, x, y, h):
    """y_{n+1} = y_n + h * f(x_n, y_n)"""
    return y + h * f(x, y)
