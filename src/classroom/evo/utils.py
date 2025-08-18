from __future__ import annotations
import random, numpy as np

def seed_all(s: int):
    random.seed(s)
    np.random.seed(s)
