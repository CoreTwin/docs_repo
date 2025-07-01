# Тестирование CoreTwin Platform

## Обзор

Система тестирования CoreTwin Platform обеспечивает высокое качество кода и надежность приложения через комплексное покрытие тестами.

## Текущее покрытие

- **Общее покрытие**: 80%+
- **Backend**: Unit и Integration тесты
- **Frontend**: Component и E2E тесты (планируется)

## Структура тестов

### Backend тесты
```
backend/tests/
├── unit/                  # Unit тесты
│   ├── test_auth_service.py
│   ├── test_user_model.py
│   └── test_logging_service.py
├── integration/           # Integration тесты
│   ├── test_auth_api.py
│   └── test_dependencies.py
├── conftest.py           # Pytest конфигурация
└── README.md
```

### Типы тестов

#### Unit тесты
- Тестирование отдельных функций и методов
- Изоляция зависимостей через моки
- Быстрое выполнение

#### Integration тесты
- Тестирование взаимодействия компонентов
- Использование тестовой базы данных
- Проверка API endpoints

## Конфигурация

### pytest.ini
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
    --cov=app
    --cov=services
    --cov-report=term-missing
    --cov-report=html:htmlcov
    --cov-fail-under=50
```

### Тестовая база данных
- PostgreSQL для integration тестов
- Автоматическое создание/удаление тестовых данных
- Изоляция между тестами

## Запуск тестов

### Все тесты
```bash
cd backend
pytest
```

### С покрытием
```bash
pytest --cov=app --cov=services --cov-report=html
```

### Конкретный файл
```bash
pytest tests/unit/test_auth_service.py -v
```

### По маркерам
```bash
pytest -m "not slow"
```

## Фикстуры

### Базовые фикстуры
- `db_session` - сессия базы данных
- `test_client` - HTTP клиент для API
- `test_user` - тестовый пользователь
- `auth_headers` - заголовки авторизации

### Пример использования
```python
def test_create_user(db_session):
    user_data = UserCreate(
        email="test@example.com",
        full_name="Test User",
        password="password123"
    )
    user = create_user(db_session, user_data)
    assert user.email == "test@example.com"
```

## Моки и заглушки

### Внешние зависимости
```python
@patch('services.auth.service.verify_password')
def test_authenticate_user(mock_verify, db_session):
    mock_verify.return_value = True
    # тест логики
```

### База данных
```python
@pytest.fixture
def mock_db_session():
    session = MagicMock()
    yield session
```

## Тестирование API

### Аутентификация
```python
def test_login_success(test_client):
    response = test_client.post("/api/v1/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
```

### Защищенные endpoints
```python
def test_get_current_user(test_client, auth_headers):
    response = test_client.get("/api/v1/auth/me", headers=auth_headers)
    assert response.status_code == 200
```

## Тестирование ошибок

### Валидация данных
```python
def test_create_user_invalid_email(test_client):
    response = test_client.post("/api/v1/auth/register", json={
        "email": "invalid-email",
        "password": "password123"
    })
    assert response.status_code == 422
```

### Обработка исключений
```python
def test_database_error_handling(db_session):
    with patch.object(db_session, 'commit', side_effect=SQLAlchemyError):
        with pytest.raises(DatabaseError):
            create_user(db_session, user_data)
```

## Производительность

### Профилирование тестов
```bash
pytest --durations=10
```

### Параллельное выполнение
```bash
pytest -n auto
```

## CI/CD интеграция

### GitHub Actions
```yaml
- name: Run tests
  run: |
    cd backend
    pytest --cov=app --cov=services --cov-report=xml

- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./backend/coverage.xml
```

## Лучшие практики

### Именование тестов
- Используйте описательные имена
- Следуйте паттерну `test_<action>_<expected_result>`
- Группируйте связанные тесты в классы

### Структура тестов
- Arrange - подготовка данных
- Act - выполнение действия
- Assert - проверка результата

### Изоляция тестов
- Каждый тест должен быть независимым
- Используйте фикстуры для подготовки данных
- Очищайте состояние после тестов

## Отчеты

### HTML отчет покрытия
```bash
pytest --cov-report=html
open htmlcov/index.html
```

### XML отчет для CI
```bash
pytest --cov-report=xml
```

## Будущие улучшения

### Frontend тестирование
- Jest для unit тестов
- React Testing Library для компонентов
- Cypress для E2E тестов

### Нагрузочное тестирование
- Locust для API нагрузки
- Профилирование производительности
- Мониторинг метрик

### Безопасность
- SAST сканирование
- Dependency scanning
- Penetration testing
