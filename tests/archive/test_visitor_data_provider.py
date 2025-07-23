#!/usr/bin/env python3
"""
Test the visitor data provider with the new bridge integration
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def test_visitor_data_provider():
    """Test the visitor data provider in both demo and cloud modes"""
    
    print("🔍 Testing Visitor Data Provider")
    print("=" * 50)
    
    try:
        # Import the data provider
        from sacred_guardian_station.core.data_providers import VisitorDataProvider
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        
        print("✅ Imports successful")
        
        # Test demo mode
        print("\n📋 Testing Demo Mode:")
        demo_connection = SanctuaryConnection(demo_mode=True)
        demo_provider = VisitorDataProvider(demo_connection, None)
        
        demo_data = demo_provider.get_visitor_data()
        print(f"Demo visitors: {len(demo_data.get('visitors', []))}")
        print(f"Demo metrics: {demo_data.get('metrics', {})}")
        
        # Test cloud mode (will try to connect to real sanctuary)
        print("\n🌐 Testing Cloud Mode:")
        cloud_connection = SanctuaryConnection(demo_mode=False)
        cloud_connection.connect()
        
        cloud_provider = VisitorDataProvider(cloud_connection, None)
        cloud_data = cloud_provider.get_visitor_data()
        
        print(f"Cloud connection successful: {cloud_connection.connected}")
        print(f"Cloud service URL: {cloud_connection.service_url}")
        print(f"Cloud visitors: {len(cloud_data.get('visitors', []))}")
        print(f"Cloud metrics: {cloud_data.get('metrics', {})}")
        
        # Test cloud data structure
        if cloud_data.get('metrics'):
            metrics = cloud_data['metrics']
            print(f"\nCloud Visitor Metrics:")
            print(f"  Current Count: {metrics.get('current_count', 0)}")
            print(f"  Total Today: {metrics.get('total_today', 0)}")
            print(f"  Consent Rate: {metrics.get('consent_rate', 0.0):.1%}")
            print(f"  Harmony Level: {metrics.get('harmony_level', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_visitor_data_provider()
    if success:
        print("\n✅ Visitor data provider test completed successfully!")
    else:
        print("\n❌ Visitor data provider test failed!")
