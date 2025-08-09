import networkx as nx
from classroom.graphs.traversal import bfs_order, dfs_order
from classroom.graphs.spectral import fiedler

def test_bfs_small_graph():
    G = nx.path_graph(5)
    assert bfs_order(G, 0) == [0, 1, 2, 3, 4]

def test_dfs_small_graph():
    G = nx.path_graph(5)
    order = dfs_order(G, 0)
    assert set(order) == set(range(5))

def test_fiedler_positive():
    G = nx.karate_club_graph()
    lam2, _ = fiedler(G)
    assert lam2 > 0
