"""Autómatas celulares elementales (1D) de Wolfram."""

import numpy as np


def rule_to_binary(rule: int) -> np.ndarray:
    """Convierte un número de regla (0-255) a un arreglo de 8 bits."""
    return np.array([int(x) for x in np.binary_repr(rule, width=8)], dtype=int)


def evolve_1d(initial: np.ndarray, rule: int, steps: int) -> np.ndarray:
    """Evoluciona un autómata 1D durante `steps` pasos con la regla dada."""
    binary_rule = rule_to_binary(rule)
    n = len(initial)
    grid = np.zeros((steps + 1, n), dtype=int)
    grid[0] = initial
    for t in range(steps):
        prev = grid[t]
        new = np.zeros(n, dtype=int)
        for i in range(n):
            neighborhood = prev[(i - 1) % n], prev[i], prev[(i + 1) % n]
            idx = (neighborhood[0] << 2) | (neighborhood[1] << 1) | neighborhood[2]
            new[i] = binary_rule[7 - idx]
        grid[t + 1] = new
    return grid
