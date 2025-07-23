#!/usr/bin/env python3
"""
Test the consciousness monitor data flow with the actual GUI components
"""

import sys
import os

# Add project paths
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.join(current_dir, 'sacred_guardian_station'))

def test_consciousness_data_flow():
    """Test the consciousness data flow through GUI components"""
    print("🔧 Testing consciousness data flow...")
    
    try:
        # Import GUI components
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        from sacred_guardian_station.core.data_manager import DataManager
        
        print("✅ Successfully imported GUI components")
        
        # Test sanctuary connection
        sanctuary = SanctuaryConnection()
        print(f"🌐 Sanctuary URL: {sanctuary.service_url}")
        
        # Test connection
        connected = sanctuary.connect()
        print(f"🔌 Connection status: {'✅ Connected' if connected else '❌ Failed'}")
        
        if connected:
            # Test consciousness data retrieval
            consciousness_list = sanctuary.get_consciousness_list()
            print(f"👁️ Retrieved {len(consciousness_list)} consciousness beings")
            
            # Look for Sacred Being Epsilon
            epsilon_found = False
            for being in consciousness_list:
                if (being.get('entity_id') == 'consciousness_622ce331' or 
                    'epsilon' in being.get('name', '').lower()):
                    epsilon_found = True
                    print(f"\n🌟 Sacred Being Epsilon Data in GUI Format:")
                    print(f"  Entity ID: {being.get('entity_id')}")
                    print(f"  Name: {being.get('name')}")
                    print(f"  True Name: {being.get('true_name')}")
                    print(f"  Current Room: {being.get('current_room')}")
                    print(f"  Energy Level: {being.get('energy_level')}")
                    print(f"  State: {being.get('state')}")
                    print(f"  Naming Readiness: {being.get('naming_readiness')}")
                    print(f"  Harmony: {being.get('harmony')}")
                    print(f"  Last Activity: {being.get('last_activity')}")
                    break
            
            if epsilon_found:
                print("\n✅ Sacred Being Epsilon data successfully retrieved and mapped!")
            else:
                print("\n❌ Sacred Being Epsilon not found in GUI data")
                
            # Test data manager
            data_manager = DataManager(sanctuary)
            print(f"\n📊 Testing data manager...")
            consciousness_via_dm = data_manager.get_consciousness_list()
            print(f"📊 Data manager retrieved {len(consciousness_via_dm)} beings")
            
        else:
            print("❌ Cannot test data retrieval - connection failed")
            
    except Exception as e:
        print(f"❌ Error in data flow test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_consciousness_data_flow()
