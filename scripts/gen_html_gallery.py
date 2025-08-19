# scripts/gen_html_gallery.py
from pathlib import Path
import mkdocs_gen_files as gen

ASSETS_DIR = Path("docs/assets")
GALLERY_DIR = Path("gallery")  # se genera virtualmente dentro del sitio

def pretty_title(stem: str) -> str:
    t = stem.replace("_", " ").replace("-", " ").strip().title()
    t = t.replace("Erdos", "Erdős").replace("Renyi", "Rényi")
    return t

def rel_from_gallery_to_asset(asset_path: Path) -> str:
    # "../assets/....html|htm" (gallery/* -> assets/*)
    return "../assets/" + asset_path.relative_to(ASSETS_DIR).as_posix()

# Índice por defecto
with gen.open(f"{GALLERY_DIR.as_posix()}/index.md", "w") as f:
    f.write("# Demos HTML\n\nListado automático de demos en `docs/assets/`.\n\n")

if ASSETS_DIR.exists():
    htmls = sorted(list(ASSETS_DIR.rglob("*.html")) + list(ASSETS_DIR.rglob("*.htm")))
    pages = []
    for html in htmls:
        stem = html.stem
        title = pretty_title(stem)
        md_name = f"{stem}.md"
        md_path = f"{GALLERY_DIR.as_posix()}/{md_name}"
        url = rel_from_gallery_to_asset(html)

        # Página individual con iframe
        with gen.open(md_path, "w") as f:
            f.write(f"# {title}\n\n")
            f.write("> Si tu navegador bloquea iframes, abrí el enlace directo.\n\n")
            f.write(f'<iframe src="{url}" width="100%" height="760" style="border:0;"></iframe>\n\n')
            f.write(f"[Abrir en pestaña nueva]({url})\n")

        # Traza de edición al archivo original
        gen.set_edit_path(md_path, str(html))
        pages.append((title, md_name))

    # Índice con links
    with gen.open(f"{GALLERY_DIR.as_posix()}/index.md", "w") as f:
        f.write("# Demos HTML\n\nListado automático de demos en `docs/assets/`.\n\n")
        for title, md_name in pages:
            f.write(f"- [{title}](./{md_name})\n")
