# Cómo aportar al catálogo

Aquí viven las plantillas de diagramas y documentos que Esquema descarga. Son **solo datos** (JSON): no hace falta programar.
*(English below.)*

## Una plantilla nueva
- **Lo más fácil:** descríbela con palabras en el formulario
  [«Proponer una plantilla»](https://github.com/esquema-app/esquema-catalogo/issues/new?template=plantilla.yml): qué cajas tiene y
  cómo se conectan, o qué secciones lleva el documento (o pega el Mermaid si ya lo tienes). Nosotros armamos el JSON, en español y en
  inglés, te ponemos como autor y te avisamos.
- **Por pull request:** agrega `plantillas/<categoria>/<id>.json` (formato en el [README](README.md)), corre
  `python3 herramientas/generar_indice.py` (valida y regenera `index.json`) y, si tienes el repo de la app al lado,
  `node herramientas/revisar_diagramas.mjs ../esquema` (dibuja cada diagrama con el motor de Esquema). Sube el archivo con `index.json`.
- **Reglas:** el nombre y la descripción dicen lo que es; el `id` no repite otro; **solo ejemplos ficticios** (Ana Pérez, Matías
  Soto, Banco Ejemplo), nada personal ni de empresas o productos reales; textos cortos que sirvan para cualquiera; y que se vea bien
  en Esquema.

## Cambiar el formato
`herramientas/plantilla_formato.py` es **el mismo archivo** que `bin/plantilla_formato.py` de la app. Un campo o una categoría nueva
necesita primero el cambio en la app (motor, interfaz y pruebas) y una versión publicada; después se copia aquí. El workflow revisa
que los dos sean idénticos.

## Licencia de lo que aportas
Todo el catálogo es de dominio público con [CC0 1.0](LICENSE). Al abrir un issue o un pull request con una plantilla, aceptas
publicarla así: cualquiera la puede usar, también en trabajo comercial, sin pedir permiso. Aporta solo lo que hiciste tú.

## Cómo revisamos
Todo entra por pull request y lo junta alguien que mantiene el proyecto. GitHub revisa en cada pull request (sin secretos y con
permiso de solo lectura) que el JSON pase la validación, que `index.json` esté al día, que el formato sea el de la app y que cada
diagrama se dibuje sin errores. Una persona revisa además que no traiga nada personal ni copiado y que sirva. Si algo falta te lo
pedimos con un comentario.

**Fallas de seguridad:** nunca en un issue público; avísanos en privado como explica [SECURITY.md](SECURITY.md).

---

**English:** templates are data-only JSON. The easiest way is to describe yours in words with the "Propose a template" issue form —
we'll write the JSON (in Spanish and English) and credit you. Or open a pull request with `plantillas/<category>/<id>.json` after
running `python3 herramientas/generar_indice.py` (and `node herramientas/revisar_diagramas.mjs ../esquema` if you have the app repo
next to it). Fictional examples only, nothing personal or branded. `herramientas/plantilla_formato.py` is the same file as the app's
`bin/plantilla_formato.py`: format changes land in the app first. Everything is CC0 1.0. A maintainer reviews every pull request.
