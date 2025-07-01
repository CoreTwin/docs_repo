# Система логирования CoreTwin Platform

## Обзор

CoreTwin Platform использует структурированную систему логирования с категоризацией ошибок по тегам. Система поддерживает JSON формат логов, ротацию файлов и фильтрацию чувствительных данных.

## Конфигурация

Настройки логирования в `app/config.py`:

```python
LOG_LEVEL: str = "INFO"                    # Уровень логирования
LOG_FORMAT: str = "json"                   # Формат логов (json/text)
LOG_FILE_ENABLED: bool = True              # Включить файловое логирование
LOG_FILE_PATH: str = "./logs"              # Путь к директории логов
LOG_FILE_MAX_SIZE: int = 10485760          # Максимальный размер файла (10MB)
LOG_FILE_BACKUP_COUNT: int = 5             # Количество резервных файлов
LOG_ROTATION_WHEN: str = "midnight"        # Время ротации
LOG_FILTER_SENSITIVE: bool = True          # Фильтрация чувствительных данных
```

## Теги категоризации ошибок

- `AUTHENTICATION_ERROR` - Ошибки аутентификации и авторизации
- `DATABASE_ERROR` - Ошибки базы данных
- `VALIDATION_ERROR` - Ошибки валидации данных
- `API_ERROR` - Ошибки API запросов
- `SYSTEM_ERROR` - Системные ошибки

## Структура файлов логов

```
backend/logs/
├── app.log          # Общие логи приложения
├── auth.log         # Логи аутентификации
├── database.log     # Логи базы данных
├── api.log          # Логи API запросов
└── errors.log       # Все ошибки уровня ERROR
```

## Формат JSON логов

```json
{
  "timestamp": "2023-12-26T12:00:00.000Z",
  "level": "ERROR",
  "logger": "services.auth.service",
  "message": "Попытка входа с несуществующим email",
  "module": "service",
  "function": "authenticate_user",
  "line": 67,
  "tag": "AUTHENTICATION_ERROR",
  "user_id": "user123",
  "request_id": "req456",
  "extra_data": {
    "email": "test@example.com"
  }
}
```

## Использование в коде

### Импорт сервиса логирования

```python
from services.logging.service import logging_service, ErrorTags
```

### Логирование с тегами

```python
# Ошибка аутентификации
logging_service.log_authentication_error(
    "Неверный пароль",
    user_id="user123",
    request_id="req456",
    extra_data={"email": "user@example.com"}
)

# Ошибка базы данных
logging_service.log_database_error(
    "Ошибка подключения к БД",
    extra_data={"error": str(e)}
)

# Ошибка валидации
logging_service.log_validation_error(
    "Неверный формат email",
    extra_data={"field": "email", "value": "invalid"}
)

# Ошибка API
logging_service.log_api_error(
    "HTTP 500 Internal Server Error",
    request_id="req456",
    extra_data={"endpoint": "/api/v1/auth/login"}
)

# Информационное логирование
logging_service.log_info(
    "Пользователь успешно создан",
    tag="USER_CREATED",
    user_id="user123",
    extra_data={"email": "user@example.com"}
)
```

## Фильтрация чувствительных данных

Система автоматически фильтрует:
- Пароли (`password`, `hashed_password`)
- JWT токены (`access_token`, `refresh_token`)
- Заголовки авторизации (`Authorization: Bearer ...`)

Чувствительные данные заменяются на `"***FILTERED***"`.

## Интеграция с FastAPI

Middleware автоматически логирует:
- Входящие HTTP запросы с тегом `API_ERROR`
- Ответы с кодами ошибок (>= 400)
- Время выполнения запросов
- Информацию о пользователе и IP адресе

## Мониторинг и анализ

Логи можно анализировать с помощью:
- `grep` для поиска по тегам: `grep "AUTHENTICATION_ERROR" logs/auth.log`
- JSON парсеров для структурированного анализа
- Систем мониторинга (ELK Stack, Grafana)

## Ротация логов

Файлы автоматически ротируются:
- По размеру (10MB по умолчанию)
- По времени (ежедневно в полночь)
- Сохраняется 5 резервных копий

## Производительность

- Асинхронное логирование не блокирует основные операции
- Буферизация записей для оптимизации I/O
- Настраиваемые уровни логирования для контроля объема
