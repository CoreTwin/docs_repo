# update_docs/core.py

import os
import re
import json

HEADER_RE = re.compile(
    r"^(#{1,6})\s+(.*?)\s*(?:<!--\s*id:([\w\-]+)\s*-->)?\s*$",
    re.MULTILINE,
)
INCLUDE_RE = re.compile(r"<!--\s*include:([^\s#]+)#([\w\-]+)\s*-->")

def slugify(text):
    return re.sub(r"[^\w\-]", "-", text.lower())

def extract_headers(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    headers = []
    for match in HEADER_RE.finditer(content):
        level = len(match.group(1))
        title = match.group(2).strip()
        id_tag = match.group(3) or slugify(title)
        headers.append({
            "level": level,
            "title": title,
            "id": id_tag
        })
    return headers

def build_toc(docs_dir):
    toc = []
    header_map = {}
    for root, dirs, files in os.walk(docs_dir):
        dirs.sort()
        for file in sorted(files):
            if file.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, file), docs_dir)
                headers = extract_headers(os.path.join(docs_dir, rel_path))
                if headers:
                    toc.append({
                        "file": rel_path.replace("\\", "/"),
                        "headers": headers
                    })
                    for h in headers:
                        header_map[(rel_path.replace("\\", "/"), h["id"])] = {
                            "title": h["title"],
                            "level": h["level"],
                            "file": rel_path.replace("\\", "/")
                        }
    return toc, header_map

def extract_section(file_path, section_id, level):
    with open(file_path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    section = []
    found = False
    current_level = None
    for i, line in enumerate(lines):
        match = HEADER_RE.match(line)
        if match:
            l = len(match.group(1))
            t = match.group(2).strip()
            id_tag = match.group(3) or slugify(t)
            if id_tag == section_id:
                found = True
                current_level = l
                continue
            if found and l <= current_level:
                break
        if found:
            section.append(line)
    return "\n".join(section).strip()

def update_includes(docs_dir, header_map):
    errors = []
    for root, dirs, files in os.walk(docs_dir):
        dirs.sort()
        for file in sorted(files):
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, docs_dir)
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()

                updated = content
                changed = False

                for match in INCLUDE_RE.finditer(content):
                    include_file, include_id = match.groups()
                    key = (include_file, include_id)
                    if key not in header_map:
                        errors.append(f"⚠️ include not found: {include_file}#{include_id} in {rel_path}")
                        continue

                    original_path = os.path.join(docs_dir, include_file)
                    level = header_map[key]["level"]
                    text = extract_section(original_path, include_id, level)

                    block = f"<!-- BEGIN include:{include_file}#{include_id} -->\n{text}\n<!-- END include -->"
                    block_re = re.compile(
                        rf"<!--\s*BEGIN\s+include:{re.escape(include_file)}#{re.escape(include_id)}\s*-->.*?<!--\s*END\s+include\s*-->",
                        re.DOTALL,
                    )
                    if block_re.search(updated):
                        updated = block_re.sub(block, updated)
                        changed = True
                    else:
                        insert_point = match.end()
                        updated = updated[:insert_point] + "\n" + block + updated[insert_point:]
                        changed = True

                if changed:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(updated)
    return errors


def write_markdown_toc(toc, toc_md_path):
    with open(toc_md_path, "w", encoding="utf-8") as f:
        f.write("# Table of Contents\n\n")
        for entry in toc:
            file_path = entry["file"]
            anchor = slugify(file_path.replace("/", "-"))
            f.write(f'- <a id="{anchor}"></a>[{file_path}]({file_path})\n')


def inject_back_to_toc_links(docs_dir, toc_md_path, toc):
    abs_toc = os.path.abspath(toc_md_path)
    for entry in toc:
        rel_file = entry["file"]
        file_path = os.path.join(docs_dir, rel_file)
        if os.path.abspath(file_path) == abs_toc:
            continue
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
        anchor = slugify(rel_file.replace("/", "-"))
        relative = os.path.relpath(toc_md_path, os.path.dirname(file_path)).replace("\\", "/")
        link = f"[Back to TOC]({relative}#{anchor})"
        if link in content:
            continue
        updated = f"{link}\n\n{content}"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated)

def update_all(docs_dir, toc_path, toc_md_path=None):
    toc, header_map = build_toc(docs_dir)
    with open(toc_path, "w", encoding="utf-8") as f:
        json.dump(toc, f, indent=2, ensure_ascii=False)
    if toc_md_path:
        write_markdown_toc(toc, toc_md_path)
    errors = update_includes(docs_dir, header_map)
    if toc_md_path:
        inject_back_to_toc_links(docs_dir, toc_md_path, toc)
    print(f"✅ TOC updated and saved to: {toc_path}")
    if errors:
        print("\n".join(errors))
    else:
        print("✅ All includes are valid.")
