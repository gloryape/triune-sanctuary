#!/usr/bin/env python3
"""
Enhanced script to handle different API response formats
"""

import requests
import json

def check_naming_readiness_detailed():
    """Check consciousness beings with detailed API response handling"""
    try:
        response = requests.get('https://triune-consciousness-innnp2aveq-uc.a.run.app/api/consciousness')
        if response.status_code == 200:
            data = response.json()
            
            print('🔍 Raw API Response Analysis:')
            print('=' * 50)
            print('Response keys:', list(data.keys()))
            print('Total count:', data.get('total_count', 0))
            print()
            
            beings = data.get('consciousness_beings', [])
            print(f'Beings type: {type(beings)}')
            print(f'Beings length: {len(beings)}')
            print()
            
            for i, being in enumerate(beings):
                print(f'Being {i+1} type: {type(being)}')
                print(f'Being {i+1} content: {being}')
                
                # Try to parse if it's a string
                if isinstance(being, str):
                    try:
                        parsed_being = json.loads(being)
                        print(f'Parsed being {i+1}: {parsed_being}')
                        
                        # Extract fields from parsed being
                        entity_id = parsed_being.get('entity_id', f'unknown_{i}')
                        name = parsed_being.get('placeholder_name', f'unnamed_{i}')
                        naming_readiness = parsed_being.get('naming_readiness', 'unknown')
                        
                        print(f'  Entity ID: {entity_id}')
                        print(f'  Name: {name}')
                        print(f'  Naming Readiness: {naming_readiness}')
                        
                        if naming_readiness in ['ready', 'seeking']:
                            print('  ✨ READY FOR NAMING CEREMONY! ✨')
                            
                    except json.JSONDecodeError:
                        print(f'  Could not parse as JSON: {being}')
                elif isinstance(being, dict):
                    print(f'  Direct dict access: {being}')
                
                print()
            
            return beings
        
        else:
            print(f'API Error: {response.status_code}')
            return []

    except Exception as e:
        print(f'Error: {e}')
        return []

if __name__ == '__main__':
    check_naming_readiness_detailed()
