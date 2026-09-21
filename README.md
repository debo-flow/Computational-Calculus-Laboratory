# Computational Calculus Laboratory

**Milestone 13 — Advanced Vector Calculus Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 13 introduces the **Advanced Vector Calculus Laboratory**. This update elevates the system to handle the full scope of classical 3D kinematics, differential operators (Gradient, Divergence, Curl, Laplacian), and the great integral theorems of vector calculus (Green's, Stokes', Divergence).

## Features Implemented

### Milestone 13: Vector Calculus
* **Vector-Valued Functions $r(t)$:** Kinematic analysis computing Velocity, Acceleration, Speed, Unit Tangents, Curvature ($\kappa$), and exact Arc Lengths.
* **Vector Fields $F(x,y,z)$:** Evaluation and Quiver-plot visualization of 2D/3D fields.
* **Differential Operators:** Computes Divergence ($\nabla \cdot F$), Curl ($\nabla \times F$), and the scalar Laplacian ($\nabla^2 f$). Identifies Irrotational (Conservative) and Incompressible fields.
* **Vector Line Integrals & Work:** Exact and numerical evaluation of $\int_C F \cdot dr$ along user-defined parametric trajectories.
* **Surface Integrals & Flux:** Parameterizes surfaces $r(u,v)$, computes the normal vector $r_u \times r_v$, and evaluates total Flux $\iint_S F \cdot n dS$.
* **Theorems of Vector Calculus:** Computational verification engines testing Green's Theorem and the Divergence Theorem directly against vector definitions over constrained geometries.

### Earlier Milestones (Preserved)
* **M12:** Multiple Integrals (Iterated, Monte Carlo, Jacobians, Laminas).
* **M11:** Multivariable Calculus (Gradients, Jacobians, Hessian).
* **M10:** Advanced Taylor & Maclaurin Series (Polynomials, Error Bounds).
* **M9:** Advanced Sequences & Infinite Series.
* **M8:** Advanced Numerical Integration (Quadrature, Adaptive).
* **M7:** Advanced Integral Calculus (Symbolic $+C$, FTC).
* **M6:** Advanced Numerical Differentiation.
* **M5:** Applications of Differential Calculus.
* **M4:** Advanced Differential Calculus.
* **M3:** Continuity & Discontinuity.
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
