# update-docs

Автоматический инструмент для:

- сканирования Markdown-документации;
- построения и обновления оглавления (`toc.json`);
- вставки и синхронизации `<!-- include:file#id -->` блоков;
- валидации ссылок и заголовков.

## 📦 Установка

```bash
pip install -e .
```

## 🚀 Использование

Команда для запуска CLI из корня проекта:
```bash
update-docs --docs docs --toc toc.json
```
или через Python (если вдруг не работает entry point):
```bash
python -m update_docs.cli --docs docs --toc toc.json
```

- `--docs`: путь к папке с документацией (по умолчанию: `docs`)
- `--toc`: путь к JSON-файлу оглавления (по умолчанию: `toc.json`)

## 🔁 Интеграция с Git pre-commit hook

Создайте файл `.git/hooks/pre-commit` со следующим содержимым:

```bash
#!/bin/bash
echo "🛠 Запуск update-docs перед коммитом..."
update-docs --docs docs --toc toc.json
```

Сделайте его исполняемым:

```bash
chmod +x .git/hooks/pre-commit
```

Теперь перед каждым коммитом будет автоматически обновляться документация.
