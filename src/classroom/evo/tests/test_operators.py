import random
from evo.operators import ox, swap_mutation

def test_ox_is_permutation():
    p1 = list(range(20)); p2 = p1[::-1]
    c1, c2 = ox(p1, p2)
    assert sorted(c1) == list(range(20))
    assert sorted(c2) == list(range(20))

def test_swap_mutation_changes_or_not():
    random.seed(0)
    p = list(range(10))
    swap_mutation(p, 1.0)
    assert p != list(range(10))
