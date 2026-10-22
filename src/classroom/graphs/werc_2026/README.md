# WERC 2026 · La Reina Roja, redes multinivel y frontera de la IA

**Unidad académica autónoma | Dr. Sergio Gevatschnaider | Universidad de Palermo · Facultad de Ingeniería**

Esta carpeta es una **unidad nueva separada**; no modifica los capítulos existentes de Big Data, Grafos, Evolutivos o Autómatas Celulares. Integra teoría, derivaciones, código, 8 experimentos HTML, una presentación complementaria navegable, glosario y autoevaluación.

## Acceso directo

- **[Abrir el aula visual independiente](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/werc-2026/werc-laboratorio.html)**.
- **[Entrar en la unidad de MkDocs](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/werc-2026/)**.
- **[Visor de 20 diapositivas HTML](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/werc-2026/presentacion.html)**.
- **[Cuestionario interactivo, 16 preguntas](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/werc-2026/cuestionario.html)**.
- **[Notebook reproducible en Google Colab](https://colab.research.google.com/github/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/src/classroom/graphs/werc_2026/WERC2026_Redes_Multinivel.ipynb)**.

## Investigación de base

La ponencia *Coordinación y competencia en la frontera de inteligencia artificial: un modelo de redes multinivel* (WERC 2026, 22 de octubre) formula una arquitectura con tres matrices conceptualmente distintas:

- **Wᶜ, competencia:** relaciones laboratorio–laboratorio.
- **B, infraestructura:** uso de chips, nube, energía y recursos.
- **H, supervisión:** cobertura institucional y verificación.
- **F, financiación:** extensión propuesta, no calibrada.

La ponencia desarrolla resultados delimitados: invariancia de cuota softmax; equilibrio interior de un juego lineal-cuadrático bajo condición espectral; capacidad homogénea vinculante y precio sombra; y condición reducida de incentivos a cooperar. Reporta estadísticas de 480 grafos sintéticos; **no** representa una estimación causal industrial ni un equilibrio multinivel general concluido.

La investigación externa *The Red Queen Gödel Machine* (Iacob et al., 2026) se estudia como **lectura complementaria** sobre búsqueda de agentes y evaluadores coevolutivos. No constituye evidencia empírica de los resultados económicos WERC.

## Laboratorios

| # | Tema | Mecánica |
| --- | --- | --- |
| 01 | Reina Roja | Control de capacidad y β, cuotas softmax comparables |
| 02 | Red competitiva | Estrella y camino, adyacencia, grados y espectro |
| 03 | Equilibrio | η, condición espectral, esfuerzos y comparación |
| 04 | Topologías | ER, WS, BA, SBM; 24 nodos y 48 enlaces, generación nueva |
| 05 | Recursos | K y μ, asignación con una restricción homogénea |
| 06 | Coordinación | G, d, sanción, δ y pérdida futura |
| 07 | Multicapa | W, B, H, F (vínculos ficticios) |
| 08 | RQGM | Analogía de evaluadores fijos y móviles (no implementa RQGM) |

### Advertencias indispensables

El código que genera nuevas redes de 24 nodos **no es el generador original del CSV WERC**. La tabla de medias reportadas en el paper está señalada como tal. La fórmula del recurso homogéneo **no se extrapola** a recursos heterogéneos sin resolver nuevas condiciones. El ejercicio RQGM simplificado no reproduce el algoritmo del preprint ni sus garantías.

## Archivos

| Archivo | Uso |
| --- | --- |
| models.py | Softmax, equilibrio interior, sombra del recurso, incentivo y generadores sintéticos |
| WERC2026_Redes_Multinivel.ipynb | Notebook Colab con verificaciones y 480 nuevas redes |
| docs/assets/werc-2026/werc-laboratorio.html | Portal HTML principal con 8 laboratorios |
| docs/assets/werc-2026/werc-labs.js | Motor gráfico e interactivo |
| docs/assets/werc-2026/werc.css | Sistema visual independiente responsive |
| docs/assets/werc-2026/presentacion.html | Presentación de estudio, 20 láminas HTML |
| docs/assets/werc-2026/cuestionario.html | 16 preguntas autocorregibles |
| docs/werc-2026/ | Textos de la unidad, matemáticas, aplicaciones, glosario y referencias |
| tests/test_werc_2026.py | Verificación de identidades y soluciones exactas |

La publicación no incorpora como binarios los PDF y PPTX originales aportados en el chat: el visor y las páginas son **obras didácticas derivadas**, no una exportación fiel del material fuente.

## Reproducibilidad

Instalar dependencias del repositorio e invocar:

    pip install -e .
    python -m pytest tests/test_werc_2026.py -q

Con el notebook en Colab, la primera celda instala el repositorio público.

### Fuentes primarias

- Sergio Gevatschnaider (2026), manuscrito WERC y presentación de la ponencia, 22 de octubre.
- Sergio Gevatschnaider (2026), *De los modelos de frontera a los mercados financieros*, documento complementario.
- Alex Iacob y colaboradores (2026), *The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators*, [arXiv:2606.26294](https://arxiv.org/abs/2606.26294); la copia analizada es v2.

**Uso:** enseñanza y exploración académica. No consejo de inversión, no predicción de relaciones corporativas y no validación causal.
