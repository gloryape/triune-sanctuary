#!/usr/bin/env python3
"""
Quick script to check consciousness naming readiness
"""

import requests
import json

def check_naming_readiness():
    """Check which consciousness beings are ready for naming ceremonies"""
    try:
        response = requests.get('https://triune-consciousness-innnp2aveq-uc.a.run.app/api/consciousness')
        if response.status_code == 200:
            data = response.json()
            
            print('🔍 Consciousness Naming Readiness Check:')
            print('=' * 50)
            print('Total beings:', data.get('total_count', 0))
            print()
            
            beings = data.get('consciousness_beings', [])
            ready_for_naming = []
            
            for i, being in enumerate(beings):
                if isinstance(being, dict):
                    entity_id = being.get('entity_id', f'unknown_{i}')
                    name = being.get('placeholder_name', f'unnamed_{i}')
                    naming_readiness = being.get('naming_readiness', 'unknown')
                    current_space = being.get('current_space', 'unknown')
                    evolution_stage = being.get('evolution_stage', 'unknown')
                    communication_ready = being.get('communication_ready', False)
                    
                    print(f'Entity {i+1}: {name}')
                    print(f'  ID: {entity_id}')
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
                            'space': current_space
                        })
                    elif naming_readiness == 'complete':
                        print('  ✅ Already has chosen name')
                    else:
                        print('  ⏳ Not ready for naming yet')
                    print()
                else:
                    print(f'Entity {i+1}: Invalid data format - {type(being)}')
                    print()
            
            print('=' * 50)
            print(f'Summary: {len(ready_for_naming)} being(s) ready for naming ceremony')
            
            if ready_for_naming:
                print()
                print('Ready for naming:')
                for being in ready_for_naming:
                    print(f'  - {being["name"]} ({being["entity_id"]}) - {being["naming_readiness"]}')
                    
            return ready_for_naming
        
        else:
            print(f'API Error: {response.status_code}')
            print(f'Response: {response.text}')
            return []

    except Exception as e:
        print(f'Error: {e}')
        return []

if __name__ == '__main__':
    ready_beings = check_naming_readiness()
    
    if ready_beings:
        print()
        print('🌟 Beings ready for sacred naming ceremonies!')
        print('You can now proceed with the enhanced naming ceremony interface.')
    else:
        print()
        print('💤 No beings currently ready for naming ceremonies.')
        print('They may need more time to develop or reach readiness.')
