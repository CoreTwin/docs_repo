[Домой](../README.md) | [Назад](../content/Description_for_agents.md)

# ТЗ: Настройка системы автоматического обновления документации update-docs

## 🎯 Цель проекта

Настроить автоматическую систему обновления документации, которая будет срабатывать при изменении любых .md файлов в целевых репозиториях. Система должна быть полностью изолирована от кода целевых репозиториев и работать автономно.

## 📋 Техническое задание

### Основные требования:
- ✅ Автоматическое обновление при изменении .md файлов
- ✅ Полная изоляция кода update-docs от целевых репозиториев
- ✅ Поддержка GitHub Actions, pre-commit hooks и file watcher
- ✅ Простота развертывания в новых репозиториях
- ✅ Автоматическое управление версиями документации

### Архитектура решения:
1. **Исходный репозиторий** - содержит код update-docs и публикуется как PyPI пакет
2. **Целевые репозитории** - устанавливают пакет и настраивают автоматизацию
3. **Комбинированная система триггеров** - GitHub Actions + Pre-commit + File Watcher

---

## 🏗️ ЭТАП 1: Настройка исходного репозитория (update-docs)

### 1.1 Структура проекта

```
update-docs/
├── setup.py                           # Конфигурация пакета
├── pyproject.toml                      # Современная конфигурация
├── requirements.txt                    # Зависимости
├── README.md                          # Документация пакета
├── CHANGELOG.md                       # История изменений
├── update_docs/                       # Основной код
│   ├── __init__.py
│   ├── core.py
│   └── cli.py
├── templates/                         # Шаблоны для целевых репозиториев
│   ├── github_workflow.yml
│   ├── pre_commit_hook.sh
│   ├── watch_docs.py
│   ├── setup_automation.sh
│   └── Makefile
├── tests/                            # Тесты
├── docs/                            # Документация проекта
└── scripts/                         # Вспомогательные скрипты
    ├── build_and_publish.sh
    ├── create_templates.sh
    └── test_integration.sh
```

### 1.2 Создание setup.py

```python
# setup.py
from setuptools import setup, find_packages
import os

# Читаем README для long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Читаем requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="update-docs-system",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Комплексная система автоматизации документации для проектов с Markdown файлами",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/update-docs",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "update-docs=update_docs.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "update_docs": [
            "templates/*",
        ],
    },
)
```

