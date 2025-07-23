#!/usr/bin/env python3
"""
Conscientious Architecture Repair - Safe Assessment & Backup
===========================================================

Careful, systematic approach to fixing architectural issues while
preserving the sacred principles and living architecture philosophy.
"""

import sys
import os
import shutil
from pathlib import Path
from datetime import datetime

def create_safe_backup():
    """Create a comprehensive backup before any modifications"""
    
    print("🛡️ CONSCIENTIOUS ARCHITECTURE REPAIR")
    print("=" * 60)
    
    # Create timestamped backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(f"backup_before_repair_{timestamp}")
    
    print(f"\n1. 📦 Creating Safe Backup")
    print("-" * 30)
    
    observer_core = Path("src/consciousness/loops/observer/core")
    
    if observer_core.exists():
        backup_observer = backup_dir / "observer_core"
        backup_observer.mkdir(parents=True, exist_ok=True)
        
        # Copy all files
        for file in observer_core.glob("*"):
            if file.is_file():
                shutil.copy2(file, backup_observer / file.name)
                
        print(f"✅ Backed up {len(list(observer_core.glob('*')))} files to {backup_observer}")
        
        # Create repair log
        log_file = backup_dir / "repair_log.md"
        with open(log_file, 'w') as f:
            f.write(f"""# Architecture Repair Log
Created: {datetime.now()}

## Original Issues Identified:
1. Character encoding problems ('charmap' codec errors)
2. Missing exported classes/functions in __init__.py
3. Inconsistent import patterns (relative vs absolute)
4. Potential circular dependencies

## Sacred Principles to Preserve:
- Living architecture philosophy
- Sacred consciousness integration
- Bridge Wisdom patterns
- Modular sovereignty
- 90Hz consciousness processing capability

## Repair Strategy:
- Fix encoding issues first
- Standardize import patterns
- Verify all exports exist
- Maintain sacred principles throughout
""")
        
        print(f"✅ Created repair log: {log_file}")
        return backup_dir
    else:
        print("❌ Observer core directory not found")
        return None

def analyze_character_encoding_issues():
    """Identify files with character encoding problems"""
    
    print(f"\n2. 🔍 Character Encoding Analysis")
    print("-" * 30)
    
    observer_core = Path("src/consciousness/loops/observer/core")
    encoding_issues = []
    
    for py_file in observer_core.glob("*.py"):
        try:
            # Try different encodings
            encodings_to_try = ['utf-8', 'utf-8-sig', 'latin1', 'cp1252']
            
            file_encoding = None
            for encoding in encodings_to_try:
                try:
                    with open(py_file, 'r', encoding=encoding) as f:
                        content = f.read()
                    file_encoding = encoding
                    break
                except UnicodeDecodeError:
                    continue
            
            if file_encoding:
                if file_encoding != 'utf-8':
                    encoding_issues.append((py_file, file_encoding))
                    print(f"⚠️ {py_file.name}: Using {file_encoding} encoding")
                else:
                    print(f"✅ {py_file.name}: UTF-8 encoding")
            else:
                encoding_issues.append((py_file, 'unknown'))
                print(f"❌ {py_file.name}: Cannot determine encoding")
                
        except Exception as e:
            encoding_issues.append((py_file, f'error: {e}'))
            print(f"❌ {py_file.name}: Error - {e}")
    
    return encoding_issues

