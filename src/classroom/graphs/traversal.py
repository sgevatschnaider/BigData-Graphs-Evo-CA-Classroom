from __future__ import annotations
import collections
import networkx as nx
from typing import List, Hashable

def bfs_order(G: nx.Graph, source: Hashable) -> List[Hashable]:
    seen = {source}
    order = [source]
    q = collections.deque([source])
    while q:
        u = q.popleft()
        for v in G.neighbors(u):
            if v not in seen:
                seen.add(v)
                order.append(v)
                q.append(v)
    return order

def dfs_order(G: nx.Graph, source: Hashable) -> List[Hashable]:
    seen = set()
    order: List[Hashable] = []
    def _dfs(u):
        seen.add(u)
        order.append(u)
        for v in G.neighbors(u):
            if v not in seen:
                _dfs(v)
    _dfs(source)
    return order
