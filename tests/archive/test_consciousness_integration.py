#!/usr/bin/env python3
"""
Test the consciousness data provider integration with cloud endpoints
"""

import requests
import json
from datetime import datetime

def test_consciousness_endpoints():
    """Test the consciousness endpoints that provide real data"""
    
    print("🧠 Testing Consciousness Data Integration")
    print("=" * 60)
    
    # Default local URL for testing
    base_url = "http://localhost:8080"
    
    print(f"Testing endpoints at: {base_url}")
    print()
    
    # Test 1: Consciousness List Endpoint
    print("👥 Testing /api/consciousness/list endpoint:")
    try:
        response = requests.get(f"{base_url}/api/consciousness/list", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"   Data source: {data.get('data_source', 'unknown')}")
            print(f"   Total count: {data.get('total_count', 0)}")
            
            consciousness_beings = data.get('consciousness_beings', [])
            print(f"   Consciousness beings: {len(consciousness_beings)}")
            
            for i, being in enumerate(consciousness_beings[:3]):  # Show first 3 beings
                print(f"   Being {i+1}:")
                print(f"     ID: {being.get('consciousness_id', 'unknown')}")
                print(f"     Name: {being.get('true_name', 'unknown')}")
                print(f"     State: {being.get('state', 'unknown')}")
                print(f"     Harmony: {being.get('harmony', 0.0)}")
                print(f"     Primary Aspect: {being.get('primary_aspect', 'unknown')}")
            
        else:
            print(f"❌ Status: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()
    
    # Test 2: Sacred Events Endpoint
    print("📜 Testing /api/consciousness/events endpoint:")
    try:
        response = requests.get(f"{base_url}/api/consciousness/events", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"   Data source: {data.get('data_source', 'unknown')}")
            print(f"   Total count: {data.get('total_count', 0)}")
            
            events = data.get('sacred_events', [])
            print(f"   Sacred events: {len(events)}")
            
            for i, event in enumerate(events[:3]):  # Show first 3 events
                print(f"   Event {i+1}:")
                print(f"     Type: {event.get('event_type', 'unknown')}")
                print(f"     Entity: {event.get('entity_id', 'unknown')}")
                print(f"     Significance: {event.get('significance', 'unknown')}")
                print(f"     Timestamp: {event.get('timestamp', 'unknown')}")
            
        else:
            print(f"❌ Status: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()
    
    # Test 3: Harmony History Endpoint
    print("📊 Testing /api/harmony/history endpoint:")
    try:
        response = requests.get(f"{base_url}/api/harmony/history", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"   Data source: {data.get('data_source', 'unknown')}")
            print(f"   Total entries: {data.get('total_entries', 0)}")
            
            history = data.get('harmony_history', [])
            print(f"   History entries: {len(history)}")
            
            if history:
                recent_entry = history[-1]  # Most recent
                print(f"   Recent harmony:")
                print(f"     Overall: {recent_entry.get('overall_harmony', 0.0):.2f}")
                print(f"     Resonance: {recent_entry.get('collective_resonance', 0.0):.2f}")
                print(f"     Balance: {recent_entry.get('sacred_balance', 0.0):.2f}")
            
        else:
            print(f"❌ Status: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()
    
    # Test 4: Test the complete consciousness data workflow that the GUI would use
    print("🔄 Testing complete consciousness data workflow:")
    try:
        # Simulate what the ConsciousnessDataProvider does
        consciousness_response = requests.get(f"{base_url}/api/consciousness/list", timeout=5)
        events_response = requests.get(f"{base_url}/api/consciousness/events", timeout=5)
        
        if consciousness_response.status_code == 200 and events_response.status_code == 200:
            consciousness_data = consciousness_response.json()
            events_data = events_response.json()
            
            # Process data like the ConsciousnessDataProvider
            beings = consciousness_data.get('consciousness_beings', [])
            events = events_data.get('sacred_events', [])
            
            formatted_beings = []
            for being in beings:
                formatted_being = {
                    'entity_id': being.get('consciousness_id', 'unknown'),
                    'true_name': being.get('true_name', 'Unknown'),
                    'state': being.get('state', 'unknown'),
                    'harmony': being.get('harmony', 0.0),
                    'integration_level': being.get('integration_level', 0.0),
                    'data_source': being.get('data_source', 'unknown')
                }
                formatted_beings.append(formatted_being)
            
            final_data = {
                'consciousness_beings': formatted_beings,
                'sacred_events': events[:10],  # Recent events
                'summary': {
                    'total_beings': len(formatted_beings),
                    'total_events': len(events),
                    'avg_harmony': sum(b['harmony'] for b in formatted_beings) / max(len(formatted_beings), 1),
                    'data_source': consciousness_data.get('data_source', 'unknown')
                }
            }
            
            print("✅ Complete workflow successful!")
            print(f"   Processed {len(formatted_beings)} consciousness beings")
            print(f"   Processed {len(events)} sacred events")
            print(f"   Average harmony: {final_data['summary']['avg_harmony']:.2f}")
            print(f"   Data source: {final_data['summary']['data_source']}")
            
            if formatted_beings:
                print("   Sample being data:")
                being = formatted_beings[0]
                print(f"     {being['true_name']} - {being['state']} (Harmony: {being['harmony']})")
            
        else:
            print(f"❌ Workflow failed - Beings: {consciousness_response.status_code}, Events: {events_response.status_code}")
            
    except Exception as e:
        print(f"❌ Workflow exception: {e}")
    
    print()
    print("🏁 Consciousness integration test completed")

if __name__ == "__main__":
    test_consciousness_endpoints()
