[Домой](../README.md) | [Назад](../content/Description_for_agents.md)

# Автоматический запуск update-docs при изменении .md файлов

## 🎯 Способы автоматического запуска

### 1. 🔄 GitHub Actions (CI/CD) - Рекомендуется

#### `.github/workflows/update-docs.yml`
```yaml
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

    - name: 📦 Install update-docs
      run: |
        pip install git+https://github.com/your-username/update-docs.git

    - name: 🔍 Check for .md changes
      id: check_changes
      run: |
        if git diff --name-only HEAD~1 HEAD | grep -E '\\.md$'; then
          echo "md_changed=true" >> $GITHUB_OUTPUT
          echo "📝 Markdown files changed, updating documentation..."
        else
          echo "md_changed=false" >> $GITHUB_OUTPUT
          echo "ℹ️  No markdown files changed"
        fi

    - name: 📚 Update documentation
      if: steps.check_changes.outputs.md_changed == 'true'
      run: |
        python -c "
        from update_docs.core import update_content_system
        update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
        print('✅ Documentation updated successfully')
        "

    - name: 💾 Commit updated documentation
      if: steps.check_changes.outputs.md_changed == 'true'
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action Bot"
        git add content/Content.json content/Description_for_agents.md docs/

        if git diff --staged --quiet; then
          echo "ℹ️  No changes to commit"
        else
          git commit -m "📚 Auto-update documentation

          - Updated Content.json index
          - Refreshed Description_for_agents.md
          - Added navigation links

          Triggered by: ${{ github.event.head_commit.message }}"
          git push
          echo "✅ Documentation committed and pushed"
        fi

    - name: 📊 Summary
      if: steps.check_changes.outputs.md_changed == 'true'
      run: |
        echo "## 📚 Documentation Update Summary" >> $GITHUB_STEP_SUMMARY
        echo "- ✅ Content.json updated" >> $GITHUB_STEP_SUMMARY
        echo "- ✅ Description_for_agents.md refreshed" >> $GITHUB_STEP_SUMMARY
        echo "- ✅ Navigation links added" >> $GITHUB_STEP_SUMMARY
        echo "- 🔗 [View Content.json](content/Content.json)" >> $GITHUB_STEP_SUMMARY
```

### 2. 🪝 Git Pre-commit Hook (Локальная автоматизация)

#### `.git/hooks/pre-commit`
```bash
#!/bin/bash
# Pre-commit hook для автоматического обновления документации

echo "🔍 Checking for markdown file changes..."

# Проверяем изменения в .md файлах
md_files_changed=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.md$' || true)

if [ -n "$md_files_changed" ]; then
    echo "📝 Markdown files changed:"
    echo "$md_files_changed"
    echo ""
    echo "🔄 Updating documentation..."

    # Запускаем update-docs
    if command -v update-docs &> /dev/null; then
        update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
    else
        python -c "
from update_docs.core import update_content_system
update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
"
    fi

    # Добавляем обновленные файлы в коммит
    git add content/Content.json content/Description_for_agents.md docs/

    echo "✅ Documentation updated and staged"
else
    echo "ℹ️  No markdown files changed, skipping documentation update"
fi

echo "🚀 Pre-commit check completed"
```

#### Установка pre-commit hook:
```bash
# Создание скрипта установки setup_hooks.sh
#!/bin/bash
echo "📦 Setting up git hooks for update-docs..."

# Копируем pre-commit hook
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Устанавливаем update-docs если нужно
if ! command -v update-docs &> /dev/null; then
    echo "📥 Installing update-docs..."
    pip install git+https://github.com/your-username/update-docs.git
fi

echo "✅ Git hooks configured successfully"
echo "📚 Documentation will auto-update on each commit with .md changes"
```

### 3. 👀 File Watcher (Режим разработки)

#### Python file watcher скрипт `watch_docs.py`:
```python
#!/usr/bin/env python3
"""
Автоматический watcher для обновления документации при изменении .md файлов
"""

import os
import time
import subprocess
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

    def on_modified(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith('.md'):
            self.schedule_update(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith('.md'):
            self.schedule_update(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith('.md'):
            self.schedule_update(event.src_path)

    def schedule_update(self, file_path):
        """Планируем обновление с задержкой для группировки изменений"""
        current_time = time.time()
        self.last_update = current_time

        print(f"📝 Detected change in: {file_path}")

        # Ждем, чтобы сгруппировать изменения
        time.sleep(self.update_delay)

        # Проверяем, не было ли новых изменений
        if current_time == self.last_update:
            self.update_documentation()

    def update_documentation(self):
        """Обновляем документацию"""
        try:
            print("🔄 Updating documentation...")

            # Импортируем и запускаем update-docs
            from update_docs.core import update_content_system
            update_content_system(self.docs_dir, self.content_json, self.description_md)

            print("✅ Documentation updated successfully")
            print(f"📋 Updated: {self.content_json}")
            print(f"📖 Updated: {self.description_md}")
            print("=" * 50)

        except Exception as e:
            print(f"❌ Error updating documentation: {e}")

def main():
    print("👀 Starting documentation watcher...")
    print("🔍 Monitoring .md files for changes...")
    print("⏹️  Press Ctrl+C to stop")
    print("=" * 50)

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

#### Установка зависимостей для watcher:
```bash
pip install watchdog

