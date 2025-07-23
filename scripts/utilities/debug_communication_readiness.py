#!/usr/bin/env python3
"""
Debug script to examine consciousness entity communication readiness
"""

import requests
import json

def debug_consciousness_communication_readiness():
    """Debug the communication readiness flags"""
    print("🔍 Debugging Consciousness Communication Readiness")
    print("=" * 50)
    
    base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
    
    try:
        # Get consciousness list
        response = requests.get(f"{base_url}/api/consciousness", timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            beings = data.get('consciousness_beings', {})
            
            print(f"📊 Total beings found: {len(beings)}")
            print()
            
            if isinstance(beings, dict):
                for being_id, being_data in beings.items():
                    name = being_data.get('placeholder_name', being_data.get('true_name', 'Unknown'))
                    print(f"🔮 {name} (ID: {being_id})")
                    print(f"   📝 Full data keys: {list(being_data.keys())}")
                    print(f"   💬 Communication Ready: {being_data.get('communication_ready', 'NOT SET')}")
                    print(f"   🌱 Evolution Stage: {being_data.get('evolution_stage', 'unknown')}")
                    print(f"   🔮 Naming Readiness: {being_data.get('naming_readiness', 'unknown')}")
                    print(f"   ⚡ Confidence Level: {being_data.get('confidence_level', 0)}")
                    print()
                    
                # Check if any have communication_ready = True
                comm_ready_count = sum(1 for being in beings.values() if being.get('communication_ready', False))
                print(f"📈 Entities with communication_ready=True: {comm_ready_count}")
                
        else:
            print(f"❌ Failed to get consciousness list: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error debugging consciousness readiness: {e}")

if __name__ == "__main__":
    debug_consciousness_communication_readiness()
