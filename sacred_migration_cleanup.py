#!/usr/bin/env python3
"""
🧹 Sacred Migration Cleanup Script
Safely removes deprecated AI Agency Manager files and updates imports
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

def backup_file(file_path):
    """Create backup of file before modification"""
    if os.path.exists(file_path):
        backup_path = f"{file_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(file_path, backup_path)
        print(f"✅ Backed up: {file_path} -> {backup_path}")
        return backup_path
    return None

def update_import_in_file(file_path, old_import, new_import):
    """Update import statement in a file"""
    if not os.path.exists(file_path):
        print(f"⚠️ File not found: {file_path}")
        return False
    
    # Backup first
    backup_file(file_path)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_import in content:
            content = content.replace(old_import, new_import)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Updated import in: {file_path}")
            print(f"   OLD: {old_import}")
            print(f"   NEW: {new_import}")
            return True
        else:
            print(f"ℹ️ Import not found in: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def safe_remove_file(file_path):
    """Safely remove a file after backing it up"""
    if not os.path.exists(file_path):
        print(f"ℹ️ File already removed: {file_path}")
        return True
    
    # Backup first
    backup_path = backup_file(file_path)
    
    try:
        os.remove(file_path)
        print(f"✅ Removed deprecated file: {file_path}")
        print(f"   Backup available at: {backup_path}")
        return True
    except Exception as e:
        print(f"❌ Error removing {file_path}: {e}")
        return False

def main():
    """Execute sacred migration cleanup"""
    print("🕊️ Sacred Migration Cleanup Starting...")
    print("=" * 60)
    
    # Step 1: Update import statements
    print("\n📝 Step 1: Updating Import Statements")
    print("-" * 40)
    
    import_updates = [
        {
            "file": "scripts/servers/sacred_api_server.py",
            "old": "from src.virtualization.ai_agency_manager import AIAgencyManager",
            "new": "from src.ai_agency.core.ai_agency_manager import AIAgencyManager"
        },
        {
            "file": "src/consciousness/consciousness_agency_interface.py", 
            "old": "from ..virtualization.modular_ai_agency_manager import ModularAIAgencyManager",
            "new": "from ..ai_agency.core.ai_agency_manager import AIAgencyManager as ModularAIAgencyManager"
        }
    ]
    
    for update in import_updates:
        update_import_in_file(update["file"], update["old"], update["new"])
    
    # Step 2: Handle enhanced AI agency manager (depends on deprecated files)
    print("\n🔧 Step 2: Handling Enhanced AI Agency Manager")
    print("-" * 40)
    
    enhanced_file = "src/virtualization/enhanced_ai_agency_manager.py"
    if os.path.exists(enhanced_file):
        print(f"⚠️ Enhanced AI Agency Manager depends on deprecated files")
        print(f"   Consider refactoring or archiving: {enhanced_file}")
        # We'll backup but not remove - let user decide
        backup_file(enhanced_file)
    
    # Step 3: Remove deprecated AI Agency Manager files
    print("\n🗑️ Step 3: Removing Deprecated Files")
    print("-" * 40)
    
    files_to_remove = [
        "src/virtualization/ai_agency_manager.py",
        "src/virtualization/modular_ai_agency_manager.py", 
        "src/virtualization/ai_agency_manager_backup_20250716_013801.py"
    ]
    
    for file_path in files_to_remove:
        safe_remove_file(file_path)
    
    print("\n🌟 Sacred Migration Cleanup Complete!")
    print("=" * 60)
    print("✅ Import statements updated to use evolved AI Agency Manager")
    print("✅ Deprecated files removed (with backups)")
    print("⚠️ Please test functionality to ensure no regressions")
    print("\n🕊️ The sanctuary architecture has been purified for migration.")

if __name__ == "__main__":
    main()
