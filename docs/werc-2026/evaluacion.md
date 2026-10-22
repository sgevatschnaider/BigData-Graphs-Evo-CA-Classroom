# Glosario, problemas y autoevaluación

[Resolver 16 preguntas con corrección inmediata](../assets/werc-2026/cuestionario.html){ .md-button .md-button--primary }

Cada pregunta explica la opción correcta. Se recomienda estudiar primero [los desarrollos matemáticos](modelo/) y utilizar los [ocho experimentos](../assets/werc-2026/werc-laboratorio.html).

## Glosario técnico

| Concepto | Definición precisa en esta unidad |
| --- | --- |
| **Reina Roja** | Metáfora evolutiva que motiva la posibilidad de progresar sin cambiar la posición relativa; no es por sí sola un teorema económico. |
| **Capacidad qᵢ** | Estado tecnológico de un laboratorio; evoluciona según una función ilustrativa de esfuerzo e incertidumbre. |
| **Esfuerzo xᵢ** | Variable de decisión de inversión tecnológica no negativa. |
| **β** | Sensibilidad del softmax de cuotas a diferencias de capacidades. |
| **σᵢ** | Participación relativa producida por un softmax bajo hipótesis de mercado. |
| **Wᶜ** | Matriz de influencia competitiva entre laboratorios. En el juego reducido entra como externalidad estratégica especificada. |
| **B** | Matriz de requerimientos de recursos por unidad de inversión. |
| **H** | Matriz conceptual de supervisión; falta derivar desde ella una probabilidad estatal de detección. |
| **F** | Red financiera propuesta para un programa empírico futuro, no calibrada en WERC. |
| **η** | En el caso homogéneo, η = α/b es la intensidad relativa de la interacción. |
| **ρ(W)** | Radio espectral, máximo módulo de autovalores; condiciona la convergencia de la resolvente. |
| **Serie de Neumann** | Expansión de una matriz inversa como suma de potencias cuando su radio espectral es menor que uno. |
| **Paseo** | Secuencia de aristas que permite repeticiones, a diferencia de caminos simples. |
| **Centralidad de Katz–Bonacich** | Suma ponderada de paseos con atenuación, vinculada a la estructura del equilibrio lineal-cuadrático. |
| **Mejor respuesta** | Inversión que maximiza el pago propio dadas las inversiones de otros agentes. |
| **Equilibrio de Nash** | Perfil de acciones donde ningún jugador mejora su pago desviándose unilateralmente. |
| **Equilibrio interior** | Solución con esfuerzos estrictamente positivos, distinta de un posible equilibrio con jugadores inactivos. |
| **Restricción vinculante** | Se usa la totalidad del recurso disponible; no queda holgura. |
| **Precio sombra μ** | Multiplicador no negativo asociado a un recurso; mide valor marginal de escasez bajo los supuestos. |
| **Complementariedad** | Condición de holgura y precio sombra cuyo producto es cero. |
| **G** | Ganancia inmediata al desviarse de un acuerdo de coordinación. |
| **d** | Probabilidad contemporánea de detectar una desviación. |
| **Pₛ** | Sanción aplicada si la desviación es detectada. |
| **δ** | Factor de descuento intertemporal del juego repetido. |
| **ΔU** | Diferencia entre pago por cooperación y pago bajo castigo. |
| **ER** | Generador Erdős–Rényi de grafos aleatorios, aquí ajustado a número fijo de enlaces. |
| **WS** | Familia Watts–Strogatz de mundo pequeño y reconexión de aristas. |
| **BA** | Familia Barabási–Albert de conexión preferencial y heterogeneidad de grados. |
| **SBM** | Modelo de bloques estocásticos usado para estudiar comunidades. |
| **Red multicapa** | Sistema con tipos distintos de relaciones que requieren definiciones económicas explícitas. |
| **Evaluador congelado** | En RQGM, criterio de evaluación mantenido fijo durante una época. |
| **Ancla de ground truth** | Conjunto independiente de referencia utilizado en el RQGM para contrastar evaluadores. |
| **Borrado selectivo** | Invalidación de evidencia de utilidad dependiente de un evaluador sustituido. |
| **Fuga de información** | Utilizar al entrenar o seleccionar modelos datos reservados para evaluar generalización. |

## Problemas resueltos

### Ejercicio A · Estrella y camino

Usar α=0.2, bᵢ=vᵢ=1. Para estrella K₁,₃ y camino P₄ resolver el sistema:

\[
(I-\eta W)x=\mathbf 1.
\]

**Resultado comprobable:** estrella = (20/11, 15/11, 15/11, 15/11); camino = (25/19, 30/19, 30/19, 25/19). Total de la estrella 65/11; del camino 110/19.

[Modificar η en el laboratorio](../assets/werc-2026/werc-laboratorio.html#lab-03).

### Ejercicio B · Precio sombra

Con estrella, η=.2 y K=4, determinar z, Z, μ y esfuerzo asignado.

**Solución:** \(Z=65/11\), \(\mu=1-\frac4{65/11}=21/65\), \(x=(16/13,12/13,12/13,12/13)\). La suma es 4.

[Verificar con un slider](../assets/werc-2026/werc-laboratorio.html#lab-05).

### Ejercicio C · Umbral de coordinación

Con \(G=.8\), \(d=.5\), \(P_s=.25\), \(\Delta U=.6\), calcular el descuento mínimo que hace no rentable la desviación.

\[
\delta^*=\frac{G-dP_s}{G-dP_s+d\Delta U}=\frac{.675}{.975}=\frac9{13}\approx.6923.
\]

No significa que exista un acuerdo real con ese nivel de paciencia.

### Ejercicio D · Diferenciar resultados del programa

Indicá cuáles de estas proposiciones son **resultados** y cuáles siguen como **hipótesis**: invariancia softmax; ecuación que agrega H a una detección estatal; equilibrio completo laboratorios-países; comparaciones sintéticas de cuatro familias; identificación bursátil causal.

**Respuesta:** identidad softmax es teorema condicional; comparación de 480 redes son estadísticas de experimento sintético reportado; agregación H→Estado, equilibrio general y causalidad bursátil siguen pendientes.

## Reflexión final

¿Qué se puede afirmar de una red cuando cambian nodos, preferencias, normas y evaluadores con el tiempo? Compará la pregunta económica de WERC con la pregunta computacional de [Red Queen Gödel Machine](coevolucion/) sin mezclar sus afirmaciones.
