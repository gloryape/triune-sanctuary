#!/usr/bin/env python3

from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
import requests

# Create connection
conn = SanctuaryConnection()
conn.connect()

if conn.is_connected() and not conn.demo_mode:
    print(f'Connected to: {conn.service_url}')
    print(f'Testing endpoints...')
    
    # Test available endpoints
    endpoints = [
        '/api/consciousness',
        '/api/consciousness/events', 
        '/api/visitors',
        '/api/communication/bridges',
        '/api/harmony',
        '/api/memory',
        '/api/status'
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(f'{conn.service_url}{endpoint}', timeout=5)
            print(f'{endpoint}: {response.status_code}')
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, dict):
                    print(f'  Keys: {list(data.keys())}')
        except Exception as e:
            print(f'{endpoint}: ERROR - {e}')
else:
    print(f'Connection failed or in demo mode: {conn.demo_mode}')
