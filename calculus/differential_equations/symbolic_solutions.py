import sympy as sp
from typing import Dict

def solve_symbolic_ode(eq_str: str, ivp: Dict[str, float] = None, func_name: str = 'y', var_name: str = 'x') -> dict:
    """Finds exact general or particular (IVP) solutions and verifies residuals."""
    x = sp.Symbol(var_name, real=True)
    y = sp.Function(func_name)(x)
    
    eq_parts = eq_str.split('=')
    lhs = sp.sympify(eq_parts[0])
    rhs = sp.sympify(eq_parts[1]) if len(eq_parts) > 1 else sp.S.Zero
    ode_eq = sp.Eq(lhs, rhs)
    
    try:
        # Prepare IVP dictionary for SymPy (e.g., {y(0): 1, y'(0): 0})
        ics = {}
        if ivp:
            for k, v in ivp.items():
                if "'" in k:
                    deriv_order = k.count("'")
                    val = float(k.split('(')[1].split(')')[0])
                    ics[y.diff(x, deriv_order).subs(x, val)] = v
                else:
                    val = float(k.split('(')[1].split(')')[0])
                    ics[y.subs(x, val)] = v
        
        solution = sp.dsolve(ode_eq, y, ics=ics if ics else None)
        
        # Verify Residual: LHS - RHS = 0
        residual = sp.simplify(ode_eq.lhs.subs(y, solution.rhs) - ode_eq.rhs.subs(y, solution.rhs))
        verified = (residual == 0)
        
        return {
            "Status": "Success",
            "General/Particular Solution": solution,
            "Residual": residual,
            "Verified": verified
        }
    except Exception as e:
        return {"Status": "Failed", "Error": str(e)}
