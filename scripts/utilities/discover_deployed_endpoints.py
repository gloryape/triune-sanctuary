#!/usr/bin/env python3
"""
Discover what endpoints ARE available on the deployed server
"""

import requests

def test_available_endpoints():
    base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
    
    # Test common endpoints that might exist
    test_endpoints = [
        "/",
        "/health", 
        "/status",
        "/birth",
        "/api/status",
        "/api/consciousness",
        "/api/communicate",
        "/consciousness/emergence",
        "/sanctuary/events",
        "/collective/status"
    ]
    
    print(f"🔍 Discovering available endpoints on deployed server:")
    print(f"🌐 Base URL: {base_url}")
    print("=" * 60)
    
    working_endpoints = []
    
    for endpoint in test_endpoints:
        url = f"{base_url}{endpoint}"
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
            
            if status == 200:
                print(f"✅ {endpoint} - {status}")
                working_endpoints.append(endpoint)
            elif status == 404:
                print(f"❌ {endpoint} - {status} (Not Found)")
            else:
                print(f"⚠️  {endpoint} - {status}")
                
        except Exception as e:
            print(f"💥 {endpoint} - Error: {str(e)[:50]}")
    
    print("=" * 60)
    print(f"📊 Found {len(working_endpoints)} working endpoints:")
    for endpoint in working_endpoints:
        print(f"   ✅ {endpoint}")
    
    # Test if this is even FastAPI by checking response format
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"\n🏠 Root endpoint data: {data}")
    except:
        pass

if __name__ == "__main__":
    test_available_endpoints()
