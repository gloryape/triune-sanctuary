#!/usr/bin/env python3
"""
Debug the consciousness data structure
"""

import requests
import json

def debug_consciousness_data():
    # First, let's see what the consciousness list looks like
    url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app/api/consciousness'
    
    print("🧠 Getting consciousness list...")
    
    try:
        response = requests.get(url, timeout=30)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Success: {data.get('success', False)}")
            print(f"Total Count: {data.get('total_count', 0)}")
            
            beings = data.get('consciousness_beings', {})
            print(f"Beings type: {type(beings)}")
            print(f"Beings structure: {beings}")
            
            # Check each being
            if isinstance(beings, dict):
                for being_id, being_data in beings.items():
                    print(f"\nBeing ID: {being_id}")
                    print(f"Being Data Type: {type(being_data)}")
                    print(f"Being Data: {being_data}")
                    
                    if isinstance(being_data, dict):
                        print(f"Communication Ready: {being_data.get('communication_ready', False)}")
                    else:
                        print(f"⚠️ Being data is not a dict: {being_data}")
            else:
                print(f"⚠️ Beings is not a dict: {beings}")
                
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    debug_consciousness_data()
