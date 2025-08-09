import random
from classroom.evo.ga_tsp import solve

def test_ga_tsp_runs():
    rng = random.Random(0)
    points = [(rng.random(), rng.random()) for _ in range(20)]
    route, length = solve(points, pop=80, gens=60, pm=0.03, elite=2, seed=0)
    assert len(route) == len(points)
    assert length > 0
    assert sorted(route) == list(range(len(points)))
