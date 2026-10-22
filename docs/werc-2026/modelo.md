# El modelo WERC 2026, paso por paso

Esta guía estudia los **submodelos delimitados** del manuscrito aportado por el autor. Las hipótesis son parte de cada proposición; se evita generalizarlas al equilibrio completo entre países y laboratorios.

## 1. Arquitectura multinivel

Sean \(n\) laboratorios, \(m\) recursos y \(r\) supervisores. Las matrices \(W^C\in\mathbb{R}_+^{n\times n}\), \(B\in\mathbb{R}_+^{n\times m}\) y \(H\in\mathbb{R}_+^{r\times n}\) tienen unidades diferentes. \(W^C\) modela influencias competitivas; \(B\), uso físico de recursos; y \(H\), cobertura institucional. La eventual red \(F\) es una ampliación no calibrada.

## 2. Capacidad tecnológica y Reina Roja

La capacidad tecnológica satisface, en una especificación ilustrativa:

\[
q_{i,t+1}=q_{it}+\phi_i\log(1+x_{it})+\varepsilon_{it},\qquad x_{it}\geq0,\ \phi_i>0.
\]

\(x_{it}\) es esfuerzo de innovación; \(\phi_i\) traduce esfuerzo en capacidad con rendimientos decrecientes; \(\varepsilon_{it}\) resume perturbaciones. La forma logarítmica es un **supuesto**, no una regresión calibrada.

La participación relativa en un mismo mercado se define por

\[
\sigma_i(q)=\frac{\exp(\beta q_i)}{\sum_{j=1}^n\exp(\beta q_j)},\qquad\beta>0.
\]

**Proposición 1.** Si todos los participantes obtienen el mismo desplazamiento \(g\), manteniendo fijo \(\beta\) y el universo de firmas:

\[
\sigma_i(q+g\mathbf 1)=\frac{e^{\beta g}e^{\beta q_i}}{e^{\beta g}\sum_j e^{\beta q_j}}=\sigma_i(q).
\]

Ejemplo: 80/80 pasa a 90/90; cada firma permanece en 50 %. Si solo A pasa a 90 con \(\beta=0.1\), su cuota es \(\frac{e^9}{e^9+e^8}\approx73.1\%\).

En tiempo continuo y \(\beta\) fijo:

\[
\frac{d}{dt}\log\sigma_i=\beta\left(\dot q_i-\sum_j\sigma_j\dot q_j\right).
\]

**Precaución:** que las cuotas se mantengan no demuestra pérdida social. La innovación puede beneficiar a usuarios aun sin cambiar las participaciones.

## 3. Softmax y signo de la interacción

En el submodelo multimercado, la derivada cruzada de los ingresos simplificados cumple:

\[
\frac{\partial^2 R_i}{\partial x_i\partial x_j}
=V\beta^2q'_iq'_j\sigma_i\sigma_j(2\sigma_i-1).
\]

Su signo depende de si \(\sigma_i\) supera o no \(1/2\). Por tanto, **complementariedad positiva global** no se deduce del softmax: es un supuesto independiente del siguiente juego reducido.

## 4. Juego estático y mejores respuestas

\[
u_i(x)=v_ix_i-\frac{b_i}{2}x_i^2+\alpha x_i\sum_{j=1}^n w^C_{ij}x_j,
\quad b_i>0,\quad \alpha\geq0.
\]

El incentivo \(v_i=a_i-\tau_i-\sum_k B_{ik}(p_k^0+\mu_k)\) representa rentabilidad base menos gravámenes y costos de recursos.

La condición de primer orden produce

\[
\frac{\partial u_i}{\partial x_i}=v_i-b_ix_i+\alpha\sum_jw_{ij}^Cx_j=0.
\]

Como \(\frac{\partial^2u_i}{\partial x_i^2}=-b_i<0\), la mejor respuesta con no negatividad es

\[
BR_i(x_{-i})=\max\left\{0,\frac{v_i+\alpha\sum_jw^C_{ij}x_j}{b_i}\right\}.
\]

No se debe aplicar una fórmula de solución interior a casos de esquina sin verificar todas las condiciones de complementariedad.

## 5. Equilibrio interior y propagación

**Proposición 2.** Suponiendo \(W^C\geq0\), \(b_i>0\), \(v_i>0\), \(\alpha\geq0\) y

\[
\rho(\alpha D_b^{-1}W^C)<1
\]

existe un único equilibrio interior:

\[
x^*=(D_b-\alpha W^C)^{-1}v.
\]

La serie de Neumann converge bajo la condición espectral. Con \(D_b=bI\), \(\eta=\alpha/b\):

\[
x^*=\frac1b(I-\eta W^C)^{-1}v
=\frac1b\sum_{k=0}^{\infty}\eta^k(W^C)^kv.
\]

