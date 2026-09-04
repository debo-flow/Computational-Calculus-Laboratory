from typing import Union

def calculate_absolute_error(exact: float, approximation: float) -> float:
    """
    Calculates Absolute Error: |exact - approximation|
    """
    return abs(exact - approximation)

def calculate_relative_error(exact: float, approximation: float) -> Union[float, str]:
    """
    Calculates Relative Error: |exact - approximation| / |exact|.
    Handles exact == 0 gracefully.
    """
    if exact == 0.0:
        if approximation == 0.0:
            return 0.0
        return "Undefined (Division by zero as exact value is 0)"
    
    return abs(exact - approximation) / abs(exact)
