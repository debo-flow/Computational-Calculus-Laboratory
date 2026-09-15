from .polynomial import TaylorPolynomial
from .remainder import calculate_remainder_bounds

def estimate_order_for_tolerance(poly: TaylorPolynomial, x_eval: float, tol: float, max_order: int = 30) -> dict:
    """Iteratively finds the minimum order n required to meet target tolerance."""
    history = []
    
    for n in range(max_order + 1):
        res = calculate_remainder_bounds(poly, x_eval, n)
        if res["Status"] == "Failed":
            return {"Status": "Failed", "Reason": "Function evaluation failed."}
            
        actual_err = res["Actual Error"]
        history.append({"Order": n, "Actual Error": actual_err})
        
        if actual_err < tol:
            return {"Status": "Success", "Target Order": n, "Actual Error": actual_err, "History": history}
            
    return {"Status": "Failed (Max Order Reached)", "Best Order": max_order, "History": history}
