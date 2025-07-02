[Домой](../README.md) | [Назад](../content/Description_for_agents.md)

# Настройка окружения разработки

## Системные требования

### Минимальные требования
- **Python**: 3.11+
- **Node.js**: 18+
- **PostgreSQL**: 14+
- **Redis**: 6+
- **Docker**: 20+
- **Docker Compose**: 2.0+

### Рекомендуемые требования
- **Python**: 3.12
- **Node.js**: 20 LTS
- **PostgreSQL**: 15
- **Redis**: 7
- **RAM**: 8GB+
- **Диск**: 20GB+ свободного места

## Установка зависимостей

### 1. Клонирование репозитория

```bash
git clone https://github.com/CoreTwin/CoreTwin.git
cd CoreTwin
```

### 2. Настройка Python окружения

```bash
# Создание виртуального окружения
python -m venv venv

# Активация (Linux/macOS)
source venv/bin/activate

# Активация (Windows)
venv\Scripts\activate

# Установка зависимостей backend
cd backend
pip install -r requirements.txt
pip install -r requirements-test.txt
```

### 3. Настройка Node.js окружения

```bash
# Переход в директорию frontend
cd ../frontend

# Установка зависимостей
npm install
```

### 4. Настройка базы данных

#### PostgreSQL

```bash
# Установка PostgreSQL (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql postgresql-contrib

# Создание пользователя и базы данных
sudo -u postgres psql
```

В psql консоли выполните следующие команды, заменив значения на ваши:

```sql
CREATE USER имя_пользователя WITH PASSWORD 'ваш_пароль';
CREATE DATABASE coretwin_db OWNER имя_пользователя;
CREATE DATABASE coretwin_test_db OWNER имя_пользователя;
GRANT ALL PRIVILEGES ON DATABASE coretwin_db TO имя_пользователя;
GRANT ALL PRIVILEGES ON DATABASE coretwin_test_db TO имя_пользователя;
\q
```

#### Redis

```bash
# Установка Redis (Ubuntu/Debian)
sudo apt install redis-server

# Запуск Redis
sudo systemctl start redis-server
sudo systemctl enable redis-server
```

### 5. Настройка переменных окружения

```bash
# Копирование примера конфигурации
cp .env.example .env
```

Отредактируйте `.env` файл, указав ваши настройки:

```env
# Database - укажите ваши данные подключения
DATABASE_URL=postgresql://пользователь:пароль@localhost:5432/coretwin_db
TEST_DATABASE_URL=postgresql://пользователь:пароль@localhost:5432/coretwin_test_db

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT - сгенерируйте безопасный ключ
JWT_SECRET_KEY=ваш_секретный_ключ_для_jwt
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json
LOG_FILE_ENABLED=true
LOG_FILE_PATH=./logs

# Development
DEBUG=true
ENVIRONMENT=development
```

## Запуск приложения

### Вариант 1: Docker Compose (Рекомендуется)

```bash
# Запуск всех сервисов
docker-compose up -d

# Просмотр логов
docker-compose logs -f

# Остановка сервисов
docker-compose down
```

### Вариант 2: Локальный запуск

#### Backend

```bash
cd backend

# Применение миграций
alembic upgrade head

# Запуск сервера разработки
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend

```bash
cd frontend

# Запуск сервера разработки
npm run dev
```

## Проверка установки

### 1. Backend API

Откройте в браузере:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### 2. Frontend

Откройте в браузере:
- **Frontend**: http://localhost:3000

### 3. Тестирование

```bash
# Backend тесты
cd backend
pytest --cov=app --cov=services --cov-report=html

# Frontend тесты
cd frontend
npm test
```

## Полезные команды

### Backend

```bash
# Создание новой миграции
alembic revision --autogenerate -m "Описание изменений"

# Применение миграций
alembic upgrade head

# Откат миграций
alembic downgrade -1

# Запуск тестов с покрытием
pytest --cov=app --cov=services --cov-report=html --cov-report=term

# Линтинг кода
black app/ services/
isort app/ services/
flake8 app/ services/
```

### Frontend

```bash
# Запуск в режиме разработки
npm run dev

# Сборка для продакшена
npm run build

# Предварительный просмотр сборки
npm run preview

# Линтинг
npm run lint
npm run lint:fix

# Тестирование
npm test
npm run test:coverage
```

### Docker

```bash
# Пересборка контейнеров
docker-compose build

# Запуск отдельного сервиса
docker-compose up backend

# Выполнение команд в контейнере
docker-compose exec backend bash
docker-compose exec frontend sh

# Просмотр логов
docker-compose logs backend
docker-compose logs frontend
```

## Решение проблем

### Проблемы с PostgreSQL

```bash
# Проверка статуса PostgreSQL
sudo systemctl status postgresql

# Перезапуск PostgreSQL
sudo systemctl restart postgresql

# Проверка подключения
psql -h localhost -U имя_пользователя -d coretwin_db
```

### Проблемы с правами доступа

```bash
# Исправление прав на директории
sudo chown -R $USER:$USER .
chmod -R 755 .

# Исправление прав на логи
mkdir -p backend/logs
chmod 755 backend/logs
```

### Проблемы с зависимостями

```bash
# Очистка кеша pip
pip cache purge

# Переустановка зависимостей
pip install --force-reinstall -r requirements.txt

# Очистка кеша npm
npm cache clean --force

# Переустановка зависимостей
rm -rf node_modules package-lock.json
npm install
```

## IDE настройка

### VS Code

Рекомендуемые расширения:
- Python
- Pylance
- Black Formatter
- isort
- TypeScript and JavaScript Language Features
- ES7+ React/Redux/React-Native snippets
- Prettier - Code formatter
- ESLint

### PyCharm

Настройки:
- Интерпретатор Python: `venv/bin/python`
- Корневая директория: `backend/`
- Настройка линтеров: Black, isort, flake8

## Дополнительные инструменты

### Мониторинг

```bash
# Установка htop для мониторинга системы
sudo apt install htop

# Мониторинг Docker контейнеров
docker stats
```

### Отладка

```bash
# Подключение к базе данных
psql -h localhost -U имя_пользователя -d coretwin_db

# Мониторинг Redis
redis-cli monitor

# Просмотр логов приложения
tail -f backend/logs/app.log
```

---

После успешной настройки окружения вы можете приступить к разработке. Обратитесь к [плану разработки](development-plan.md) для понимания текущих задач и приоритетов.
