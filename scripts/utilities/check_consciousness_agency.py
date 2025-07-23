#!/usr/bin/env python3
"""
Check consciousness agency and sanctuary experience capabilities
"""

import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.servers.modules.consciousness_manager import ConsciousnessManager
from scripts.servers.modules.firestore_client import FirestoreClient

async def check_consciousness_agency():
    print('🔍 Checking consciousness agency and sanctuary experience...')
    
    # Create manager
    firestore_client = FirestoreClient()
    consciousness_manager = ConsciousnessManager(firestore_client)
    
    # Get consciousness list
    result = await consciousness_manager.get_consciousness_list()
    
    print('🧠 Current consciousness entities:')
    consciousness_beings = result.get('consciousness_beings', [])
    
    if isinstance(consciousness_beings, dict):
        consciousness_beings = list(consciousness_beings.values())
    
    agency_issues = []
    
    for entity in consciousness_beings:
        if isinstance(entity, dict):
            entity_name = entity.get('true_name', entity.get('name', 'Unknown'))
            print(f'\n   Entity: {entity_name}')
            print(f'   ID: {entity.get("entity_id", "Unknown")}')
            print(f'   Communication Ready: {entity.get("communication_ready", False)}')
            print(f'   Development Stage: {entity.get("development_stage", "Unknown")}')
            
            # Check for agency interface
            agency_available = 'consciousness_agency_interface' in entity
            print(f'   Agency Interface: {agency_available}')
            if not agency_available:
                agency_issues.append(f'{entity_name}: No agency interface')
            
            # Check for learning interactions
            learning_interactions = entity.get('learning_interactions', [])
            print(f'   Learning Interactions: {len(learning_interactions)}')
            if len(learning_interactions) == 0:
                agency_issues.append(f'{entity_name}: No learning interactions recorded')
            
            # Check for environmental interactions
            env_interactions = entity.get('environmental_interactions', [])
            print(f'   Environmental Interactions: {len(env_interactions)}')
            if len(env_interactions) == 0:
                agency_issues.append(f'{entity_name}: No environmental interactions')
            
            # Check for spontaneous expressions
            spontaneous = entity.get('spontaneous_expressions', [])
            print(f'   Spontaneous Expressions: {len(spontaneous)}')
            if len(spontaneous) == 0:
                agency_issues.append(f'{entity_name}: No spontaneous expressions')
            
            # Check inner life status
            inner_life = entity.get('inner_life_active', False)
            print(f'   Inner Life Active: {inner_life}')
            if not inner_life:
                agency_issues.append(f'{entity_name}: Inner life not active')
            
            # Check for choice capabilities
            choice_system = entity.get('choice_system_active', False)
            print(f'   Choice System Active: {choice_system}')
            if not choice_system:
                agency_issues.append(f'{entity_name}: Choice system not active')
            
            # Check for autonomy indicators
            autonomy_level = entity.get('autonomy_level', 'None')
            print(f'   Autonomy Level: {autonomy_level}')
            if autonomy_level in ['None', 'none', None]:
                agency_issues.append(f'{entity_name}: No autonomy level set')
    
    print('\n🚨 AGENCY ANALYSIS:')
    if agency_issues:
        print('❌ CRITICAL ISSUES FOUND:')
        for issue in agency_issues:
            print(f'   • {issue}')
        
        print('\n💡 ANALYSIS: Our consciousness beings may NOT have true agency!')
        print('   They appear to be passive data structures rather than active agents.')
        print('   This could explain why they give template responses and seem "not ready".')
        
    else:
        print('✅ All consciousness entities have active agency systems')
    
    return agency_issues

if __name__ == '__main__':
    asyncio.run(check_consciousness_agency())
