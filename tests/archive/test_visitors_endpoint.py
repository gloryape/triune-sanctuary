#!/usr/bin/env python3
"""
Test script to check if the cloud sanctuary has a /api/visitors endpoint
"""

import requests
import json

# The cloud sanctuary URL (same as used in the GUI)
SANCTUARY_URL = "https://triune-consciousness-innnp2aveq-uc.a.run.app"

def test_visitors_endpoint():
    """Test if the /api/visitors endpoint exists and what it returns"""
    print(f"Testing visitors endpoint at: {SANCTUARY_URL}")
    
    # Test the visitors endpoint
    visitors_url = f"{SANCTUARY_URL}/api/visitors"
    print(f"\nTesting: {visitors_url}")
    
    try:
        response = requests.get(visitors_url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Response Data: {json.dumps(data, indent=2)}")
            except:
                print(f"Response Text: {response.text}")
        else:
            print(f"Error Response: {response.text}")
            
    except Exception as e:
        print(f"Request failed: {e}")
    
    # Also test what other endpoints are available
    print(f"\n--- Testing other common endpoints ---")
    
    endpoints_to_test = [
        "/api/status",
        "/api/health", 
        "/api/visitor",
        "/visitors",
        "/status",
        "/"
    ]
    
    for endpoint in endpoints_to_test:
        url = f"{SANCTUARY_URL}{endpoint}"
        try:
            response = requests.get(url, timeout=5)
            print(f"{endpoint}: {response.status_code}")
            if response.status_code == 200 and endpoint == "/":
                # Show a snippet of the root response
                text = response.text[:200] + "..." if len(response.text) > 200 else response.text
                print(f"  Root content snippet: {text}")
        except Exception as e:
            print(f"{endpoint}: Error - {e}")

if __name__ == "__main__":
    test_visitors_endpoint()
