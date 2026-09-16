# Computational Calculus Laboratory

**Milestone 12 — Advanced Multiple Integrals & Multivariable Analysis Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 12 introduces the **Advanced Multiple Integrals & Multivariable Analysis Laboratory**. This completes the transition into $\mathbb{R}^n$ integration by implementing iterated double/triple integrals, algorithmic coordinate transformations with symbolic Jacobian $|J|$ computations, physical applications (Mass, Moments of Inertia), and stochastic Monte Carlo integration to benchmark deterministic bounds.

## Features Implemented

### Milestone 12: Multiple Integrals
* **Iterated Integration & Fubini's Theorem:** Computes precise $\iint_D$ and $\iiint_V$ integrals, verifying mathematically that reversing integration limits over continuous boundaries ($dx dy \to dy dx$) yields invariant areas/volumes.
* **Coordinate Transformations & Jacobians:** Automatically maps Cartesian domains to Polar, Cylindrical, and Spherical boundaries. Symbolically computes the Jacobian matrix determinant to produce the exact scaling factor $|J| dV$.
* **Physical Applications:** Simulates 2D laminas to dynamically compute Total Mass ($M = \iint \rho dA$), Centroids ($\bar{x}, \bar{y}$), and Moments of Inertia ($I_x, I_y, I_0$) based on variable density equations.
* **Monte Carlo Integration:** Integrates probability theory to evaluate highly complex or discrete multivariable integrals stochastically, visualizing the $O(1/\sqrt{N})$ convergence limitations through error vs. standard-deviation tables.
* **Region Visualization:** Visualizes custom bounding rectangles overlaid with uniform sample-point distributions.

### Earlier Milestones (Preserved)
* **M11:** Advanced Multivariable Calculus (Gradients, Jacobians, Hessian).
* **M10:** Advanced Taylor & Maclaurin Series (Polynomials, Error Bounds).
* **M9:** Advanced Sequences & Infinite Series.
* **M8:** Advanced Numerical Integration (Quadrature, Adaptive).
* **M7:** Advanced Integral Calculus (Symbolic $+C$, FTC).
* **M6:** Advanced Numerical Differentiation.
* **M5:** Applications of Differential Calculus.
* **M4:** Advanced Differential Calculus.
* **M3:** Continuity and Discontinuity Classification.
* **M2:** Limits Laboratory.
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
