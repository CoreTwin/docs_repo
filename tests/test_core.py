from update_docs.core import (
    slugify,
    extract_headers,
    build_toc,
    extract_section,
    update_includes,
    write_markdown_toc,
    inject_back_to_toc_links,
)


def test_slugify():
    assert slugify("Hello World!") == "hello-world-"


def test_extract_headers(tmp_path):
    md = tmp_path / "sample.md"
    md.write_text("# Title <!-- id:main-title -->\n## Subsection\n")
    headers = extract_headers(md)
    assert headers == [
        {"level": 1, "title": "Title", "id": "main-title"},
        {"level": 2, "title": "Subsection", "id": "subsection"},
    ]


def test_build_toc(tmp_path):
    docs = tmp_path
    (docs / "a.md").write_text("# A\n")
    sub = docs / "sub"
    sub.mkdir()
    (sub / "b.md").write_text("# B\n")

    toc, header_map = build_toc(docs)

    assert toc == [
        {"file": "a.md", "headers": [{"level": 1, "title": "A", "id": "a"}]},
        {"file": "sub/b.md", "headers": [{"level": 1, "title": "B", "id": "b"}]},
    ]
    assert header_map[("a.md", "a")] == {"title": "A", "level": 1, "file": "a.md"}


def test_extract_section(tmp_path):
    md = tmp_path / "section.md"
    md.write_text(
        "# Top\ntext\n## Section\nline1\nline2\n## End\n"
    )
    result = extract_section(md, "section", 2)
    assert result == "line1\nline2"


def test_update_includes(tmp_path):
    docs = tmp_path
    (docs / "src.md").write_text("# Source\n## part\ncontent\n")
    target = docs / "dest.md"
    target.write_text("# Dest\n<!-- include:src.md#part -->\n")

    toc, header_map = build_toc(docs)
    errors = update_includes(docs, header_map)

    assert errors == []
    content = target.read_text()
    assert "<!-- BEGIN include:src.md#part -->" in content
    assert "content" in content


def test_write_markdown_toc(tmp_path):
    toc = [{"file": "index.md", "headers": []}]
    path = tmp_path / "toc.md"
    write_markdown_toc(toc, path)
    content = path.read_text()
    assert "[index.md](docs/index.md)" in content
    assert '<a id="index-md"></a>' in content


def test_inject_back_to_toc_links(tmp_path):
    docs = tmp_path
    md = docs / "index.md"
    md.write_text("# Title\n")
    toc_md = tmp_path / "toc.md"
    toc_md.write_text("toc")
    toc = [{"file": "index.md", "headers": []}]
    inject_back_to_toc_links(docs, toc_md, toc)
    content = md.read_text().splitlines()[0]
    assert "[Back to TOC]" in content

