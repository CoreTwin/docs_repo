#!/usr/bin/env python3

import os
import sys
import pytest
sys.path.insert(0, '.')

from update_docs.core import update_content_system

def test_content_system():
    """Test the Content.json system functionality"""
    print("Testing Content.json system...")
    
    os.makedirs('test_content', exist_ok=True)
    
    try:
        update_content_system('docs', 'test_content/Content.json', 'test_content/Description_for_agents.md')

        assert os.path.exists('test_content/Content.json'), 'Content.json not created'
        assert os.path.exists('test_content/Description_for_agents.md'), 'Description_for_agents.md not created'

        print("✅ Content.json system test completed successfully")

    except Exception as e:
        print(f"❌ Content.json system test failed: {e}")
        pytest.fail('failure')

if __name__ == "__main__":
    test_content_system()
