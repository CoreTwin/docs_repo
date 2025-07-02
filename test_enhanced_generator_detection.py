#!/usr/bin/env python3

import os
import sys
import json
import shutil
sys.path.insert(0, '.')

from update_docs.core import (
    detect_author_type_enhanced,
    check_generator_registry,
    scan_for_generator_functions,
    update_content_system
)

def test_enhanced_generator_detection():
    """Тестирует улучшенную систему определения автогенераторов"""
    print("=== Тестирование улучшенной системы определения автогенераторов ===")
    
    print("\n1. Создание тестовых автогенерированных файлов...")
    os.system("python example_doc_generator.py")
    
    print("\n2. Тестирование определения авторства по маркерам...")
    test_files = [
        "docs/auto_generated/api_documentation.md",
        "docs/auto_generated/CHANGELOG_AUTO.md",
        "docs/auto_generated/metrics_report.md"
    ]
    
    for file_path in test_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            author_type, source = detect_author_type_enhanced(file_path, content)
            print(f"  {file_path}:")
            print(f"    Автор: {author_type}")
            print(f"    Источник: {source}")
            print(f"    Ожидается: generator")
            print(f"    ✅ Корректно" if author_type == "generator" else "❌ Ошибка")
    
    print("\n3. Тестирование проверки реестра автогенераторов...")
    registry_check = check_generator_registry("docs/auto_generated/api_documentation.md")
    print(f"  Проверка реестра: {'✅ Найден' if registry_check else '❌ Не найден'}")
    
    print("\n4. Сканирование функций-генераторов в кодовой базе...")
    generator_functions = scan_for_generator_functions()
    print(f"  Найдено функций-генераторов: {len(generator_functions)}")
    
    for func in generator_functions:
        print(f"    - {func['function']} в {func['file']}")
    
    print("\n5. Тестирование интеграции с Content.json...")
    update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
    
    if os.path.exists('content/Content.json'):
        with open('content/Content.json', 'r', encoding='utf-8') as f:
            content_data = json.load(f)
        
        generator_files = [entry for entry in content_data if entry.get('author') == 'generator']
        print(f"  Файлов с авторством 'generator' в Content.json: {len(generator_files)}")
        
        for entry in generator_files:
            editable = entry.get('editable', True)
            print(f"    - {entry['path']}: editable={editable}")
            if not editable:
                print(f"      ✅ Корректно защищен от редактирования")
            else:
                print(f"      ❌ Должен быть защищен от редактирования")
    
    print("\n6. Проверка Description_for_agents.md...")
    if os.path.exists('content/Description_for_agents.md'):
        with open('content/Description_for_agents.md', 'r', encoding='utf-8') as f:
            desc_content = f.read()
        
        has_generator_icon = '⚙️' in desc_content
        has_lock_icon = '🔒' in desc_content
        
        print(f"  Иконка генератора (⚙️): {'✅ Найдена' if has_generator_icon else '❌ Не найдена'}")
        print(f"  Иконка блокировки (🔒): {'✅ Найдена' if has_lock_icon else '❌ Не найдена'}")
    
    print("\n=== Тестирование завершено ===")

def cleanup_test_files():
    """Очищает тестовые файлы после тестирования"""
    print("\n🧹 Очистка тестовых файлов...")
    
    if os.path.exists("docs/auto_generated"):
        shutil.rmtree("docs/auto_generated")
        print("  ✅ Удалена папка docs/auto_generated")

if __name__ == "__main__":
    try:
        test_enhanced_generator_detection()
        
        response = input("\nОчистить тестовые файлы? (y/n): ")
        if response.lower() in ['y', 'yes', 'да', 'д']:
            cleanup_test_files()
        else:
            print("Тестовые файлы сохранены для дальнейшего анализа.")
            
    except Exception as e:
        print(f"❌ Ошибка при тестировании: {e}")
        import traceback
        traceback.print_exc()
