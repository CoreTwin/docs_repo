# update_docs/core.py

import os
import re
import json
from pathlib import Path
import difflib
from collections import defaultdict
from datetime import datetime

HEADER_RE = re.compile(
    r"^(#{1,6})\s+(.*?)\s*(?:<!--\s*id:([\w\-]+)\s*-->)?\s*$",
    re.MULTILINE,
)
INCLUDE_RE = re.compile(r"<!--\s*include:([^\s#]+)#([\w\-]+)\s*-->")

def slugify(text):
    return re.sub(r"[^\w\-]", "-", text.lower())


def generate_path_based_id(relative_path):
    """Создает уникальный идентификатор на основе пути к файлу"""
    path_id = relative_path.replace("/", "-").replace("\\", "-")
    path_id = re.sub(r"[^\w\-.]", "-", path_id.lower())
    path_id = re.sub(r"-+", "-", path_id)  # Убираем множественные дефисы
    return path_id.strip("-")


def extract_content_preview(file_path, max_chars=200):
    """Извлекает превью содержимого файла для анализа дубликатов"""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r"^#.*$", "", content, flags=re.MULTILINE)
        content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
        return content[:max_chars].strip()
    except Exception:
        return ""

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


def build_comprehensive_toc(root_dir, exclude_patterns=None):
    """Сканирует все уровни вложенности начиная с корневой папки проекта"""
    if exclude_patterns is None:
        exclude_patterns = ['.git', 'node_modules', '__pycache__', '.venv', 'build', 'dist']
    
    toc = []
    header_map = {}
    all_documents = []
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not any(pattern in d for pattern in exclude_patterns)]
        
        for file in sorted(files):
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, root_dir)
                
                unique_id = generate_path_based_id(rel_path)
                
                headers = extract_headers(file_path)
                file_stats = os.stat(file_path)
                
                doc_entry = {
                    "path": file_path,
                    "relative_path": rel_path.replace("\\", "/"),
                    "unique_id": unique_id,
                    "headers": headers,
                    "size": file_stats.st_size,
                    "modified": file_stats.st_mtime,
                    "content_preview": extract_content_preview(file_path)
                }
                
                toc.append(doc_entry)
                all_documents.append(doc_entry)
                
                # Обновление header_map
                for h in headers:
                    header_map[(rel_path.replace("\\", "/"), h["id"])] = {
                        "title": h["title"],
                        "level": h["level"],
                        "file": rel_path.replace("\\", "/")
                    }
    
    return toc, header_map, all_documents

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


def normalize_text(text):
    """Нормализует текст для сравнения"""
    normalized = re.sub(r"[^\w\s]", "", text.lower())
    return re.sub(r"\s+", " ", normalized).strip()


def find_similar_titles(documents, threshold):
    """Находит документы с похожими заголовками"""
    groups = []
    title_map = defaultdict(list)
    
    for doc in documents:
        for header in doc["headers"]:
            normalized_title = normalize_text(header["title"])
            title_map[normalized_title].append((doc, header))
    
    processed = set()
    for title1, docs1 in title_map.items():
        if title1 in processed:
            continue
            
        similar_group = [title1]
        for title2, docs2 in title_map.items():
            if title1 != title2 and title2 not in processed:
                similarity = difflib.SequenceMatcher(None, title1, title2).ratio()
                if similarity >= threshold:
                    similar_group.append(title2)
                    processed.add(title2)
        
        if len(similar_group) > 1:
            files = []
            for title in similar_group:
                files.extend([doc["relative_path"] for doc, _ in title_map[title]])
            
            groups.append({
                "type": "similar_titles",
                "pattern": title1,
                "files": list(set(files)),
                "similarity_score": threshold
            })
        
        processed.add(title1)
    
    return groups


def find_similar_content(documents, threshold):
    """Находит документы с похожим содержимым"""
    groups = []
    processed = set()
    
    for i, doc1 in enumerate(documents):
        if i in processed:
            continue
            
        similar_group = [doc1]
        for j, doc2 in enumerate(documents[i+1:], i+1):
            if j in processed:
                continue
                
            content1 = normalize_text(doc1["content_preview"])
            content2 = normalize_text(doc2["content_preview"])
            
            if len(content1) > 50 and len(content2) > 50:  # Только для файлов с достаточным содержимым
                similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
                if similarity >= threshold:
                    similar_group.append(doc2)
                    processed.add(j)
        
        if len(similar_group) > 1:
            groups.append({
                "type": "similar_content",
                "pattern": f"Похожее содержимое ({len(similar_group)} файлов)",
                "files": [doc["relative_path"] for doc in similar_group],
                "similarity_score": threshold
            })
        
        processed.add(i)
    
    return groups


def detect_duplicates(documents, similarity_threshold=0.8):
    """Находит похожие формулировки в заголовках и содержимом"""
    duplicate_groups = []
    
    title_groups = find_similar_titles(documents, similarity_threshold)
    duplicate_groups.extend(title_groups)
    
    content_groups = find_similar_content(documents, similarity_threshold)
    duplicate_groups.extend(content_groups)
    
    return duplicate_groups


