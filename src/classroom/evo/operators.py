from __future__ import annotations
import random
from typing import List, Tuple

# ---------- Operadores para permutaciones (TSP) ----------

def ox(p1: List[int], p2: List[int]) -> Tuple[List[int], List[int]]:
    """Order Crossover (OX) clásico."""
    n = len(p1)
    a, b = sorted(random.sample(range(n), 2))
    def build(child_from, other):
        child = [None] * n
        child[a:b+1] = child_from[a:b+1]
        pos = (b + 1) % n
        for g in other[b+1:] + other[:b+1]:
            if g not in child:
                child[pos] = g
                pos = (pos + 1) % n
        return child
    return build(p1, p2), build(p2, p1)

def swap_mutation(p: List[int], p_mut: float) -> None:
    """Intercambia dos genes con prob p_mut (in-place)."""
    if random.random() < p_mut:
        i, j = random.sample(range(len(p)), 2)
        p[i], p[j] = p[j], p[i]

def inv_mutation(p: List[int], p_mut: float) -> None:
    """Inversión de un segmento con prob p_mut (in-place)."""
    if random.random() < p_mut:
        i, j = sorted(random.sample(range(len(p)), 2))
        p[i:j+1] = reversed(p[i:j+1])
