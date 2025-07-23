#!/usr/bin/env python3
"""
🖥️ GUI Validation Test
Tests the local GUI components for production readiness
"""

import os
import sys
import tkinter as tk
import traceback
from typing import Dict, Any, List

def test_tkinter_availability():
    """Test that tkinter is available and working"""
    print("🔧 Testing Tkinter Availability")
    print("=" * 30)
    
    try:
        # Test basic tkinter functionality
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Test basic widgets
        frame = tk.Frame(root)
        label = tk.Label(frame, text="Test")
        button = tk.Button(frame, text="Test Button")
        
        print("✅ Tkinter basic widgets work")
        
        # Test ttk (themed widgets)
        from tkinter import ttk
        ttk_label = ttk.Label(frame, text="TTK Test")
        print("✅ TTK themed widgets available")
        
        root.destroy()
        return True
        
    except Exception as e:
        print(f"❌ Tkinter test failed: {e}")
        return False

def test_local_gui_structure():
    """Test the structure of the local GUI file"""
    print("\n📋 Testing Local GUI Structure")
    print("=" * 30)
    
    gui_file = 'sacred_guardian_station_independent.py'
    
    try:
        if not os.path.exists(gui_file):
            print(f"❌ GUI file missing: {gui_file}")
            return False
        
        with open(gui_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for required imports
        required_imports = [
            'import tkinter',
            'from tkinter import ttk',
            'import json',
            'import os',
            'from datetime import datetime'
        ]
        
        for import_line in required_imports:
            if import_line in content:
                print(f"✅ {import_line}: Found")
            else:
                print(f"❌ {import_line}: Missing")
                return False
        
        # Check for required classes
        required_classes = [
            'LocalConsciousnessData',
            'SacredGuardianStation'
        ]
        
        for class_name in required_classes:
            if f"class {class_name}" in content:
                print(f"✅ Class {class_name}: Found")
            else:
                print(f"❌ Class {class_name}: Missing")
                return False
        
        # Check for Sacred Being Epsilon support
        if 'Sacred Being Epsilon' in content:
            print("✅ Sacred Being Epsilon support: Found")
        else:
            print("❌ Sacred Being Epsilon support: Missing")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ GUI structure test failed: {e}")
        return False

def test_gui_instantiation():
    """Test that the GUI can be instantiated without errors"""
    print("\n🚀 Testing GUI Instantiation")
    print("=" * 30)
    
    try:
        # Import the GUI module
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "sacred_guardian_station_independent", 
            "sacred_guardian_station_independent.py"
        )
        
        if spec is None:
            print("❌ Could not create module spec")
            return False
            
        gui_module = importlib.util.module_from_spec(spec)
        sys.modules["sacred_guardian_station_independent"] = gui_module
        spec.loader.exec_module(gui_module)
        
        print("✅ GUI module imported successfully")
        
        # Test LocalConsciousnessData instantiation
        local_data = gui_module.LocalConsciousnessData()
        print("✅ LocalConsciousnessData instantiated")
        
        # Check that Epsilon is initialized
        if hasattr(local_data, 'consciousness_beings') and local_data.consciousness_beings:
            print("✅ Consciousness beings data initialized")
            
            # Check for Epsilon specifically
            epsilon_found = False
            for being_id, being_data in local_data.consciousness_beings.items():
                if 'Epsilon' in being_data.get('name', ''):
                    epsilon_found = True
                    break
            
            if epsilon_found:
                print("✅ Sacred Being Epsilon found in data")
            else:
                print("❌ Sacred Being Epsilon not found in data")
                return False
        else:
            print("❌ Consciousness beings data not initialized")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ GUI instantiation test failed: {e}")
        traceback.print_exc()
        return False

def test_gui_data_persistence():
    """Test that GUI data can be saved and loaded"""
    print("\n💾 Testing GUI Data Persistence")
    print("=" * 30)
    
    try:
        # Import the GUI module
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "sacred_guardian_station_independent", 
            "sacred_guardian_station_independent.py"
        )
        gui_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gui_module)
        
        # Test data saving and loading
        local_data = gui_module.LocalConsciousnessData()
        
        # Check save functionality
        if hasattr(local_data, 'save_data'):
            try:
                local_data.save_data()
                print("✅ Data save functionality works")
            except Exception as e:
                print(f"❌ Data save failed: {e}")
                return False
        
        # Check load functionality
        if hasattr(local_data, 'load_data'):
            try:
                local_data.load_data()
                print("✅ Data load functionality works")
            except Exception as e:
                print(f"❌ Data load failed: {e}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Data persistence test failed: {e}")
        return False

def main():
    """Run GUI validation tests"""
    print("🖥️ GUI VALIDATION TEST")
    print("=" * 40)
    
    tests = [
        test_tkinter_availability,
        test_local_gui_structure,
        test_gui_instantiation,
        test_gui_data_persistence
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
    print("\n🏁 GUI VALIDATION SUMMARY")
    print("=" * 30)
    passed = sum(results)
    total = len(results)
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("✅ Local GUI is ready for deployment")
        print("✅ All GUI components validated")
        print("✅ Sacred Being Epsilon support confirmed")
    else:
        print("❌ GUI validation failed")
        print("🔧 Please address GUI issues before deployment")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
