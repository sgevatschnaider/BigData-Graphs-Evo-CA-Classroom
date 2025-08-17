﻿<div align="center">
  <a href="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/">
    <img src="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/banner.svg" alt="Project Banner: Big Data, Graphs, Evolutionary Algorithms, Cellular Automata">
  </a>
</div>

<p align="center">
  <a href="https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/tests.yml"><img alt="CI" src="https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/tests.yml/badge.svg?branch=main"></a>
  <a href="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/"><img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fsgevatschnaider.github.io%2FBigData-Graphs-Evo-CA-Classroom%2F"></a>
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/python-3.10 | 3.11-blue"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="https://pre-commit.com/"><img alt="pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
</p>

---

Este repositorio contiene una colecciÃ³n de materiales didÃ¡cticos para un curso introductorio a **Big Data, Grafos, Algoritmos Evolutivos y AutÃ³matas Celulares**.

El objetivo es ofrecer notebooks reproducibles, datasets ligeros y mÃ³dulos de cÃ³digo reutilizables para facilitar la enseÃ±anza y el aprendizaje. Este repositorio se complementa con [GraphAIâ€‘Dataâ€‘Scienceâ€‘ML](https://github.com/sgevatschnaider/GraphAI-Data-Science-ML), que contiene demos exploratorias y material de investigaciÃ³n.


<div align="center">
  <a href="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/">
    <img
      src="https://raw.githubusercontent.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/88fa2f36409fbef3bda9de2b7241cf2c2bbf1443/docs/assets/hipercubo.gif"
      alt="Hipercubo 4D Animado"
      width="800"
    />
  </a>
</div>


## ðŸ“‹ Tabla de Contenidos
*   [âœ¨ Â¿Por quÃ© este curso?](#-por-quÃ©-este-curso)
*   [ðŸŽ¯ PÃºblico Objetivo y Requisitos](#-pÃºblico-objetivo-y-requisitos)
*   [ðŸ› ï¸ Uso y EjecuciÃ³n](#ï¸-uso-y-ejecuciÃ³n)
*   [ðŸ“š MÃ³dulos y Notebooks](#-mÃ³dulos-y-notebooks)
*   [ðŸ—ºï¸ Roadmap del Proyecto](#ï¸-roadmap-del-proyecto)
*   [ðŸ“‚ Estructura del Repositorio](#-estructura-del-repositorio)
*   [ðŸ¤ CÃ³mo Contribuir](#-cÃ³mo-contribuir)
*   [âš–ï¸ Licencia](#ï¸-licencia)
*   [ðŸŽ“ Citar este trabajo](#-citar-este-trabajo)


## âœ¨ Â¿Por quÃ© este curso?
*   **Enfoque PrÃ¡ctico**: Aprendizaje basado en la ejecuciÃ³n y modificaciÃ³n de cÃ³digo real.
*   **Reproducibilidad**: Notebooks listos para ejecutar localmente o en la nube (Google Colab).
*   **Modularidad**: CÃ³digo fuente organizado en mÃ³dulos para facilitar su reutilizaciÃ³n y estudio.
*   **Open Source**: Totalmente abierto a contribuciones y mejoras de la comunidad.

## ðŸŽ¯ PÃºblico Objetivo y Requisitos

Este material estÃ¡ diseÃ±ado para:
*   Estudiantes de grado en Ciencias de la ComputaciÃ³n, IngenierÃ­a o carreras afines.
*   Autodidactas con interÃ©s en temas avanzados de algoritmia e inteligencia artificial.
*   Profesores que busquen material de apoyo interactivo para sus clases.

**Requisitos Previos:**
*   Conocimientos sÃ³lidos de **Python** (funciones, clases, estructuras de datos).
*   Familiaridad con conceptos de **Ã¡lgebra lineal** y **estadÃ­stica** elemental.
*   Experiencia bÃ¡sica usando la terminal y `git`.


## ðŸ› ï¸ Uso y EjecuciÃ³n

Tienes varias formas de ejecutar los notebooks y probar el cÃ³digo:

### 1. Entorno Local (Recomendado para desarrolladores)

Clona este repositorio, crea un entorno virtual e instala las dependencias.

```bash
git clone https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom.git
cd BigData-Graphs-Evo-CA-Classroom

# Crea y activa un entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instala el paquete en modo editable y las dependencias
pip install -e .
pip install -r requirements.txt

# Corre las pruebas para verificar que todo funcione correctamente
pytest
```

### 2. Google Colab (Recomendado para estudiantes)
No requiere instalaciÃ³n local. Solo necesitas una cuenta de Google para ejecutar los notebooks de forma interactiva en la nube. Haz clic en los badges de la siguiente secciÃ³n.

### 3. GitHub Codespaces (Alternativa "cero instalaciÃ³n")
Si tienes acceso a esta funciÃ³n, puedes lanzar un entorno de desarrollo completo en tu navegador con un solo clic, sin instalar nada en tu mÃ¡quina.

## ðŸ“š MÃ³dulos y Notebooks

El contenido se divide en cuatro mÃ³dulos principales. Cada uno tiene un notebook asociado que sirve como lecciÃ³n interactiva.

| MÃ³dulo | DescripciÃ³n | Notebook | Abrir en Colab |
| :--- | :--- | :--- | :--- |
| **01. Big Data** | IntroducciÃ³n al paradigma Big Data y tÃ©cnicas de muestreo eficientes. | `01_BigData_Intro.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/01_BigData_Intro.ipynb) |
| **02. Grafos** | Fundamentos, algoritmos de recorrido (BFS/DFS) y propiedades espectrales. | `02_Graphs_Fundamentals.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/02_Graphs_Fundamentals.ipynb) |
| **03. Algoritmos Evolutivos** | Uso de un Algoritmo GenÃ©tico para resolver el Problema del Viajante (TSP). | `03_Evolutionary_Algorithms.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/03_Evolutionary_Algorithms.ipynb) |
| **04. AutÃ³matas Celulares**| ExploraciÃ³n de reglas elementales 1D y el Juego de la Vida de Conway. | `04_Cellular_Automata.ipynb`| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/04_Cellular_Automata.ipynb) |

## ðŸ—ºï¸ Roadmap del Proyecto
Este proyecto es una iniciativa en constante desarrollo. Los planes futuros incluyen:

- [ ] **MÃ³dulo 5: Redes Complejas**: AÃ±adir un notebook sobre mÃ©tricas de centralidad (degree, betweenness) y modelos de mundo pequeÃ±o.
- [ ] **Ejercicios Propuestos**: Incluir problemas y preguntas al final de cada notebook para reforzar el aprendizaje.
- [ ] **TraducciÃ³n al InglÃ©s**: Localizar los materiales para un mayor alcance internacional.
- [ ] **DocumentaciÃ³n Web Avanzada**: Mejorar el sitio generado con `MkDocs` para incluir explicaciones teÃ³ricas detalladas y una galerÃ­a de ejemplos.

## ðŸ“‚ Estructura del Repositorio
<details>
<summary>Haz clic para ver la estructura de archivos del proyecto</summary>

```
BigData-Graphs-Evo-CA-Classroom/
â”œâ”€â”€ README.md             # Esta descripciÃ³n del proyecto
â”œâ”€â”€ LICENSE               # Licencia de uso del cÃ³digo (MIT)
â”œâ”€â”€ CITATION.cff          # Fichero para la cita acadÃ©mica del software
â”œâ”€â”€ pyproject.toml        # Metadatos del paquete y configuraciÃ³n de herramientas
â”œâ”€â”€ requirements.txt      # Dependencias bÃ¡sicas para el usuario final
â”œâ”€â”€ .github/              # Workflows de CI/CD (tests, docs) y plantillas
â”œâ”€â”€ docs/                 # Ficheros fuente para el sitio web (incluye assets)
â”œâ”€â”€ src/classroom/        # CÃ³digo fuente modular de la librerÃ­a
â”œâ”€â”€ notebooks/            # Lecciones interactivas en formato Jupyter
â”œâ”€â”€ datasets/             # Conjuntos de datos ligeros para los ejemplos
â””â”€â”€ tests/                # Pruebas unitarias y de integraciÃ³n
```
</details>

## ðŸ¤ CÃ³mo Contribuir

Â¡Tu contribuciÃ³n es muy bienvenida! Este es un proyecto educativo que crece gracias a la comunidad.

1.  **Reporta Errores o Sugiere Mejoras**: Si encuentras un bug, una errata o tienes una idea, abre un [issue](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/issues) usando una de las plantillas.
2.  **AÃ±ade o Mejora Contenido**: Para proponer cambios en el cÃ³digo o los notebooks, sigue estos pasos:
    *   Haz un **fork** de este repositorio.
    *   Crea una rama descriptiva para tu cambio (`git checkout -b feat/agregar-ejercicios-grafos`).
    *   Realiza tus cambios y haz **commit** siguiendo un estilo convencional.
    *   AsegÃºrate de que las pruebas sigan pasando ejecutando `pytest`.
    *   Abre un **Pull Request** detallando claramente quÃ© problema resuelves o quÃ© mejora aportas.


## âš–ï¸ Licencia

El contenido de este repositorio estÃ¡ licenciado bajo los tÃ©rminos de la [Licencia MIT](LICENSE). Puedes reutilizarlo, modificarlo y distribuirlo libremente, preservando la atribuciÃ³n original.

## ðŸŽ“ Citar este trabajo
Si utilizas este material en tu investigaciÃ³n, clases o cualquier trabajo acadÃ©mico, te agradecemos que lo cites para dar crÃ©dito a sus autores. Puedes usar el fichero `CITATION.cff` que GitHub integra automÃ¡ticamente o el siguiente formato BibTeX:

```bibtex
@software{Gevatschnaider_2025_BigDataClassroom,
  author       = {S. Gevatschnaider and Community Contributors},
  title        = {{Big Data Â· Graphs Â· Evolutionary Â· Cellular Automata â€” Classroom: Interactive Educational Materials}},
  month        = aug,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {0.1.0},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom}
}
```
*(Nota: El DOI de Zenodo se puede generar creando un archivo del repositorio en la plataforma Zenodo para obtener un identificador persistente).*
```


