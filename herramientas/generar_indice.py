#!/usr/bin/env python3
"""Valida todas las plantillas y regenera index.json (lo que la app de Esquema descarga).

Uso: python3 herramientas/generar_indice.py             (desde la raíz del catálogo; solo biblioteca estándar)
     python3 herramientas/generar_indice.py --revisar   (no escribe nada: sale con 1 si hay problemas o si index.json no está al día)

Todo es solo datos. La validación de cada plantilla sale de herramientas/plantilla_formato.py, que es el MISMO archivo que usa la
app (esquema/bin/plantilla_formato.py, el validador de su pieza «catálogo») para revisar lo que descarga: claves y tipos conocidos,
largos máximos, nombres de archivo sin rutas. Aquí se suman las reglas del índice (las mismas que revisa la app al leerlo, en
bin/catalogo.py): cada plantilla en plantillas/<categoria>/<id>.json, sin ids repetidos y hasta 100 KB. El índice lleva la huella
SHA-256 y el tamaño de cada archivo: la app los compara con lo que descarga antes de guardarlo.
"""
import glob
import hashlib
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "herramientas"))
import plantilla_formato  # noqa: E402

MAX_BYTES = 100 * 1024        # una plantilla (el archivo .json): lo mismo que acepta la app
MAX_EN_INDICE = 1000          # plantillas en el índice
RUTA = re.compile(r"plantillas/([a-z-]+)/([a-z0-9]+(?:-[a-z0-9]+)*)\.json")


def indice(raiz):
    """Valida <raiz>/plantillas/<categoria>/<id>.json y devuelve (índice, problemas). Solo entra lo que pasa todas las reglas."""
    categorias = plantilla_formato.CATEGORIAS
    lista, problemas, vistos = [], [], {}
    base = os.path.join(raiz, "plantillas")
    for nombre in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        if not os.path.isdir(os.path.join(base, nombre)):
            if not nombre.endswith(".md"):
                problemas.append(f"plantillas/{nombre}: aquí solo van carpetas de categorías")
            continue
        if nombre not in categorias:
            problemas.append(f"plantillas/{nombre}/: categoría desconocida (" + ", ".join(categorias) + ")")
    for ruta in sorted(glob.glob(os.path.join(base, "*", "*"))):
        rel = os.path.relpath(ruta, raiz).replace(os.sep, "/")
        m = RUTA.fullmatch(rel)
        if not m or os.path.islink(ruta) or not os.path.isfile(ruta):
            problemas.append(f"{rel}: solo archivos plantillas/<categoria>/<id>.json (minúsculas, números y guiones)")
            continue
        if m.group(1) not in categorias:
            continue
        with open(ruta, "rb") as f:
            crudo = f.read(MAX_BYTES + 1)
        if len(crudo) > MAX_BYTES:
            problemas.append(f"{rel}: pesa más de {MAX_BYTES // 1024} KB")
            continue
        try:
            p = json.loads(crudo.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as e:
            problemas.append(f"{rel}: no es JSON válido en UTF-8 ({e})")
            continue
        e = plantilla_formato.validar(p)
        if not e and p["id"] != m.group(2):
            e = ["el archivo tiene que llamarse como su id"]
        if not e and p["categoria"] != m.group(1):
            e = [f"está en la carpeta {m.group(1)} y su categoria es «{p['categoria']}»"]
        if not e and p["id"] in vistos:
            e = [f"el id «{p['id']}» ya está en {vistos[p['id']]}"]
        if e:
            problemas.append(f"{rel}: " + ", ".join(e))
            continue
        vistos[p["id"]] = rel
        lista.append({**p, "ruta": rel, "sha256": hashlib.sha256(crudo).hexdigest(), "tamano": len(crudo)})
    if len(lista) > MAX_EN_INDICE:
        problemas.append(f"el índice no puede tener más de {MAX_EN_INDICE} plantillas")
    return {"formato": plantilla_formato.FORMATO, "plantillas": lista[:MAX_EN_INDICE]}, problemas


def main():
    datos, problemas = indice(RAIZ)
    for p in datos["plantillas"]:
        print("✓ " + p["ruta"])
    for p in problemas:
        print("✗ " + p)
    texto = json.dumps(datos, ensure_ascii=False, indent=1) + "\n"
    ruta = os.path.join(RAIZ, "index.json")
    if "--revisar" in sys.argv:
        actual = open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else ""
        if actual != texto:
            problemas.append("index.json no está al día: corre python3 herramientas/generar_indice.py y súbelo")
            print("✗ " + problemas[-1])
    elif not problemas:
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
    print(f"\n{len(datos['plantillas'])} plantillas en el índice" + (f", {len(problemas)} problemas" if problemas else ""))
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
