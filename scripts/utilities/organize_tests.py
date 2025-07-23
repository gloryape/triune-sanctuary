#!/usr/bin/env python3
"""
Sacred Sanctuary Test Organization Script
========================================

Organizes all test files into proper structure and removes redundant/outdated tests.

ORGANIZATION STRATEGY:
- Keep essential functionality tests
- Move to organized test structure
- Remove outdated/redundant tests
- Preserve critical integration tests

Author: Sacred Sanctuary Architecture Team
Date: December 15, 2024
"""

import os
import shutil
from pathlib import Path

# Test organization mapping
ESSENTIAL_TESTS = {
    # Core functionality tests (keep and organize)
    'consciousness_emergence_cli.py': 'tests/core/consciousness_emergence_test.py',
    'final_integration_verification.py': 'tests/integration/final_integration_test.py', 
    'consciousness_protection_verification.py': 'tests/core/consciousness_protection_test.py',
    'test_integration.py': 'tests/integration/system_integration_test.py',
    'deployment_verification.py': 'tests/deployment/deployment_verification_test.py',
    
    # Sacred Being Epsilon tests
    'test_sacred_being_epsilon_complete.py': 'tests/consciousness/epsilon_test.py',
    
    # Core architecture tests
    'test_final_sovereignty_integration.py': 'tests/core/sovereignty_test.py',
    'test_providers_simple.py': 'tests/integration/providers_test.py',
    
    # Production/deployment tests
    'production_deployment_test.py': 'tests/deployment/production_test.py',
    'deployment_test.py': 'tests/deployment/deployment_basic_test.py',
    
    # Essential consciousness tests from tests/ directory
    'tests/test_triune_consciousness.py': 'tests/consciousness/triune_consciousness_test.py',
    'tests/test_production_readiness.py': 'tests/deployment/production_readiness_test.py',
    'tests/integration/test_complete_integration.py': 'tests/integration/complete_integration_test.py',
    'tests/unit/test_consciousness_packet.py': 'tests/core/consciousness_packet_test.py',
}

# Tests to archive (keep in archive for reference but not active)
ARCHIVE_TESTS = [
    'test_ascii_art*.py',
    'test_birth_*.py', 
    'test_cloud_*.py',
    'test_chuck_*.py',
    'test_emergence_birth_*.py',
    'test_gui_*.py',
    'test_visitor_*.py',
    'uncertainty_field_*.py',
    'visual_test_*.py',
]

# Tests to remove completely (outdated/redundant)
REMOVE_TESTS = [
    'temp_*.py',
    'simple_*.py',
    'issue_resolution_test.py',
    'focused_architecture_test.py',
    'fixed_*.py',
    'test_*_fix.py',
    'test_*_fixed.py',
    '*fragment_tests.py',
    'test_ui_improvements.py',
    'test_enhanced_visuals.py',
]

