"""Funciones de selección para algoritmos evolutivos."""

import numpy as np


def roulette_wheel_selection(population: list, fitness: np.ndarray, rng) -> tuple:
    """Selecciona dos individuos usando ruleta proporcional al fitness."""
    probs = fitness / fitness.sum()
    idx = rng.choice(len(population), size=2, p=probs)
    return population[idx[0]], population[idx[1]]


def tournament_selection(population: list, fitness: np.ndarray, k: int, rng) -> tuple:
    """Selecciona dos individuos por torneo de tamaño k."""
    def select_one():
        contenders = rng.choice(len(population), size=k, replace=False)
        best = contenders[np.argmax(fitness[contenders])]
        return population[best]
    return select_one(), select_one()
