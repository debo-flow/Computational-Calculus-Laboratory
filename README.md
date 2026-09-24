# Computational Calculus Laboratory

**Milestone 17 — Advanced Differential Equations & Dynamical Systems Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 17 is the culminating architecture for the **Advanced Differential Equations & Dynamical Systems Laboratory**. It unites linear algebra, vector fields, and exact numerical approximation to evaluate multidimensional ODEs. It heavily focuses on rigorous error bounds, empirical convergence orders ($p \approx \log(E_1/E_2)/\log(h_1/h_2)$), nullcline mapping, and bifurcation / chaos foundations.

## Features Implemented

### Milestone 17: Differential Equations Finalization
* **ODE Classification & Exact Solvers:** Symbolically parses Linearity, Homogeneity, and Autonomy. Computes Exact, Separable, and First-Order Linear integrating factors utilizing SymPy residual verification.
* **Empirical Convergence Benchmarking:** Systematically halves $h$ iteratively to prove the theoretical convergence limits of Explicit Euler $O(h)$, Midpoint $O(h^2)$, and RK4 $O(h^4)$.
* **Dynamical Phase Spaces:** Maps interactive vector fields overlaid with computed $f(x,y)=0$ and $g(x,y)=0$ Nullclines to visually anchor equilibrium candidates.
* **Bifurcation & Chaos Foundations:** 
  * Parameter sweeps iteratively track the creation/destruction of roots (e.g., Pitchfork Bifurcations at $\mu=0$).
  * Sensitivity analysis generates log-scale plots tracking the exponential divergence $D(t) = ||X_1(t) - X_2(t)||$ of perturbed initial states (e.g., Lorenz Attractors).
* **Unified Solvers & 3D Visualization:** Maps adaptive $N$-dimensional trajectories, rendering 3D parametric phase space limits.

### Earlier Milestones (Preserved)
* **M16:** Stiff ODE Integration (BDF), Matrix Characteristic Root Analysis.
* **M15:** Boundary Value Problems (Shooting, Finite Difference).
* **M14:** Jacobian Linearization, Eigenvalue Stability Classification.
* **M13:** Advanced Vector Calculus (Divergence, Curl, Theorems).
* **M12:** Multiple Integrals (Iterated, Monte Carlo).
* **M11:** Multivariable Calculus (Gradients, Jacobians).
* **M10:** Advanced Taylor Series (Polynomials, Error Bounds).
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