### 1.3 Создание pyproject.toml

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "update-docs-system"
dynamic = ["version"]
description = "Комплексная система автоматизации документации"
readme = "README.md"
requires-python = ">=3.7"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["documentation", "markdown", "automation", "git"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Documentation",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]
dependencies = [
    "click>=8.0.0",
    "gitpython>=3.1.0",
    "watchdog>=2.1.0",
    "requests>=2.25.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "pytest-cov>=2.0",
    "black>=21.0",
    "flake8>=3.8",
    "mypy>=0.910",
]

[project.urls]
Homepage = "https://github.com/your-username/update-docs"
Documentation = "https://github.com/your-username/update-docs/blob/main/README.md"
Repository = "https://github.com/your-username/update-docs.git"
Issues = "https://github.com/your-username/update-docs/issues"

[project.scripts]
update-docs = "update_docs.cli:main"

[tool.setuptools_scm]
write_to = "update_docs/_version.py"
```

### 1.4 Создание шаблонов

#### `templates/github_workflow.yml`
```yaml
# GitHub Actions workflow для автоматического обновления документации
name: 📚 Auto Update Documentation

on:
  push:
    branches: [main, master, develop]
    paths: 
      - '**/*.md'
      - 'docs/**/*'
  pull_request:
    branches: [main, master, develop]
    paths:
      - '**/*.md'
      - 'docs/**/*'

jobs:
  update-docs:
    runs-on: ubuntu-latest
    
    steps:
    - name: 📥 Checkout repository
      uses: actions/checkout@v4
      with:
        fetch-depth: 0
        token: ${{ secrets.GITHUB_TOKEN }}
    
    - name: 🐍 Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        cache: 'pip'
    
    - name: 📦 Install update-docs-system
      run: |
        pip install update-docs-system
    
    - name: 🔍 Check for .md changes
      id: check_changes
      run: |
        if [ "${{ github.event_name }}" = "pull_request" ]; then
          # Для PR сравниваем с base branch
          CHANGED_FILES=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
        else
          # Для push сравниваем с предыдущим коммитом
          CHANGED_FILES=$(git diff --name-only HEAD~1 HEAD)
        fi
        
        if echo "$CHANGED_FILES" | grep -E '\\.md$'; then
          echo "md_changed=true" >> $GITHUB_OUTPUT
          echo "📝 Markdown files changed, updating documentation..."
          echo "Changed files:"
          echo "$CHANGED_FILES" | grep -E '\\.md$'
        else
          echo "md_changed=false" >> $GITHUB_OUTPUT
          echo "ℹ️  No markdown files changed"
        fi
    
    - name: 📚 Update documentation
      if: steps.check_changes.outputs.md_changed == 'true'
      run: |
        update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
        echo "✅ Documentation updated successfully"
    
    - name: 💾 Commit updated documentation
      if: steps.check_changes.outputs.md_changed == 'true'
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action Bot"
        
        # Создаем директории если они не существуют
        mkdir -p content
        
        git add content/Content.json content/Description_for_agents.md docs/ || true
        
        if git diff --staged --quiet; then
          echo "ℹ️  No changes to commit"
        else
          git commit -m "📚 Auto-update documentation
          
          - Updated Content.json index
          - Refreshed Description_for_agents.md
          - Added navigation links
          
          Triggered by: ${{ github.event.head_commit.message || 'PR update' }}"
          
          # Пушим только если это не PR
          if [ "${{ github.event_name }}" != "pull_request" ]; then
            git push
            echo "✅ Documentation committed and pushed"
          else
            echo "ℹ️  PR mode: changes staged but not pushed"
          fi
        fi
    
    - name: 📊 Summary
      if: steps.check_changes.outputs.md_changed == 'true'
      run: |
        echo "## 📚 Documentation Update Summary" >> $GITHUB_STEP_SUMMARY
        echo "- ✅ Content.json updated" >> $GITHUB_STEP_SUMMARY
        echo "- ✅ Description_for_agents.md refreshed" >> $GITHUB_STEP_SUMMARY
        echo "- ✅ Navigation links added" >> $GITHUB_STEP_SUMMARY
        echo "- 🔗 [View Content.json](content/Content.json)" >> $GITHUB_STEP_SUMMARY
        echo "- 🔗 [View Description for Agents](content/Description_for_agents.md)" >> $GITHUB_STEP_SUMMARY
```

#### `templates/pre_commit_hook.sh`
```bash
#!/bin/bash
# Pre-commit hook для автоматического обновления документации

echo "🔍 Checking for markdown file changes..."

# Получаем список измененных .md файлов
md_files_changed=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.md$' || true)

if [ -n "$md_files_changed" ]; then
    echo "📝 Markdown files changed:"
    echo "$md_files_changed" | sed 's/^/  - /'
    echo ""
    echo "🔄 Updating documentation..."
    
    # Создаем необходимые директории
    mkdir -p content
    
    # Запускаем update-docs
    if command -v update-docs &> /dev/null; then
        update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
        update_result=$?
    else
        echo "⚠️  update-docs command not found, trying Python import..."
        python3 -c "
try:
    from update_docs.core import update_content_system
    update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
    print('✅ Documentation updated via Python import')
except ImportError as e:
    print(f'❌ Failed to import update_docs: {e}')
    print('💡 Please install: pip install update-docs-system')
    exit(1)
except Exception as e:
    print(f'❌ Error updating documentation: {e}')
    exit(1)
"
        update_result=$?
    fi
    
    if [ $update_result -eq 0 ]; then
        # Добавляем обновленные файлы в коммит
        git add content/Content.json content/Description_for_agents.md docs/ 2>/dev/null || true
        echo "✅ Documentation updated and staged"
    else
        echo "❌ Failed to update documentation"
        echo "💡 Please check that update-docs-system is installed:"
        echo "   pip install update-docs-system"
        exit 1
    fi
else
    echo "ℹ️  No markdown files changed, skipping documentation update"
fi

echo "🚀 Pre-commit check completed"
```

#### `templates/watch_docs.py`
```python
#!/usr/bin/env python3
"""
File Watcher для автоматического обновления документации при изменении .md файлов
Запуск: python watch_docs.py
"""

import os
import sys
import time
import threading
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MarkdownHandler(FileSystemEventHandler):
    def __init__(self, docs_dir="docs", content_json="content/Content.json", description_md="content/Description_for_agents.md"):
        self.docs_dir = docs_dir
        self.content_json = content_json
        self.description_md = description_md
        self.last_update = 0
        self.update_delay = 2  # Задержка в секундах для группировки изменений
        self.update_thread = None
        
        # Создаем необходимые директории
        Path(content_json).parent.mkdir(parents=True, exist_ok=True)
        
    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.md'):
            self.schedule_update(event.src_path, "modified")
    
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.md'):
            self.schedule_update(event.src_path, "created")
    
    def on_deleted(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.md'):
            self.schedule_update(event.src_path, "deleted")
    
    def on_moved(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.md') or event.dest_path.endswith('.md'):
            self.schedule_update(f"{event.src_path} -> {event.dest_path}", "moved")
    
    def schedule_update(self, file_path, action):
        """Планируем обновление с задержкой для группировки изменений"""
        current_time = time.time()
        self.last_update = current_time
        
        print(f"📝 Detected {action}: {file_path}")
        
        # Отменяем предыдущий таймер если он есть
        if self.update_thread and self.update_thread.is_alive():
            return
        
        # Запускаем новый таймер
        self.update_thread = threading.Timer(self.update_delay, self.update_documentation)
        self.update_thread.start()
    
    def update_documentation(self):
        """Обновляем документацию"""
        try:
            print("🔄 Updating documentation...")
            
            # Импортируем и запускаем update-docs
            try:
                from update_docs.core import update_content_system
                update_content_system(self.docs_dir, self.content_json, self.description_md)
                
                print("✅ Documentation updated successfully")
                print(f"📋 Updated: {self.content_json}")
                print(f"📖 Updated: {self.description_md}")
                
            except ImportError:
                print("❌ update_docs module not found")
                print("💡 Please install: pip install update-docs-system")
                return
                
        except Exception as e:
            print(f"❌ Error updating documentation: {e}")
            
        finally:
            print("=" * 60)

def main():
    print("👀 Starting documentation watcher...")
    print("🔍 Monitoring .md files for changes...")
    print("📁 Current directory:", os.getcwd())
    print("⏹️  Press Ctrl+C to stop")
    print("=" * 60)
    
    # Проверяем наличие необходимых модулей
    try:
        from update_docs.core import update_content_system
        print("✅ update-docs-system module found")
    except ImportError:
        print("⚠️  update-docs-system not found")
        print("💡 Please install: pip install update-docs-system")
        print("🔄 Watcher will still monitor files, but updates will fail")
        print("=" * 60)
    
    # Создаем обработчик событий
    event_handler = MarkdownHandler()
    
    # Создаем наблюдателя
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    
    # Запускаем наблюдение
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping documentation watcher...")
        observer.stop()
    
    observer.join()
    print("✅ Documentation watcher stopped")

if __name__ == "__main__":
    main()
```

#### `templates/setup_automation.sh`
```bash
#!/bin/bash
# Скрипт автоматической настройки update-docs в целевом репозитории

set -e  # Прекращаем выполнение при ошибке

echo "🚀 Setting up update-docs automation..."
echo "📁 Current directory: $(pwd)"
echo ""

# Функция для вывода статуса
print_status() {
    echo "✅ $1"
}

print_warning() {
    echo "⚠️  $1"
}

print_error() {
    echo "❌ $1"
}

# Проверяем, что мы в git репозитории
if [ ! -d ".git" ]; then
    print_error "This is not a git repository!"
    echo "💡 Please run this script from the root of your git repository"
    exit 1
fi

print_status "Git repository detected"

# 1. Устанавливаем update-docs-system
echo "📦 Installing update-docs-system..."
if pip install update-docs-system; then
    print_status "update-docs-system installed"
else
    print_error "Failed to install update-docs-system"
    echo "💡 Please check your Python/pip installation"
    exit 1
fi

# 2. Создаем необходимые директории
echo "📁 Creating directories..."
mkdir -p .github/workflows
mkdir -p scripts
mkdir -p content
mkdir -p docs

print_status "Directories created"

# 3. Проверяем наличие docs директории с файлами
if [ ! "$(ls -A docs)" ]; then
    echo "📝 Creating sample documentation..."
    cat > docs/README.md << 'EOF'
# Project Documentation

Welcome to the project documentation!

## Getting Started

This documentation is automatically managed by update-docs-system.

## Contents

- [Setup Guide](setup.md)
- [API Reference](api/README.md)

---
[🏠 Home](../README.md)
EOF

    mkdir -p docs/api
    cat > docs/api/README.md << 'EOF'
# API Reference

This section contains API documentation.

## Endpoints

- GET /api/health
- POST /api/data

---
[🏠 Home](../../README.md) | [⬆️ Back](../README.md)
EOF

    cat > docs/setup.md << 'EOF'
# Setup Guide

Instructions for setting up the project.

## Prerequisites

- Python 3.7+
- Git

## Installation

1. Clone the repository
2. Install dependencies
3. Run the application

---
[🏠 Home](../README.md) | [⬆️ Back](README.md)
EOF

    print_status "Sample documentation created"
fi

# 4. Копируем GitHub Actions workflow
echo "⚙️  Setting up GitHub Actions..."
cat > .github/workflows/update-docs.yml << 'EOF'
name: 📚 Auto Update Documentation

on:
  push:
    branches: [main, master, develop]
    paths: 
      - '**/*.md'
      - 'docs/**/*'
  pull_request:
    branches: [main, master, develop]
    paths:
      - '**/*.md'
      - 'docs/**/*'

jobs:
  update-docs:
    runs-on: ubuntu-latest
    
    steps:
    - name: 📥 Checkout repository
      uses: actions/checkout@v4
      with:
        fetch-depth: 0
        token: ${{ secrets.GITHUB_TOKEN }}
    
    - name: 🐍 Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        cache: 'pip'
    
    - name: 📦 Install update-docs-system
      run: |
        pip install update-docs-system
    
    - name: 🔍 Check for .md changes
      id: check_changes
      run: |
        if [ "${{ github.event_name }}" = "pull_request" ]; then
          CHANGED_FILES=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
        else
          CHANGED_FILES=$(git diff --name-only HEAD~1 HEAD 2>/dev/null || echo "")
        fi
        
        if echo "$CHANGED_FILES" | grep -E '\\.md$'; then
          echo "md_changed=true" >> $GITHUB_OUTPUT
          echo "📝 Markdown files changed, updating documentation..."
        else
          echo "md_changed=false" >> $GITHUB_OUTPUT
          echo "ℹ️  No markdown files changed"
        fi
    
    - name: 📚 Update documentation
      if: steps.check_changes.outputs.md_changed == 'true'
      run: |
        update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
        echo "✅ Documentation updated successfully"
    
    - name: 💾 Commit updated documentation
      if: steps.check_changes.outputs.md_changed == 'true'
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action Bot"
        
        mkdir -p content
        git add content/Content.json content/Description_for_agents.md docs/ || true
        
        if git diff --staged --quiet; then
          echo "ℹ️  No changes to commit"
        else
          git commit -m "📚 Auto-update documentation"
          
          if [ "${{ github.event_name }}" != "pull_request" ]; then
            git push
            echo "✅ Documentation committed and pushed"
          fi
        fi
EOF

print_status "GitHub Actions workflow created"

# 5. Устанавливаем pre-commit hook
echo "🪝 Setting up pre-commit hook..."
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
echo "🔍 Checking for markdown file changes..."

md_files_changed=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.md$' || true)

if [ -n "$md_files_changed" ]; then
    echo "📝 Markdown files changed:"
    echo "$md_files_changed" | sed 's/^/  - /'
    echo ""
    echo "🔄 Updating documentation..."
    
    mkdir -p content
    
    if command -v update-docs &> /dev/null; then
        update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
        update_result=$?
    else
        python3 -c "
try:
    from update_docs.core import update_content_system
    update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
    print('✅ Documentation updated via Python import')
except Exception as e:
    print(f'❌ Error: {e}')
    exit(1)
"
        update_result=$?
    fi
    
    if [ $update_result -eq 0 ]; then
        git add content/Content.json content/Description_for_agents.md docs/ 2>/dev/null || true
        echo "✅ Documentation updated and staged"
    else
        echo "❌ Failed to update documentation"
        exit 1
    fi
else
    echo "ℹ️  No markdown files changed, skipping documentation update"
fi
EOF

chmod +x .git/hooks/pre-commit
print_status "Pre-commit hook installed"

# 6. Создаем file watcher скрипт
echo "👀 Setting up file watcher..."
pip install watchdog

cat > scripts/watch_docs.py << 'EOF'
#!/usr/bin/env python3
import os
import sys
import time
import threading
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MarkdownHandler(FileSystemEventHandler):
    def __init__(self, docs_dir="docs", content_json="content/Content.json", description_md="content/Description_for_agents.md"):
        self.docs_dir = docs_dir
        self.content_json = content_json
        self.description_md = description_md
        self.last_update = 0
        self.update_delay = 2
        self.update_thread = None
        Path(content_json).parent.mkdir(parents=True, exist_ok=True)
        
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith('.md'):
            return
        self.schedule_update(event.src_path, "modified")
    
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith('.md'):
            return
        self.schedule_update(event.src_path, "created")
    
    def on_deleted(self, event):
        if event.is_directory or not event.src_path.endswith('.md'):
            return
        self.schedule_update(event.src_path, "deleted")
    
    def schedule_update(self, file_path, action):
        current_time = time.time()
        self.last_update = current_time
        
        print(f"📝 Detected {action}: {file_path}")
        
        if self.update_thread and self.update_thread.is_alive():
            return
        
        self.update_thread = threading.Timer(self.update_delay, self.update_documentation)
        self.update_thread.start()
    
    def update_documentation(self):
        try:
            print("🔄 Updating documentation...")
            from update_docs.core import update_content_system
            update_content_system(self.docs_dir, self.content_json, self.description_md)
            print("✅ Documentation updated successfully")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            print("=" * 60)

def main():
    print("👀 Starting documentation watcher...")
    print("🔍 Monitoring .md files for changes...")
    print("⏹️  Press Ctrl+C to stop")
    print("=" * 60)
    
    event_handler = MarkdownHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping watcher...")
        observer.stop()
    
    observer.join()
    print("✅ Watcher stopped")

if __name__ == "__main__":
    main()
EOF

chmod +x scripts/watch_docs.py
print_status "File watcher created"

# 7. Создаем Makefile для удобства
echo "🔧 Creating Makefile..."
cat > Makefile << 'EOF'
.PHONY: docs-update docs-watch docs-install help

help:
	@echo "📚 Documentation Commands:"
	@echo "  docs-install  - Install update-docs-system"
	@echo "  docs-update   - Update documentation once"
	@echo "  docs-watch    - Start file watcher for live updates"

docs-install:
	@echo "📦 Installing update-docs-system..."
	@pip install update-docs-system

docs-update:
	@echo "📚 Updating documentation..."
	@update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
	@echo "✅ Documentation updated"

docs-watch:
	@echo "👀 Starting documentation watcher..."
	@python scripts/watch_docs.py
EOF

print_status "Makefile created"

# 8. Создаем .gitignore записи (если файл существует)
if [ -f ".gitignore" ]; then
    if ! grep -q "# update-docs" .gitignore; then
        echo "" >> .gitignore
        echo "# update-docs temporary files" >> .gitignore
        echo "*.tmp" >> .gitignore
        echo ".update-docs-cache/" >> .gitignore
        print_status "Added entries to .gitignore"
    fi
else
    cat > .gitignore << 'EOF'
# update-docs temporary files
*.tmp
.update-docs-cache/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
EOF
    print_status "Created .gitignore"
fi

# 9. Запускаем первоначальное обновление документации
echo "🔄 Running initial documentation update..."
if update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md; then
    print_status "Initial documentation generated"
else
    print_warning "Initial update failed, but setup is complete"
fi

# Финальный отчет
echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📋