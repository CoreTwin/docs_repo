# update-docs

Комплексная система автоматизации документации для проектов с Markdown файлами. Инструмент обеспечивает автоматическое сканирование, структурирование, навигацию и защиту документации с интеллектуальным определением авторства.

## 🎯 Основные возможности

### 📋 Система управления содержимым
- **Content.json** - машиночитаемый индекс всех файлов документации с метаданными
- **Description_for_agents.md** - структурированное оглавление для AI-систем и разработчиков
- **Автоматическая навигация** - русские ссылки "Домой" и "Назад" во всех файлах
- **Persistent file_id** - уникальные идентификаторы файлов на основе содержимого

### 🤖 Интеллектуальное определение авторства
- **Человек (human)** - файлы, созданные разработчиками
- **ИИ (ai)** - файлы, созданные AI-системами (ChatGPT, Claude, Devin)
- **Генератор (generator)** - автоматически созданные файлы скриптами
- **Смешанное (mixed)** - файлы с множественным авторством

### 🔒 Защита автогенерированных файлов
- **Многоуровневая детекция** автогенераторов:
  1. Реестр генераторов (`generator_registry.json`)
  2. Маркеры комментариев (`<!-- AUTO-GENERATED -->`)
  3. Расположение файлов (`/auto_generated/`)
  4. Паттерны имен файлов (`*_auto.md`, `api_documentation.md`)
- **Автоматическая защита** - файлы генераторов помечаются как `editable=false`
- **Визуальные индикаторы** - иконки 🔒 и ⚙️ для защищенных файлов

### 📖 Классические функции
- **TOC генерация** - автоматическое создание оглавлений в JSON и Markdown
- **Include-директивы** - вставка содержимого между файлами `<!-- include:file#id -->`
- **Валидация структуры** - проверка ссылок, заголовков и целостности
- **Git интеграция** - pre-commit hooks для автоматического обновления

## 📚 Документация проекта

- [📋 Структурированное содержание (Content.json)](content/Content.json) - машиночитаемый индекс всех файлов документации
- [📖 Навигация для агентов (Description_for_agents.md)](content/Description_for_agents.md) - структурированное оглавление для AI-систем

## 📦 Установка

```bash
pip install -r requirements.txt
```

## 🚀 Использование

### Современная система Content.json (рекомендуется)

```bash
# Создание полной системы документации с определением авторства
python -c "
from update_docs.core import update_content_system
update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
"

# Или через CLI
python -m update_docs.cli --docs docs --content-json content/Content.json --description-md content/Description_for_agents.md
```

**Результат:**
- `content/Content.json` - структурированный индекс с метаданными и авторством
- `content/Description_for_agents.md` - человекочитаемое оглавление с навигацией
- Автоматические ссылки "Домой" и "Назад" во всех файлах документации

### Классическая система TOC (legacy)

```bash
# Базовое обновление документации
python -m update_docs.cli --docs docs --toc toc.json

# Создание Markdown оглавления
python -m update_docs.cli --docs docs --toc toc.json --toc-md toc.md

# Комплексное сканирование с обнаружением дубликатов
python -m update_docs.cli --docs docs --toc toc.json --comprehensive --similarity-threshold 0.8
```

### Работа с автогенераторами

```bash
# Создание примера автогенератора
python example_doc_generator.py

# Тестирование системы определения автогенераторов
python test_enhanced_generator_detection.py

# Сканирование функций-генераторов в проекте
python -c "
from update_docs.core import scan_for_generator_functions
generators = scan_for_generator_functions()
for gen in generators:
    print(f'{gen[\"function\"]} в {gen[\"file\"]}')
"
```

## 🔧 Интеграция с Git

### Современный подход (Content.json)
```bash
# Pre-commit hook для Content.json системы
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
python -c "
from update_docs.core import update_content_system
update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
"
git add content/Content.json content/Description_for_agents.md docs/
EOF

chmod +x .git/hooks/pre-commit
```

### Классический подход (TOC)
```bash
# Pre-commit hook для toc.json
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
python -m update_docs.cli --docs docs --toc toc.json
git add toc.json
EOF

chmod +x .git/hooks/pre-commit
```

## 🧪 Тестирование

```bash
# Запуск всех тестов
python -m pytest tests/test_core_syntax_fixed.py -v

# Тестирование соответствия спецификации
python test_specification_compliance.py

# Тестирование системы автогенераторов
python test_enhanced_generator_detection.py

# Тестирование русской навигации
python test_russian_navigation.py
```

## 📊 Мониторинг и анализ

```bash
# Анализ авторства файлов
python -c "
import json
with open('content/Content.json', 'r') as f:
    data = json.load(f)
authors = {}
for entry in data:
    author = entry.get('author', 'unknown')
    authors[author] = authors.get(author, 0) + 1
print('Статистика авторства:', authors)
"

# Поиск защищенных файлов
python -c "
import json
with open('content/Content.json', 'r') as f:
    data = json.load(f)
protected = [entry['path'] for entry in data if not entry.get('editable', True)]
print('Защищенные файлы:', protected)
"
```

## 📁 Структура проекта

```
update_docs/
├── __init__.py          # Основные утилиты
├── cli.py              # CLI интерфейс
└── core.py             # Основная логика обработки

content/                 # Современная система документации
├── Content.json        # Структурированный индекс файлов
└── Description_for_agents.md  # Человекочитаемое оглавление

tests/
├── test_core_syntax_fixed.py  # Основные тесты функций
└── test_cli.py               # Тесты CLI интерфейса

docs/                   # Документация проекта
├── auto_generated/     # Автогенерированные файлы (защищены)
├── README.md
├── setup.md
└── ...

# Вспомогательные скрипты
example_doc_generator.py           # Пример автогенератора
test_enhanced_generator_detection.py  # Тестирование автогенераторов
test_specification_compliance.py      # Проверка соответствия спецификации
test_russian_navigation.py           # Тестирование русской навигации
```

## 🔍 Система определения авторства

### Типы авторства
- **human** - файлы, созданные разработчиками вручную
- **ai** - файлы, созданные AI-системами (определяется по маркерам и git истории)
- **generator** - автоматически созданные файлы (защищены от редактирования)
- **mixed** - файлы с множественным авторством

### Методы детекции автогенераторов
1. **Реестр генераторов** - проверка в `generator_registry.json`
2. **Маркеры комментариев** - `<!-- AUTO-GENERATED -->`, `# AUTO-GENERATED`
3. **Расположение файлов** - папки `/auto_generated/`
4. **Паттерны имен** - `*_auto.md`, `*_generated.md`, `api_documentation.md`

### Защита файлов
Файлы с авторством "generator" автоматически:
- Помечаются как `editable: false` в Content.json
- Отображаются с иконкой 🔒 в Description_for_agents.md
- Защищены от случайного редактирования

## 🎉 Итоги реализации

Система update-docs превратилась в комплексное решение для управления документацией:

### ✅ Реализованные функции
- **Интеллектуальное определение авторства** с 4-уровневой системой детекции
- **Автоматическая защита** автогенерированных файлов от редактирования
- **Русская навигация** с ссылками "Домой" и "Назад"
- **Persistent file_id** для стабильной идентификации файлов
- **Content.json система** для структурированного управления документацией
- **Comprehensive TOC** с обнаружением дубликатов и аннотациями

### 🚀 Готово к использованию
Система полностью протестирована и готова к промышленному использованию в проектах любого масштаба.

