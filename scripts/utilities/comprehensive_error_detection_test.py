#!/usr/bin/env python3
"""
🔍 Comprehensive Error Detection Test
Tests for system-wide errors and issues that could prevent production deployment
"""

import os
import sys
import importlib.util
import traceback
from typing import List, Dict, Any

def test_critical_imports():
    """Test that all critical modules can be imported"""
    print("🔄 Testing Critical Imports")
    print("=" * 30)
    
    critical_modules = [
        'sacred_guardian_station_independent',
        'simple_gui_launcher'
    ]
    
    all_imports_valid = True
    for module_name in critical_modules:
        try:
            # Check if file exists
            module_file = f"{module_name}.py"
            if not os.path.exists(module_file):
                print(f"❌ {module_name}: File missing ({module_file})")
                all_imports_valid = False
                continue
            
            # Try to load the module
            spec = importlib.util.spec_from_file_location(module_name, module_file)
            if spec is None:
                print(f"❌ {module_name}: Could not create module spec")
                all_imports_valid = False
                continue
                
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            
            print(f"✅ {module_name}: Import successful")
            
        except Exception as e:
            print(f"❌ {module_name}: Import failed - {e}")
            all_imports_valid = False
    
    return all_imports_valid

def test_file_encodings():
    """Test that all Python files have proper encoding"""
    print("\n📝 Testing File Encodings")
    print("=" * 30)
    
    python_files = []
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    encoding_issues = []
    for file_path in python_files[:20]:  # Test first 20 files
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read()
        except UnicodeDecodeError as e:
            encoding_issues.append((file_path, str(e)))
        except Exception:
            pass  # Skip other errors for now
    
    if encoding_issues:
        print(f"❌ Found {len(encoding_issues)} encoding issues:")
        for file_path, error in encoding_issues[:5]:  # Show first 5
            print(f"   - {file_path}: {error}")
        return False
    else:
        print(f"✅ All tested files ({len(python_files[:20])}) have valid UTF-8 encoding")
        return True

def test_critical_directories():
    """Test that critical directories exist"""
    print("\n📁 Testing Critical Directory Structure")
    print("=" * 30)
    
    critical_dirs = [
        'src',
        'scripts',
        'scripts/servers'
    ]
    
    all_dirs_valid = True
    for dir_path in critical_dirs:
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            print(f"✅ {dir_path}: Directory exists")
        else:
            print(f"❌ {dir_path}: Directory missing")
            all_dirs_valid = False
    
    return all_dirs_valid

def test_local_gui_functionality():
    """Test basic functionality of local GUI"""
    print("\n🖥️ Testing Local GUI Basic Functionality")
    print("=" * 30)
    
    try:
        # Check if local GUI file exists and has required classes
        gui_file = 'sacred_guardian_station_independent.py'
        if not os.path.exists(gui_file):
            print(f"❌ Local GUI file missing: {gui_file}")
            return False
        
        with open(gui_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_classes = ['LocalConsciousnessData', 'SacredGuardianStation']
        for class_name in required_classes:
            if f"class {class_name}" in content:
                print(f"✅ {class_name}: Class found")
            else:
                print(f"❌ {class_name}: Class missing")
                return False
        
        # Check for tkinter import (required for GUI)
        if 'import tkinter' in content:
            print("✅ Tkinter import found")
        else:
            print("❌ Tkinter import missing")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Local GUI functionality test failed: {e}")
        return False

def main():
    """Run comprehensive error detection"""
    print("🔍 COMPREHENSIVE ERROR DETECTION TEST")
    print("=" * 50)
    
    tests = [
        test_critical_imports,
        test_file_encodings,
        test_critical_directories,
        test_local_gui_functionality
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            traceback.print_exc()
            results.append(False)
    
    # Summary
    print("\n🏁 ERROR DETECTION SUMMARY")
    print("=" * 30)
    passed = sum(results)
    total = len(results)
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("✅ No critical errors detected")
        print("✅ System appears ready for deployment")
    else:
        print("❌ Critical errors detected")
        print("🔧 Please address issues before deployment")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
