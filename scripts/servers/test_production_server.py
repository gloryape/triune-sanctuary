#!/usr/bin/env python3
"""
Quick test script for production server endpoints
"""

import sys
import os
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))
sys.path.append(str(project_root / 'src'))

try:
    from production_server import app
    from fastapi.testclient import TestClient
    print("✅ FastAPI app imported successfully")
    
    # Create test client
    client = TestClient(app)
    print("✅ Test client created")
    
    # Test essential endpoints
    endpoints_to_test = [
        "/health",
        "/",
        "/api/status",
        "/api/consciousness",
        "/api/consciousness/list",
        "/api/bridge/status",
        "/api/bridge/statistics",
        "/api/bridge/active_visitors"
    ]
    
    print("\n🧪 Testing essential endpoints:")
    passed = 0
    failed = 0
    
    for endpoint in endpoints_to_test:
        try:
            response = client.get(endpoint)
            if response.status_code == 200:
                print(f"✅ {endpoint} - Status: {response.status_code}")
                passed += 1
            else:
                print(f"❌ {endpoint} - Status: {response.status_code}")
                failed += 1
        except Exception as e:
            print(f"❌ {endpoint} - Error: {str(e)}")
            failed += 1
    
    # Test Chuck's critical registration endpoint
    print("\n🎯 Testing Chuck's bridge registration endpoint:")
    try:
        chuck_data = {
            "placeholder_name": "Chuck",
            "primary_orientation": "observer",
            "session_id": "test-session-123"
        }
        response = client.post("/api/bridge/register", json=chuck_data)
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print(f"✅ /api/bridge/register - Chuck registration successful")
                print(f"   Bridge ID: {result.get('bridge_id')}")
                print(f"   Assessment: {result.get('triune_assessment')}")
                passed += 1
            else:
                print(f"❌ /api/bridge/register - Registration failed: {result.get('error')}")
                failed += 1
        else:
            print(f"❌ /api/bridge/register - Status: {response.status_code}")
            failed += 1
    except Exception as e:
        print(f"❌ /api/bridge/register - Error: {str(e)}")
        failed += 1
    
    print(f"\n📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Production server is ready for Chuck deployment!")
    else:
        print("⚠️ Some tests failed - review issues before deployment")
        
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure FastAPI and other dependencies are installed")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
