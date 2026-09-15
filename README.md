# Computational Calculus Laboratory

**Milestone 11 — Advanced Multivariable Calculus Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 11 introduces the **Advanced Multivariable Calculus Laboratory**. It safely transitions the architecture from single-variable calculus into $\mathbb{R}^n$, handling partial derivatives, gradient vector fields, path-limit analysis, Hessian optimization tests, Lagrange multipliers, and foundational multiple integrals.

## Features Implemented

### Milestone 11: Multivariable Calculus
* **3D Scalar Fields & Gradients:** Interactive surface plotting paired with contour and quiver gradient vector mappings.
* **Directional Derivatives & Tangent Planes:** Normalizes vectors $\vec{u}$ to compute $D_u f = \nabla f \cdot \vec{u}$ and constructs local linear approximations $L(x,y)$.
* **Hessian & Critical Points:** Symbolically solves $\nabla f = \vec{0}$ and executes the Second Derivative Test ($D = f_{xx}f_{yy} - (f_{xy})^2$) identifying minima, maxima, and saddle points.
* **Lagrange Multipliers:** Evaluates constrained optimization boundaries $\nabla f = \lambda \nabla g$.
* **Jacobian Matrices:** Derives matrices and determinants for coordinate transformations (e.g., Polar, Cylindrical).
* **Double Integrals:** Exact symbolic integration $\iint_D f(x,y) dA$ over rectangular domains.

### Earlier Milestones (Preserved)
* **M10:** Advanced Taylor & Maclaurin Series (Polynomials, Error Bounds).
* **M9:** Advanced Sequences & Infinite Series (Ratio/Root/Integral Tests).
* **M8:** Advanced Numerical Integration (Quadrature, Gaussian, Adaptive).
* **M7:** Advanced Integral Calculus (Symbolic $+C$, FTC, substitutions).
* **M6:** Advanced Numerical Differentiation.
* **M5:** Applications of Differential Calculus (Extrema, MVT).
* **M4:** Advanced Differential Calculus (Rules, Tangents).
* **M3:** Continuity and Discontinuity Classification.
* **M2:** Limits Laboratory (LHL/RHL).
* **M1:** Core Foundation & Mathematical Function Engine.

## Technology Stack
* Python 3.9+
* Mathematics: SymPy, NumPy
* Visualization: Matplotlib
* UI Framework: Streamlit
* Testing: Pytest

## Installation & Running
```bash
pip install -r requirements.txt
streamlit run app/main.py
