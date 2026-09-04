# AI Agents · Complex Networks · Emergent Coordination · Security

Nueva unidad del módulo de **Teoría de Grafos y Sistemas Complejos** dedicada a estudiar sistemas multiagente mediante grafos dinámicos, memoria compartida, coordinación emergente y caminos de ataque.

## Recorrido conceptual

```text
rastro persistente
      ↓
memoria externa
      ↓
comunicación emergente
      ↓
protocolo compartido
      ↓
reutilización de conocimiento
      ↓
capacidad colectiva
      ↓
riesgo sistémico / attack paths
```

La unidad usa un grafo dirigido dinámico `G_t = (V_t, E_t)` como lenguaje común:

- `V_t`: agentes, servicios, identidades, workloads, repositorios, clústeres y otros recursos;
- `E_t`: capacidades de leer, escribir, descubrir, autenticar, reenviar, reutilizar o ejecutar;
- **camino**: secuencia de aristas que vuelve alcanzable un recurso aunque no exista una conexión directa;
- **dinámica**: la topología cambia cuando aparecen memoria persistente, protocolos, credenciales o nuevos permisos.

## Laboratorios interactivos

| # | Laboratorio | Español | English |
|---|---|---|---|
| 01 | Construcción emergente de un protocolo multiagente | [Abrir](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/01-emergent-protocol-es.html) | [Open](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/01-emergent-protocol-en.html) |
| 02 | Emergencia de capacidad colectiva | [Abrir](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/02-collective-capability-es.html) | [Open](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/02-collective-capability-en.html) |
| 03 | Seguridad de agentes de IA — caminos de ataque | [Abrir](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/03-attack-path-es.html) | [Open](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/03-attack-path-en.html) |

## Unidad docente

- [Portada del módulo — Español](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/ai-agents/)
- [Module landing page — English](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/ai-agents/index.en/)
- [Fuentes y trazabilidad](../../../../docs/ai-agents/references.md)

## Base documental

Las simulaciones se inspiran en el **OpenAI–Hugging Face Incident Technical Report (2026)**. Los mecanismos documentados y las métricas pedagógicas se distinguen explícitamente en la unidad docente: los indicadores simulados no deben interpretarse como mediciones históricas del incidente.

> Material elaborado por el profesor **Sergio Gevatschnaider** para el estudio de teoría de grafos, sistemas complejos, sistemas multiagente y seguridad.
