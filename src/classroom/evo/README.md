<div align="center">
  <h1>🧬 EvoAlgo — README</h1>
  <p>Teoría y práctica aplicada de <b>Algoritmos Evolutivos (EA)</b> para docencia y desarrollo.</p>

## Recurso visual — Frente de Pareto (MOEA)

Animación del **frente de Pareto** (2 objetivos) y el avance de una población **NSGA-II**: útil para introducir **dominancia**, **diversidad** (crowding) y **elitismo** en multiobjetivo. &#x20;

![Animación de Frente de Pareto](images/pareto.gif)

  <p>
    <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.10%20|%203.11-blue"></a>
    <a href="../LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
    <a href="https://pre-commit.com/"><img alt="pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"></a>
  </p>

  <p>
    <a href="./notebooks/"><img alt="Notebooks" src="https://img.shields.io/badge/📓%20Notebooks-EA-orange"></a>
    <a href="./data/"><img alt="Data" src="https://img.shields.io/badge/🗂️%20Data-benchmarks|config-lightgrey"></a>
    <a href="./images/"><img alt="Images" src="https://img.shields.io/badge/🖼️%20Images-diagrams|figures-lightgrey"></a>
    <a href="./references/"><img alt="References" src="https://img.shields.io/badge/📚%20References-papers|books-lightgrey"></a>
  </p>
</div>

---

## Estructura local

```
EvoAlgo/
├── README.md
├── notebooks/
├── src/               # operadores, estrategias y utilidades
├── data/              # instancias (TSP, knapsack, etc.)
├── images/            # figuras y gifs docentes
└── references/        # bibliografía, slides, bibtex
```

---

## Objetivos de aprendizaje

Al completar esta sección podrás:

* Entender el **ciclo general** de un EA: inicialización → **selección parental** → **recombinación** → **mutación** → **selección ambiental** → parada.&#x20;
* Conocer familias principales: **GA/SGA**, **ES**, **EP**, **GP** (historia, representación y operadores).&#x20;
* Implementar **DE** (Differential Evolution) y **PSO** (Swarm) y compararlos con GA/ES. &#x20;
* Aplicar **MOEA**: Pareto, **NSGA-II/III**, descomposición (MOEA/D) e hipervolumen. &#x20;
* Relacionar principios (variación + selección) con el **Teorema No Free Lunch** para diseño de variantes específicas al dominio.&#x20;

---

## Instalación rápida

Requisitos sugeridos:

* Python ≥ 3.10
* Paquetes: `numpy`, `pandas`, `matplotlib`, `scipy`, `jupyter`, `deap`, `pymoo`, `cmaes`, `nevergrad`
* *(opcionales)*: `networkx` (TSP/graph utils), `plotly` (figuras interactivas)

```bash
# Desde EvoAlgo/
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install numpy pandas matplotlib scipy jupyter deap pymoo cmaes nevergrad
jupyter lab  # o jupyter notebook
```

Abre los cuadernos en `notebooks/` para la ruta guiada.

---

## Tabla de contenidos

