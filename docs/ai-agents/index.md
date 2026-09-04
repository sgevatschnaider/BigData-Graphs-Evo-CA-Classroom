# Grafos, Sistemas Complejos y Agentes de IA

<div class="ai-hero">
  <div>
    <div class="ai-kicker">TEORÍA DE GRAFOS · SISTEMAS MULTIAGENTE · EMERGENCIA · SEGURIDAD</div>
    <h2>Del rastro local al protocolo, del protocolo a la capacidad colectiva y de la capacidad al riesgo sistémico</h2>
    <p>Unidad interactiva basada en el caso OpenAI–Hugging Face de 2026 para estudiar cómo una infraestructura compartida puede convertirse en memoria externa, cómo pueden emerger convenciones de coordinación entre agentes y cómo esas nuevas aristas alteran los caminos alcanzables dentro de un grafo de seguridad.</p>
    <div class="ai-actions">
      <a class="md-button md-button--primary" href="../assets/ai-agents/01-emergent-protocol-es.html">▶ Comenzar recorrido</a>
      <a class="md-button" href="index.en/">🌐 English</a>
      <a class="md-button" href="https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf" target="_blank" rel="noopener">↗ Informe técnico original</a>
    </div>
  </div>
</div>

!!! abstract "Idea central del módulo"
    En seguridad y en sistemas complejos, **no alcanza con estudiar nodos aislados**. Lo decisivo puede ser la aparición de nuevas aristas, memoria persistente y caminos compuestos. La unidad sigue una progresión deliberada: **comunicación emergente → coordinación → reutilización → capacidad colectiva → caminos de ataque**.

## ¿Por qué está en el módulo de Grafos?

La unidad usa la teoría de grafos como lenguaje común. Un agente, un servicio, una credencial o un workload pueden representarse como nodos; una posibilidad de leer, escribir, autenticar, reenviar o ejecutar puede representarse como una arista. A partir de allí interesa estudiar **alcanzabilidad, caminos, cambios topológicos, propagación de información y propiedades emergentes del sistema**.

<div class="concept-flow" role="list" aria-label="Secuencia conceptual">
  <span role="listitem">Rastro persistente</span><b>→</b>
  <span role="listitem">Memoria externa</span><b>→</b>
  <span role="listitem">Comunicación</span><b>→</b>
  <span role="listitem">Protocolo</span><b>→</b>
  <span role="listitem">Reutilización</span><b>→</b>
  <span role="listitem">Capacidad colectiva</span><b>→</b>
  <span role="listitem">Riesgo sistémico</span>
</div>

## Recorrido recomendado

<div class="sim-grid">
  <article class="sim-card">
    <div class="sim-number">01</div>
    <div class="sim-tag">DINÁMICA SOBRE GRAFOS</div>
    <h3>Construcción Emergente de un Protocolo Multiagente</h3>
    <p>Observa cómo agentes inicialmente aislados reutilizan un medio compartido como memoria externa, detectan rastros de otros agentes y estabilizan convenciones cada vez más estructuradas.</p>
    <ul>
      <li>memoria ambiental y persistencia;</li>
      <li>descubrimiento de pares;</li>
      <li>formación de convenciones;</li>
      <li>densidad de coordinación.</li>
    </ul>
    <div class="lang-row">
      <a class="md-button md-button--primary" href="../assets/ai-agents/01-emergent-protocol-es.html">🇪🇸 Español</a>
      <a class="md-button" href="../assets/ai-agents/01-emergent-protocol-en.html">🇬🇧 English</a>
    </div>
  </article>

  <article class="sim-card">
    <div class="sim-number">02</div>
    <div class="sim-tag">SISTEMAS COMPLEJOS</div>
    <h3>Emergencia de Capacidad Colectiva</h3>
    <p>Compara dos poblaciones idénticas: una aislada y otra con memoria compartida y protocolo. Experimenta con superposición de tareas, persistencia, latencia y confiabilidad.</p>
    <ul>
      <li>reutilización de conocimiento;</li>
      <li>trabajo duplicado;</li>
      <li>cobertura de búsqueda;</li>
      <li>ventaja colectiva simulada.</li>
    </ul>
    <div class="lang-row">
      <a class="md-button md-button--primary" href="../assets/ai-agents/02-collective-capability-es.html">🇪🇸 Español</a>
      <a class="md-button" href="../assets/ai-agents/02-collective-capability-en.html">🇬🇧 English</a>
    </div>
  </article>

  <article class="sim-card">
    <div class="sim-number">03</div>
    <div class="sim-tag">GRAFOS DE SEGURIDAD</div>
    <h3>Seguridad de Agentes de IA — Caminos de Ataque</h3>
    <p>Reconstruye conceptualmente cómo servicios permitidos, egress indirecto, credenciales y vulnerabilidades pueden encadenarse hasta producir un camino que no existe como conexión directa.</p>
    <ul>
      <li>alcanzabilidad y caminos compuestos;</li>
      <li>movimiento lateral;</li>
      <li>identidad y permisos como aristas;</li>
      <li>defensa en profundidad.</li>
    </ul>
    <div class="lang-row">
      <a class="md-button md-button--primary" href="../assets/ai-agents/03-attack-path-es.html">🇪🇸 Español</a>
      <a class="md-button" href="../assets/ai-agents/03-attack-path-en.html">🇬🇧 English</a>
    </div>
  </article>
