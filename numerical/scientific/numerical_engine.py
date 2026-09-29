import numpy as np
from typing import Dict, Any

def solve_1d_heat_pde(L: float, T: float, Nx: int, Nt: int, alpha: float) -> Dict[str, Any]:
    """
    Finite Difference foundation for 1D Heat Equation: u_t = alpha * u_xx.
    Includes rigorous CFL Stability condition analysis.
    """
    x = np.linspace(0, L, Nx)
    dx = x[1] - x[0]
    dt = T / Nt
    
    # CFL Condition for explicit FTCS scheme
    cfl = alpha * dt / (dx**2)
    stable = cfl <= 0.5
    
    u = np.sin(np.pi * x / L) # Initial condition: u(x,0) = sin(pi*x/L)
    u_history = [u.copy()]
    
    if stable:
        for _ in range(Nt):
            u_new = u.copy()
            for i in range(1, Nx - 1):
                u_new[i] = u[i] + cfl * (u[i+1] - 2*u[i] + u[i-1])
            u = u_new
            u_history.append(u.copy())
            
    return {
        "x_grid": x.tolist(),
        "Time Steps": Nt,
        "dx": dx,
        "dt": dt,
        "CFL Stability Parameter": cfl,
        "Stable": stable,
        "Required dt Limit": (dx**2) / (2 * alpha),
        "u_final": u.tolist() if stable else [],
        "History": u_history if stable else []
    }