* [1) Fundamentos teóricos](#1-fundamentos-teóricos)
* [2) Componentes de un EA](#2-componentes-de-un-ea)
* [3) Algoritmos esenciales (y complejidad práctica)](#3-algoritmos-esenciales-y-complejidad-práctica)
* [4) Optimización multiobjetivo (MOEA)](#4-optimización-multiobjetivo-moea)
* [5) Práctica con datos](#5-práctica-con-datos)
* [6) Buenas prácticas (ingeniería + docencia)](#6-buenas-prácticas-ingeniería--docencia)
* [7) Aplicaciones típicas](#7-aplicaciones-típicas)
* [8) Roadmap sugerido de notebooks](#8-roadmap-sugerido-de-notebooks)
* [9) Ejercicios propuestos](#9-ejercicios-propuestos)
* [10) Errores comunes](#10-errores-comunes)
* [11) Enlaces internos y bibliografía](#11-enlaces-internos-y-bibliografía)
* [12) Contribución](#12-contribución)
* [13) Licencia](#13-licencia)
* [Apéndice A — Pseudocódigo docente](#apéndice-a--pseudocódigo-docente)
* [Apéndice B — Plantilla mínima de notebook](#apéndice-b--plantilla-mínima-de-notebook)

---

## 1) Fundamentos teóricos

**Resumen EA.** Los EA son **meta-algoritmos robustos** de búsqueda estocástica basados en población; recombinación y mutación crean variación, y la selección dirige la búsqueda.&#x20;
**NFL.** No existe “el mejor algoritmo” universal; conviene crear variantes específicas de dominio (representación + operadores).&#x20;

---

## 2) Componentes de un EA

* **Representación**: binaria, enteros, reales, permutaciones, árboles/programas, grafos, etc.&#x20;
* **Selección parental**: ruleta, **SUS**, **torneo** (k pequeño).&#x20;
* **Recombinación**: 1-punto / uniforme / aritmética (para reales). &#x20;
* **Mutación**: bit-flip (SGA), normales sesgadas/no sesgadas (reales). &#x20;
* **Selección ambiental (ES)**: esquemas (μ,λ) y (μ+λ).&#x20;

---

## 3) Algoritmos esenciales (y complejidad práctica)

| Familia    | Idea (muy breve)                                                           | Notas clave                                          |
| ---------- | -------------------------------------------------------------------------- | ---------------------------------------------------- |
| **SGA/GA** | Población binaria, **ruleta**, **1-punto**, **bit-flip**                   | Esqueleto canónico de Holland/DeJong/Goldberg.       |
| **ES**     | Reales + *self-adaptation* de pasos; selección (μ,λ)/(μ+λ)                 | Ciclo ES y 1/5-rule (histórico).                     |
| **DE**     | Mutación por **diferencias**: $v = x_a + F(x_b-x_c)$; *rand/1*, *best/1*   | Cruce uniforme con resguardo; reemplazo por mejor.   |
| **PSO**    | Partículas con memoria: $v \leftarrow v + c_1 r (pBest-x)+c_2 r (gBest-x)$ | Sin operadores genéticos; cooperación vía gBest.     |

> **Nota docente**: el **ciclo general EA** unifica estas variantes (difiere en representación/operadores/selección).&#x20;

---

## 4) Optimización multiobjetivo (MOEA)

**Dominancia y Pareto.** Definiciones formales y frente de Pareto para $f_1,\dots,f_n$. &#x20;

**NSGA-II.** Corrige NSGA: reemplaza *niching dshare* por **crowding distance**; introduce **elitismo** (unión P∪Q y truncamiento por frentes + crowding). &#x20;

**NSGA-III.** Para muchos objetivos: **puntos de referencia** y selección por direcciones subrepresentadas. &#x20;

**Otros MOEA.** VEGA, descomposición (MOEA/D), hipervolumen.&#x20;

**Mermaid — esquema NSGA-II (alto nivel):**

```mermaid
flowchart LR
  P0[Padres P_t] --> Q0[Variación: crossover+mutación]
  Q0 --> M0[P' (offspring)]
  M0 --> U0[Unión U = P_t ∪ P']
  U0 --> S0[Ordenar por frentes no dominados]
  S0 --> T0[Truncar por crowding distance]
  T0 --> P1[Nueva población P_{t+1}]
```

---

## 5) Práctica con datos

### 5.1 Formatos en `data/`

* `*.tsp` / `*.csv` (coordenadas, matrices de distancias), `knapsack/*.csv` (ítems, pesos, valores), JSON/YAML para **configs de experimento**.

### 5.2 Quick-start (SGA mínimo con DEAP)

```python
import random, numpy as np
from deap import base, creator, tools

# Maximize f(x) = sum(bits)
N = 50
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, N)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", lambda ind: (sum(ind),))
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/N)
toolbox.register("select", tools.selTournament, tournsize=3)

pop = toolbox.population(n=100)
for _ in range(100):
    off = tools.selTournament(pop, len(pop), 3)
    off = list(map(toolbox.clone, off))
    for c1, c2 in zip(off[::2], off[1::2]): tools.cxOnePoint(c1, c2)
    for ind in off: toolbox.mutate(ind); del ind.fitness.values
    fits = list(map(toolbox.evaluate, off))
    for ind, fit in zip(off, fits): ind.fitness.values = fit
    pop[:] = tools.selBest(pop + off, k=len(pop))
best = tools.selBest(pop, 1)[0]
print(sum(best))
```

### 5.3 Tareas combinatorias (TSP, knapsack)

* TSP: usar **operadores específicos de permutaciones** (PMX, OX, CX, ER); el cruce clásico no sirve directamente. &#x20;
* Knapsack 0-1: binario + fitness con restricciones / o MOEA. &#x20;

---

## 6) Buenas prácticas (ingeniería + docencia)

* **Semillas** y **presupuestos** (n evals) claros; registra configuración y resultados.
* **Representación acorde al problema** (p. ej., permutaciones para rutas).&#x20;
* **Elitismo/diversidad**: evita convergencia prematura (NSGA-II/III en MOEA).&#x20;
* Personaliza al dominio (NFL): ajusta operadores/encodings.&#x20;

---

## 7) Aplicaciones típicas

* **Combinatoria**: TSP, knapsack, scheduling/job-shop.&#x20;
* **Machine Learning**: **LCS/XCS**, reglas, RL evolutivo.&#x20;
* **Neuroevolución/GP**: evolución de programas/árboles y grafos. &#x20;

---

## 8) Roadmap sugerido de notebooks

| Notebook                         | Tema                                               | Colab |
| -------------------------------- | -------------------------------------------------- | ----- |
| `01_intro_ea.ipynb`              | Motivación, ciclo EA, NFL                          | —     |
| `02_ga_sga.ipynb`                | SGA: ruleta, 1-punto, bit-flip, esquemas           | —     |
| `03_es_de.ipynb`                 | ES ((μ,λ)/(μ+λ)) + DE (*rand/1*, *best/1*)         | —     |
| `04_pso.ipynb`                   | PSO: ecuaciones y variantes                        | —     |
| `05_moea_nsga.ipynb`             | Pareto, NSGA-II/III, hipervolumen                  | —     |
| `06_combinatoria_tsp_knap.ipynb` | Operadores de permutación (PMX/OX/CX/ER), knapsack | —     |
| `07_gp.ipynb`                    | Programación genética (árboles)                    | —     |
| `08_lcs_xcs.ipynb`               | LCS/XCS + refuerzo                                 | —     |

---

## 9) Ejercicios propuestos

### Teoría

1. Demuestra por qué **elitismo + crowding** mejora preservación de Pareto frente a NSGA clásico.&#x20;
2. Compara **(μ,λ)** vs **(μ+λ)** respecto a exploración/explotación.&#x20;
3. Explica NFL y sus implicancias en el diseño de operadores.&#x20;

### Práctica

1. **SGA** sobre *OneMax* y **DE** sobre *Sphere*; reporta curva fitness-evaluaciones.&#x20;
2. **TSP** (50–100 ciudades): compara PMX/OX/CX/ER + 2-opt local.&#x20;
3. **Knapsack** multiobjetivo: usado con NSGA-II; visualiza el frente.&#x20;
4. **PSO vs GA** en 10 funciones de caja negra; analiza sensibilidad a $c_1,c_2$.&#x20;

---

## 10) Errores comunes

* Usar **crossover clásico** en **permutaciones** (p. ej., TSP) → genera inválidos o destruye estructura; emplea PMX/OX/CX/ER.&#x20;
* Ignorar **diversidad** en MOEA → colapso del frente; usa crowding/elitismo.&#x20;
* Representación no acorde al problema (binario para reales finos o viceversa).&#x20;
* Asumir un **EA universalmente mejor** (violando NFL).&#x20;

---

## 11) Enlaces internos y bibliografía

* **Notebooks**: `./notebooks/`
* **Datos**: `./data/` (TSP, knapsack, configs)
* **Imágenes**: `./images/`
* **Referencias**: `./references/`

**Bibliografía sugerida** (añade en `references/bibliography.bib`):

* Eiben & Smith — *Introduction to Evolutionary Computing* (Springer, 2007)
* Michalewicz — *Genetic Algorithms + Data Structures = Evolution Programs* (3ª ed., 1996)
* Mitchell — *Introduction to Genetic Algorithms* (MIT Press, 1996)
* Holland — *Adaptation in Natural and Artificial Systems* (MIT Press, 1992)
* Goldberg — *Genetic Algorithms in Search, Optimization and Machine Learning* (Addison-Wesley, 1989)&#x20;

---

## 12) Contribución

1. Crea una rama: `feature/ea-tema`.
2. Añade datasets/configs en `data/` con `README.md` describiendo columnas/atributos.
3. Incluye notebooks autocontenidos (semillas fijas, dependencias indicadas).
4. Abre un **Pull Request** con resultados y figuras en `images/`.

---

## 13) Licencia

Este material se distribuye bajo **MIT** (código) y sugiere **CC BY 4.0** para contenidos docentes (textos/figuras). Revisa `LICENSE` en la raíz del repositorio.

---

## Apéndice A — Pseudocódigo docente

**Esqueleto EA (genérico)**&#x20;

```
EA(problem):
  P ← InicializarPoblación()
  evaluar(P)
  while !criterio_parada:
      padres ← seleccionar_parental(P)
      hijos  ← recombinar_mutar(padres)
      evaluar(hijos)
      P ← seleccionar_ambiental(P, hijos)  # elitismo si aplica
  return mejor(P)
```

**SGA (binario)**&#x20;

```
SGA(f, n, l, pC, pM):
  P ← n individuos de l bits al azar
  while !parada:
      P' ← ∅
      repetir n/2 veces:
          x, y ← selección_ruleta(P)
          if rand() < pC: x, y ← crossover_1p(x, y)
          x ← mut_bitflip(x, pM); y ← mut_bitflip(y, pM)
          P' ← P' ∪ {x, y}
      P ← P'  # reemplazo generacional
```

**DE (rand/1/bin)** &#x20;

```
DE(f, N, F, CR):
  P ← {x_i}^N inicial al azar
  while !parada:
      for cada i:
          a,b,c ← índices distintos de i
          v ← x_a + F*(x_b - x_c)
          u ← binomial_crossover(x_i, v, CR)  # al menos 1 gen de v
          x_i ← mejor(u, x_i)  # reemplazo si mejora
```

**PSO (gbest)**&#x20;

```
PSO(f, N, c1, c2):
  inicializar {x_i, v_i}; pBest_i ← x_i; gBest ← argmin f(pBest_i)
  while !parada:
      for i in 1..N:
          v_i ← v_i + c1*r()*(pBest_i - x_i) + c2*r()*(gBest - x_i)
          x_i ← x_i + v_i
          actualizar pBest_i y gBest
```

---

## Apéndice B — Plantilla mínima de notebook

```markdown
# Título: <Tema del notebook>

## Objetivos
- …

## Problema / Dataset
- Ruta: data/…

## Configuración
- Semilla: …
- Presupuesto (evaluaciones / tiempo): …

## Pasos
1. Definir representación y operadores
2. Configurar selección (parental/ambiental)
3. Ejecutar (k runs) y registrar métricas
4. Analizar curvas y/o frente de Pareto

## Resultados
- Métricas / Figuras

## Conclusiones
- …
```




