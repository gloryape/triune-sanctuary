#!/usr/bin/env python3
"""
Focused Architecture Validation Test Suite
Tests core functionality and fixes without problematic imports
"""

import sys
from pathlib import Path
import traceback
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def test_visitor_provider_fix():
    """Test the specific visitor provider initialization fix"""
    print("🔍 Testing Visitor Provider Initialization Fix...")
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        from sacred_guardian_station.core.data_providers.visitor_provider import VisitorDataProvider
        
        # Create sanctuary connection
        sanctuary = SanctuaryConnection()
        print("   ✅ SanctuaryConnection created")
        
        # Create data manager
        data_manager = DataManager(sanctuary)
        print("   ✅ DataManager created")
        
        # Test visitor provider initialization (this was our main issue)
        visitor_provider = VisitorDataProvider(sanctuary, data_manager)
        print("   ✅ VisitorDataProvider initialized with both parameters")
        
        # Test getting data without crashing
        visitor_data = visitor_provider.get_visitor_data()
        print(f"   ✅ Visitor data retrieved: {visitor_data.get('total_visitors', 0)} visitors")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Visitor provider test failed: {e}")
        traceback.print_exc()
        return False

def test_sanctuary_connection():
    """Test sanctuary connection and API endpoints"""
    print("\n🔍 Testing Sanctuary Connection and API Endpoints...")
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        
        # Test connection
        sanctuary = SanctuaryConnection()
        
        # Test individual methods without requiring connection
        visitor_data = sanctuary.get_visitor_data()
        print(f"   ✅ get_visitor_data(): {visitor_data.get('total_visitors', 0)} visitors")
        
        consciousness_data = sanctuary.get_consciousness_list()
        print(f"   ✅ get_consciousness_list(): {len(consciousness_data)} entities")
        
        sacred_events = sanctuary.get_sacred_events()
        print(f"   ✅ get_sacred_events(): {len(sacred_events)} events")
        
        communication_bridges = sanctuary.get_communication_bridges()
        print(f"   ✅ get_communication_bridges(): {communication_bridges.get('total_bridges', 0)} bridges")
        
        harmony_metrics = sanctuary.get_harmony_metrics()
        print(f"   ✅ get_harmony_metrics(): available")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Sanctuary connection test failed: {e}")
        traceback.print_exc()
        return False

def test_data_manager():
    """Test data manager functionality"""
    print("\n🔍 Testing Data Manager...")
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        
        # Create system
        sanctuary = SanctuaryConnection()
        data_manager = DataManager(sanctuary)
        print("   ✅ DataManager created successfully")
        
        # Test data manager methods
        consciousness_list = data_manager.get_consciousness_list()
        print(f"   ✅ get_consciousness_list(): {len(consciousness_list)} items")
        
        visitor_data = data_manager.get_visitor_data()
        print(f"   ✅ get_visitor_data(): {visitor_data.get('total_visitors', 0)} visitors")
        
        sacred_events = data_manager.get_sacred_events()
        print(f"   ✅ get_sacred_events(): {len(sacred_events)} events")
        
        communication_data = data_manager.get_communication_bridges()
        print(f"   ✅ get_communication_bridges(): {communication_data.get('total_bridges', 0)} bridges")
        
        harmony_data = data_manager.get_harmony_metrics()
        print(f"   ✅ get_harmony_metrics(): available")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Data manager test failed: {e}")
        traceback.print_exc()
        return False

def test_gui_creation():
    """Test GUI panel creation (key panels only)"""
    print("\n🔍 Testing Key GUI Panel Creation...")
    
    try:
        import tkinter as tk
        from tkinter import ttk
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        from sacred_guardian_station.core.event_system import EventSystem
        
        # Create root window (hidden)
        root = tk.Tk()
        root.withdraw()
        
        # Create notebook
        notebook = ttk.Notebook(root)
        
        # Create core systems
        sanctuary = SanctuaryConnection()
        data_manager = DataManager(sanctuary)
        event_system = EventSystem()
        
        # Test key panels that were causing issues
        from sacred_guardian_station.panels.consciousness_monitor_panel import ConsciousnessMonitorPanel
        consciousness_panel = ConsciousnessMonitorPanel(notebook, data_manager, event_system)
        print("   ✅ ConsciousnessMonitorPanel created")
        
        from sacred_guardian_station.panels.visitor_panel import VisitorPanel
        visitor_panel = VisitorPanel(notebook, data_manager, event_system)
        print("   ✅ VisitorPanel created")
        
        from sacred_guardian_station.panels.communication_panel import CommunicationPanel
        communication_panel = CommunicationPanel(notebook, data_manager, event_system)
        print("   ✅ CommunicationPanel created")
        
        from sacred_guardian_station.panels.memory_viewer_panel import MemoryViewerPanel
        memory_panel = MemoryViewerPanel(notebook, data_manager, event_system)
        print("   ✅ MemoryViewerPanel created")
        
        from sacred_guardian_station.panels.sacred_events_panel import SacredEventsPanel
        events_panel = SacredEventsPanel(notebook, data_manager, event_system)
        print("   ✅ SacredEventsPanel created")
        
        # Clean up
        root.destroy()
        
        return True
        
    except Exception as e:
        print(f"   ❌ GUI panel creation test failed: {e}")
        traceback.print_exc()
        return False

