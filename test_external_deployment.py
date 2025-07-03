#!/usr/bin/env python3
"""
Тест интеграции для проверки развертывания update-docs в внешних репозиториях
"""

import os
import sys
import tempfile
import shutil
import subprocess
import json
from pathlib import Path

def test_external_deployment():
    """Тестирует полный цикл развертывания в тестовом репозитории"""
    print("🧪 Testing external deployment...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        test_repo = Path(temp_dir) / "test_repo"
        test_repo.mkdir()
        
        os.chdir(test_repo)
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], check=True)
        subprocess.run(["git", "config", "user.name", "Test User"], check=True)
        
        print(f"✅ Created test repository: {test_repo}")
        
        docs_dir = test_repo / "docs"
        docs_dir.mkdir()
        
        (docs_dir / "README.md").write_text("""# Test Project

This is a test project for update-docs integration.


- Automatic documentation updates
- Content.json generation
- Navigation links
""")
        
        (docs_dir / "setup.md").write_text("""# Setup Guide

Instructions for setting up the test project.


- Python 3.7+
- Git
""")
        
        api_dir = docs_dir / "api"
        api_dir.mkdir()
        (api_dir / "README.md").write_text("""# API Reference

API documentation for the test project.


- GET /api/test
- POST /api/data
""")
        
        print("✅ Created test documentation structure")
        
        try:
            result = subprocess.run([
                sys.executable, "-c", 
                "from update_docs.core import update_content_system; print('✅ Package import successful')"
            ], check=True, capture_output=True, text=True)
            print(result.stdout.strip())
        except subprocess.CalledProcessError as e:
            print(f"❌ Package import failed: {e}")
            return False
        
        try:
            result = subprocess.run([
                sys.executable, "-m", "update_docs.cli",
                "--docs", "docs",
                "--content-json", "content/Content.json",
                "--description-md", "content/Description_for_agents.md"
            ], check=True, capture_output=True, text=True, cwd=test_repo)
            print("✅ CLI command executed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ CLI command failed: {e}")
            print(f"stdout: {e.stdout}")
            print(f"stderr: {e.stderr}")
            return False
        
        content_json = test_repo / "content" / "Content.json"
        description_md = test_repo / "content" / "Description_for_agents.md"
        
        if not content_json.exists():
            print("❌ Content.json not created")
            return False
        
        if not description_md.exists():
            print("❌ Description_for_agents.md not created")
            return False
        
        print("✅ Generated files exist")
        
        try:
            with open(content_json, 'r', encoding='utf-8') as f:
                content_data = json.load(f)
            
            if not isinstance(content_data, list):
                print("❌ Content.json is not a list")
                return False
            
            if len(content_data) < 3:
                print(f"❌ Expected at least 3 files, got {len(content_data)}")
                return False
            
            for entry in content_data:
                required_fields = ['path', 'title', 'author', 'editable', 'file_id']
                for field in required_fields:
                    if field not in entry:
                        print(f"❌ Missing field '{field}' in Content.json entry")
                        return False
            
            print(f"✅ Content.json contains {len(content_data)} valid entries")
            
        except Exception as e:
            print(f"❌ Error reading Content.json: {e}")
            return False
        
        try:
            description_content = description_md.read_text(encoding='utf-8')
            
            if "# Описание документации проекта" not in description_content:
                print("❌ Description_for_agents.md missing main header")
                return False
            
            if "docs/README.md" not in description_content:
                print("❌ Description_for_agents.md missing file references")
                return False
            
            print("✅ Description_for_agents.md contains expected content")
            
        except Exception as e:
            print(f"❌ Error reading Description_for_agents.md: {e}")
            return False
        
        print("🔄 Testing file update...")
        
        new_file = docs_dir / "new_feature.md"
        new_file.write_text("""# New Feature

Documentation for a new feature.
""")
        
        try:
            subprocess.run([
                sys.executable, "-m", "update_docs.cli",
                "--docs", "docs",
                "--content-json", "content/Content.json",
                "--description-md", "content/Description_for_agents.md"
            ], check=True, capture_output=True, cwd=test_repo)
            
            with open(content_json, 'r', encoding='utf-8') as f:
                updated_content = json.load(f)
            
            if len(updated_content) <= len(content_data):
                print("❌ New file not detected in update")
                return False
            
            print("✅ File update detection works")
            
        except Exception as e:
            print(f"❌ Update test failed: {e}")
            return False
        
        print("🎉 All tests passed!")
        return True

if __name__ == "__main__":
    success = test_external_deployment()
    sys.exit(0 if success else 1)
