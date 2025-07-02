[Домой](../README.md) | [Назад](../content/Description_for_agents.md)

# CoreTwin Platform

**Цифровой двойник вашего бизнеса — под полным контролем**1

CoreTwin Platform — универсальная платформа для построения «цифрового двойника» организации. Она позволяет визуально спроектировать оргструктуру предприятия, назначить сотрудников на должности, определить их функциональные обязанности, настроить шаблоны документов и управлять бизнес-процессами в единой адаптивной системе.

## 🎯 Ключевые возможности

- **Универсальность**: подходит для компаний любого масштаба и сферы деятельности
- **Гибкость**: модульная архитектура — подключайте только нужные компоненты
- **Прозрачность**: вся структура, роли и процессы управляемы через единый интерфейс
- **Интеграция**: кадры, процессы согласования и документооборот в одной экосистеме
- **ИИ-поддержка**: интеллектуальные рекомендации через Model Context Protocol (MCP)

## 🏗️ Архитектура

### Технологический стек
- **Backend**: FastAPI + SQLAlchemy + Python + Go + Rust
- **Frontend**: React + TypeScript + React Flow + Rete.js + Ant Design
- **База данных**: PostgreSQL + Redis + ClickHouse
- **Развертывание**: Docker + Kubernetes
- **ИИ-интеграция**: Model Context Protocol (MCP)

### Структура проекта

```
backend/          # Серверная логика (FastAPI + SQLAlchemy)
  services/       # Микросервисы по доменам
frontend/         # Веб-интерфейс на React + TypeScript
database/         # SQL-миграции и схемы таблиц
deployments/      # Docker, Kubernetes, CI/CD
docs/             # Документация проекта
  specs/          # Техническое задание
  architecture/   # Архитектурные решения
  references/     # Справочники и классификации
  development/    # План и процесс разработки
.env              # Конфигурации окружения
```

## 📚 Документация

### Быстрый старт
1. [Техническое задание](docs/specs/technical-specification.md) - полное описание платформы
2. [Архитектура системы](docs/architecture/service-design.md) - логика модульной архитектуры
3. [План разработки](docs/development/development-plan.md) - детальный план реализации

### Архитектура и дизайн
- [Технологический стек](docs/architecture/technology-stack.md) - рекомендации по технологиям
- [Интеграция MCP](docs/architecture/mcp-integration.md) - применение ИИ в платформе
- [Дизайн сервисов](docs/architecture/service-design.md) - модульная архитектура

### Справочники
- [Глобальный справочник должностей](docs/references/job-directory.md) - каталог специальностей
- [Классификация отраслей](docs/references/industries-classification.md) - ISCO-08 и ISIC Rev.4

### Разработка
- [Процесс разработки](docs/development/README.md) - методология и стандарты
- [Детальный план](docs/development/development-plan.md) - фазы и временные рамки

## 📊 Статус проекта

**Текущая фаза**: MVP разработка

**Реализовано**:
- ✅ Базовая архитектура проекта
- ✅ Система аутентификации с JWT
- ✅ Модели пользователей и компаний
- ✅ Структурированное логирование с категоризацией ошибок
- ✅ Тестовое покрытие 80% с pytest
- ✅ Docker контейнеризация
- ✅ Система документации (MkDocs, Sphinx, TypeDoc)
- ✅ GitHub Actions для CI/CD
- ✅ Frontend компоненты (React/TypeScript)

**В разработке**:
- 🔄 Справочник должностей ISCO-08
- 🔄 Конструктор организационных структур

**Планируется**:
- 📋 Система рекомендаций с ИИ
- 📋 Интеграция с внешними системами
- 📋 Аналитика и отчеты

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Docker и Docker Compose

### Установка

1. **Клонирование репозитория:**
```bash
git clone https://github.com/CoreTwin/CoreTwin.git
cd CoreTwin
```

2. **Настройка окружения:**
```bash
cp .env.example .env
# Отредактируйте .env файл с вашими настройками
```

3. **Запуск с Docker Compose:**
```bash
docker-compose up -d
```

4. **Или локальный запуск:**
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

### Доступ к приложению
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Документация**: http://localhost:8000/docs
- **Документация проекта**: Запустите `mkdocs serve` для локального просмотра

### Тестирование
```bash
# Backend тесты
cd backend
pytest --cov=app --cov=services --cov-report=html

# Frontend тесты
cd frontend
npm test
```

### Манифесты
- [Manifest Architecture](docs/manifest/manifest_architecture.md) - архитектурные принципы
- [Manifest Structure](docs/manifest/manifest_structure.md) - структурирование проекта
- [Manifest Documentation](docs/manifest/manifest_documentation.md) - документация и версии
- [Manifest Testing](docs/manifest/manifest_testing.md) - тестирование и QA
- [Manifest Security](docs/manifest/manifest_security.md) - безопасность и доступ
- [Manifest Code Standards](docs/manifest/manifest_code_standards.md) - кодстайл и соглашения
- [Manifest International Standards](docs/manifest/manifest_international_standards.md) - международные нормы 
- [Manifest UI Design](docs/manifest/manifest_ui_design.md) - визуальный интерфейс
- [Manifest Configuration](docs/manifest/manifest_configuration.md) - конфигурации и окружения
- [Manifest Versioning](docs/manifest/manifest_versioning.md) - релизы и версионирование
- [Manifest Digital Twins](docs/manifest/manifest_digital_twins.md) - цифровые двойники
- [Manifest Data Quality](docs/manifest/manifest_data_quality.md) - качество и валидация данных
- [Manifest Ethics AI Moderation](docs/manifest/manifest_ethics_ai_moderation.md) - AI и модерация
- [Manifest Knowledge Management](docs/manifest/manifest_knowledge_management.md) - управление компетенциями
- [Manifest Scalability Reuse](docs/manifest/manifest_scalability_reuse.md) - масштабируемость и реюз

## 📊 Основные модули

1. **Specialties & Duties** - справочник должностей и обязанностей
2. **Company Structure** - конструктор организационной структуры
3. **Module Recommendations** - система автоматических рекомендаций
4. **Document Templates** - управление шаблонами документов
5. **Approval Workflows** - маршруты согласования
6. **MCP Integration** - ИИ-сервисы и интеллектуальные рекомендации

## 🌍 Стандарты

Платформа использует международные классификации:
- **ISCO-08**: Международная стандартная классификация занятий
- **ISIC Rev.4**: Международная стандартная отраслевая классификация
- Поддержка российских стандартов (ОКЗ, ОКВЭД2)

## 📞 Контакты

- **Репозиторий**: [CoreTwin](https://github.com/CoreTwin/CoreTwin)
- **Документация**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/CoreTwin/CoreTwin/issues)

---

*CoreTwin Platform — это будущее управления организационными структурами. Создавайте, управляйте и оптимизируйте свой бизнес с помощью цифрового двойника.*
