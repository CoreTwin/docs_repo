#!/usr/bin/env python3

import os
import sys
sys.path.insert(0, '.')

from update_docs.core import update_content_system

def test_content_system():
    """Test the Content.json system functionality"""
    print("Testing Content.json system...")
    
    os.makedirs('test_content', exist_ok=True)
    
    try:
        update_content_system('docs', 'test_content/Content.json', 'test_content/Description_for_agents.md')
        
        if os.path.exists('test_content/Content.json'):
            print("✅ Content.json created successfully")
        else:
            print("❌ Content.json not created")
            
        if os.path.exists('test_content/Description_for_agents.md'):
            print("✅ Description_for_agents.md created successfully")
        else:
            print("❌ Description_for_agents.md not created")
            
        print("✅ Content.json system test completed successfully")
        return True
        
    except Exception as e:
        print(f"❌ Content.json system test failed: {e}")
        return False

if __name__ == "__main__":
    test_content_system()
