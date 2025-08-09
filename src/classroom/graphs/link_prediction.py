from __future__ import annotations
import networkx as nx
from math import log
from typing import Iterable, Tuple

Edge = Tuple[int, int]

def candidate_non_edges(G: nx.Graph) -> Iterable[Edge]:
    return nx.non_edges(G)

def common_neighbors_score(G: nx.Graph, u: int, v: int) -> int:
    return len(list(nx.common_neighbors(G, u, v)))

def adamic_adar_score(G: nx.Graph, u: int, v: int) -> float:
    score = 0.0
    for w in nx.common_neighbors(G, u, v):
        deg = G.degree[w]
        if deg > 1:
            score += 1.0 / log(deg)
    return score
