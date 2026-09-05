import sympy as sp
from typing import Dict, Union, Tuple
from calculus.functions.function_engine import FunctionEngine

class LimitEngine:
    """
    Symbolic engine for calculating exact limits.
    """
    def __init__(self, engine: FunctionEngine):
        self.engine = engine
        self.x = engine.x
        self.expr = engine.expression

    def evaluate_limits(self, point: Union[float, str]) -> Dict[str, Union[sp.Expr, str]]:
        """
        Evaluates Left-Hand, Right-Hand, and Two-Sided limits symbolically.
        """
        try:
            # Parse the limit point (handle 'oo' and '-oo' for infinity)
            if str(point).lower() in ['inf', 'oo', 'infinity']:
                a = sp.oo
            elif str(point).lower() in ['-inf', '-oo', '-infinity']:
                a = -sp.oo
            else:
                a = sp.sympify(point)

            results = {}
            
            # If a is infinity, LHL and RHL conceptually merge into the limit at infinity
            if a == sp.oo or a == -sp.oo:
                lim = sp.limit(self.expr, self.x, a)
                results['Left-Hand Limit'] = lim
                results['Right-Hand Limit'] = lim
                results['Two-Sided Limit'] = lim
            else:
                # Calculate directional limits
                lhl = sp.limit(self.expr, self.x, a, dir='-')
                rhl = sp.limit(self.expr, self.x, a, dir='+')
                
                results['Left-Hand Limit'] = lhl
                results['Right-Hand Limit'] = rhl
                
                # Compare for Two-Sided limit existence
                if lhl == rhl:
                    results['Two-Sided Limit'] = lhl
                else:
                    results['Two-Sided Limit'] = "Does Not Exist"
                    
            return results
            
        except Exception as e:
            raise ValueError(f"Symbolic limit evaluation failed: {str(e)}")
