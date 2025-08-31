#!/usr/bin/env node
import { promises as fs } from "fs";
import path from "path";
import { execSync } from "child_process";

const ROOT = process.cwd();
const SRC_DIR = "src/classroom/graphs/recursos";  // carpeta donde subís los .html

function guessTag(name) {
  const n = name.toLowerCase();
  if (n.includes("konigsberg")) return "Grafos";
  if (n.includes("viralidad")) return "Redes";
  if (n.includes("hipercomput")) return "Comp. teórica";
  return "Demo";
}

async function main() {
  const abs = path.join(ROOT, SRC_DIR);
  const entries = await fs.readdir(abs, { withFileTypes: true });
  const htmls = entries.filter(e => e.isFile() && e.name.toLowerCase().endsWith(".html"));

  const items = [];
  for (const e of htmls) {
    const fileAbs = path.join(abs, e.name);
    const relWeb = `/${SRC_DIR}/${e.name}`.replace(/\\/g, "/"); // ruta pública
    const raw = await fs.readFile(fileAbs, "utf8");
    const m = raw.match(/<title[^>]*>([^<]+)<\/title>/i);
    const title = (m ? m[1] : path.parse(e.name).name).trim();

    let mtime = "";
    try {
      mtime = execSync(`git log -1 --format=%cI -- "${path.relative(ROOT, fileAbs)}"`).toString().trim();
    } catch {}

    items.push({ title, path: relWeb, tag: guessTag(e.name), desc: "", mtime });
  }

  items.sort((a,b) => a.title.localeCompare(b.title, "es"));
  await fs.writeFile(path.join(ROOT, "demos.json"), JSON.stringify(items, null, 2));
  console.log(`demos.json actualizado (${items.length} items).`);
}

main().catch(err => { console.error(err); process.exit(1); });
