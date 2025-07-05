# 📜 Changelog

Все значимые изменения проекта `update-docs-system` документируются в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/ru/1.0.0/)  
Проект использует [Semantic Versioning](https://semver.org/lang/ru/).

## [1.0.0] - 2025-07-05

### 🚀 Добавлено

- Первая стабильная версия CLI-инструмента `update-docs-system`
- Генерация JSON-оглавлений (`toc.json`) и Markdown-оглавлений (`toc.md`)
- Система `Content.json` с определением структуры, заголовков и авторства
- Классификация авторов файлов: `human`, `ai`, `generator`, `mixed`
- Добавление русских навигационных ссылок: "🏠 Домой" и "⬆️ Назад"
- Поддержка include-блоков (`<!-- include:file#header -->`)
- Генерация файла `Description_for_agents.md` с аннотацией документации
- Поддержка шаблонов автоматизации: GitHub Actions, pre-commit, file watcher
- Возможность публикации как: PyPI-пакет, Git Submodule, Docker-контейнер

### 👤 Автор

William Evans — [we256681@gmail.com](mailto:we256681@gmail.com)
