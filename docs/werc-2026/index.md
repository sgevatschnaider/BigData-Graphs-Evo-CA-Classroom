# WERC 2026 · Redes multinivel y competencia tecnológica

<div class="ai-hero">
<div class="ai-kicker">UNIDAD ESPECIAL AUTÓNOMA · TEORÍA DE GRAFOS Y SISTEMAS COMPLEJOS</div>
<h2>La Reina Roja en la frontera de la inteligencia artificial</h2>
<p>Elaborada a partir de la ponencia académica <em>Coordinación y competencia en la frontera de inteligencia artificial: un modelo de redes multinivel</em>, del Dr. Sergio Gevatschnaider (WERC 2026), con aplicaciones didácticas y una lectura diferenciada de <em>The Red Queen Gödel Machine</em> (Iacob et al., 2026).</p>
<div class="ai-actions">
  <a class="md-button md-button--primary" href="../assets/werc-2026/werc-laboratorio.html">▶ Abrir aula visual y laboratorios</a>
  <a class="md-button" href="../assets/werc-2026/presentacion.html">◈ Visor de diapositivas</a>
  <a class="md-button" href="modelo/">∑ Desarrollo matemático</a>
</div></div>

!!! info "Módulo independiente"
    Esta unidad agrega archivos propios. No sustituye ni renumera los contenidos anteriores de Grafos, Big Data, Evolutivos o Autómatas Celulares. La navegación previa permanece disponible.

## Una pregunta, cuatro capas

¿Cómo modifica una red de rivalidad la inversión de laboratorios de IA de frontera y bajo qué condiciones podría sostenerse una desaceleración coordinada?

| Capa | Matriz | Interpretación | Estado en la investigación |
| --- | --- | --- | --- |
| Rivalidad | **Wᶜ** (laboratorio × laboratorio) | Exposición competitiva | Juego reducido resuelto bajo hipótesis |
| Recursos | **B** (laboratorio × insumo) | Chips, nube, energía y restricciones | Caso cerrado: recurso homogéneo |
| Supervisión | **H** (supervisor × laboratorio) | Auditoría, monitoreo y detección | Agregación al nivel estatal pendiente |
| Financiera | **F** (extensión) | Financiación y valoración de activos | Diseño empírico propuesto; no calibrado |

No se suman estas matrices sin justificar su compatibilidad dimensional y económica.

## Recorrido recomendado

1. **[Intuición y matemática](modelo/)** — softmax, juego de inversión, resolvente espectral, precio sombra y coordinación.
2. **[Ocho laboratorios visuales](../assets/werc-2026/werc-laboratorio.html#lab-01)** — experimentos modificables con controles y métricas.
3. **[Ponencia académica](ponencia/)** — resultados demostrados, supuestos y límites de las simulaciones reportadas.
4. **[De las redes a las finanzas](aplicaciones/)** — mapa de variables económicas y diseño empírico.
5. **[Red Queen Gödel Machine](coevolucion/)** — agentes y evaluadores que coevolucionan, como lectura complementaria.
6. **[Autoevaluación y glosario](evaluacion/)** — términos, ejercicios, cuestionario interactivo.
7. **[Fuentes y trazabilidad](referencias/)** — bibliografía, evidencia y advertencias.

## 8 experiencias interactivas

| # | Laboratorio | Pregunta |
| --- | --- | --- |
| 01 | [Reina Roja](../assets/werc-2026/werc-laboratorio.html#lab-01) | ¿Qué sucede con la cuota si todos mejoran? |
| 02 | [Red Wᶜ](../assets/werc-2026/werc-laboratorio.html#lab-02) | ¿Qué estructura tienen las influencias estratégicas? |
| 03 | [Equilibrio en red](../assets/werc-2026/werc-laboratorio.html#lab-03) | ¿Cómo importan el espectro y la topología? |
| 04 | [Familias de redes](../assets/werc-2026/werc-laboratorio.html#lab-04) | ¿Cómo contrastar ER, WS, BA y SBM? |
| 05 | [Infraestructura](../assets/werc-2026/werc-laboratorio.html#lab-05) | ¿Por qué surge un precio sombra? |
| 06 | [Coordinación](../assets/werc-2026/werc-laboratorio.html#lab-06) | ¿Cómo influyen sanción y detección? |
| 07 | [Capas económicas](../assets/werc-2026/werc-laboratorio.html#lab-07) | ¿Cómo distinguir competencia, recursos y financiación? |
| 08 | [Coevolución](../assets/werc-2026/werc-laboratorio.html#lab-08) | ¿Qué sucede si cambia el propio evaluador? |

## Qué es riguroso y qué queda por demostrar

**Teoremas condicionales:** invariancia de cuotas softmax; equilibrio interior bajo condición espectral; precio sombra del recurso homogéneo vinculante; restricción de incentivo del juego repetido. **Experimentación:** 480 redes sintéticas reportadas por la ponencia, con estadísticas resumidas; este portal NO pretende reproducir sin el CSV/código generador originales esas realizaciones. **Agenda futura:** el juego dinámico conjunto, la supervisión estatal desde H, la red financiera F y la calibración industrial.

!!! warning "Advertencia esencial"
    Las animaciones, valores de sliders y redes ficticias **no son hechos observados** sobre OpenAI, Anthropic, Google u otros actores. La identidad de la Reina Roja no demuestra automáticamente ineficiencia social. El artículo RQGM no es una validación empírica del modelo de WERC.

**Autor:** Dr. Sergio Gevatschnaider · Universidad de Palermo, Facultad de Ingeniería · Doctor en Ciencias Económicas, Universidad de Buenos Aires.

[Consultar fuentes y detalles de procedencia →](referencias/){ .md-button }
