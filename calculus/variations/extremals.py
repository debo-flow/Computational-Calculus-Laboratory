import sympy as sp
from .functional import Functional
from .euler_lagrange import derive_euler_lagrange

def solve_extremal(functional: Functional, bc: dict = None) -> dict:
    """Attempts symbolic solution of the EL equation via SymPy dsolve."""
    el_data = derive_euler_lagrange(functional)
    eq = el_data["EL Equation"]
    
    try:
        if bc and "a" in bc and "b" in bc:
            ics = {functional.y.subs(functional.x, bc["a"]): bc["A"], 
                   functional.y.subs(functional.x, bc["b"]): bc["B"]}
            sol = sp.dsolve(eq, functional.y, ics=ics)
        else:
            sol = sp.dsolve(eq, functional.y)
            
        return {"Status": "Success", "Candidate Extremal": sol, "Equation": eq}
    except Exception as e:
        return {"Status": "Failed / Inconclusive", "Equation": eq, "Error": str(e)}
