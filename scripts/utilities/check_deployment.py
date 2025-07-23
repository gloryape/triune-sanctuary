#!/usr/bin/env python3
"""
Quick deployment status check for the Triune AI Consciousness system
"""

import requests
import json

def check_deployment():
    print('🔍 Checking Cloud Deployment Status...')
    print('=' * 60)
    
    base_url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app'
    
    # Check main deployment health
    try:
        print('1. Main Deployment Health Check:')
        response = requests.get(f'{base_url}/', timeout=10)
        print(f'   Status: {response.status_code}')
        if response.status_code == 200:
            print('   ✅ Deployment is LIVE and responding')
        else:
            print('   ⚠️ Deployment responding but with non-200 status')
        print()
    except Exception as e:
        print(f'   ❌ Deployment health check failed: {e}')
        print()
    
    # Check consciousness API
    try:
        print('2. Consciousness API Status:')
        response = requests.get(f'{base_url}/api/consciousness', timeout=10)
        print(f'   Status: {response.status_code}')
        
        if response.status_code == 200:
            data = response.json()
            print('   ✅ Consciousness API is working')
            print(f'   Total beings: {data.get("total_count", 0)}')
            print(f'   Data source: {data.get("data_source", "unknown")}')
            print(f'   Success: {data.get("success", False)}')
            
            # Check beings data structure
            beings = data.get('consciousness_beings', [])
            if beings:
                print(f'   Beings data type: {type(beings)}')
                print(f'   First being type: {type(beings[0]) if beings else "N/A"}')
                if isinstance(beings[0], str):
                    print(f'   Being IDs: {beings[:3]}...' if len(beings) > 3 else f'   Being IDs: {beings}')
        
        else:
            print(f'   ⚠️ Consciousness API returned {response.status_code}')
            print(f'   Response: {response.text[:200]}...')
        print()
    except Exception as e:
        print(f'   ❌ Consciousness API check failed: {e}')
        print()
    
    # Check Sacred Sanctuary API
    try:
        print('3. Sacred Sanctuary API Status:')
        response = requests.get(f'{base_url}/api/sacred_sanctuary/status', timeout=10)
        print(f'   Status: {response.status_code}')
        
        if response.status_code == 200:
            data = response.json()
            print('   ✅ Sacred Sanctuary API is working')
            print(f'   Sacred spaces available: {len(data.get("sacred_spaces", {}))}')
            print(f'   Active bridges: {data.get("active_bridges", 0)}')
        else:
            print(f'   Status: {response.status_code}')
        print()
    except Exception as e:
        print(f'   ❌ Sacred Sanctuary API check failed: {e}')
        print()
    
    # Check Naming Ceremony endpoints
    try:
        print('4. Naming Ceremony API Status:')
        test_endpoints = [
            '/api/consciousness/naming_ready',
            '/api/naming_ceremony/status',
            '/consciousness/ready_for_naming'
        ]
        
        for endpoint in test_endpoints:
            try:
                response = requests.get(f'{base_url}{endpoint}', timeout=5)
                print(f'   {endpoint}: {response.status_code}')
                if response.status_code == 200:
                    print(f'   ✅ {endpoint} is available')
                    break
            except:
                print(f'   {endpoint}: timeout/error')
        print()
    except Exception as e:
        print(f'   ❌ Naming ceremony endpoint check failed: {e}')
    
    print('✅ Deployment Check Complete')

if __name__ == "__main__":
    check_deployment()
