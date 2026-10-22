"""Research-classroom calculations inspired by Gevatschnaider (WERC 2026).

All networks generated here are SYNTHETIC. This is not a reconstruction of
the 480 reported graphs; an exact replication needs the original CSV/code.
"""
from __future__ import annotations
import numpy as np


def softmax(q, beta=0.1):
    """Stable softmax of technology capabilities; beta must be positive."""
    q = np.asarray(q, dtype=float)
    if q.ndim != 1 or not len(q) or not np.all(np.isfinite(q)) or beta <= 0:
        raise ValueError("q must be a nonempty finite vector, beta > 0")
    z = beta * q
    e = np.exp(z - z.max())
    return e / e.sum()


def nash_equilibrium(w, alpha=0.12, b=1.0, v=None):
    """Interior equilibrium x* = (diag(b)-alpha W)^(-1) v.

    Requires nonnegative W with no self-loops, alpha >= 0, b_i > 0,
    v_i > 0 and rho(alpha diag(b)^(-1) W) < 1.
    """
    w = np.asarray(w, dtype=float)
    n = len(w)
    b = np.broadcast_to(np.asarray(b, dtype=float), (n,))
    v = np.ones(n) if v is None else np.broadcast_to(np.asarray(v, dtype=float), (n,))
    if w.shape != (n,n) or n == 0 or np.any(w < 0) or np.any(np.diag(w) != 0):
        raise ValueError("W must be nonnegative square with zero diagonal")
    if alpha < 0 or np.any(b <= 0) or np.any(v <= 0) or not (
        np.all(np.isfinite(w)) and np.all(np.isfinite(b)) and np.all(np.isfinite(v))
    ):
        raise ValueError("Parameters must satisfy model hypotheses")
    rho = max(abs(np.linalg.eigvals(alpha * w / b[:, None])))
    if rho >= 1 - 1e-10:
        raise ValueError(f"Spectral stability condition fails (rho={rho:.6f})")
    x = np.linalg.solve(np.diag(b) - alpha * w, v)
    if np.any(x <= 0):
        raise ValueError("Not an interior equilibrium")
    return x, float(rho)


def resource_equilibrium(w, capacity, eta=0.12):
    """Homogeneous single input with 0<K<Z, or slack when K>=Z.

    Matches Proposition 3 in the supplied WERC 2026 paper. Not valid for
    heterogeneous resources or arbitrary network games.
    """
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    z, rho = nash_equilibrium(w, alpha=eta)
    Z = z.sum()
    if capacity >= Z:
        return z, 0.0, False
    mu = 1.0 - capacity / Z
    return capacity / Z * z, float(mu), True


def cooperation_margin(G, d, sanction, delta, future_loss):
    """Positive margin means the one-period deviation is not profitable.

    G <= d*sanction + delta*d/(1-delta)*future_loss; credible punishment
    is an assumption; not estimated from supervisory network H.
    """
    if min(G, sanction, future_loss) < 0 or not 0 <= d <= 1 or not 0 < delta < 1:
        raise ValueError("Parameters outside defined domain")
    return d * sanction + delta * d * future_loss / (1 - delta) - G


def make_network(family, n=24, m=48, seed=20261020):
    """Simple reproducible undirected synthetic topologies with fixed n,m.

    WS and BA may be adjusted to exactly m edges; this can alter their
    characteristic distributions. No claim of reproducing the WERC CSV.
    """
    if n < 8 or not 0 <= m <= n*(n-1)//2:
        raise ValueError("Unsupported network size")
    rng = np.random.default_rng(seed)
    edges = set()
    def add(i,j):
        if i != j: edges.add(tuple(sorted((int(i),int(j)))))
    if family == "ER":
        all_pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        edges={all_pairs[k] for k in rng.choice(len(all_pairs),size=m,replace=False)}
    elif family == "WS":
        # Degree-4 ring; rewire some edges, preserving edge count.
        for i in range(n):
            for step in (1,2):add(i,(i+step)%n)
        for i in range(n):
            for step in (1,2):
                j=(i+step)%n
                old=tuple(sorted((i,j)))
                if old in edges and rng.random()<0.12:
                    forbidden={i}|{v if u==i else u for u,v in edges if u==i or v==i}
                    available=[k for k in range(n) if k not in forbidden]
                    if available:
                        edges.remove(old);add(i,rng.choice(available))
    elif family == "BA":
        for i,j in [(0,1),(0,2),(1,2)]:add(i,j)
        deg=np.zeros(n,float);deg[:3]=2
        for i in range(3,n):
            p=(deg[:i]+.00001)/(deg[:i]+.00001).sum()
            new=rng.choice(i,size=2,replace=False,p=p)
            for j in new:add(i,j);deg[i]+=1;deg[j]+=1
    elif family == "SBM":
        for i in range(n):
            for j in range(i+1,n):
                p=.31 if (i<n//2)==(j<n//2) else .018
                if rng.random()<p:add(i,j)
    else:
        raise ValueError("family must be ER, WS, BA or SBM")
    # Exact-edge adjustment is part of this *new* teaching generator.
    all_pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    while len(edges)>m:
        edges.remove(tuple(sorted(list(edges)))[int(rng.integers(len(edges)))])
    if len(edges)<m:
        missing=[e for e in all_pairs if e not in edges]
        for k in rng.choice(len(missing),size=m-len(edges),replace=False):
            edges.add(missing[int(k)])
    W=np.zeros((n,n),dtype=float)
    for i,j in edges:W[i,j]=W[j,i]=1.
    return W
