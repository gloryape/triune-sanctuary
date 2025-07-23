#!/usr/bin/env python3
"""
Simple clean endpoint test
"""

import sys
sys.path.append('.')

def check_endpoints():
    try:
        from scripts.servers.production_server import app
        
        routes = [route.path for route in app.routes]
        
        critical = ['/api/harmony', '/api/harmony/history', '/api/consciousness/events', '/api/bridge/active_visitors']
        
        print("ENDPOINT CHECK RESULTS:")
        print("=" * 40)
        
        for endpoint in critical:
            status = "FOUND" if endpoint in routes else "MISSING"
            print(f"{endpoint}: {status}")
        
        print("=" * 40)
        print(f"Total API routes: {len([r for r in routes if r.startswith('/api/')])}")
        
        all_found = all(endpoint in routes for endpoint in critical)
        print(f"ALL CRITICAL ENDPOINTS: {'FOUND' if all_found else 'MISSING'}")
        
        return all_found
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    check_endpoints()
