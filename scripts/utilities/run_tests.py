#!/usr/bin/env python3
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
    print(f"\n🧪 Running {category_name} Tests")
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
    
    print("\n🏆 TEST SUITE COMPLETE!")

if __name__ == "__main__":
    main()
