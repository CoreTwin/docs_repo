# 📘 Структура документации проекта

*Автоматически сгенерировано системой update-docs*

<!-- AUTO-GENERATED -->

## 📊 Статистика авторства

- 🤖 **ai**: 3 файлов
- 👤 **human**: 33 файлов

## 📁 корень

### ✏️ 👤 [Authentication API](authentication.md)
**File ID:** `authentication-cb4f6ea7`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Authentication API](authentication.md#authentication-api) — *The authentication system provides secure user registration, login, and JWT token management for t*
  - [Overview](authentication.md#overview) — *The authentication system provides secure user registration, login, and JWT token management for th*
  - [Endpoints](authentication.md#endpoints) — *Register a new user account.*
    - [POST /api/v1/auth/register](authentication.md#post--api-v1-auth-register) — *Register a new user account.  **Request Body:***
    - [POST /api/v1/auth/login](authentication.md#post--api-v1-auth-login) — *Authenticate user and receive JWT tokens.  **Request Body:***
    - [POST /api/v1/auth/refresh](authentication.md#post--api-v1-auth-refresh) — *Refresh access token using refresh token.  **Request Body:***
    - [GET /api/v1/auth/me](authentication.md#get--api-v1-auth-me) — *Get current authenticated user information.  **Headers:***
    - [POST /api/v1/auth/change-password](authentication.md#post--api-v1-auth-change-password) — *Change user password.  **Headers:***
    - [POST /api/v1/auth/logout](authentication.md#post--api-v1-auth-logout) — *Logout user (invalidate tokens).  **Headers:***
  - [Authentication Flow](authentication.md#authentication-flow) — *1. **Registration**: User creates account with email and password 2. **Login**: User authenticates*
  - [Security Features](authentication.md#security-features) — *- **Password Hashing**: Uses bcrypt for secure password storage - **JWT Tokens**: Stateless authent*
  - [Related Documentation](authentication.md#related-documentation) — *- [User Management API](users.md) - [Security Architecture](../architecture/security.md) - [Develop*

### ✏️ 👤 [Changelog](CHANGELOG.md)
**File ID:** `changelog-21a32e44`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Changelog](CHANGELOG.md#changelog) — *Все значимые изменения в проекте CoreTwin Platform будут документированы в этом файле.  Формат осно*
  - [[Unreleased]](CHANGELOG.md#-unreleased-) — *- Полная структура документации проекта - Техническое задание платформы CoreTwin*
    - [Добавлено](CHANGELOG.md#добавлено) — *- Полная структура документации проекта - Техническое задание платформы CoreTwin - Архитектурные спе...*
    - [Изменено](CHANGELOG.md#изменено) — *- Обновлен главный README.md с полным описанием проекта - Реорганизована структура документации*
  - [[0.1.0] - 2024-12-26](CHANGELOG.md#-0-1-0----2024-12-26) — *- Инициализация репозитория - Базовая структура проекта*
    - [Добавлено](CHANGELOG.md#добавлено) — *- Инициализация репозитория - Базовая структура проекта - Placeholder файлы для основных компонентов...*

### ✏️ 👤 [Companies API](companies.md)
**File ID:** `companies-4c402d12`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Companies API](companies.md#companies-api) — *The companies API provides functionality for managing company information and organizational struc*
  - [Overview](companies.md#overview) — *The companies API provides functionality for managing company information and organizational struct*
  - [Endpoints](companies.md#endpoints) — *Get list of companies.*
    - [GET /api/v1/companies/](companies.md#get--api-v1-companies-) — *Get list of companies.  **Headers:***
    - [POST /api/v1/companies/](companies.md#post--api-v1-companies-) — *Create a new company.  **Headers:***
  - [Related Documentation](companies.md#related-documentation) — *- [Authentication API](authentication.md) - [Users API](users.md) - [Development Setup](../developm*

### ✏️ 👤 [CoreTwin Platform](README.md)
**File ID:** `readme-9db4e87f`  
**Автор:** human | **Редактируемый:** Да
**Последний автор:** we256681 <we256681@gmail.com>  
**Все авторы:** we256681 <we256681@gmail.com>, woodg9461 <woodg9461@gmail.com>  

**Структура заголовков:**
- [CoreTwin Platform](README.md#coretwin-platform) — ***Цифровой двойник вашего бизнеса — под полным контролем**1  CoreTwin Platform — универсальная плат*
  - [🎯 Ключевые возможности](README.md#--ключевые-возможности) — *- **Универсальность**: подходит для компаний любого масштаба и сферы деятельности - **Гибкость**: м*
  - [🏗️ Архитектура](README.md#---архитектура) — *- **Backend**: FastAPI + SQLAlchemy + Python + Go + Rust - **Frontend**: React + TypeScript + React*
    - [Технологический стек](README.md#технологический-стек) — *- **Backend**: FastAPI + SQLAlchemy + Python + Go + Rust - **Frontend**: React + TypeScript + React*
    - [Структура проекта](README.md#структура-проекта) — *``` backend/          # Серверная логика (FastAPI + SQLAlchemy) services/       # Микросервисы по д*
  - [📚 Документация](README.md#--документация) — *1. [Техническое задание](docs/specs/technical-specification.md) - полное описание платформы 2. [Арх*
    - [Быстрый старт](README.md#быстрый-старт) — *1. [Техническое задание](docs/specs/technical-specification.md) - полное описание платформы 2. [Архи...*
    - [Архитектура и дизайн](README.md#архитектура-и-дизайн) — *- [Технологический стек](docs/architecture/technology-stack.md) - рекомендации по технологиям - [Инт...*
    - [Справочники](README.md#справочники) — *- [Глобальный справочник должностей](docs/references/job-directory.md) - каталог специальностей - [К...*
    - [Разработка](README.md#разработка) — *- [Процесс разработки](docs/development/README.md) - методология и стандарты - [Детальный план](docs...*
  - [📊 Статус проекта](README.md#--статус-проекта) — ***Текущая фаза**: MVP разработка  **Реализовано**:*
  - [🚀 Быстрый старт](README.md#--быстрый-старт) — *- Python 3.11+ - Node.js 18+*
    - [Предварительные требования](README.md#предварительные-требования) — *- Python 3.11+ - Node.js 18+ - PostgreSQL 14+ - Docker и Docker Compose*
    - [Установка](README.md#установка) — *1. **Клонирование репозитория:** ```bash git clone https://github.com/CoreTwin/CoreTwin.git*
- [Отредактируйте .env файл с вашими настройками](README.md#отредактируйте--env-файл-с-вашими-настройками) — *```  3. **Запуск с Docker Compose:** ```bash*
- [Backend](README.md#backend) — *cd backend pip install -r requirements.txt uvicorn app.main:app --reload*
- [Frontend](README.md#frontend) — *cd frontend npm install npm run dev ```*
    - [Доступ к приложению](README.md#доступ-к-приложению) — *- **Frontend**: http://localhost:3000 - **Backend API**: http://localhost:8000 - **API Документация*...*
    - [Тестирование](README.md#тестирование) — *```bash cd backend pytest --cov=app --cov=services --cov-report=html*
- [Backend тесты](README.md#backend-тесты) — *cd backend pytest --cov=app --cov=services --cov-report=html*
- [Frontend тесты](README.md#frontend-тесты) — *cd frontend npm test ```*
    - [Манифесты](README.md#манифесты) — *- [Manifest Architecture](docs/manifest/manifest_architecture.md) - архитектурные принципы - [Manife...*
  - [📊 Основные модули](README.md#--основные-модули) — *1. **Specialties & Duties** - справочник должностей и обязанностей 2. **Company Structure** - конст*
  - [🌍 Стандарты](README.md#--стандарты) — *Платформа использует международные классификации: - **ISCO-08**: Международная стандартная классифи*
  - [📞 Контакты](README.md#--контакты) — *- **Репозиторий**: [CoreTwin](https://github.com/CoreTwin/CoreTwin) - **Документация**: [docs/](doc*

### ✏️ 👤 [CoreTwin Platform](index.md)
**File ID:** `index-bd536f93`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [CoreTwin Platform](index.md#coretwin-platform) — ***Цифровой двойник вашего бизнеса — под полным контролем**  Добро пожаловать в документацию платфор*
  - [🎯 О платформе](index.md#--о-платформе) — *CoreTwin Platform позволяет:  - **Визуально проектировать** организационную структуру предприятия*
  - [🚀 Быстрый старт](index.md#--быстрый-старт) — *1. Ознакомьтесь с [техническим заданием](specs/technical-specification.md) 2. Изучите [архитектуру*
    - [Для пользователей](index.md#для-пользователей) — *1. Ознакомьтесь с [техническим заданием](specs/technical-specification.md) 2. Изучите [архитектуру с...*
    - [Для разработчиков](index.md#для-разработчиков) — *1. Изучите [план разработки](development/development-plan.md) 2. Настройте [окружение разработки](de...*
  - [🏗️ Архитектура](index.md#---архитектура) — *- **Backend**: FastAPI + SQLAlchemy + Python - **Frontend**: React + TypeScript + Ant Design*
    - [Технологический стек](index.md#технологический-стек) — *- **Backend**: FastAPI + SQLAlchemy + Python - **Frontend**: React + TypeScript + Ant Design - **Баз...*
    - [Ключевые компоненты](index.md#ключевые-компоненты) — *- **Система аутентификации** с JWT токенами - **Справочник должностей** на основе ISCO-08 - **Констр...*
  - [📊 Статус проекта](index.md#--статус-проекта) — ***Текущая фаза**: MVP разработка  **Реализовано**:*
  - [🌍 Стандарты](index.md#--стандарты) — *Платформа использует международные классификации: - **ISCO-08**: Международная стандартная классифи*
  - [📚 Навигация по документации](index.md#--навигация-по-документации) — *Техническая архитектура, дизайн сервисов и интеграции*
    - [🏛️ [Архитектура](architecture/overview.md)](index.md#----архитектура--architecture-overview-md-) — *Техническая архитектура, дизайн сервисов и интеграции  Документация REST API и интеграционных интерф...*
    - [🔌 [API](api/authentication.md)](index.md#---api--api-authentication-md-) — *Документация REST API и интеграционных интерфейсов  Руководства для разработчиков, процессы и станда...*
    - [👨‍💻 [Разработка](development/README.md)](index.md#-----разработка--development-readme-md-) — *Руководства для разработчиков, процессы и стандарты  Классификации отраслей, должностей и стандарты*
    - [📖 [Справочники](references/industries-classification.md)](index.md#---справочники--references-industries-classification-md-) — *Классификации отраслей, должностей и стандарты  Техническое задание и требования к системе*
    - [📋 [Спецификации](specs/technical-specification.md)](index.md#---спецификации--specs-technical-specification-md-) — *Техническое задание и требования к системе  ---*

### ✏️ 👤 [CoreTwin Platform Backend](README (2).md)
**File ID:** `readme--2--502c9dfd`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [CoreTwin Platform Backend](README (2).md#coretwin-platform-backend) — *Backend платформы CoreTwin построен на основе **FastAPI** с использованием **SQLAlchemy** для рабо*
  - [Архитектура Backend](README (2).md#архитектура-backend) — *Backend платформы CoreTwin построен на основе **FastAPI** с использованием **SQLAlchemy** для работ*
  - [📁 Структура проекта](README (2).md#--структура-проекта) — *``` backend/ ├── app/                    # Основное приложение*
  - [🚀 Технологический стек](README (2).md#--технологический-стек) — *- **FastAPI** - современный веб-фреймворк для Python - **SQLAlchemy** - ORM для работы с базой данн*
  - [🔧 Настройка разработки](README (2).md#--настройка-разработки) — *- Python 3.11+ - PostgreSQL 15+*
    - [Требования](README (2).md#требования) — *- Python 3.11+ - PostgreSQL 15+ - Redis 7+*
    - [Установка зависимостей](README (2).md#установка-зависимостей) — *```bash cd backend pip install -r requirements.txt ```*
    - [Переменные окружения](README (2).md#переменные-окружения) — *Скопируйте `.env.example` в `.env` и настройте переменные: ```bash cp ../.env.example .env ```*
    - [Запуск для разработки](README (2).md#запуск-для-разработки) — *```bash uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 ```*
  - [📊 Микросервисы](README (2).md#--микросервисы) — *- Регистрация и аутентификация пользователей - JWT токены*
    - [1. Auth Service](README (2).md#1--auth-service) — *- Регистрация и аутентификация пользователей - JWT токены - Управление ролями и разрешениями*
    - [2. Specialties Service](README (2).md#2--specialties-service) — *- Справочник должностей ISCO-08 - Управление обязанностями - Рекомендации модулей*
    - [3. Companies Service](README (2).md#3--companies-service) — *- Управление организационными структурами - Drag & Drop конструктор - Назначение сотрудников*
    - [4. Documents Service](README (2).md#4--documents-service) — *- Шаблоны документов - Генерация документов - Версионирование*
    - [5. Workflows Service](README (2).md#5--workflows-service) — *- Маршруты согласования - Статусы задач - Уведомления*
    - [6. MCP Service](README (2).md#6--mcp-service) — *- Интеграция с Model Context Protocol - AI-рекомендации - Модерация контента*
  - [🧪 Тестирование](README (2).md#--тестирование) — *```bash pytest*
- [Запуск всех тестов](README (2).md#запуск-всех-тестов) — *pytest  pytest --cov=app*
- [Запуск с покрытием](README (2).md#запуск-с-покрытием) — *pytest --cov=app  pytest tests/services/test_specialties.py*
- [Запуск конкретного сервиса](README (2).md#запуск-конкретного-сервиса) — *pytest tests/services/test_specialties.py ```*
  - [📝 API Документация](README (2).md#--api-документация) — *После запуска сервера документация доступна по адресам: - Swagger UI: http://localhost:8000/docs -*
  - [🔒 Безопасность](README (2).md#--безопасность) — *- JWT аутентификация - CORS настройки - Валидация входных данных*
  - [📈 Мониторинг](README (2).md#--мониторинг) — *- Prometheus метрики - Sentry для отслеживания ошибок - Структурированное логирование*

### ✏️ 👤 [CoreTwin Platform Frontend](README (3).md)
**File ID:** `readme--3--0c749397`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [CoreTwin Platform Frontend](README (3).md#coretwin-platform-frontend) — *Frontend платформы CoreTwin построен на **React** с **TypeScript** и использует современные инстру*
  - [Архитектура Frontend](README (3).md#архитектура-frontend) — *Frontend платформы CoreTwin построен на **React** с **TypeScript** и использует современные инструм*
  - [📁 Структура проекта](README (3).md#--структура-проекта) — *``` frontend/ ├── src/*
  - [🚀 Технологический стек](README (3).md#--технологический-стек) — *- **React 18** - библиотека для создания пользовательских интерфейсов - **TypeScript** - типизирова*
  - [🔧 Настройка разработки](README (3).md#--настройка-разработки) — *- Node.js 18+ - npm 9+*
    - [Требования](README (3).md#требования) — *- Node.js 18+ - npm 9+*
    - [Установка зависимостей](README (3).md#установка-зависимостей) — *```bash cd frontend npm install ```*
    - [Запуск для разработки](README (3).md#запуск-для-разработки) — *```bash npm run dev ```*
    - [Сборка для продакшена](README (3).md#сборка-для-продакшена) — *```bash npm run build ```*
  - [🎨 Компоненты](README (3).md#--компоненты) — *- **AppLayout** - основной макет приложения - **Sidebar** - боковая навигация*
    - [1. Layout Components](README (3).md#1--layout-components) — *- **AppLayout** - основной макет приложения - **Sidebar** - боковая навигация - **Header** - шапка с...*
    - [2. Business Components](README (3).md#2--business-components) — *- **OrganizationBuilder** - drag & drop конструктор структур - **SpecialtySelector** - выбор должнос...*
    - [3. Common Components](README (3).md#3--common-components) — *- **DataTable** - таблицы с данными - **SearchInput** - поиск с автодополнением - **FileUpload** - з...*
  - [🔄 Управление состоянием](README (3).md#--управление-состоянием) — *```typescript interface AppState {*
    - [Zustand Store](README (3).md#zustand-store) — *```typescript interface AppState { user: User | null; currentCompany: Company | null;*
    - [React Query](README (3).md#react-query) — *- Кэширование API запросов - Автоматическое обновление данных - Оптимистичные обновления - Обработка...*
  - [🧪 Тестирование](README (3).md#--тестирование) — *Тесты расположены в каталоге `tests` и используют **Vitest** совместно с **Testing Library**.  ```b*
- [Запуск всех тестов](README (3).md#запуск-всех-тестов) — *npm test  npm run test:ui*
- [Интерактивный режим](README (3).md#интерактивный-режим) — *npm run test:ui  npm run test:coverage*
- [Отчёт по покрытию](README (3).md#отчёт-по-покрытию) — *npm run test:coverage ```*
    - [Типы тестов](README (3).md#типы-тестов) — *- **Unit тесты** - компоненты и утилиты - **Integration тесты** - взаимодействие компонентов - **E2E...*
  - [📱 Адаптивность](README (3).md#--адаптивность) — *- Поддержка мобильных устройств - Responsive дизайн - Touch-friendly интерфейс*
  - [🎯 Ключевые функции](README (3).md#--ключевые-функции) — *- Создание организационных структур - Перетаскивание должностей*
    - [1. Drag & Drop Builder](README (3).md#1--drag---drop-builder) — *- Создание организационных структур - Перетаскивание должностей - Визуальное редактирование*
    - [2. Smart Recommendations](README (3).md#2--smart-recommendations) — *- AI-powered предложения - Контекстные подсказки - Автоматическое заполнение*
    - [3. Document Management](README (3).md#3--document-management) — *- Шаблоны документов - Предварительный просмотр - Экспорт в различные форматы*
    - [4. Workflow Designer](README (3).md#4--workflow-designer) — *- Визуальный редактор процессов - Настройка маршрутов согласования - Мониторинг статусов*
  - [🔒 Безопасность](README (3).md#--безопасность) — *- JWT токены в httpOnly cookies - CSRF protection - XSS защита*
  - [📊 Аналитика](README (3).md#--аналитика) — *- Отслеживание пользовательских действий - Метрики производительности - A/B тестирование*

### ✏️ 👤 [Security Architecture](security.md)
**File ID:** `security-10889e1e`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Security Architecture](security.md#security-architecture) — *The CoreTwin Platform implements a comprehensive security architecture designed to protect user da*
  - [Overview](security.md#overview) — *The CoreTwin Platform implements a comprehensive security architecture designed to protect user dat*
  - [Authentication & Authorization](security.md#authentication---authorization) — *The platform uses JSON Web Tokens (JWT) for stateless authentication:*
    - [JWT Token System](security.md#jwt-token-system) — *The platform uses JSON Web Tokens (JWT) for stateless authentication:  - **Access Tokens**: Short-l*
    - [Password Security](security.md#password-security) — *- **Hashing**: bcrypt with configurable salt rounds - **Validation**: Strong password requirements*
    - [Role-Based Access Control (RBAC)](security.md#role-based-access-control--rbac-) — *- **User Roles**: Admin, Manager, Employee with hierarchical permissions - **Resource Protection**:*
  - [Data Protection](security.md#data-protection) — *- **Connection Encryption**: TLS/SSL for database connections*
    - [Database Security](security.md#database-security) — *- **Connection Encryption**: TLS/SSL for database connections - **Query Protection**: SQLAlchemy OR*
    - [API Security](security.md#api-security) — *- **Input Validation**: Pydantic schemas validate all input data - **Rate Limiting**: Protection ag*
    - [Data Encryption](security.md#data-encryption) — *- **At Rest**: Database encryption for sensitive fields - **In Transit**: HTTPS/TLS for all communi*
  - [Infrastructure Security](security.md#infrastructure-security) — *- **Base Images**: Minimal, regularly updated base images*
    - [Container Security](security.md#container-security) — *- **Base Images**: Minimal, regularly updated base images - **Vulnerability Scanning**: Automated s*
    - [Network Security](security.md#network-security) — *- **Firewall Rules**: Restrictive network access policies - **VPC Configuration**: Isolated network*
    - [Monitoring & Logging](security.md#monitoring---logging) — *- **Security Events**: Comprehensive logging of authentication events - **Anomaly Detection**: Moni*
  - [Compliance & Standards](security.md#compliance---standards) — *- **GDPR Compliance**: User data protection and privacy rights*
    - [Data Privacy](security.md#data-privacy) — *- **GDPR Compliance**: User data protection and privacy rights - **Data Minimization**: Collection*
    - [Security Standards](security.md#security-standards) — *- **OWASP Guidelines**: Following web application security best practices - **ISO 27001**: Informat*
  - [Security Policies](security.md#security-policies) — *- **Secure Coding**: Security-first development practices*
    - [Development Security](security.md#development-security) — *- **Secure Coding**: Security-first development practices - **Code Review**: Mandatory security rev*
    - [Operational Security](security.md#operational-security) — *- **Access Management**: Strict access controls for production systems - **Incident Response**: Def*
  - [Security Testing](security.md#security-testing) — *- **Static Analysis**: Code security scanning in CI/CD pipeline*
    - [Automated Testing](security.md#automated-testing) — *- **Static Analysis**: Code security scanning in CI/CD pipeline - **Dynamic Testing**: Runtime secu*
    - [Manual Testing](security.md#manual-testing) — *- **Penetration Testing**: Regular security assessments - **Code Audits**: Manual security code rev*
  - [Incident Response](security.md#incident-response) — *- **Real-time Monitoring**: Continuous security monitoring*
    - [Detection](security.md#detection) — *- **Real-time Monitoring**: Continuous security monitoring - **Alert Systems**: Automated incident*
    - [Response Procedures](security.md#response-procedures) — *- **Incident Classification**: Severity-based response procedures - **Containment**: Immediate thre*
  - [Security Configuration](security.md#security-configuration) — *```env*
    - [Environment Variables](security.md#environment-variables) — *```env JWT_SECRET_KEY=${JWT_SECRET_KEY}*
- [JWT Configuration](security.md#jwt-configuration) — *JWT_SECRET_KEY=${JWT_SECRET_KEY} JWT_ALGORITHM=HS256 JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_...*
- [Database Security](security.md#database-security) — *DATABASE_SSL_MODE=require DATABASE_SSL_CERT_PATH=/path/to/cert DATABASE_SSL_KEY_PATH=/path/to/key*
- [API Security](security.md#api-security) — *CORS_ORIGINS=["https://app.coretwin.com"] RATE_LIMIT_REQUESTS_PER_MINUTE=100 ```*
    - [Security Headers](security.md#security-headers) — *- **HSTS**: HTTP Strict Transport Security - **CSP**: Content Security Policy - **X-Frame-Options***
  - [Related Documentation](security.md#related-documentation) — *- [Authentication API](../api/authentication.md) - [Development Setup](../development/setup.md) - [*

### ✏️ 👤 [Shared Components](README (1).md)
**File ID:** `readme--1--b5ac9c2c`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Shared Components](README (1).md#shared-components) — *Общие компоненты, типы и утилиты, используемые как в backend, так и в frontend частях платформы Cor*
  - [📁 Структура](README (1).md#--структура) — *``` shared/ ├── types/           # TypeScript типы и интерфейсы*
  - [🔧 Типы данных](README (1).md#--типы-данных) — *- **User** - пользователь системы - **Company** - организация*
    - [Основные интерфейсы](README (1).md#основные-интерфейсы) — *- **User** - пользователь системы - **Company** - организация - **Specialty** - должность из справоч...*
    - [ISCO-08 типы](README (1).md#isco-08-типы) — *- **ISCOCode** - коды классификации профессий - **SkillLevel** - уровни квалификации - **OccupationG...*
  - [🛠️ Утилиты](README (1).md#---утилиты) — *- Проверка ISCO кодов2 - Валидация email адресов*
    - [Валидация](README (1).md#валидация) — *- Проверка ISCO кодов2 - Валидация email адресов - Проверка паролей*
    - [Форматирование](README (1).md#форматирование) — *- Форматирование дат - Обработка текста - Конвертация данных*
  - [📊 Константы](README (1).md#--константы) — *- Роли пользователей - Статусы документов*
    - [Системные константы](README (1).md#системные-константы) — *- Роли пользователей - Статусы документов - Типы уведомлений - Коды ошибок*
    - [ISCO-08 константы](README (1).md#isco-08-константы) — *- Основные группы профессий - Уровни квалификации - Отраслевые коды*

### ✏️ 👤 [Users API](users.md)
**File ID:** `users-e559b9f9`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Users API](users.md#users-api) — *The users API provides functionality for managing user accounts and profiles in the CoreTwin Platf*
  - [Overview](users.md#overview) — *The users API provides functionality for managing user accounts and profiles in the CoreTwin Platfo*
  - [Endpoints](users.md#endpoints) — *Get list of all users (admin only).*
    - [GET /api/v1/users/](users.md#get--api-v1-users-) — *Get list of all users (admin only).  **Headers:***
    - [GET /api/v1/users/{user_id}](users.md#get--api-v1-users--user_id-) — *Get specific user information.  **Headers:***
  - [Related Documentation](users.md#related-documentation) — *- [Authentication API](authentication.md) - [Companies API](companies.md) - [Security Architecture]*

### ✏️ 👤 [manifest_digital_twins](manifest_digital_twins.md)
**File ID:** `manifest_digital_twins-5b8de75b`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [manifest_documentation](manifest_documentation.md)
**File ID:** `manifest_documentation-c4b0da41`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 🤖 [manifest_ethics_ai_moderation](manifest_ethics_ai_moderation.md)
**File ID:** `manifest_ethics_ai_moderation-19d49f65`  
**Автор:** ai | **Редактируемый:** Да


### ✏️ 👤 [manifest_international_standards](manifest_international_standards.md)
**File ID:** `manifest_international_standards-d5e331e8`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [manifest_knowledge_management](manifest_knowledge_management.md)
**File ID:** `manifest_knowledge_management-c858c55a`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [manifest_knowledge_management (1)](manifest_knowledge_management (1).md)
**File ID:** `manifest_knowledge_management--1--c858c55a`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [manifest_scalability_reuse](manifest_scalability_reuse.md)
**File ID:** `manifest_scalability_reuse-de05fcdc`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [manifest_security](manifest_security.md)
**File ID:** `manifest_security-20405e8c`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [manifest_testing](manifest_testing.md)
**File ID:** `manifest_testing-9754597e`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [manifest_ui_design](manifest_ui_design.md)
**File ID:** `manifest_ui_design-b6a7ad0f`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [manifest_versioning](manifest_versioning.md)
**File ID:** `manifest_versioning-f43e4861`  
**Автор:** human | **Редактируемый:** Да


### ✏️ 👤 [Архитектура CoreTwin Platform](overview.md)
**File ID:** `overview-0b297153`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Архитектура CoreTwin Platform](overview.md#архитектура-coretwin-platform) — *CoreTwin Platform представляет собой модульную систему для создания цифрового двойника организации*
  - [Обзор системы](overview.md#обзор-системы) — *CoreTwin Platform представляет собой модульную систему для создания цифрового двойника организации,*
  - [Архитектурные принципы](overview.md#архитектурные-принципы) — *- Четкое разделение на backend и frontend - Независимые сервисы по доменам*
    - [1. Модульность](overview.md#1--модульность) — *- Четкое разделение на backend и frontend - Независимые сервисы по доменам - Слабая связанность межд...*
    - [2. Масштабируемость](overview.md#2--масштабируемость) — *- Горизонтальное масштабирование сервисов - Кеширование с Redis - Асинхронная обработка с Celery*
    - [3. Безопасность](overview.md#3--безопасность) — *- JWT аутентификация - RBAC авторизация - Валидация данных на всех уровнях*
  - [Компоненты системы](overview.md#компоненты-системы) — *``` backend/*
    - [Backend (Python/FastAPI)](overview.md#backend--python-fastapi-) — *``` backend/ ├── app/                    # Основное приложение │   ├── api/               # REST API...*
    - [Frontend (React/TypeScript)](overview.md#frontend--react-typescript-) — *``` frontend/ ├── src/ │   ├── components/       # React компоненты*
    - [База данных](overview.md#база-данных) — *- **PostgreSQL** - основная база данных - **Redis** - кеширование и сессии - **ClickHouse** - аналит...*
  - [Потоки данных](overview.md#потоки-данных) — *1. Пользователь отправляет credentials 2. Backend проверяет данные*
    - [Аутентификация](overview.md#аутентификация) — *1. Пользователь отправляет credentials 2. Backend проверяет данные 3. Генерируется JWT токен 4. Токе...*
    - [API запросы](overview.md#api-запросы) — *1. Frontend отправляет HTTP запрос 2. Middleware проверяет авторизацию 3. Валидация данных через Pyd...*
  - [Безопасность](overview.md#безопасность) — *- JWT токены с коротким временем жизни - Refresh токены для обновления*
    - [Аутентификация](overview.md#аутентификация) — *- JWT токены с коротким временем жизни - Refresh токены для обновления - Хеширование паролей с bcryp...*
    - [Авторизация](overview.md#авторизация) — *- Role-Based Access Control (RBAC) - Проверка прав на уровне API - Изоляция данных по компаниям*
    - [Валидация](overview.md#валидация) — *- Pydantic схемы для входящих данных - SQLAlchemy модели с ограничениями - Санитизация пользовательс...*
  - [Мониторинг и логирование](overview.md#мониторинг-и-логирование) — *- JSON формат логов - Категоризация по типам ошибок*
    - [Структурированное логирование](overview.md#структурированное-логирование) — *- JSON формат логов - Категоризация по типам ошибок - Ротация файлов логов - Фильтрация чувствительн...*
    - [Метрики](overview.md#метрики) — *- Время ответа API - Количество запросов - Ошибки и исключения - Использование ресурсов*
  - [Развертывание](overview.md#развертывание) — *- Docker контейнеры для всех сервисов - Docker Compose для локальной разработки*
    - [Контейнеризация](overview.md#контейнеризация) — *- Docker контейнеры для всех сервисов - Docker Compose для локальной разработки - Kubernetes для про...*
    - [CI/CD](overview.md#ci-cd) — *- GitHub Actions для автоматизации - Автоматические тесты - Деплой документации - Security scanning*
  - [Интеграции](overview.md#интеграции) — *- Интеграция с ИИ-сервисами - Обмен контекстом между системами*
    - [Model Context Protocol (MCP)](overview.md#model-context-protocol--mcp-) — *- Интеграция с ИИ-сервисами - Обмен контекстом между системами - Стандартизированный протокол*
    - [Внешние API](overview.md#внешние-api) — *- Интеграция с HR системами - Синхронизация справочников - Экспорт/импорт данных*
  - [Производительность](overview.md#производительность) — *- Redis для сессий пользователей - Кеширование справочников*
    - [Кеширование](overview.md#кеширование) — *- Redis для сессий пользователей - Кеширование справочников - Кеширование результатов запросов*
    - [Оптимизация БД](overview.md#оптимизация-бд) — *- Индексы на часто используемых полях - Пагинация для больших списков - Ленивая загрузка связанных д...*
  - [Будущие улучшения](overview.md#будущие-улучшения) — *- Выделение отдельных сервисов по доменам - Service mesh для коммуникации*
    - [Микросервисы](overview.md#микросервисы) — *- Выделение отдельных сервисов по доменам - Service mesh для коммуникации - Распределенная трассиров...*
    - [Аналитика](overview.md#аналитика) — *- Интеграция с ClickHouse - Дашборды и отчеты - Машинное обучение для рекомендаций*

### ✏️ 👤 [База специальностей и профессий (ISCO-08) с сопоставлением отраслей (ISIC Rev.4)](industries-classification (1).md)
**File ID:** `industries-classification--1--6cb07d03`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [База специальностей и профессий (ISCO-08) с сопоставлением отраслей (ISIC Rev.4)](industries-classification (1).md#база-специальностей-и-профессий--isco-08--с-сопоставлением-отраслей--isic-rev-4-) — *В качестве основы взяты международные классификации:*
  - [Используемые стандарты и структура классификации](industries-classification (1).md#используемые-стандарты-и-структура-классификации) — *В качестве основы взяты международные классификации: - **ISCO-08** (International Standard Classifi*
  - [Структура ISCO-08](industries-classification (1).md#структура-isco-08) — *ISCO-08 организует профессии и должности в иерархию по двум основным признакам: - **Уровень квалифи*
    - [Основные группы ISCO-08:](industries-classification (1).md#основные-группы-isco-08-) — ***1. Руководители (Managers)** - 11 Руководители высшего звена, высшие должностные лица и законодат*
  - [Структура ISIC Rev.4](industries-classification (1).md#структура-isic-rev-4) — ***A. Сельское, лесное и рыбное хозяйство***
    - [Разделы экономической деятельности:](industries-classification (1).md#разделы-экономической-деятельности-) — ***A. Сельское, лесное и рыбное хозяйство** - 01 Растениеводство и животноводство, охота - 02 Лесово*
  - [Применение в CoreTwin Platform](industries-classification (1).md#применение-в-coretwin-platform) — *1. **Справочник должностей** основан на ISCO-08 кодах*
    - [Интеграция стандартов](industries-classification (1).md#интеграция-стандартов) — *1. **Справочник должностей** основан на ISCO-08 кодах 2. **Отраслевая привязка** использует ISIC Re*
    - [Техническая реализация](industries-classification (1).md#техническая-реализация) — *```sql -- Таблица отраслей на базе ISIC Rev.4 CREATE TABLE industries (*
    - [Использование в рекомендациях](industries-classification (1).md#использование-в-рекомендациях) — *- **Отраслевые модули**: Рекомендации модулей на основе отрасли компании - **Специфические должност*

### ✏️ 👤 [База специальностей и профессий (ISCO-08) с сопоставлением отраслей (ISIC Rev.4)](industries-classification (2).md)
**File ID:** `industries-classification--2--72905eb2`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [База специальностей и профессий (ISCO-08) с сопоставлением отраслей (ISIC Rev.4)](industries-classification (2).md#база-специальностей-и-профессий--isco-08--с-сопоставлением-отраслей--isic-rev-4-) — *В качестве основы взяты международные классификации:*
  - [Используемые стандарты и структура классификации](industries-classification (2).md#используемые-стандарты-и-структура-классификации) — *В качестве основы взяты международные классификации: - **ISCO-08** (International Standard Classifi*
  - [Структура ISCO-08](industries-classification (2).md#структура-isco-08) — *ISCO-08 организует профессии и должности в иерархию по двум основным признакам: - **Уровень квалифи*
    - [Основные группы ISCO-08:](industries-classification (2).md#основные-группы-isco-08-) — ***1. Руководители (Managers)** - 11 Руководители высшего звена, высшие должностные лица и законодат*
  - [Структура ISIC Rev.4](industries-classification (2).md#структура-isic-rev-4) — ***A. Сельское, лесное и рыбное хозяйство***
    - [Разделы экономической деятельности:](industries-classification (2).md#разделы-экономической-деятельности-) — ***A. Сельское, лесное и рыбное хозяйство** - 01 Растениеводство и животноводство, охота - 02 Лесово*
  - [Применение в CoreTwin Platform](industries-classification (2).md#применение-в-coretwin-platform) — *1. **Справочник должностей** основан на ISCO-08 кодах*
    - [Интеграция стандартов](industries-classification (2).md#интеграция-стандартов) — *1. **Справочник должностей** основан на ISCO-08 кодах 2. **Отраслевая привязка** использует ISIC Re*
    - [Техническая реализация](industries-classification (2).md#техническая-реализация) — *```sql -- Таблица отраслей на базе ISIC Rev.4 CREATE TABLE industries (*
    - [Использование в рекомендациях](industries-classification (2).md#использование-в-рекомендациях) — *- **Отраслевые модули**: Рекомендации модулей на основе отрасли компании - **Специфические должност*

### ✏️ 👤 [База специальностей и профессий (ISCO-08) с сопоставлением отраслей (ISIC Rev.4)](industries-classification.md)
**File ID:** `industries-classification-ef788415`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [База специальностей и профессий (ISCO-08) с сопоставлением отраслей (ISIC Rev.4)](industries-classification.md#база-специальностей-и-профессий--isco-08--с-сопоставлением-отраслей--isic-rev-4-) — *В качестве основы взяты международные классификации:*
  - [Используемые стандарты и структура классификации](industries-classification.md#используемые-стандарты-и-структура-классификации) — *В качестве основы взяты международные классификации: - **ISCO-08** (International Standard Classifi*
  - [Структура ISCO-08](industries-classification.md#структура-isco-08) — *ISCO-08 организует профессии и должности в иерархию по двум основным признакам: - **Уровень квалифи*
    - [Основные группы ISCO-08:](industries-classification.md#основные-группы-isco-08-) — ***1. Руководители (Managers)** - 11 Руководители высшего звена, высшие должностные лица и законодат*
  - [Структура ISIC Rev.4](industries-classification.md#структура-isic-rev-4) — ***A. Сельское, лесное и рыбное хозяйство***
    - [Разделы экономической деятельности:](industries-classification.md#разделы-экономической-деятельности-) — ***A. Сельское, лесное и рыбное хозяйство** - 01 Растениеводство и животноводство, охота - 02 Лесово*
  - [Применение в CoreTwin Platform](industries-classification.md#применение-в-coretwin-platform) — *1. **Справочник должностей** основан на ISCO-08 кодах*
    - [Интеграция стандартов](industries-classification.md#интеграция-стандартов) — *1. **Справочник должностей** основан на ISCO-08 кодах 2. **Отраслевая привязка** использует ISIC Re*
    - [Техническая реализация](industries-classification.md#техническая-реализация) — *```sql -- Таблица отраслей на базе ISIC Rev.4 CREATE TABLE industries (*
    - [Использование в рекомендациях](industries-classification.md#использование-в-рекомендациях) — *- **Отраслевые модули**: Рекомендации модулей на основе отрасли компании - **Специфические должност*

### ✏️ 👤 [Глобальный справочник должностей CoreTwin Platform](job-directory.md)
**File ID:** `job-directory-eeb16609`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Глобальный справочник должностей CoreTwin Platform](job-directory.md#глобальный-справочник-должностей-coretwin-platform) — *Глобальный справочник должностей CoreTwin Platform представляет собой комплексную базу данных спец*
  - [Обзор справочника](job-directory.md#обзор-справочника) — *Глобальный справочник должностей CoreTwin Platform представляет собой комплексную базу данных специ*
  - [🎯 Назначение и цели](job-directory.md#--назначение-и-цели) — *1. **Стандартизация должностей** - единый подход к описанию ролей в организации 2. **Автоматические*
    - [Основные функции справочника:](job-directory.md#основные-функции-справочника-) — *1. **Стандартизация должностей** - единый подход к описанию ролей в организации 2. **Автоматические*
    - [Целевые пользователи:](job-directory.md#целевые-пользователи-) — *- **HR-специалисты** - для создания должностных инструкций - **Руководители** - для планирования орг...*
  - [📊 Структура данных](job-directory.md#--структура-данных)
    - [Основные сущности](job-directory.md#основные-сущности) — *```sql CREATE TABLE specialties (*
      - [1. Specialties (Специальности)](job-directory.md#1--specialties--специальности-) — *```sql CREATE TABLE specialties ( id UUID PRIMARY KEY DEFAULT gen_random_uuid(), isco_code VARCHAR(1...*
      - [2. Duties (Функциональные обязанности)](job-directory.md#2--duties--функциональные-обязанности-) — *```sql CREATE TABLE duties ( id UUID PRIMARY KEY DEFAULT gen_random_uuid(), name VARCHAR(255) NOT NU...*
      - [3. Specialty-Duties Relations (Связи специальностей и обязанностей)](job-directory.md#3--specialty-duties-relations--связи-специальностей-и-обязанностей-) — *```sql CREATE TABLE specialty_duties ( id UUID PRIMARY KEY DEFAULT gen_random_uuid(), specialty_id U...*
  - [🌍 Международные стандарты](job-directory.md#--международные-стандарты) — *Справочник полностью интегрирован с **Международной стандартной классификацией занятий ISCO-08**:*
    - [ISCO-08 Integration](job-directory.md#isco-08-integration) — *Справочник полностью интегрирован с **Международной стандартной классификацией занятий ISCO-08**:  -...*
      - [Иерархическая структура:](job-directory.md#иерархическая-структура-) — *- **Уровень 1**: Основные группы (1-9, 0) - **Уровень 2**: Подгруппы (двузначные коды) - **Уровень 3...*
      - [Примеры специальностей по группам:](job-directory.md#примеры-специальностей-по-группам-) — ***1. Руководители** - 1120 Руководители высшего звена - 1211 Финансовые директора*
  - [🔧 Функциональные возможности](job-directory.md#--функциональные-возможности) — *- **Текстовый поиск** по названиям и описаниям - **Фильтрация по ISCO кодам** и уровням квалификаци*
    - [1. Поиск и фильтрация](job-directory.md#1--поиск-и-фильтрация) — *- **Текстовый поиск** по названиям и описаниям - **Фильтрация по ISCO кодам** и уровням квалификации...*
    - [2. Генерация рекомендаций](job-directory.md#2--генерация-рекомендаций) — *- Автоматические предложения модулей на основе выбранных должностей - Рекомендации шаблонов документ...*
    - [3. Кастомизация компаний](job-directory.md#3--кастомизация-компаний) — *- Добавление собственных должностей и обязанностей - Адаптация под отраслевую специфику - Локализаци...*
  - [🔄 Интеграция с MCP](job-directory.md#--интеграция-с-mcp) — *Справочник должностей активно использует возможности Model Context Protocol для:*
    - [AI-модерация новых должностей](job-directory.md#ai-модерация-новых-должностей) — *- Проверка корректности названий и описаний - Сопоставление с существующими специальностями - Предло...*
    - [Интеллектуальные рекомендации](job-directory.md#интеллектуальные-рекомендации) — *- Анализ потребностей компании на основе выбранных должностей - Предложение дополнительных специальн...*
  - [📈 Метрики и аналитика](job-directory.md#--метрики-и-аналитика) — *- Статистика использования должностей - Тренды в различных отраслях*
    - [Популярность специальностей](job-directory.md#популярность-специальностей) — *- Статистика использования должностей - Тренды в различных отраслях - Региональные особенности - Сез...*
    - [Эффективность рекомендаций](job-directory.md#эффективность-рекомендаций) — *- Процент принятых предложений - Время создания структуры - Удовлетворенность пользователей - ROI от...*

### ✏️ 🤖 [Детальный план разработки платформы CoreTwin](development-plan.md)
**File ID:** `development-plan-18eefc30`  
**Автор:** ai | **Редактируемый:** Да

**Структура заголовков:**
- [Детальный план разработки платформы CoreTwin](development-plan.md#детальный-план-разработки-платформы-coretwin) — **Версия: 1.0* *Дата: 26 июня 2025* *Автор: Devin AI**
  - [Оглавление](development-plan.md#оглавление) — *1. [Анализ архитектуры и ключевых требований](#1-анализ-архитектуры-и-ключевых-требований) 2. [Техн*
  - [1. Анализ архитектуры и ключевых требований](development-plan.md#1--анализ-архитектуры-и-ключевых-требований) — ***CoreTwin Platform** — это комплексная платформа для создания цифрового двойника организации, пре*
    - [1.1 Общая концепция](development-plan.md#1-1-общая-концепция) — ***CoreTwin Platform** — это комплексная платформа для создания цифрового двойника организации, пред*
    - [1.2 Ключевые модули системы](development-plan.md#1-2-ключевые-модули-системы) — *1. **Specialties & Duties Management** - Глобальный справочник должностей (специальностей) - Справо*
  - [2. Техническая архитектура](development-plan.md#2--техническая-архитектура) — *```*
    - [2.1 Общая архитектура системы](development-plan.md#2-1-общая-архитектура-системы) — *``` ┌─────────────────────────────────────────────────────────────┐ │                    Frontend (*
    - [2.2 Backend Architecture (FastAPI + SQLAlchemy)](development-plan.md#2-2-backend-architecture--fastapi---sqlalchemy-) — *``` backend/ ├── core/                           # Ядро системы*
    - [2.3 Frontend Architecture (React + TypeScript)](development-plan.md#2-3-frontend-architecture--react---typescript-) — *``` frontend/ ├── src/*
  - [3. Модель данных](development-plan.md#3--модель-данных)
    - [3.1 Основные сущности и связи](development-plan.md#3-1-основные-сущности-и-связи) — *```sql*
      - [3.1.1 Компании и пользователи (Мультитенантность)](development-plan.md#3-1-1-компании-и-пользователи--мультитенантность-) — *```sql -- Компании (основа мультитенантности) CREATE TABLE companies (*
      - [3.1.2 Справочники (Глобальные данные)](development-plan.md#3-1-2-справочники--глобальные-данные-) — *```sql -- Отрасли экономики (ISIC Rev.4) CREATE TABLE industries (*
      - [3.1.3 Организационные структуры](development-plan.md#3-1-3-организационные-структуры) — *```sql -- Подразделения компании CREATE TABLE company_units (*
  - [4. API Design](development-plan.md#4--api-design)
    - [4.1 REST API Endpoints](development-plan.md#4-1-rest-api-endpoints) — *``` POST   /api/v1/auth/login           # Вход в систему*
      - [4.1.1 Аутентификация и авторизация](development-plan.md#4-1-1-аутентификация-и-авторизация) — *``` POST   /api/v1/auth/login           # Вход в систему POST   /api/v1/auth/logout          # Выход...*
      - [4.1.2 Справочники должностей](development-plan.md#4-1-2-справочники-должностей) — *``` GET    /api/v1/specialties/         # Список должностей POST   /api/v1/specialties/         # Со...*
      - [4.1.3 Организационные структуры](development-plan.md#4-1-3-организационные-структуры) — *``` GET    /api/v1/orgstructure/units/  # Подразделения компании POST   /api/v1/orgstructure/units/*
      - [4.1.4 Рекомендации модулей](development-plan.md#4-1-4-рекомендации-модулей) — *``` GET    /api/v1/recommendations/     # Рекомендации для компании POST   /api/v1/recommendations/c...*
      - [4.1.5 MCP интеграция и AI](development-plan.md#4-1-5-mcp-интеграция-и-ai) — *``` POST   /api/v1/ai/moderate          # Модерация контента POST   /api/v1/ai/recommend         # A...*
  - [5. Frontend Requirements](development-plan.md#5--frontend-requirements)
    - [5.1 Ключевые UI компоненты](development-plan.md#5-1-ключевые-ui-компоненты) — *- **React Flow** + **Rete.js** для реализации drag & drop функциональности - **Визуальный редактор**
      - [5.1.1 Drag & Drop конструктор организационных структур](development-plan.md#5-1-1-drag---drop-конструктор-организационных-структур) — *- **React Flow** + **Rete.js** для реализации drag & drop функциональности - **Визуальный редактор**...*
      - [5.1.2 Панель рекомендаций модулей](development-plan.md#5-1-2-панель-рекомендаций-модулей) — *- **Интеллектуальные предложения** на основе выбранных должностей - **Карточки модулей** с описанием...*
    - [5.2 Технологический стек Frontend](development-plan.md#5-2-технологический-стек-frontend) — *- **React 18+** с TypeScript для типобезопасности - **Vite** как сборщик и dev-сервер*
      - [5.2.1 Основные технологии](development-plan.md#5-2-1-основные-технологии) — *- **React 18+** с TypeScript для типобезопасности - **Vite** как сборщик и dev-сервер - **React Rout...*
      - [5.2.2 UI библиотеки и компоненты](development-plan.md#5-2-2-ui-библиотеки-и-компоненты) — *- **Ant Design** или **Material-UI** для базовых компонентов - **React Flow** + **Rete.js** для drag...*
  - [6. Интеграции](development-plan.md#6--интеграции)
    - [6.1 Model Context Protocol (MCP) интеграция](development-plan.md#6-1-model-context-protocol--mcp--интеграция) — *- **Автоматическая проверка** названий должностей и описаний - **Выявление некорректного контента***
      - [6.1.1 Модерация пользовательского контента](development-plan.md#6-1-1-модерация-пользовательского-контента) — *- **Автоматическая проверка** названий должностей и описаний - **Выявление некорректного контента***
      - [6.1.2 Интеллектуальные рекомендации](development-plan.md#6-1-2-интеллектуальные-рекомендации) — *- **AI-анализ** организационной структуры - **Персонализированные предложения** модулей и шаблонов -...*
      - [6.1.3 AI-помощник в интерфейсе](development-plan.md#6-1-3-ai-помощник-в-интерфейсе) — *- **Чат-бот** для помощи пользователям - **Контекстные подсказки** и рекомендации - **Автодополнение...*
  - [7. Инфраструктура и деплоймент](development-plan.md#7--инфраструктура-и-деплоймент)
    - [7.1 Контейнеризация и оркестрация](development-plan.md#7-1-контейнеризация-и-оркестрация) — *```dockerfile*
      - [7.1.1 Docker конфигурация](development-plan.md#7-1-1-docker-конфигурация) — *```dockerfile FROM python:3.11-slim WORKDIR /app*
- [Backend Dockerfile](development-plan.md#backend-dockerfile) — *FROM python:3.11-slim WORKDIR /app COPY requirements.txt . RUN pip install -r requirements.txt*
- [Frontend Dockerfile](development-plan.md#frontend-dockerfile) — *FROM node:18-alpine AS builder WORKDIR /app COPY package*.json ./ RUN npm ci*
    - [7.2 Хранилища данных](development-plan.md#7-2-хранилища-данных) — *- **Версия**: PostgreSQL 15+ - **Расширения**: UUID, JSONB, Full-text search*
      - [7.2.1 PostgreSQL (основная БД)](development-plan.md#7-2-1-postgresql--основная-бд-) — *- **Версия**: PostgreSQL 15+ - **Расширения**: UUID, JSONB, Full-text search - **Репликация**: Maste...*
      - [7.2.2 Redis (кэш и сессии)](development-plan.md#7-2-2-redis--кэш-и-сессии-) — *- **Кэширование**: API ответы, справочники - **Сессии**: Пользовательские сессии - **Очереди**: Фоно...*
  - [8. Фазы разработки](development-plan.md#8--фазы-разработки)
    - [8.1 Фаза 1: MVP (2-3 месяца)](development-plan.md#8-1-фаза-1--mvp--2-3-месяца-) — ***Backend:** - Настройка FastAPI проекта с базовой структурой*
      - [8.1.1 Базовая архитектура (3-4 недели)](development-plan.md#8-1-1-базовая-архитектура--3-4-недели-) — ***Backend:** - Настройка FastAPI проекта с базовой структурой - Конфигурация SQLAlchemy и Alembic дл...*
      - [8.1.4 Система документации (1-2 недели) ✅](development-plan.md#8-1-4-система-документации--1-2-недели---) — ***Инструменты документации:** ✅ - ✅ Настройка MkDocs для основной документации проекта - ✅ Конфигура...*
      - [8.1.2 Справочники и аутентификация (2-3 недели)](development-plan.md#8-1-2-справочники-и-аутентификация--2-3-недели-) — ***Backend:** - API для работы со справочниками (specialties, duties, industries) - Загрузка данных I...*
      - [8.1.3 Организационные структуры (3-4 недели)](development-plan.md#8-1-3-организационные-структуры--3-4-недели-) — ***Backend:** - Модели для организационных структур (company_units, company_positions) - API для созд...*
    - [8.2 Фаза 2: Основной функционал (3-4 месяца)](development-plan.md#8-2-фаза-2--основной-функционал--3-4-месяца-) — ***Frontend:** - Интеграция React Flow + Rete.js*
      - [8.2.1 Drag & Drop конструктор (4-5 недель)](development-plan.md#8-2-1-drag---drop-конструктор--4-5-недель-) — ***Frontend:** - Интеграция React Flow + Rete.js - Визуальный редактор структур с drag&drop - Зоны дл...*
      - [8.2.2 Recommendation Engine (5-6 недель)](development-plan.md#8-2-2-recommendation-engine--5-6-недель-) — ***Backend:** - Алгоритм расчета рекомендаций модулей - Модели duty_modules, module_archetypes - Сист...*
      - [8.2.3 Шаблоны документов (4-5 недель)](development-plan.md#8-2-3-шаблоны-документов--4-5-недель-) — ***Backend:** - Модели document_templates, duty_templates - API для управления шаблонами - Система пе...*
    - [8.3 Фаза 3: Продвинутые функции (2-3 месяца)](development-plan.md#8-3-фаза-3--продвинутые-функции--2-3-месяца-) — ***Backend:** - Модели approval_workflows, document_approvals*
      - [8.3.1 Маршруты согласования (5-6 недель)](development-plan.md#8-3-1-маршруты-согласования--5-6-недель-) — ***Backend:** - Модели approval_workflows, document_approvals - Движок выполнения workflow - Система*
      - [8.3.2 MCP интеграция (4-5 недель)](development-plan.md#8-3-2-mcp-интеграция--4-5-недель-) — ***Backend:** - MCP клиент для взаимодействия с AI - Модерация пользовательского контента - AI рекоме...*
      - [8.3.3 Аналитика и отчеты (3-4 недели)](development-plan.md#8-3-3-аналитика-и-отчеты--3-4-недели-) — ***Backend:** - ClickHouse интеграция - Сбор метрик использования - Аудит действий пользователей*
    - [8.4 Фаза 4: Масштабирование и оптимизация (1-2 месяца)](development-plan.md#8-4-фаза-4--масштабирование-и-оптимизация--1-2-месяца-) — *- Оптимизация запросов к БД - Кэширование на разных уровнях*
      - [8.4.1 Производительность (3-4 недели)](development-plan.md#8-4-1-производительность--3-4-недели-) — *- Оптимизация запросов к БД - Кэширование на разных уровнях - Индексы и партиционирование - Оптимиза...*
      - [8.4.2 Безопасность и соответствие (2-3 недели)](development-plan.md#8-4-2-безопасность-и-соответствие--2-3-недели-) — *- Аудит безопасности - GDPR соответствие - Шифрование данных - Логирование безопасности*
      - [8.4.3 Интеграции и API (2-3 недели)](development-plan.md#8-4-3-интеграции-и-api--2-3-недели-) — *- REST API документация (OpenAPI/Swagger) - Webhooks для внешних систем - SDK для популярных языков*
  - [9. Лучшие практики и рекомендации](development-plan.md#9--лучшие-практики-и-рекомендации)
    - [9.1 Разработка](development-plan.md#9-1-разработка) — *- **Используйте Pydantic** для валидации данных и сериализации - **Применяйте dependency injection**
      - [9.1.1 Backend](development-plan.md#9-1-1-backend) — *- **Используйте Pydantic** для валидации данных и сериализации - **Применяйте dependency injection**...*
      - [9.1.2 Frontend](development-plan.md#9-1-2-frontend) — *- **Используйте TypeScript** строго - избегайте any - **Применяйте React Query** для управления серв...*
      - [9.1.3 База данных](development-plan.md#9-1-3-база-данных) — *- **Используйте миграции** для всех изменений схемы - **Применяйте индексы** для часто запрашиваемых...*
    - [9.2 Тестирование](development-plan.md#9-2-тестирование) — *- **Unit тесты** для бизнес-логики (pytest) - **Integration тесты** для API эндпоинтов*
      - [9.2.1 Backend тестирование](development-plan.md#9-2-1-backend-тестирование) — *- **Unit тесты** для бизнес-логики (pytest) - **Integration тесты** для API эндпоинтов - **Database*
      - [9.2.2 Frontend тестирование](development-plan.md#9-2-2-frontend-тестирование) — *- **Unit тесты** для утилит и хуков (Jest) - **Component тесты** с React Testing Library - **E2E тес...*
    - [9.3 Деплоймент и DevOps](development-plan.md#9-3-деплоймент-и-devops) — *- **Автоматические тесты** на каждый PR - **Линтинг и форматирование** кода*
      - [9.3.1 CI/CD](development-plan.md#9-3-1-ci-cd) — *- **Автоматические тесты** на каждый PR - **Линтинг и форматирование** кода - **Security scanning***
      - [9.3.2 Мониторинг](development-plan.md#9-3-2-мониторинг) — *- **Application Performance Monitoring** (APM) - **Error tracking** и алертинг - **Business metrics*...*
  - [10. Риски и митигация](development-plan.md#10--риски-и-митигация)
    - [10.1 Технические риски](development-plan.md#10-1-технические-риски) — ***Риск**: Медленная работа с большими организационными структурами **Митигация**:*
      - [10.1.1 Производительность](development-plan.md#10-1-1-производительность) — ***Риск**: Медленная работа с большими организационными структурами **Митигация**: - Виртуализация сп...*
      - [10.1.2 Масштабируемость](development-plan.md#10-1-2-масштабируемость) — ***Риск**: Неспособность обслуживать большое количество пользователей **Митигация**: - Микросервисная...*
      - [10.1.3 Интеграция с MCP](development-plan.md#10-1-3-интеграция-с-mcp) — ***Риск**: Нестабильность или недоступность MCP сервисов **Митигация**: - Graceful degradation при не...*
    - [10.2 Бизнес риски](development-plan.md#10-2-бизнес-риски) — ***Риск**: Пользователи не смогут эффективно использовать drag&drop конструктор **Митигация**:*
      - [10.2.1 Сложность пользовательского интерфейса](development-plan.md#10-2-1-сложность-пользовательского-интерфейса) — ***Риск**: Пользователи не смогут эффективно использовать drag&drop конструктор **Митигация**: - Exte...*
      - [10.2.2 Качество данных](development-plan.md#10-2-2-качество-данных) — ***Риск**: Некачественные данные в справочниках ISCO-08/ISIC Rev.4 **Митигация**: - Валидация данных*
    - [10.3 Безопасность](development-plan.md#10-3-безопасность) — ***Риск**: Несанкционированный доступ к данным компаний **Митигация**:*
      - [10.3.1 Утечка данных](development-plan.md#10-3-1-утечка-данных) — ***Риск**: Несанкционированный доступ к данным компаний **Митигация**: - Строгая мультитенантность -*
      - [10.3.2 GDPR соответствие](development-plan.md#10-3-2-gdpr-соответствие) — ***Риск**: Нарушение требований GDPR **Митигация**: - Data anonymization - Right to be forgotten impl...*
  - [11. Метрики успеха](development-plan.md#11--метрики-успеха)
    - [11.1 Технические метрики](development-plan.md#11-1-технические-метрики) — *- **API Response Time**: < 200ms для 95% запросов - **Page Load Time**: < 3 секунды для первой загр*
      - [11.1.1 Производительность](development-plan.md#11-1-1-производительность) — *- **API Response Time**: < 200ms для 95% запросов - **Page Load Time**: < 3 секунды для первой загру...*
      - [11.1.2 Качество кода](development-plan.md#11-1-2-качество-кода) — *- **Test Coverage**: > 80% покрытие кода тестами - **Code Quality**: Sonar Quality Gate passed - **S...*
    - [11.2 Пользовательские метрики](development-plan.md#11-2-пользовательские-метрики) — *- **Time to Create Structure**: < 30 минут для создания базовой структуры - **User Error Rate**: <*
      - [11.2.1 Usability](development-plan.md#11-2-1-usability) — *- **Time to Create Structure**: < 30 минут для создания базовой структуры - **User Error Rate**: < 5...*
      - [11.2.2 Adoption](development-plan.md#11-2-2-adoption) — *- **Daily Active Users**: Рост на 20% месяц к месяцу - **Feature Adoption**: > 60% пользователей исп...*
    - [11.3 Бизнес метрики](development-plan.md#11-3-бизнес-метрики) — *- **Recommendation Accuracy**: > 85% релевантных рекомендаций - **Content Moderation**: > 95% точно*
      - [11.3.1 AI/MCP эффективность](development-plan.md#11-3-1-ai-mcp-эффективность) — *- **Recommendation Accuracy**: > 85% релевантных рекомендаций - **Content Moderation**: > 95% точнос...*
      - [11.3.2 Интеграции](development-plan.md#11-3-2-интеграции) — *- **API Usage**: > 1000 API calls в день - **Integration Success Rate**: > 95% успешных интеграций -...*
  - [Заключение](development-plan.md#заключение) — *Данный план разработки представляет собой комплексный подход к созданию платформы CoreTwin, основан*
  - [Статус выполнения задач](development-plan.md#статус-выполнения-задач)
    - [✅ Завершенные задачи (Декабрь 2024 - Июнь 2025)](development-plan.md#--завершенные-задачи--декабрь-2024---июнь-2025-) — *- **Статус**: ✅ Завершено - **Описание**: Реализована комплексная система управления зависимостями*
      - [🔧 Управление зависимостями и линтинг (Июнь 2025)](development-plan.md#--управление-зависимостями-и-линтинг--июнь-2025-) — *- **Статус**: ✅ Завершено - **Описание**: Реализована комплексная система управления зависимостями и...*
      - [📚 Система документации (Июнь 2025)](development-plan.md#--система-документации--июнь-2025-) — *- **Статус**: ✅ Завершено - **Описание**: Реализована комплексная система документации с автоматичес...*
      - [🔐 Система аутентификации (Декабрь 2024)](development-plan.md#--система-аутентификации--декабрь-2024-) — *- **Статус**: ✅ Завершено - **Описание**: Полнофункциональная система аутентификации с JWT токенами*
      - [🧪 Тестирование (Декабрь 2024)](development-plan.md#--тестирование--декабрь-2024-) — *- **Статус**: ✅ Завершено - **Описание**: Комплексная система тестирования с покрытием >30% - **Выпо...*
      - [🗃️ База данных PostgreSQL (Декабрь 2024)](development-plan.md#---база-данных-postgresql--декабрь-2024-) — *- **Статус**: ✅ Завершено - **Описание**: Настроена PostgreSQL с миграциями и тестовой средой - **Вы...*
      - [📝 Система логирования (Декабрь 2024)](development-plan.md#--система-логирования--декабрь-2024-) — *- **Статус**: ✅ Завершено - **Описание**: Структурированная система логирования с ротацией файлов -*
    - [🔄 Текущие задачи](development-plan.md#--текущие-задачи) — *- **Статус**: 🔄 В процессе - **Описание**: Создана базовая структура проекта с модульной архитектур*
      - [🏗️ Структура проекта и архитектура](development-plan.md#---структура-проекта-и-архитектура) — *- **Статус**: 🔄 В процессе - **Описание**: Создана базовая структура проекта с модульной архитектуро...*
    - [📋 Планируемые задачи](development-plan.md#--планируемые-задачи) — *- **Статус**: 📋 Запланировано - **Описание**: Реализация глобального справочника должностей*
      - [📊 Справочник должностей ISCO-08](development-plan.md#--справочник-должностей-isco-08) — *- **Статус**: 📋 Запланировано - **Описание**: Реализация глобального справочника должностей - **Прио...*
      - [🏢 Конструктор организационных структур](development-plan.md#--конструктор-организационных-структур) — *- **Статус**: 📋 Запланировано - **Описание**: Drag & Drop конструктор для создания оргструктур - **П...*
      - [🤖 Интеграция с MCP (Model Context Protocol)](development-plan.md#--интеграция-с-mcp--model-context-protocol-) — *- **Статус**: 📋 Запланировано - **Описание**: AI-возможности для автоматизации и рекомендаций - **Пр...*

### ✏️ 👤 [Логика модульной архитектуры на базе должностей и обязанностей](service-design.md)
**File ID:** `service-design-c6a0c7cd`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Логика модульной архитектуры на базе должностей и обязанностей](service-design.md#логика-модульной-архитектуры-на-базе-должностей-и-обязанностей) — *Построить гибкую платформу, где компании самостоятельно формируют организационную структуру, выбир*
  - [🔹 Цель](service-design.md#--цель) — *Построить гибкую платформу, где компании самостоятельно формируют организационную структуру, выбира*
  - [🧱 Ключевые сущности](service-design.md#--ключевые-сущности) — *- Универсальный список: бухгалтер, прораб, юрист, HR, и т.д. - Используется как основа структуры ко*
    - [1. specialties — Справочник должностей](service-design.md#1--specialties---справочник-должностей) — *- Универсальный список: бухгалтер, прораб, юрист, HR, и т.д. - Используется как основа структуры ком...*
    - [2. duties — Функциональные обязанности](service-design.md#2--duties---функциональные-обязанности) — *- Типовые обязанности по каждой должности (например, "Подготовка отчётности") - Могут быть системные...*
    - [3. specialty_duties — Связь должности и обязанностей](service-design.md#3--specialty_duties---связь-должности-и-обязанностей) — *- Позволяет задать важность, необходимость, приоритетность каждой функции для конкретной специальнос...*
    - [4. duty_modules — Связь обязанности и модуля](service-design.md#4--duty_modules---связь-обязанности-и-модуля) — *- Отображает, какие модули требуются для выполнения конкретной функции - Основа для автоматических р...*
    - [5. company_custom_duties — Дополнительные обязанности от компании](service-design.md#5--company_custom_duties---дополнительные-обязанности-от-компании) — *- Позволяет компаниям добавлять уникальные требования - Сохраняет связность со стандартной моделью -...*
    - [6. module_archetypes — Архетипы модулей](service-design.md#6--module_archetypes---архетипы-модулей) — *- Универсальные строительные блоки: docflow, finance, hr, procurement и т.д. - Шаблоны конфигурации*
    - [7. duty_templates — Связь обязанностей с шаблонами документов](service-design.md#7--duty_templates---связь-обязанностей-с-шаблонами-документов) — *- Определяет, какие шаблоны документов соответствуют конкретным обязанностям - Автоматическая генера...*
    - [8. duty_approval_flows — Маршруты согласования по функциям](service-design.md#8--duty_approval_flows---маршруты-согласования-по-функциям) — *- Описывает этапы согласования для выполнения определённой функции - Автоматическое назначение участ...*
    - [9. specialty_roles — Рекомендованные роли по должностям](service-design.md#9--specialty_roles---рекомендованные-роли-по-должностям) — *- Помогает автоматизировать создание ролей доступа на основе должности - RBAC (Role-Based Access Con...*
  - [🔄 Логика работы системы](service-design.md#--логика-работы-системы) — *1. Компания выбирает подразделения из архетипов 2. Назначает должности из глобального справочника s*
    - [Этап 1: Создание организационной структуры](service-design.md#этап-1--создание-организационной-структуры) — *1. Компания выбирает подразделения из архетипов 2. Назначает должности из глобального справочника sp...*
    - [Этап 2: Автоматические рекомендации](service-design.md#этап-2--автоматические-рекомендации) — *1. На основе выбранных обязанностей система рассчитывает рекомендации модулей 2. Учитываются веса ва...*
    - [Этап 3: Настройка и кастомизация](service-design.md#этап-3--настройка-и-кастомизация) — *1. Компания может принять или отклонить рекомендации 2. Настройка параметров модулей под специфику б...*
  - [🎯 Преимущества архитектуры](service-design.md#--преимущества-архитектуры) — *- Модульная структура позволяет подключать только необходимые компоненты - Легкая адаптация под раз*
    - [Гибкость](service-design.md#гибкость) — *- Модульная структура позволяет подключать только необходимые компоненты - Легкая адаптация под разл...*
    - [Масштабируемость](service-design.md#масштабируемость) — *- Микросервисная архитектура - Горизонтальное масштабирование компонентов - Независимое развитие мод...*
    - [Интеллектуальность](service-design.md#интеллектуальность) — *- AI-рекомендации через MCP интеграцию - Автоматическая модерация контента - Машинное обучение на ос...*
    - [Стандартизация](service-design.md#стандартизация) — *- Использование международных классификаций - Единые подходы к описанию процессов - Совместимость с*
  - [🔧 Техническая реализация](service-design.md#--техническая-реализация) — *- RESTful API для всех операций - GraphQL для сложных запросов*
    - [API Design](service-design.md#api-design) — *- RESTful API для всех операций - GraphQL для сложных запросов - WebSocket для real-time обновлений*
    - [Модель данных](service-design.md#модель-данных) — *- PostgreSQL для основных данных - JSONB для гибких структур - Индексы для оптимизации запросов - Ми...*
    - [Безопасность](service-design.md#безопасность) — *- Мультитенантность с изоляцией по company_id - JWT аутентификация - RBAC авторизация - Аудит всех о...*
    - [Интеграции](service-design.md#интеграции) — *- MCP для AI-сервисов - Webhooks для внешних систем - REST API для интеграций - Экспорт/импорт данны...*
  - [📊 Метрики и аналитика](service-design.md#--метрики-и-аналитика) — *- Время создания структуры - Процент принятых рекомендаций*
    - [Пользовательские метрики](service-design.md#пользовательские-метрики) — *- Время создания структуры - Процент принятых рекомендаций - Частота использования модулей - Удовлет...*
    - [Технические метрики](service-design.md#технические-метрики) — *- Время отклика API - Точность рекомендаций - Производительность системы - Доступность сервисов*
    - [Бизнес метрики](service-design.md#бизнес-метрики) — *- Количество активных компаний - Средний размер организационной структуры - Популярность модулей - R...*

### ✏️ 👤 [Настройка окружения разработки](setup.md)
**File ID:** `setup-37461a54`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Настройка окружения разработки](setup.md#настройка-окружения-разработки)
  - [Системные требования](setup.md#системные-требования) — *- **Python**: 3.11+ - **Node.js**: 18+*
    - [Минимальные требования](setup.md#минимальные-требования) — *- **Python**: 3.11+ - **Node.js**: 18+ - **PostgreSQL**: 14+ - **Redis**: 6+*
    - [Рекомендуемые требования](setup.md#рекомендуемые-требования) — *- **Python**: 3.12 - **Node.js**: 20 LTS - **PostgreSQL**: 15 - **Redis**: 7*
  - [Установка зависимостей](setup.md#установка-зависимостей) — *```bash*
    - [1. Клонирование репозитория](setup.md#1--клонирование-репозитория) — *```bash git clone https://github.com/CoreTwin/CoreTwin.git cd CoreTwin*
    - [2. Настройка Python окружения](setup.md#2--настройка-python-окружения) — *```bash python -m venv venv*
- [Создание виртуального окружения](setup.md#создание-виртуального-окружения) — *python -m venv venv  source venv/bin/activate*
- [Активация (Linux/macOS)](setup.md#активация--linux-macos-) — *source venv/bin/activate  venv\Scripts\activate*
- [Активация (Windows)](setup.md#активация--windows-) — *venv\Scripts\activate  cd backend*
- [Установка зависимостей backend](setup.md#установка-зависимостей-backend) — *cd backend pip install -r requirements.txt pip install -r requirements-test.txt ```*
    - [3. Настройка Node.js окружения](setup.md#3--настройка-node-js-окружения) — *```bash cd ../frontend*
- [Переход в директорию frontend](setup.md#переход-в-директорию-frontend) — *cd ../frontend  npm install*
- [Установка зависимостей](setup.md#установка-зависимостей) — *npm install ```*
    - [4. Настройка базы данных](setup.md#4--настройка-базы-данных) — *```bash*
      - [PostgreSQL](setup.md#postgresql) — *```bash sudo apt update*
- [Установка PostgreSQL (Ubuntu/Debian)](setup.md#установка-postgresql--ubuntu-debian-) — *sudo apt update sudo apt install postgresql postgresql-contrib*
- [Создание пользователя и базы данных](setup.md#создание-пользователя-и-базы-данных) — *sudo -u postgres psql ```  В psql консоли выполните следующие команды, заменив значения на ваши:*
      - [Redis](setup.md#redis) — *```bash sudo apt install redis-server*
- [Установка Redis (Ubuntu/Debian)](setup.md#установка-redis--ubuntu-debian-) — *sudo apt install redis-server  sudo systemctl start redis-server*
- [Запуск Redis](setup.md#запуск-redis) — *sudo systemctl start redis-server sudo systemctl enable redis-server ```*
    - [5. Настройка переменных окружения](setup.md#5--настройка-переменных-окружения) — *```bash cp .env.example .env*
- [Копирование примера конфигурации](setup.md#копирование-примера-конфигурации) — *cp .env.example .env ```  Отредактируйте `.env` файл, указав ваши настройки:*
- [Database - укажите ваши данные подключения](setup.md#database---укажите-ваши-данные-подключения) — *DATABASE_URL=postgresql://пользователь:пароль@localhost:5432/coretwin_db TEST_DATABASE_URL=postgresq...*
- [Redis](setup.md#redis) — *REDIS_URL=redis://localhost:6379/0  JWT_SECRET_KEY=ваш_секретный_ключ_для_jwt*
- [JWT - сгенерируйте безопасный ключ](setup.md#jwt---сгенерируйте-безопасный-ключ) — *JWT_SECRET_KEY=ваш_секретный_ключ_для_jwt JWT_ALGORITHM=HS256 JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT...*
- [Logging](setup.md#logging) — *LOG_LEVEL=INFO LOG_FORMAT=json LOG_FILE_ENABLED=true LOG_FILE_PATH=./logs*
- [Development](setup.md#development) — *DEBUG=true ENVIRONMENT=development ```*
  - [Запуск приложения](setup.md#запуск-приложения) — *```bash*
    - [Вариант 1: Docker Compose (Рекомендуется)](setup.md#вариант-1--docker-compose--рекомендуется-) — *```bash docker-compose up -d*
- [Запуск всех сервисов](setup.md#запуск-всех-сервисов) — *docker-compose up -d  docker-compose logs -f*
- [Просмотр логов](setup.md#просмотр-логов) — *docker-compose logs -f  docker-compose down*
- [Остановка сервисов](setup.md#остановка-сервисов) — *docker-compose down ```*
    - [Вариант 2: Локальный запуск](setup.md#вариант-2--локальный-запуск) — *```bash*
      - [Backend](setup.md#backend) — *```bash cd backend*
- [Применение миграций](setup.md#применение-миграций) — *alembic upgrade head  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000*
- [Запуск сервера разработки](setup.md#запуск-сервера-разработки) — *uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 ```*
      - [Frontend](setup.md#frontend) — *```bash cd frontend*
- [Запуск сервера разработки](setup.md#запуск-сервера-разработки) — *npm run dev ```*
  - [Проверка установки](setup.md#проверка-установки) — *Откройте в браузере:*
    - [1. Backend API](setup.md#1--backend-api) — *Откройте в браузере: - **Swagger UI**: http://localhost:8000/docs - **ReDoc**: http://localhost:800*
    - [2. Frontend](setup.md#2--frontend) — *Откройте в браузере: - **Frontend**: http://localhost:3000*
    - [3. Тестирование](setup.md#3--тестирование) — *```bash cd backend*
- [Backend тесты](setup.md#backend-тесты) — *cd backend pytest --cov=app --cov=services --cov-report=html*
- [Frontend тесты](setup.md#frontend-тесты) — *cd frontend npm test ```*
  - [Полезные команды](setup.md#полезные-команды) — *```bash*
    - [Backend](setup.md#backend) — *```bash alembic revision --autogenerate -m "Описание изменений"*
- [Создание новой миграции](setup.md#создание-новой-миграции) — *alembic revision --autogenerate -m "Описание изменений"  alembic upgrade head*
- [Применение миграций](setup.md#применение-миграций) — *alembic upgrade head  alembic downgrade -1*
- [Откат миграций](setup.md#откат-миграций) — *alembic downgrade -1  pytest --cov=app --cov=services --cov-report=html --cov-report=term*
- [Запуск тестов с покрытием](setup.md#запуск-тестов-с-покрытием) — *pytest --cov=app --cov=services --cov-report=html --cov-report=term  black app/ services/*
- [Линтинг кода](setup.md#линтинг-кода) — *black app/ services/ isort app/ services/ flake8 app/ services/ ```*
    - [Frontend](setup.md#frontend) — *```bash npm run dev*
- [Запуск в режиме разработки](setup.md#запуск-в-режиме-разработки) — *npm run dev  npm run build*
- [Сборка для продакшена](setup.md#сборка-для-продакшена) — *npm run build  npm run preview*
- [Предварительный просмотр сборки](setup.md#предварительный-просмотр-сборки) — *npm run preview  npm run lint*
- [Линтинг](setup.md#линтинг) — *npm run lint npm run lint:fix*
- [Тестирование](setup.md#тестирование) — *npm test npm run test:coverage ```*
    - [Docker](setup.md#docker) — *```bash docker-compose build*
- [Пересборка контейнеров](setup.md#пересборка-контейнеров) — *docker-compose build  docker-compose up backend*
- [Запуск отдельного сервиса](setup.md#запуск-отдельного-сервиса) — *docker-compose up backend  docker-compose exec backend bash*
- [Выполнение команд в контейнере](setup.md#выполнение-команд-в-контейнере) — *docker-compose exec backend bash docker-compose exec frontend sh*
- [Просмотр логов](setup.md#просмотр-логов) — *docker-compose logs backend docker-compose logs frontend ```*
  - [Решение проблем](setup.md#решение-проблем) — *```bash*
    - [Проблемы с PostgreSQL](setup.md#проблемы-с-postgresql) — *```bash sudo systemctl status postgresql*
- [Проверка статуса PostgreSQL](setup.md#проверка-статуса-postgresql) — *sudo systemctl status postgresql  sudo systemctl restart postgresql*
- [Перезапуск PostgreSQL](setup.md#перезапуск-postgresql) — *sudo systemctl restart postgresql  psql -h localhost -U имя_пользователя -d coretwin_db*
- [Проверка подключения](setup.md#проверка-подключения) — *psql -h localhost -U имя_пользователя -d coretwin_db ```*
    - [Проблемы с правами доступа](setup.md#проблемы-с-правами-доступа) — *```bash sudo chown -R $USER:$USER .*
- [Исправление прав на директории](setup.md#исправление-прав-на-директории) — *sudo chown -R $USER:$USER . chmod -R 755 .*
- [Исправление прав на логи](setup.md#исправление-прав-на-логи) — *mkdir -p backend/logs chmod 755 backend/logs ```*
    - [Проблемы с зависимостями](setup.md#проблемы-с-зависимостями) — *```bash pip cache purge*
- [Очистка кеша pip](setup.md#очистка-кеша-pip) — *pip cache purge  pip install --force-reinstall -r requirements.txt*
- [Переустановка зависимостей](setup.md#переустановка-зависимостей) — *pip install --force-reinstall -r requirements.txt  npm cache clean --force*
- [Очистка кеша npm](setup.md#очистка-кеша-npm) — *npm cache clean --force  rm -rf node_modules package-lock.json*
- [Переустановка зависимостей](setup.md#переустановка-зависимостей) — *rm -rf node_modules package-lock.json npm install ```*
  - [IDE настройка](setup.md#ide-настройка) — *Рекомендуемые расширения:*
    - [VS Code](setup.md#vs-code) — *Рекомендуемые расширения: - Python - Pylance*
    - [PyCharm](setup.md#pycharm) — *Настройки: - Интерпретатор Python: `venv/bin/python` - Корневая директория: `backend/`*
  - [Дополнительные инструменты](setup.md#дополнительные-инструменты) — *```bash*
    - [Мониторинг](setup.md#мониторинг) — *```bash sudo apt install htop*
- [Установка htop для мониторинга системы](setup.md#установка-htop-для-мониторинга-системы) — *sudo apt install htop  docker stats*
- [Мониторинг Docker контейнеров](setup.md#мониторинг-docker-контейнеров) — *docker stats ```*
    - [Отладка](setup.md#отладка) — *```bash psql -h localhost -U имя_пользователя -d coretwin_db*
- [Подключение к базе данных](setup.md#подключение-к-базе-данных) — *psql -h localhost -U имя_пользователя -d coretwin_db  redis-cli monitor*
- [Мониторинг Redis](setup.md#мониторинг-redis) — *redis-cli monitor  tail -f backend/logs/app.log*
- [Просмотр логов приложения](setup.md#просмотр-логов-приложения) — *tail -f backend/logs/app.log ```  ---*

### ✏️ 🤖 [Применение Model Context Protocol (MCP) в платформе CoreTwin](mcp-integration.md)
**File ID:** `mcp-integration-0a56fc9c`  
**Автор:** ai | **Редактируемый:** Да

**Структура заголовков:**
- [Применение Model Context Protocol (MCP) в платформе CoreTwin](mcp-integration.md#применение-model-context-protocol--mcp--в-платформе-coretwin) — *CoreTwin спроектирован как API-first платформа на микросервисной архитектуре для создания цифровых*
  - [Введение](mcp-integration.md#введение) — *CoreTwin спроектирован как API-first платформа на микросервисной архитектуре для создания цифровых*
  - [📌 Сценарий 1: ИИ-модерация пользовательского контента](mcp-integration.md#--сценарий-1--ии-модерация-пользовательского-контента) — *Когда администраторы компаний вносят пользовательские элементы (например, новые должности, обязанн*
    - [🎯 Цель и польза](mcp-integration.md#--цель-и-польза) — *Когда администраторы компаний вносят пользовательские элементы (например, новые должности, обязанно*
    - [🧾 Пример MCP-контекста (JSON)](mcp-integration.md#--пример-mcp-контекста--json-) — *```json { "role": "ContentModeratorAI",*
    - [🔄 Процесс модерации](mcp-integration.md#--процесс-модерации) — *1. **Получение контекста**: ИИ получает информацию о новой обязанности, связанной специальности и с*
  - [📌 Сценарий 2: Интеллектуальные рекомендации модулей](mcp-integration.md#--сценарий-2--интеллектуальные-рекомендации-модулей) — *На основе созданной организационной структуры и выбранных должностей, ИИ анализирует потребности к*
    - [🎯 Цель и польза](mcp-integration.md#--цель-и-польза) — *На основе созданной организационной структуры и выбранных должностей, ИИ анализирует потребности ко*
    - [🧾 Пример MCP-контекста для рекомендаций](mcp-integration.md#--пример-mcp-контекста-для-рекомендаций) — *```json { "role": "ModuleRecommendationAI",*
    - [🔄 Процесс генерации рекомендаций](mcp-integration.md#--процесс-генерации-рекомендаций) — *1. **Анализ структуры**: ИИ изучает организационную структуру компании 2. **Сопоставление потребнос*
  - [📌 Сценарий 3: AI-помощник в интерфейсе](mcp-integration.md#--сценарий-3--ai-помощник-в-интерфейсе) — *Интеграция AI-помощника непосредственно в пользовательский интерфейс для:*
    - [🎯 Цель и польза](mcp-integration.md#--цель-и-польза) — *Интеграция AI-помощника непосредственно в пользовательский интерфейс для:  - Помощи в создании орга*
    - [🧾 Пример MCP-контекста для помощника](mcp-integration.md#--пример-mcp-контекста-для-помощника) — *```json { "role": "UserAssistantAI",*
  - [🔧 Техническая реализация MCP](mcp-integration.md#--техническая-реализация-mcp) — *```*
    - [Архитектура интеграции](mcp-integration.md#архитектура-интеграции) — *``` ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐ │   CoreTwin      │    │   MC*
    - [Компоненты системы](mcp-integration.md#компоненты-системы) — *1. **MCP Client** - клиент для взаимодействия с AI сервисами 2. **Context Builder** - формирование*
    - [API эндпоинты](mcp-integration.md#api-эндпоинты) — *``` POST /api/v1/ai/moderate          # Модерация контента POST /api/v1/ai/recommend         # Гене*
  - [🛡️ Безопасность и надежность](mcp-integration.md#---безопасность-и-надежность) — *- **Изоляция данных**: Строгое разделение данных компаний*
    - [Принципы безопасности](mcp-integration.md#принципы-безопасности) — *- **Изоляция данных**: Строгое разделение данных компаний - **Минимальные привилегии**: AI получает*
    - [Обработка ошибок](mcp-integration.md#обработка-ошибок) — *- **Graceful Degradation**: Система работает без AI при недоступности - **Circuit Breaker**: Защита*
  - [📊 Метрики и мониторинг](mcp-integration.md#--метрики-и-мониторинг) — *- **Точность модерации**: > 95% корректных решений*
    - [Ключевые метрики](mcp-integration.md#ключевые-метрики) — *- **Точность модерации**: > 95% корректных решений - **Релевантность рекомендаций**: > 85% принятых*
    - [Мониторинг качества](mcp-integration.md#мониторинг-качества) — *- A/B тестирование рекомендаций - Пользовательская обратная связь - Анализ принятых/отклоненных пре*

### ✏️ 👤 [Разработка CoreTwin Platform](README (5).md)
**File ID:** `readme--5--cad7b60f`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Разработка CoreTwin Platform](README (5).md#разработка-coretwin-platform) — *CoreTwin Platform разрабатывается по методологии Agile с использованием фазированного подхода. Про*
  - [Обзор процесса разработки](README (5).md#обзор-процесса-разработки) — *CoreTwin Platform разрабатывается по методологии Agile с использованием фазированного подхода. Прое*
  - [Фазы разработки](README (5).md#фазы-разработки) — ***Цель**: Создание минимально жизнеспособного продукта с базовой функциональностью*
    - [🚀 Фаза 1: MVP (2-3 месяца)](README (5).md#--фаза-1--mvp--2-3-месяца-) — ***Цель**: Создание минимально жизнеспособного продукта с базовой функциональностью  **Ключевые компо...*
    - [🏗️ Фаза 2: Основная функциональность (3-4 месяца)](README (5).md#---фаза-2--основная-функциональность--3-4-месяца-) — ***Цель**: Расширение функциональности до полноценной рабочей системы  **Ключевые компоненты**: - Dra...*
    - [🤖 Фаза 3: AI и аналитика (2-3 месяца)](README (5).md#--фаза-3--ai-и-аналитика--2-3-месяца-) — ***Цель**: Внедрение интеллектуальных возможностей и аналитики  **Ключевые компоненты**: - Полная инт...*
    - [📈 Фаза 4: Масштабирование и оптимизация (1-2 месяца)](README (5).md#--фаза-4--масштабирование-и-оптимизация--1-2-месяца-) — ***Цель**: Подготовка к промышленной эксплуатации  **Ключевые компоненты**: - Оптимизация производите...*
  - [Технологический стек](README (5).md#технологический-стек) — *- **FastAPI** - основной веб-фреймворк - **SQLAlchemy** - ORM для работы с базой данных*
    - [Backend](README (5).md#backend) — *- **FastAPI** - основной веб-фреймворк - **SQLAlchemy** - ORM для работы с базой данных - **GO** - *...*
    - [Frontend](README (5).md#frontend) — *- **React** + **TypeScript** + **React Flow** + **Rete.js** - основной стек - **Vite** - сборщик и d...*
    - [DevOps](README (5).md#devops) — *- **Docker** - контейнеризация - **Kubernetes** - оркестрация - **GitHub Actions** - CI/CD - **Prome...*
  - [Архитектурные принципы](README (5).md#архитектурные-принципы) — *- Разделение на независимые сервисы - API Gateway для маршрутизации*
    - [1. Микросервисная архитектура](README (5).md#1--микросервисная-архитектура) — *- Разделение на независимые сервисы - API Gateway для маршрутизации - Асинхронная коммуникация через...*
    - [2. API-First подход](README (5).md#2--api-first-подход) — *- Все функции доступны через REST API - OpenAPI документация - Версионирование API*
    - [3. Мультитенантность](README (5).md#3--мультитенантность) — *- Строгая изоляция данных по company_id - Масштабируемость для SaaS-модели - Гибкая система тарифов*
    - [4. Безопасность](README (5).md#4--безопасность) — *- JWT аутентификация - RBAC авторизация - Шифрование данных - Аудит операций*
  - [Процесс разработки](README (5).md#процесс-разработки) — *``` main ← develop ← feature/task-name*
    - [Git Workflow](README (5).md#git-workflow) — *``` main ← develop ← feature/task-name ```*
    - [Code Review](README (5).md#code-review) — *- Все изменения проходят через Pull Request - Минимум 2 ревьюера для критических изменений - Автомат...*
    - [Тестирование](README (5).md#тестирование) — *- **Unit тесты** - покрытие не менее 80% - **Integration тесты** - для API эндпоинтов - **E2E тесты*...*
  - [Стандарты качества](README (5).md#стандарты-качества) — *- Следование принципам SOLID - Использование type hints в Python*
    - [Backend](README (5).md#backend) — *- Следование принципам SOLID - Использование type hints в Python - Документирование API через docstr...*
    - [Frontend](README (5).md#frontend) — *- Строгий TypeScript (no any) - Компонентная архитектура - Переиспользуемые UI компоненты - Accessib...*
    - [База данных](README (5).md#база-данных) — *- Миграции для всех изменений схемы - Индексы для оптимизации запросов - Нормализация данных - Backu...*
  - [Мониторинг и метрики](README (5).md#мониторинг-и-метрики) — *- API Response Time < 200ms (95 перцентиль) - Database Query Time < 100ms (90 перцентиль)*
    - [Технические метрики](README (5).md#технические-метрики) — *- API Response Time < 200ms (95 перцентиль) - Database Query Time < 100ms (90 перцентиль) - Uptime >...*
    - [Бизнес метрики](README (5).md#бизнес-метрики) — *- Time to Create Structure < 30 минут - User Satisfaction > 4.0/5.0 - Feature Adoption > 60% - Month...*
  - [Документация](README (5).md#документация) — *- [Архитектура системы](../architecture/overview.md) - [API документация](../api/authentication.md)*
    - [Техническая документация](README (5).md#техническая-документация) — *- [Архитектура системы](../architecture/overview.md) - [API документация](../api/authentication.md)*
    - [Инструменты документации](README (5).md#инструменты-документации) — *Проект использует комплексный подход к автоматической генерации документации:  - **MkDocs** - основн...*
    - [Пользовательская документация](README (5).md#пользовательская-документация) — *- Руководство пользователя - Видео-туториалы - FAQ и база знаний - Changelog*
  - [Команда и роли](README (5).md#команда-и-роли) — *- **Product Owner** - определение требований - **Tech Lead** - техническое руководство*
    - [Роли в проекте](README (5).md#роли-в-проекте) — *- **Product Owner** - определение требований - **Tech Lead** - техническое руководство - **Backend D...*
    - [Коммуникация](README (5).md#коммуникация) — *- **Daily Standups** - ежедневные синхронизации - **Sprint Planning** - планирование спринтов - **Re...*

### ✏️ 👤 [Рекомендации по технологиям](technology-stack.md)
**File ID:** `technology-stack-9533b775`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Рекомендации по технологиям](technology-stack.md#рекомендации-по-технологиям)
  - [Бэкенд](technology-stack.md#бэкенд) — *- **FastAPI** + **Node.js** - для основных сервисов - **Java Spring Boot** - для enterprise решений*
    - [Микросервисы](technology-stack.md#микросервисы) — *- **FastAPI** + **Node.js** - для основных сервисов - **Java Spring Boot** - для enterprise решений*
    - [Основные технологии](technology-stack.md#основные-технологии) — *- **Python 3.11+** с FastAPI - **SQLAlchemy** для работы с базой данных - **Pydantic** для валидации...*
  - [Фронтенд](technology-stack.md#фронтенд) — *- **React** + **TypeScript** + **React Flow** + **Rete.js**- основной стек - **Vite** - сборщик и d*
    - [Обязательные технологии](technology-stack.md#обязательные-технологии) — *- **React** + **TypeScript** + **React Flow** + **Rete.js**- основной стек - **Vite** - сборщик и de...*
    - [Дополнительные библиотеки](technology-stack.md#дополнительные-библиотеки) — *- **D3.js** для диаграмм и визуализации - **React Flow + Rete.js** для drag & drop функциональности*
  - [База данных](technology-stack.md#база-данных) — *- **PostgreSQL** (основные данные) - Версия 15+*
    - [Основное хранилище](technology-stack.md#основное-хранилище) — *- **PostgreSQL** (основные данные) - Версия 15+ - Расширения: UUID, JSONB, Full-text search - Реплик...*
    - [Дополнительные хранилища](technology-stack.md#дополнительные-хранилища) — *- **Redis** (кеш и сессии) - Кэширование API ответов - Пользовательские сессии - Очереди фоновых зад...*
  - [Архитектура](technology-stack.md#архитектура) — *- **Микросервисная архитектура** - **API Gateway** для маршрутизации запросов*
    - [Основные принципы](technology-stack.md#основные-принципы) — *- **Микросервисная архитектура** - **API Gateway** для маршрутизации запросов - **Message Queue** (R...*
    - [Паттерны проектирования](technology-stack.md#паттерны-проектирования) — *- Repository pattern для работы с данными - Dependency Injection в FastAPI - SOLID принципы - Circui...*
  - [Развертывание](technology-stack.md#развертывание) — *- **Docker** для контейнеризации приложений - **Docker Compose** для локальной разработки*
    - [Контейнеризация](technology-stack.md#контейнеризация) — *- **Docker** для контейнеризации приложений - **Docker Compose** для локальной разработки - Multi-st...*
    - [Оркестрация](technology-stack.md#оркестрация) — *- **Kubernetes** для production развертывания - **Helm** для управления конфигурациями - **Ingress**...*
    - [Облачные платформы](technology-stack.md#облачные-платформы) — *- **AWS** / **Google Cloud** / **Azure** - **Managed databases** для production - **CDN** для статич...*
  - [CI/CD](technology-stack.md#ci-cd) — *- **GitHub Actions** / **GitLab CI** / **Jenkins** - Автоматические тесты на каждый PR*
    - [Пайплайн разработки](technology-stack.md#пайплайн-разработки) — *- **GitHub Actions** / **GitLab CI** / **Jenkins** - Автоматические тесты на каждый PR - Линтинг и ф...*
    - [Стратегия развертывания](technology-stack.md#стратегия-развертывания) — *- **Blue-Green deployment** для zero-downtime - **Canary releases** для постепенного развертывания -...*
  - [Мониторинг и логирование](technology-stack.md#мониторинг-и-логирование) — *- **Prometheus** + **Grafana** для метрик - **Jaeger** / **Zipkin** для трассировки*
    - [Application Performance Monitoring](technology-stack.md#application-performance-monitoring) — *- **Prometheus** + **Grafana** для метрик - **Jaeger** / **Zipkin** для трассировки - **ELK Stack***
    - [Error Tracking](technology-stack.md#error-tracking) — *- **Sentry** для отслеживания ошибок - **DataDog** / **New Relic** для комплексного мониторинга*
  - [Безопасность](technology-stack.md#безопасность) — *- **JWT** токены для API - **OAuth2** для внешних интеграций*
    - [Аутентификация и авторизация](technology-stack.md#аутентификация-и-авторизация) — *- **JWT** токены для API - **OAuth2** для внешних интеграций - **RBAC** (Role-Based Access Control)*
    - [Защита данных](technology-stack.md#защита-данных) — *- **HTTPS** везде (TLS 1.3) - **Шифрование данных** в покое и в движении - **Secrets management** (H...*
  - [💡 Дополнительные рекомендации](technology-stack.md#--дополнительные-рекомендации) — *- **Начать с MVP** на простом стеке, затем масштабировать - **Использование TypeScript** для больши*
    - [Стратегия развития](technology-stack.md#стратегия-развития) — *- **Начать с MVP** на простом стеке, затем масштабировать - **Использование TypeScript** для больших...*
    - [Качество кода](technology-stack.md#качество-кода) — *- **Покрытие тестами** не менее 80% - **Code review** для всех изменений - **Автоматическое форматир...*
    - [Производительность](technology-stack.md#производительность) — *- **Lazy loading** для фронтенда - **Code splitting** для оптимизации загрузки - **Database indexing...*

### ✏️ 👤 [Система логирования CoreTwin Platform](logging.md)
**File ID:** `logging-4d45c557`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Система логирования CoreTwin Platform](logging.md#система-логирования-coretwin-platform) — *CoreTwin Platform использует структурированную систему логирования с категоризацией ошибок по тега*
  - [Обзор](logging.md#обзор) — *CoreTwin Platform использует структурированную систему логирования с категоризацией ошибок по тегам*
  - [Конфигурация](logging.md#конфигурация) — *Настройки логирования в `app/config.py`:  ```python*
  - [Теги категоризации ошибок](logging.md#теги-категоризации-ошибок) — *- `AUTHENTICATION_ERROR` - Ошибки аутентификации и авторизации - `DATABASE_ERROR` - Ошибки базы дан*
  - [Структура файлов логов](logging.md#структура-файлов-логов) — *``` backend/logs/ ├── app.log          # Общие логи приложения*
  - [Формат JSON логов](logging.md#формат-json-логов) — *```json { "timestamp": "2023-12-26T12:00:00.000Z",*
  - [Использование в коде](logging.md#использование-в-коде) — *```python*
    - [Импорт сервиса логирования](logging.md#импорт-сервиса-логирования) — *```python from services.logging.service import logging_service, ErrorTags ```*
    - [Логирование с тегами](logging.md#логирование-с-тегами) — *```python logging_service.log_authentication_error(*
- [Ошибка аутентификации](logging.md#ошибка-аутентификации) — *logging_service.log_authentication_error( "Неверный пароль", user_id="user123", request_id="req456",...*
- [Ошибка базы данных](logging.md#ошибка-базы-данных) — *logging_service.log_database_error( "Ошибка подключения к БД", extra_data={"error": str(e)} )*
- [Ошибка валидации](logging.md#ошибка-валидации) — *logging_service.log_validation_error( "Неверный формат email", extra_data={"field": "email", "value"...*
- [Ошибка API](logging.md#ошибка-api) — *logging_service.log_api_error( "HTTP 500 Internal Server Error", request_id="req456", extra_data={"e...*
- [Информационное логирование](logging.md#информационное-логирование) — *logging_service.log_info( "Пользователь успешно создан", tag="USER_CREATED", user_id="user123",*
  - [Фильтрация чувствительных данных](logging.md#фильтрация-чувствительных-данных) — *Система автоматически фильтрует: - Пароли (`password`, `hashed_password`) - JWT токены (`access_tok*
  - [Интеграция с FastAPI](logging.md#интеграция-с-fastapi) — *Middleware автоматически логирует: - Входящие HTTP запросы с тегом `API_ERROR` - Ответы с кодами ош*
  - [Мониторинг и анализ](logging.md#мониторинг-и-анализ) — *Логи можно анализировать с помощью: - `grep` для поиска по тегам: `grep "AUTHENTICATION_ERROR" logs*
  - [Ротация логов](logging.md#ротация-логов) — *Файлы автоматически ротируются: - По размеру (10MB по умолчанию) - По времени (ежедневно в полночь)*
  - [Производительность](logging.md#производительность) — *- Асинхронное логирование не блокирует основные операции - Буферизация записей для оптимизации I/O*

### ✏️ 👤 [Тестирование CoreTwin Platform](README (4).md)
**File ID:** `readme--4--539bf89c`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Тестирование CoreTwin Platform](README (4).md#тестирование-coretwin-platform) — *Тестовая среда использует PostgreSQL базу данных для обеспечения максимальной совместимости с прод*
  - [Конфигурация PostgreSQL для тестов](README (4).md#конфигурация-postgresql-для-тестов) — *Тестовая среда использует PostgreSQL базу данных для обеспечения максимальной совместимости с прода*
    - [Требования](README (4).md#требования) — *- PostgreSQL 14+ установлен и запущен - Тестовая база данных `coretwin_test_db` создана - Python па*
    - [Настройка тестовой базы данных](README (4).md#настройка-тестовой-базы-данных) — *```bash sudo -u postgres createdb coretwin_test_db*
- [Создание тестовой базы данных](README (4).md#создание-тестовой-базы-данных) — *sudo -u postgres createdb coretwin_test_db  sudo -u postgres psql -c "SELECT datname FROM pg_databas...*
- [Проверка подключения](README (4).md#проверка-подключения) — *sudo -u postgres psql -c "SELECT datname FROM pg_database WHERE datname = 'coretwin_test_db';" ```*
    - [Запуск тестов](README (4).md#запуск-тестов) — *```bash pip install -r requirements-test.txt*
- [Установка зависимостей для тестирования](README (4).md#установка-зависимостей-для-тестирования) — *pip install -r requirements-test.txt  pytest --cov=app --cov=services --cov-report=html --cov-report...*
- [Запуск всех тестов с покрытием](README (4).md#запуск-всех-тестов-с-покрытием) — *pytest --cov=app --cov=services --cov-report=html --cov-report=term  pytest tests/unit/test_auth_ser...*
- [Запуск конкретных тестов](README (4).md#запуск-конкретных-тестов) — *pytest tests/unit/test_auth_service.py -v pytest tests/integration/test_auth_api.py -v ```*
    - [Покрытие кода](README (4).md#покрытие-кода) — *Минимальное требование покрытия: **80%**  Текущее покрытие системы аутентификации: **80%+***
    - [Изоляция тестов](README (4).md#изоляция-тестов) — *Каждый тест выполняется в изолированной среде: - Создание всех таблиц перед тестом - Полная очистка*
    - [Структура тестов](README (4).md#структура-тестов) — *``` tests/ ├── __init__.py*
    - [Фикстуры](README (4).md#фикстуры) — *- `db_session`: Сессия PostgreSQL базы данных для теста - `client`: FastAPI тестовый клиент - `asyn*

### ✏️ 👤 [Тестирование CoreTwin Platform](testing.md)
**File ID:** `testing-e6ecbf14`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Тестирование CoreTwin Platform](testing.md#тестирование-coretwin-platform) — *Система тестирования CoreTwin Platform обеспечивает высокое качество кода и надежность приложения*
  - [Обзор](testing.md#обзор) — *Система тестирования CoreTwin Platform обеспечивает высокое качество кода и надежность приложения ч*
  - [Текущее покрытие](testing.md#текущее-покрытие) — *- **Общее покрытие**: 80%+ - **Backend**: Unit и Integration тесты - **Frontend**: Component и E2E*
  - [Структура тестов](testing.md#структура-тестов) — *``` backend/tests/*
    - [Backend тесты](testing.md#backend-тесты) — *``` backend/tests/ ├── unit/                  # Unit тесты │   ├── test_auth_service.py*
    - [Типы тестов](testing.md#типы-тестов) — *- Тестирование отдельных функций и методов - Изоляция зависимостей через моки*
      - [Unit тесты](testing.md#unit-тесты) — *- Тестирование отдельных функций и методов - Изоляция зависимостей через моки - Быстрое выполнение*
      - [Integration тесты](testing.md#integration-тесты) — *- Тестирование взаимодействия компонентов - Использование тестовой базы данных - Проверка API endpoi...*
  - [Конфигурация](testing.md#конфигурация) — *```ini [tool:pytest]*
    - [pytest.ini](testing.md#pytest-ini) — *```ini [tool:pytest] testpaths = tests python_files = test_*.py*
    - [Тестовая база данных](testing.md#тестовая-база-данных) — *- PostgreSQL для integration тестов - Автоматическое создание/удаление тестовых данных - Изоляция ме...*
  - [Запуск тестов](testing.md#запуск-тестов) — *```bash cd backend*
    - [Все тесты](testing.md#все-тесты) — *```bash cd backend pytest ```*
    - [С покрытием](testing.md#с-покрытием) — *```bash pytest --cov=app --cov=services --cov-report=html ```*
    - [Конкретный файл](testing.md#конкретный-файл) — *```bash pytest tests/unit/test_auth_service.py -v ```*
    - [По маркерам](testing.md#по-маркерам) — *```bash pytest -m "not slow" ```*
  - [Фикстуры](testing.md#фикстуры) — *- `db_session` - сессия базы данных - `test_client` - HTTP клиент для API*
    - [Базовые фикстуры](testing.md#базовые-фикстуры) — *- `db_session` - сессия базы данных - `test_client` - HTTP клиент для API - `test_user` - тестовый п...*
    - [Пример использования](testing.md#пример-использования) — *```python def test_create_user(db_session): user_data = UserCreate( email="test@example.com",*
  - [Моки и заглушки](testing.md#моки-и-заглушки) — *```python @patch('services.auth.service.verify_password')*
    - [Внешние зависимости](testing.md#внешние-зависимости) — *```python @patch('services.auth.service.verify_password') def test_authenticate_user(mock_verify, db...*
    - [База данных](testing.md#база-данных) — *```python @pytest.fixture def mock_db_session(): session = MagicMock()*
  - [Тестирование API](testing.md#тестирование-api) — *```python def test_login_success(test_client):*
    - [Аутентификация](testing.md#аутентификация) — *```python def test_login_success(test_client): response = test_client.post("/api/v1/auth/login", jso...*
    - [Защищенные endpoints](testing.md#защищенные-endpoints) — *```python def test_get_current_user(test_client, auth_headers): response = test_client.get("/api/v1/...*
  - [Тестирование ошибок](testing.md#тестирование-ошибок) — *```python def test_create_user_invalid_email(test_client):*
    - [Валидация данных](testing.md#валидация-данных) — *```python def test_create_user_invalid_email(test_client): response = test_client.post("/api/v1/auth...*
    - [Обработка исключений](testing.md#обработка-исключений) — *```python def test_database_error_handling(db_session): with patch.object(db_session, 'commit', side...*
  - [Производительность](testing.md#производительность) — *```bash pytest --durations=10*
    - [Профилирование тестов](testing.md#профилирование-тестов) — *```bash pytest --durations=10 ```*
    - [Параллельное выполнение](testing.md#параллельное-выполнение) — *```bash pytest -n auto ```*
  - [CI/CD интеграция](testing.md#ci-cd-интеграция) — *```yaml - name: Run tests*
    - [GitHub Actions](testing.md#github-actions) — *```yaml - name: Run tests run: | cd backend*
  - [Лучшие практики](testing.md#лучшие-практики) — *- Используйте описательные имена - Следуйте паттерну `test_<action>_<expected_result>`*
    - [Именование тестов](testing.md#именование-тестов) — *- Используйте описательные имена - Следуйте паттерну `test_<action>_<expected_result>` - Группируйте...*
    - [Структура тестов](testing.md#структура-тестов) — *- Arrange - подготовка данных - Act - выполнение действия - Assert - проверка результата*
    - [Изоляция тестов](testing.md#изоляция-тестов) — *- Каждый тест должен быть независимым - Используйте фикстуры для подготовки данных - Очищайте состоя...*
  - [Отчеты](testing.md#отчеты) — *```bash pytest --cov-report=html*
    - [HTML отчет покрытия](testing.md#html-отчет-покрытия) — *```bash pytest --cov-report=html open htmlcov/index.html ```*
    - [XML отчет для CI](testing.md#xml-отчет-для-ci) — *```bash pytest --cov-report=xml ```*
  - [Будущие улучшения](testing.md#будущие-улучшения) — *- Jest для unit тестов - React Testing Library для компонентов*
    - [Frontend тестирование](testing.md#frontend-тестирование) — *- Jest для unit тестов - React Testing Library для компонентов - Cypress для E2E тестов*
    - [Нагрузочное тестирование](testing.md#нагрузочное-тестирование) — *- Locust для API нагрузки - Профилирование производительности - Мониторинг метрик*
    - [Безопасность](testing.md#безопасность) — *- SAST сканирование - Dependency scanning - Penetration testing*

### ✏️ 👤 [Техническое задание платформы CoreTwin](technical-specification.md)
**File ID:** `technical-specification-8b358d28`  
**Автор:** human | **Редактируемый:** Да

**Структура заголовков:**
- [Техническое задание платформы CoreTwin](technical-specification.md#техническое-задание-платформы-coretwin) — ***Миссия CoreTwin**: предоставить инструмент для создания цифрового двойника компании любой отрасл*
  - [1. Миссия и ценности платформы](technical-specification.md#1--миссия-и-ценности-платформы) — ***Миссия CoreTwin**: предоставить инструмент для создания цифрового двойника компании любой отрасли*
    - [Ключевые ценности CoreTwin:](technical-specification.md#ключевые-ценности-coretwin-) — *- **Универсальность**: платформа подходит для компаний любого масштаба и сферы деятельности - **Гиб*
  - [2. Обзор платформы](technical-specification.md#2--обзор-платформы) — *CoreTwin Platform – универсальная платформа для построения «цифрового двойника» организации. Она по*
  - [3. Функциональные модули платформы](technical-specification.md#3--функциональные-модули-платформы) — ***Specialties (Специальности)**: глобальный справочник типовых должностей (ролей) – например, бухг*
    - [3.1. Specialties & Duties (Справочник должностей и обязанностей)](technical-specification.md#3-1--specialties---duties--справочник-должностей-и-обязанностей-) — ***Specialties (Специальности)**: глобальный справочник типовых должностей (ролей) – например, бухга*
    - [3.2. Company Structure (Модель организационной структуры)](technical-specification.md#3-2--company-structure--модель-организационной-структуры-) — *Оргструктура компании – иерархическое представление подразделений и позиций. Пользователь может соз*
    - [3.3. Module Recommendation Engine](technical-specification.md#3-3--module-recommendation-engine) — *Система автоматических рекомендаций модулей на основе выбранных должностей и обязанностей: - Алгори*
    - [3.4. Template & Document Management](technical-specification.md#3-4--template---document-management) — *Управление шаблонами документов и документооборотом: - Библиотека шаблонов документов - Связь шабло*
    - [3.5. Approval Workflows](technical-specification.md#3-5--approval-workflows) — *Система маршрутов согласования: - Конструктор маршрутов согласования - Автоматическое назначение уч*
    - [3.6. MCP Integration & AI Services](technical-specification.md#3-6--mcp-integration---ai-services) — *Интеграция с искусственным интеллектом через Model Context Protocol: - Модерация пользовательского*
  - [4. Технические требования](technical-specification.md#4--технические-требования) — *- Микросервисная архитектура - API-first подход*
    - [4.1. Архитектура](technical-specification.md#4-1--архитектура) — *- Микросервисная архитектура - API-first подход - Мультитенантность для SaaS-модели - Модульная сист...*
    - [4.2. Технологический стек](technical-specification.md#4-2--технологический-стек) — *- **Backend**: FastAPI + SQLAlchemy + Python + Go + Rust - **Frontend**: React + TypeScript + React*
    - [4.3. Стандарты и классификации](technical-specification.md#4-3--стандарты-и-классификации) — *- **ISCO-08**: Международная стандартная классификация занятий - **ISIC Rev.4**: Международная станд...*
  - [5. Безопасность и соответствие](technical-specification.md#5--безопасность-и-соответствие) — *- Строгая мультитенантность с изоляцией данных по company_id - Система ролей и разрешений (RBAC) -*
  - [6. Интеграции](technical-specification.md#6--интеграции) — *- Model Context Protocol (MCP) для AI-сервисов - REST API для внешних систем - Webhooks для уведомл*

