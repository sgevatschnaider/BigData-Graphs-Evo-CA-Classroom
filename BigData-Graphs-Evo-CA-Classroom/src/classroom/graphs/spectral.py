"""Funciones espectrales para grafos."""

import numpy as np
import networkx as nx


def laplacian_matrix(G: nx.Graph) -> np.ndarray:
    """Devuelve la matriz laplaciana de un grafo como array NumPy."""
    return nx.laplacian_matrix(G).astype(float).toarray()


def second_smallest_eigenvalue(L: np.ndarray) -> float:
    """Calcula el segundo valor propio (lambda_2) de una matriz laplaciana."""
    eigenvalues = np.linalg.eigvalsh(L)
    return np.sort(eigenvalues)[1]
