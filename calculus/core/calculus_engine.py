from calculus.symbolic.symbolic_engine import CASRouter
from calculus.verification.symbolic_verification import verify_symbolic_identity

class CalculusEngine:
    """Unified Python API aggregating all mathematical subsystems."""
    
    def simplify(self, expr: str):
        return CASRouter.simplify(expr)
        
    def solve(self, expr: str, var: str):
        return CASRouter.solve(expr, var)
        
    def differentiate(self, expr: str, var: str, order: int = 1):
        return CASRouter.calculus_route("derivative", expr, var, order=order)
        
    def integrate(self, expr: str, var: str):
        return CASRouter.calculus_route("integral_indefinite", expr, var)
        
    def limit(self, expr: str, var: str, point: float):
        return CASRouter.calculus_route("limit", expr, var, point=point)
        
    def validate(self, lhs: str, rhs: str):
        return verify_symbolic_identity(lhs, rhs)
