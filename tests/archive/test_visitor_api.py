#!/usr/bin/env python3
"""
Test the visitor API endpoint
"""

from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
import requests

def test_visitor_api():
    try:
        sanctuary = SanctuaryConnection()
        service_url = sanctuary._get_deployed_service_url()
        print(f'Service URL: {service_url}')
        
        if service_url:
            response = requests.get(f'{service_url}/api/bridge/active_visitors', timeout=10)
            print(f'Visitor API Status: {response.status_code}')
            if response.status_code == 200:
                data = response.json()
                print(f'Visitor API Response: {data}')
            else:
                print(f'Response content: {response.text[:200]}')
        else:
            print('No service URL found')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    test_visitor_api()
