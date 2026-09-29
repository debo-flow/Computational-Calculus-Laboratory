import sympy as sp
from typing import List, Tuple

class IndexManager:
    """Manages Einstein Summation and upper/lower index validation."""
    @staticmethod
    def validate_contraction(upper_idx: List[str], lower_idx: List[str]) -> Tuple[bool, str]:
        overlap = set(upper_idx).intersection(set(lower_idx))
        if not overlap:
            return False, "No matching upper and lower indices to contract."
        return True, list(overlap)[0]

    @staticmethod
    def format_tensor_symbol(base: str, upper: List[str], lower: List[str]) -> str:
        u_str = "".join(upper)
        l_str = "".join(lower)
        if u_str and l_str: return f"{base}^{{{u_str}}}_{{{l_str}}}"
        elif u_str: return f"{base}^{{{u_str}}}"
        elif l_str: return f"{base}_{{{l_str}}}"
        return base
