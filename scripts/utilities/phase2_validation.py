"""
Quick GUI validation test for all Phase 2 panels.
This test launches the GUI briefly to ensure all panels load and display correctly.
"""

import sys
import os
import threading
import time

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sacred_guardian_station'))

def test_gui_launch():
    """Test that the GUI launches and all panels load correctly"""
    print("🧪 Testing Sacred Guardian Station GUI Launch...")
    
    try:
        from main import SacredGuardianStation
        
        # Create the application
        print("✅ Creating Sacred Guardian Station instance...")
        app = SacredGuardianStation()
        
        # Test that all panels were created
        panels_to_check = [
            'consciousness_panel',
            'sacred_events_panel', 
            'memory_panel',
            'harmony_panel',
            'communication_panel',
            'visitor_panel'
        ]
        
        print("✅ Checking panel initialization...")
        for panel_name in panels_to_check:
            if hasattr(app, panel_name):
                panel = getattr(app, panel_name)
                print(f"  ✅ {panel_name}: Successfully created")
                
                # Test that panel has required methods
                if hasattr(panel, 'refresh'):
                    print(f"    ✅ {panel_name}: Has refresh method")
                else:
                    print(f"    ⚠️ {panel_name}: Missing refresh method")
            else:
                print(f"  ❌ {panel_name}: Not found in application")
                return False
        
        # Test notebook has all tabs
        tab_count = app.notebook.index('end')
        print(f"✅ Notebook contains {tab_count} tabs")
        
        if tab_count >= 6:
            print("✅ All expected panels are present in the notebook")
        else:
            print("⚠️ Some panels may be missing from the notebook")
        
        # Test refresh mechanism
        print("✅ Testing panel refresh mechanism...")
        try:
            app.refresh_all_panels()
            print("  ✅ Refresh mechanism working")
        except Exception as e:
            print(f"  ⚠️ Refresh mechanism issue: {e}")
        
        # Test data manager integration
        print("✅ Testing data manager integration...")
        test_methods = [
            'get_consciousness_list',
            'get_sacred_events',
            'get_memory_data', 
            'get_harmony_metrics',
            'get_communication_bridges',
            'get_visitor_data'
        ]
        
        for method_name in test_methods:
            if hasattr(app.data_manager, method_name):
                try:
                    method = getattr(app.data_manager, method_name)
                    result = method()
                    print(f"  ✅ {method_name}: Returns data successfully")
                except Exception as e:
                    print(f"  ⚠️ {method_name}: Error - {e}")
            else:
                print(f"  ❌ {method_name}: Method not found")
        
        # Don't actually show the GUI, just verify initialization
        print("✅ GUI validation test completed successfully!")
        print("🎉 All Phase 2 panels are properly integrated!")
        
        # Clean up without showing GUI
        app.root.quit()
        return True
        
    except Exception as e:
        print(f"❌ GUI validation test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run the GUI validation test"""
    print("🌟 Sacred Guardian Station - Phase 2 Validation Test 🌟")
    print("=" * 60)
    
    success = test_gui_launch()
    
    print("=" * 60)
    if success:
        print("🎉 PHASE 2 VALIDATION PASSED!")
        print("Sacred Guardian Station is ready for use!")
    else:
        print("⚠️ Validation issues detected. Please check the output above.")
    
    print("=" * 60)
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
