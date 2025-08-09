from __future__ import annotations
import numpy as np

def rule_table(rule: int) -> np.ndarray:
    assert 0 <= rule <= 255
    bits = np.array([(rule >> i) & 1 for i in range(8)], dtype=np.uint8)
    return bits

def step_1d(state: np.ndarray, rule: int) -> np.ndarray:
    state = state.astype(np.uint8)
    left = np.roll(state, 1)
    right = np.roll(state, -1)
    pattern = (left << 2) | (state << 1) | right
    tbl = rule_table(rule)
    return tbl[pattern]
