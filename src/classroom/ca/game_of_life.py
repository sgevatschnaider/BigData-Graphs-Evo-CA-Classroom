from __future__ import annotations
import numpy as np
from scipy.signal import convolve2d

KERNEL = np.array([[1,1,1],[1,0,1],[1,1,1]], dtype=np.uint8)

def step(board: np.ndarray) -> np.ndarray:
    board = (board > 0).astype(np.uint8)
    n = convolve2d(board, KERNEL, mode="same", boundary="wrap")
    born = (board == 0) & (n == 3)
    survive = (board == 1) & ((n == 2) | (n == 3))
    return (born | survive).astype(np.uint8)
