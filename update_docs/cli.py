# update_docs/cli.py

import argparse
from update_docs.core import update_all

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
    update_all(args.docs, args.toc, args.toc_md)

if __name__ == "__main__":
    main()
