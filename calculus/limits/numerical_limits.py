import sympy as sp
from typing import List, Dict, Union
from calculus.functions.function_engine import FunctionEngine
from numerical.validation import calculate_absolute_error

class NumericalLimitEngine:
    """
    Engine for calculating limits via numerical convergence tables.
    """
    def __init__(self, engine: FunctionEngine):
        self.engine = engine
        self.x = engine.x
        self.expr = engine.expression

    def generate_convergence_table(
        self, 
        point: float, 
        direction: str = 'both', 
        steps: int = 5
    ) -> Dict[str, List[Dict[str, Union[float, str]]]]:
        """
        Generates convergence data progressively approaching the limit point.
        Direction: 'left', 'right', or 'both'.
        """
        tables = {}
        distances = [10**(-i) for i in range(1, steps + 1)]

        if direction in ['left', 'both']:
            tables['left'] = self._build_table(point, distances, is_left=True)
            
        if direction in ['right', 'both']:
            tables['right'] = self._build_table(point, distances, is_left=False)

        return tables

    def generate_infinity_table(
        self, 
        positive_infinity: bool = True, 
        steps: int = 5
    ) -> List[Dict[str, Union[float, str]]]:
        """
        Generates convergence data for limits approaching infinity.
        """
        magnitudes = [10**i for i in range(1, steps + 1)]
        if not positive_infinity:
            magnitudes = [-m for m in magnitudes]
            
        table = []
        prev_val = None
        
        for m in magnitudes:
            row = self._evaluate_row(m, prev_val)
            table.append(row)
            prev_val = row["f(x)"] if isinstance(row["f(x)"], float) else None
            
        return table

    def _build_table(self, point: float, distances: List[float], is_left: bool) -> List[Dict[str, Union[float, str]]]:
        table = []
        prev_val = None
        
        for d in distances:
            x_val = point - d if is_left else point + d
            row = self._evaluate_row(x_val, prev_val)
            row["Distance"] = d
            table.append(row)
            prev_val = row["f(x)"] if isinstance(row["f(x)"], float) else None
            
        return table

    def _evaluate_row(self, x_val: float, prev_val: Union[float, None]) -> Dict[str, Union[float, str]]:
        exact, num = self.engine.evaluate(x_val)
        
        change = "N/A"
        if isinstance(num, float) and prev_val is not None:
            change = calculate_absolute_error(num, prev_val)

        return {
            "x": x_val,
            "f(x)": num,
            "Change from Previous": change
        }