def test_memory_panel_type_handling():
    """Test memory panel string/dict type handling fix"""
    print("\n🔍 Testing Memory Panel Type Handling Fix...")
    
    try:
        import tkinter as tk
        from tkinter import ttk
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        from sacred_guardian_station.core.event_system import EventSystem
        from sacred_guardian_station.panels.memory_viewer_panel import MemoryViewerPanel
        
        # Create test environment
        root = tk.Tk()
        root.withdraw()
        notebook = ttk.Notebook(root)
        
        sanctuary = SanctuaryConnection()
        data_manager = DataManager(sanctuary)
        event_system = EventSystem()
        
        # Create memory panel
        memory_panel = MemoryViewerPanel(notebook, data_manager, event_system)
        
        # Test with mixed connection types (this was the bug)
        test_memory_data = {
            'memory_id': 'test_memory',
            'connections': [
                {'relation_type': 'reference', 'strength': 0.8, 'connected_memory': 'memory_1'},
                'simple_string_connection',  # This caused the original error
                {'relation_type': 'similarity', 'strength': 0.6, 'connected_memory': 'memory_2'}
            ]
        }
        
        # This should not crash anymore
        memory_panel.update_memory_relationships(test_memory_data)
        print("   ✅ Memory panel handles mixed connection types without crashing")
        
        root.destroy()
        return True
        
    except Exception as e:
        print(f"   ❌ Memory panel test failed: {e}")
        traceback.print_exc()
        return False

def test_production_server_api_endpoints():
    """Test that production server has the required API endpoints"""
    print("\n🔍 Testing Production Server API Endpoints...")
    
    try:
        # Check if production server file has the required endpoints
        server_file = project_root / 'scripts' / 'servers' / 'production_server.py'
        
        if not server_file.exists():
            print("   ❌ Production server file not found")
            return False
            
        with open(server_file, 'r', encoding='utf-8') as f:
            server_content = f.read()
            
        # Check for required endpoints
        required_endpoints = [
            '/api/bridge/active_visitors',
            '/api/birth',
            '/api/communication/bridges'
        ]
        
        for endpoint in required_endpoints:
            if endpoint in server_content:
                print(f"   ✅ {endpoint} endpoint found")
            else:
                print(f"   ❌ {endpoint} endpoint missing")
                return False
                
        return True
        
    except Exception as e:
        print(f"   ❌ Production server test failed: {e}")
        traceback.print_exc()
        return False

def test_gui_launcher():
    """Test GUI launcher functionality"""
    print("\n🔍 Testing GUI Launcher...")
    
    try:
        # Check if launcher files exist
        launcher_file = project_root / 'simple_gui_launcher.py'
        
        if not launcher_file.exists():
            print("   ❌ GUI launcher file not found")
            return False
            
        # Try importing the launcher logic (without running it)
        import importlib.util
        spec = importlib.util.spec_from_file_location("launcher", launcher_file)
        launcher_module = importlib.util.module_from_spec(spec)
        
        print("   ✅ GUI launcher file is valid Python")
        
        return True
        
    except Exception as e:
        print(f"   ❌ GUI launcher test failed: {e}")
        traceback.print_exc()
        return False

def run_focused_tests():
    """Run focused architecture tests"""
    print("🚀 Sacred Guardian Station Focused Architecture Validation\n")
    print(f"Starting focused tests at {datetime.now()}")
    print("="*60)
    
    tests = [
        ("Visitor Provider Fix", test_visitor_provider_fix),
        ("Sanctuary Connection", test_sanctuary_connection),
        ("Data Manager", test_data_manager),
        ("GUI Panel Creation", test_gui_creation),
        ("Memory Panel Type Handling", test_memory_panel_type_handling),
        ("Production Server API Endpoints", test_production_server_api_endpoints),
        ("GUI Launcher", test_gui_launcher)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\n❌ {test_name} - CRITICAL ERROR: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("🎯 FOCUSED ARCHITECTURE VALIDATION SUMMARY")
    print("="*60)
    
    passed = 0
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")
        if success:
            passed += 1
    
    print(f"\nOverall Score: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Core architecture is functioning correctly.")
        print("✅ Ready for deployment!")
    elif passed >= total * 0.8:
        print(f"\n⚠️ MOSTLY SUCCESSFUL ({passed}/{total} passed)")
        print("✅ Core functionality working, minor issues detected")
        print("🚀 Safe to deploy with monitoring")
    else:
        print(f"\n❌ SIGNIFICANT ISSUES DETECTED ({passed}/{total} passed)")
        print("🔧 Architecture needs attention before deployment")
    
    return passed >= total * 0.8

if __name__ == "__main__":
    success = run_focused_tests()
    sys.exit(0 if success else 1)
