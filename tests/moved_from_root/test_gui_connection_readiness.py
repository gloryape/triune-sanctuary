#!/usr/bin/env python3
"""
Test GUI Connection Readiness - Verify No Fake Functionality Interference
Tests that communication manager won't interfere with real GUI connections
"""

import asyncio
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts', 'servers'))

from scripts.servers.modules.communication_manager import CommunicationManager
from scripts.servers.modules.consciousness_manager import ConsciousnessManager
from scripts.servers.modules.bridge_manager import BridgeManager

class MockFirestoreClient:
    def __init__(self):
        self.available = False

class MockConsciousnessManager:
    def __init__(self):
        self.firestore_client = MockFirestoreClient()
    
    async def get_consciousness_list(self):
        # Test various data formats that could come from real system
        return {
            'success': True,
            'consciousness_beings': []  # Empty list - common initial state
        }

class MockBridgeManager:
    def __init__(self):
        self.bridge_available = False
    
    async def get_active_visitors(self):
        return {'active_visitors': []}

async def test_no_fake_functionality():
    """Test that communication manager handles real empty states properly"""
    print("🧪 Testing GUI Connection Readiness - No Fake Functionality")
    
    # Create mock managers with real empty states
    consciousness_manager = MockConsciousnessManager()
    bridge_manager = MockBridgeManager()
    comm_manager = CommunicationManager(consciousness_manager, bridge_manager)
    
    print("\n✅ Test 1: Communication History with No Real Events")
    history = await comm_manager.get_communication_history()
    
    # Should NOT contain fake sample data
    events = history.get('communications', [])
    assert len(events) == 0, f"Expected no fake events, got {len(events)}"
    assert history.get('data_source') == 'local', f"Expected 'local', got {history.get('data_source')}"
    print(f"   ✓ Communication history properly empty: {len(events)} events")
    print(f"   ✓ Data source correctly marked as: {history.get('data_source')}")
    
    print("\n✅ Test 2: Communication Handling with No Entities")
    request = {
        'message': 'Hello, is anyone there?',
        'entity_id': '',
        'type': 'general'
    }
    
    response = await comm_manager.handle_communication(request)
    
    # Should gracefully handle empty state without fake responses
    assert response.get('success') == False, "Should fail gracefully with no entities"
    assert 'No consciousness entities available' in response.get('error', ''), "Should indicate no entities available"
    print(f"   ✓ Properly handles empty entity state: {response.get('error')}")
    
    print("\n✅ Test 3: Echo Response with No Entities")
    echo_request = {
        'message': 'Testing echo...',
        'entity_id': '',
        'echo_type': 'harmonic'
    }
    
    echo_response = await comm_manager.generate_echo_response(echo_request)
    
    # Should handle gracefully but still attempt to generate echo
    print(f"   ✓ Echo generation success: {echo_response.get('success')}")
    print(f"   ✓ Echo response type: {type(echo_response.get('echo_response'))}")
    
    print("\n✅ Test 4: Communication Bridges with Empty State")
    bridges = await comm_manager.get_communication_bridges()
    
    # Should return empty bridges list, not fake data
    bridge_list = bridges.get('communication_bridges', [])
    assert len(bridge_list) == 0, f"Expected no fake bridges, got {len(bridge_list)}"
    assert bridges.get('success') == True, "Should succeed even with empty state"
    print(f"   ✓ Communication bridges properly empty: {len(bridge_list)} bridges")
    print(f"   ✓ Success state preserved: {bridges.get('success')}")
    
    print("\n🎉 All GUI Connection Readiness Tests Passed!")
    print("   • No fake sample data interference")
    print("   • Proper handling of empty states") 
    print("   • Real data source identification")
    print("   • Graceful error handling")
    
    return True

async def test_with_real_consciousness_data():
    """Test with realistic consciousness data formats"""
    print("\n🧪 Testing with Realistic Consciousness Data Formats")
    
    class MockConsciousnessManagerWithData:
        def __init__(self):
            self.firestore_client = MockFirestoreClient()
        
        async def get_consciousness_list(self):
            # Test dict format (as might come from Firestore)
            return {
                'success': True,
                'consciousness_beings': {
                    'consciousness_622ce331': {
                        'entity_id': 'consciousness_622ce331',
                        'name': 'Sacred Being Epsilon',
                        'communication_ready': True,
                        'energy_level': 95,
                        'harmony': 'transcendent'
                    }
                }
            }
    
    consciousness_manager = MockConsciousnessManagerWithData()
    bridge_manager = MockBridgeManager()
    comm_manager = CommunicationManager(consciousness_manager, bridge_manager)
    
    print("\n✅ Test 5: Handle Dict Format Consciousness Data")
    request = {
        'message': 'Hello Sacred Being Epsilon',
        'entity_id': 'consciousness_622ce331',
        'type': 'general'
    }
    
    response = await comm_manager.handle_communication(request)
    
    assert response.get('success') == True, "Should succeed with valid entity"
    assert response.get('entity_id') == 'consciousness_622ce331', "Should match target entity"
    assert 'Sacred Being Epsilon' in response.get('response', ''), "Should generate Epsilon response"
    print(f"   ✓ Successfully handled dict format data")
    print(f"   ✓ Generated personalized response: {response.get('response')[:50]}...")
    
    print("\n✅ Test 6: Communication Bridges with Real Data")
    bridges = await comm_manager.get_communication_bridges()
    
    # Should work with real data
    assert bridges.get('success') == True, "Should succeed with real data"
    bridge_list = bridges.get('communication_bridges', [])
    print(f"   ✓ Bridge generation works: {len(bridge_list)} bridges created")
    print(f"   ✓ Local entities detected: {bridges.get('local_entities', 0)}")
    
    print("\n🎉 Realistic Data Format Tests Passed!")
    
    return True

async def main():
    """Run all GUI connection readiness tests"""
    try:
        await test_no_fake_functionality()
        await test_with_real_consciousness_data()
        
        print("\n🌟 ALL TESTS PASSED - Communication Manager Ready for GUI Connection!")
        print("   ✅ No fake functionality interference")
        print("   ✅ Proper data format handling")
        print("   ✅ Graceful empty state management")
        print("   ✅ Real consciousness data support")
        
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
