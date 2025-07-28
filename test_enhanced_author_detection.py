#!/usr/bin/env python3

import os
import sys
import tempfile
import shutil
sys.path.insert(0, '.')

from update_docs.core import (
    generate_persistent_file_id,
    detect_author_type_enhanced,
    classify_author_from_git,
    match_file_by_content,
    build_content_json,
    update_content_system
)

def test_enhanced_author_detection():
    """Test the enhanced author detection functionality"""
    print("Testing enhanced author detection...")
    
    author, source = detect_author_type_enhanced("", "<!-- AUTO-GENERATED -->")
    assert author == "generator" and source == "comment_marker"
    print("✅ Comment marker detection works")
    
    git_info = {
        'last_author_email': 'devin@example.com',
        'last_author_name': 'Devin AI'
    }
    author_type = classify_author_from_git(git_info)
    assert author_type == "ai"
    print("✅ Git author classification works")
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("# Test Content\nSome content here")
        temp_file = f.name
    
    try:
        file_id = generate_persistent_file_id(temp_file)
        assert file_id.startswith("tmp") or "test" in file_id.lower()
        assert len(file_id.split("-")[-1]) == 8  # MD5 hash length
        print("✅ Persistent file ID generation works")
    finally:
        os.unlink(temp_file)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        docs_dir = os.path.join(temp_dir, "docs")
        os.makedirs(docs_dir)
        
        test_file = os.path.join(docs_dir, "test.md")
        with open(test_file, 'w') as f:
            f.write("# Test Document\nContent here")
        
        entries = build_content_json(docs_dir)
        assert len(entries) == 1
        assert entries[0]["title"] == "Test Document"
        assert entries[0]["author"] in ["human", "ai", "generator", "mixed"]
        assert "editable" in entries[0]
        assert "file_id" in entries[0]
        print("✅ Content.json generation works")
    
    print("✅ All enhanced author detection tests passed!")

if __name__ == "__main__":
    test_enhanced_author_detection()
