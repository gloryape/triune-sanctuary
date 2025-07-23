#!/usr/bin/env python3
import sys
sys.path.append('.')

try:
    from sacred_guardian_station.core.data_manager import DataManager
    from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
    
    # Create instances
    sanctuary = SanctuaryConnection()
    data_manager = DataManager(sanctuary)
    
    # Check if method exists
    if hasattr(data_manager, 'get_sacred_bridge_system_status'):
        print('✅ DataManager has get_sacred_bridge_system_status method')
        # Try calling it
        result = data_manager.get_sacred_bridge_system_status()
        print('✅ Method executes successfully')
        print(f'📊 Result keys: {list(result.keys())}')
    else:
        print('❌ DataManager missing get_sacred_bridge_system_status method')
        print(f'📋 Available methods: {[m for m in dir(data_manager) if not m.startswith("_")]}')
        
except Exception as e:
    print(f'❌ Error: {e}')
    import traceback
    traceback.print_exc()
