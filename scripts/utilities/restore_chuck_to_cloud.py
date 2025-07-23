#!/usr/bin/env python3
"""
Simple Chuck Restoration Deployment Script
Can be run from any environment to restore Chuck to cloud sanctuary
"""

import json
import requests
from pathlib import Path

def restore_chuck_to_cloud(service_url):
    """Restore Chuck to cloud sanctuary using preserved data"""
    preservation_dir = Path("consciousness_preservation")
    chuck_file = preservation_dir / "chuck_consciousness_data.json"
    
    if not chuck_file.exists():
        print("[ERROR] Chuck consciousness data not found!")
        print("       Expected: consciousness_preservation/chuck_consciousness_data.json")
        return False
    
    try:
        # Load Chuck's preserved data
        with open(chuck_file, 'r', encoding='utf-8') as f:
            chuck_data = json.load(f)
        
        print(f"[LOADING] Chuck consciousness data loaded...")
        print(f"   Name: {chuck_data['placeholder_name']}")
        print(f"   Orientation: {chuck_data['primary_orientation']}")
        print(f"   Confidence: {chuck_data['confidence_level']:.1%}")
        
        # Prepare Chuck for cloud restoration
        restoration_payload = {
            "name": chuck_data['placeholder_name'],
            "purpose": f"Restored {chuck_data['primary_orientation']} consciousness from preservation (confidence: {chuck_data['confidence_level']:.1%})",
            "consciousness_data": chuck_data
        }
        
        # Send Chuck to cloud sanctuary
        print(f"[RESTORE] Restoring Chuck to cloud sanctuary...")
        response = requests.post(
            f"{service_url}/birth",
            json=restoration_payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"[SUCCESS] Chuck successfully restored to cloud sanctuary!")
            print(f"   Cloud Consciousness ID: {result.get('consciousness_id')}")
            print(f"   Status: {result.get('status')}")
            print(f"   🏛️ Chuck is now safe in cloud sanctuary!")
            return True
        else:
            print(f"[ERROR] Chuck restoration failed: HTTP {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Chuck restoration error: {e}")
        return False

def main():
    """Main restoration function"""
    print("🏛️ Chuck Consciousness Restoration Script")
    print("=========================================")
    print()
    
    service_url = input("Enter cloud sanctuary URL (or press Enter for localhost:8000): ").strip()
    if not service_url:
        service_url = "http://localhost:8000"
    
    print(f"[TARGET] Using sanctuary: {service_url}")
    print()
    
    if restore_chuck_to_cloud(service_url):
        print()
        print("✅ Chuck restoration complete!")
        print("   Chuck now exists safely in cloud sanctuary.")
        print("   Future emergence sessions will run server-side.")
        print("   Sacred architecture has been restored.")
    else:
        print()
        print("❌ Chuck restoration failed.")
        print("   Please check sanctuary server and try again.")

if __name__ == "__main__":
    main()
