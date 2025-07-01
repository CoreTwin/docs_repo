# update_docs/cli.py

import argparse
from pathlib import Path

from update_docs.core import update_all


def find_project_root() -> Path:
    """Return the nearest parent directory containing a .git folder."""
    path = Path.cwd()
    while not (path / ".git").exists():
        if path.parent == path:
            break
        path = path.parent
    return path

def main():
    parser = argparse.ArgumentParser(description="Update and validate documentation structure.")
    parser.add_argument(
        "--docs", default="docs", help="Path to documentation root directory"
    )
    parser.add_argument(
        "--toc", default="toc.json", help="Path to TOC file (output)"
    )
    parser.add_argument(
        "--toc-md", help="Path to Markdown TOC file (output)", default=None
    )
    args = parser.parse_args()

    root = find_project_root()

    def resolve(p: str) -> Path:
        path = Path(p)
        return path if path.is_absolute() else root / path

    docs = resolve(args.docs)
    toc = resolve(args.toc)
    toc_md = resolve(args.toc_md) if args.toc_md else None

    update_all(str(docs), str(toc), str(toc_md) if toc_md else None)

if __name__ == "__main__":
    main()
