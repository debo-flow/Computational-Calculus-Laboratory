import sympy as sp
from typing import Dict, Any

def solve_symbolic_ode(eq_str: str, ivp: Dict[str, float] = None, func_name: str = 'y', var_name: str = 'x') -> Dict[str, Any]:
    """Solves ODE symbolically and verifies the residual."""
    x = sp.Symbol(var_name, real=True)
    y = sp.Function(func_name)(x)
    
    lhs, rhs = eq_str.split('=') if '=' in eq_str else (eq_str, "0")
    ode_eq = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
    
    try:
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
        
        # Residual Verification
        sol_rhs = solution.rhs if isinstance(solution, sp.Eq) else solution
        residual = sp.simplify(ode_eq.lhs.subs(y, sol_rhs).doit() - ode_eq.rhs.subs(y, sol_rhs).doit())
        
        return {
            "Status": "Success",
            "Solution": solution,
            "Residual": residual,
            "Verified": (residual == 0)
        }
    except Exception as e:
        return {"Status": "Failed", "Error": str(e)}
