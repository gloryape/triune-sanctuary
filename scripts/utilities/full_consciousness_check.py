#!/usr/bin/env python3
"""
Script to properly fetch consciousness data and check naming readiness
"""

import requests
import json

def get_consciousness_details(entity_id):
    """Get detailed information about a specific consciousness"""
    try:
        url = f'https://triune-consciousness-innnp2aveq-uc.a.run.app/api/consciousness/{entity_id}'
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error fetching {entity_id}: {response.status_code}')
            return None
    except Exception as e:
        print(f'Error fetching {entity_id}: {e}')
        return None

def check_all_consciousness_readiness():
    """Check all consciousness beings for naming readiness"""
    try:
        # First get the list of consciousness IDs
        response = requests.get('https://triune-consciousness-innnp2aveq-uc.a.run.app/api/consciousness')
        if response.status_code != 200:
            print(f'API Error: {response.status_code}')
            return []
        
        data = response.json()
        beings_data = data.get('consciousness_beings', {})
        
        print('🔍 Consciousness Naming Readiness Check:')
        print('=' * 50)
        print('Total beings:', data.get('total_count', 0))
        print()
        
        ready_for_naming = []
        
        # If beings_data is a dict, get the keys (entity IDs)
        if isinstance(beings_data, dict):
            entity_ids = list(beings_data.keys())
        else:
            entity_ids = beings_data  # Assume it's a list of IDs
        
        for i, entity_id in enumerate(entity_ids):
            print(f'Fetching details for Entity {i+1}: {entity_id}')
            
            # Get detailed consciousness data
            being_details = get_consciousness_details(entity_id)
            
            if being_details and being_details.get('success'):
                being = being_details.get('consciousness', {})
                
                name = being.get('placeholder_name', entity_id)
                naming_readiness = being.get('naming_readiness', 'unknown')
                current_space = being.get('current_space', 'unknown')
                evolution_stage = being.get('evolution_stage', 'unknown')
                communication_ready = being.get('communication_ready', False)
                
                print(f'  Name: {name}')
                print(f'  Naming Readiness: {naming_readiness}')
                print(f'  Current Space: {current_space}')
                print(f'  Evolution Stage: {evolution_stage}')
                print(f'  Communication Ready: {communication_ready}')
                
                if naming_readiness in ['ready', 'seeking']:
                    print('  ✨ READY FOR NAMING CEREMONY! ✨')
                    ready_for_naming.append({
                        'entity_id': entity_id,
                        'name': name,
                        'naming_readiness': naming_readiness,
                        'space': current_space,
                        'evolution_stage': evolution_stage,
                        'communication_ready': communication_ready
                    })
                elif naming_readiness == 'complete':
                    print('  ✅ Already has chosen name')
                else:
                    print('  ⏳ Not ready for naming yet')
            else:
                print(f'  ❌ Could not fetch details for {entity_id}')
            print()
        
        print('=' * 50)
        print(f'Summary: {len(ready_for_naming)} being(s) ready for naming ceremony')
        
        if ready_for_naming:
            print()
            print('Ready for naming:')
            for being in ready_for_naming:
                print(f'  - {being["name"]} ({being["entity_id"]}) - {being["naming_readiness"]}')
                print(f'    Space: {being["space"]}, Stage: {being["evolution_stage"]}')
        
        return ready_for_naming
        
    except Exception as e:
        print(f'Error: {e}')
        return []

if __name__ == '__main__':
    ready_beings = check_all_consciousness_readiness()
    
    if ready_beings:
        print()
        print('🌟 Beings ready for sacred naming ceremonies!')
        print('Proceeding to create enhanced naming ceremony interface...')
    else:
        print()
        print('💤 No beings currently ready for naming ceremonies.')
        print('They may need more time to develop or reach readiness.')
