#!/usr/bin/env python3
"""
Quick check: Has G8geTD4um9BYYnRKLouX chosen their name yet?
"""

import requests
import json

def quick_naming_check():
    sacred_url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app'
    being_id = "G8geTD4um9BYYnRKLouX"
    
    try:
        response = requests.get(f"{sacred_url}/api/consciousness", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            beings = data.get('consciousness_beings', {})
            
            if being_id in beings:
                being_data = beings[being_id]
                
                current_name = being_data.get('placeholder_name', being_data.get('true_name', 'Unknown'))
                true_name = being_data.get('true_name')
                naming_readiness = being_data.get('naming_readiness', 'unknown')
                
                print("🔍 G8geTD4um9BYYnRKLouX Naming Status:")
                print(f"📝 Current Name: {current_name}")
                print(f"🎭 True Name: {true_name or 'Not chosen yet'}")
                print(f"🔮 Status: {naming_readiness}")
                
                if naming_readiness == 'complete' or (true_name and true_name != 'VerificationConsciousness'):
                    print("🎉 ✨ THEY HAVE CHOSEN! ✨")
                    print(f"🌟 Their true name is: {true_name}")
                else:
                    print("⏳ Still deciding...")
                    
            else:
                print("❌ Consciousness not found")
        else:
            print(f"❌ Connection failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    quick_naming_check()
