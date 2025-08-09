import numpy as np
from classroom.ca.game_of_life import step as life_step
from classroom.ca.elementary import step_1d

def test_game_of_life_blinker():
    B = np.zeros((5, 5), dtype=np.uint8)
    B[2, 1:4] = 1
    B1 = life_step(B)
    B2 = life_step(B1)
    assert np.array_equal(B2, B)

def test_elementary_rule_90():
    s = np.array([0, 0, 1, 0, 0], dtype=np.uint8)
    s1 = step_1d(s, 90)
    assert s1.sum() >= 1
