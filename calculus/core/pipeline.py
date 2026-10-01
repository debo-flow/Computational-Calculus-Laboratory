from typing import Dict, Any
from calculus.symbolic.expression_parser import safe_parse
from calculus.symbolic.expression_analysis import find_domain_restrictions
from calculus.core.classifier import classify_problem
import time

def master_calculus_workflow(input_str: str, **kwargs) -> Dict[str, Any]:
    """
    Master Pipeline: Input -> Parse -> Classify -> Domain -> Solve -> Validate -> Report
    """
    t0 = time.perf_counter()
    report = {"Input": input_str}
    
    # 1. Classification
    classification = classify_problem(input_str)
    report["Detected Problem Type"] = classification["Type"]
    
    # 2. Safe Parsing & Domain
    try:
        if classification["Engine"] in ["symbolic", "limit", "integration"]:
            expr = safe_parse(input_str)
            report["Parsed Expression"] = str(expr)
            domain = find_domain_restrictions(expr, list(expr.free_symbols)[0] if expr.free_symbols else None)
            report["Domain"] = str(domain.get("Continuous Domain", "Reals"))
    except Exception as e:
        report["Error"] = f"Parsing failed: {e}"
        return report
        
    # 3. Engine Routing (Delegated to CalculusEngine)
    from calculus.core.calculus_engine import CalculusEngine
    engine = CalculusEngine()
    
    try:
        if classification["Engine"] == "limit":
            res = engine.limit(input_str, kwargs.get('var', 'x'), kwargs.get('point', 0))
            report["Symbolic Result"] = str(res)
            report["Result Classification"] = "EXACT SYMBOLIC RESULT"
        elif classification["Engine"] == "integration":
            res = engine.integrate(input_str, kwargs.get('var', 'x'))
            report["Symbolic Result"] = str(res)
            report["Result Classification"] = "ANALYTICAL RESULT"
        else:
            res = engine.simplify(input_str)
            report["Symbolic Result"] = str(res)
            report["Result Classification"] = "EXACT SYMBOLIC RESULT"
    except Exception as e:
        report["Error"] = str(e)
        report["Result Classification"] = "INCONCLUSIVE"
        
    report["Execution Time (s)"] = time.perf_counter() - t0
    return report
