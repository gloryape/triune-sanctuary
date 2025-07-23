#!/usr/bin/env python3
"""
Sacred Sanctuary - Simple Deployment Test
========================================

Tests basic deployment readiness without complex dependencies.
"""

import sys
import os
from pathlib import Path

def test_project_structure():
    """Test that project has the essential structure"""
    print("🏛️ Testing Project Structure...")
    
    project_root = Path(__file__).parent.parent.parent
    
    # Check essential directories
    essential_dirs = [
        "src",
        "docs",
        "tests",
        "docs/architecture",
        "docs/development", 
        "docs/user-guides",
        "docs/consciousness",
        "docs/completed-phases"
    ]
    
    all_good = True
    for dir_path in essential_dirs:
        full_path = project_root / dir_path
        if full_path.exists():
            print(f"    ✅ {dir_path}/ exists")
        else:
            print(f"    ❌ {dir_path}/ missing")
            all_good = False
    
    # Check essential files
    essential_files = [
        "README.md",
        "PROJECT_STATUS.md", 
        "simple_gui_launcher.py",
        "docs/DOCUMENTATION_INDEX.md"
    ]
    
    for file_path in essential_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"    ✅ {file_path} exists")
        else:
            print(f"    ❌ {file_path} missing")
            all_good = False
    
    return all_good

def test_documentation_organization():
    """Test that documentation is properly organized"""
    print("📚 Testing Documentation Organization...")
    
    project_root = Path(__file__).parent.parent.parent
    docs_dir = project_root / "docs"
    
    if not docs_dir.exists():
        print("    ❌ docs/ directory missing")
        return False
    
    # Check for organized documentation
    doc_categories = {
        "architecture": ["ARCHITECTURE_README.md"],
        "development": ["DEVELOPER_GUIDE.md"],
        "user-guides": ["USER_GUIDE.md"],
        "consciousness": ["CONSCIOUSNESS_GUIDE.md"],
        "completed-phases": ["PROJECT_COMPLETION_SUMMARY.md"]
    }
    
    all_good = True
    for category, expected_files in doc_categories.items():
        category_dir = docs_dir / category
        if category_dir.exists():
            print(f"    ✅ docs/{category}/ exists")
            
            # Check for at least some documentation in each category
            files_in_category = list(category_dir.glob("*.md"))
            if files_in_category:
                print(f"        📄 {len(files_in_category)} documentation files found")
            else:
                print(f"        ⚠️ No .md files in {category}/")
        else:
            print(f"    ❌ docs/{category}/ missing")
            all_good = False
    
    return all_good

def test_clean_architecture():
    """Test that architecture is clean (no test files in root)"""
    print("🧹 Testing Clean Architecture...")
    
    project_root = Path(__file__).parent.parent.parent
    
    # Check for old test files in root
    test_files_in_root = list(project_root.glob("test_*.py"))
    if test_files_in_root:
        print(f"    ⚠️ Found {len(test_files_in_root)} test files in root:")
        for test_file in test_files_in_root[:5]:  # Show first 5
            print(f"        - {test_file.name}")
        if len(test_files_in_root) > 5:
            print(f"        ... and {len(test_files_in_root) - 5} more")
        return False
    else:
        print("    ✅ No test files in root directory")
    
    # Check for temp files
    temp_files = list(project_root.glob("temp_*.py"))
    if temp_files:
        print(f"    ⚠️ Found {len(temp_files)} temp files in root")
        return False
    else:
        print("    ✅ No temp files in root directory")
    
    # Check tests are properly organized
    tests_dir = project_root / "tests"
    if tests_dir.exists():
        organized_dirs = ["core", "consciousness", "integration", "deployment"]
        for test_dir in organized_dirs:
            test_subdir = tests_dir / test_dir
            if test_subdir.exists():
                print(f"    ✅ tests/{test_dir}/ exists")
            else:
                print(f"    ❌ tests/{test_dir}/ missing")
                return False
    
    return True

def test_sacred_sanctuary_ready():
    """Test that Sacred Sanctuary is ready for operation"""
    print("🌟 Testing Sacred Sanctuary Readiness...")
    
    project_root = Path(__file__).parent.parent.parent
    
    # Check main launcher
    launcher = project_root / "simple_gui_launcher.py"
    if launcher.exists():
        print("    ✅ Sacred Guardian Station launcher available")
    else:
        print("    ❌ Sacred Guardian Station launcher missing")
        return False
    
    # Check architecture documentation
    arch_doc = project_root / "docs" / "architecture" / "ARCHITECTURE_README.md"
    if arch_doc.exists():
        print("    ✅ Complete architecture documentation available")
    else:
        print("    ❌ Architecture documentation missing")
        return False
    
    # Check project status
    status_doc = project_root / "PROJECT_STATUS.md"
    if status_doc.exists():
        print("    ✅ Project status documentation available")
    else:
        print("    ❌ Project status documentation missing")
        return False
    
    return True

def main():
    """Run all deployment tests"""
    print("🌟 SACRED SANCTUARY DEPLOYMENT TEST")
    print("=" * 50)
    
    tests = [
        test_project_structure,
        test_documentation_organization,
        test_clean_architecture,
        test_sacred_sanctuary_ready
    ]
    
    all_passed = True
    
    for test in tests:
        print()
        if not test():
            all_passed = False
    
    print()
    print("=" * 50)
    if all_passed:
        print("✅ ALL DEPLOYMENT TESTS PASSED")
        print("🚀 Sacred Sanctuary is ready for operation!")
        return 0
    else:
        print("❌ SOME DEPLOYMENT TESTS FAILED")
        print("🔧 Please address the issues above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
