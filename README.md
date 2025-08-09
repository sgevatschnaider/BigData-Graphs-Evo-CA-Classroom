# Big Data · Graphs · Evolutionary · Cellular Automata — Classroom

[![Tests](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/tests.yml/badge.svg)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/tests.yml)
[![Docs](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/pages.yml/badge.svg)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Material docente reproducible para Big Data, Teoría de Grafos, Algoritmos Evolutivos y Autómatas Celulares. Incluye:

- Notebooks con botón **Open in Colab**
- Módulos reutilizables en `src/classroom/`
- **Tests** (incluye ejecución de notebooks con nbmake)
- **Docs** con MkDocs Material (syllabus y cronograma)

##  Inicio rápido

```bash
pip install -r requirements.txt
pip install -e .
pytest -q
pytest --nbmake notebooks/01_BigData_Intro.ipynb
pytest --nbmake notebooks/02_Graphs_Fundamentals.ipynb
```

## 📓 Notebooks (abrir en Colab)
- 01 Big Data Intro – [Open in Colab](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/01_BigData_Intro.ipynb)
- 02 Graphs Fundamentals – [Open in Colab](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/02_Graphs_Fundamentals.ipynb)

## 📚 Documentación
Sitio: https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/

## 🔧 Estructura
- `src/classroom/`: funciones listas para usar en clase (BFS/DFS, λ₂, GA-TSP, CA 1D y Game of Life)
- `notebooks/`: cuadernos autocontenidos con datasets livianos
- `tests/`: pruebas unitarias + notebooks con nbmake
- `docs/`: sitio del curso (MkDocs Material)

## 📄 Licencia
MIT — ver `LICENSE`.
