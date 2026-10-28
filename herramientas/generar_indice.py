#!/usr/bin/env python3
"""Valida todas las plantillas y regenera index.json (lo que la app de Esquema descarga).

Uso: python3 herramientas/generar_indice.py             (desde la raíz del catálogo; solo biblioteca estándar)
     python3 herramientas/generar_indice.py --revisar   (no escribe nada: sale con 1 si hay problemas o si index.json no está al día)

Todo es solo datos. La validación y el índice salen de herramientas/plantilla_formato.py, que es el MISMO archivo que usa la app
(esquema/bin/plantilla_formato.py) para revisar lo que descarga: claves y tipos conocidos, largos máximos, nombres de archivo sin
rutas, cada plantilla en plantillas/<categoria>/<id>.json, sin ids repetidos y hasta 100 KB. El índice lleva la huella SHA-256 y el
tamaño de cada archivo: la app los compara con lo que descarga antes de guardarlo.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "herramientas"))
import plantilla_formato  # noqa: E402


def main():
    datos, problemas = plantilla_formato.indice(RAIZ)
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
