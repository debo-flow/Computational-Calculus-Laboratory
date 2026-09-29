import numpy as np
from scipy import linalg
from typing import Dict, Any

def analyze_svd(matrix_data: list) -> Dict[str, Any]:
    """Computes Singular Value Decomposition A = U \Sigma V^T."""
    A = np.array(matrix_data, dtype=float)
    U, s, Vh = linalg.svd(A)
    
    # Reconstruction to verify
    Sigma = np.zeros_like(A, dtype=float)
    np.fill_diagonal(Sigma, s)
    A_reconstructed = U @ Sigma @ Vh
    reconstruction_error = np.linalg.norm(A - A_reconstructed)
    
    return {
        "U (Orthogonal)": U.tolist(),
        "Singular Values (Sigma)": s.tolist(),
        "V^T (Orthogonal)": Vh.tolist(),
        "Rank Estimate": int(np.sum(s > 1e-10)),
        "Condition Number": float(s[0] / s[-1]) if s[-1] > 1e-10 else float('inf'),
        "Reconstruction Error": float(reconstruction_error)
    }

def analyze_eigen(matrix_data: list) -> Dict[str, Any]:
    """Computes eigenvalues and eigenvectors, calculating the residual ||Av - \lambda v||."""
    A = np.array(matrix_data, dtype=complex)
    eigenvalues, eigenvectors = linalg.eig(A)
    
    residuals = []
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i]
        lam = eigenvalues[i]
        residual = np.linalg.norm(A @ v - lam * v)
        residuals.append(float(residual))
        
    return {
        "Eigenvalues": np.round(eigenvalues, 5).tolist(),
        "Eigenvectors": np.round(eigenvectors, 5).tolist(),
        "Max Residual": max(residuals)
    }
