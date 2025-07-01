# CoreTwin Platform Backend

## Архитектура Backend

Backend платформы CoreTwin построен на основе **FastAPI** с использованием **SQLAlchemy** для работы с базой данных и следует принципам микросервисной архитектуры.

## 📁 Структура проекта

```
backend/
├── app/                    # Основное приложение
│   ├── __init__.py
│   ├── main.py            # Точка входа FastAPI
│   ├── config.py          # Конфигурация приложения
│   └── dependencies.py    # Зависимости FastAPI
├── services/              # Микросервисы по доменам
│   ├── auth/             # Аутентификация и авторизация
│   ├── specialties/      # Справочник должностей
│   ├── companies/        # Управление компаниями
│   ├── documents/        # Шаблоны документов
│   ├── workflows/        # Маршруты согласования
│   └── mcp/             # Интеграция с MCP
├── models/               # SQLAlchemy модели
├── schemas/              # Pydantic схемы
├── api/                  # API роутеры
├── core/                 # Базовые компоненты
├── utils/                # Утилиты
└── tests/                # Тесты
```

## 🚀 Технологический стек

- **FastAPI** - современный веб-фреймворк для Python
- **SQLAlchemy** - ORM для работы с базой данных
- **Alembic** - миграции базы данных
- **Pydantic** - валидация данных
- **PostgreSQL** - основная база данных
- **Redis** - кэширование и очереди
- **Celery** - фоновые задачи
- **pytest** - тестирование

## 🔧 Настройка разработки

### Требования
- Python 3.11+
- PostgreSQL 15+
- Redis 7+

### Установка зависимостей
```bash
cd backend
pip install -r requirements.txt
```

### Переменные окружения
Скопируйте `.env.example` в `.env` и настройте переменные:
```bash
cp ../.env.example .env
```

### Запуск для разработки
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📊 Микросервисы

### 1. Auth Service
- Регистрация и аутентификация пользователей
- JWT токены
- Управление ролями и разрешениями

### 2. Specialties Service
- Справочник должностей ISCO-08
- Управление обязанностями
- Рекомендации модулей

### 3. Companies Service
- Управление организационными структурами
- Drag & Drop конструктор
- Назначение сотрудников

### 4. Documents Service
- Шаблоны документов
- Генерация документов
- Версионирование

### 5. Workflows Service
- Маршруты согласования
- Статусы задач
- Уведомления

### 6. MCP Service
- Интеграция с Model Context Protocol
- AI-рекомендации
- Модерация контента

## 🧪 Тестирование

```bash
# Запуск всех тестов
pytest

# Запуск с покрытием
pytest --cov=app

# Запуск конкретного сервиса
pytest tests/services/test_specialties.py
```

## 📝 API Документация

После запуска сервера документация доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔒 Безопасность

- JWT аутентификация
- CORS настройки
- Валидация входных данных
- SQL injection защита
- Rate limiting

## 📈 Мониторинг

- Prometheus метрики
- Sentry для отслеживания ошибок
- Структурированное логирование
- Health check endpoints
