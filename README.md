# Computational Calculus Laboratory

**Milestone 18 — Advanced Differential Equations & Dynamical Systems Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 18 completes the **Dynamical Systems Laboratory**. It unites numerical integration, symbolic classification, and multivariable linear algebra to rigorously analyze ODEs. It heavily focuses on empirical error bounds ($p \approx \log(E_1/E_2)/\log(h_1/h_2)$), multidimensional nullcline mapping, and robust adaptive vs. fixed-step (Euler to RK4) numerical benchmarks.

## Features Implemented

### Milestone 18: Differential Equations & Dynamical Systems
* **ODE Classification & Exact Solvers:** Symbolically parses Linearity, Homogeneity, and Autonomy. Computes exact analytical solutions (General and IVP) using SymPy, independently verifying results via residual elimination ($LHS - RHS = 0$).
* **Empirical Convergence Benchmarking:** Systematically halves step size $h$ iteratively to experimentally prove the theoretical convergence limits of Explicit Euler $O(h)$, Heun/Midpoint $O(h^2)$, RK3 $O(h^3)$, and RK4 $O(h^4)$.
* **Dynamical Phase Spaces:** Maps interactive vector fields overlaid with computed $f(x,y)=0$ and $g(x,y)=0$ Nullclines to visually anchor equilibrium candidates and trajectories.
* **Equilibrium & Stability:** Symbolically hunts for autonomous equilibrium roots ($f(X)=0$). Computes the evaluating Jacobian ($J$), extracts Eigenvalues, and strictly classifies linearized 2D stability (Nodes, Saddles, Foci, Centers).
* **Stiffness Foundations:** Introduces implicit integration frameworks (BDF via SciPy) allowing the stable resolution of multi-timescale stiff ODEs where explicit methods (RK45) catastrophically stall.

### Earlier Milestones (Preserved)
* **M17/16/15/14:** Foundational ODEs, BVPs, Chaos Sensitivity, and Energy Conservation.
* **M13:** Advanced Vector Calculus (Divergence, Curl, Flux, Green/Stokes Theorems).
* **M12:** Multiple Integrals (Iterated, Monte Carlo, Jacobians, Laminas).
* **M11:** Multivariable Calculus (Gradients, Jacobians, Hessian).
* **M10:** Advanced Taylor & Maclaurin Series (Polynomials, Error Bounds).
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
* Mathematics: SymPy, NumPy, SciPy
* Visualization: Matplotlib
* UI Framework: Streamlit
* Testing: Pytest

## Installation & Running
```bash
pip install -r requirements.txt
streamlit run app/main.py
