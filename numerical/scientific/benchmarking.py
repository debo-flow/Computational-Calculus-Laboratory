import time
import platform
import numpy as np
from typing import Callable, Dict, Any

def generate_scientific_report(func: Callable, *args, **kwargs) -> Dict[str, Any]:
    """Wraps numerical functions to append reproducible context and execution metrics."""
    start_time = time.perf_counter()
    try:
        result = func(*args, **kwargs)
        status = "Success"
    except Exception as e:
        result = str(e)
        status = "Failed"
    execution_time = time.perf_counter() - start_time
    
    return {
        "Algorithm": func.__name__,
        "Execution Time (s)": execution_time,
        "Status": status,
        "Result": result,
        "Reproducibility": {
            "Architecture": platform.machine(),
            "Python Version": platform.python_version(),
            "NumPy Version": np.__version__
        }
    }
