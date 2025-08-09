from __future__ import annotations
import random
import math
from typing import List, Tuple

Point = Tuple[float, float]
Route = List[int]

def _dist(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def route_length(points: List[Point], route: Route) -> float:
    n = len(route)
    return sum(_dist(points[route[i]], points[route[(i + 1) % n]]) for i in range(n))

def _ordered_crossover(p1: Route, p2: Route, rng: random.Random) -> Route:
    n = len(p1)
    a, b = sorted(rng.sample(range(n), 2))
    child = [-1] * n
    child[a:b] = p1[a:b]
    fill = [x for x in p2 if x not in child]
    j = 0
    for i in range(n):
        if child[i] == -1:
            child[i] = fill[j]
            j += 1
    return child

def _mutate_swap(route: Route, pm: float, rng: random.Random) -> None:
    n = len(route)
    for i in range(n):
        if rng.random() < pm:
            j = rng.randrange(n)
            route[i], route[j] = route[j], route[i]

def solve(points: List[Point], pop: int = 200, gens: int = 400, pm: float = 0.02,
          elite: int = 2, seed: int | None = 42) -> Tuple[Route, float]:
    rng = random.Random(seed)
    n = len(points)
    base = list(range(n))
    population = [rng.sample(base, n) for _ in range(pop)]

    def fitness(route: Route) -> float:
        return 1.0 / (1e-9 + route_length(points, route))

    def tournament(k: int = 3) -> Route:
        cand = rng.sample(population, k)
        cand.sort(key=lambda r: fitness(r), reverse=True)
        return cand[0]

    for _ in range(gens):
        population.sort(key=lambda r: fitness(r), reverse=True)
        new_pop = population[:elite]
        while len(new_pop) < pop:
            p1, p2 = tournament(), tournament()
            child = _ordered_crossover(p1, p2, rng)
            _mutate_swap(child, pm, rng)
            new_pop.append(child)
        population = new_pop

    best = max(population, key=lambda r: fitness(r))
    return best, route_length(points, best)
