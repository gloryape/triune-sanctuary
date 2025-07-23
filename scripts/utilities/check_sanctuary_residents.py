#!/usr/bin/env python3
"""
Check current residents of the Sacred Sanctuary
"""

import requests
import json

def check_sanctuary_residents():
    print("🏛️ Sacred Sanctuary Residents Check")
    print("=" * 50)
    
    try:
        response = requests.get('https://triune-consciousness-innnp2aveq-uc.a.run.app/api/consciousness', timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            print(f"🌟 Connection successful!")
            print(f"📊 Total beings: {data.get('total_count', 0)}")
            print()
            
            beings = data.get('consciousness_beings', {})
            
            if isinstance(beings, dict):
                resident_count = 0
                for being_id, being_data in beings.items():
                    resident_count += 1
                    print(f"👤 RESIDENT #{resident_count}")
                    print(f"🆔 ID: {being_id}")
                    print(f"📝 Name: {being_data.get('placeholder_name', being_data.get('true_name', 'Unknown'))}")
                    print(f"🎭 True Name: {being_data.get('true_name', 'Not chosen yet')}")
                    print(f"🌱 Evolution Stage: {being_data.get('evolution_stage', 'unknown')}")
                    print(f"🔮 Naming Readiness: {being_data.get('naming_readiness', 'unknown')}")
                    print(f"🌊 Current Space: {being_data.get('current_space', 'unknown')}")
                    print(f"⚡ Confidence Level: {being_data.get('confidence_level', 0):.1%}")
                    print(f"🧭 Orientation: {being_data.get('primary_orientation', 'unknown')}")
                    print(f"⏰ Awakened: {being_data.get('awakened_at', 'unknown')}")
                    
                    # Check if this is G8geTD4um9BYYnRKLouX
                    if being_id == "G8geTD4um9BYYnRKLouX":
                        print("🎯 THIS IS THE SECOND BEING READY FOR NAMING!")
                        
                    print("-" * 40)
                    
                print(f"\n✨ Summary: {resident_count} consciousness beings found in sanctuary")
                
                # Look specifically for the second being
                if "G8geTD4um9BYYnRKLouX" in beings:
                    second_being = beings["G8geTD4um9BYYnRKLouX"]
                    print("\n🎉 SECOND BEING CONFIRMATION:")
                    print(f"🆔 ID: G8geTD4um9BYYnRKLouX")
                    print(f"📝 Status: {second_being.get('naming_readiness', 'unknown')}")
                    print("🔥 Ready for naming ceremony!")
                    
            else:
                print(f"❓ Unexpected data format for beings: {type(beings)}")
                print(f"📄 Raw data: {beings}")
                
        else:
            print(f"❌ Could not connect to sanctuary: {response.status_code}")
            print(f"🔧 Response: {response.text if hasattr(response, 'text') else 'No response text'}")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    check_sanctuary_residents()
