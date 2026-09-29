import sympy as sp

def compute_christoffel_symbols(g: sp.Matrix, g_inv: sp.Matrix, vars_sym: List[sp.Symbol]) -> list:
    """Γ^k_ij = 1/2 * g^{kl} (∂_i g_{jl} + ∂_j g_{il} - ∂_l g_{ij})"""
    dim = len(vars_sym)
    Gamma = [[[sp.S.Zero for _ in range(dim)] for _ in range(dim)] for _ in range(dim)]
    
    for k in range(dim):
        for i in range(dim):
            for j in range(dim):
                term = sp.S.Zero
                for l in range(dim):
                    term += g_inv[k, l] * (sp.diff(g[j, l], vars_sym[i]) + 
                                           sp.diff(g[i, l], vars_sym[j]) - 
                                           sp.diff(g[i, j], vars_sym[l]))
                Gamma[k][i][j] = sp.simplify(term / 2)
    return Gamma
