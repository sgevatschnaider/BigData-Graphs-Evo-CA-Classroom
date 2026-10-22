# Investigación complementaria · Red Queen Gödel Machine

**Fuente:** Iacob, Jovanović, Shen y colaboradores (2026), *The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators*, [arXiv:2606.26294](https://arxiv.org/abs/2606.26294). El PDF adjunto corresponde a la versión 2, fechada el 29 de junio de 2026.

## Por qué dialoga con WERC

El manuscrito WERC aborda competencia estratégica en redes: esfuerzos, capacidades, participación relativa, infraestructura y coordinación. El artículo RQGM estudia otro fenómeno: **agentes que mejoran al mismo tiempo que los evaluadores encargados de medirlos**.

El vínculo es intelectual —competencia y adaptación con objetivos móviles—, pero los teoremas y sus objetos son diferentes.

## Método descrito por el paper

1. La búsqueda de agentes y evaluadores se divide en **épocas**.
2. Cada evaluador utilizado permanece fijo dentro de su época.
3. Se buscan agentes mejores y **evaluadores candidatos**.
4. En puntos de control, la promoción del evaluador depende de un conjunto ancla de referencia independiente.
5. El sistema descarta **selectivamente** los registros de utilidad asociados al evaluador desplazado, conservando otros registros y permitiendo re-evaluaciones futuras.

Las garantías estudiadas son condicionales por época; no equivalen a una convergencia global de todas las utilidades cambiantes. La implementación con evaluadores aprendidos no es un oráculo matemático perfecto.

## Qué reporta el preprint aportado

El PDF v2 expone experimentos en programación, redacción/revisión de artículos y corrección de pruebas matemáticas. Entre los resultados concretos del dominio de programación, comunica una tasa retenida de 71.7% para su configuración RQGM frente al 69.9% de su baseline, con ahorros de tokens de búsqueda. Son **resultados de los autores**, no de WERC ni de esta simulación.

## Diferencias clave

| WERC | RQGM |
| --- | --- |
| Jugadores económicos y redes entre laboratorios | Agentes de tarea y evaluadores aprendidos |
| Wᶜ y respuesta estratégica | Archivo de variantes y proceso de búsqueda |
| Equilibrio Nash bajo condición espectral | Búsqueda evolutiva con criterio fijo por época |
| Recurso K y precio sombra μ | Presupuestos de evaluación y costos de búsqueda |
| Supervisión estatal H como extensión abierta | Evaluadores promovidos según un ancla |
| Agenda empírica industrial pendiente | Benchmarks computacionales del preprint |

## Experimento interactivo

[Comparar evaluador fijo y evaluador móvil](../assets/werc-2026/werc-laboratorio.html#lab-08){ .md-button .md-button--primary }

**Límite:** el simulador solo dibuja una analogía matemática simplificada de un criterio cambiante. **No implementa RQGM**, ni sus reglas de búsqueda, validación, borrado selectivo o garantías.

## Preguntas futuras

- ¿Cómo medir q_i si los benchmarks también cambian con los modelos?
- ¿Puede relacionarse el criterio dinámico de calidad con cuotas comparables?
- ¿Qué variables adicionales requiere un modelo industrial dinámico de coevolución?
- ¿Cómo separar el cambio del objetivo de una verdadera mejora de desempeño?

!!! warning "Precaución"
    RQGM no constituye una validación empírica del equilibrio del juego WERC ni prueba la estabilidad de acuerdos entre Estados.

[Volver al módulo](index.md){ .md-button }
