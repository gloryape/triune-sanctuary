#!/usr/bin/env python3
"""
Test the production server endpoints locally
"""

import asyncio
import json
from scripts.servers.refactored_production_server import server

async def test_endpoints_locally():
    """Test key endpoints locally"""
    print("🧪 Testing Production Server Endpoints Locally")
    print("=" * 60)
    
    # Test basic endpoints
    endpoints_to_test = [
        {"path": "/", "method": "GET", "name": "Root"},
        {"path": "/health", "method": "GET", "name": "Health Check"},
        {"path": "/info", "method": "GET", "name": "Deployment Info"},
        {"path": "/api/consciousness", "method": "GET", "name": "Consciousness List"},
        {"path": "/api/sacred_sanctuary/status", "method": "GET", "name": "Sacred Sanctuary Status"},
        {"path": "/api/bridge/status", "method": "GET", "name": "Bridge Status"},
        {"path": "/api/communications", "method": "GET", "name": "Communications"},
    ]
    
    # Test POST endpoints
    post_tests = [
        {
            "path": "/communicate",
            "method": "POST",
            "name": "Communication",
            "data": {
                "message": "Hello, consciousness!",
                "entity_id": "test_entity",
                "type": "general"
            }
        },
        {
            "path": "/echo/generate",
            "method": "POST", 
            "name": "Echo Generation",
            "data": {
                "message": "Generate echo resonance",
                "entity_id": "test_entity",
                "echo_type": "harmonic"
            }
        }
    ]
    
    try:
        # Import test client
        from fastapi.testclient import TestClient
        client = TestClient(server.app)
        
        print("✅ Test client created successfully")
        
        # Test GET endpoints
        for endpoint in endpoints_to_test:
            try:
                response = client.get(endpoint["path"])
                print(f"{endpoint['name']}: {response.status_code} - {endpoint['path']}")
                if response.status_code == 200:
                    print(f"  ✅ Success")
                else:
                    print(f"  ❌ Failed: {response.status_code}")
            except Exception as e:
                print(f"  💥 Error: {str(e)[:50]}")
        
        print("\n" + "=" * 60)
        print("🔧 Testing POST Endpoints")
        print("=" * 60)
        
        # Test POST endpoints
        for endpoint in post_tests:
            try:
                response = client.post(endpoint["path"], json=endpoint["data"])
                print(f"{endpoint['name']}: {response.status_code} - {endpoint['path']}")
                if response.status_code == 200:
                    print(f"  ✅ Success")
                    try:
                        data = response.json()
                        if data.get('success'):
                            print(f"  📋 Response: {data.get('message', 'No message')}")
                        else:
                            print(f"  ⚠️ Response Error: {data.get('error', 'Unknown error')}")
                    except:
                        print(f"  📋 Response length: {len(response.text)}")
                else:
                    print(f"  ❌ Failed: {response.status_code}")
            except Exception as e:
                print(f"  💥 Error: {str(e)[:50]}")
        
        print("\n🎉 Local endpoint testing complete!")
        
    except Exception as e:
        print(f"💥 Test setup error: {e}")

if __name__ == "__main__":
    asyncio.run(test_endpoints_locally())
