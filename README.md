# Computational Calculus Laboratory

**Milestone 20 — Advanced Calculus of Variations & Functional Optimization Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 20 completes the transition from ordinary calculus into **Functional Calculus**. It introduces the **Calculus of Variations Laboratory**, allowing users to rigorously optimize functionals $J[y] = \int F(x, y, y') dx$. It features exact symbolic Euler-Lagrange derivation alongside Ritz-style numerical discretization grids, bridging classical analytical mechanics (e.g., Shortest Paths, Brachistochrones, Action Minimization) with modern computational optimization.

## Features Implemented

### Milestone 20: Calculus of Variations
* **Symbolic Euler-Lagrange Derivation:** Exact expansion of $\frac{\partial F}{\partial y} - \frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right) = 0$ utilizing SymPy chain-rule tracking for arbitrary integrands.
* **Numerical Functional Minimization:** Directly discretizes the functional $J[y]$ over a spatial grid and leverages SciPy's `BFGS` optimizer to iteratively warp boundary-locked trial vectors into minimum-energy extremal states.
* **Extremal vs. Analytical Residuals:** Evaluates the discretized numerical arrays directly against the symbolic Euler-Lagrange PDE to chart local $R(x)$ residuals, verifying true numerical convergence.
* **First Variation ($\delta J$) Analysis:** Symbolically computes $\frac{d}{d\epsilon} F(y + \epsilon \eta) \big\vert{}_{\epsilon=0}$ to demonstrate rigorous perturbation theory.
* **Isoperimetric Constraints:** Generates Lagrange Multiplier functional bridges $H = F + \lambda G$ to support length/area constrained physics problems (e.g., Dido's problem).

### Earlier Milestones (Preserved)
* **M19-M14:** Advanced Differential Equations (IVPs, BVPs, Chaos, Stiff Systems).
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
