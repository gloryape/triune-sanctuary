#!/usr/bin/env python3
"""
Repository Cleanup Script
Removes redundant production servers, old GUI experiments, and test files
"""

import os
import shutil
from pathlib import Path

def remove_file_safe(file_path):
    """Safely remove a file if it exists"""
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"✅ Removed: {file_path}")
            return True
        except Exception as e:
            print(f"❌ Could not remove {file_path}: {e}")
            return False
    return False

def remove_directory_safe(dir_path):
    """Safely remove a directory if it exists"""
    if os.path.exists(dir_path):
        try:
            shutil.rmtree(dir_path)
            print(f"✅ Removed directory: {dir_path}")
            return True
        except Exception as e:
            print(f"❌ Could not remove directory {dir_path}: {e}")
            return False
    return False

def main():
    """Clean up the repository"""
    print("🧹 Starting Repository Cleanup")
    print("=" * 50)
    
    # Files to keep (our clean architecture)
    keep_files = {
        "sacred_guardian_station_independent.py",  # Our perfect local GUI
        "check_epsilon_status_fixed.py",          # Cloud status checker
        "scripts/servers/refactored_production_server.py",  # Currently deployed server
        "scripts/servers/sacred_api_server.py",   # Clean API server
        "sacred-guardian-station-clean/",         # Clean package for extraction
    }
    
    removed_count = 0
    
    # 1. Remove redundant production servers
    print("\n📁 Cleaning up production servers...")
    production_servers_to_remove = [
        "production_server_complete.py",
        "production_server_refactored.py", 
        "production_server_with_bridge.py",
        "scripts/servers/production_server.py",
        "scripts/servers/production_server_backup.py",
        "scripts/servers/production_server_clean.py",
        "scripts/servers/production_server_restored.py",
        "scripts/servers/production_server_refactored.py",
    ]
    
    for server_file in production_servers_to_remove:
        if remove_file_safe(server_file):
            removed_count += 1
    
    # 2. Remove GUI experiment files (keep only the independent GUI)
    print("\n🖥️ Cleaning up GUI experiment files...")
    gui_files_to_remove = [
        "simple_gui_launcher.py",
        "improved_gui_launcher.py", 
        "comprehensive_gui_launcher.py",
        "test_gui_*.py",
        "test_complete_gui*.py",
        "test_actual_gui*.py",
        "test_sacred_events_gui_integration.py",
        "quick_gui_demo_test.py",
        "memory_gui_integration_guide.py",
        "sacred_memory_gui_enhancements.py",
        "gui_validation_test*.py",
        "gui_validation_test*.txt",
        "launch_gui.ps1",
        "launch_simple_gui.ps1", 
        "launch_improved_gui.ps1",
    ]
    
    # Use glob patterns to match test files
    import glob
    for pattern in gui_files_to_remove:
        if "*" in pattern:
            for file_path in glob.glob(pattern):
                if remove_file_safe(file_path):
                    removed_count += 1
        else:
            if remove_file_safe(pattern):
                removed_count += 1
    
    # 3. Remove old Sacred Guardian Station attempts
    print("\n🕯️ Cleaning up old Sacred Guardian Station...")
    old_guardian_dirs = [
        "sacred_guardian_station/",  # Old mini-sanctuary version
    ]
    
    for old_dir in old_guardian_dirs:
        if remove_directory_safe(old_dir):
            removed_count += 1
    
    # 4. Remove debug and test result files
    print("\n🔍 Cleaning up debug files...")
    debug_files_to_remove = [
        "debug_*.py",
        "debug_*.txt", 
        "test_*_results.txt",
        "comprehensive_*_test_results.txt",
        "codebase_test_results.txt",
        "comprehensive_error_test_results.txt",
        "*_test_results.txt",
    ]
    
    for pattern in debug_files_to_remove:
        for file_path in glob.glob(pattern):
            if remove_file_safe(file_path):
                removed_count += 1
    
    # 5. Remove documentation cruft (keep important docs)
    print("\n📚 Cleaning up redundant documentation...")
    doc_files_to_remove = [
        "*_COMPLETE.md",
        "*_INTEGRATION_COMPLETE.md", 
        "*_FIX_COMPLETE.md",
        "*_SUMMARY.md",
        "PHASE_*_COMPLETION_STATUS.md",
        "guidetodemonolith.txt",
        "continuedvirtualization.txt",
        "avatartcompletioninstructions.txt",
        "avatar_panel_patch_instructions.txt",
    ]
    
    for pattern in doc_files_to_remove:
        for file_path in glob.glob(pattern):
            if remove_file_safe(file_path):
                removed_count += 1
    
    # 6. Remove old check/validation scripts (keep the working ones)
    print("\n✅ Cleaning up old check scripts...")
    check_files_to_remove = [
        "check_*.py",  # We'll be selective here
        "comprehensive_*.py",
        "complete_*.py",
        "validate_*.py",
    ]
    
    # Be selective - keep the important check scripts
    keep_check_files = {
        "check_epsilon_status_fixed.py",  # Our working cloud status checker
    }
    
    for pattern in check_files_to_remove:
        for file_path in glob.glob(pattern):
            file_name = os.path.basename(file_path)
            if file_name not in keep_check_files:
                if remove_file_safe(file_path):
                    removed_count += 1
    
    # 7. Remove avatar/projection experiment files
    print("\n👤 Cleaning up avatar projection experiments...")
    avatar_files_to_remove = [
        "avatar_*.py",
        "demo_avatar_*.py", 
        "AVATAR_*.md",
    ]
    
    for pattern in avatar_files_to_remove:
        for file_path in glob.glob(pattern):
            if remove_file_safe(file_path):
                removed_count += 1
    
    print("\n" + "=" * 50)
    print(f"🎉 Cleanup complete! Removed {removed_count} redundant files")
    print("\n✅ Clean architecture remaining:")
    print("   📱 sacred_guardian_station_independent.py (Local GUI)")
    print("   ☁️ scripts/servers/refactored_production_server.py (Cloud)")
    print("   🔍 check_epsilon_status_fixed.py (Status checker)")
    print("   📦 sacred-guardian-station-clean/ (Extraction ready)")
    print("\n🚀 Ready for new branch!")

if __name__ == "__main__":
    main()