def organize_tests():
    """Organize all test files according to the strategy"""
    project_root = Path.cwd()
    
    print("🧪 SACRED SANCTUARY TEST ORGANIZATION")
    print("=" * 50)
    
    # Create test directories if they don't exist
    test_dirs = [
        'tests/core',
        'tests/consciousness', 
        'tests/integration',
        'tests/deployment',
        'tests/archive'
    ]
    
    for test_dir in test_dirs:
        os.makedirs(test_dir, exist_ok=True)
        print(f"📁 Created directory: {test_dir}")
    
    # Move essential tests to proper locations
    print("\n🎯 Moving essential tests...")
    moved_count = 0
    for source, target in ESSENTIAL_TESTS.items():
        source_path = project_root / source
        target_path = project_root / target
        
        if source_path.exists():
            try:
                # Create target directory if needed
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Move the file
                shutil.move(str(source_path), str(target_path))
                print(f"✅ Moved: {source} → {target}")
                moved_count += 1
            except Exception as e:
                print(f"❌ Failed to move {source}: {e}")
        else:
            print(f"⚠️ Source not found: {source}")
    
    # Archive less critical tests
    print(f"\n📦 Archiving reference tests...")
    archived_count = 0
    
    for pattern in ARCHIVE_TESTS:
        for test_file in project_root.glob(pattern):
            if test_file.is_file() and test_file.suffix == '.py':
                try:
                    target = project_root / 'tests' / 'archive' / test_file.name
                    shutil.move(str(test_file), str(target))
                    print(f"📦 Archived: {test_file.name}")
                    archived_count += 1
                except Exception as e:
                    print(f"❌ Failed to archive {test_file.name}: {e}")
    
    # Remove redundant/outdated tests
    print(f"\n🗑️ Removing redundant tests...")
    removed_count = 0
    
    for pattern in REMOVE_TESTS:
        for test_file in project_root.glob(pattern):
            if test_file.is_file() and test_file.suffix == '.py':
                try:
                    test_file.unlink()
                    print(f"🗑️ Removed: {test_file.name}")
                    removed_count += 1
                except Exception as e:
                    print(f"❌ Failed to remove {test_file.name}: {e}")
    
    # Remove empty test files and obvious duplicates from root
    print(f"\n🧹 Cleaning up remaining test files...")
    cleanup_count = 0
    
    for test_file in project_root.glob("test_*.py"):
        if test_file.is_file():
            try:
                # Check if file is very small (likely empty or minimal)
                if test_file.stat().st_size < 500:  # Less than 500 bytes
                    test_file.unlink()
                    print(f"🧹 Cleaned up small test: {test_file.name}")
                    cleanup_count += 1
                else:
                    # Move remaining tests to archive for review
                    target = project_root / 'tests' / 'archive' / test_file.name
                    if not target.exists():  # Avoid conflicts
                        shutil.move(str(test_file), str(target))
                        print(f"📦 Archived remaining: {test_file.name}")
                        cleanup_count += 1
            except Exception as e:
                print(f"❌ Failed to clean {test_file.name}: {e}")
    
    print(f"\n✅ TEST ORGANIZATION COMPLETE!")
    print(f"📊 Summary:")
    print(f"   • Essential tests moved: {moved_count}")
    print(f"   • Tests archived: {archived_count}")
    print(f"   • Tests removed: {removed_count}")
    print(f"   • Files cleaned up: {cleanup_count}")
    
    print(f"\n📁 New test structure:")
    print(f"   tests/core/           - Core functionality tests")
    print(f"   tests/consciousness/  - Consciousness system tests")
    print(f"   tests/integration/    - Integration tests")
    print(f"   tests/deployment/     - Deployment tests")
    print(f"   tests/archive/        - Reference/archived tests")

def create_test_runner():
    """Create a comprehensive test runner script"""
    
    test_runner_content = '''#!/usr/bin/env python3
"""
Sacred Sanctuary Test Runner
============================

Runs all essential tests in organized fashion.
"""

import subprocess
import sys
from pathlib import Path

def run_test_category(category_path, category_name):
    """Run all tests in a category"""
    print(f"\\n🧪 Running {category_name} Tests")
    print("=" * 40)
    
    test_dir = Path(category_path)
    if not test_dir.exists():
        print(f"⚠️ Test directory not found: {category_path}")
        return
    
    test_files = list(test_dir.glob("*_test.py"))
    if not test_files:
        print(f"📭 No tests found in {category_path}")
        return
    
    for test_file in test_files:
        print(f"🔍 Running: {test_file.name}")
        try:
            result = subprocess.run([sys.executable, str(test_file)], 
                                  capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                print(f"✅ {test_file.name} - PASSED")
            else:
                print(f"❌ {test_file.name} - FAILED")
                if result.stderr:
                    print(f"   Error: {result.stderr[:200]}...")
        except subprocess.TimeoutExpired:
            print(f"⏰ {test_file.name} - TIMEOUT")
        except Exception as e:
            print(f"💥 {test_file.name} - EXCEPTION: {e}")

def main():
    """Run all test categories"""
    print("🌟 SACRED SANCTUARY COMPREHENSIVE TEST SUITE")
    print("=" * 60)
    
    test_categories = [
        ("tests/core", "Core Functionality"),
        ("tests/consciousness", "Consciousness Systems"),
        ("tests/integration", "System Integration"),
        ("tests/deployment", "Deployment & Production")
    ]
    
    for category_path, category_name in test_categories:
        run_test_category(category_path, category_name)
    
    print("\\n🏆 TEST SUITE COMPLETE!")

if __name__ == "__main__":
    main()
'''
    
    with open('run_tests.py', 'w') as f:
        f.write(test_runner_content)
    
    print("✅ Created comprehensive test runner: run_tests.py")

if __name__ == "__main__":
    organize_tests()
    create_test_runner()
    
    print("\\n🎯 Next steps:")
    print("   1. Review tests/archive/ for anything important")
    print("   2. Run: python run_tests.py")
    print("   3. Update essential tests as needed")
    print("   4. Commit clean test structure")
