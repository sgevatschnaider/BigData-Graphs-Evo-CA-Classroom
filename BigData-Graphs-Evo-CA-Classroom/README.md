<div align="center">
  <h1>Big Data · Graphs · Evolutionary · Cellular Automata — Classroom</h1>
</div>

<p align="center">
  <i>Materiales didácticos interactivos y reproducibles para la enseñanza de conceptos avanzados en computación.</i>
</p>

<p align="center">
  <a href="https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/tests.yml"><img alt="CI" src="https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/tests.yml/badge.svg?branch=main"></a>
  <a href="https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/"><img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fsgevatschnaider.github.io%2FBigData-Graphs-Evo-CA-Classroom%2F"></a>
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/python-3.10 | 3.11-blue"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="https://pre-commit.com/"><img alt="pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
</p>

---

Este repositorio contiene una colección de materiales didácticos para un curso introductorio a **Big Data, Grafos, Algoritmos Evolutivos y Autómatas Celulares**.

El objetivo es ofrecer notebooks reproducibles, datasets ligeros y módulos de código reutilizables para facilitar la enseñanza y el aprendizaje. Este repositorio se complementa con [GraphAI‑Data‑Science‑ML](https://github.com/sgevatschnaider/GraphAI-Data-Science-ML), que contiene demos exploratorias y material de investigación.

## 📋 Tabla de Contenidos
*   [✨ ¿Por qué este curso?](#-por-qué-este-curso)
*   [🎯 Público Objetivo y Requisitos](#-público-objetivo-y-requisitos)
*   [🛠️ Uso y Ejecución](#️-uso-y-ejecución)
*   [📚 Módulos y Notebooks](#-módulos-y-notebooks)
*   [🗺️ Roadmap del Proyecto](#️-roadmap-del-proyecto)
*   [📂 Estructura del Repositorio](#-estructura-del-repositorio)
*   [🤝 Cómo Contribuir](#-cómo-contribuir)
*   [⚖️ Licencia](#️-licencia)
*   [🎓 Citar este trabajo](#-citar-este-trabajo)


## ✨ ¿Por qué este curso?
*   **Enfoque Práctico**: Aprendizaje basado en la ejecución y modificación de código real.
*   **Reproducibilidad**: Notebooks listos para ejecutar localmente o en la nube (Google Colab).
*   **Modularidad**: Código fuente organizado en módulos para facilitar su reutilización y estudio.
*   **Open Source**: Totalmente abierto a contribuciones y mejoras de la comunidad.

## 🎯 Público Objetivo y Requisitos

Este material está diseñado para:
*   Estudiantes de grado en Ciencias de la Computación, Ingeniería o carreras afines.
*   Autodidactas con interés en temas avanzados de algoritmia e inteligencia artificial.
*   Profesores que busquen material de apoyo interactivo para sus clases.

**Requisitos Previos:**
*   Conocimientos sólidos de **Python** (funciones, clases, estructuras de datos).
*   Familiaridad con conceptos de **álgebra lineal** y **estadística** elemental.
*   Experiencia básica usando la terminal y `git`.


## 🛠️ Uso y Ejecución

Tienes varias formas de ejecutar los notebooks y probar el código:

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
No requiere instalación local. Solo necesitas una cuenta de Google para ejecutar los notebooks de forma interactiva en la nube. Haz clic en los badges de la siguiente sección.

### 3. GitHub Codespaces (Alternativa "cero instalación")
Si tienes acceso a esta función, puedes lanzar un entorno de desarrollo completo en tu navegador con un solo clic, sin instalar nada en tu máquina.

## 📚 Módulos y Notebooks

El contenido se divide en cuatro módulos principales. Cada uno tiene un notebook asociado que sirve como lección interactiva.

| Módulo | Descripción | Notebook | Abrir en Colab |
| :--- | :--- | :--- | :--- |
| **01. Big Data** | Introducción al paradigma Big Data y técnicas de muestreo eficientes. | `01_BigData_Intro.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/01_BigData_Intro.ipynb) |
| **02. Grafos** | Fundamentos, algoritmos de recorrido (BFS/DFS) y propiedades espectrales. | `02_Graphs_Fundamentals.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/02_Graphs_Fundamentals.ipynb) |
| **03. Algoritmos Evolutivos** | Uso de un Algoritmo Genético para resolver el Problema del Viajante (TSP). | `03_Evolutionary_Algorithms.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/03_Evolutionary_Algorithms.ipynb) |
| **04. Autómatas Celulares**| Exploración de reglas elementales 1D y el Juego de la Vida de Conway. | `04_Cellular_Automata.ipynb`| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/04_Cellular_Automata.ipynb) |

## 🗺️ Roadmap del Proyecto
Este proyecto es una iniciativa en constante desarrollo. Los planes futuros incluyen:

- [ ] **Módulo 5: Redes Complejas**: Añadir un notebook sobre métricas de centralidad (degree, betweenness) y modelos de mundo pequeño.
- [ ] **Ejercicios Propuestos**: Incluir problemas y preguntas al final de cada notebook para reforzar el aprendizaje.
- [ ] **Traducción al Inglés**: Localizar los materiales para un mayor alcance internacional.
- [ ] **Documentación Web Avanzada**: Mejorar el sitio generado con `MkDocs` para incluir explicaciones teóricas detalladas y una galería de ejemplos.

## 📂 Estructura del Repositorio
<details>
<summary>Haz clic para ver la estructura de archivos del proyecto</summary>

```
BigData-Graphs-Evo-CA-Classroom/
├── README.md             # Esta descripción del proyecto
├── LICENSE               # Licencia de uso del código (MIT)
├── CITATION.cff          # Fichero para la cita académica del software
├── pyproject.toml        # Metadatos del paquete y configuración de herramientas
├── requirements.txt      # Dependencias básicas para el usuario final
├── .github/              # Workflows de CI/CD (tests, docs) y plantillas
├── docs/                 # Ficheros fuente para el sitio web con MkDocs
├── src/classroom/        # Código fuente modular de la librería
├── notebooks/            # Lecciones interactivas en formato Jupyter
├── datasets/             # Conjuntos de datos ligeros para los ejemplos
└── tests/                # Pruebas unitarias y de integración para asegurar la calidad
```
</details>

## 🤝 Cómo Contribuir

¡Tu contribución es muy bienvenida! Este es un proyecto educativo que crece gracias a la comunidad.

1.  **Reporta Errores o Sugiere Mejoras**: Si encuentras un bug, una errata o tienes una idea, abre un [issue](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/issues) usando una de las plantillas.
2.  **Añade o Mejora Contenido**: Para proponer cambios en el código o los notebooks, sigue estos pasos:
    *   Haz un **fork** de este repositorio.
    *   Crea una rama descriptiva para tu cambio (`git checkout -b feat/agregar-ejercicios-grafos`).
    *   Realiza tus cambios y haz **commit** siguiendo un estilo convencional.
    *   Asegúrate de que las pruebas sigan pasando ejecutando `pytest`.
    *   Abre un **Pull Request** detallando claramente qué problema resuelves o qué mejora aportas.


## ⚖️ Licencia

El contenido de este repositorio está licenciado bajo los términos de la [Licencia MIT](LICENSE). Puedes reutilizarlo, modificarlo y distribuirlo libremente, preservando la atribución original.

## 🎓 Citar este trabajo
Si utilizas este material en tu investigación, clases o cualquier trabajo académico, te agradecemos que lo cites para dar crédito a sus autores. Puedes usar el fichero `CITATION.cff` que GitHub integra automáticamente o el siguiente formato BibTeX:

```bibtex
@software{Gevatschnaider_2025_BigDataClassroom,
  author       = {S. Gevatschnaider and Community Contributors},
  title        = {{Big Data · Graphs · Evolutionary · Cellular Automata — Classroom: Interactive Educational Materials}},
  month        = aug,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {0.1.0},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom}
}
```
*(Nota: El DOI de Zenodo se puede generar creando un archivo del repositorio en la plataforma Zenodo para obtener un identificador persistente).*
