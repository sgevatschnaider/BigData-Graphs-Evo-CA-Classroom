import numpy as np
from classroom.ca.elementary import evolve_1d
from classroom.ca.game_of_life import step


def test_elementary_ca():
    initial = np.array([0, 1, 0, 1, 0])
    grid = evolve_1d(initial, rule=30, steps=2)
    assert grid.shape == (3, 5)


def test_game_of_life_step():
    board = np.zeros((5, 5), dtype=int)
    board[2, 1:4] = 1  # una línea horizontal de 3
    next_board = step(board)
    # debería rotar a línea vertical según reglas del juego de la vida
    assert next_board[1:4, 2].sum() == 3
