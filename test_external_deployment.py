#!/usr/bin/env python3
"""Интеграционный тест развертывания update-docs во внешнем репозитории."""

import os
import sys
import tempfile
import subprocess
import json
from pathlib import Path
import pytest


def test_external_deployment():
    print("🧪 Testing external deployment...")
    orig_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as temp_dir:
        test_repo = Path(temp_dir) / "test_repo"
        test_repo.mkdir()
        try:
            os.chdir(test_repo)
            subprocess.run(["git", "init"], check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], check=True)
            subprocess.run(["git", "config", "user.name", "Test User"], check=True)

            print(f"✅ Created test repository: {test_repo}")

            docs_dir = test_repo / "docs"
            docs_dir.mkdir()
            (docs_dir / "README.md").write_text("# Test Project\n")
            (docs_dir / "setup.md").write_text("# Setup Guide\n")
            api_dir = docs_dir / "api"
            api_dir.mkdir()
            (api_dir / "README.md").write_text("# API Reference\n")

            print("✅ Created test documentation structure")

            repo_root = Path(__file__).resolve().parent
            subprocess.run([sys.executable, "-m", "pip", "install", "-e", str(repo_root)],
                           check=True, capture_output=True, text=True)
            result = subprocess.run([
                sys.executable,
                "-c",
                "from update_docs.core import update_content_system; print('✅ Package import successful')"
            ], check=True, capture_output=True, text=True)
            print(result.stdout.strip())

            subprocess.run([
                sys.executable, "-m", "update_docs.cli",
                "--docs", "docs",
                "--content-json", "content/Content.json",
                "--description-md", "content/Description_for_agents.md"
            ], check=True, capture_output=True, text=True)
            print("✅ CLI command executed successfully")

            content_json = test_repo / "content" / "Content.json"
            description_md = test_repo / "content" / "Description_for_agents.md"
            assert content_json.exists(), "Content.json not created"
            assert description_md.exists(), "Description_for_agents.md not created"
            print("✅ Generated files exist")

            with open(content_json, "r", encoding="utf-8") as f:
                content_data = json.load(f)

            assert isinstance(content_data, list), "Content.json is not a list"
            assert len(content_data) >= 3, "Content.json entries missing"
            for entry in content_data:
                for field in ["path", "title", "author", "editable", "file_id"]:
                    assert field in entry, f"Missing field '{field}'"

            print(f"✅ Content.json contains {len(content_data)} valid entries")

            description_content = description_md.read_text(encoding="utf-8")
            assert "# 📘 Структура документации проекта" in description_content
            assert "docs/README.md" in description_content
            print("✅ Description_for_agents.md contains expected content")

            new_file = docs_dir / "new_feature.md"
            new_file.write_text("# New Feature\n")

            subprocess.run([
                sys.executable, "-m", "update_docs.cli",
                "--docs", "docs",
                "--content-json", "content/Content.json",
                "--description-md", "content/Description_for_agents.md"
            ], check=True, capture_output=True)

            with open(content_json, "r", encoding="utf-8") as f:
                updated_content = json.load(f)
            assert len(updated_content) > len(content_data), "New file not detected in update"
            print("✅ File update detection works")
            print("🎉 All tests passed!")
        finally:
            os.chdir(orig_cwd)

if __name__ == "__main__":
    test_external_deployment()
