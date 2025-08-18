from __future__ import annotations
import math, random
from typing import List, Tuple
import numpy as np

def euclidean_matrix(coords: List[Tuple[float, float]]) -> np.ndarray:
    n = len(coords)
    D = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            d = math.dist(coords[i], coords[j])
            D[i, j] = D[j, i] = d
    return D

def random_euclidean(n: int, seed: int = 0) -> np.ndarray:
    random.seed(seed)
    coords = [(random.random(), random.random()) for _ in range(n)]
    return euclidean_matrix(coords)

def tour_length(tour: List[int], D: np.ndarray) -> float:
    return sum(D[tour[i], tour[(i + 1) % len(tour)]] for i in range(len(tour)))
