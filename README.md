# Computational Calculus Laboratory

**Milestone 22 — Advanced Numerical Calculus & Scientific Computing Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 22 introduces the **Scientific Computing Laboratory**, bridging continuous mathematics with discrete numerical implementations. This suite explicitly quantifies algorithmic accuracy vs. precision limits, mapping machine round-off behaviors, truncation boundaries, condition number sensitivities, and establishing explicit finite-difference PDE solver stability limits.

## Features Implemented

### Milestone 22: Scientific Computing & Numerics
* **Problem Conditioning & Precision:** Isolates algorithmic instability from inherent mathematical sensitivity by computing Relative Condition Numbers ($K$). Evaluates numerical artifacts up to 100-digit precision utilizing `mpmath`.
* **Numerical Linear Algebra:** Generates robust Singular Value Decompositions ($A = U \Sigma V^T$) and Eigen-system solvers, calculating tight residual bounds ($\vert{}\vert{}Av - \lambda v\vert{}\vert{}$) for validation.
* **PDE Stability Foundations:** Implements FTCS grid stepping for the 1D Heat Equation ($u_t = \alpha u_{xx}$), strictly enforcing and visually demonstrating exponential blow-up when the Courant–Friedrichs–Lewy (CFL) limit ($\Delta t \le \frac{\Delta x^2}{2\alpha}$) is breached.
* **Richardson Extrapolation:** Eliminates lowest-order numerical truncation error terms to drastically artificially inflate the order of accuracy of derivative approximations.
* **Cubic Spline Interpolation:** Reconstructs continuous piecewise functions over discrete, unordered datasets using globally enforced boundary stiffness (Natural Splines).
* **Reproducibility Benchmarking:** Injects Python versioning, architectural metadata, and millisecond execution metrics into JSON scientific reports for rigorous academic replication.

### Earlier Milestones (Preserved)
* **M21:** Tensor Calculus & Differential Geometry (Christoffel, Curvatures).
* **M20:** Calculus of Variations (Euler-Lagrange, Numerical Functionals).
* **M19-M14:** Advanced Differential Equations (IVPs, BVPs, Chaos).
* **M13:** Advanced Vector Calculus (Divergence, Curl, Flux).
* **M12:** Multiple Integrals (Iterated, Monte Carlo).
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
