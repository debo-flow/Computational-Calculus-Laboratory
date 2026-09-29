import sympy as sp
from typing import List

def generate_geodesic_odes(Gamma: list, vars_sym: List[sp.Symbol]) -> List[sp.Expr]:
    """Generates the RHS of the geodesic equation system: x^k'' = - Γ^k_ij x^i' x^j'"""
    dim = len(vars_sym)
    # Define first derivatives (velocities)
    vels = [sp.Symbol(f"v_{v}") for v in vars_sym]
    
    odes = []
    for k in range(dim):
        accel_k = sp.S.Zero
        for i in range(dim):
            for j in range(dim):
                accel_k -= Gamma[k][i][j] * vels[i] * vels[j]
        odes.append(sp.simplify(accel_k))
        
    return odes
