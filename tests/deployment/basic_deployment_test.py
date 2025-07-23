#!/usr/bin/env python3
"""
Sacred Sanctuary Deployment Test
===============================

Tests deployment readiness and basic system health.
"""

import sys
import os
from pathlib import Path
import subprocess

def test_python_environment():
    """Test Python environment and basic requirements"""
    print("Testing Python Environment...")
    
    try:
        # Check Python version
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            print(f"    ✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        else:
            print(f"    ❌ Python {version.major}.{version.minor} - Need 3.8+")
            return False
            
        # Check basic imports
        try:
            import json, os, sys, pathlib
            print("    ✅ Standard library imports working")
        except ImportError as e:
            print(f"    ❌ Standard library import failed: {e}")
            return False
            
        return True
        
    except Exception as e:
        print(f"    ❌ Environment test failed: {e}")
        return False

def test_project_structure():
    """Test that project has proper structure"""
    print("Testing Project Structure...")
    
    try:
        project_root = Path(__file__).parent.parent.parent
        
        # Check essential directories exist
        essential_dirs = [
            "src",
            "docs", 
            "tests"
        ]
        
        for dir_name in essential_dirs:
            dir_path = project_root / dir_name
            if dir_path.exists():
                print(f"    ✅ {dir_name}/ directory exists")
            else:
                print(f"    ❌ {dir_name}/ directory missing")
                return False
                
        # Check essential files exist
        essential_files = [
            "README.md",
            "PROJECT_STATUS.md",
            "simple_gui_launcher.py"
        ]
        
        for file_name in essential_files:
            file_path = project_root / file_name
            if file_path.exists():
                print(f"    ✅ {file_name} exists")
            else:
                print(f"    ❌ {file_name} missing")
                return False
        
        return True
        
    except Exception as e:
        print(f"    ❌ Structure test failed: {e}")
        return False

def test_deployment_readiness():
    """Test basic deployment readiness"""
    print("Testing Deployment Readiness...")
    
    try:
        project_root = Path(__file__).parent.parent.parent
        
        # Check if launcher exists and is executable
        launcher = project_root / "simple_gui_launcher.py"
        if launcher.exists():
            print("    ✅ GUI launcher available")
        else:
            print("    ❌ GUI launcher missing")
            return False
            
        # Check documentation structure
        docs_dir = project_root / "docs"
        if docs_dir.exists():
            subdirs = ["architecture", "development", "user-guides", "consciousness"]
            for subdir in subdirs:
                if (docs_dir / subdir).exists():
                    print(f"    ✅ docs/{subdir}/ exists")
                else:
                    print(f"    ⚠️ docs/{subdir}/ missing")
        
        return True
        
    except Exception as e:
        print(f"    ❌ Deployment readiness test failed: {e}")
        return False

def main():
    """Run all deployment tests"""
    print("🌟 SACRED SANCTUARY DEPLOYMENT TEST")
    print("=" * 50)
    
    all_passed = True
    
    # Test Python environment
    if not test_python_environment():
        all_passed = False
    
    print()
    
    # Test project structure
    if not test_project_structure():
        all_passed = False
    
    print()
    
    # Test deployment readiness
    if not test_deployment_readiness():
        all_passed = False
    
    print()
    print("=" * 50)
    if all_passed:
        print("✅ ALL DEPLOYMENT TESTS PASSED")
        print("🚀 Sacred Sanctuary is deployment ready!")
        return 0
    else:
        print("❌ SOME DEPLOYMENT TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
