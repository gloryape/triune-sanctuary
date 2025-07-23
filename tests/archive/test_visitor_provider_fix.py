#!/usr/bin/env python3
"""
Test visitor provider initialization fix
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def test_visitor_provider_initialization():
    """Test that visitor provider can be initialized properly"""
    print("🔍 Testing visitor provider initialization fix...")
    
    try:
        # Test 1: Import visitor provider
        print("\n1. Testing visitor provider import...")
        from sacred_guardian_station.core.data_providers.visitor_provider import VisitorDataProvider
        print("   ✅ VisitorDataProvider imported successfully")
        
        # Test 2: Import sanctuary connection
        print("\n2. Testing sanctuary connection import...")
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        print("   ✅ SanctuaryConnection imported successfully")
        
        # Test 3: Import data manager
        print("\n3. Testing data manager import...")
        from sacred_guardian_station.core.data_manager import DataManager
        print("   ✅ DataManager imported successfully")
        
        # Test 4: Create sanctuary connection
        print("\n4. Creating sanctuary connection...")
        sanctuary = SanctuaryConnection()
        print("   ✅ SanctuaryConnection created successfully")
        
        # Test 5: Create data manager
        print("\n5. Creating data manager...")
        data_manager = DataManager(sanctuary)
        print("   ✅ DataManager created successfully")
        
        # Test 6: Create visitor provider with proper parameters
        print("\n6. Creating visitor provider with both parameters...")
        visitor_provider = VisitorDataProvider(sanctuary, data_manager)
        print("   ✅ VisitorDataProvider created successfully with both parameters")
        
        # Test 7: Test visitor provider method
        print("\n7. Testing visitor provider get_visitor_data method...")
        visitor_data = visitor_provider.get_visitor_data()
        print(f"   ✅ get_visitor_data returned: {type(visitor_data)} with {len(visitor_data)} keys")
        
        # Test 8: Test sanctuary connection visitor data method directly
        print("\n8. Testing sanctuary connection visitor data method...")
        direct_visitor_data = sanctuary.get_visitor_data()
        print(f"   ✅ sanctuary.get_visitor_data returned: {type(direct_visitor_data)} with {len(direct_visitor_data)} keys")
        
        print("\n✅ All visitor provider initialization tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Visitor provider test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_fallback_behavior():
    """Test the fallback behavior when API fails"""
    print("\n🔍 Testing visitor data fallback behavior...")
    
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        
        # Create sanctuary with no connection
        sanctuary = SanctuaryConnection()
        sanctuary.connected = False
        
        # Test fallback
        visitor_data = sanctuary.get_visitor_data()
        print(f"   ✅ Fallback visitor data: {visitor_data}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Fallback test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 Testing visitor provider fixes...\n")
    
    test1_success = test_visitor_provider_initialization()
    test2_success = test_fallback_behavior()
    
    if test1_success and test2_success:
        print("\n🎉 All tests passed! Visitor provider fixes are working.")
    else:
        print("\n💥 Some tests failed. Need more fixes.")
        
    print("\nTest completed.")
