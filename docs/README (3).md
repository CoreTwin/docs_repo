# CoreTwin Platform Frontend

## Архитектура Frontend

Frontend платформы CoreTwin построен на **React** с **TypeScript** и использует современные инструменты разработки для создания интуитивного пользовательского интерфейса.

## 📁 Структура проекта

```
frontend/
├── src/
│   ├── components/        # Переиспользуемые компоненты
│   │   ├── common/       # Общие компоненты
│   │   ├── forms/        # Формы
│   │   ├── layout/       # Компоненты макета
│   │   └── ui/           # UI компоненты
│   ├── pages/            # Страницы приложения
│   │   ├── auth/         # Аутентификация
│   │   ├── dashboard/    # Главная панель
│   │   ├── companies/    # Управление компаниями
│   │   ├── specialties/  # Справочник должностей
│   │   └── settings/     # Настройки
│   ├── hooks/            # Пользовательские хуки
│   ├── utils/            # Утилиты
│   ├── types/            # TypeScript типы
│   ├── services/         # API сервисы
│   ├── store/            # Состояние приложения
│   └── assets/           # Статические ресурсы
├── public/               # Публичные файлы
└── tests/                # Тесты
```

## 🚀 Технологический стек

- **React 18** - библиотека для создания пользовательских интерфейсов
- **TypeScript** - типизированный JavaScript
- **Vite** - быстрый сборщик и dev-сервер
- **Ant Design** - UI библиотека компонентов
- **React Query** - управление серверным состоянием
- **Zustand** - управление клиентским состоянием
- **React Router** - маршрутизация
- **React Flow + Rete.js** - drag & drop функциональность
- **D3.js** - визуализация данных

## 🔧 Настройка разработки

### Требования
- Node.js 18+
- npm 9+

### Установка зависимостей
```bash
cd frontend
npm install
```

### Запуск для разработки
```bash
npm run dev
```

### Сборка для продакшена
```bash
npm run build
```

## 🎨 Компоненты

### 1. Layout Components
- **AppLayout** - основной макет приложения
- **Sidebar** - боковая навигация
- **Header** - шапка с пользовательским меню
- **Breadcrumbs** - навигационные крошки

### 2. Business Components
- **OrganizationBuilder** - drag & drop конструктор структур
- **SpecialtySelector** - выбор должностей
- **DocumentTemplates** - управление шаблонами
- **WorkflowDesigner** - конструктор маршрутов

### 3. Common Components
- **DataTable** - таблицы с данными
- **SearchInput** - поиск с автодополнением
- **FileUpload** - загрузка файлов
- **ConfirmDialog** - диалоги подтверждения

## 🔄 Управление состоянием

### Zustand Store
```typescript
interface AppState {
  user: User | null;
  currentCompany: Company | null;
  theme: 'light' | 'dark';
  setUser: (user: User) => void;
  setCompany: (company: Company) => void;
  toggleTheme: () => void;
}
```

### React Query
- Кэширование API запросов
- Автоматическое обновление данных
- Оптимистичные обновления
- Обработка ошибок

## 🧪 Тестирование

Тесты расположены в каталоге `tests` и используют **Vitest** совместно с **Testing Library**.

```bash
# Запуск всех тестов
npm test

# Интерактивный режим
npm run test:ui

# Отчёт по покрытию
npm run test:coverage
```

### Типы тестов
- **Unit тесты** - компоненты и утилиты
- **Integration тесты** - взаимодействие компонентов
- **E2E тесты** - пользовательские сценарии

## 📱 Адаптивность

- Поддержка мобильных устройств
- Responsive дизайн
- Touch-friendly интерфейс
- PWA возможности

## 🎯 Ключевые функции

### 1. Drag & Drop Builder
- Создание организационных структур
- Перетаскивание должностей
- Визуальное редактирование

### 2. Smart Recommendations
- AI-powered предложения
- Контекстные подсказки
- Автоматическое заполнение

### 3. Document Management
- Шаблоны документов
- Предварительный просмотр
- Экспорт в различные форматы

### 4. Workflow Designer
- Визуальный редактор процессов
- Настройка маршрутов согласования
- Мониторинг статусов

## 🔒 Безопасность

- JWT токены в httpOnly cookies
- CSRF protection
- XSS защита
- Валидация на клиенте

## 📊 Аналитика

- Отслеживание пользовательских действий
- Метрики производительности
- A/B тестирование
- Heatmaps и user sessions
