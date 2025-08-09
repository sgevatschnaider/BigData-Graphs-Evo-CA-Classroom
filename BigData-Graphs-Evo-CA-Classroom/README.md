# Big Data · Graphs · Evolutionary · Cellular Automata — Classroom

Esta es una colección de materiales didácticos para un curso introductorio a Big Data, grafos, algoritmos evolutivos y autómatas celulares.  El objetivo es ofrecer notebooks reproducibles, datasets ligeros y módulos de código reutilizables que faciliten la enseñanza y el aprendizaje.  El repositorio se complementa con [GraphAI‑Data‑Science‑ML](https://github.com/sgevatschnaider/GraphAI-Data-Science-ML), que contiene demos exploratorios y material de investigación.

## Estado del proyecto

⚠️ Este repositorio es un esqueleto inicial. Los badges a continuación son ejemplos; debes actualizar `<usuario>` y `<repo>` con tu usuario de GitHub una vez lo publiques.

| Badge | Descripción |
|------|-------------|
| ![Tests](https://github.com/<usuario>/<repo>/actions/workflows/tests.yml/badge.svg) | CI que corre `pytest` y ejecuta todos los notebooks con `nbmake`. |
| ![Docs](https://github.com/<usuario>/<repo>/actions/workflows/pages.yml/badge.svg) | Publicación automática del sitio de clase con MkDocs. |
| ![MIT](https://img.shields.io/badge/license-MIT-blue.svg) | Licencia abierta para reutilizar el contenido. |

## Cómo empezar

Clona este repositorio y crea un entorno virtual con Python ≥ 3.10.  Luego instala el paquete en modo editable y las dependencias:

```bash
pip install -e .
pip install -r requirements.txt
pytest      # corre las pruebas unitarias y ejecuta los notebooks
```

Si prefieres usar Conda, crea un entorno con las versiones equivalentes de las bibliotecas de `requirements.txt`.

## Notebooks

Los notebooks están en el directorio `notebooks/`.  Cada archivo incluye al inicio un enlace para abrirse en Colab.  A continuación un listado de los principales notebooks (los enlaces deben actualizarse al publicar el repo):

- **01_BigData_Intro.ipynb** – Introducción a Big Data y técnicas de muestreo.  
- **02_Graphs_Fundamentals.ipynb** – Fundamentos de grafos: BFS/DFS y propiedades espectrales.  
- **03_Evolutionary_Algorithms.ipynb** – Algoritmos evolutivos: GA para el problema del viajante (TSP).  
- **04_Cellular_Automata.ipynb** – Autómatas celulares: reglas 1D y Game of Life.

Cada notebook se puede ejecutar localmente o en Colab.  Para Colab, sustituye `<usuario>` y `<repo>` en el siguiente enlace: `https://colab.research.google.com/github/<usuario>/<repo>/blob/main/notebooks/01_BigData_Intro.ipynb`.

## Estructura del proyecto

El repositorio sigue esta estructura:

```
BigData-Graphs-Evo-CA-Classroom/
├── README.md             # esta descripción
├── LICENSE               # licencia MIT
├── CITATION.cff          # cita recomendada
├── pyproject.toml        # configuración del paquete y dependencias
├── requirements.txt      # dependencias básicas
├── .gitignore            # archivos a ignorar por git
├── .pre-commit-config.yaml # configuración de pre-commit
├── .github/
│   ├── workflows/
│   │   ├── tests.yml    # CI: pytest + nbmake
│   │   └── pages.yml    # GitHub Pages con MkDocs
│   └── ISSUE_TEMPLATE/  # plantillas para issues
├── docs/
│   ├── index.md          # portada del sitio
│   ├── syllabus.md       # programa del curso
│   ├── schedule.md       # cronograma
│   └── modules/
│       ├── 01-bigdata.md
│       ├── 02-graphs.md
│       ├── 03-evolutionary.md
│       └── 04-cellular-automata.md
├── src/
│   └── classroom/
│       ├── __init__.py
│       ├── bigdata/
│       │   ├── sampling.py
│       │   └── spark_utils.py
│       ├── graphs/
│       │   ├── traversal.py
│       │   ├── spectral.py
│       │   └── link_prediction.py
│       ├── evo/
│       │   ├── ga_tsp.py
│       │   └── selection.py
│       └── ca/
│           ├── elementary.py
│           └── game_of_life.py
├── notebooks/
│   ├── 01_BigData_Intro.ipynb
│   ├── 02_Graphs_Fundamentals.ipynb
│   ├── 03_Evolutionary_Algorithms.ipynb
│   └── 04_Cellular_Automata.ipynb
├── datasets/
│   ├── karate.csv
│   ├── grid_50x50.npz
│   └── tsp_50_cities.csv
└── tests/
    ├── test_graphs.py
    ├── test_evo.py
    ├── test_ca.py
    └── test_notebooks.py
```

## Contribuir

Las contribuciones son bienvenidas. Para proponer cambios, crea un *fork* del repositorio, trabaja en una rama descriptiva y abre un *pull request*.  Asegúrate de que el CI se mantenga en verde ejecutando `pytest` y verificando que los notebooks sigan corriendo.

## Licencia

El contenido de este repositorio está licenciado bajo [MIT](LICENSE).  Puedes reutilizarlo y adaptarlo libremente, siempre y cuando preserves la atribución original.

