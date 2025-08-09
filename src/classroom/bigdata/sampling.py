from __future__ import annotations
import random
from typing import Iterable, List, TypeVar

T = TypeVar("T")

def reservoir_sample(stream: Iterable[T], k: int, seed: int | None = 42) -> List[T]:
    """Reservoir sampling (Vitter)."""
    if k <= 0:
        return []
    rng = random.Random(seed)
    it = iter(stream)
    reservoir = []
    for i, x in enumerate(it):
        if i < k:
            reservoir.append(x)
        else:
            j = rng.randint(0, i)
            if j < k:
                reservoir[j] = x
    return reservoir
