# Computational Calculus Laboratory

**Milestone 16 — Advanced Differential Equations & Dynamical Systems Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 16 solidifies the **Dynamical Systems Laboratory**. It expands beyond solver implementation into deep dynamical system properties: identifying structural stiffness, tracing sensitive dependence on initial conditions (Chaos theory foundations), evaluating characteristic matrix stability, and rigorously tracking physical energy conservation laws via symbolic derivatives and numerical drift analysis.

## Features Implemented

### Milestone 16: Advanced ODEs & Dynamical Systems
* **Matrix Linear Systems & Characteristic Roots:** Computes homogeneous solutions for $ay'' + by' + cy = 0$ via characteristic root classification, and provides strict determinant/trace stability analysis for linear 2x2 matrix systems ($X' = AX$).
* **Conservation Laws & Energy:** Symbolically proves the existence of system invariants by deriving $dI/dt = \nabla I \cdot \vec{F} = 0$, and visually tracks numerical energy dissipation/drift over long integration times.
* **Sensitive Dependence (Chaos):** Simulates coupled chaotic attractors (e.g., Lorenz) under infinitesimal perturbations ($X_0 + \delta X$), graphing the exponential trajectory divergence over time via interpolation.
* **Stiffness Foundations:** Introduces implicit integration frameworks (BDF/Radau via SciPy) allowing the stable resolution of multi-timescale stiff ODEs (e.g., Van der Pol oscillator $\mu = 1000$) where explicit methods (RK45) catastrophically stall.
* **Unified ODE Solver API:** Consolidates explicit fixed-step solvers (Euler, Heun, Midpoint, RK4) alongside Adaptive explicit/implicit routines into a single, scalable pipeline.

### Earlier Milestones (Preserved)
* **M15:** Boundary Value Problems (BVP), Isoclines, First-Order Analytical.
* **M14:** Phase Space, Jacobian Linearization, Numerical Initial Value Problems.
* **M13:** Advanced Vector Calculus (Divergence, Curl, Flux, Theorems).
* **M12:** Multiple Integrals (Iterated, Monte Carlo, Jacobians).
* **M11:** Multivariable Calculus (Gradients, Jacobians, Hessian).
* **M10:** Advanced Taylor Series (Polynomials, Error Bounds).
* **M9:** Advanced Sequences & Infinite Series.
* **M8:** Advanced Numerical Integration.
* **M7:** Advanced Integral Calculus.
* **M6:** Advanced Numerical Differentiation.
* **M5:** Applications of Differential Calculus.
* **M4:** Advanced Differential Calculus.
* **M3:** Continuity & Discontinuity.
* **M2:** Limits Laboratory.
* **M1:** Core Foundation & Function Engine.

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
