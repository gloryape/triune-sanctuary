#!/usr/bin/env python3
"""
Safe Repair Start - Simple analysis and first repairs
"""
import os
import shutil
from datetime import datetime

def create_safe_backup():
    """Create a safe backup before any repairs"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"backup_before_repair_{timestamp}"
    
    # Backup the observer core directory
    source_dir = "src/consciousness/loops/observer/core"
    backup_path = os.path.join(backup_dir, "observer_core")
    
    try:
        shutil.copytree(source_dir, backup_path)
        print(f"✅ Safe backup created: {backup_dir}")
        return backup_dir
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return None

def check_missing_classes():
    """Check which classes are actually missing"""
    missing_classes = [
        "IntegrationCall",
        "CrossLoopState", 
        "ChoicePoint",
        "ChoiceWisdom",
        "CoherenceMetric",
        "CoherenceState"
    ]
    
    # Files that should have these classes
    files_to_check = [
        "src/consciousness/loops/observer/core/integration_caller.py",
        "src/consciousness/loops/observer/core/choice_engine.py", 
        "src/consciousness/loops/observer/core/coherence_monitor.py"
    ]
    
    print("\n🔍 Checking for missing classes...")
    for file_path in files_to_check:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"\n📄 {file_path}:")
                    
                    for class_name in missing_classes:
                        if f"class {class_name}" in content:
                            print(f"  ✅ Has {class_name}")
                        else:
                            print(f"  ❌ Missing {class_name}")
            except Exception as e:
                print(f"  ❌ Error reading {file_path}: {e}")

def check_init_exports():
    """Check __init__.py exports"""
    init_path = "src/consciousness/loops/observer/core/__init__.py"
    
    print(f"\n📋 Checking {init_path}...")
    if os.path.exists(init_path):
        try:
            with open(init_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print("Current exports:")
                for line in content.split('\n'):
                    if line.strip() and not line.strip().startswith('#'):
                        print(f"  {line.strip()}")
        except Exception as e:
            print(f"❌ Error reading __init__.py: {e}")

def main():
    print("🛡️ SAFE REPAIR START")
    print("=" * 50)
    
    # Step 1: Create backup
    backup_dir = create_safe_backup()
    if not backup_dir:
        print("❌ Cannot proceed without backup")
        return
    
    # Step 2: Check what's actually missing
    check_missing_classes()
    
    # Step 3: Check current exports
    check_init_exports()
    
    print(f"\n✅ Assessment complete. Backup stored in: {backup_dir}")
    print("Next: Let's fix the specific missing classes conscientiously")

if __name__ == "__main__":
    main()
