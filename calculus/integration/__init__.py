"""
Advanced Integral Calculus Laboratory Module
Provides symbolic integration, definite integrals, Riemann approximations,
analytical techniques, and mathematical verification.
"""

from .integral_engine import IntegralEngine
from .indefinite_integrals import compute_indefinite_integral
from .definite_integrals import compute_definite_integral
from .integration_rules import identify_integration_rule
from .improper_integrals import evaluate_improper_integral
from .integral_analysis import (
    compute_riemann_sum,
    riemann_convergence_series,
    verify_fundamental_theorem_part1,
    verify_fundamental_theorem_part2,
    area_between_curves,
    integration_by_parts,
    partial_fractions_decomposition
)

__all__ = [
    "IntegralEngine",
    "compute_indefinite_integral",
    "compute_definite_integral",
    "identify_integration_rule",
    "evaluate_improper_integral",
    "compute_riemann_sum",
    "riemann_convergence_series",
    "verify_fundamental_theorem_part1",
    "verify_fundamental_theorem_part2",
    "area_between_curves",
    "integration_by_parts",
    "partial_fractions_decomposition"
]
