from __future__ import annotations
import numpy as np
import networkx as nx
from typing import Tuple

def laplacian_matrix(G: nx.Graph) -> np.ndarray:
    return nx.laplacian_matrix(G).astype(float).toarray()

def fiedler(G: nx.Graph) -> Tuple[float, np.ndarray]:
    L = laplacian_matrix(G)
    vals, vecs = np.linalg.eigh(L)
    idx = np.argsort(vals)
    vals, vecs = vals[idx], vecs[:, idx]
    if len(vals) < 2:
        return 0.0, np.zeros((L.shape[0],))
    return float(vals[1]), vecs[:, 1]
