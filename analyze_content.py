#!/usr/bin/env python3

import json
import os

def analyze_content_json():
    """Analyze the generated Content.json file"""
    print("=== Content.json Analysis ===")
    
    if not os.path.exists('content/Content.json'):
        print("❌ Content.json not found")
        return
    
    with open('content/Content.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"✅ Total files: {len(data)}")
    
    authors = {}
    editable_count = 0
    for entry in data:
        author = entry.get('author', 'unknown')
        authors[author] = authors.get(author, 0) + 1
        if entry.get('editable', False):
            editable_count += 1
    
    print(f"📊 Author distribution: {authors}")
    print(f"✏️ Editable files: {editable_count}/{len(data)}")
    
    sample_entry = data[0] if data else {}
    required_fields = ['file_id', 'title', 'path', 'editable', 'author', 'headers']
    missing_fields = [field for field in required_fields if field not in sample_entry]
    
    if missing_fields:
        print(f"❌ Missing required fields: {missing_fields}")
    else:
        print("✅ All required fields present")
    
    if data and 'headers' in data[0] and data[0]['headers']:
        header = data[0]['headers'][0]
        header_fields = ['id', 'level', 'title', 'excerpt', 'parent_id']
        missing_header_fields = [field for field in header_fields if field not in header]
        
        if missing_header_fields:
            print(f"❌ Missing header fields: {missing_header_fields}")
        else:
            print("✅ Header structure compliant")
    
    print(f"📝 Sample entry keys: {list(sample_entry.keys())}")
    
    return data

if __name__ == "__main__":
    analyze_content_json()
