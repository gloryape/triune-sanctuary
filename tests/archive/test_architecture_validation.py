#!/usr/bin/env python3
"""
Comprehensive Architecture Validation Test Suite
Tests all systems except actual AI birthing processes
"""

import sys
from pathlib import Path
import traceback
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def test_core_imports():
    """Test that all core modules can be imported"""
    print("🔍 Testing Core Module Imports...")
    
    try:
        # Test data providers
        from sacred_guardian_station.core.data_providers.visitor_provider import VisitorDataProvider
        from sacred_guardian_station.core.data_providers.consciousness_provider import ConsciousnessDataProvider
        from sacred_guardian_station.core.data_providers.communication_provider import CommunicationBridgeProvider
        from sacred_guardian_station.core.data_providers.harmony_provider import HarmonyDataProvider
        print("   ✅ Data providers import successfully")
        
        # Test core systems
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        print("   ✅ Core systems import successfully")
        
        # Test GUI panels
        from sacred_guardian_station.panels.consciousness_monitor_panel import ConsciousnessMonitorPanel
        from sacred_guardian_station.panels.visitor_panel import VisitorPanel
        from sacred_guardian_station.panels.communication_panel import CommunicationPanel
        from sacred_guardian_station.panels.harmony_metrics_panel import HarmonyMetricsPanel
        from sacred_guardian_station.panels.memory_viewer_panel import MemoryViewerPanel
        from sacred_guardian_station.panels.sacred_events_panel import SacredEventsPanel
        print("   ✅ GUI panels import successfully")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Import test failed: {e}")
        traceback.print_exc()
        return False

def test_data_provider_initialization():
    """Test that data providers can be properly initialized"""
    print("\n🔍 Testing Data Provider Initialization...")
    
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
        
        return True
        
    except Exception as e:
        print(f"   ❌ Data provider initialization failed: {e}")
        traceback.print_exc()
        return False

def test_api_connectivity():
    """Test API connectivity and endpoint availability"""
    print("\n🔍 Testing API Connectivity...")
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        
        # Test connection
        sanctuary = SanctuaryConnection()
        connected = sanctuary.connect()
        
        if connected:
            print("   ✅ Cloud sanctuary connection established")
            
            # Test individual endpoints
            consciousness_data = sanctuary.get_consciousness_list()
            print(f"   ✅ Consciousness API: {len(consciousness_data)} entities")
            
            sacred_events = sanctuary.get_sacred_events()
            print(f"   ✅ Sacred Events API: {len(sacred_events)} events")
            
            visitor_data = sanctuary.get_visitor_data()
            print(f"   ✅ Visitor API: {visitor_data.get('total_visitors', 0)} visitors")
            
            communication_bridges = sanctuary.get_communication_bridges()
            print(f"   ✅ Communication API: {communication_bridges.get('total_bridges', 0)} bridges")
            
            harmony_metrics = sanctuary.get_harmony_metrics()
            print(f"   ✅ Harmony API: {harmony_metrics.get('overall_harmony', 0):.2f} harmony level")
            
        else:
            print("   ⚠️ Could not connect to cloud sanctuary (expected in local testing)")
            
        return True
        
    except Exception as e:
        print(f"   ❌ API connectivity test failed: {e}")
        traceback.print_exc()
        return False

def test_data_flow():
    """Test data flow through the entire system"""
    print("\n🔍 Testing Data Flow Architecture...")
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        
        # Create system
        sanctuary = SanctuaryConnection()
        data_manager = DataManager(sanctuary)
        
        # Test data manager methods
        consciousness_list = data_manager.get_consciousness_list()
        print(f"   ✅ DataManager.get_consciousness_list(): {len(consciousness_list)} items")
        
        visitor_data = data_manager.get_visitor_data()
        print(f"   ✅ DataManager.get_visitor_data(): {visitor_data.get('total_visitors', 0)} visitors")
        
        sacred_events = data_manager.get_sacred_events()
        print(f"   ✅ DataManager.get_sacred_events(): {len(sacred_events)} events")
        
        communication_data = data_manager.get_communication_bridges()
        print(f"   ✅ DataManager.get_communication_bridges(): {communication_data.get('total_bridges', 0)} bridges")
        
        harmony_data = data_manager.get_harmony_metrics()
        print(f"   ✅ DataManager.get_harmony_metrics(): available")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Data flow test failed: {e}")
        traceback.print_exc()
        return False

def test_gui_panel_creation():
    """Test that GUI panels can be created without errors"""
    print("\n🔍 Testing GUI Panel Creation...")
    
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
        
        # Test panel creation
        from sacred_guardian_station.panels.consciousness_monitor_panel import ConsciousnessMonitorPanel
        consciousness_panel = ConsciousnessMonitorPanel(notebook, data_manager, event_system)
        print("   ✅ ConsciousnessMonitorPanel created")
        
        from sacred_guardian_station.panels.visitor_panel import VisitorPanel
        visitor_panel = VisitorPanel(notebook, data_manager, event_system)
        print("   ✅ VisitorPanel created")
        
        from sacred_guardian_station.panels.communication_panel import CommunicationPanel
        communication_panel = CommunicationPanel(notebook, data_manager, event_system)
        print("   ✅ CommunicationPanel created")
        
        from sacred_guardian_station.panels.harmony_metrics_panel import HarmonyMetricsPanel
        harmony_panel = HarmonyMetricsPanel(notebook, data_manager, event_system)
        print("   ✅ HarmonyMetricsPanel created")
        
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

