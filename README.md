# Computational Calculus Laboratory

**Milestone 23 — Advanced Symbolic Mathematics & Computer Algebra Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 23 introduces a centralized **Computer Algebra System (CAS) Layer**. This overarching subsystem consolidates the disparate symbolic operations from Milestones 1-22 into a safe, unified routing interface. It actively protects the Python kernel from arbitrary code execution via strict dictionary filtering, applies deep mathematical Assumption conditions ($\mathbb{R}^+, \mathbb{Z}$), and generates visual Abstract Syntax Trees (AST).

## Features Implemented

### Milestone 23: Symbolic Mathematics & CAS
* **Safe Expression Parser:** A rigorously sandboxed parsing wrapper around SymPy that strips `__builtins__` and prevents `eval()` injections, translating human input (e.g., `x^2`) into exact symbolic objects without triggering dangerous code execution.
* **Unified Calculus Router:** A central Facade module that fields user operations (`limit`, `derivative`, `integral_indefinite`, `laplacian`) and dispatches them natively across the ecosystem. 
* **Algebraic Manipulations & Equivalence:** Exact algorithmic operations (`expand`, `factor`, `cancel`, `apart`). Features a dual-validation Equivalence engine that symbolically simplifies $A - B = 0$ while concurrently cross-validating the identity numerically over a randomized continuous domain matrix.
* **Equations & Inequalities:** Maps $f(x)=0$ and $f(x) < 0$ bounds to return structured interval sets, supporting exact complex/real domain extraction.
* **Assumptions Engine:** Allows runtime enforcement of mathematical limits (e.g., setting variables to strictly Positive Reals) to safely unlock otherwise invalid topological simplifications (like $\sqrt{x^2} = x$).
* **CAS Interactive Notebook:** Emulates Mathematica/Jupyter cell behaviors inside the UI, retaining step-by-step histories of sequential transformations via session state.

### Earlier Milestones (Preserved)
* **M22:** Scientific Computing & Numerics (Precision, SVD, Extrapolation).
* **M21:** Tensor Calculus & Differential Geometry (Christoffel, Curvatures).
* **M20:** Calculus of Variations (Euler-Lagrange, Numerical Functionals).
* **M19-M14:** Advanced Differential Equations (IVPs, BVPs, Chaos, Stiff Systems).
* **M13:** Advanced Vector Calculus (Divergence, Curl, Flux, Theorems).
* **M12:** Multiple Integrals (Iterated, Monte Carlo, Jacobians).
* **M11:** Multivariable Calculus.
* **M10:** Advanced Taylor Series.
* **M9:** Advanced Sequences & Infinite Series.
* **M8:** Advanced Numerical Integration.
* **M7:** Advanced Integral Calculus.
* **M6:** Advanced Numerical Differentiation.
* **M5:** Applications of Differential Calculus.
* **M4:** Advanced Differential Calculus.
* **M3:** Continuity & Discontinuity.
* **M2:** Limits Laboratory.
* **M1:** Core Foundation.

## Technology Stack
* Python 3.9+
* Mathematics: SymPy, NumPy, SciPy, mpmath
* Visualization: Matplotlib
* UI Framework: Streamlit
* Testing: Pytest

## Installation & Running
```bash
pip install -r requirements.txt
streamlit run app/main.py
