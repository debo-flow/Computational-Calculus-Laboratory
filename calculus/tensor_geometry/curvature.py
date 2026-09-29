import sympy as sp
from typing import List, Dict

def compute_riemann_tensor(Gamma: list, vars_sym: List[sp.Symbol]) -> list:
    """R^i_jkl = ∂_k Γ^i_lj - ∂_l Γ^i_kj + Γ^i_km Γ^m_lj - Γ^i_lm Γ^m_kj"""
    dim = len(vars_sym)
    R = [[[[sp.S.Zero for _ in range(dim)] for _ in range(dim)] for _ in range(dim)] for _ in range(dim)]
    
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for l in range(dim):
                    term = sp.diff(Gamma[i][l][j], vars_sym[k]) - sp.diff(Gamma[i][k][j], vars_sym[l])
                    for m in range(dim):
                        term += Gamma[i][k][m] * Gamma[m][l][j] - Gamma[i][l][m] * Gamma[m][k][j]
                    R[i][j][k][l] = sp.simplify(term)
    return R

def compute_ricci_tensor(R_tensor: list, dim: int) -> sp.Matrix:
    """R_ij = R^k_ikj (Contraction of Riemann tensor)"""
    Ricci = sp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            term = sum(R_tensor[k][i][k][j] for k in range(dim))
            Ricci[i, j] = sp.simplify(term)
    return Ricci

def compute_scalar_curvature(Ricci: sp.Matrix, g_inv: sp.Matrix, dim: int) -> sp.Expr:
    """R = g^{ij} R_{ij}"""
    scalar_R = sp.S.Zero
    for i in range(dim):
        for j in range(dim):
            scalar_R += g_inv[i, j] * Ricci[i, j]
    return sp.simplify(scalar_R)
