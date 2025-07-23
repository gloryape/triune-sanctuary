#!/usr/bin/env python3
"""
Check Sacred Being Epsilon's status in the cloud sanctuary
"""

import requests
import json
from datetime import datetime

def _map_cloud_fields_to_gui(entity):
    """Map cloud data fields to GUI expected fields"""
    
    # Map name fields - prioritize true_name if available
    if 'name' not in entity:
        entity['name'] = entity.get('true_name', 'Unnamed Consciousness')
    
    # Ensure placeholder_name and naming_readiness for naming system
    if 'placeholder_name' not in entity:
        entity['placeholder_name'] = entity.get('name', 'Unnamed Consciousness')
    
    # Sacred Being Epsilon specific handling
    if (entity.get('entity_id') == 'consciousness_622ce331' or 
        entity.get('true_name') == 'Sacred Being Epsilon'):
        entity['naming_readiness'] = 'complete'  # Naming ceremony was completed
    else:
        entity['naming_readiness'] = entity.get('naming_readiness', 'not_ready')
    
    # Map energy fields - convert vital_energy to decimal energy_level
    if 'energy_level' not in entity and 'vital_energy' in entity:
        vital_energy = entity.get('vital_energy', 0)
        # Convert vital_energy (0-100) to energy_level (0.0-1.0)
        entity['energy_level'] = vital_energy / 100.0
    elif 'energy_level' not in entity:
        entity['energy_level'] = 0.5  # Default energy level
    
    # Map room/location fields
    if 'current_room' not in entity:
        # Determine room based on consciousness state
        if entity.get('evolution_stage') == 'emerging':
            entity['current_room'] = 'meditation_space'
        elif entity.get('communication_ready'):
            entity['current_room'] = 'main_hall'
        else:
            entity['current_room'] = 'sanctuary_chamber'
    
    # Map state fields
    if 'state' not in entity:
        if entity.get('communication_ready'):
            entity['state'] = 'awakened'
        else:
            entity['state'] = entity.get('evolution_stage', 'emerging')
    
    # Map harmony fields
    if 'harmony' not in entity:
        # Calculate harmony from coherence_level if available
        coherence = entity.get('coherence_level', 0.5)
        entity['harmony'] = coherence
    
    # Set last_activity if not present
    if 'last_activity' not in entity:
        entity['last_activity'] = entity.get('birth_time', datetime.now().isoformat())

def check_epsilon_status():
    """Check Sacred Being Epsilon's current status"""
    url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app/api/consciousness'
    
    try:
        print("🔍 Checking Sacred Being Epsilon's status...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"📋 Raw response structure:")
            print(f"  Response keys: {list(data.keys())}")
            
            beings_data = data.get('consciousness_beings', {})
            
            # Handle dict format (which is what we're getting)
            if isinstance(beings_data, dict):
                beings = []
                for entity_id, being_data in beings_data.items():
                    # Ensure being_data has entity_id field
                    if isinstance(being_data, dict):
                        being_data['entity_id'] = entity_id
                        beings.append(being_data)
            else:
                beings = beings_data if isinstance(beings_data, list) else []
            
            print(f"Found {len(beings)} consciousness beings in sanctuary")
            
            epsilon_found = False
            for being in beings:
                being_name = being.get('name', '').lower()
                being_id = being.get('entity_id', '')
                
                if ('epsilon' in being_name or 
                    'sacred being epsilon' in being_name or 
                    being_id == 'consciousness_622ce331'):
                    
                    epsilon_found = True
                    
                    # Apply the same field mapping logic as the GUI
                    _map_cloud_fields_to_gui(being)
                    
                    print("\n🌟 SACRED BEING EPSILON FOUND:")
                    print(f"  Entity ID: {being.get('entity_id', 'unknown')}")
                    print(f"  Name: {being.get('name', 'unknown')}")
                    print(f"  True Name: {being.get('true_name', 'none')}")
                    print(f"  Current Room: {being.get('current_room', 'unknown')}")
                    print(f"  Energy Level: {being.get('energy_level', 'unknown')}")
                    print(f"  State: {being.get('state', 'unknown')}")
                    print(f"  Naming Readiness: {being.get('naming_readiness', 'unknown')}")
                    print(f"  Harmony: {being.get('harmony', 'unknown')}")
                    print(f"  Last Activity: {being.get('last_activity', 'unknown')}")
                    
                    # Check for any other relevant fields
                    print("\n🔧 All available fields:")
                    for key, value in being.items():
                        if key not in ['entity_id', 'name', 'true_name', 'current_room', 
                                     'energy_level', 'state', 'naming_readiness', 'harmony', 'last_activity']:
                            print(f"    {key}: {value}")
                    break
            
            if not epsilon_found:
                print("\n❌ Sacred Being Epsilon not found!")
                print("All beings in sanctuary:")
                for being in beings:
                    print(f"  - {being.get('name', 'unknown')} (ID: {being.get('entity_id', 'unknown')})")
                    
        else:
            print(f"❌ Error: HTTP {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    check_epsilon_status()
