# Computational Calculus Laboratory

**An Interactive Computational Environment for Symbolic, Numerical, and Visual Exploration of Calculus.**

![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![SymPy](https://img.shields.io/badge/SymPy-Symbolic_CAS-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-Array_Computing-orange.svg)
![SciPy](https://img.shields.io/badge/SciPy-Scientific_Algorithms-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive_UI-red.svg)
![Pytest](https://img.shields.io/badge/Pytest-Automated_Validation-yellowgreen.svg)

[**Overview**](#1-project-overview) | [**Capabilities**](#2-complete-mathematical-capabilities) | [**Architecture**](#3-symbolic-and-numerical-computation-architecture) | [**Examples**](#5-mathematical-examples) | [**Installation**](#6-installation-and-setup) | [**Testing**](#8-testing-and-scientific-validation) | [**Milestones**](#11-roadmap-and-milestone-history)

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Complete Mathematical Capabilities](#2-complete-mathematical-capabilities)
3. [Symbolic and Numerical Computation Architecture](#3-symbolic-and-numerical-computation-architecture)
4. [Interactive Laboratory Features](#4-interactive-laboratory-features)
5. [Mathematical Examples](#5-mathematical-examples)
6. [Installation and Setup](#6-installation-and-setup)
7. [Project Architecture](#7-project-architecture)
8. [Testing and Scientific Validation](#8-testing-and-scientific-validation)
9. [Benchmarks and Performance](#9-benchmarks-and-performance)
10. [Mathematical Reliability and Limitations](#10-mathematical-reliability-and-limitations)
11. [Roadmap and Milestone History](#11-roadmap-and-milestone-history)
12. [Contribution Guidelines](#12-contribution-guidelines)
13. [License and Acknowledgements](#13-license-and-acknowledgements)
14. [Frequently Asked Questions (FAQ)](#14-frequently-asked-questions-faq)

---

## 1. Project Overview

**Computational Calculus Laboratory** is a modular, Python-based scientific computing and mathematical experimentation platform. It integrates exact symbolic manipulation, finite-precision numerical analysis, geometric visualization, and automated theorem verification into a unified computational architecture.

### Purpose and Scope
Standard calculators and black-box solvers often obscure the distinction between an exact analytical derivation and a floating-point numerical approximation. This project was developed to bridge that pedagogical and computational gap by exposing intermediate symbolic steps, truncation residuals, conditioning metrics, and convergence behaviors alongside final results.

### Core Pillars
* **Symbolic Computation:** Manipulates mathematical expressions as exact Abstract Syntax Trees (ASTs) without floating-point rounding, enabling exact differentiation, integration, algebraic factorization, and identity simplification.
* **Numerical Computation:** Approximates intractable integrals, differential equations, and variational functionals using discrete grid stepping, adaptive quadrature, and iterative optimization.
* **Mathematical Visualization:** Renders 2D function profiles, slope fields, phase portraits with nullclines, 3D parametric surfaces, and intrinsic Gaussian curvature colormaps.
* **Theorem Verification & Validation:** Cross-checks dual computational pathways (such as line integrals against double integrals in Green's Theorem) and conducts Monte Carlo counterexample searches.

### Symbolic Mathematics vs. Numerical Approximation
| Dimension | Symbolic Computation | Numerical Approximation |
| :--- | :--- | :--- |
| **Representation** | Exact algebraic trees ($\pi, \sqrt{2}, e^x$) | IEEE 754 floating-point numbers or arbitrary-precision decimals |
| **Error Profile** | Zero rounding or truncation error | Subject to round-off, underflow/overflow, and discretization truncation |
| **Primary Strength** | Closed-form solutions, exact identities, parameter dependency | Solving non-elementary integrals, nonlinear ODE systems, and stiff BVPs |
| **Epistemological Status** | Exact analytical derivation | Empirical approximation requiring error bounds and convergence checks |

> **Epistemological Disclaimer:** Computational Calculus Laboratory is an educational and scientific exploration environment. Numerical agreement, visual phase trajectories, and empirical Monte Carlo validations provide computational evidence, **not** formal mathematical proof.

---

## 2. Complete Mathematical Capabilities

The laboratory is organized into specialized mathematical subsystems built across 25 incremental milestones.

### A. Function Analysis and Symbolic CAS (`calculus/functions/`, `calculus/symbolic/`)
* **Sandboxed Expression Parsing:** Converts user strings into SymPy expressions via `safe_parse`, stripping `__builtins__` to prevent arbitrary code execution.
* **Algebraic Manipulation:** Supports `expand`, `factor`, `collect`, `cancel`, `together`, and partial fraction decomposition (`apart`).
* **Polynomial & Complexity Analytics:** Extracts polynomial degree, leading coefficients, AST node counts, and expression tree depth.
* **Domain & Singularity Detection:** Identifies real continuous domains (`ContinuousDomain`) and isolated singularities.
* **Assumption-Aware Evaluation:** Applies explicit domain constraints (e.g., $x \in \mathbb{R}^+$) to evaluate conditional identities such as $\sqrt{x^2} = x$.

### B. Limits and Continuity (`calculus/limits/`, `calculus/continuity/`)
* **Symbolic Limits:** Evaluates one-sided ($x \to a^+$, $x \to a^-$), two-sided, and infinite limits ($\lim_{x \to \infty} f(x)$).
* **Continuity Verification:** Checks point continuity by comparing $\lim_{x \to a} f(x)$ against the evaluated function value $f(a)$.
* **Multivariable Path Exploration:** Tests path-dependent limit behavior along parameterized trajectories.

### C. Differential Calculus and Applications (`calculus/differentiation/`, `calculus/applications/`)
* **Symbolic Differentiation:** Computes first-order and higher-order derivatives $\frac{d^n f}{dx^n}$ via `CASRouter`.
* **Numerical Differentiation:** Implements forward, backward, and central finite differences alongside **Richardson Extrapolation** ($A \approx \frac{4D(h/2) - D(h)}{3}$) to eliminate leading-order truncation error.
* **Analytical Applications:** Supports critical-point detection, tangent/normal line construction, and extremum analysis.

### D. Integral Calculus (`calculus/integration/`, `numerical/integration/`)
* **Symbolic Integration:** Computes indefinite antiderivatives $\int f(x)\,dx$ and exact definite integrals $\int_a^b f(x)\,dx$.
* **Numerical Quadrature:** Provides composite Trapezoidal, Simpson's rule, and adaptive quadrature routines for non-elementary integrands, paired with residual and truncation error reporting.

### E. Sequences, Series, and Taylor Expansions (`calculus/sequences/`, `calculus/series/`, `calculus/taylor/`)
* **Infinite Series & Sequences:** Evaluates partial sums and convergence characteristics.
* **Taylor & Maclaurin Polynomials:** Generates $n$-th order symbolic series expansions around $x = a$ (`sp.series(...).removeO()`) and evaluates remainder error bounds $E_n(x) = \vert{}f(x) - T_n(x)\vert{}$.

### F. Multivariable Calculus (`calculus/multivariable/`)
* **Partial Differentiation:** Computes first-order and mixed higher-order partial derivatives.
* **Differential Operators:** Constructs symbolic Gradient vectors ($\nabla f$), Jacobian matrices ($J$), and Hessian matrices ($H$) for scalar and vector-valued mappings.
* **Multiple Integrals:** Evaluates iterated double/triple integrals and stochastic Monte Carlo volume estimates.

### G. Vector Calculus (`calculus/vector_calculus/`)
* **Field Operators:** Computes symbolic Divergence ($\nabla \cdot \mathbf{F}$), Curl ($\nabla \times \mathbf{F}$), and the scalar/vector **Laplacian** ($\nabla^2 f = \sum \frac{\partial^2 f}{\partial x_i^2}$).
* **Integral Theorems:** Provides computational verification workflows comparing boundary line integrals against surface/area integrals (e.g., Green's Theorem).

### H. Differential Equations and Dynamical Systems (`calculus/differential_equations/`, `numerical/ode_solvers.py`)
* **ODE Classification:** Automatically classifies ODE order, linearity, homogeneity, autonomy, separability, exactness, and Bernoulli structure.
* **First-Order Analytical Solvers:**
  * *Exact Equations:* Verifies $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ and constructs potential functions $F(x,y) = C$.
  * *Bernoulli Equations:* Applies the transformation $v = y^{1-n}$ to linearize $\frac{dy}{dx} + P(x)y = Q(x)y^n$ and solves via integrating factors $\mu(x) = e^{\int (1-n)P(x)\,dx}$.
  * *Residual Verification:* Substitutes symbolic `dsolve` outputs back into the ODE to confirm $LHS - RHS = 0$.
* **Second-Order & Matrix Systems:** Solves constant-coefficient homogeneous equations ($ay'' + by' + cy = 0$) via characteristic roots (distinct real, repeated real, complex conjugate) and analyzes 2D linear matrix systems ($\mathbf{X}' = \mathbf{A}\mathbf{X}$) using trace-determinant stability criteria.
* **Numerical IVP & BVP Solvers:**
  * Fixed-step explicit solvers: **Euler**, **Heun (Improved Euler)**, **Midpoint (RK2)**, **RK3**, and **Classical RK4**.
  * Adaptive and stiff solvers: Wraps SciPy `solve_ivp` supporting explicit **RK45** and implicit **BDF** (Backward Differentiation Formula) for stiff systems such as the high-$\mu$ Van der Pol oscillator.
  * Boundary Value Problems (BVPs): Implements the **Secant Shooting Method** (`basic_shooting_method`) to convert two-point BVPs ($y(a)=\alpha, y(b)=\beta$) into iterative IVPs.
* **Phase Space & Nonlinear Dynamics:**
  * Solves $\mathbf{F}(\mathbf{X}) = \mathbf{0}$ for equilibrium points and linearizes via the Jacobian $J(\mathbf{X}^*)$ to classify nodes, saddles, spirals, and centers.
  * Computes and plots normalized direction fields, phase portraits, and $dx/dt = 0, dy/dt = 0$ nullclines.
  * Evaluates trajectory separation $D(t) = \Vert{}\mathbf{X}_1(t) - \mathbf{X}_2(t)\Vert{}$ for nearby initial states ($\mathbf{X}_0 + \delta\mathbf{X}$) and verifies conservation invariants via $\frac{dI}{dt} = \nabla I \cdot \mathbf{F} = 0$.

### I. Calculus of Variations (`calculus/variations/`)
* **Symbolic Euler–Lagrange Engine:** Derives $\frac{\partial F}{\partial y} - \frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right) + \frac{d^2}{dx^2}\left(\frac{\partial F}{\partial y''}\right) = 0$ for functionals $J[y] = \int_a^b F(x, y, y', y'')\,dx$.
* **First Variation & Perturbations:** Symbolically expands $\delta J = \left.\frac{d}{d\epsilon} J[y + \epsilon\eta]\right\vert{}_{\epsilon=0}$.
* **Constrained Functionals:** Constructs modified Lagrangians $H = F + \lambda G$ for isoperimetric problems.
* **Direct Numerical Minimization:** Discretizes $J[y]$ over a finite spatial grid using central differences and Simpson's rule, optimizing interior nodes via SciPy's `BFGS` algorithm and plotting the local Euler–Lagrange residual $R(x)$.

### J. Tensor Calculus and Differential Geometry (`calculus/tensor_geometry/`)
* **Metric & Index Management:** Tracks covariant (lower) and contravariant (upper) indices, validates Einstein summation contractions, raises/lowers indices via $g_{ij}$ and $g^{ij}$, and detects singular metrics ($\det(g) = 0$).
* **Christoffel Symbols & Geodesics:** Symbolically derives Christoffel symbols of the second kind:
  $$\Gamma^k_{ij} = \frac{1}{2} g^{kl} \left( \frac{\partial g_{jl}}{\partial x^i} + \frac{\partial g_{il}}{\partial x^j} - \frac{\partial g_{ij}}{\partial x^l} \right)$$
  and generates the coupled geodesic ODEs $\frac{d^2 x^k}{d\lambda^2} + \Gamma^k_{ij} \frac{dx^i}{d\lambda}\frac{dx^j}{d\lambda} = 0$.
* **Riemannian Curvature:** Constructs the rank-4 Riemann tensor $R^i_{jkl}$, contracts to the Ricci tensor $R_{ij} = R^k_{ikj}$, and computes the Scalar Curvature $R = g^{ij}R_{ij}$.
* **Surface Geometry & Differential Forms:** Computes First ($E, F, G$) and Second ($e, f, g$) Fundamental Forms, Gaussian Curvature $K = \frac{eg - f^2}{EG - F^2}$, Mean Curvature $H$, and the exterior derivative $d\omega$ of 1-forms $\omega = P\,dx + Q\,dy + R\,dz$.

### K. Scientific Computing and Theorem Verification (`numerical/scientific/`, `calculus/verification/`)
* **Precision & Conditioning:** Compares 64-bit IEEE 754 floats against arbitrary-precision `mpmath` evaluations and computes relative condition numbers $K = \left\vert{}\frac{x f'(x)}{f(x)}\right\vert{}$.
* **Numerical Linear Algebra:** Computes Singular Value Decomposition ($\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$), rank estimates, condition numbers, and eigenvalue/eigenvector residuals $\Vert{}\mathbf{A}\mathbf{v} - \lambda\mathbf{v}\Vert{}$.
* **Spline Interpolation & PDE Foundations:** Implements natural/clamped Cubic Splines (`CubicSpline`) and a 1D Heat Equation ($u_t = \alpha u_{xx}$) Forward-Time Central-Space (FTCS) solver with strict Courant–Friedrichs–Lewy (CFL) stability enforcement ($\alpha \frac{\Delta t}{\Delta x^2} \le 0.5$).
* **Automated Verification:** Combines symbolic identity verification ($LHS - RHS = 0$) with randomized Monte Carlo counterexample searches (`search_counterexample`).

---

## 3. Symbolic and Numerical Computation Architecture

The platform separates symbolic representation from numerical execution while allowing seamless cross-validation between the two paradigms.

```text
User Input (String)
       │
       ▼
[ safe_parse() ] ──► Sandboxed SymPy AST (Blocks __builtins__ / eval)
       │
       ├──► [ classify_problem() ] ──► Identifies Problem Domain (ODE, Limit, Integral, etc.)
       │
       ├──► SYMBOLIC PIPELINE (SymPy)
       │       ├── Exact Algebraic / Calculus Transformations
       │       ├── Residual Substitution Check (LHS - RHS == 0)
       │       └── Classification: EXACT SYMBOLIC / ANALYTICAL RESULT
       │
       └──► NUMERICAL PIPELINE (NumPy / SciPy / mpmath)
               ├── sp.lambdify()Compilation to Vectorized NumPy Callables
               ├── Grid Stepping (RK4, BDF, BFGS, FTCS, Quadrature)
               ├── Empirical Convergence & Truncation Error Estimation
               └── Classification: NUMERICAL RESULT / APPROXIMATION / EVIDENCE
```

### Role of Core Libraries
* **SymPy:** Powers the Computer Algebra System (`CASRouter`), symbolic ODE classification, Euler–Lagrange derivations, Christoffel symbol generation, and exact identity verification.
* **NumPy:** Provides vectorized array evaluation via `sp.lambdify`, meshgrid construction for phase portraits and 3D surfaces, and finite-difference gradient approximations.
* **SciPy:** Supplies adaptive ODE solvers (`scipy.integrate.solve_ivp` with `RK45` and `BDF`), numerical integration (`simpson`), functional minimization (`scipy.optimize.minimize` via `BFGS`), cubic splines (`CubicSpline`), and matrix decompositions (`scipy.linalg.svd`, `eig`).
* **mpmath:** Enables arbitrary-precision floating-point arithmetic (configurable decimal places `dps`) to measure 64-bit IEEE 754 round-off drift.
* **Matplotlib:** Renders 2D plots, quiver slope fields, streamline phase portraits, log-log convergence charts, and 3D curvature-mapped manifolds.
* **Streamlit:** Serves the interactive web laboratory with stateful session history and dual-mode UI views.

---

## 4. Interactive Laboratory Features

The Streamlit application (`app/main.py`) provides an interactive workbench organized into specialized modules and user interface modes.

### Interface Modes
1. **Beginner Mode (Learning Mode):** Streamlines the interface to focus on core mathematical inputs, formatted LaTeX outputs, visual plots, and conceptual explanations.
2. **Advanced / Research Mode:** Exposes solver configurations, Jacobian matrices, eigenvalue spectra, Euler–Lagrange residual curves, CFL stability parameters, execution timing, and downloadable JSON/Markdown verification reports.

### Core Workbenches Available in UI
* **Home Dashboard & Calculus Knowledge Map:** Overview of all integrated subsystems and epistemological guidelines.
* **Master Workflow & Auto-Analysis:** Accepts general expressions, automatically detects the problem type, extracts continuous real domains, computes results, and exports structured JSON reports.
* **Domain-Specific Laboratories:** Dedicated tabs for Limits, Differentiation, Integration, Series/Taylor, Multivariable/Vector Calculus, ODEs & Phase Space, Calculus of Variations, Tensor Geometry, Scientific Computing, Symbolic CAS Notebook, and Automated Verification.

### Visual Gallery (Placeholders)
> *Note: No static image files are bundled in the repository to keep the codebase lightweight. When running the application locally, screenshots of the generated plots can be added to a `docs/images/` directory and linked below:*
> * `[Placeholder: Phase Portrait & Nullclines of Lotka-Volterra System]`
> * `[Placeholder: 3D Gaussian Curvature Colormap on a Parameterized Torus/Sphere]`
> * `[Placeholder: Numerical vs. Analytical Extremal & Euler-Lagrange Residual Plot]`

---

## 5. Mathematical Examples

All examples below use verified functions and CLI commands implemented in the repository.

### Example 1: Unified Python API — Symbolic Differentiation, Integration, and Validation
Using `CalculusEngine` from `calculus/core/calculus_engine.py`:

```python
from calculus.core.calculus_engine import CalculusEngine

engine = CalculusEngine()

# 1. Symbolic Differentiation
deriv = engine.differentiate("x**3 * sin(x)", "x", order=1)
print("Derivative:", deriv)
# Output: Derivative: x**3*cos(x) + 3*x**2*sin(x)

# 2. Indefinite Integration
integral = engine.integrate("2*x * exp(x**2)", "x")
print("Integral:", integral)
# Output: Integral: exp(x**2)

# 3. Symbolic Identity Validation
validation = engine.validate("sin(x)**2 + cos(x)**2", "1")
print("Validation:", validation)
# Output: Validation: {'LHS': 'sin(x)**2 + cos(x)**2', 'RHS': '1', 'Simplified Difference': '0', 'Status': 'SYMBOLICALLY VERIFIED'}
```

### Example 2: Command-Line Interface (CLI) Workflow
Using the root `app.py` entry point:

```bash
# Run the master auto-classification and domain analysis pipeline
python app.py analyze "x^2 * sin(x)"

# Compute symbolic derivatives and integrals directly from the terminal
python app.py diff "exp(x^2)" --var x
python app.py int "2*x" --var x
```

### Example 3: Calculus of Variations — Symbolic & Numerical Extremal
Finding the shortest path between $(0,0)$ and $(1,1)$ using `calculus/variations/`:

```python
from calculus.variations.functional import Functional
from calculus.variations.euler_lagrange import derive_euler_lagrange
from calculus.variations.numerical_variations import numerical_functional_optimization

# Define arc-length functional J[y] = \int \sqrt{1 + (y')^2} dx
func = Functional("sqrt(1 + yp**2)")

# Derive symbolic Euler-Lagrange equation
el_eq = derive_euler_lagrange(func)
print("Euler-Lagrange Equation:", el_eq["EL Equation"])

# Minimize numerically over 20 discretized grid nodes with fixed endpoints (0,0) -> (1,1)
opt_res = numerical_functional_optimization(func, a=0.0, b=1.0, A=0.0, B=1.0, N=20)
print(f"Status: {opt_res['Status']}, Minimum J[y]: {opt_res['J_min']:.6f}")
# Output: Status: Converged, Minimum J[y]: 1.414214 (Approximates sqrt(2))
```

### Example 4: Differential Geometry — Christoffel Symbols & Gaussian Curvature
Computing polar connection coefficients and spherical curvature using `calculus/tensor_geometry/`:

```python
import sympy as sp
from calculus.tensor_geometry.christoffel import compute_christoffel_symbols
from calculus.tensor_geometry.differential_geometry import compute_surface_geometry

# 1. Christoffel symbols for 2D Polar Metric g_ij = diag(1, r^2)
r, theta = sp.symbols("r theta")
g = sp.Matrix([[1, 0], [0, r**2]])
Gamma = compute_christoffel_symbols(g, g.inv(), [r, theta])
print("Gamma^r_{theta,theta}:", Gamma[0][1][1])      # Output: -r
print("Gamma^theta_{r,theta}:", Gamma[1][0][1])      # Output: 1/r

# 2. Gaussian Curvature of a Sphere of Radius R
surf = compute_surface_geometry("R*cos(u)*sin(v)", "R*sin(u)*sin(v)", "R*cos(v)", "u, v")
print("Gaussian Curvature K:", surf["Gaussian Curvature (K)"])
# Output: Gaussian Curvature K: 1/R**2
```

### Example 5: Theorem Verification — Green's Theorem
Verifying $\oint_C (P\,dx + Q\,dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$ on $[0,1] \times [0,1]$:

```python
from calculus.verification.theorem_verification import verify_greens_theorem

res = verify_greens_theorem(P_str="-y", Q_str="x", x_bnds=(0, 1), y_bnds=(0, 1))
print(res["LHS (Line Integral)"], "==", res["RHS (Surface Integral)"], "->", res["Status"])
# Output: 2 == 2 -> SYMBOLICALLY VERIFIED
```

---

## 6. Installation and Setup

### System Requirements
* **Python:** Version `3.9` or higher (verified in `.github/workflows/verification.yml`).
* **Core Dependencies:** `sympy`, `numpy`, `scipy`, `mpmath`, `matplotlib`, `streamlit`, `pandas`, `pytest`.
* **Operating System:** Cross-platform (Linux, macOS, Windows).

### Step-by-Step Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/debo-flow/Computational-Calculus-Laboratory.git](https://github.com/debo-flow/Computational-Calculus-Laboratory.git)
   cd Computational-Calculus-Laboratory
   ```

2. **Create and Activate a Virtual Environment:**
   * **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * **Windows (Command Prompt / PowerShell):**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Required Dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Launching the Application

* **Launch the Interactive Streamlit Web Laboratory:**
  ```bash
  streamlit run app/main.py
  ```
  The application will open automatically in your default browser at `http://localhost:8501`.

* **Run the Command-Line Interface (CLI):**
  ```bash
  python app.py --help
  ```

### Troubleshooting Common Issues
* **`ModuleNotFoundError: No module named 'calculus'`:** Ensure you are executing commands from the root directory (`Computational-Calculus-Laboratory/`). If running scripts from a subdirectory, set your Python path: `export PYTHONPATH=$(pwd)` (Linux/macOS) or `set PYTHONPATH=%cd%` (Windows).
* **`mpmath` Missing Error:** While SymPy bundles an internal version of `mpmath`, Milestone 22 imports `mpmath` directly for arbitrary-precision benchmarking. Run `pip install mpmath` if not present in your environment.
* **Matplotlib Backend Warnings in Streamlit:** Always pass Matplotlib `Figure` objects directly to `st.pyplot(fig)` rather than calling `plt.show()`.

---

## 7. Project Architecture

The repository enforces a modular separation of concerns across mathematical computation, numerical solvers, visualization, user interfaces, and automated verification:

```text
Computational-Calculus-Laboratory/
│
├── app.py                                     # CLI entry point (analyze, diff, int)
├── requirements.txt                           # Python package dependencies
├── README.md                                  # Project documentation
│
├── .github/
│   └── workflows/
│       └── verification.yml                   # GitHub Actions CI regression workflow
│
├── app/
│   └── main.py                                # Unified Streamlit web application
│
├── calculus/                                  # Core Symbolic & Analytical Subsystems
│   ├── core/                                  # Master orchestration layer (M25)
│   │   ├── calculus_engine.py                 # Unified Python API facade
│   │   ├── classifier.py                      # Regex-based mathematical problem classifier
│   │   └── pipeline.py                        # End-to-end execution & reporting workflow
│   ├── functions/                             # Function representation & domain analysis
│   ├── limits/                                # Symbolic & path-based limit engines
│   ├── continuity/                            # Point & interval continuity analyzers
│   ├── differentiation/                       # Symbolic derivative engines
│   ├── applications/                          # Extrema, tangent/normal, MVT analysis
│   ├── integration/                           # Indefinite & definite symbolic integration
│   ├── sequences/                             # Sequence term & limit analysis
│   ├── series/                                # Infinite series & convergence tests
│   ├── taylor/                                # Taylor/Maclaurin polynomials & error bounds
│   ├── multivariable/                         # Partial derivatives, gradients, Jacobians, Hessians
│   ├── vector_calculus/                       # Divergence, curl, flux & integral theorems
│   ├── differential_equations/                # ODE classification, symbolic & phase-space analysis
│   │   ├── first_order.py                     # Exact & Bernoulli equation solvers
│   │   ├── second_order.py                    # Characteristic equation & root classification
│   │   ├── symbolic_solver.py                 # SymPy dsolve wrapper with residual verification
│   │   ├── numerical_solver.py                # Euler, Heun, RK2, RK3, RK4 & adaptive wrappers
│   │   ├── boundary_value.py                  # Secant shooting method for BVPs
│   │   ├── systems.py                         # 2D matrix systems & classical dynamical models
│   │   ├── equilibrium.py                     # Autonomous equilibrium root finder
│   │   ├── stability.py                       # Jacobian linearization & eigenvalue classifier
│   │   ├── phase_portraits.py                 # Vector grid & nullcline contour generator
│   │   ├── direction_fields.py                # Normalized slope field computation
│   │   └── ode_analysis.py                    # Conservation laws, sensitivity & convergence order
│   ├── variations/                            # Calculus of Variations Laboratory (M20)
│   │   ├── functional.py                      # Functional representation & trial evaluation
│   │   ├── euler_lagrange.py                  # First & higher-order Euler-Lagrange derivation
│   │   ├── variational_derivatives.py         # First variation (\delta J) perturbation engine
│   │   ├── extremals.py                       # Symbolic extremal ODE solver
│   │   ├── constraints.py                     # Isoperimetric Lagrange multiplier setup
│   │   ├── numerical_variations.py            # Direct BFGS discretized functional optimizer
│   │   └── variation_analysis.py              # Discretized Euler-Lagrange residual calculator
│   ├── tensor_geometry/                       # Tensor Calculus & Differential Geometry (M21)
│   │   ├── indices.py                         # Upper/lower index formatting & contraction checks
│   │   ├── tensor.py                          # Rank-N tensor container
│   │   ├── metric.py                          # Metric determinant, inverse & index raising/lowering
│   │   ├── christoffel.py                     # Christoffel symbols of the second kind
│   │   ├── curvature.py                       # Riemann, Ricci & Scalar curvature tensors
│   │   ├── geodesics.py                       # Symbolic geodesic ODE generator
│   │   ├── differential_geometry.py           # 1st/2nd fundamental forms, Gaussian/Mean curvature
│   │   └── geometry_analysis.py               # 1-form exterior derivative (wedge product)
│   ├── symbolic/                              # Computer Algebra System Layer (M23)
│   │   ├── expression_parser.py               # Safe AST parser blocking arbitrary code execution
│   │   ├── assumptions.py                     # Symbol assumption binding (real, positive, integer)
│   │   ├── algebra.py                         # Expand, factor, collect, cancel, apart, poly info
│   │   ├── equations.py                       # Exact equation, system & inequality solvers
│   │   ├── substitutions.py                   # Simultaneous symbolic substitution engine
│   │   ├── expression_analysis.py             # Complexity metrics, AST tree & domain extraction
│   │   ├── symbolic_validation.py             # Equivalence proof & random sample cross-check
│   │   └── symbolic_engine.py                 # Central CASRouter facade
│   └── verification/                          # Automated Theorem Verification Layer (M24)
│       ├── error_analysis.py                  # Absolute, relative, RMS error & convergence order
│       ├── symbolic_verification.py           # Exact identity verification (LHS - RHS == 0)
│       ├── numerical_verification.py          # Monte Carlo counterexample search
│       ├── theorem_verification.py            # Computational Green's Theorem verifier
│       └── verification_report.py             # JSON and Markdown report serializer
│
├── numerical/                                 # Numerical Methods & Scientific Computing
│   ├── validation.py                          # Numerical error helpers
│   ├── root_finding.py                        # Nonlinear root-finding routines
│   ├── ode_solvers.py                         # Unified fixed-step & adaptive ODE solvers
│   ├── differentiation/                       # Finite-difference derivative modules
│   ├── integration/                           # Numerical quadrature modules
│   └── scientific/                            # Scientific Computing Laboratory (M22)
│       ├── precision.py                       # 64-bit float vs. mpmath arbitrary precision
│       ├── error_analysis.py                  # Absolute & relative condition number (K) calculator
│       ├── differentiation.py                 # Richardson extrapolation engine
│       ├── linear_algebra.py                  # SVD (rank, conditioning) & Eigenvalue residual analysis
│       ├── interpolation.py                   # Cubic spline interpolation wrapper
│       ├── numerical_engine.py                # 1D Heat Equation FTCS solver & CFL stability check
│       └── benchmarking.py                    # Execution timer & hardware reproducibility wrapper
│
├── benchmarks/                                # Performance & Scaling Suite
│   └── benchmark_calculus.py                  # Iterative timing & polynomial derivative scaling
│
├── visualization/                             # Matplotlib Plotting Engines
│   ├── ode_plots.py                           # Phase portraits, nullclines, 3D trajectories
│   ├── dynamical_system_plots.py              # Direction fields & multi-solver comparisons
│   ├── variation_plots.py                     # Extremal comparisons & EL residual plots
│   ├── tensor_geometry_plots.py               # 3D Gaussian curvature surface colormaps
│   ├── scientific_computing_plots.py          # Cubic splines & 1D Heat PDE evolution plots
│   └── verification_plots.py                  # Log-log error scaling & runtime benchmark curves
│
└── tests/                                     # Automated Pytest Regression Suite
    ├── test_differential_equations.py         # ODE solvers, BVP, stability & conservation tests
    ├── test_variations.py                     # Functional evaluation, EL & BFGS optimization tests
    ├── test_tensor_geometry.py                # Metric, Christoffel, curvature & exterior form tests
    ├── test_scientific_computing.py           # Precision, SVD, Richardson & PDE CFL tests
    ├── test_symbolic_cas.py                   # Safe parser, algebra, inequality & router tests
    ├── test_verification.py                   # Identity, counterexample & Green's theorem tests
    └── test_core_pipeline.py                  # Classifier, master pipeline & unified API tests
```

---

## 8. Testing and Scientific Validation

The repository uses **Pytest** for automated unit, integration, and mathematical regression testing, backed by a GitHub Actions Continuous Integration workflow (`.github/workflows/verification.yml`).

### Running the Test Suite
```bash
# Run the complete regression test suite (excluding slow performance benchmarks)
pytest tests/ -m "not benchmark" --maxfail=10 --disable-warnings

# Run a specific subsystem test module
pytest tests/test_differential_equations.py
pytest tests/test_tensor_geometry.py
pytest tests/test_verification.py
```

### Validation Methodology
1. **Symbolic Residual Verification:** Analytical ODE and Euler–Lagrange solutions are substituted back into the governing operator $\mathcal{L}[y] - f(x)$ and simplified symbolically to verify that the residual equals zero.
2. **Empirical Order of Convergence ($p$):** Numerical ODE solvers (`Euler`, `Heun`, `Midpoint`, `RK4`) are tested across successively halved step sizes ($h, h/2, h/4, h/8$) against exact analytical references ($y' = y \implies y = e^x$) to verify that the observed convergence rate $p \approx \frac{\log(E_1/E_2)}{\log(h_1/h_2)}$ matches theoretical expectations.
3. **Result Confidence Classification:** The pipeline explicitly categorizes outputs to prevent misinterpreting numerical approximations as formal proofs:
   * `EXACT SYMBOLIC RESULT` / `SYMBOLICALLY VERIFIED`
   * `ANALYTICAL RESULT`
   * `NUMERICAL RESULT` / `APPROXIMATION`
   * `EMPIRICALLY VALIDATED` (`NO COUNTEREXAMPLE FOUND IN TESTED DOMAIN`)
   * `INCONCLUSIVE` / `FAILED`

---

## 9. Benchmarks and Performance

The `benchmarks/benchmark_calculus.py` and `numerical/scientific/benchmarking.py` modules collect execution timing and algorithmic scaling data without making hardware-dependent universal performance claims.

### What is Benchmarked
* **Symbolic AST Scaling (`scaling_test_polynomial_derivative`):** Measures how SymPy differentiation runtime scales as polynomial degree increases from $N = 10$ to $N = 200$.
* **Solver Convergence vs. Evaluations:** Tracks function evaluation counts (`nfev`), accepted steps, and wall-clock execution time (`time.perf_counter()`) across explicit (`RK45`) and implicit (`BDF`) adaptive ODE integrators.
* **Reproducibility Metadata (`generate_scientific_report`):** Wraps numerical executions (such as SVD decomposition) with hardware architecture (`platform.machine()`), Python version, NumPy version, and high-resolution execution timestamps.

---

## 10. Mathematical Reliability and Limitations

Users and developers should interpret all computational outputs within the theoretical constraints of computer algebra and numerical analysis:

1. **IEEE 754 Floating-Point Precision:** Standard numerical routines operate in 64-bit double precision ($\approx 15\text{–}17$ significant decimal digits, machine epsilon $\epsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$). Subtracting nearly equal numbers causes catastrophic cancellation. Use the Milestone 22 `mpmath` precision comparator to inspect round-off drift.
2. **Problem Conditioning vs. Algorithm Stability:** A high relative condition number $K = \left|\frac{x f'(x)}{f(x)}\right|$ indicates that the mathematical problem itself is sensitive to input perturbations, regardless of the numerical algorithm used.
3. **Finite-Difference Truncation vs. Round-Off Trade-Off:** Decreasing step size $h$ in finite-difference differentiation reduces truncation error $\mathcal{O}(h^2)$ but amplifies floating-point division round-off $\mathcal{O}(\epsilon_{\text{mach}}/h)$.
4. **Explicit PDE and ODE Stiffness Limits:** Explicit time-stepping schemes (Euler, RK4, FTCS Heat solver) become numerically unstable if step sizes violate stability bounds (such as the CFL condition $\alpha \frac{\Delta t}{\Delta x^2} \le 0.5$). Stiff systems require implicit solvers (`BDF`).
5. **Linearization Inconclusiveness:** Jacobian eigenvalue stability analysis ($\mathbf{u}' = \mathbf{J}(\mathbf{X}^*)\mathbf{u}$) is strictly local (Hartman–Grobman theorem). Non-hyperbolic equilibria (where eigenvalues have zero real parts, such as centers) are explicitly flagged as `Linearization Inconclusive globally`.
6. **Undecidability of Symbolic Simplification:** By Richardson's theorem, determining whether an arbitrary symbolic expression $A - B$ equals zero is undecidable in general. Failure of `sp.simplify(A - B)` to reach `0` does not strictly disprove an identity, and failure of Monte Carlo sampling to find a counterexample does not prove one.

---

## 11. Roadmap and Milestone History

The repository was engineered across 25 structured milestones, progressing from foundational single-variable calculus to a unified scientific computing platform.

| Milestone | Subsystem / Laboratory Title | Key Implemented Capabilities |
| :---: | :--- | :--- |
| **M1** | Core Foundation & Function Engine | Safe expression parsing, domain extraction, parity, function evaluation tables |
| **M2** | Limits Laboratory | One-sided, two-sided, and infinite symbolic limits; numerical table sequences |
| **M3** | Continuity & Discontinuity | Point continuity verification, jump/removable/infinite discontinuity detection |
| **M4** | Advanced Differential Calculus | First and higher-order symbolic derivatives, chain/product/quotient routing |
| **M5** | Applications of Differential Calculus | Critical points, extrema classification, tangent/normal lines, MVT analysis |
| **M6** | Advanced Numerical Differentiation | Forward, backward, central finite differences; step-size truncation analysis |
| **M7** | Advanced Integral Calculus | Symbolic indefinite and definite integration via the Fundamental Theorem of Calculus |
| **M8** | Advanced Numerical Integration | Trapezoidal, Simpson's, and adaptive quadrature with error bounding |
| **M9** | Advanced Sequences & Infinite Series | Sequence convergence, partial sum trajectories, ratio/root/integral tests |
| **M10** | Advanced Taylor & Maclaurin Series | Symbolic polynomial expansion around $x=a$, Lagrange remainder error analysis |
| **M11** | Multivariable Calculus | Partial derivatives, directional derivatives, symbolic Gradients, Jacobians, Hessians |
| **M12** | Multiple Integrals | Iterated double/triple integration, coordinate Jacobians, Monte Carlo volume estimation |
| **M13** | Advanced Vector Calculus | Divergence, Curl, Line/Surface flux integrals, Green's/Stokes'/Divergence theorems |
| **M14** | Dynamical Systems Foundation | Autonomous equilibrium finding, Jacobian linearization, 2D phase portraits |
| **M15** | Boundary Value Problems & First-Order ODEs | Secant shooting method, finite-difference BVP foundation, isoclines, exact ODEs |
| **M16** | Matrix Systems, Chaos & Stiffness | Constant-coefficient 2nd-order ODEs, $2\times 2$ matrix systems, conservation laws, BDF stiff solver |
| **M17** | Convergence & Bifurcation Foundation | Empirical convergence order ($p$) benchmarking, nullcline contours, parameter sweeps |
| **M18** | Full Runge-Kutta Suite & Direction Fields | Explicit Euler, Heun, RK2, RK3, RK4 steppers; normalized quiver slope fields |
| **M19** | Advanced ODE Deep Analysis | Bernoulli transformation solver, potential function construction, classical model sandbox |
| **M20** | Calculus of Variations Laboratory | Symbolic Euler–Lagrange derivation, first variation $\delta J$, BFGS discretized optimization |
| **M21** | Tensor Calculus & Differential Geometry | Metric tensors, Christoffel symbols, Riemann/Ricci/Scalar curvature, surface $K$ & $H$, 1-forms |
| **M22** | Scientific Computing Laboratory | `mpmath` precision comparison, condition numbers, Richardson extrapolation, SVD/Eigen, 1D Heat PDE CFL |
| **M23** | Symbolic Mathematics & CAS Layer | Sandboxed `safe_parse`, assumption binding, inequality solver, AST tree builder, stateful CAS Notebook |
| **M24** | Automated Verification & Benchmarking | Symbolic identity prover, Monte Carlo counterexample search, AST scaling benchmarks, GitHub CI |
| **M25** | Unified Computational Calculus Laboratory | `CalculusEngine` API facade, regex problem classifier, master pipeline, CLI (`app.py`), unified UI |

### Planned Future Directions (Post-Milestone 25)
The following enhancements are planned for future iterations and are **not** yet implemented:
* **2D Elliptic & Hyperbolic PDE Solvers:** Extending the 1D Heat FTCS foundation to 2D Poisson/Laplace relaxation and wave propagation grids.
* **Symplectic Integrators:** Adding leapfrog and Verlet integrators for long-term Hamiltonian energy conservation in orbital and mechanical systems.
* **Interactive Plotly 3D Backend:** Providing optional WebGL rotation for 3D phase-space attractors and Riemannian curvature manifolds.

---

## 12. Contribution Guidelines

Contributions that improve mathematical rigor, numerical stability, test coverage, or educational clarity are welcome.

### Development Workflow
1. **Fork and Clone:** Fork the repository and create a feature branch (`git checkout -b fix/ode-singular-jacobian` or `git checkout -b feat/symplectic-euler`).
2. **Preserve Architectural Modularity:**
   * Place symbolic algorithms in `calculus/<subsystem>/`.
   * Place floating-point numerical routines in `numerical/`.
   * Place Matplotlib rendering functions in `visualization/` (always return a `matplotlib.figure.Figure` object; never call `plt.show()` inside library modules).
3. **Mathematical & Security Standards:**
   * Never use Python's raw `eval()` or `exec()` on user inputs; route all string parsing through `calculus.symbolic.expression_parser.safe_parse`.
   * Clearly label whether an algorithm produces an exact symbolic result or a numerical approximation.
   * Handle division-by-zero, singular matrices, and solver divergence gracefully with descriptive status messages.
4. **Testing Requirements:**
   * Add unit and analytical reference tests in `tests/` for every new mathematical function.
   * Run `pytest tests/ -m "not benchmark"` locally and ensure all tests pass before opening a Pull Request.

---

## 13. License and Acknowledgements

### License Status
No `LICENSE` file is currently present in the root repository. Under standard copyright law, all rights are reserved by the repository author unless an explicit license file is added. Contributors and users should contact the repository maintainer regarding redistribution or commercial licensing permissions.

### Acknowledgements
Computational Calculus Laboratory builds upon the open-source scientific Python ecosystem:
* [**SymPy**](https://www.sympy.org/) for symbolic mathematics and computer algebra.
* [**NumPy**](https://numpy.org/) and [**SciPy**](https://scipy.org/) for array computing, numerical integration, optimization, and linear algebra.
* [**mpmath**](https://mpmath.org/) for arbitrary-precision floating-point arithmetic.
* [**Matplotlib**](https://matplotlib.org/) for 2D and 3D scientific visualization.
* [**Streamlit**](https://streamlit.io/) for the interactive web application framework.
* [**Pytest**](https://docs.pytest.org/) for automated regression testing.

*(Note: Use of these libraries does not imply official endorsement by their respective maintainers).*

---

## 14. Frequently Asked Questions (FAQ)

**Q: What is Computational Calculus Laboratory?**  
**A:** It is an integrated Python platform combining a symbolic Computer Algebra System (CAS), numerical analysis solvers, 2D/3D mathematical visualization, and automated theorem verification across single-variable calculus, multivariable/vector calculus, differential equations, calculus of variations, and differential geometry.

**Q: Does this software replace formal mathematical proofs?**  
**A:** No. While the Symbolic Verification engine can algebraically simplify certain identities ($LHS - RHS = 0$), numerical evaluations, phase portraits, and Monte Carlo counterexample searches provide empirical computational evidence rather than formal proof.

**Q: How does the platform protect against malicious code input?**  
**A:** All mathematical string inputs are processed through `safe_parse()` in `calculus/symbolic/expression_parser.py`, which strips Python's `__builtins__` and restricts allowed tokens strictly to mathematical symbols and SymPy functions.

**Q: Can I use the mathematical engines in my own Python scripts without launching Streamlit?**  
**A:** Yes. You can import `CalculusEngine` from `calculus.core.calculus_engine` or invoke specific subsystem functions directly in Python, or run commands from the terminal using `python app.py`.

**Q: Why does the 1D Heat Equation solver refuse to run for certain step sizes?**  
**A:** The explicit Forward-Time Central-Space (FTCS) scheme is conditionally stable. If your chosen thermal diffusivity $\alpha$, time step $\Delta t$, and spatial grid spacing $\Delta x$ violate the Courant–Friedrichs–Lewy (CFL) criterion ($\alpha \frac{\Delta t}{\Delta x^2} \le 0.5$), the solver halts and reports the exact critical $\Delta t$ limit rather than returning exponentially corrupted numerical noise.
