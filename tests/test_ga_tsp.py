from classroom.evo.ga_tsp import ga_tsp
from classroom.evo.problems.tsp import random_euclidean

def test_ga_tsp_runs():
    D = random_euclidean(20, seed=1)
    tour, length = ga_tsp(D, gens=60, pop_size=80, seed=1)
    assert len(tour) == D.shape[0]
    assert len(set(tour)) == D.shape[0]
    assert length > 0.0
