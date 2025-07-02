#!/usr/bin/env python3

import os
import sys
sys.path.insert(0, '.')

from update_docs.core import update_content_system

def test_russian_navigation():
    """Test that Russian navigation links are generated correctly"""
    print("=== Testing Russian Navigation Links ===")
    
    update_content_system('docs', 'content/Content.json', 'content/Description_for_agents.md')
    
    sample_files = ['docs/setup.md', 'docs/authentication.md', 'docs/README.md']
    
    for file_path in sample_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            first_line = lines[0] if lines else ""
            
            print(f"\n{file_path}:")
            print(f"  First line: {first_line}")
            
            has_home = 'Домой' in first_line
            has_back = 'Назад' in first_line
            has_broken = 'basic_toc.md' in content or 'comprehensive_toc.md' in content
            
            print(f"  Has 'Домой': {has_home}")
            print(f"  Has 'Назад': {has_back}")
            print(f"  Has broken links: {has_broken}")
    
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    has_content_json_link = 'content/Content.json' in readme_content
    has_description_link = 'content/Description_for_agents.md' in readme_content
    
    print(f"\nREADME.md navigation:")
    print(f"  Has Content.json link: {has_content_json_link}")
    print(f"  Has Description_for_agents.md link: {has_description_link}")

if __name__ == "__main__":
    test_russian_navigation()
