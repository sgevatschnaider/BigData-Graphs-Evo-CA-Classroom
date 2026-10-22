# Fuentes, metodología y trazabilidad

Esta unidad distingue **resultados matemáticos**, **resultados computacionales reportados**, **investigación externa** y **visualizaciones pedagógicas nuevas**.

## Material entregado por el autor

- Gevatschnaider, S. (2026). *Coordinación y competencia en la frontera de inteligencia artificial: un modelo de redes multinivel*. Manuscrito WERC de 12 páginas. **Fuente principal de las proposiciones y cifras de experimentación.**
- Gevatschnaider, S. (2026). *WERC 2026 — Ponencia*, PDF de 16 páginas y PPTX con bibliografía. **Fuente de la exposición y sus advertencias.**
- Gevatschnaider, S. (2026). *De los modelos de frontera a los mercados financieros*. Documento complementario de 14 páginas, fechado 21/10/2026. **Fuente de la matriz de aplicaciones empíricas.**

Los originales estaban adjuntos en la conversación de elaboración. **Los binarios PDF y PPTX no se incorporaron en GitHub**. El portal contiene un visor HTML nuevo, una guía de fórmulas y sus respectivas referencias; no se ofrece una copia descargable original alojada en GitHub.

## Investigación externa

- Iacob, A., Jovanović, A., Shen, W. F., et al. (2026). *The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators*. [arXiv:2606.26294](https://arxiv.org/abs/2606.26294). Se estudió la copia PDF v2 del 29/06/2026.

## Referencias clásicas

- Van Valen, L. (1973). *A New Evolutionary Law*. Evolutionary Theory, 1, 1–30.
- Ridley, M. (1993). *The Red Queen: Sex and the Evolution of Human Nature*. Viking.
- Ballester, C., Calvó-Armengol, A. y Zenou, Y. (2006). *Who's Who in Networks. Wanted: The Key Player*. Econometrica 74(5).
- Newman, M. (2010). *Networks: An Introduction*. Oxford University Press.
- Watts, D. J. y Strogatz, S. H. (1998). *Collective dynamics of small-world networks*. Nature.
- Barabási, A.-L. y Albert, R. (1999). *Emergence of scaling in random networks*. Science.
- Kipf, T. N. y Welling, M. (2016). *Variational Graph Auto-Encoders*. [arXiv:1611.07308](https://arxiv.org/abs/1611.07308).

## Matriz de estatuto

| Material | Fuente | Qué se puede sostener |
| --- | --- | --- |
| Cuota softmax | WERC, proposición 1 | Invariancia exacta con desplazamiento común |
| Equilibrio interior | WERC, proposición 2 | Resultado bajo supuestos de positividad y condición espectral |
| Estrella y camino | WERC, ecuaciones 15–16 | Soluciones algebraicas verificables |
| 480 grafos | WERC, sección 8 | Estadísticas consolidadas reportadas, no recomputadas del CSV |
| Precio sombra | WERC, proposición 3 | Caso homogéneo con K vinculante |
| Juego repetido | WERC, proposición 4 | Condición bajo detección/castigo supuestos |
| Mercados financieros | Documento complementario | Hipótesis por medir; sin estimación causal |
| Agentes y evaluadores | RQGM v2 | Investigación distinta y preprint experimental |
| Sliders, grafos nuevos, puntajes | Implementación del aula | Exclusivamente sintéticos |

## Reproducibilidad

- Motor matemático: [código Python para modelos WERC](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/src/classroom/graphs/werc_2026/models.py).
- Pruebas de valores exactos, softmax y redes: [tests/test_werc_2026.py](https://github.com/sgevatschnaider/BigData-Graphs-Evo-CA-Classroom/blob/main/tests/test_werc_2026.py).
- Aula interactiva: [ocho experimentos en HTML](../assets/werc-2026/werc-laboratorio.html).

**Advertencias:** la generadora de redes nueva ajusta WS/BA/SBM a 48 aristas cuando procede, y eso cambia las distribuciones. Una replicación exacta de WERC necesita el código y los 480 registros originales. Las relaciones económicas ilustradas con agentes ficticios no son vínculos corporativos documentados.

[Volver al módulo](index.md){ .md-button }
