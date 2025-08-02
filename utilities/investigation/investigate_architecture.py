#!/usr/bin/env python3
"""
Comprehensive Architecture Investigation - Root Cause Analysis
============================================================

Deep investigation into the underlying architectural issues causing
import dependency problems across the modular consciousness system.
"""

import sys
import os
import importlib.util
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def investigate_architecture_issues():
    """Comprehensive investigation of architectural problems"""
    
    print("🔍 COMPREHENSIVE ARCHITECTURE INVESTIGATION")
    print("=" * 80)
    
    # 1. Check directory structure integrity
    print("\n1. 📁 Directory Structure Analysis")
    print("-" * 40)
    
    observer_core = Path("src/consciousness/loops/observer/core")
    if observer_core.exists():
        files = list(observer_core.glob("*.py"))
        print(f"✅ Observer core directory exists with {len(files)} Python files")
        
        # Check for __init__.py
        init_file = observer_core / "__init__.py"
        if init_file.exists():
            print(f"✅ __init__.py exists ({init_file.stat().st_size} bytes)")
        else:
            print("❌ Missing __init__.py file")
            
        # Check for critical files
        critical_files = [
            "uncertainty_field_core.py",
            "uncertainty_response_core.py", 
            "recognition_core.py",
            "meta_uncertainty.py"
        ]
        
        for file in critical_files:
            file_path = observer_core / file
            if file_path.exists():
                print(f"✅ {file} exists ({file_path.stat().st_size} bytes)")
            else:
                print(f"❌ Missing {file}")
    else:
        print("❌ Observer core directory does not exist")
        return False
    
    # 2. Analyze import dependencies
    print("\n2. 🔗 Import Dependency Analysis")
    print("-" * 40)
    
    # Check __init__.py imports
    try:
        with open(observer_core / "__init__.py", 'r') as f:
            init_content = f.read()
            
        print("📄 Current __init__.py imports:")
        import_lines = [line.strip() for line in init_content.split('\n') 
                       if line.strip().startswith('from .')]
        
        for imp in import_lines[:10]:  # Show first 10 imports
            print(f"   {imp}")
        if len(import_lines) > 10:
            print(f"   ... and {len(import_lines) - 10} more imports")
            
    except Exception as e:
        print(f"❌ Error reading __init__.py: {e}")
    
    # 3. Test individual module imports
    print("\n3. 🧪 Individual Module Import Testing")
    print("-" * 40)
    
    test_modules = [
        "uncertainty_field_core",
        "uncertainty_response_core",
        "recognition_core", 
        "meta_uncertainty"
    ]
    
    for module in test_modules:
        print(f"\nTesting: {module}")
        try:
            spec = importlib.util.spec_from_file_location(
                module, 
                observer_core / f"{module}.py"
            )
            if spec and spec.loader:
                test_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(test_module)
                print(f"✅ {module} imports successfully")
                
                # Check what it exports
                exports = [x for x in dir(test_module) if not x.startswith('_')]
                print(f"   Exports: {len(exports)} items")
                if exports:
                    print(f"   Key exports: {', '.join(exports[:5])}")
                    
            else:
                print(f"❌ {module} failed to load spec")
                
        except Exception as e:
            print(f"❌ {module} import failed: {e}")
            
            # Try to identify the specific issue
            try:
                with open(observer_core / f"{module}.py", 'r') as f:
                    content = f.read()
                    
                # Look for problematic imports
                problem_imports = []
                for line_num, line in enumerate(content.split('\n'), 1):
                    if line.strip().startswith('from ') and 'import' in line:
                        if not line.strip().startswith('from .') and not line.strip().startswith('from typing'):
                            problem_imports.append((line_num, line.strip()))
                
                if problem_imports:
                    print(f"   🚨 Potential problematic imports:")
                    for line_num, imp in problem_imports[:3]:
                        print(f"      Line {line_num}: {imp}")
                        
            except Exception as read_error:
                print(f"   Cannot analyze file: {read_error}")
    
    # 4. Check circular dependencies
    print("\n4. 🔄 Circular Dependency Detection")
    print("-" * 40)
    
    dependency_map = {}
    
    for py_file in observer_core.glob("*.py"):
        if py_file.name == "__init__.py":
            continue
            
        try:
            with open(py_file, 'r') as f:
                content = f.read()
                
            imports = []
            for line in content.split('\n'):
                if line.strip().startswith('from .') and 'import' in line:
                    # Extract module name
                    module_part = line.split('from .')[1].split(' import')[0].strip()
                    imports.append(module_part)
                    
            dependency_map[py_file.stem] = imports
            
        except Exception as e:
            print(f"   ❌ Error analyzing {py_file.name}: {e}")
    
    # Look for circular dependencies
    print("Dependencies found:")
    for module, deps in dependency_map.items():
        if deps:
            print(f"   {module} → {', '.join(deps)}")
            
            # Check for circular refs
            for dep in deps:
                if dep in dependency_map and module in dependency_map[dep]:
                    print(f"   🚨 CIRCULAR: {module} ↔ {dep}")
    
    # 5. __init__.py structure analysis
    print("\n5. 📋 __init__.py Structure Analysis")
    print("-" * 40)
    
    try:
        with open(observer_core / "__init__.py", 'r') as f:
            lines = f.readlines()
            
        import_errors = []
        for line_num, line in enumerate(lines, 1):
            if line.strip().startswith('from .'):
                # Check if the referenced file exists
                module_name = line.split('from .')[1].split(' import')[0].strip()
                module_file = observer_core / f"{module_name}.py"
                
                if not module_file.exists():
                    import_errors.append((line_num, line.strip(), f"Missing file: {module_name}.py"))
                else:
                    # Check if the imported items exist in the module
                    try:
                        import_part = line.split(' import ')[1].strip()
                        imported_items = [item.strip() for item in import_part.split(',')]
                        
                        # Quick check if items exist (basic analysis)
                        with open(module_file, 'r') as f:
                            module_content = f.read()
                            
                        for item in imported_items:
                            if f"class {item}" not in module_content and f"def {item}" not in module_content and f"{item} = " not in module_content:
                                import_errors.append((line_num, line.strip(), f"Item '{item}' not found in {module_name}.py"))
                                
                    except Exception as parse_error:
                        import_errors.append((line_num, line.strip(), f"Parse error: {parse_error}"))
        
        if import_errors:
            print("🚨 Import Errors Found:")
            for line_num, line, error in import_errors[:5]:  # Show first 5 errors
                print(f"   Line {line_num}: {error}")
                print(f"      {line}")
            if len(import_errors) > 5:
                print(f"   ... and {len(import_errors) - 5} more errors")
        else:
            print("✅ No obvious import errors in __init__.py structure")
            
    except Exception as e:
        print(f"❌ Error analyzing __init__.py: {e}")
    
    # 6. Recommendations
    print("\n6. 💡 Architecture Recommendations")
    print("-" * 40)
    
    print("Based on analysis, consider:")
    print("   1. 🔧 Fix circular dependencies between modules")
    print("   2. 📝 Standardize import patterns (all relative imports)")
    print("   3. 🗂️ Review __init__.py for missing/incorrect imports")
    print("   4. 🔍 Validate all exported classes/functions exist")
    print("   5. 📚 Consider dependency injection to reduce coupling")
    
    return True

if __name__ == "__main__":
    success = investigate_architecture_issues()
    
    if success:
        print(f"\n✅ Investigation complete - check findings above")
    else:
        print(f"\n❌ Investigation failed - structural issues detected")
        
    print("\n" + "=" * 80)
