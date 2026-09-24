# Computational Calculus Laboratory

**Milestone 15 — Advanced Differential Equations & Dynamical Systems Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 15 expands the **Dynamical Systems Laboratory**. It unites linear algebra, vector calculus, and integration to systematically classify analytical first-order ODEs (Exact, Linear), while introducing robust numerical frameworks for **Boundary Value Problems (BVPs)** utilizing the Finite Difference and Shooting methods.

## Features Implemented

### Milestone 15: Differential Equations & Dynamical Systems
* **Analytical First-Order ODEs:** Detects exact differentials ($M dx + N dy = 0$) and computes potential functions $F(x,y)$. Implements the Integrating Factor method for standard linear ODEs.
* **Boundary Value Problems (BVP):** 
  * **Shooting Method:** Iteratively corrects initial slopes $y'(a)$ using the Secant root-finding method over RK4 integrations to hit the terminal target $y(b) = \beta$.
  * **Finite Difference Matrix:** Discretizes the spatial domain to construct and solve a tridiagonal linear algebra system for 2nd order linear BVPs.
* **Symbolic General & Particular Solutions:** Extracts initial conditions dynamically to lock particular integration constants, verifying accuracy via residual elimination ($LHS - RHS = 0$).
* **Isoclines & Slope Fields:** Extends geometric vector plots to map level curves $f(x,y) = C$ where the slope strictly rests constant.
* **Equilibria & Local Stability:** Symbolically roots autonomous systems, extracts evaluating Jacobians, computes eigenvalues, and definitively classifies the geometry of nodes, saddles, and foci.

### Earlier Milestones (Preserved)
* **M13:** Advanced Vector Calculus (Divergence, Curl, Flux, Theorems).
* **M12:** Multiple Integrals (Iterated, Monte Carlo, Jacobians).
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
