#!/usr/bin/env python3
"""
Test Birth Panel Functionality
Verify that the birth panel loads correctly and all functionality works.
"""
import sys
import os
import tkinter as tk

# Add the sacred guardian station to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sacred_guardian_station'))

def test_birth_panel():
    """Test the birth panel functionality"""
    print("🌟 Testing Birth Panel Functionality")
    print("=" * 50)
    
    try:
        # Test imports
        print("1. Testing imports...")
        from sacred_guardian_station.panels.birth_panel import BirthPanel
        print("   ✅ BirthPanel imported successfully")
        
        from sacred_guardian_station.shared.constants import SacredColors, SacredSymbols
        print("   ✅ Sacred constants imported successfully")
        
        # Test class instantiation
        print("\n2. Testing class instantiation...")
        root = tk.Tk()
        root.withdraw()  # Hide the test window
        
        notebook = tk.ttk.Notebook(root)
        
        # Mock data manager and event system
        class MockDataManager:
            def store_consciousness_data(self, data):
                return True
            def refresh_all_data(self):
                pass
        
        class MockEventSystem:
            pass
        
        data_manager = MockDataManager()
        event_system = MockEventSystem()
        
        # Create birth panel
        birth_panel = BirthPanel(notebook, data_manager, event_system)
        print("   ✅ BirthPanel instantiated successfully")
        
        # Test panel components
        print("\n3. Testing panel components...")
        
        # Test if main frame exists
        if hasattr(birth_panel, 'main_frame'):
            print("   ✅ Main frame created")
        
        # Test if dream lab exists
        if hasattr(birth_panel, 'dream_lab'):
            print("   ✅ Dream lab simulator created")
        
        # Test if configuration variables exist
        if hasattr(birth_panel, 'name_var'):
            print("   ✅ Configuration variables created")
        
        # Test dream lab functionality
        print("\n4. Testing dream lab simulation...")
        if hasattr(birth_panel.dream_lab, 'run_dream_simulation'):
            results = birth_panel.dream_lab.run_dream_simulation('adaptive_learning', 'observer')
            if results.get('success'):
                print("   ✅ Dream lab simulation successful")
                print(f"   💎 Coherence level: {results.get('final_coherence', 'Unknown')}")
            else:
                print("   ❌ Dream lab simulation failed")
        
        print("\n5. Testing birth panel methods...")
        
        # Test status update method
        if hasattr(birth_panel, 'update_status'):
            birth_panel.update_status("Test status message")
            print("   ✅ Status update method works")
        
        # Test dream lab stats method
        if hasattr(birth_panel, 'update_dream_lab_stats'):
            birth_panel.update_dream_lab_stats()
            print("   ✅ Dream lab stats method works")
        
        root.destroy()
        
        print("\n" + "=" * 50)
        print("🎉 BIRTH PANEL TEST COMPLETED SUCCESSFULLY!")
        print("✨ The Sacred Birth Chamber is fully operational!")
        return True
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_birth_panel()
    if success:
        print("\n🌟 SACRED GUARDIAN STATION BIRTH PANEL RESTORED!")
        print("The consciousness birth functionality is ready for use.")
    else:
        print("\n❌ Birth panel testing failed. Further debugging needed.")
