# Big Data - Graphs - Evolutionary - Cellular Automata - Classroom

[![src/classroom/bigdata](https://img.shields.io/badge/src-bigdata-0366d6)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/tree/main/src/classroom/bigdata)
[![src/classroom/graphs](https://img.shields.io/badge/src-graphs-0366d6)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/tree/main/src/classroom/graphs)
[![src/classroom/evo](https://img.shields.io/badge/src-evo-0366d6)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/tree/main/src/classroom/evo)
[![src/classroom/ca](https://img.shields.io/badge/src-ca-0366d6)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/tree/main/src/classroom/ca)


<p align="center">
  <a href="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/" target="_blank" rel="noopener">
    <img alt="Live docs — GitHub Pages"
         src="https://img.shields.io/badge/Live%20docs-GitHub%20Pages-2b3137?style=for-the-badge&logo=github" />
  </a>
  &nbsp;
  <a href="https://clinquant-meringue-3930c2.netlify.app/" target="_blank" rel="noopener">
    <img alt="Live demos — Netlify"
         src="https://img.shields.io/badge/Live%20demos-Netlify-00c7b7?style=for-the-badge&logo=netlify" />
  </a>
</p>

Material docente reproducible para Big Data, Teoría de Grafos, Algoritmos Evolutivos y Autómatas Celulares. Incluye notebooks, módulos en src/, tests (nbmake/pytest) y docs (MkDocs Material con syllabus y cronograma).


Material docente reproducible para Big Data, Teoria de Grafos, Algoritmos Evolutivos y Automatas Celulares.

Incluye: notebooks, modulos en `src/`, tests (nbmake) y docs (MkDocs Material con syllabus y cronograma).


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
# Notebooks Interactivos  
Puedes abrir y ejecutar los notebooks en Google Colab directamente desde aquí:  

---


## 📝 Fundamentos de la Teoría de Grafos

| 📄 Recurso | 📥 Acceso |
|---|---|
| **Introducción a la Teoría de Grafos (Taller Interactivo)** <br><br> <details><summary><strong>Resumen:</strong> <em>(haz clic para expandir/colapsar)</em></summary><p>Este cuaderno interactivo introduce los conceptos esenciales de la teoría de grafos, transformando una lección teórica en una aplicación web visual y dinámica. Explora las definiciones de vértices y aristas, y detalla los distintos tipos de grafos (dirigidos, no dirigidos, ponderados, bipartitos, etc.) a través de visualizaciones claras. La lección destaca por su construcción técnica: utiliza Python con <code>networkx</code> y <code>matplotlib</code> para generar los grafos, los convierte a formato Base64 y los incrusta en una página HTML con CSS y JavaScript para ofrecer una interfaz interactiva con temas claro/oscuro y secciones colapsables. El objetivo es proporcionar una comprensión intuitiva y práctica de cómo se modelan y analizan las redes y relaciones.</p></details> | [![Ver en GitHub](https://img.shields.io/badge/Ver%20en-GitHub-blue?style=for-the-badge&logo=github)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/fdacac884643cdc9f8d15c59e720ed19f50afca7/src/classroom/graphs/notebooks/Introducci%C3%B3n_a_la_teor%C3%ADa_y_aplicaciones_de_los_grafos_.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/fdacac884643cdc9f8d15c59e720ed19f50afca7/src/classroom/graphs/notebooks/Introducci%C3%B3n_a_la_teor%C3%ADa_y_aplicaciones_de_los_grafos_.ipynb) |

## 📝Modelo Erdős–Rényi

| 📄 Recurso | 📥 Acceso |
|---|---|
| **Modelo Erdős–Rényi (G(n,p))** <br><br> <details><summary><strong>Resumen:</strong> <em>(haz clic para expandir/colapsar)</em></summary><p>Grafo aleatorio donde cada arista aparece de forma independiente con probabilidad <code>p</code>. Permite explorar umbrales de componente gigante (<code>p≈1/n</code>) y conectividad (<code>p≈\ln(n)/n</code>), ver estadísticas (nodos, aristas, componentes, tamaño de la mayor componente, <code>E[m]=p·C(n,2)</code>) y animación por fuerzas.</p></details> | [![Abrir Página](https://img.shields.io/badge/Abrir%20P%C3%A1gina-Interactiva-brightgreen?style=for-the-badge&logo=html5)](https://sgevatschnaider.github.io/GraphAI-Data-Science-ML/recursos/Modelo%20Erd%C5%91s%E2%80%93R%C3%A9nyi.html) [![Código en GitHub](https://img.shields.io/badge/C%C3%B3digo-GitHub-black?style=for-the-badge&logo=github)](https://github.com/sgevatschnaider/GraphAI-Data-Science-ML/blob/7cedd0c280c2598110b385150b606ffa16474cb7/recursos/Modelo%20Erd%C5%91s%E2%80%93R%C3%A9nyi.html) |






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



