// Dibuja cada plantilla del catálogo con el motor de Esquema (el mismo de la app) y falla si algún diagrama tiene errores o si
// Esquema todavía no sabe dibujarlo. Así nunca llega a la app una plantilla que se vea rota.
// Uso: node herramientas/revisar_diagramas.mjs <carpeta de esquema>   (por ejemplo ../esquema; el workflow la baja en _esquema)
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const ESQUEMA = path.resolve(process.argv[2] || path.join(RAIZ, "..", "esquema"));
const require = createRequire(import.meta.url);
for (const f of ["texto", "flujo", "secuencia", "capas", "formas", "dibujo", "markdown"]) require(path.join(ESQUEMA, "ui/motor", f + ".js"));
const M = globalThis.EsquemaMotor;
let fallas = 0, revisados = 0;

function revisar(nombre, texto) {
  revisados++;
  const r = M.dibujar(texto);
  if (r.errores.length) { fallas++; console.log(`✗ ${nombre}: línea ${r.errores[0].linea + 1}: ${M.frase(r.errores[0])}`); return; }
  if (r.tipo !== "flujo" && r.tipo !== "secuencia") { fallas++; console.log(`✗ ${nombre}: Esquema todavía no dibuja este tipo de diagrama`); return; }
  if (!r.partes.length) { fallas++; console.log(`✗ ${nombre}: el diagrama está vacío`); }
}

const base = path.join(RAIZ, "plantillas");
for (const cat of fs.readdirSync(base).filter((x) => fs.statSync(path.join(base, x)).isDirectory()).sort()) {
  for (const archivo of fs.readdirSync(path.join(base, cat)).filter((x) => x.endsWith(".json")).sort()) {
    const pl = JSON.parse(fs.readFileSync(path.join(base, cat, archivo), "utf8"));
    for (const [idioma, texto] of Object.entries(pl.contenido || {})) {
      const nombre = `plantillas/${cat}/${archivo} (${idioma})`;
      if (pl.tipo === "diagrama") revisar(nombre, texto);
      else {
        const bloques = M.bloquesMermaid(texto);
        if (!bloques.length) console.log(`  ${nombre}: documento sin diagramas`);
        bloques.forEach((b, i) => revisar(`${nombre}, diagrama ${i + 1}`, b.contenido));
      }
    }
  }
}
console.log(fallas ? `\n${fallas} diagramas con problemas` : `✓ ${revisados} diagramas se dibujan sin errores con el motor de Esquema`);
process.exit(fallas ? 1 : 0);
