"""Execution tests for project notebooks.

Each notebook is executed in isolation using ``pytest.mark.parametrize``
so that failures are reported per file.  Heavy notebooks are skipped unless
the environment variable ``RUN_ALL_NOTEBOOKS=1`` is provided.
"""

from __future__ import annotations

import os
from pathlib import Path

import nbformat
import pytest
from nbconvert.preprocessors import ExecutePreprocessor

# Path to all notebooks in the repository
NOTEBOOK_DIR = Path("notebooks")

# Notebooks that require considerable resources/time
HEAVY_NOTEBOOKS = {
    "03_Evolutionary_Algorithms.ipynb",
    "04_Cellular_Automata.ipynb",
}

ALL_NOTEBOOKS = list(NOTEBOOK_DIR.glob("*.ipynb"))


@pytest.mark.parametrize("nb_file", ALL_NOTEBOOKS, ids=lambda p: p.stem)
def test_execute_notebook(nb_file: Path) -> None:
    """Execute a single notebook and ensure it runs without errors."""

    run_all = os.environ.get("RUN_ALL_NOTEBOOKS") == "1"
    if not run_all and nb_file.name in HEAVY_NOTEBOOKS:
        pytest.skip("Skipping heavy notebook. Set RUN_ALL_NOTEBOOKS=1 to run.")

    with open(nb_file, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=300, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": "."}})

