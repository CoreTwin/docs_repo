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
    args = parser.parse_args()
    update_all(args.docs, args.toc)

if __name__ == "__main__":
    main()