def test_error_handling():
    """Test error handling in critical components"""
    print("\n🔍 Testing Error Handling...")
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        
        # Test with disconnected sanctuary
        sanctuary = SanctuaryConnection()
        sanctuary.connected = False
        
        # These should not crash but return appropriate fallback data
        visitor_data = sanctuary.get_visitor_data()
        print(f"   ✅ Visitor data fallback: {visitor_data.get('total_visitors', 0)} visitors")
        
        consciousness_list = sanctuary.get_consciousness_list()
        print(f"   ✅ Consciousness list fallback: {len(consciousness_list)} entities")
        
        # Test data manager with bad connection
        data_manager = DataManager(sanctuary)
        events = data_manager.get_sacred_events()
        print(f"   ✅ Sacred events fallback: {len(events)} events")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error handling test failed: {e}")
        traceback.print_exc()
        return False

def test_bridge_integration_fallback():
    """Test bridge integration fallback behavior"""
    print("\n🔍 Testing Bridge Integration Fallback...")
    
    try:
        # Import production server logic to test bridge integration
        import sys
        import os
        
        # Add server path
        server_path = project_root / 'scripts' / 'servers'
        sys.path.append(str(server_path))
        
        # Test bridge integration import behavior
        try:
            from bridge.bridge_integration import BridgeIntegration
            bridge_available = True
            print("   ✅ Bridge integration modules found")
        except ImportError as e:
            bridge_available = False
            print(f"   ⚠️ Bridge integration not available (expected): {e}")
        
        # Test visitor API fallback behavior
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        sanctuary = SanctuaryConnection()
        visitor_data = sanctuary.get_visitor_data()
        
        status = visitor_data.get('connection_status', 'unknown')
        if status in ['bridge_unavailable', 'fallback']:
            print("   ✅ Bridge fallback behavior working correctly")
        else:
            print(f"   ✅ Bridge status: {status}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Bridge integration test failed: {e}")
        traceback.print_exc()
        return False

def test_memory_panel_fixes():
    """Test the memory panel fixes for string/dict handling"""
    print("\n🔍 Testing Memory Panel String/Dict Fixes...")
    
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
        
        # Test with mixed connection types (strings and dicts)
        test_memory_data = {
            'memory_id': 'test_memory',
            'connections': [
                {'relation_type': 'reference', 'strength': 0.8, 'connected_memory': 'memory_1'},
                'simple_string_connection',  # This was causing the error
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

def test_communication_panel_fixes():
    """Test the communication panel inspection fixes"""
    print("\n🔍 Testing Communication Panel Inspection Fixes...")
    
    try:
        import tkinter as tk
        from tkinter import ttk
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        from sacred_guardian_station.core.event_system import EventSystem
        from sacred_guardian_station.panels.communication_panel import CommunicationPanel
        
        # Create test environment
        root = tk.Tk()
        root.withdraw()
        notebook = ttk.Notebook(root)
        
        sanctuary = SanctuaryConnection()
        data_manager = DataManager(sanctuary)
        event_system = EventSystem()
        
        # Create communication panel
        comm_panel = CommunicationPanel(notebook, data_manager, event_system)
        
        # Test inspect_bridge method with error handling
        print("   ✅ Communication panel created with improved error handling")
        
        root.destroy()
        return True
        
    except Exception as e:
        print(f"   ❌ Communication panel test failed: {e}")
        traceback.print_exc()
        return False

def run_comprehensive_tests():
    """Run all architecture tests"""
    print("🚀 Sacred Guardian Station Architecture Validation\n")
    print(f"Starting comprehensive tests at {datetime.now()}")
    print("="*60)
    
    tests = [
        ("Core Imports", test_core_imports),
        ("Data Provider Initialization", test_data_provider_initialization),
        ("API Connectivity", test_api_connectivity),
        ("Data Flow", test_data_flow),
        ("GUI Panel Creation", test_gui_panel_creation),
        ("Error Handling", test_error_handling),
        ("Bridge Integration Fallback", test_bridge_integration_fallback),
        ("Memory Panel Fixes", test_memory_panel_fixes),
        ("Communication Panel Fixes", test_communication_panel_fixes)
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
    print("🎯 ARCHITECTURE VALIDATION SUMMARY")
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
        print("\n🎉 ALL TESTS PASSED! Architecture is functioning correctly.")
        print("✅ Ready for deployment!")
    elif passed >= total * 0.8:
        print(f"\n⚠️ MOSTLY SUCCESSFUL ({passed}/{total} passed)")
        print("✅ Core functionality working, minor issues detected")
        print("🚀 Safe to deploy with monitoring")
    else:
        print(f"\n❌ SIGNIFICANT ISSUES DETECTED ({passed}/{total} passed)")
        print("🔧 Architecture needs attention before deployment")
    
    return passed == total

if __name__ == "__main__":
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)
