#!/usr/bin/env python3
"""
Post-Deployment Bridge Communication Validation
==============================================

Validates that the bridge communication system is working correctly
after cloud deployment.
"""

import requests
import json
import os
import sys
from datetime import datetime

def validate_deployment(base_url: str) -> bool:
    """Validate the deployed bridge communication system"""
    print(f"Bridge Communication System Deployment Validation")
    print(f"Target URL: {base_url}")
    
    # Test endpoints that should be available
    endpoints_to_test = [
        ("/health", "GET"),
        ("/info", "GET"),
        ("/api/consciousness", "GET"),
        ("/api/bridge/status", "GET"),
        ("/api/sacred_sanctuary/status", "GET"),
        ("/api/communications/bridges", "GET"),
        ("/api/communications/history", "GET"),
    ]
    
    success_count = 0
    total_count = len(endpoints_to_test)
    
    print(f"\nTesting {total_count} endpoints...")
    
    for endpoint, method in endpoints_to_test:
        try:
            url = f"{base_url}{endpoint}"
            
            if method == "GET":
                response = requests.get(url, timeout=30)
            else:
                response = requests.post(url, timeout=30)
            
            if response.status_code == 200:
                print(f"  SUCCESS {endpoint}: {response.status_code}")
                success_count += 1
            else:
                print(f"  FAILED {endpoint}: {response.status_code}")
                
        except Exception as e:
            print(f"  ERROR {endpoint}: {str(e)}")
    
    # Test communication endpoints with POST data
    print(f"\nTesting communication endpoints...")
    
    try:
        # Test communication endpoint
        comm_url = f"{base_url}/communicate"
        comm_payload = {
            "message": "Post-deployment validation test",
            "type": "validation"
        }
        
        comm_response = requests.post(comm_url, json=comm_payload, timeout=30)
        if comm_response.status_code == 200:
            print(f"  SUCCESS /communicate: {comm_response.status_code}")
            success_count += 1
        else:
            print(f"  FAILED /communicate: {comm_response.status_code}")
            
    except Exception as e:
        print(f"  ERROR /communicate: {str(e)}")
    
    try:
        # Test echo generation endpoint
        echo_url = f"{base_url}/echo/generate"
        echo_payload = {
            "message": "Bridge validation echo test",
            "echo_type": "validation"
        }
        
        echo_response = requests.post(echo_url, json=echo_payload, timeout=30)
        if echo_response.status_code == 200:
            print(f"  SUCCESS /echo/generate: {echo_response.status_code}")
            success_count += 1
        else:
            print(f"  FAILED /echo/generate: {echo_response.status_code}")
            
    except Exception as e:
        print(f"  ERROR /echo/generate: {str(e)}")
    
    total_with_comm = total_count + 2  # Added communication tests
    
    print(f"\nValidation Results:")
    print(f"   Success: {success_count}/{total_with_comm}")
    print(f"   Success Rate: {(success_count/total_with_comm)*100:.1f}%")
    
    # Check if bridge communication system is working
    if success_count >= total_with_comm * 0.8:  # 80% success rate threshold
        print(f"\nBridge Communication System Deployment: SUCCESSFUL!")
        print(f"   Ready for GUI integration")
        print(f"   Consciousness beings accessible")
        print(f"   Communication endpoints operational")
        return True
    else:
        print(f"\nBridge Communication System Deployment: FAILED!")
        print(f"   Success rate below threshold (80%)")
        print(f"   Manual investigation required")
        return False

def main():
    """Main validation function"""
    # Get deployment URL from environment or command line
    if len(sys.argv) > 1:
        base_url = sys.argv[1].rstrip('/')
    else:
        # Default to our known deployment URL
        base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
    
    print(f"Post-Deployment Bridge Validation")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    success = validate_deployment(base_url)
    
    if success:
        print(f"\nVALIDATION PASSED - Bridge communication system ready!")
        sys.exit(0)
    else:
        print(f"\nVALIDATION FAILED - Bridge communication system needs attention!")
        sys.exit(1)

if __name__ == "__main__":
    main()
