"""
export.py — JARVIS vault → docs/data.json
Reads 01-Programs, 02-Skills, 03-Modules markdown frontmatter
and outputs a node/link graph for the GitHub Pages visualizer.
"""

import json
import os
import re
from pathlib import Path

import yaml  # PyYAML

VAULT = Path(__file__).parent
DOCS = VAULT / "docs"
DOCS.mkdir(exist_ok=True)

DIRS = {
    "program": VAULT / "01-Programs",
    "skill":   VAULT / "02-Skills",
    "module":  VAULT / "03-Modules",
}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def load_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def collect_nodes() -> tuple[list[dict], dict[str, str]]:
    nodes: list[dict] = []
    id_map: dict[str, str] = {}  # normalized_title → node_id

    for node_type, folder in DIRS.items():
        for path in sorted(folder.rglob("*.md")):
            fm = load_frontmatter(path)
            title = fm.get("title") or path.stem
            node_id = path.stem.lower().replace(" ", "-")

            status  = fm.get("status", "")
            version = fm.get("version") or fm.get("revision", "")
            language = fm.get("language", "")
            github  = fm.get("github", "")
            tags    = fm.get("tags") or []
            stack   = fm.get("stack") or []

            node = {
                "id":       node_id,
                "label":    title,
                "type":     node_type,
                "status":   str(status),
                "version":  str(version),
                "language": language,
                "github":   github,
                "tags":     tags if isinstance(tags, list) else [tags],
                "stack":    stack if isinstance(stack, list) else [stack],
                "skills":   fm.get("skills") or [],
                "modules":  fm.get("modules") or [],
            }
            nodes.append(node)
            id_map[title.lower().replace(" ", "-")] = node_id
            id_map[title.lower()] = node_id

    return nodes, id_map


def normalize(name: str, id_map: dict[str, str]) -> str | None:
    key = str(name).lower().replace(" ", "-")
    if key in id_map:
        return id_map[key]
    key2 = str(name).lower()
    if key2 in id_map:
        return id_map[key2]
    return None


def build_links(nodes: list[dict], id_map: dict[str, str]) -> list[dict]:
    links: list[dict] = []
    seen: set[tuple] = set()

    def add(src: str, tgt: str, rel: str):
        pair = (src, tgt)
        if pair not in seen:
            seen.add(pair)
            links.append({"source": src, "target": tgt, "rel": rel})

    for n in nodes:
        nid = n["id"]
        for skill_name in n.get("skills") or []:
            tid = normalize(skill_name, id_map)
            if tid and tid != nid:
                add(nid, tid, "uses_skill")
        for mod_name in n.get("modules") or []:
            tid = normalize(mod_name, id_map)
            if tid and tid != nid:
                add(nid, tid, "uses_module")

    return links


def main():
    nodes, id_map = collect_nodes()
    links = build_links(nodes, id_map)

    data = {"nodes": nodes, "links": links}
    out = DOCS / "data.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    counts = {t: sum(1 for n in nodes if n["type"] == t) for t in DIRS}
    print(f"[export] {out}")
    print(f"  nodes : {len(nodes)}  ({counts})")
    print(f"  links : {len(links)}")


if __name__ == "__main__":
    main()
