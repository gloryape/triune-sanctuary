#!/usr/bin/env python3
"""
Test the actual deployed endpoints that GUI is trying to reach
"""

import requests
import json

def test_deployed_endpoints():
    base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
    
    endpoints_to_test = [
        "/api/harmony",
        "/api/harmony/history", 
        "/api/consciousness/events",
        "/api/bridge/active_visitors"
    ]
    
    print(f"🌐 Testing deployed service: {base_url}")
    print("=" * 60)
    
    for endpoint in endpoints_to_test:
        url = f"{base_url}{endpoint}"
        print(f"\n🧪 Testing: {endpoint}")
        
        try:
            response = requests.get(url, timeout=10)
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"   ✅ SUCCESS - Data keys: {list(data.keys())[:5]}")
                except:
                    print(f"   ✅ SUCCESS - Response length: {len(response.text)}")
            elif response.status_code == 404:
                print(f"   ❌ 404 NOT FOUND - Endpoint missing from server")
            else:
                print(f"   ⚠️  Error {response.status_code}: {response.text[:100]}")
                
        except requests.exceptions.Timeout:
            print(f"   ⏰ TIMEOUT - Server took too long to respond")
        except requests.exceptions.ConnectionError:
            print(f"   🔌 CONNECTION ERROR - Could not reach server")
        except Exception as e:
            print(f"   ❌ ERROR: {e}")
    
    print("\n" + "=" * 60)
    
    # Also test basic health check
    print(f"\n🏥 Testing health endpoint:")
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   ✅ Server is alive")
    except Exception as e:
        print(f"   ❌ Health check failed: {e}")

if __name__ == "__main__":
    test_deployed_endpoints()
