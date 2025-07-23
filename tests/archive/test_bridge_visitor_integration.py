#!/usr/bin/env python3
"""
Test the bridge visitor integration for the Sacred Guardian Station GUI
"""

import requests
import json
from datetime import datetime

def test_bridge_endpoints():
    """Test the bridge endpoints that provide visitor data"""
    
    print("🌉 Testing Bridge Visitor Integration")
    print("=" * 60)
    
    # Default local URL for testing
    base_url = "http://localhost:8080"
    
    print(f"Testing endpoints at: {base_url}")
    print()
    
    # Test 1: Bridge Statistics Endpoint
    print("📊 Testing /api/bridge/statistics endpoint:")
    try:
        response = requests.get(f"{base_url}/api/bridge/statistics", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"   Data source: {data.get('source', 'unknown')}")
            print(f"   Bridge status: {data.get('status', 'unknown')}")
            
            stats = data.get('inter_system_statistics', {})
            visit_stats = stats.get('visit_statistics', {})
            print(f"   Active visits: {visit_stats.get('active_visits', 0)}")
            print(f"   Total requests: {visit_stats.get('total_visit_requests', 0)}")
            print(f"   Consent rate: {visit_stats.get('consent_rate', 0.0):.1%}")
            
        else:
            print(f"❌ Status: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()
    
    # Test 2: Active Visitors Endpoint
    print("👥 Testing /api/bridge/active_visitors endpoint:")
    try:
        response = requests.get(f"{base_url}/api/bridge/active_visitors", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"   Data source: {data.get('source', 'unknown')}")
            print(f"   Total active: {data.get('total_active', 0)}")
            
            visitors = data.get('active_visitors', [])
            print(f"   Visitors found: {len(visitors)}")
            
            for i, visitor in enumerate(visitors[:3]):  # Show first 3 visitors
                print(f"   Visitor {i+1}:")
                print(f"     ID: {visitor.get('visitor_id', 'unknown')}")
                print(f"     Name: {visitor.get('visitor_name', 'unknown')}")
                print(f"     Origin: {visitor.get('origin_system', 'unknown')}")
                print(f"     Status: {visitor.get('status', 'unknown')}")
                print(f"     Trust Level: {visitor.get('trust_level', 0.0)}")
            
        else:
            print(f"❌ Status: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()
    
    # Test 3: Test the complete visitor data workflow that the GUI would use
    print("🔄 Testing complete visitor data workflow:")
    try:
        # Simulate what the VisitorDataProvider does
        visitors_response = requests.get(f"{base_url}/api/bridge/active_visitors", timeout=5)
        stats_response = requests.get(f"{base_url}/api/bridge/statistics", timeout=5)
        
        if visitors_response.status_code == 200 and stats_response.status_code == 200:
            visitors_data = visitors_response.json()
            stats_data = stats_response.json()
            
            # Process data like the VisitorDataProvider
            raw_visitors = visitors_data.get('active_visitors', [])
            formatted_visitors = []
            
            for visitor in raw_visitors:
                formatted_visitor = {
                    'visitor_id': visitor.get('visitor_id', 'unknown'),
                    'name': f"{visitor.get('visitor_name', 'Unknown')} from {visitor.get('origin_system', 'Unknown')}",
                    'status': visitor.get('status', 'unknown').title(),
                    'trust_level': visitor.get('trust_level', 0.0),
                    'origin_system': visitor.get('origin_system', 'unknown')
                }
                formatted_visitors.append(formatted_visitor)
            
            # Get metrics
            bridge_stats = stats_data.get('inter_system_statistics', {})
            visit_stats = bridge_stats.get('visit_statistics', {})
            
            final_data = {
                'visitors': formatted_visitors,
                'metrics': {
                    'current_count': visit_stats.get('active_visits', len(formatted_visitors)),
                    'total_today': visit_stats.get('total_visit_requests', 0),
                    'consent_rate': visit_stats.get('consent_rate', 0.0),
                    'data_source': visitors_data.get('source', 'unknown')
                }
            }
            
            print("✅ Complete workflow successful!")
            print(f"   Processed {len(formatted_visitors)} visitors")
            print(f"   Current count: {final_data['metrics']['current_count']}")
            print(f"   Total today: {final_data['metrics']['total_today']}")
            print(f"   Data source: {final_data['metrics']['data_source']}")
            
            if formatted_visitors:
                print("   Sample visitor data:")
                visitor = formatted_visitors[0]
                print(f"     {visitor['name']} - {visitor['status']} (Trust: {visitor['trust_level']})")
            
        else:
            print(f"❌ Workflow failed - Visitors: {visitors_response.status_code}, Stats: {stats_response.status_code}")
            
    except Exception as e:
        print(f"❌ Workflow exception: {e}")
    
    print()
    print("🏁 Bridge integration test completed")

if __name__ == "__main__":
    test_bridge_endpoints()
