# 🚀 Руководство по развертыванию update-docs в других репозиториях

## 📦 Быстрая установка (Рекомендуется)

### Автоматическая настройка
```bash
# В целевом репозитории
pip install update-docs-system

# Скачиваем и запускаем скрипт автоматической настройки
curl -sSL https://raw.githubusercontent.com/CoreTwin/docs_repo/main/scripts/setup_automation.sh | bash
```

### Ручная настройка
```bash
# 1. Установка пакета
pip install update-docs-system

# 2. Создание структуры директорий
mkdir -p .github/workflows scripts content docs

# 3. Копирование шаблонов
python -c "
import pkg_resources
import shutil

# GitHub Actions
template = pkg_resources.resource_filename('update_docs', 'templates/github_workflow.yml')
shutil.copy(template, '.github/workflows/update-docs.yml')

# Pre-commit hook
template = pkg_resources.resource_filename('update_docs', 'templates/pre_commit_hook.sh')
shutil.copy(template, '.git/hooks/pre-commit')

# File watcher
template = pkg_resources.resource_filename('update_docs', 'templates/watch_docs.py')
shutil.copy(template, 'scripts/watch_docs.py')

# Makefile
template = pkg_resources.resource_filename('update_docs', 'templates/Makefile')
shutil.copy(template, 'Makefile')
"

# 4. Установка прав доступа
chmod +x .git/hooks/pre-commit
chmod +x scripts/watch_docs.py

# 5. Первоначальное обновление
update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
```

## 🎯 Способы использования

### 1. GitHub Actions (Автоматизация CI/CD)
- ✅ Автоматически срабатывает при push/PR с изменениями .md файлов
- ✅ Коммитит обновленную документацию
- ✅ Работает для всей команды

### 2. Pre-commit Hook (Локальная разработка)
- ✅ Обновляет документацию перед каждым коммитом
- ✅ Мгновенная обратная связь разработчику
- ✅ Предотвращает "забывание" обновить документацию

### 3. File Watcher (Активная разработка документации)
- ✅ Отслеживает изменения в реальном времени
- ✅ Идеально для написания документации
- ✅ Мгновенное обновление при сохранении файла

```bash
# Запуск file watcher
python scripts/watch_docs.py
```

### 4. Ручное обновление
```bash
# Обновление документации вручную
update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md

# Или через Makefile
make docs-update
```

## 📁 Структура файлов в целевом репозитории

```
target-repo/
├── .github/
│   └── workflows/
│       └── update-docs.yml          # GitHub Actions
├── scripts/
│   └── watch_docs.py                # File watcher
├── docs/                            # Документация
│   ├── README.md
│   ├── setup.md
│   └── api/
│       └── README.md
├── content/                         # Генерируемые файлы
│   ├── Content.json                 # Метаданные документации
│   └── Description_for_agents.md    # Описание для ИИ-агентов
├── Makefile                         # Команды автоматизации
└── .git/hooks/
    └── pre-commit                   # Pre-commit hook
```

## 🔧 Настройка параметров

### Изменение путей к документации
```bash
# Если документация находится не в папке docs/
update-docs --docs documentation --content-json meta/Content.json --description-md meta/Description.md
```

### Настройка GitHub Actions
Отредактируйте `.github/workflows/update-docs.yml`:
```yaml
# Изменить пути мониторинга
paths: 
  - 'documentation/**/*.md'  # Вместо docs/**/*
  - '**/*.md'

# Изменить команду обновления
run: |
  update-docs --docs documentation --content-json meta/Content.json --description-md meta/Description.md
```

## 🧪 Тестирование установки

### Проверка работоспособности
```bash
# 1. Создаем тестовый файл
echo "# Test Document" > docs/test.md
echo "This is a test." >> docs/test.md

# 2. Запускаем обновление
update-docs --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md

# 3. Проверяем результат
ls -la content/
cat content/Content.json

# 4. Удаляем тестовый файл
rm docs/test.md
```

### Проверка автоматизации
```bash
# Тест pre-commit hook
echo "# Another test" > docs/test2.md
git add docs/test2.md
git commit -m "Test commit"  # Должен автоматически обновить документацию

# Тест file watcher
python scripts/watch_docs.py &  # Запуск в фоне
echo "# Live test" > docs/test3.md  # Должно автоматически обновиться
```

## 🔒 Безопасность и права доступа

### .gitignore
```gitignore
# update-docs временные файлы
*.tmp
.update-docs-cache/

# Если не хотите коммитить метаданные (опционально)
# content/Content.json
# content/Description_for_agents.md
```

### GitHub Actions права
Убедитесь, что в `.github/workflows/update-docs.yml` есть:
```yaml
permissions:
  contents: write
  pull-requests: write
```

## 🆘 Устранение неполадок

### Проблема: "update-docs command not found"
```bash
# Решение 1: Переустановка
pip uninstall update-docs-system
pip install update-docs-system

# Решение 2: Использование Python модуля
python -c "from update_docs.core import update_content_system; update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')"
```

### Проблема: GitHub Actions не срабатывает
1. Проверьте права доступа в настройках репозитория
2. Убедитесь, что workflow файл находится в `.github/workflows/`
3. Проверьте синтаксис YAML файла

### Проблема: Pre-commit hook не работает
```bash
# Проверка прав доступа
ls -la .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Проверка содержимого
cat .git/hooks/pre-commit
```

## 📞 Поддержка

- **GitHub Issues**: https://github.com/CoreTwin/docs_repo/issues
- **Документация**: https://github.com/CoreTwin/docs_repo/blob/main/README.md
- **Примеры**: https://github.com/CoreTwin/docs_repo/tree/main/examples
