# Big Data · Graphs · Evolutionary · Cellular Automata — Classroom

[![Tests](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/tests.yml/badge.svg)](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/tests.yml)
[![Docs](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/actions/workflows/pages.yml/badge.svg)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Material docente **reproducible** que integra **Teoría de Grafos**, **Algoritmos Evolutivos** y **Autómatas Celulares** con **aplicaciones en Big Data, Machine Learning (ML) e Inteligencia Artificial (IA)**.  
Incluye notebooks interactivos (Colab), módulos en `src/`, **tests** automatizados y **documentación** con MkDocs.

---

## 🎯 Resultados de aprendizaje
Al finalizar, el estudiante podrá:
- Implementar **BFS/DFS** y calcular **espectro de grafos** (λ₂: conectividad algebraica) para extraer *features* útiles en ML.
- Diseñar y ejecutar un **algoritmo evolutivo (GA)** para **TSP** y adaptarlo a tareas de optimización en datos.
- Modelar **Autómatas Celulares** (1D y **Game of Life**) para analizar difusión/contagio y dinámicas espaciotemporales.
- Construir **pipelines reproducibles** con notebooks y módulos en Python, validando con **tests** y **nbmake**.
- Interpretar resultados y comunicar métricas relevantes para **Big Data/ML/IA**.

---

## 🧭 Mapa de contenidos (tres ejes)

**1) Grafos → Big Data/ML/IA**
- **BFS/DFS** para recorridos y extracción de subestructuras en grandes volúmenes.
- **Espectro de grafos (λ₂)**: conectividad algebraica como *feature* para modelos de ML.
- **Centralidades y medidas estructurales** para **feature engineering**, detección de **anomalías** y **sistemas de recomendación**.
- **Graph sampling** y consideraciones de **escalabilidad** en pipelines de Big Data.

**2) Algoritmos Evolutivos → ML/IA**
- **Optimización de hiperparámetros** y **selección de características**.
- **Búsqueda de arquitecturas/heurísticas** y meta-heurísticas en problemas combinatorios ligados a datos.
- **GA para TSP** como caso base y plantilla para otras tareas de optimización.

**3) Autómatas Celulares → Big Data/ML/IA**
- **Modelado de difusión/contagio** y fenómenos en redes de datos.
- **Dinámica espaciotemporal** y patrones emergentes (1D y **Game of Life**).
- **Simulación y generación de datos sintéticos** para análisis y validación de modelos.

---

## 📓 Notebooks (Open in Colab)
- **01 Big Data Intro** — [Open in Colab](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/01_BigData_Intro.ipynb)
- **02 Graphs Fundamentals** — [Open in Colab](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/notebooks/02_Graphs_Fundamentals.ipynb)

> **Nota:** se irán añadiendo nuevos notebooks a lo largo del curso.

---

## ⚡️ Inicio rápido

```bash
# 1) Instalar dependencias y el paquete en modo editable
pip install -r requirements.txt
pip install -e .

# 2) Ejecutar tests (unitarios y de integración)
pytest -q

# 3) Verificar notebooks con nbmake (ejecución de punta a punta)
pytest --nbmake notebooks/01_BigData_Intro.ipynb
pytest --nbmake notebooks/02_Graphs_Fundamentals.ipynb
