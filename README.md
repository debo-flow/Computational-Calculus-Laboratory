# Computational Calculus Laboratory

**Milestone 25 — FEATURE-COMPLETE UNIFIED COMPUTATIONAL CALCULUS LABORATORY**

## Project Overview
The Computational Calculus Laboratory is a comprehensive, production-grade, extensible Python-based interactive mathematics environment. 

Milestone 25 represents the culmination of the project. It fuses 24 independent mathematical laboratories into a singular, cohesive computational engine. It features a master routing workflow, automatic problem classification, continuous integration safety, and a unified API that strictly delineates exact symbolic proof from empirical numerical observation.

---

## 🧭 Master Calculus Workflow
Input parsing is fully automated via the `CalculusEngine` Facade. The system executes the following pipeline:
`INPUT` $\rightarrow$ `Safe Parse` $\rightarrow$ `Auto-Classify` $\rightarrow$ `Domain Extractor` $\rightarrow$ `Engine Route` $\rightarrow$ `Solve` $\rightarrow$ `Cross-Validate` $\rightarrow$ `JSON Report`

---

## 🧮 Mathematical Capabilities (Milestones 1–25)

* **Core Calculus (M1-M7):** Exact limits, continuity mapping, automated symbolic differentiation, applications (MVT, Extrema), and indefinite/definite symbolic integration via FTC.
* **Numerical Analysis (M6, M8, M22):** Adaptive Quadrature, Richardson Extrapolation, High-Precision arbitrary floats, algorithmic Condition Numbers ($K$), and Truncation error bounding.
* **Sequences, Series & Taylor (M9-M10):** Convergence tests (Ratio/Root/Integral), discrete partial sums, and rigorously bounded polynomial remainder approximations (Lagrange error).
* **Multivariable & Multiple Integrals (M11-M12):** Jacobian coordinate transformations, Hessians, constrained Lagrange optimization, and stochastic Monte Carlo volume bounding.
* **Vector Calculus (M13):** Divergence, Curl, Flux line/surface integrals, and computational verification of Green's, Stokes', and the Divergence Theorems.
* **Differential Equations & Dynamical Systems (M14-M19):** Analyzes linear/exact/Bernoulli forms, evaluates BVPs (Shooting/Finite Difference), integrates Stiff PDEs (BDF), and visualizes Chaotic Phase Spaces (Nullclines, Eigenvalue Stability).
* **Calculus of Variations (M20):** Symbolically derives Euler-Lagrange extremals and numerically optimizes discretized functionals $J[y]$.
* **Tensor Calculus & Differential Geometry (M21):** Computes Christoffel symbols, Riemannian/Ricci curvatures, Geodesic trajectories, and intrinsic Gaussian surface curvatures from arbitrary metrics.
* **Symbolic CAS & Verification (M23-M24):** A sandboxed algebraic parser governing rigorous mathematical identity verification, equivalence testing, and automated performance benchmarking.

---

## 🖥️ Unified Architecture
* `calculus/core/`: The centralized `CalculusEngine` API and `pipeline.py` workflow manager.
* `calculus/{subsystems}/`: 10+ independent mathematical physics and symbolic engines.
* `numerical/`: Robust floating-point, ODE stepper, and linear algebra backends.
* `visualization/`: Unified Matplotlib plotting interfaces for Phase Spaces, 3D Tensors, and Error Curves.
* `tests/`: Extensive Pytest integration tracking numerical regression and mathematical accuracy.

## 🚀 Installation & Usage

**1. Install Dependencies**
```bash
pip install -r requirements.txt
```

**2. Launch Unified Interactive UI (Streamlit)**
Features both **Beginner Mode** (simplified outputs with educational steps) and **Research Mode** (exposing Jacobian matrices, tolerances, numerical residuals, and JSON exports).
```bash
streamlit run app/main.py
```

**3. Use the Command Line Interface (CLI)**
```bash
python app.py analyze "x^2 * sin(x)"
python app.py diff "exp(x^2)" --var x
python app.py int "2*x"
```

## 🛡️ Mathematical Philosophy & Safety
1. **No Untrusted Execution:** All string expressions bypass `eval()` via strict AST SymPy dictionary whitelisting (`safe_parse`).
2. **Confidence Classification:** The application UI explicitly tags outputs as `EXACT SYMBOLIC`, `NUMERICAL APPROXIMATION`, or `INCONCLUSIVE`. **Computational verification is never presented as formal mathematical proof.**
3. **No Fake Precision:** Algorithms safely reject indeterminate forms and halt on stiff ODE blow-ups, emitting exact condition warnings rather than silent truncations.

## 🧪 Testing & Continuous Integration (CI)
The project utilizes GitHub Actions to execute a complete regression matrix on every push, ensuring foundational limits (M1) remain unbroken by Tensor geometry additions (M21).
```bash
pytest tests/ -m "not benchmark"
```

---
*Status: FEATURE-COMPLETE COMPUTATIONAL CALCULUS LABORATORY.*
