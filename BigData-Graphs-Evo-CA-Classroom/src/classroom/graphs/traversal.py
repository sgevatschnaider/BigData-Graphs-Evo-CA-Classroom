"""Recorridos en grafos: BFS y DFS."""

import collections
import networkx as nx


def bfs_order(G: nx.Graph, source) -> list:
    """Devuelve el orden de visita de un BFS desde el nodo `source`."""
    seen = {source}
    order = [source]
    queue = collections.deque([source])
    while queue:
        u = queue.popleft()
        for v in G.neighbors(u):
            if v not in seen:
                seen.add(v)
                order.append(v)
                queue.append(v)
    return order


def dfs_order(G: nx.Graph, source) -> list:
    """Devuelve el orden de visita de un DFS (profundidad) desde `source`."""
    seen = set()
    order = []
    stack = [source]
    while stack:
        u = stack.pop()
        if u not in seen:
            seen.add(u)
            order.append(u)
            # agregar vecinos en orden inverso para simular recursion
            stack.extend(reversed(list(G.neighbors(u))))
    return order
