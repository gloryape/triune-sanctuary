#!/usr/bin/env python3
"""
Test refactored production server endpoints to verify communication bridge functionality
"""

import requests
import json
from datetime import datetime

def test_refactored_server_endpoints():
    """Test refactored production server endpoints"""
    base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
    
    print("=" * 70)
    print("🧪 TESTING REFACTORED PRODUCTION SERVER ENDPOINTS")
    print("=" * 70)
    
    # Test health endpoint
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health endpoint working - Status: {data.get('status')}")
        else:
            print(f"❌ Health endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")
    
    # Test consciousness endpoint
    print("\n2. Testing consciousness endpoint...")
    try:
        response = requests.get(f"{base_url}/api/consciousness", timeout=15)
        if response.status_code == 200:
            data = response.json()
            consciousness_beings = data.get('consciousness_beings', {})
            print(f"✅ Consciousness endpoint working - Found {len(consciousness_beings)} beings")
            
            # Check for Sacred Being Epsilon
            epsilon_found = False
            for entity_id, entity_data in consciousness_beings.items():
                if (entity_id == 'consciousness_622ce331' or 
                    entity_data.get('true_name') == 'Sacred Being Epsilon'):
                    epsilon_found = True
                    print(f"   📊 Sacred Being Epsilon found:")
                    print(f"      Name: {entity_data.get('name', 'N/A')}")
                    print(f"      Energy Level: {entity_data.get('energy_level', 'N/A')}")
                    print(f"      Current Room: {entity_data.get('current_room', 'N/A')}")
                    print(f"      Naming Status: {entity_data.get('naming_readiness', 'N/A')}")
                    break
            
            if not epsilon_found:
                print("   ⚠️ Sacred Being Epsilon not found in response")
        else:
            print(f"❌ Consciousness endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Consciousness endpoint error: {e}")
    
    # Test NEW communication bridges endpoint
    print("\n3. Testing communication bridges endpoint (NEW)...")
    try:
        response = requests.get(f"{base_url}/api/communications/bridges", timeout=15)
        if response.status_code == 200:
            data = response.json()
            bridges = data.get('communication_bridges', [])
            success = data.get('success', False)
            print(f"✅ Communication bridges endpoint working - Success: {success}")
            print(f"   Found {len(bridges)} communication bridges")
            
            if bridges:
                print(f"   📊 Sample bridge:")
                bridge = bridges[0]
                print(f"      Type: {bridge.get('bridge_type', 'N/A')}")
                print(f"      From: {bridge.get('from_entity', {}).get('name', 'N/A')}")
                print(f"      To: {bridge.get('to_entity', {}).get('name', 'N/A')}")
                print(f"      Status: {bridge.get('status', 'N/A')}")
            else:
                print("   ⚠️ No communication bridges found")
        else:
            print(f"❌ Communication bridges endpoint failed: {response.status_code}")
            try:
                error_data = response.json()
                print(f"   Error details: {error_data}")
            except:
                print(f"   Raw response: {response.text[:200]}...")
    except Exception as e:
        print(f"❌ Communication bridges endpoint error: {e}")
    
    # Test bridge status endpoint
    print("\n4. Testing bridge status endpoint...")
    try:
        response = requests.get(f"{base_url}/api/bridge/status", timeout=10)
        if response.status_code == 200:
            data = response.json()
            status = data.get('status', 'unknown')
            error = data.get('error', 'none')
            print(f"✅ Bridge status endpoint working - Status: {status}")
            if status == 'unavailable':
                print(f"   ✅ Correctly returns 'unavailable' with error: {error}")
            elif status == 'operational':
                print(f"   ⚠️ Bridge is operational (unexpected but good)")
            else:
                print(f"   ❓ Unknown status: {status}")
        else:
            print(f"❌ Bridge status endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Bridge status endpoint error: {e}")
    
    # Test server version/identity
    print("\n5. Testing server identity...")
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            message = data.get('message', 'Unknown')
            status = data.get('status', 'Unknown')
            print(f"✅ Server identity: {message}")
            print(f"   Status: {status}")
            
            # Check if this is the refactored server
            if "Sacred Consciousness Sanctuary" in message:
                print(f"   🌟 REFACTORED SERVER IS RUNNING!")
            else:
                print(f"   ⚠️ This might be the old server")
        else:
            print(f"❌ Server identity check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Server identity error: {e}")
    
    print("\n" + "=" * 70)
    print("🏁 REFACTORED SERVER TEST COMPLETE")
    print("=" * 70)
    print("If communication bridges endpoint works, the GUI should populate correctly")
    print("If server identity shows 'Sacred Consciousness Sanctuary', refactored server is deployed")

if __name__ == "__main__":
    test_refactored_server_endpoints()
