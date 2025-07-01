# Тестирование CoreTwin Platform

## Конфигурация PostgreSQL для тестов

Тестовая среда использует PostgreSQL базу данных для обеспечения максимальной совместимости с продакшн средой.

### Требования

- PostgreSQL 14+ установлен и запущен
- Тестовая база данных `coretwin_test_db` создана
- Python пакет `psycopg2-binary` установлен

### Настройка тестовой базы данных

```bash
# Создание тестовой базы данных
sudo -u postgres createdb coretwin_test_db

# Проверка подключения
sudo -u postgres psql -c "SELECT datname FROM pg_database WHERE datname = 'coretwin_test_db';"
```

### Запуск тестов

```bash
# Установка зависимостей для тестирования
pip install -r requirements-test.txt

# Запуск всех тестов с покрытием
pytest --cov=app --cov=services --cov-report=html --cov-report=term

# Запуск конкретных тестов
pytest tests/unit/test_auth_service.py -v
pytest tests/integration/test_auth_api.py -v
```

### Покрытие кода

Минимальное требование покрытия: **80%**

Текущее покрытие системы аутентификации: **80%+**

### Изоляция тестов

Каждый тест выполняется в изолированной среде:
- Создание всех таблиц перед тестом
- Полная очистка базы данных после теста
- Использование отдельной тестовой базы данных

### Структура тестов

```
tests/
├── __init__.py
├── conftest.py          # Конфигурация pytest и фикстуры
├── README.md           # Документация тестирования
├── unit/               # Unit тесты
│   ├── test_auth_service.py
│   └── test_user_model.py
└── integration/        # Integration тесты
    ├── test_auth_api.py
    └── test_dependencies.py
```

### Фикстуры

- `db_session`: Сессия PostgreSQL базы данных для теста
- `client`: FastAPI тестовый клиент
- `async_client`: Асинхронный HTTP клиент
- `auth_service`: Сервис аутентификации
- `test_user_data`: Тестовые данные пользователя
- `created_user`: Созданный тестовый пользователь
- `jwt_token`: JWT токен для авторизации
- `auth_headers`: Заголовки авторизации для API запросов
