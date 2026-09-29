# Computational Calculus Laboratory

**Milestone 24 — Automated Theorem Verification, Validation & Benchmarking Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 24 introduces the **Automated Theorem Verification, Validation & Benchmarking Laboratory**. This final operational layer acts as the rigorous testing and validation engine for the entire ecosystem. It systematically isolates mathematical proof (symbolic identity verification) from computational evidence (numerical counterexample searches), tracks algorithmic scaling efficiency, computationally validates major theorems (e.g., Green's Theorem), and enforces continuous integration (CI) regression safety.

## Features Implemented

### Milestone 24: Verification & Benchmarking
* **Symbolic Identity Verification:** Rigorously proves algebraic/calculus equivalence by symbolically reducing $LHS - RHS$ to exactly $0$ using the internal CAS engine.
* **Numerical Counterexample Search:** Deploys Monte-Carlo domain sampling to hunt for floating-point violations of proposed mathematical claims, strictly distinguishing empirical validation from formal proof.
* **Computational Theorem Validation:** Independently evaluates dual mathematical pathways (e.g., mapping Line Integrals against Double Integrals for Green's Theorem) to computationally verify foundational calculus theorems.
* **Algorithmic Benchmarking:** Tracks and plots mathematical engine efficiency, measuring execution time scaling across expanding polynomial degrees, matrix sizes, or grid resolutions.
* **Structured Verification Reports:** Serializes comprehensive regression benchmarks, theorem validations, and environment metadata into reproducible JSON and Markdown reports.
* **Continuous Integration (CI/CD):** Implements GitHub Actions (`verification.yml`) to automatically execute the mathematical regression suite (`pytest`) on every repository push.

### Earlier Milestones (Preserved)
* **M23:** Symbolic Mathematics & Computer Algebra System (CAS).
* **M22:** Scientific Computing & Numerics (Precision, SVD, Extrapolation).
* **M21:** Tensor Calculus & Differential Geometry (Christoffel, Curvatures).
* **M20:** Calculus of Variations (Euler-Lagrange, Numerical Functionals).
* **M19-M14:** Advanced Differential Equations (IVPs, BVPs, Chaos, Stiff Systems).
* **M13:** Advanced Vector Calculus (Divergence, Curl, Flux, Green/Stokes Theorems).
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
* **M1:** Core Foundation.

## Technology Stack
* Python 3.9+
* Mathematics: SymPy, NumPy, SciPy, mpmath
* Visualization: Matplotlib
* UI Framework: Streamlit
* Testing & CI: Pytest, GitHub Actions

## Installation & Running
```bash
pip install -r requirements.txt
streamlit run app/main.py