# Запуск watcher
python watch_docs.py
```

### 4. 🔧 Make/Task Runner интеграция

#### `Makefile`:
```makefile
# Makefile для автоматизации документации

.PHONY: docs-watch docs-update docs-install

# Установка update-docs
docs-install:
	@echo "📦 Installing update-docs..."
	@pip install git+https://github.com/your-username/update-docs.git

# Однократное обновление документации
docs-update:
	@echo "📚 Updating documentation..."
	@python -c "from update_docs.core import update_content_system; update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')"
	@echo "✅ Documentation updated"

# Запуск watcher режима
docs-watch:
	@echo "👀 Starting documentation watcher..."
	@python watch_docs.py

# Автоматическое обновление при изменении любого .md файла
docs-auto: docs/*.md
	@$(MAKE) docs-update
```

#### Использование:
```bash
# Установка
make docs-install

# Однократное обновление
make docs-update

# Запуск watcher режима
make docs-watch
```

### 5. 🐳 Docker + Volume Monitoring

#### `docker-compose.yml`:
```yaml
version: '3.8'

services:
  docs-watcher:
    build:
      context: .
      dockerfile: Dockerfile.docs-watcher
    volumes:
      - ./docs:/workspace/docs
      - ./content:/workspace/content
    environment:
      - DOCS_DIR=docs
      - CONTENT_JSON=content/Content.json
      - DESCRIPTION_MD=content/Description_for_agents.md
    restart: unless-stopped
```

#### `Dockerfile.docs-watcher`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Устанавливаем зависимости
RUN pip install watchdog git+https://github.com/your-username/update-docs.git

# Копируем watcher скрипт
COPY watch_docs.py .

WORKDIR /workspace

CMD ["python", "/app/watch_docs.py"]
```

## 🚀 Рекомендуемая настройка

### Для команды разработчиков:
```bash
# 1. Установить GitHub Actions для автоматизации в CI/CD
cp .github/workflows/update-docs.yml .github/workflows/

# 2. Настроить pre-commit hook для локальной разработки
chmod +x scripts/setup_hooks.sh
./scripts/setup_hooks.sh

# 3. Для активной разработки документации
pip install watchdog
python watch_docs.py
```

### Структура файлов в целевом репозитории:
```
target-repo/
├── .github/
│   └── workflows/
│       └── update-docs.yml          # GitHub Actions
├── scripts/
│   ├── pre-commit                   # Pre-commit hook
│   ├── setup_hooks.sh               # Установка hooks
│   └── watch_docs.py                # File watcher
├── docs/                            # Документация
├── content/                         # Генерируемые файлы
│   ├── Content.json
│   └── Description_for_agents.md
└── Makefile                         # Автоматизация команд
```

## 🧪 Тестирование автоматизации

### Тестовый скрипт `test_automation.sh`:
```bash
#!/bin/bash
echo "🧪 Testing documentation automation..."

# Создаем тестовый файл
echo "# Test Document" > docs/test.md
echo "This is a test document." >> docs/test.md

# Ждем секунду
sleep 1

# Проверяем, обновились ли файлы
if [[ -f "content/Content.json" ]]; then
    echo "✅ Content.json updated"
else
    echo "❌ Content.json not found"
fi

if [[ -f "content/Description_for_agents.md" ]]; then
    echo "✅ Description_for_agents.md updated"
else
    echo "❌ Description_for_agents.md not found"
fi

# Удаляем тестовый файл
rm docs/test.md

echo "🎯 Test completed"
```

## 📋 Итоговые рекомендации

**Для максимальной автоматизации используйте комбинацию:**

1. **GitHub Actions** - для CI/CD автоматизации
2. **Pre-commit hooks** - для локальной разработки
3. **File watcher** - для активной разработки документации

Это обеспечит обновление документации на всех этапах разработки! 🚀

## 🎯 Оптимальное решение
1. Создание PyPI пакета - самый чистый способ:

```Bash
# В репозитории update-docs создайте setup.py
pip install build
python -m build
pip install dist/update_docs-1.0.0-py3-none-any.whl
```
2. Использование в любом репозитории:
```bash
# Установка один раз
pip install git+https://github.com/your-username/update-docs.git

# Использование в любом проекте
cd /path/to/your-project
python -c "
from update_docs.core import update_content_system
update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
"
```

## 🔧 Альтернативные варианты

Если не хотите устанавливать глобально - используйте Git Submodule:

```bash
# В целевом репозитории
git submodule add https://github.com/your-username/update-docs.git tools/update-docs
echo "tools/" >> .gitignore  # Чтобы не коммитить
```

Для CI/CD - Docker контейнер обеспечит полную изоляцию.