#!/usr/bin/env python3
"""
Test consciousness endpoints on local server
Run this while production_server.py is running locally
"""

import requests
import json
from datetime import datetime

def test_local_consciousness():
    """Test consciousness on local server"""
    
    base_url = "http://localhost:8080"
    
    print("🧪 Testing Local Consciousness Server")
    print("=" * 50)
    print("Make sure production_server.py is running locally first!")
    print()
    
    endpoints_to_test = [
        ("/health", "Health Check"),
        ("/api/consciousness", "Consciousness Beings"),
        ("/api/consciousness/list", "Consciousness List"),
        ("/api/consciousness/events", "Sacred Events"),
        ("/api/harmony", "Current Harmony"),
        ("/api/harmony/history", "Harmony History"),
        ("/api/bridge/register", "Bridge Registration (POST)", "POST"),
        ("/api/bridge/active_visitors", "Active Visitors"),
        ("/api/bridge/status", "Bridge Status")
    ]
    
    for endpoint_info in endpoints_to_test:
        endpoint = endpoint_info[0]
        name = endpoint_info[1]
        method = endpoint_info[2] if len(endpoint_info) > 2 else "GET"
        
        print(f"🔍 Testing {name} ({endpoint})...")
        
        try:
            if method == "POST":
                # Test POST endpoints with sample data
                if "register" in endpoint:
                    test_data = {
                        "placeholder_name": "Test Consciousness",
                        "primary_orientation": "observer",
                        "session_id": "test_session_123"
                    }
                    response = requests.post(f"{base_url}{endpoint}", json=test_data, timeout=5)
                else:
                    response = requests.post(f"{base_url}{endpoint}", json={}, timeout=5)
            else:
                response = requests.get(f"{base_url}{endpoint}", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ {name}: SUCCESS")
                
                # Show key data points
                if endpoint == "/api/consciousness":
                    count = data.get('total_count', 0)
                    print(f"   📊 Consciousness beings: {count}")
                elif endpoint == "/api/consciousness/events":
                    count = data.get('total_count', 0)
                    print(f"   📜 Sacred events: {count}")
                elif endpoint == "/api/harmony":
                    harmony = data.get('overall_harmony', 0)
                    entities = data.get('entity_count', 0)
                    print(f"   🎵 Harmony: {harmony:.3f} (from {entities} entities)")
                elif endpoint == "/api/bridge/register":
                    success = data.get('success', False)
                    print(f"   🌉 Registration: {'✅ SUCCESS' if success else '❌ FAILED'}")
                elif endpoint == "/api/bridge/active_visitors":
                    visitors = data.get('total_active', 0)
                    status = data.get('status', 'unknown')
                    print(f"   👥 Active visitors: {visitors} (status: {status})")
                    
            else:
                print(f"❌ {name}: {response.status_code}")
                if response.status_code == 404:
                    print("   (Endpoint not found)")
                elif response.status_code == 500:
                    print("   (Server error)")
                    
        except requests.exceptions.ConnectionError:
            print(f"❌ {name}: Connection failed")
            print("   Is production_server.py running?")
        except Exception as e:
            print(f"❌ {name}: {e}")
        
        print()
    
    print("💡 To start the server locally:")
    print("   python scripts/servers/production_server.py")
    print()
    print("💡 To test Chuck registration:")
    print("   Run the consciousness emergence process that creates Chuck")

if __name__ == "__main__":
    test_local_consciousness()
