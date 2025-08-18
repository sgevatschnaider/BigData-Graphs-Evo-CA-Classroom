from __future__ import annotations
import csv
import math
import random
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import numpy as np


# ============================================================
# Utilidades para instancias de TSP (euclídeo y loaders)
# ============================================================

def euclidean_matrix(
    coords: Sequence[Tuple[float, float]],
    metric: str = "euclidean",
) -> np.ndarray:
    """
    Construye una matriz de distancias NxN a partir de coordenadas 2D.

    metric:
      - "euclidean": distancia euclídea (por defecto)
      - "manhattan": distancia L1
    """
    n = len(coords)
    D = np.zeros((n, n), dtype=float)

    if metric == "euclidean":
        dist = lambda a, b: math.dist(a, b)
    elif metric == "manhattan":
        dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    else:
        raise ValueError(f"metric no soportada: {metric}")

    for i in range(n):
        for j in range(i + 1, n):
            d = dist(coords[i], coords[j])
            D[i, j] = D[j, i] = d
    return D


def random_euclidean(
    n: int,
    seed: int = 0,
    low: float = 0.0,
    high: float = 1.0,
) -> np.ndarray:
    """
    Genera una instancia aleatoria euclídea con n ciudades en [low, high]^2.
    Devuelve la matriz de distancias NxN.
    """
    random.seed(seed)
    coords = [(random.uniform(low, high), random.uniform(low, high)) for _ in range(n)]
    return euclidean_matrix(coords, metric="euclidean")


def tour_length(tour_
