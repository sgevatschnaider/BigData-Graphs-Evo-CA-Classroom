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
| 01 | Construcción emergente de un protocolo multiagente | [![Abrir ES](https://img.shields.io/badge/Abrir-ES-0969da?style=for-the-badge)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/01-emergent-protocol-es.html) | [![Open EN](https://img.shields.io/badge/Open-EN-1f6feb?style=for-the-badge)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/01-emergent-protocol-en.html) |
| 02 | Emergencia de capacidad colectiva | [![Abrir ES](https://img.shields.io/badge/Abrir-ES-0969da?style=for-the-badge)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/02-collective-capability-es.html) | [![Open EN](https://img.shields.io/badge/Open-EN-1f6feb?style=for-the-badge)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/02-collective-capability-en.html) |
| 03 | Seguridad de agentes de IA — caminos de ataque | [![Abrir ES](https://img.shields.io/badge/Abrir-ES-0969da?style=for-the-badge)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/03-attack-path-es.html) | [![Open EN](https://img.shields.io/badge/Open-EN-1f6feb?style=for-the-badge)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/assets/ai-agents/03-attack-path-en.html) |

## Unidad docente

[![Portada ES](https://img.shields.io/badge/Portada-ES-0969da?style=for-the-badge)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/ai-agents/)
[![Module EN](https://img.shields.io/badge/Module-EN-1f6feb?style=for-the-badge)](https://sgevatschnaider.github.io/BigData-Graphs-Evo-CA-Classroom/ai-agents/index.en/)
[![Fuentes](https://img.shields.io/badge/Fuentes-Trazabilidad-57606a?style=for-the-badge)](../../../../docs/ai-agents/references.md)

## Base documental

Las simulaciones se inspiran en el **OpenAI–Hugging Face Incident Technical Report (2026)**. Los mecanismos documentados y las métricas pedagógicas se distinguen explícitamente en la unidad docente: los indicadores simulados no deben interpretarse como mediciones históricas del incidente.

> Material elaborado por el profesor **Sergio Gevatschnaider** para el estudio de teoría de grafos, sistemas complejos, sistemas multiagente y seguridad.
