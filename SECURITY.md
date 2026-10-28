# Seguridad del catálogo de Esquema

*(English below.)*

Este repo tiene las plantillas que la app [Esquema](https://github.com/esquema-app/esquema) descarga. Son **solo datos** (JSON):
ningún archivo de aquí debe poder ejecutar código, leer archivos, colar HTML o scripts en la app ni escribir fuera de la carpeta de
Esquema.

Si encuentras algo que se salte esa regla (una plantilla que haga algo raro en la app, una forma de que un JSON pase la validación con
algo escondido, un diagrama que cuele HTML en la vista previa, un problema en `herramientas/` o en el workflow), avísanos **en
privado** en [**Reportar una vulnerabilidad**](https://github.com/esquema-app/esquema-catalogo/security/advisories/new). No abras un
issue público ni un pull request con el detalle mientras no esté arreglado. Te respondemos dentro de una semana.

Cómo nos cuidamos:
- Todo entra por pull request y lo revisa una persona.
- `herramientas/generar_indice.py` valida con `herramientas/plantilla_formato.py` (el mismo archivo que la app): claves conocidas,
  textos con largo máximo, nombres de archivo sin rutas, cada plantilla en la carpeta de su categoría con el nombre de su id, sin ids
  repetidos y hasta 100 KB. GitHub lo corre en cada pull request con permiso de solo lectura, actions fijadas por SHA y sin
  `pull_request_target`, y además dibuja cada diagrama con el motor de la app.
- La app solo descarga desde `raw.githubusercontent.com/esquema-app/esquema-catalogo`, sin seguir redirecciones y con tamaño máximo;
  valida el índice, compara el tamaño y la huella SHA-256 de cada plantilla con ese índice y la vuelve a validar antes de guardarla en
  su propia carpeta (nunca en la carpeta de documentos de la persona). Lo que muestra lo escapa siempre y el motor solo dibuja SVG.

---

**English:** this repo holds data-only JSON templates downloaded by the Esquema app. If you find a way for catalog content to run
code, inject HTML or scripts into the app, write outside Esquema's own folder, or an issue in `herramientas/` or the workflow, please
report it privately via [Report a vulnerability](https://github.com/esquema-app/esquema-catalogo/security/advisories/new) instead of
a public issue. We reply within a week.
