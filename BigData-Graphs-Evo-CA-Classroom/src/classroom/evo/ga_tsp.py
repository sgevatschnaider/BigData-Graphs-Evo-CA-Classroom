"""Un algoritmo genético simple para el problema del viajante (TSP)."""

import numpy as np
from numpy.random import default_rng


def total_distance(route: np.ndarray, dist_matrix: np.ndarray) -> float:
    """Calcula la longitud total de una ruta cerrada según una matriz de distancias."""
    return np.sum(dist_matrix[route, np.roll(route, -1)])


def initialize_population(num_points: int, population_size: int, rng) -> np.ndarray:
    """Crea una población inicial de rutas aleatorias."""
    population = np.zeros((population_size, num_points), dtype=int)
    base_route = np.arange(num_points)
    for i in range(population_size):
        rng.shuffle(base_route)
        population[i] = base_route.copy()
    return population


def crossover(parent1: np.ndarray, parent2: np.ndarray, rng) -> np.ndarray:
    """Cruce de orden (OX) para TSP."""
    n = len(parent1)
    a, b = sorted(rng.choice(n, 2, replace=False))
    child = np.full(n, -1)
    child[a:b] = parent1[a:b]
    fill_positions = [i for i in range(n) if child[i] == -1]
    fill_values = [city for city in parent2 if city not in child]
    for i, pos in enumerate(fill_positions):
        child[pos] = fill_values[i]
    return child


def mutate(route: np.ndarray, mutation_rate: float, rng):
    """Intercambia dos posiciones con cierta probabilidad."""
    if rng.random() < mutation_rate:
        i, j = rng.choice(len(route), 2, replace=False)
        route[i], route[j] = route[j], route[i]


def solve(points: np.ndarray, pop: int = 200, gens: int = 200, pm: float = 0.02, seed: int = 42):
    """Resuelve una instancia pequeña de TSP mediante algoritmo genético.

    Parameters
    ----------
    points : np.ndarray
        Coordenadas de las ciudades de tamaño (n, 2).
    pop : int
        Tamaño de la población.
    gens : int
        Número de generaciones.
    pm : float
        Tasa de mutación.
    seed : int
        Semilla para reproducibilidad.

    Returns
    -------
    tuple[np.ndarray, float]
        La mejor ruta encontrada y su longitud.
    """
    n = len(points)
    rng = default_rng(seed)
    dist_matrix = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=-1)
    population = initialize_population(n, pop, rng)
    best_route = None
    best_length = np.inf
    for _ in range(gens):
        # evaluar fitness
        fitness = np.array([1.0 / total_distance(route, dist_matrix) for route in population])
        # guardar el mejor
        idx_best = np.argmax(fitness)
        current_length = total_distance(population[idx_best], dist_matrix)
        if current_length < best_length:
            best_length = current_length
            best_route = population[idx_best].copy()
        # selección por ruleta
        probs = fitness / fitness.sum()
        new_pop = []
        for _ in range(pop):
            p1, p2 = population[rng.choice(pop, size=2, p=probs)]
            child = crossover(p1, p2, rng)
            mutate(child, pm, rng)
            new_pop.append(child)
        population = np.array(new_pop)
    return best_route, best_length
