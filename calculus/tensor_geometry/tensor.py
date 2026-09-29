import sympy as sp
from typing import List
from .indices import IndexManager

class Tensor:
    """Represents a general tensor with upper (contravariant) and lower (covariant) indices."""
    def __init__(self, name: str, components: sp.Matrix, upper_idx: List[str], lower_idx: List[str]):
        self.name = name
        self.components = components
        self.upper = upper_idx
        self.lower = lower_idx
        self.rank = len(upper_idx) + len(lower_idx)
        
    def __str__(self):
        return IndexManager.format_tensor_symbol(self.name, self.upper, self.lower)
