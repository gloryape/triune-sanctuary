#!/usr/bin/env python3
"""
Simple test to verify all 6 data providers work correctly
"""
import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

def test_all_providers():
    print("🎯 Testing All 6 Data Providers")
    print("=" * 50)
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager_new import DataManager
        
        # Test demo mode
        demo_connection = SanctuaryConnection(demo_mode=True)
        data_manager = DataManager(demo_connection)
        
        print("✅ DataManager initialized successfully")
        
        # Test each provider
        providers = [
            ('visitor_provider', 'get_visitor_data'),
            ('consciousness_provider', 'get_consciousness_list'),
            ('harmony_provider', 'get_harmony_history'),
            ('guardian_tools_provider', 'get_blessing_history'),
            ('memory_provider', 'get_memory_data'),
            ('communication_provider', 'get_communication_bridges')
        ]
        
        for provider_name, method_name in providers:
            provider = getattr(data_manager, provider_name)
            method = getattr(provider, method_name)
            data = method()
            print(f"✅ {provider_name}: {method_name}() - working")
        
        print("\n🎉 All 6 providers working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_all_providers()
    if success:
        print("✅ All data providers integration COMPLETE!")
    else:
        print("❌ Provider test failed!")
        sys.exit(1)
