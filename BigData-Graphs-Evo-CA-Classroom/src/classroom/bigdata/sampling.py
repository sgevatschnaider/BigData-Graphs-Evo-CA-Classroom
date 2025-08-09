"""Funciones básicas de muestreo para big data."""

import numpy as np
import pandas as pd

def reservoir_sampling(iterable, k, seed: int | None = None):
    """Selecciona una muestra aleatoria de tamaño k de un iterable usando reservoir sampling.

    Parameters
    ----------
    iterable : Iterable
        Fuente de datos (no necesariamente indexable).
    k : int
        Tamaño de la muestra.
    seed : int | None
        Semilla para reproducibilidad.

    Returns
    -------
    list
        Muestra aleatoria de k elementos.
    """
    rng = np.random.default_rng(seed)
    sample = []
    for i, item in enumerate(iterable):
        if i < k:
            sample.append(item)
        else:
            j = rng.integers(0, i + 1)
            if j < k:
                sample[j] = item
    return sample


def random_row_sample(df: pd.DataFrame, k: int, seed: int | None = None) -> pd.DataFrame:
    """Devuelve una muestra aleatoria de k filas de un DataFrame."""
    return df.sample(n=k, random_state=seed).reset_index(drop=True)
