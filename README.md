# Computational Calculus Laboratory

**Milestone 19 — Advanced Differential Equations & Dynamical Systems Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 19 refines and finalizes the **Dynamical Systems Laboratory**. It implements meticulous symbolic parsing for First-Order differential equations (Separable, Exact, Linear, Bernoulli) verifying all analytical solutions through exact residual substitution. It strictly integrates $N$-dimensional autonomous vector fields, tracking invariant nullclines, topological phase limits, and empirical $p$-order numerical convergence testing.

## Features Implemented

### Milestone 19: Differential Equations Finalization
* **Explicit First-Order Parsing:** Automatically routes and solves Bernoulli substitutions ($v = y^{1-n}$), Linear Integrating Factors ($\mu(x) = e^{\int P dx}$), and Exact Potential Functions ($F(x,y)=C$). 
* **Convergence Verification Benchmarks:** Implements empirical stepwise convergence loops evaluating $p \approx \log(E_1/E_2)/\log(h_1/h_2)$ against exact integration bounds across Euler, Heun, Midpoint, and RK4 steppers.
* **Topological Phase Space:** Extracts symbolic $f(x,y)=0$ and $g(x,y)=0$ Nullclines overlaid across normalized direction/streamline vector fields to map global dynamical flow.
* **Equilibrium & Linearized Stability:** Computes the Jacobian matrix $\partial F / \partial X$ at $F(X)=0$, extracting Eigenvalues to decisively classify local geometric stability (Saddles, Nodes, Foci, Centers).
* **Classical Parameter Explorer:** Interactive sandbox for famous biological/physical dynamical limits (Lotka-Volterra Predator-Prey, Damped/Harmonic Oscillators, Logistic Growth).

### Earlier Milestones (Preserved)
* **M18-M14:** Advanced BVPs/IVPs, Shooting Methods, Bifurcation/Sensitivity, Stiff ODE frameworks.
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
