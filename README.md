# Catálogo de Esquema

Plantillas de **diagramas y documentación** que [Esquema](https://github.com/esquema-app/esquema) descarga gratis, hechas por la
comunidad. Sin servidores: la app lee estos archivos directo desde GitHub y **solo acepta datos JSON** que pasan la misma validación
que este repo (nunca código). *(English below.)*

En Esquema: **Nuevo → Comunidad**, toca una plantilla y queda en tus plantillas.

## Qué hay

| Categoría | Plantillas |
|---|---|
| `arquitectura` | Sitio estático con CDN · Cola de trabajos con reintentos |
| `secuencia` | Webhook de un pago · Subir un archivo con URL firmada |
| `flujo-de-usuario` | Recuperar la contraseña |
| `proceso` | Del cambio a producción |
| `documentacion` | Informe de incidente · Diseño técnico (RFC) |

| Archivo | Qué es |
|---|---|
| `plantillas/<categoria>/<id>.json` | Una plantilla por archivo. |
| `index.json` | El índice que lee la app: cada plantilla con su huella SHA-256 y su tamaño (se genera, no se edita a mano). |
| `herramientas/plantilla_formato.py` | El formato y su validación: **el mismo archivo** que usa la app (`esquema/bin/`). |
| `herramientas/generar_indice.py` | Valida todo y regenera `index.json`. |
| `herramientas/revisar_diagramas.mjs` | Dibuja cada diagrama con el motor de Esquema y avisa si alguno tiene errores. |

## Crear una plantilla (sin programar)

Una plantilla es un diagrama en [Mermaid](https://mermaid.js.org) (`.mmd`) o un documento en Markdown con diagramas (`.md`), con su
nombre y su descripción en cada idioma:

```json
{
  "formato": 1,
  "id": "recuperar-contrasena",
  "categoria": "flujo-de-usuario",
  "tipo": "diagrama",
  "nombre": { "es": "Recuperar la contraseña", "en": "Reset a password" },
  "descripcion": { "es": "Desde «Olvidé mi contraseña» hasta entrar de nuevo.", "en": "From “Forgot my password” to signing in again." },
  "archivo": { "es": "recuperar-contrasena.mmd", "en": "password-reset.mmd" },
  "contenido": { "es": "flowchart TD\n    A([Olvidé mi contraseña]) --> B[/Escribe su correo/]\n…", "en": "flowchart TD\n…" },
  "autor": "tu-usuario",
  "etiquetas": ["contraseña", "password"]
}
```

| Campo | Qué es |
|---|---|
| `id` | Minúsculas, números y guiones (hasta 60). El archivo se llama `<id>.json` y va en la carpeta de su categoría. |
| `categoria` | `arquitectura`, `secuencia`, `flujo-de-usuario`, `proceso` o `documentacion`. |
| `tipo` | `diagrama` (crea un `.mmd`) o `documento` (crea un `.md`). |
| `nombre`, `descripcion` | Por idioma (`es` obligatorio, `en` si puedes): hasta 80 y 200 caracteres. |
| `archivo` | El nombre sugerido por idioma: letras, números, `_` y `-`, terminado en `.mmd` o `.md` según el tipo. |
| `contenido` | El texto por idioma (hasta 20.000 caracteres), con el [Mermaid que Esquema dibuja](https://github.com/esquema-app/esquema/blob/main/AGENTS.md#subconjunto-de-mermaid). Íconos de arquitectura con una línea `%% esquema: {"iconos": {"API": "api"}}` que GitHub ignora. |
| `autor`, `etiquetas` | Opcionales: tu usuario y hasta 10 palabras para encontrarla. |

1. **Pruébala en Esquema:** escríbela como un archivo `.mmd` o `.md` en tu carpeta y mira que se vea bien en el lienzo.
2. **Compártela:** abre un [issue «Proponer una plantilla»](https://github.com/esquema-app/esquema-catalogo/issues/new?template=plantilla.yml)
   y descríbela con palabras (o pega el Mermaid): nosotros armamos el JSON con tu usuario como autor. También puedes abrir un pull
   request con `plantillas/<categoria>/<id>.json` después de correr `python3 herramientas/generar_indice.py`.

Usa siempre ejemplos ficticios (Ana Pérez, Banco Ejemplo): nada personal ni de empresas reales. Más detalle en
[CONTRIBUTING.md](CONTRIBUTING.md). Todo aporte lo revisa una persona antes de entrar.

## Licencia

Todo el contenido del catálogo (plantillas e índice) es de dominio público con [CC0 1.0](LICENSE): cualquiera puede usarlo, cambiarlo
y compartirlo, también en documentación de trabajo o comercial, sin pedir permiso ni nombrar a nadie. Al aportar, aceptas publicar tu
aporte así. El código de `herramientas/` es el mismo de la app y sigue con su licencia,
[AGPL-3.0](https://github.com/esquema-app/esquema/blob/main/LICENSE).

🔒 ¿Una falla de seguridad? Avísanos en privado: [SECURITY.md](SECURITY.md).

---

## English

**Esquema's community catalog:** free **diagram and documentation templates** that the [Esquema](https://github.com/esquema-app/esquema)
app downloads (**New → Community**). Each file is **data-only JSON**: a Mermaid diagram (`.mmd`) or a Markdown document with diagrams
(`.md`), with its name, description and suggested file name in each language. The app validates it with the same format file this repo
uses (`herramientas/plantilla_formato.py`), checks its size and SHA-256 against `index.json` and draws it with its own engine — nothing
here can ever run code.

Categories: `arquitectura` (architecture), `secuencia` (sequence, APIs), `flujo-de-usuario` (user flows), `proceso` (business
processes) and `documentacion` (documents such as incident reports or design docs).

**Make one without coding:** open a ["Propose a template"](https://github.com/esquema-app/esquema-catalogo/issues/new?template=plantilla.yml)
issue and describe it in words (or paste the Mermaid) — we'll write the JSON and credit you. Or open a pull request with
`plantillas/<category>/<id>.json` after running `python3 herramientas/generar_indice.py`. Use fictional examples only. A maintainer
reviews every contribution; CI checks the format, the index and that every diagram renders with Esquema's engine.

**License:** everything in the catalog (templates and index) is dedicated to the public domain under [CC0 1.0](LICENSE): anyone can
use, change and share it, including in commercial work, without asking or giving credit. By contributing, you agree to release your
contribution the same way. The code in `herramientas/` is the app's and stays under AGPL-3.0. Security issues: please report them
privately ([SECURITY.md](SECURITY.md)).