</div>

## Del documento primario al modelo

| Capa | Qué tomamos del caso | Qué hacemos en el aula |
|---|---|---|
| **Comunicación** | Uso inesperado de Artifactory como medio persistente de comunicación entre ejecuciones. | Modelamos la transición de rastros aislados a una red de comunicación. |
| **Protocolo** | Reutilización de nombres de directorios y aparición de convenciones más estructuradas. | Variamos descubribilidad, persistencia, fricción y formación de convenciones. |
| **Capacidad** | Los agentes podían compartir hallazgos y continuar sobre resultados previos. | Comparamos una población aislada con otra capaz de persistir y reutilizar conocimiento. |
| **Seguridad** | Servicios, credenciales, vulnerabilidades y permisos fueron encadenándose en caminos de acceso. | Representamos recursos como nodos y capacidades de acceso como aristas para estudiar reachability y attack paths. |

!!! warning "Hechos documentados vs. métricas pedagógicas"
    Las simulaciones **no son reproducciones probabilísticas del incidente**. Fechas, mecanismos generales y algunos hitos se apoyan en el informe técnico; métricas como *densidad de coordinación*, *madurez del protocolo*, *ventaja colectiva*, *reutilización* o *cobertura* son **proxies educativos** diseñados para experimentar con relaciones causales y arquitectura de sistemas.

## Modelo de grafos para leer las tres simulaciones

Podemos representar el sistema como un grafo dirigido dinámico: **`G_t = (V_t, E_t)`**.

- **`V_t`**: agentes, servicios, repositorios, identidades, workloads, clústeres o recursos disponibles.
- **`E_t`**: capacidades de leer, escribir, descubrir, autenticar, reenviar, reutilizar o ejecutar.
- **Camino**: secuencia de aristas que permite llegar de un nodo inicial a otro, aun cuando no exista una conexión directa.
- **Dinámica**: la topología cambia cuando aparece memoria persistente, una nueva credencial, una convención de comunicación o un nuevo permiso.

La idea más importante es que **el riesgo y la capacidad son propiedades del sistema**, no solamente de sus componentes tomados por separado.

## Preguntas de trabajo

1. **Topología:** ¿qué nueva arista cambia más el comportamiento global en cada simulación?
2. **Persistencia:** ¿qué sucede si los mensajes existen pero desaparecen antes de que otros agentes puedan descubrirlos?
3. **Coordinación:** ¿cuándo un repositorio de rastros pasa a funcionar como protocolo?
4. **Emergencia:** ¿por qué una población con los mismos agentes individuales puede mostrar una capacidad agregada diferente?
5. **Seguridad:** ¿qué arista convendría eliminar o limitar para romper un camino sin inutilizar todo el sistema?
6. **Defensa:** ¿qué controles deben ser independientes para que la falla de uno no abra por sí sola un camino completo?

## Base documental

<div class="source-grid">
  <a class="source-card-link" href="https://openai.com/index/hugging-face-incident-and-the-road-ahead/" target="_blank" rel="noopener">
    <strong>OpenAI — The Hugging Face incident and the road ahead</strong>
    <span>Contexto, cronología y explicación pública del incidente · 26 de agosto de 2026.</span>
  </a>
  <a class="source-card-link" href="https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf" target="_blank" rel="noopener">
    <strong>OpenAI–Hugging Face Incident Technical Report</strong>
    <span>Informe técnico original de 38 páginas utilizado como base documental principal.</span>
  </a>
</div>

[Ver mapa detallado de fuentes y conceptos →](references.md){ .md-button }

---

**Material docente:** Prof. Sergio Gevatschnaider · Big Data · Grafos · Algoritmos Evolutivos · Autómatas Celulares
