[Домой](../README.md) | [Назад](../content/Description_for_agents.md)

# Руководство по развертыванию update-docs в других репозиториях

## 🎯 Способы развертывания

### 1. 📦 Установка как Python пакет (Рекомендуется)

#### Вариант 1.1: Через pip + Git
```bash
# В целевом репозитории
pip install git+https://github.com/your-username/update-docs.git

# Использование
python -c "
from update_docs.core import update_content_system
update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
"
```

#### Вариант 1.2: Создание PyPI пакета
```bash
# В репозитории update-docs
python setup.py sdist bdist_wheel
twine upload dist/*

# В целевом репозитории
pip install update-docs
```

**setup.py для update-docs:**
```python
from setuptools import setup, find_packages

setup(
    name="update-docs",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "json5",
        "gitpython",
        "difflib",
    ],
    entry_points={
        'console_scripts': [
            'update-docs=update_docs.cli:main',
        ],
    },
    author="Your Name",
    description="Комплексная система автоматизации документации",
    python_requires=">=3.7",
)
```

### 2. 🔧 Git Submodule

#### Настройка:
```bash
# В целевом репозитории
git submodule add https://github.com/your-username/update-docs.git tools/update-docs
git submodule update --init --recursive

# Добавить в .gitignore целевого репозитория
echo "tools/update-docs/" >> .gitignore
```

#### Использование:
```bash
# Скрипт запуска (update_docs.sh)
#!/bin/bash
cd tools/update-docs
python -m update_docs.cli --docs ../../docs --content-json ../../content/Content.json --description-md ../../content/Description_for_agents.md
cd ../..
```

### 3. 🐳 Docker контейнер

#### Dockerfile для update-docs:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY update_docs/ ./update_docs/
COPY *.py ./

VOLUME ["/workspace"]
WORKDIR /workspace

ENTRYPOINT ["python", "/app/update_docs/cli.py"]
```

#### Использование:
```bash
# Сборка образа (в репозитории update-docs)
docker build -t update-docs:latest .

# Использование в целевом репозитории
docker run --rm -v $(pwd):/workspace update-docs:latest \
  --docs docs \
  --content-json content/Content.json \
  --description-md content/Description_for_agents.md
```

### 4. 📋 GitHub Actions Workflow

#### `.github/workflows/update-docs.yml` в целевом репозитории:
```yaml
name: Update Documentation

on:
  push:
    branches: [main, develop]
    paths: ['docs/**']
  pull_request:
    paths: ['docs/**']

jobs:
  update-docs:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install update-docs
      run: pip install git+https://github.com/your-username/update-docs.git

    - name: Update documentation
      run: |
        python -c "
        from update_docs.core import update_content_system
        update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
        "

    - name: Commit changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add content/
        git diff --staged --quiet || git commit -m "📚 Auto-update documentation"
        git push
```

### 5. 🛠️ Локальный инструмент разработчика

#### Создание глобальной команды:
```bash
# В репозитории update-docs
pip install -e .

# Теперь доступно глобально
update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
```

#### Или через alias:
```bash
# В ~/.bashrc или ~/.zshrc
alias update-docs='python /path/to/update-docs/update_docs/cli.py'

# Использование в любом репозитории
cd /path/to/target-repo
update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
```

## 🚀 Рекомендуемые конфигурации

### Для команды разработчиков:
1. **PyPI пакет** + **GitHub Actions** для автоматизации
2. **Pre-commit hooks** для локальной проверки

### Для личных проектов:
1. **Git Submodule** + **локальные скрипты**
2. **Docker контейнер** для изоляции

### Для CI/CD интеграции:
1. **Docker образ** в registry
2. **GitHub Actions** с кешированием

## 📁 Структура файлов в целевом репозитории

```
target-repo/
├── docs/                    # Документация проекта
│   ├── README.md
│   ├── api/
│   └── guides/
├── content/                 # Метаданные документации
│   ├── Content.json        # Генерируется update-docs
│   └── Description_for_agents.md  # Генерируется update-docs
├── .github/
│   └── workflows/
│       └── update-docs.yml  # CI/CD для документации
├── scripts/
│   └── update_docs.sh       # Локальный скрипт запуска
└── .gitignore              # Исключить временные файлы
```

## 🔒 Настройка безопасности

### .gitignore для целевого репозитория:
```gitignore
# update-docs временные файлы
*.tmp
.update-docs-cache/
tools/update-docs/

# Метаданные (если не нужны в репозитории)
# content/Content.json
# content/Description_for_agents.md
```

### Права доступа для GitHub Actions:
```yaml
permissions:
  contents: write
  pull-requests: write
```

## 🧪 Тестирование интеграции

### Скрипт проверки интеграции:
```bash
#!/bin/bash
# test_integration.sh

echo "🧪 Тестирование интеграции update-docs..."

# Проверка установки
if ! command -v update-docs &> /dev/null; then
    echo "❌ update-docs не установлен"
    exit 1
fi

# Создание тестовой структуры
mkdir -p test-docs/guides
echo "# Test" > test-docs/README.md
echo "# Guide" > test-docs/guides/setup.md

# Тестовый запуск
update-docs --docs test-docs --content-json test-content.json --description-md test-description.md

# Проверка результатов
if [[ -f "test-content.json" && -f "test-description.md" ]]; then
    echo "✅ Интеграция работает корректно"
    rm -rf test-docs test-content.json test-description.md
    exit 0
else
    echo "❌ Ошибка интеграции"
    exit 1
fi
```

## 📋 Checklist для внедрения

- [ ] Выбрать способ развертывания
- [ ] Настроить структуру папок в целевом репозитории
- [ ] Создать скрипты автоматизации
- [ ] Настроить CI/CD (опционально)
- [ ] Протестировать интеграцию
- [ ] Обновить .gitignore
- [ ] Документировать процесс для команды

## 🎯 Итог

Наиболее универсальный подход:
1. **Разработка** → PyPI пакет + локальная установка
2. **Продакшн** → GitHub Actions + Docker контейнер
3. **Команда** → Pre-commit hooks + общие скрипты

Это обеспечивает максимальную гибкость и изоляцию кода.

# 🎯 Лучший подход - Комбинированный
1. GitHub Actions (для CI/CD):

- Срабатывает при push/PR с изменениями .md файлов
- Автоматически коммитит обновленную документацию
- Работает для всей команды

2. Pre-commit Hook (для локальной разработки):

- Обновляет документацию перед каждым коммитом
- Мгновенная обратная связь разработчику
- Предотвращает "забывание" обновить документацию

3. File Watcher (для активной разработки):

- Отслеживает изменения в реальном времени
- Идеально для написания документации
- Мгновенное обновление при сохранении файла

🚀 Быстрая настройка

```Bash
# В целевом репозитории

mkdir -p .github/workflows scripts

# 1. Копируем GitHub Actions workflow
# (из артефакта выше)

# 2. Настраиваем pre-commit hook

chmod +x scripts/setup_hooks.sh
./scripts/setup_hooks.sh

# 3. Для разработки документации

pip install watchdog
python watch_docs.py
```
🔧 Какой способ выбрать?

Только GitHub Actions - если команда работает через PR

GitHub Actions + Pre-commit - для большинства проектов

**Все три способа** - для проектов с активной разработкой документации