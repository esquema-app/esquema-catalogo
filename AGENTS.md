# Catálogo de Esquema

Repo **público** con las plantillas de la comunidad que la app Esquema descarga a pedido («Nuevo» → «Comunidad»). Solo datos JSON,
validados por la app al descargarlos. El proyecto principal (y su `AGENTS.md`, la guía para personas y para cualquier IA) está en
[esquema-app/esquema](https://github.com/esquema-app/esquema). `CLAUDE.md` y `GEMINI.md` solo importan este archivo.

- `plantillas/<categoria>/<id>.json` (categorías: `plantilla_formato.CATEGORIAS`) + `index.json` en la raíz (generado: cada plantilla
  entera con `ruta`, `sha256` y `tamano`; la app compara tamaño y huella antes de guardar).
- `herramientas/plantilla_formato.py` es **idéntico** a `esquema/bin/plantilla_formato.py` (el workflow lo compara con `main` de la
  app y las pruebas de la app lo comparan si este repo está al lado). Un cambio de formato entra primero en la app (motor, interfaz y
  pruebas) y se publica; después se copia aquí. Así una plantilla nunca le llega a una app que no la entiende.
- `herramientas/generar_indice.py` valida y regenera `index.json` (`--revisar` no escribe: lo usa el workflow). Córrelo antes de cada commit.
- `herramientas/revisar_diagramas.mjs <carpeta de esquema>` dibuja cada diagrama con el motor de la app y falla si alguno tiene
  errores o es de un tipo que Esquema todavía no dibuja.
- Propuestas por issue (`plantilla.yml`; puede venir descrita con palabras: armar el JSON en español e inglés, `autor` = usuario de
  GitHub de quien la propuso), revisarla a mano (nada personal ni de empresas reales, nombres ficticios como Ana Pérez o Banco
  Ejemplo, el nombre dice lo que es), correr las dos herramientas y abrir el pull request.

Reglas: nada personal del usuario ni de su trabajo (es público); nunca código, HTML ni scripts en los JSON; el Mermaid, del
[subconjunto que Esquema dibuja](https://github.com/esquema-app/esquema/blob/main/AGENTS.md#subconjunto-de-mermaid). Commits en
español, autor con correo `@users.noreply.github.com`. Revisar aportes: skill `revisar-aportes-open-source`; nunca se junta sin
aprobación de quien mantiene.
