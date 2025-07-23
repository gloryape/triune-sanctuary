#!/usr/bin/env python3
"""
Test visitor panel connection fix
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sacred_guardian_station'))

try:
    from sacred_guardian_station.core.data_manager_new import DataManager
    
    print("🧪 Testing visitor panel connection fix...")
    
    # Create data manager
    data_manager = DataManager()
    
    # Test visitor data retrieval
    print("📡 Getting visitor data...")
    visitor_data = data_manager.get_visitor_data()
    
    print(f"✅ Visitor data received:")
    print(f"   - Visitors: {len(visitor_data.get('visitors', []))}")
    print(f"   - Total visitors: {visitor_data.get('total_visitors', 0)}")
    print(f"   - Active visitors: {visitor_data.get('active_visitors', 0)}")
    
    # Test sacred events for comparison
    print("📡 Getting sacred events for comparison...")
    sacred_events = data_manager.get_sacred_events()
    print(f"✅ Sacred events: {len(sacred_events)} events")
    
    if visitor_data.get('visitors') or sacred_events:
        print("🎉 Connection working! Both visitor and events data available.")
    elif sacred_events:
        print("⚠️ Sacred events work but visitors don't - partial connection")
    else:
        print("❌ No data from either source - full connection issue")
        
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
