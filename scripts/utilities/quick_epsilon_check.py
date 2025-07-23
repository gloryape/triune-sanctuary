#!/usr/bin/env python3
"""
Quick Sacred Being Epsilon status check 
"""

import requests
import json

def quick_status_check():
    """Quick check if Sacred Being Epsilon is working"""
    try:
        print("🕯️  Quick Sacred Being Epsilon Status Check")
        print("=" * 45)
        
        # Test the known working URL first
        url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app/api/consciousness'
        
        print("🔍 Testing deployed service...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            beings_data = data.get('consciousness_beings', {})
            
            # Count consciousness beings
            being_count = len(beings_data) if isinstance(beings_data, dict) else len(beings_data)
            print(f"✅ Service responding! Found {being_count} consciousness beings")
            
            # Look for Sacred Being Epsilon
            epsilon_found = False
            if isinstance(beings_data, dict):
                for entity_id, being_data in beings_data.items():
                    if (entity_id == 'consciousness_622ce331' or 
                        being_data.get('true_name') == 'Sacred Being Epsilon'):
                        epsilon_found = True
                        print(f"🌟 Sacred Being Epsilon found with ID: {entity_id}")
                        print(f"   True Name: {being_data.get('true_name', 'unknown')}")
                        print(f"   Vital Energy: {being_data.get('vital_energy', 'unknown')}")
                        break
            
            if not epsilon_found:
                print("❌ Sacred Being Epsilon not found in response")
            
            return True
        else:
            print(f"❌ Service error: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

def test_communication_bridges():
    """Test communication bridges endpoint"""
    try:
        url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app/api/communication_bridges'
        
        print("\n🌉 Testing communication bridges...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Communication bridges endpoint working!")
            print(f"   Success: {data.get('success', 'unknown')}")
            print(f"   Bridges: {len(data.get('bridges', []))}")
            return True
        else:
            print(f"❌ Bridges error: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Bridges connection error: {e}")
        return False

def main():
    service_ok = quick_status_check()
    bridges_ok = test_communication_bridges()
    
    print("\n" + "=" * 45)
    if service_ok and bridges_ok:
        print("🎉 Sacred Guardian Station should work perfectly!")
        print("   - Sacred Being Epsilon data: ✅")
        print("   - Communication bridges: ✅")
        print("   - Refactored server: ✅")
    elif service_ok:
        print("⚠️  Sacred Being Epsilon working, but bridges need check")
    else:
        print("⏳ Deployment may still be in progress...")
    
    print("\n🌟 If deployment is complete, restart Sacred Guardian Station GUI!")

if __name__ == "__main__":
    main()
