"""Implementación vectorizada del Juego de la Vida de Conway."""

import numpy as np
from scipy.signal import convolve2d

# Kernel para contar vecinos
_KERNEL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])


def step(board: np.ndarray) -> np.ndarray:
    """Calcula el siguiente estado del juego de la vida en modalidad toroidal."""
    neighbors = convolve2d(board, _KERNEL, mode="same", boundary="wrap")
    birth = (board == 0) & (neighbors == 3)
    survive = (board == 1) & ((neighbors == 2) | (neighbors == 3))
    return birth | survive
