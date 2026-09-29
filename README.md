# Computational Calculus Laboratory

**Milestone 21 — Advanced Tensor Calculus & Differential Geometry Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 21 represents the absolute pinnacle of classical analytic and differential mechanics: the **Tensor Calculus & Differential Geometry Laboratory**. It integrates tensor-algebra rules to calculate non-Euclidean intrinsic curvature natively, extracting Christoffel connections, Geodesic ODE trajectories, and Riemann/Ricci tensors exclusively from user-defined arbitrary Metric tensors.

## Features Implemented

### Milestone 21: Tensor Calculus & Geometry
* **Metrics & Connections:** Given any metric $g_{ij}$, calculates the determinant $g$, inverse $g^{ij}$, and generates the 3-index Christoffel symbols of the second kind $\Gamma^k_{ij}$.
* **Curvature Tensors:** Synthesizes the rank-4 Riemann curvature tensor ($R^i_{jkl}$), tracing it to the Ricci tensor ($R_{ij}$) and contracting it with the metric to yield the Scalar Curvature ($R$).
* **Differential Surface Geometry:** For any parameterized manifold $\vec{r}(u,v)$, computes First ($E,F,G$) and Second ($e,f,g$) Fundamental Forms to derive intrinsic Gaussian Curvature ($K$) and extrinsic Mean Curvature ($H$).
* **Geodesic Flow Generation:** Translates Christoffel symbols into the acceleration components of the geodesic differential equations: $\frac{d^2 x^k}{d\lambda^2} = - \Gamma^k_{ij} \frac{dx^i}{d\lambda}\frac{dx^j}{d\lambda}$.
* **Differential Forms:** Implements the exterior derivative $d\omega$ for arbitrary 1-forms, demonstrating the anti-commutative wedge product $dx \wedge dy$ mapping to vector curl.
* **Surface Curvature Maps:** Plots fully 3D interactive manifolds automatically color-shaded by their localized Gaussian Curvature magnitude.

### Earlier Milestones (Preserved)
* **M20:** Calculus of Variations (Euler-Lagrange, Numerical Functionals).
* **M19-M14:** Advanced Differential Equations (IVPs, BVPs, Chaos, Stiff Systems).
* **M13:** Advanced Vector Calculus (Divergence, Curl, Flux, Green/Stokes Theorems).
* **M12:** Multiple Integrals (Iterated, Monte Carlo, Jacobians, Laminas).
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
