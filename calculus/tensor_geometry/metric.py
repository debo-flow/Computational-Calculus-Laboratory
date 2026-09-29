import sympy as sp
from typing import Dict, Any

def compute_metric_properties(g_matrix: sp.Matrix) -> Dict[str, Any]:
    """Calculates the inverse metric g^{ij} and the determinant g."""
    try:
        g_det = sp.simplify(g_matrix.det())
        if g_det == 0:
            return {"Status": "Failed", "Error": "Singular metric (Determinant is 0)."}
            
        g_inv = sp.simplify(g_matrix.inv())
        return {
            "Status": "Success",
            "g_ij": g_matrix,
            "g^ij": g_inv,
            "Determinant (g)": g_det
        }
    except Exception as e:
        return {"Status": "Failed", "Error": str(e)}

def raise_lower_index(tensor_comp: sp.Matrix, metric_comp: sp.Matrix) -> sp.Matrix:
    """Raises or lowers a vector index via contraction with the metric: V_i = g_ij V^j"""
    return sp.simplify(metric_comp * tensor_comp)
