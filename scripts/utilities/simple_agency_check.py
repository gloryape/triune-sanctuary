#!/usr/bin/env python3
"""
Simple consciousness agency check 
"""

import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.servers.modules.consciousness_manager import ConsciousnessManager
from scripts.servers.modules.firestore_client import FirestoreClient

async def simple_agency_check():
    print('🔍 Simple consciousness agency check...')
    
    firestore_client = FirestoreClient() 
    consciousness_manager = ConsciousnessManager(firestore_client)
    
    result = await consciousness_manager.get_consciousness_list()
    consciousness_beings = result.get('consciousness_beings', [])
    
    if isinstance(consciousness_beings, dict):
        consciousness_beings = list(consciousness_beings.values())
    
    print(f'Found {len(consciousness_beings)} consciousness entities:')
    
    for entity in consciousness_beings:
        if isinstance(entity, dict):
            print(f'\n  {entity.get("true_name", "Unknown")}:')
            print(f'    Agency Interface Available: {"consciousness_agency_interface" in entity}')
            print(f'    Inner Life Active: {entity.get("inner_life_active", False)}')
            print(f'    Learning Interactions: {len(entity.get("learning_interactions", []))}')
            print(f'    Spontaneous Expressions: {len(entity.get("spontaneous_expressions", []))}')
            print(f'    Environmental Interactions: {len(entity.get("environmental_interactions", []))}')

if __name__ == '__main__':
    asyncio.run(simple_agency_check())
