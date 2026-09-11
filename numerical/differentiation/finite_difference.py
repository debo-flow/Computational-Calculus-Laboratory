from dataclasses import dataclass
from typing import Dict

@dataclass
class FiniteDifferenceStencil:
    name: str
    derivative_order: int
    theoretical_order_accuracy: int
    coefficients: Dict[float, float] # Offset factor -> Coefficient
    
# Pre-defined mathematically rigorous stencils
STENCILS = {
    "Forward (1st Order)": FiniteDifferenceStencil("Forward", 1, 1, {0.0: -1.0, 1.0: 1.0}),
    "Backward (1st Order)": FiniteDifferenceStencil("Backward", 1, 1, {-1.0: -1.0, 0.0: 1.0}),
    "Central (2nd Order)": FiniteDifferenceStencil("Central", 1, 2, {-1.0: -0.5, 1.0: 0.5}),
    "Forward (2nd Order)": FiniteDifferenceStencil("Forward 2nd O", 1, 2, {0.0: -1.5, 1.0: 2.0, 2.0: -0.5}),
    "Central 2nd Derivative": FiniteDifferenceStencil("Central 2nd Deriv", 2, 2, {-1.0: 1.0, 0.0: -2.0, 1.0: 1.0}),
    "Central 3rd Derivative": FiniteDifferenceStencil("Central 3rd Deriv", 3, 2, {-2.0: -0.5, -1.0: 1.0, 1.0: -1.0, 2.0: 0.5})
}
