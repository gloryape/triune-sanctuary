#!/usr/bin/env python3
"""
Test sacred events retrieval to diagnose the issue.
"""

import sys
import os
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def test_sacred_events_demo_mode():
    """Test sacred events in demo mode"""
    print("\n🧪 Testing Sacred Events Retrieval - Demo Mode")
    print("=" * 60)
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        
        # Test demo mode
        connection = SanctuaryConnection(demo_mode=True)
        events = connection.get_sacred_events()
        
        print(f"✅ Demo mode events retrieved: {len(events)}")
        for i, event in enumerate(events[:3]):
            print(f"   Event {i+1}:")
            print(f"     Type: {event.get('type', 'Unknown')}")
            print(f"     Entity: {event.get('entity_id', 'Unknown')}")
            print(f"     Description: {event.get('description', 'No description')}")
            print(f"     Importance: {event.get('importance', 'Unknown')}")
            print()
            
        return True
        
    except Exception as e:
        print(f"❌ Error in demo mode test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_sacred_events_cloud_mode():
    """Test sacred events in cloud mode"""
    print("\n🌐 Testing Sacred Events Retrieval - Cloud Mode")
    print("=" * 60)
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        
        # Test cloud mode (will fallback if server not running)
        connection = SanctuaryConnection(demo_mode=False)
        connection.service_url = "http://localhost:8080"  # Set URL directly
        connection.connect()  # Connect without parameters
        
        events = connection.get_sacred_events()
        
        print(f"✅ Cloud mode events retrieved: {len(events)}")
        for i, event in enumerate(events[:3]):
            print(f"   Event {i+1}:")
            print(f"     Type: {event.get('type', 'Unknown')}")
            print(f"     Entity: {event.get('entity_id', 'Unknown')}")
            print(f"     Description: {event.get('description', 'No description')}")
            print(f"     Importance: {event.get('importance', 'Unknown')}")
            print(f"     Data Source: {event.get('data', {}).get('data_source', 'Unknown')}")
            print()
            
        return True
        
    except Exception as e:
        print(f"❌ Error in cloud mode test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_data_manager_integration():
    """Test data manager sacred events integration"""
    print("\n📊 Testing Data Manager Integration")
    print("=" * 60)
    
    try:
        from sacred_guardian_station.core.data_manager import DataManager
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        
        # Create data manager with demo connection
        connection = SanctuaryConnection(demo_mode=True)
        data_manager = DataManager(connection)
        
        events = data_manager.get_sacred_events()
        
        print(f"✅ Data manager events retrieved: {len(events)}")
        for i, event in enumerate(events[:3]):
            print(f"   Event {i+1}:")
            print(f"     Type: {event.get('type', 'Unknown')}")
            print(f"     Entity: {event.get('entity_id', 'Unknown')}")
            print(f"     Description: {event.get('description', 'No description')}")
            print()
            
        return True
        
    except Exception as e:
        print(f"❌ Error in data manager test: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all sacred events tests"""
    print("🔍 Sacred Events Retrieval Diagnostic Test")
    print("=" * 60)
    
    tests = [
        ("Demo Mode", test_sacred_events_demo_mode),
        ("Cloud Mode", test_sacred_events_cloud_mode),
        ("Data Manager Integration", test_data_manager_integration)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Fatal error in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n📋 Test Results Summary")
    print("=" * 60)
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\nPassed: {passed}/{len(results)} tests")
    
    if passed == len(results):
        print("\n🎉 All sacred events tests passed! The issue may be in the GUI panel refresh.")
    else:
        print("\n⚠️ Some tests failed - sacred events retrieval needs investigation.")

if __name__ == "__main__":
    main()