Las potencias de \(W^C\) cuentan **paseos**, no solamente caminos simples; con incentivos uniformes aparece la estructura de centralidad Katz–Bonacich.

### Ejemplo exacto: estrella versus camino

Con cuatro agentes, tres aristas, \(a_i=b_i=1\), \(\alpha=0.2\), \(v=\mathbf1\):

| Estructura | Equilibrio exacto | Esfuerzo total |
| --- | --- | --- |
| Estrella \(K_{1,3}\) | \((20/11,15/11,15/11,15/11)\) | \(65/11\approx5.909\) |
| Camino \(P_4\) | \((25/19,30/19,30/19,25/19)\) | \(110/19\approx5.789\) |

Es una comparación específica, no una jerarquía universal. Comprobá el resultado en [Laboratorio 03](../assets/werc-2026/werc-laboratorio.html#lab-03).

## 6. Recursos y precio sombra

Para recursos \(B\), capacidades \(K\) y multiplicadores \(\mu\):

\[
B^\top x\leq K,\qquad \mu_k(K_k-(B^\top x)_k)=0,\quad\mu_k\geq0.
\]

**Proposición 3 (un recurso homogéneo).** Con \(a_i=b_i=1\), \(B=\mathbf1\), \(z=(I-\eta W^C)^{-1}\mathbf1\) y \(Z=\mathbf1^\top z\), si \(0<K<Z\) y la restricción es vinculante:

\[
\boxed{\mu=1-\frac{K}{Z},\qquad x^*=\frac{K}{Z}z,\qquad\mathbf1^\top x^*=K.}
\]

Para estrella, \(K=4\): \(\mu=21/65\), esfuerzos \((16/13,12/13,12/13,12/13)\). Si \(K\geq Z\), \(\mu=0\) y el esfuerzo total es \(Z\), no necesariamente \(K\). Extender a varios recursos heterogéneos requiere resolver un problema diferente.

## 7. Riesgo ilustrativo y juego repetido

La función de riesgo propuesta como mecanismo conceptual es

\[
P(x,s)=1-\exp[-h(x,s)],\quad
h(x,s)=\sum_i\lambda_ix_i^\nu e^{-\gamma_i s_i}.
\]

Los signos de las derivadas se derivan de la forma funcional, **no** de una estimación empírica de riesgo tecnológico.

Con ganancia de desvío \(G=U^D-U^C\), detección \(d\), sanción \(P_s\), descuento \(\delta\) y pérdida futura \(\Delta U=U^C-U^N\), bajo castigo creíble:

\[
\boxed{G\leq dP_s+\frac{\delta d}{1-\delta}\Delta U.}
\]

Si \(G>dP_s\) y \(\Delta U>0\):

\[
\delta^*=\frac{G-dP_s}{G-dP_s+d\Delta U}.
\]

Con \(G=0.8\), \(d=0.5\), \(P_s=0.25\), \(\Delta U=0.6\): \(\delta^*=9/13\approx0.6923\). Esta condición **no** estima la relación entre China y Estados Unidos ni demuestra la agregación de H al monitoreo estatal.

## 8. Cómo leer los resultados computacionales

En la ponencia se reporta un diseño de 480 redes sintéticas: 120 realizaciones por familia, \(n=24\), \(m=48\), \(a_i=b_i=1\), \(\eta=0.12\).

| Familia | Radio espectral medio | Inversión total media ± DE | Precio sombra medio |
| --- | ---: | ---: | ---: |
| Erdős–Rényi | 4.817 | 50.998 ± 1.553 | 0.275 |
| Watts–Strogatz | 4.148 | 46.743 ± 0.242 | 0.210 |
| Barabási–Albert | 5.214 | 55.692 ± 3.372 | 0.335 |
| Modelo de bloques | 4.815 | 50.214 ± 1.504 | 0.264 |

Son **estadísticas consolidadas reportadas**, no generadas nuevamente a partir del código original en esta unidad. La especificación de generación ER/WS/BA/SBM y el ajuste posterior a 48 aristas importa para replicar los resultados.

## 9. Limitaciones expresas

- El equilibrio global entre Estados, laboratorios y proveedores **no está resuelto**.
- Las probabilidades estatales \(d_s(H)\) no se derivan de la matriz H en el manuscrito.
- El bloque financiero F y los efectos bursátiles son propuestas para investigación empírica.
- Para defender una política de desaceleración por bienestar debe añadirse una función social explícita.
- La coevolución tipo RQGM es una lectura complementaria, no una calibración del juego de inversión.

**Fuente primaria:** manuscrito «Coordinación y competencia en la frontera de inteligencia artificial: un modelo de redes multinivel», entregado por el autor, páginas 2–12, WERC 2026.

[Explorar el juego en vivo →](../assets/werc-2026/werc-laboratorio.html#lab-03){ .md-button .md-button--primary }