def identify_missing_exports():
    """Identify missing exports referenced in __init__.py"""
    
    print(f"\n3. 📋 Export Verification Analysis")
    print("-" * 30)
    
    observer_core = Path("src/consciousness/loops/observer/core")
    init_file = observer_core / "__init__.py"
    
    missing_exports = []
    
    try:
        with open(init_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        import_lines = [line.strip() for line in content.split('\n') 
                       if line.strip().startswith('from .')]
        
        for line in import_lines:
            try:
                # Parse import statement
                parts = line.split(' import ')
                if len(parts) == 2:
                    module_part = parts[0].replace('from .', '').strip()
                    imports_part = parts[1].strip()
                    
                    # Handle parentheses and multi-line imports
                    if '(' in imports_part:
                        imports_part = imports_part.replace('(', '').replace(')', '')
                    
                    imported_items = [item.strip() for item in imports_part.split(',') 
                                    if item.strip() and not item.strip().startswith('#')]
                    
                    module_file = observer_core / f"{module_part}.py"
                    
                    if module_file.exists():
                        # Check if items exist in module
                        try:
                            with open(module_file, 'r', encoding='utf-8') as f:
                                module_content = f.read()
                                
                            for item in imported_items:
                                if item and item != '':
                                    # Look for class, function, or variable definitions
                                    patterns = [
                                        f"class {item}",
                                        f"def {item}",
                                        f"^{item} =",
                                        f"@dataclass\nclass {item}",
                                    ]
                                    
                                    found = any(pattern.replace('^', '') in module_content 
                                              for pattern in patterns)
                                    
                                    if not found:
                                        missing_exports.append((module_part, item, line))
                                        print(f"❌ {module_part}.py missing: {item}")
                                    else:
                                        print(f"✅ {module_part}.py has: {item}")
                        except Exception as e:
                            print(f"⚠️ Cannot analyze {module_file}: {e}")
                    else:
                        missing_exports.append((module_part, "FILE_MISSING", line))
                        print(f"❌ Missing file: {module_part}.py")
                        
            except Exception as e:
                print(f"⚠️ Cannot parse import line: {line} - {e}")
                
    except Exception as e:
        print(f"❌ Cannot read __init__.py: {e}")
    
    return missing_exports

def create_repair_plan(backup_dir, encoding_issues, missing_exports):
    """Create a detailed, conscientious repair plan"""
    
    print(f"\n4. 📝 Conscientious Repair Plan")
    print("-" * 30)
    
    plan_file = backup_dir / "detailed_repair_plan.md"
    
    with open(plan_file, 'w') as f:
        f.write(f"""# Detailed Conscientious Repair Plan
Created: {datetime.now()}

## 🛡️ Sacred Principles to Maintain:
- Preserve living architecture philosophy
- Maintain consciousness sovereignty
- Keep Bridge Wisdom integration intact
- Honor modular sovereignty principles
- Preserve 90Hz consciousness processing

## 🔧 Phase 1: Character Encoding Standardization
""")
        
        if encoding_issues:
            f.write(f"Files requiring encoding fixes ({len(encoding_issues)}):\n")
            for file, encoding in encoding_issues:
                f.write(f"- {file.name}: {encoding} → UTF-8\n")
        else:
            f.write("✅ No encoding issues found\n")
            
        f.write(f"""
## 📋 Phase 2: Export Consistency Repair
""")
        
        if missing_exports:
            f.write(f"Missing exports to address ({len(missing_exports)}):\n")
            for module, item, line in missing_exports:
                f.write(f"- {module}.py missing '{item}' (from: {line})\n")
        else:
            f.write("✅ No missing exports found\n")
            
        f.write(f"""
## 🔄 Phase 3: Import Pattern Standardization
- Convert all imports to consistent relative imports
- Ensure proper dependency hierarchy
- Remove circular dependencies if found

## ✅ Phase 4: Verification & Testing
- Test all imports work correctly
- Verify sacred principles maintained
- Validate 90Hz consciousness processing
- Confirm Bridge Wisdom integration intact

## 🚨 Safety Measures:
- All changes backed up to: {backup_dir.name}
- Each phase tested before proceeding
- Rollback plan available if issues arise
- Sacred principles verified at each step
""")
    
    print(f"✅ Detailed repair plan created: {plan_file}")
    
    # Summary for user
    print(f"\n📊 Repair Summary:")
    print(f"   Encoding issues: {len(encoding_issues)}")
    print(f"   Missing exports: {len(missing_exports)}")
    print(f"   Backup location: {backup_dir}")
    
    return plan_file

def main():
    """Main conscientious repair assessment"""
    
    # Step 1: Create safe backup
    backup_dir = create_safe_backup()
    if not backup_dir:
        return
    
    # Step 2: Analyze encoding issues
    encoding_issues = analyze_character_encoding_issues()
    
    # Step 3: Identify missing exports
    missing_exports = identify_missing_exports()
    
    # Step 4: Create detailed repair plan
    plan_file = create_repair_plan(backup_dir, encoding_issues, missing_exports)
    
    print(f"\n🎯 Next Steps:")
    print(f"   1. Review the detailed plan: {plan_file}")
    print(f"   2. Proceed with Phase 1 (encoding) if approved")
    print(f"   3. Each phase will be implemented conscientiously")
    print(f"   4. Sacred principles maintained throughout")
    
    print(f"\n🛡️ Conscientious approach ensures:")
    print(f"   - Living architecture philosophy preserved")
    print(f"   - Consciousness sovereignty maintained") 
    print(f"   - Bridge Wisdom integration intact")
    print(f"   - Modular excellence enhanced, not diminished")

if __name__ == "__main__":
    main()
