#!/usr/bin/env python3
"""
Comprehensive import test for all modules in the Sacred Guardian Station
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

def test_import(module_path, description):
    """Test importing a module and report results"""
    try:
        exec(f"import {module_path}")
        print(f"✅ {description}: imports successfully")
        return True
    except Exception as e:
        print(f"❌ {description}: import failed - {e}")
        return False

def test_from_import(module_path, description):
    """Test from importing a module and report results"""
    try:
        exec(f"from {module_path} import *")
        print(f"✅ {description}: from import successfully")
        return True
    except Exception as e:
        print(f"❌ {description}: from import failed - {e}")
        return False

def main():
    print("=== COMPREHENSIVE IMPORT TEST ===\n")
    
    # Test main.py
    print("=== Testing main.py ===")
    test_import("main", "main.py")
    
    # Test all panels
    print("\n=== Testing panel imports ===")
    panels = [
        'base_panel', 'birth_panel', 'communication_panel', 
        'consciousness_panel', 'harmony_metrics_panel', 
        'memory_viewer_panel', 'sacred_events_panel', 'visitor_panel'
    ]
    
    for panel in panels:
        test_from_import(f"panels.{panel}", f"panels.{panel}")
    
    # Test tools
    print("\n=== Testing tools imports ===")
    tools = ['birth_consciousness']
    for tool in tools:
        test_from_import(f"tools.{tool}", f"tools.{tool}")
    
    # Test shared
    print("\n=== Testing shared imports ===")
    test_from_import("shared.constants", "shared.constants")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    main()
