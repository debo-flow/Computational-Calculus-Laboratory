def classify_integration_reliability(exact: float, approx: float, method_status: str, evals: int) -> str:
    if method_status == "Failed":
        return "FAILED (Singularity or Numerical Exception)"
        
    if exact is None:
        return "CAUTION (No exact reference available to confirm accuracy)"
        
    err = abs(exact - approx)
    rel_err = err / abs(exact) if exact != 0 else err
    
    if rel_err < 1e-5:
        return "RELIABLE"
    if rel_err < 1e-2:
        return "CAUTION (Moderate numerical error)"
    if evals > 1000 and rel_err > 0.1:
        return "UNSTABLE (Severe error despite high evaluations, check for oscillation/singularity)"
        
    return "UNSTABLE"
