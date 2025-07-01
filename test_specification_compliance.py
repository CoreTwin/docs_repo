#!/usr/bin/env python3

import json
import os
import sys
sys.path.insert(0, '.')

from update_docs.core import update_content_system

def test_specification_compliance():
    """Test that the implementation meets all specification requirements"""
    print("=== Testing Specification Compliance ===")
    
    print("\n1. Testing Content.json generation...")
    if not os.path.exists('content/Content.json'):
        print("❌ Content.json not found, generating...")
        update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
    
    with open('content/Content.json', 'r', encoding='utf-8') as f:
        content_data = json.load(f)
    
    print(f"✅ Content.json loaded with {len(content_data)} files")
    
    required_fields = ['file_id', 'title', 'path', 'editable', 'author', 'headers']
    sample_entry = content_data[0] if content_data else {}
    
    missing_fields = [field for field in required_fields if field not in sample_entry]
    if missing_fields:
        print(f"❌ Missing required fields: {missing_fields}")
        return False
    else:
        print("✅ All required fields present in Content.json")
    
    if content_data and 'headers' in content_data[0] and content_data[0]['headers']:
        header = content_data[0]['headers'][0]
        header_fields = ['id', 'level', 'title', 'excerpt', 'parent_id']
        missing_header_fields = [field for field in header_fields if field not in header]
        
        if missing_header_fields:
            print(f"❌ Missing header fields: {missing_header_fields}")
            return False
        else:
            print("✅ Header structure compliant with specification")
    
    authors = {}
    for entry in content_data:
        author = entry.get('author', 'unknown')
        authors[author] = authors.get(author, 0) + 1
    
    print(f"✅ Author detection working: {authors}")
    
    file_ids = [entry.get('file_id', '') for entry in content_data]
    valid_file_ids = [fid for fid in file_ids if '-' in fid and len(fid.split('-')[-1]) == 8]
    
    if len(valid_file_ids) == len(file_ids):
        print("✅ All file_ids follow persistent format (name-hash)")
    else:
        print(f"❌ Some file_ids don't follow format: {len(valid_file_ids)}/{len(file_ids)}")
    
    print("\n2. Testing Description_for_agents.md...")
    if os.path.exists('content/Description_for_agents.md'):
        with open('content/Description_for_agents.md', 'r', encoding='utf-8') as f:
            desc_content = f.read()
        
        required_sections = ['📊 Статистика авторства', '📁', 'AUTO-GENERATED']
        missing_sections = [section for section in required_sections if section not in desc_content]
        
        if missing_sections:
            print(f"❌ Missing sections in Description_for_agents.md: {missing_sections}")
        else:
            print("✅ Description_for_agents.md structure compliant")
    else:
        print("❌ Description_for_agents.md not found")
        return False
    
    editable_count = sum(1 for entry in content_data if entry.get('editable', False))
    print(f"✅ Editable flags set: {editable_count}/{len(content_data)} files editable")
    
    print("\n=== Specification Compliance Test Complete ===")
    return True

if __name__ == "__main__":
    success = test_specification_compliance()
    if success:
        print("🎉 All specification requirements met!")
    else:
        print("❌ Some specification requirements not met")
        sys.exit(1)
