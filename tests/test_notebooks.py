import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path


def test_execute_notebooks():
    notebooks = Path('notebooks').glob('*.ipynb')
    for nb_file in notebooks:
        with open(nb_file, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=300, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': '.'}})
