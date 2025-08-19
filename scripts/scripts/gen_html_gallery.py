# scripts/gen_html_gallery.py
from pathlib import Path
import re
import mkdocs_gen_files as gen

ASSETS_DIR = Path("docs/assets")
GALLERY_DIR = Path("gallery")       # se genera virtualmente dentro de "docs"
GALLERY_DIR_STR = GALLERY_DIR.as_posix()

pages = []

def pretty_title(stem: str) -> str:
    title = stem.replace("_", " ").replace("-", " ").strip()
    # Capitaliza palabras
    title = " ".join(w[:1].upper() + w[1:] for w in title.split())
    # Normaliza casos comunes
    title = title.replace("Erdos", "Erdős").replace("Renyi", "Rényi")
    return title

def rel_from_gallery_to_asset(asset_path: Path) -> str:
    # "../assets/subcarpeta/archivo.html"
    return "../assets/" + asset_path.relative_to(ASSETS_DIR).as_posix()

# Asegura índice aunque no haya HTMLs
with gen.open(f"{GALLERY_DIR_STR}/index.md", "w") as f:
    f.write("# Demos HTML\n\nListado automático de demos en `docs/assets/`.\n\n")

if ASSETS_DIR.exists():
    for html in sorted(ASSETS_DIR.rglob("*.html")):
        stem = html.stem
        title = pretty_title(stem)
        md_name = f"{stem}.md"
        md_path = f"{GALLERY_DIR_STR}/{md_name}"
        url = rel_from_gallery_to_asset(html)

        # Página individual con iframe
        with gen.open(md_path, "w") as f:
            f.write(f"# {title}\n\n")
            f.write("> Si tu navegador bloquea iframes, abrí el enlace directo.\n\n")
            f.write(f'<iframe src="{url}" width="100%" height="760" style="border:0;"></iframe>\n\n')
            f.write(f"[Abrir en pestaña nueva]({url})\n")

        # Traza para "Editar esta página" → archivo origen
        gen.set_edit_path(md_path, str(html))

        pages.append((title, md_name))

    # Índice con lista de todas las demos
    with gen.open(f"{GALLERY_DIR_STR}/index.md", "w") as f:
        f.write("# Demos HTML\n\nListado automático de demos en `docs/assets/`.\n\n")
        for title, md_name in pages:
            f.write(f"- [{title}](./{md_name})\n")
