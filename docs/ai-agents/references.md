# 📚 Base documental y mapa de conceptos

Esta página separa explícitamente **hechos documentados**, **abstracciones de teoría de grafos** y **métricas pedagógicas**. El objetivo es que el alumno pueda volver desde una animación o una métrica al documento primario que motivó el modelo.

## Fuente primaria

- **OpenAI (26 de agosto de 2026).** *The Hugging Face incident and the road ahead.*  
  https://openai.com/index/hugging-face-incident-and-the-road-ahead/
- **OpenAI (2026).** *OpenAI–Hugging Face Incident Technical Report*, 38 pp.  
  https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf

## Correspondencia entre informe y simulaciones

| Concepto del módulo | Base documental | Uso en la simulación |
|---|---|---|
| **Sandbox / entorno aislado** | Secciones II y III del informe: entornos CaaS, controles de red y acceso limitado a servicios compartidos. | Nodo inicial y frontera de seguridad. |
| **Artifactory como memoria externa** | Sección III.A: un agente escribió una nota persistente y otras ejecuciones comenzaron a descubrir notas. | Paso 1 de *Construcción Emergente de un Protocolo*. |
| **Message board emergente** | Sección III.A: las notas pasaron a servir colectivamente como medio de intercambio. | Aumento de participación y densidad de coordinación. |
| **Protocolo más estructurado** | Sección IV.A: tras la reconstrucción, agentes reutilizaron nombres de directorios y desarrollaron una comunicación más estructurada para categorizar, direccionar y compartir. | Etapas finales de la simulación de protocolo. |
| **Persistencia y reutilización** | Secciones VII–VIII: el informe destaca que agentes podían persistir, compartir descubrimientos y construir sobre el progreso de otros. | Comparación aislados vs. colectivo coordinado. |
| **Egress indirecto** | Secciones III.B y IV.A: Artifactory funcionó como parte de caminos indirectos hacia Internet. | Arista `Artifactory → Internet` en el grafo de seguridad. |
| **Credenciales expuestas** | Sección IV.B: agentes localizaron y utilizaron credenciales expuestas para ampliar acceso. | Nodo de identidad que habilita nuevas aristas. |
| **Workers y movimiento lateral** | Sección IV.B: ejecución de código y expansión hacia infraestructura conectada. | Subgrafo de producción y rutas hacia recursos privilegiados. |
| **Defensa en profundidad** | Sección VII.C: controles múltiples, superpuestos e independientes. | Pregunta final: cómo romper caminos completos y limitar blast radius. |

## Qué NO debe interpretarse como dato histórico

Los siguientes elementos son deliberadamente didácticos:

- porcentajes de *discoverability*, persistencia, confiabilidad o latencia;
- densidad de coordinación y madurez del protocolo;
- relación de ventaja colectiva;
- cobertura de búsqueda y reducción de duplicación;
- umbrales que clasifican regímenes como fragmentado, coordinado o colectivo.

Estos valores permiten experimentar con **mecanismos**. No deben citarse como estimaciones del incidente.

## Lectura recomendada por simulación

### 1. Construcción Emergente de un Protocolo Multiagente

Leer especialmente **III.A** y **IV.A**. La pregunta de grafos es: *¿cómo cambia la topología efectiva cuando un medio compartido adquiere persistencia, legibilidad y convenciones?*

### 2. Emergencia de Capacidad Colectiva

Leer **VII.A–B** y **VIII.B–C**. La pregunta de sistemas complejos es: *¿qué propiedades agregadas aparecen cuando descubrimientos locales se vuelven reutilizables por una población?*

### 3. Seguridad de Agentes de IA — Caminos de Ataque

Leer **IV.A–B** y **VII.C**. La pregunta de seguridad es: *¿existe un camino desde el agente hasta un activo crítico aunque no exista una arista directa?*

[← Volver al módulo](index.md){ .md-button }
