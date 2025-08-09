"""Implementaciones sencillas de heurísticas para predicción de enlaces."""

import networkx as nx
import numpy as np


def common_neighbors_score(G: nx.Graph, u, v) -> int:
    """Cuenta los vecinos en común entre u y v."""
    return len(list(nx.common_neighbors(G, u, v)))


def adamic_adar_score(G: nx.Graph, u, v) -> float:
    """Calcula el índice de Adamic/Adar para u y v."""
    score = 0.0
    for w in nx.common_neighbors(G, u, v):
        deg = G.degree(w)
        if deg > 1:
            score += 1.0 / np.log(deg)
    return score


def jaccard_coefficient(G: nx.Graph, u, v) -> float:
    """Calcula el coeficiente de Jaccard para u y v."""
    union_size = len(set(G.neighbors(u)).union(G.neighbors(v)))
    if union_size == 0:
        return 0.0
    return common_neighbors_score(G, u, v) / union_size
