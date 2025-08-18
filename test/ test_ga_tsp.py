import importlib, pytest

m = importlib.import_module("evo.ga_tsp")
if not hasattr(m, "ga_tsp"):
    pytest.skip("ga_tsp() no está implementada en evo.ga_tsp", allow_module_level=True)

from evo.problems.tsp import random_euclidean

def test_ga_tsp_runs():
    D = random_euclidean(20, seed=1)
    tour, length = m.ga_tsp(D, gens=60, pop_size=80, seed=1)
    assert len(tour) == D.shape[0]
    assert len(set(tour)) == D.shape[0]
    assert length > 0.0
