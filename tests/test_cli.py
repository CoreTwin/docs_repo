import json
import subprocess
import sys
from pathlib import Path


def test_cli_creates_toc(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "index.md").write_text("# Title\n")
    toc_path = tmp_path / "toc.json"

    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "update_docs.cli", "--docs", str(docs), "--toc", str(toc_path)],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert toc_path.exists()
    data = json.loads(toc_path.read_text())
    assert data[0]["file"] == "index.md"

