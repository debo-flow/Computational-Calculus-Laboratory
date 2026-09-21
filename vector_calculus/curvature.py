import sympy as sp
from .vector_engine import VectorFunctionEngine
from .vector_functions import compute_kinematics

def compute_curvature_and_tangent(engine: VectorFunctionEngine) -> Dict[str, Any]:
    kin = compute_kinematics(engine)
    v = kin["Velocity (v)"]
    a = kin["Acceleration (a)"]
    speed = kin["Speed (|v|)"]
    
    T = [sp.simplify(vc / speed) for vc in v] if speed != 0 else ["Undefined"]
    
    if engine.dim == 3:
        v_mat, a_mat = sp.Matrix(v), sp.Matrix(a)
        cross_prod = v_mat.cross(a_mat)
        kappa = sp.simplify(cross_prod.norm() / (speed**3)) if speed != 0 else "Undefined"
    else:
        kappa = "Requires 3D Parameterization for generalized symbolic formula"

    return {"Unit Tangent (T)": T, "Curvature (kappa)": kappa}
