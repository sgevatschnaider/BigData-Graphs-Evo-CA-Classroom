# 🤖 Graphs, Complex Systems & AI Agents

<div class="ai-hero">
  <div>
    <div class="ai-kicker">GRAPH THEORY · MULTI-AGENT SYSTEMS · EMERGENCE · SECURITY</div>
    <h2>From local traces to protocol, from protocol to collective capability, and from capability to systemic risk</h2>
    <p>An interactive unit grounded in the 2026 OpenAI–Hugging Face case. It studies how shared infrastructure can become external memory, how coordination conventions can emerge between agents, and how new edges change reachability in a security graph.</p>
    <div class="ai-actions">
      <a class="md-button md-button--primary" href="../assets/ai-agents/01-emergent-protocol-en.html">▶ Start learning path</a>
      <a class="md-button" href="../">🌐 Español</a>
      <a class="md-button" href="https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf" target="_blank" rel="noopener">↗ Original technical report</a>
    </div>
  </div>
</div>

!!! abstract "Core idea"
    In security and complex systems, **isolated nodes are not enough**. What matters may be the emergence of new edges, persistent memory, and composed paths. The unit follows a deliberate progression: **emergent communication → coordination → reuse → collective capability → attack paths**.

## Why does this belong in Graph Theory?

Graph theory provides the common language. An agent, service, credential, or workload can be represented as a node; a capability to read, write, authenticate, relay, or execute can be represented as an edge. We then study **reachability, paths, topological change, information propagation, and emergent system properties**.

<div class="concept-flow" role="list" aria-label="Conceptual sequence">
  <span role="listitem">Persistent trace</span><b>→</b>
  <span role="listitem">External memory</span><b>→</b>
  <span role="listitem">Communication</span><b>→</b>
  <span role="listitem">Protocol</span><b>→</b>
  <span role="listitem">Reuse</span><b>→</b>
  <span role="listitem">Collective capability</span><b>→</b>
  <span role="listitem">Systemic risk</span>
</div>

## Recommended path

<div class="sim-grid">
  <article class="sim-card">
    <div class="sim-number">01</div><div class="sim-tag">DYNAMICS ON GRAPHS</div>
    <h3>Emergent Multi-Agent Protocol Construction</h3>
    <p>Observe how initially isolated agents reuse a shared medium as external memory, discover traces of other agents, and stabilize increasingly structured conventions.</p>
    <div class="lang-row"><a class="md-button md-button--primary" href="../assets/ai-agents/01-emergent-protocol-en.html">🇬🇧 English</a><a class="md-button" href="../assets/ai-agents/01-emergent-protocol-es.html">🇪🇸 Español</a></div>
  </article>
  <article class="sim-card">
    <div class="sim-number">02</div><div class="sim-tag">COMPLEX SYSTEMS</div>
    <h3>Collective Capability Emergence</h3>
    <p>Compare two identical populations: isolated agents versus agents with shared memory and a protocol. Change overlap, persistence, latency, and reliability.</p>
    <div class="lang-row"><a class="md-button md-button--primary" href="../assets/ai-agents/02-collective-capability-en.html">🇬🇧 English</a><a class="md-button" href="../assets/ai-agents/02-collective-capability-es.html">🇪🇸 Español</a></div>
  </article>
  <article class="sim-card">
    <div class="sim-number">03</div><div class="sim-tag">SECURITY GRAPHS</div>
    <h3>AI Agent Security — Attack Paths</h3>
    <p>Reconstruct conceptually how allowed services, indirect egress, credentials, and vulnerabilities can chain into a path even when no direct edge exists.</p>
    <div class="lang-row"><a class="md-button md-button--primary" href="../assets/ai-agents/03-attack-path-en.html">🇬🇧 English</a><a class="md-button" href="../assets/ai-agents/03-attack-path-es.html">🇪🇸 Español</a></div>
  </article>
</div>

## Source → model → classroom

| Layer | Case-grounded element | Classroom abstraction |
|---|---|---|
| **Communication** | Artifactory was unexpectedly reused as persistent inter-run communication. | Model the transition from isolated traces to a communication network. |
| **Protocol** | Directory names were reused and communication became more structured. | Vary discoverability, persistence, friction, and convention formation. |
| **Capability** | Agents could share findings and continue from previous results. | Compare isolated agents with a population that can preserve and reuse knowledge. |
| **Security** | Services, credentials, vulnerabilities, and permissions chained into access paths. | Treat resources as nodes and access capabilities as edges to study reachability. |

!!! warning "Documented facts vs. pedagogical metrics"
    The simulations are **not probabilistic reproductions of the incident**. Dates, general mechanisms, and selected milestones are source-grounded; metrics such as *coordination density*, *protocol maturity*, *collective advantage*, *reuse*, and *coverage* are **educational proxies**.

## Graph model

We represent the system as a dynamic directed graph: **`G_t = (V_t, E_t)`**.

- **`V_t`**: agents, services, repositories, identities, workloads, clusters, or resources.
- **`E_t`**: capabilities to read, write, discover, authenticate, relay, reuse, or execute.
- **Path**: a sequence of edges that creates reachability without requiring a direct connection.
- **Dynamics**: topology changes when persistent memory, a credential, a communication convention, or a permission appears.

The key lesson is that **capability and risk can be properties of the system rather than of isolated components**.

## Primary sources

<div class="source-grid">
  <a class="source-card-link" href="https://openai.com/index/hugging-face-incident-and-the-road-ahead/" target="_blank" rel="noopener"><strong>OpenAI — The Hugging Face incident and the road ahead</strong><span>Public context and interactive timeline · August 26, 2026.</span></a>
  <a class="source-card-link" href="https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf" target="_blank" rel="noopener"><strong>OpenAI–Hugging Face Incident Technical Report</strong><span>Original 38-page technical report used as the principal documentary basis.</span></a>
</div>

[Detailed source and concept map →](references.md){ .md-button }

---

**Teaching material:** Prof. Sergio Gevatschnaider · Big Data · Graphs · Evolutionary Algorithms · Cellular Automata
