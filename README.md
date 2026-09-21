# Computational Calculus Laboratory

**Milestone 14 — Advanced Differential Equations & Dynamical Systems**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 14 introduces the **Advanced Differential Equations & Dynamical Systems Laboratory**. It unites numerical integration, symbolic limits, and multivariable linear algebra to strictly classify, evaluate, and visualize linear and nonlinear Ordinary Differential Equations (ODEs) and N-dimensional Phase Spaces.

## Features Implemented

### Milestone 14: Differential Equations
* **Symbolic ODE Analysis:** Identifies Order, Linearity, and Autonomy. Computes exact analytical solutions (General and IVP) using SymPy, independently verifying results via residual elimination ($LHS - RHS = 0$).
* **Numerical Fixed-Step Solvers:** Educational side-by-side implementation of Euler, Heun, Midpoint, and classic Runge-Kutta (RK4) methods.
* **Adaptive Integration:** Industrial-grade adaptive RK45 (Fehlberg/Dormand-Prince) engine via SciPy integration.
* **Phase Space & Dynamical Systems:** Converts arbitrary higher-order ODEs to first-order systems. Maps Direction/Slope fields and Phase Portraits with Streamline tracking.
* **Equilibrium & Stability:** Symbolically hunts for autonomous equilibrium roots ($f(X)=0$). Computes the evaluated Jacobian ($J$), extracts Eigenvalues, and strictly classifies linearized 2D stability (Nodes, Saddles, Foci, Centers).

### Earlier Milestones (Preserved)
* **M13:** Advanced Vector Calculus (Divergence, Curl, Flux, Green/Stokes Theorems).
* **M12:** Multiple Integrals (Iterated, Monte Carlo, Jacobians, Laminas).
* **M11:** Multivariable Calculus (Gradients, Jacobians, Hessian).
* **M10:** Advanced Taylor & Maclaurin Series (Polynomials, Error Bounds).
* **M9:** Advanced Sequences & Infinite Series.
* **M8:** Advanced Numerical Integration.
* **M7:** Advanced Integral Calculus (Symbolic $+C$, FTC).
* **M6:** Advanced Numerical Differentiation.
* **M5:** Applications of Differential Calculus.
* **M4:** Advanced Differential Calculus.
* **M3:** Continuity & Discontinuity.
* **M2:** Limits Laboratory.
* **M1:** Core Foundation & Mathematical Function Engine.

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
