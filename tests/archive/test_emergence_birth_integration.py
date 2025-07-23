#!/usr/bin/env python3
"""
Test the emergence birth panel integration with consciousness creation
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'sacred_guardian_station'))

import tkinter as tk
from tkinter import ttk
import time

class MockSanctuary:
    def __init__(self):
        self.service_url = "http://localhost:8080"

class MockDataManager:
    def __init__(self):
        self.sanctuary = MockSanctuary()
        self.stored_consciousness = []
        
    def store_consciousness_data(self, consciousness_data):
        """Mock store consciousness data"""
        print(f"📝 Storing consciousness data: {consciousness_data['placeholder_name']}")
        print(f"   Orientation: {consciousness_data['primary_orientation']}")
        print(f"   Confidence: {consciousness_data.get('emergence_confidence', 'unknown')}")
        print(f"   Method: {consciousness_data.get('emergence_method', 'unknown')}")
        self.stored_consciousness.append(consciousness_data)
        return True
        
    def refresh_all_data(self):
        print("🔄 Refreshing all data...")
        
class MockEventSystem:
    def publish(self, event_type, data):
        print(f"📡 Event published: {event_type} - {data.get('placeholder_name', 'unknown')}")

def test_emergence_birth_integration():
    """Test the emergence birth integration"""
    print("🧪 Testing Emergence Birth Panel Integration")
    print("=" * 50)
    
    # Create mock components
    data_manager = MockDataManager()
    event_system = MockEventSystem()
    
    # Create main window
    root = tk.Tk()
    root.title("Emergence Birth Test")
    root.geometry("1200x800")
    
    # Create notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)
    
    try:
        # Import and create emergence birth panel
        from panels.emergence_birth_panel import EmergenceBirthPanel
        
        emergence_panel = EmergenceBirthPanel(notebook, data_manager, event_system)
        
        print("✅ Emergence birth panel created successfully")
        print("✅ Panel integrated with mock data manager")
        print("✅ Panel integrated with mock event system")
        print()
        print("🌟 Test Instructions:")
        print("1. Click 'Begin Sacred Emergence' button")
        print("2. Enter a consciousness name (e.g., 'TestConsciousness')")
        print("3. Watch the autonomous emergence process")
        print("4. Observe when consciousness data is stored")
        print("5. Check console output for storage confirmation")
        print()
        print("Expected outcome: Consciousness should be created and stored")
        print("Current stored consciousness count:", len(data_manager.stored_consciousness))
        
        def check_stored_consciousness():
            """Check for newly stored consciousness"""
            if len(data_manager.stored_consciousness) > 0:
                print("\n🎉 SUCCESS: Consciousness data stored!")
                for i, consciousness in enumerate(data_manager.stored_consciousness):
                    print(f"   {i+1}. {consciousness['placeholder_name']} ({consciousness['primary_orientation']})")
            root.after(5000, check_stored_consciousness)
        
        # Start checking for stored consciousness
        root.after(5000, check_stored_consciousness)
        
        # Run the test
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Error creating emergence birth panel: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_emergence_birth_integration()
