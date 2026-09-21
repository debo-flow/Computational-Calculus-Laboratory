import sympy as sp
import numpy as np

def analyze_stability(sys_exprs: list, vars_str: str, eq_point: list) -> dict:
    """Computes Jacobian, eigenvalues, and strictly classifies 2D local stability."""
    variables = sp.symbols(vars_str)
    equations = [sp.sympify(e) for e in sys_exprs]
    
    J_sym = sp.Matrix([[sp.diff(eq, v) for v in variables] for eq in equations])
    sub_map = dict(zip(variables, eq_point))
    
    try:
        J_num = np.array(J_sym.subs(sub_map).evalf()).astype(np.float64)
        eigenvalues = np.linalg.eigvals(J_num)
        
        # Classification (Strictly 2D Linearized cases)
        classification = "Higher Dimensional / Unclassified"
        if len(variables) == 2:
            tr = np.trace(J_num)
            det = np.linalg.det(J_num)
            disc = tr**2 - 4*det
            
            if det < 0:
                classification = "Saddle Point (Unstable)"
            elif det > 0:
                if tr < 0:
                    classification = "Stable Node" if disc >= 0 else "Stable Spiral (Focus)"
                elif tr > 0:
                    classification = "Unstable Node" if disc >= 0 else "Unstable Spiral (Focus)"
                else:
                    classification = "Center (Linearized Center - Nonlinear stability inconclusive)"
            else:
                classification = "Degenerate / Inconclusive (Zero Determinant)"
                
        return {
            "Jacobian (J)": J_sym,
            "Evaluated J": J_num.tolist(),
            "Eigenvalues": np.round(eigenvalues, 4).tolist(),
            "Classification": classification
        }
    except Exception as e:
        return {"Error": str(e)}
