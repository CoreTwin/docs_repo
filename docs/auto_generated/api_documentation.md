[Домой](../../README.md) | [Назад](../../content/Description_for_agents.md)

<!-- AUTO-GENERATED -->

*Автоматически сгенерировано скриптом example_doc_generator.py*  
*Дата генерации: 2025-07-02 00:21:45*


Данная документация автоматически создана на основе анализа кода.


Получение списка пользователей.

**Параметры:**
- `limit` (int): Максимальное количество записей
- `offset` (int): Смещение для пагинации

**Ответ:**
```json
{
  "users": [],
  "total": 0
}
```

Создание нового пользователя.

**Тело запроса:**
```json
{
  "name": "string",
  "email": "string"
}
```


```json
{
  "id": "integer",
  "name": "string", 
  "email": "string",
  "created_at": "datetime"
}
```

---
*Этот файл создан автоматически. Не редактируйте вручную.*