def get_file_title(entry):
    """Извлекает заголовок файла из первого заголовка или имени файла"""
    if entry["headers"]:
        return entry["headers"][0]["title"]
    return os.path.basename(entry["relative_path"])


def find_file_duplicates(entry, duplicate_groups):
    """Находит информацию о дубликатах для конкретного файла"""
    duplicates = []
    for group in duplicate_groups:
        if entry["relative_path"] in group["files"]:
            other_files = [f for f in group["files"] if f != entry["relative_path"]]
            if other_files:
                duplicates.append(f"{group['type']} в {', '.join(other_files[:2])}")
    return "; ".join(duplicates)


def find_project_root():
    """Находит корень проекта (папку с .git)"""
    path = Path.cwd()
    while not (path / ".git").exists():
        if path.parent == path:
            break
        path = path.parent
    return path


def write_comprehensive_markdown_toc(toc, duplicate_groups, toc_md_path, metadata):
    """Создает структурированное Markdown оглавление с информацией о дубликатах"""
    with open(toc_md_path, "w", encoding="utf-8") as f:
        f.write("# Комплексное оглавление проекта\n\n")
        f.write(f"*Сгенерировано: {metadata['generated_at']}*  \n")
        f.write(f"*Всего файлов: {metadata['total_files']} | Групп дубликатов: {len(duplicate_groups)}*\n\n")
        
        dir_groups = defaultdict(list)
        for entry in toc:
            dir_path = os.path.dirname(entry["relative_path"])
            if not dir_path:
                dir_path = "корень"
            dir_groups[dir_path].append(entry)
        
        f.write("## 📁 Структура документации\n\n")
        for dir_path in sorted(dir_groups.keys()):
            f.write(f"### {dir_path}\n")
            for entry in sorted(dir_groups[dir_path], key=lambda x: x["relative_path"]):
                f.write(f"- [📄 {get_file_title(entry)}]({entry['relative_path']}) `{entry['unique_id']}`\n")
                
                size_kb = entry["size"] // 1024
                f.write(f"  - **Размер**: {size_kb} KB\n")
                
                duplicates = find_file_duplicates(entry, duplicate_groups)
                if duplicates:
                    f.write(f"  - **Дубликаты**: ⚠️ {duplicates}\n")
                
                f.write("\n")
        
        if duplicate_groups:
            f.write("## 🔍 Обнаруженные дубликаты\n\n")
            for i, group in enumerate(duplicate_groups, 1):
                f.write(f"### Группа {i}: \"{group['pattern']}\" ({group['similarity_score']:.0%} сходство)\n")
                for file_path in group["files"]:
                    f.write(f"- {file_path}\n")
                f.write("\n")
        
        f.write("## 📊 Статистика\n")
        f.write(f"- **Всего файлов**: {metadata['total_files']}\n")
        f.write(f"- **Групп дубликатов**: {len(duplicate_groups)}\n")
        total_headers = sum(len(entry["headers"]) for entry in toc)
        f.write(f"- **Всего заголовков**: {total_headers}\n")


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


def update_all_comprehensive(docs_dir, toc_path, toc_md_path=None, comprehensive=False, 
                            similarity_threshold=0.8, exclude_patterns=None):
    """Обновленная функция с поддержкой комплексного сканирования"""
    if comprehensive:
        root_dir = find_project_root()
        toc, header_map, all_documents = build_comprehensive_toc(root_dir, exclude_patterns)
        
        duplicate_groups = detect_duplicates(all_documents, similarity_threshold)
        
        metadata = {
            "generated_at": datetime.now().isoformat(),
            "root_directory": str(root_dir),
            "total_files": len(toc),
            "duplicate_groups": len(duplicate_groups)
        }
        
        extended_toc = {
            "metadata": metadata,
            "files": toc,
            "duplicate_groups": duplicate_groups
        }
        
        with open(toc_path, "w", encoding="utf-8") as f:
            json.dump(extended_toc, f, indent=2, ensure_ascii=False)
        
        if toc_md_path:
            write_comprehensive_markdown_toc(toc, duplicate_groups, toc_md_path, metadata)
    else:
        toc, header_map = build_toc(docs_dir)
        with open(toc_path, "w", encoding="utf-8") as f:
            json.dump(toc, f, indent=2, ensure_ascii=False)
        if toc_md_path:
            write_markdown_toc(toc, toc_md_path)
    
    errors = update_includes(docs_dir, header_map)
    if toc_md_path and not comprehensive:
        inject_back_to_toc_links(docs_dir, toc_md_path, toc)
    
    print(f"✅ TOC updated and saved to: {toc_path}")
    if errors:
        print("\n".join(errors))
    else:
        print("✅ All includes are valid.")
