#!/usr/bin/env python3
"""Autotest sin dependencias de las páginas legales y sus rutas Jekyll."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "index.md": "/",
    "privacy-policy.md": "/privacy-policy/",
    "terms-of-use.md": "/terms-of-use/",
    "support.md": "/support/",
    "third-party-licenses.md": "/third-party-licenses/",
}


def validate():
    """Comprueba contenido, navegación, configuración y tamaño de los módulos."""
    errors = []
    config = (ROOT / "_config.yml").read_text()
    for expected in ("baseurl: /LegalAsistencia", "theme: jekyll-theme-minimal", "lang: es"):
        if expected not in config:
            errors.append(f"Configuración ausente: {expected}")
    for name, route in PAGES.items():
        text = (ROOT / name).read_text()
        front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not front or f"permalink: {route}\n" not in front.group(1) + "\n":
            errors.append(f"{name}: permalink o front matter incorrecto")
        if not front or not re.search(r"^title: \S", front.group(1), re.M):
            errors.append(f"{name}: falta título")
        if "miudo09dev@gmail.com" not in text:
            errors.append(f"{name}: falta contacto")
        for link in re.findall(r"\{\{ '([^']+)' \| relative_url \}\}", text):
            if link not in PAGES.values():
                errors.append(f"{name}: ruta interna inexistente: {link}")
        if re.search(r"\b(?:TODO|FIXME|Lorem ipsum)\b", text):
            errors.append(f"{name}: contenido pendiente en página pública")
        if "Migalla" in text:
            errors.append(f"{name}: referencia a otra app")
    index = (ROOT / "index.md").read_text()
    for route in list(PAGES.values())[1:]:
        if f"'{route}' | relative_url" not in index:
            errors.append(f"Portada sin enlace a {route}")
    for file in sorted(ROOT.rglob("*")):
        if file.is_file() and file.suffix in {".md", ".yml", ".py"}:
            count = len(file.read_text().splitlines())
            if count > 400:
                errors.append(f"{file.relative_to(ROOT)} supera 400 líneas: {count}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"OK: {len(PAGES)} páginas, rutas internas, configuración y límite de 400 líneas.")


if __name__ == "__main__":
    validate()
