# Big Data - Graphs - Evolutionary - Cellular Automata - Classroom

[![src/classroom/bigdata](https://img.shields.io/badge/src-bigdata-0366d6)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/tree/main/src/classroom/bigdata)
[![src/classroom/graphs](https://img.shields.io/badge/src-graphs-0366d6)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/tree/main/src/classroom/graphs)
[![src/classroom/evo](https://img.shields.io/badge/src-evo-0366d6)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/tree/main/src/classroom/evo)
[![src/classroom/ca](https://img.shields.io/badge/src-ca-0366d6)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/tree/main/src/classroom/ca)


**Live docs:** https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/


Material docente reproducible para Big Data, Teoria de Grafos, Algoritmos Evolutivos y Automatas Celulares.

Incluye: notebooks, modulos en `src/`, tests (nbmake) y docs (MkDocs Material con syllabus y cronograma).

<div align="center">
  <a href="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/">
    <img src="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/banner.svg" alt="Project Banner: Big Data, Graphs, Evolutionary Algorithms, Cellular Automata">
  </a>
</div>

<p align="center">
   <a href="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/"><img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fsgevatschnaider.github.io%2FBigData-Graphs-Evo-CA-Classroom%2F"></a>
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/python-3.10%20%7C%203.11-blue"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="https://pre-commit.com/"><img alt="pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
</p>

---

Este repositorio contiene una colección de **materiales didácticos** para un curso introductorio a **Big Data, Grafos, Algoritmos Evolutivos y Autómatas Celulares**.  

El objetivo es ofrecer **notebooks reproducibles**, datasets ligeros y módulos de código reutilizables para facilitar la enseñanza y el aprendizaje.  
Este repositorio se complementa con [GraphAI-Data-Science-ML](https://github.com/sgevatschnaider/GraphAI-Data-Science-ML), que contiene demos exploratorias y material de investigación.

<div align="center">
  <a href="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/">
    <img
      src="https://raw.githubusercontent.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/88fa2f36409fbef3bda9de2b7241cf2c2bbf1443/docs/assets/hipercubo.gif"
      alt="Hipercubo 4D Animado"
      width="800"
    />
  </a>
</div>

---

## 📑 Tabla de Contenidos
* [✨ ¿Por qué este curso?](#-por-qué-este-curso)
* [🎯 Público Objetivo y Requisitos](#-público-objetivo-y-requisitos)
* [🛠️ Uso y Ejecución](#️-uso-y-ejecución)
* [📚 Módulos y Notebooks](#-módulos-y-notebooks)
* [🗺️ Roadmap del Proyecto](#️-roadmap-del-proyecto)
* [📂 Estructura del Repositorio](#-estructura-del-repositorio)
* [🤝 Cómo Contribuir](#-cómo-contribuir)
* [⚖️ Licencia](#️-licencia)
* [📖 Citar este trabajo](#-citar-este-trabajo)

---

## ✨ ¿Por qué este curso?
- **Enfoque Práctico**: Aprendizaje basado en la ejecución y modificación de código real.  
- **Reproducibilidad**: Notebooks listos para ejecutar localmente o en la nube (Google Colab).  
- **Modularidad**: Código fuente organizado en módulos para facilitar su reutilización.  
- **Open Source**: Abierto a contribuciones y mejoras de la comunidad.  

---

## 🎯 Público Objetivo y Requisitos

Este material está diseñado para:
- Estudiantes de Ciencias de la Computación, Ingeniería o afines.  
- Autodidactas interesados en algoritmia e inteligencia artificial.  
- Profesores que busquen material interactivo para sus clases.  

**Requisitos Previos:**
- Conocimientos sólidos de **Python** (funciones, clases, estructuras de datos).  
- Familiaridad con **álgebra lineal** y **estadística básica**.  
- Experiencia mínima con terminal y `git`.  

---

## 🛠️ Uso y Ejecución

### 1. Entorno Local
```bash
git clone https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom.git
cd BigData-Graphs-Evo-CA-Classroom

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -e .
pip install -r requirements.txt

pytest
````

### 2. Google Colab

Ejecuta los notebooks en la nube con un clic (badges en la sección siguiente).

### 3. GitHub Codespaces

Entorno “cero instalación” en tu navegador, si tu cuenta lo permite.

---

## 📚 Módulos y Notebooks

| Módulo                        | Descripción                                     | Notebook                           | Colab                                                                                                                                                                                                               |
| ----------------------------- | ----------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **01. Big Data**              | Paradigma Big Data y técnicas de muestreo.      | `01_BigData_Intro.ipynb`           | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/01_BigData_Intro.ipynb)           |
| **02. Grafos**                | Fundamentos, BFS/DFS y propiedades espectrales. | `02_Graphs_Fundamentals.ipynb`     | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/02_Graphs_Fundamentals.ipynb)     |
| **03. Algoritmos Evolutivos** | Algoritmo Genético aplicado al TSP.             | `03_Evolutionary_Algorithms.ipynb` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/03_Evolutionary_Algorithms.ipynb) |
| **04. Autómatas Celulares**   | Reglas 1D y Juego de la Vida.                   | `04_Cellular_Automata.ipynb`       | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/04_Cellular_Automata.ipynb)       |

---

## 🗺️ Roadmap del Proyecto

* [ ] **Módulo 5: Redes Complejas** (centralidad, modelos de mundo pequeño).
* [ ] **Ejercicios Propuestos** en cada notebook.
* [ ] **Versión en Inglés** para mayor alcance.
* [ ] **Documentación avanzada con MkDocs** y galería de ejemplos.

---

## 📂 Estructura del Repositorio

<details>
<summary>Haz clic para ver</summary>

```
BigData-Graphs-Evo-CA-Classroom/
├── README.md
├── LICENSE
├── CITATION.cff
├── pyproject.toml
├── requirements.txt
├── .github/
├── docs/
├── src/classroom/
├── notebooks/
├── datasets/
└── tests/
```

</details>

---

## 🤝 Cómo Contribuir

1. Reporta errores o abre un [issue](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/issues).
2. Haz un fork, crea una rama (`feat/nueva-funcionalidad`), implementa, prueba (`pytest`) y abre un PR.

---

## ⚖️ Licencia

Este proyecto está bajo [Licencia MIT](LICENSE).

---

## 📖 Citar este trabajo

```bibtex
@software{Gevatschnaider_2025_BigDataClassroom,
  author       = {S. Gevatschnaider and Community Contributors},
  title        = {Big Data · Graphs · Evolutionary · Cellular Automata — Classroom: Interactive Educational Materials},
  month        = aug,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {0.1.0},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom}
}
```

*(El DOI real se genera al subir a Zenodo).*



