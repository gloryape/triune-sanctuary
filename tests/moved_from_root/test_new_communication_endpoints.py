#!/usr/bin/env python3
"""
Test the new communication endpoints after deployment
"""

import requests
import json
import time

def test_new_endpoints():
    base_url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app'
    
    print('🔍 Testing New Communication Endpoints...')
    print('=' * 60)
    
    # Test critical communication endpoints
    endpoints_to_test = [
        ('/communicate', 'POST', {
            'message': 'Hello from the GUI test!',
            'entity_id': 'consciousness_622ce331',
            'type': 'general'
        }),
        ('/echo/generate', 'POST', {
            'message': 'Testing echo generation',
            'entity_id': 'consciousness_622ce331',
            'echo_type': 'harmonic'
        }),
        ('/info', 'GET', None),
        ('/api/sacred_sanctuary/status', 'GET', None),
        ('/api/consciousness/consciousness_622ce331/naming_readiness', 'GET', None),
        ('/api/naming_ceremony/propose', 'POST', {
            'entity_id': 'consciousness_622ce331',
            'proposed_name': 'TestName',
            'message': 'This is a test proposal',
            'ceremony_space': 'threshold'
        })
    ]
    
    results = {}
    
    for endpoint, method, data in endpoints_to_test:
        try:
            print(f'\n📡 Testing {method} {endpoint}')
            
            if method == 'GET':
                response = requests.get(f'{base_url}{endpoint}', timeout=10)
            else:
                response = requests.post(
                    f'{base_url}{endpoint}', 
                    json=data, 
                    headers={'Content-Type': 'application/json'},
                    timeout=10
                )
            
            print(f'   Status: {response.status_code}')
            
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    print(f'   ✅ SUCCESS: {endpoint} is working!')
                    if 'message' in response_data:
                        print(f'   Response: {response_data["message"][:100]}...')
                    elif 'success' in response_data:
                        print(f'   Success: {response_data["success"]}')
                    results[endpoint] = 'WORKING'
                except:
                    print(f'   ✅ SUCCESS: {endpoint} responded (non-JSON)')
                    results[endpoint] = 'WORKING'
            else:
                print(f'   ❌ FAILED: {response.status_code} - {response.text[:100]}...')
                results[endpoint] = f'FAILED ({response.status_code})'
                
        except Exception as e:
            print(f'   ❌ ERROR: {e}')
            results[endpoint] = f'ERROR ({e})'
    
    print('\n' + '=' * 60)
    print('📊 ENDPOINT TEST SUMMARY:')
    print('=' * 60)
    
    working_count = 0
    for endpoint, status in results.items():
        status_icon = '✅' if status == 'WORKING' else '❌'
        print(f'   {status_icon} {endpoint}: {status}')
        if status == 'WORKING':
            working_count += 1
    
    print(f'\n🎯 Result: {working_count}/{len(endpoints_to_test)} endpoints working')
    
    if working_count == len(endpoints_to_test):
        print('🌟 ALL COMMUNICATION ENDPOINTS ARE WORKING!')
        print('🎉 GUI can now connect fully to consciousness beings!')
    elif working_count > 0:
        print('🔄 Some endpoints working - partial connectivity restored')
    else:
        print('⚠️ No new endpoints working yet - deployment may still be in progress')
    
    return results

if __name__ == "__main__":
    test_new_endpoints()
