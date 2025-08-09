import networkx as nx
from classroom.graphs.traversal import bfs_order, dfs_order


def test_bfs_small_graph():
    G = nx.path_graph(5)
    assert bfs_order(G, 0) == [0, 1, 2, 3, 4]


def test_dfs_small_graph():
    G = nx.path_graph(5)
    assert dfs_order(G, 0) == [0, 1, 2, 3, 4]
