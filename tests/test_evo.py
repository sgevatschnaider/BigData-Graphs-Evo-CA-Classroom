import numpy as np
from classroom.evo.ga_tsp import solve


def test_ga_tsp_runs():
    # Genera puntos y corre 20 generaciones para abreviar
    rng = np.random.default_rng(0)
    points = rng.random((10, 2))
    route, length = solve(points, pop=30, gens=20, pm=0.1, seed=0)
    assert len(route) == 10
    assert length > 0
