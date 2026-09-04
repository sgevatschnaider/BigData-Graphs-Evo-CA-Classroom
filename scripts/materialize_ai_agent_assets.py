#!/usr/bin/env python3
"""Materialize and verify the bilingual AI-agent HTML simulations for MkDocs."""

from __future__ import annotations

import gzip
import hashlib
import lzma
from pathlib import Path

SRC = Path("assets-src/ai-agents")
DST = Path("docs/assets/ai-agents")

EXPECTED = {
    "01-emergent-protocol-en.html": "d77a7f677e12f5d43d7c306088274a4d3c8eecdd8da3fe15bbf2b0227db522c7",
    "01-emergent-protocol-es.html": "b72b65a4d1628a9b7f22708778b3ca1594547cbcd8d3a234cecf82532bb9a6fe",
    "02-collective-capability-en.html": "3736b17c679a5b457ec513ffef932f7cba98e8a2fdbf5825a2c26b3a3f056aed",
    "02-collective-capability-es.html": "911ad60882cdff95a4a4db6f782701c2e7a5e6ba712b98b3265ec8ebe2c39881",
    "03-attack-path-en.html": "fc8cae5fdf41968ebc9c9aff12a4de3c9abce3755e4fb7d6d8de7c1c55e6e176",
    "03-attack-path-es.html": "702cde22e8ff48dd268415e69efce370120e099eb4df2ef46f79d5f502f982ff",
}


def materialize(source: Path, target: Path) -> None:
    raw = source.read_bytes()
    if source.suffix == ".gz":
        data = gzip.decompress(raw)
    elif source.suffix == ".xz":
        data = lzma.decompress(raw)
    else:
        raise ValueError(f"Unsupported source format: {source}")
    target.write_bytes(data)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)

    sources = {
        "01-emergent-protocol-en.html": SRC / "01-emergent-protocol-en.html.gz",
        "01-emergent-protocol-es.html": SRC / "01-emergent-protocol-es.html.gz",
        "02-collective-capability-en.html": SRC / "02-collective-capability-en.html.gz",
        "02-collective-capability-es.html": SRC / "02-collective-capability-es.html.gz",
        "03-attack-path-en.html": SRC / "03-attack-path-en.html.gz",
        "03-attack-path-es.html": SRC / "03-attack-path-es.html.xz",
    }

    for name, source in sources.items():
        if not source.is_file():
            raise SystemExit(f"Missing simulation source: {source}")
        target = DST / name
        materialize(source, target)
        digest = sha256(target)
        if digest != EXPECTED[name]:
            raise SystemExit(
                f"Integrity check failed for {name}: expected {EXPECTED[name]}, got {digest}"
            )
        print(f"OK  {name}  {digest[:12]}")

    print(f"Materialized and verified {len(sources)} bilingual simulation assets in {DST}")


if __name__ == "__main__":
    main()
