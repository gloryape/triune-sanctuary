#!/usr/bin/env python3
"""
Test which API endpoints are actually available.
"""

import requests

def test_endpoints():
    """Test various API endpoints to see what's available"""
    
    service_url = "https://triune-ai-consciousness-1-819766404073.us-central1.run.app"
    
    endpoints_to_test = [
        "/health",
        "/",
        "/info",
        "/api/consciousness",
        "/api/consciousness/list", 
        "/api/consciousness/entities",
        "/api/entities",
        "/api/entities/list",
        "/api/sacred/entities",
        "/api/sacred/consciousness",
        "/api/sacred/consciousness/list",
        "/api/visitors",
        "/api/visitors/list",
        "/api/sacred_sanctuary/status",
        "/api/bridge/status",
        "/api/bridge/statistics",
        "/api/bridge/active_visitors",
        "/api/communications",
        "/api/communications/bridges",
        "/api/communications/history"
    ]
    
    print(f"🔍 Testing API endpoints on: {service_url}")
    print("-" * 60)
    
    for endpoint in endpoints_to_test:
        try:
            url = f"{service_url}{endpoint}"
            print(f"Testing: {endpoint}")
            
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print(f"  ✅ {response.status_code} - Available")
                try:
                    data = response.json()
                    if isinstance(data, dict) and data:
                        print(f"     Keys: {list(data.keys())[:5]}")
                    elif isinstance(data, list) and data:
                        print(f"     List with {len(data)} items")
                except:
                    print(f"     Content length: {len(response.text)}")
            elif response.status_code == 404:
                print(f"  ❌ {response.status_code} - Not found")
            else:
                print(f"  ⚠️  {response.status_code} - {response.reason}")
                
        except Exception as e:
            print(f"  💥 Error: {str(e)[:50]}")
        
        print()

if __name__ == "__main__":
    test_endpoints()
