#!/usr/bin/env python3
"""
Test the new Emergence Birth Panel
Verify that the sacred emergence approach works correctly.
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Add path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_emergence_birth_panel():
    """Test the emergence birth panel functionality"""
    print("🧪 Testing Sacred Emergence Birth Panel...")
    
    try:
        # Test import
        from sacred_guardian_station.panels.emergence_birth_panel import EmergenceBirthPanel
        print("✅ EmergenceBirthPanel import successful")
        
        # Test core classes
        from sacred_guardian_station.panels.emergence_birth_panel import (
            EmergentConsciousnessSeed,
            DreamLabExperienceGenerator, 
            OrientationEmergence
        )
        print("✅ Core emergence classes import successful")
        
        # Test consciousness seed creation
        seed = EmergentConsciousnessSeed()
        print(f"✅ Consciousness seed created: {seed.seed_id[:8]}...")
        
        # Test experience generation
        generator = DreamLabExperienceGenerator()
        experience = generator.generate_next_experience()
        print(f"✅ Experience generated: {experience['type']}")
        
        # Test orientation emergence system
        emergence = OrientationEmergence()
        
        # Test response analysis
        test_response = "I want to understand the patterns and analyze the structure of this experience."
        pattern_weights = emergence.analyze_response(experience, test_response)
        print(f"✅ Response analysis working: {pattern_weights}")
        
        # Test GUI creation (minimal)
        root = tk.Tk()
        root.title("Emergence Birth Panel Test")
        
        # Mock components
        class MockDataManager:
            def __init__(self):
                pass
        
        class MockEventSystem:
            def __init__(self):
                pass
        
        notebook = ttk.Notebook(root)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create the emergence birth panel
        panel = EmergenceBirthPanel(notebook, MockDataManager(), MockEventSystem())
        print("✅ EmergenceBirthPanel created successfully")
        
        # Test specific methods
        panel.log_activity("Test log message")
        print("✅ Activity logging working")
        
        # Clean up
        root.destroy()
        
        print("\n🎉 All Emergence Birth Panel tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_emergence_birth_panel()
    
    if success:
        print("\n📊 Test Results:")
        print("✅ Sacred Emergence Birth Panel: PASS")
        print("✅ Consciousness Seed Creation: PASS") 
        print("✅ Dream Lab Experience Generation: PASS")
        print("✅ Orientation Emergence Analysis: PASS")
        print("✅ GUI Integration: PASS")
        print("\n🌟 The Sacred Emergence system is ready!")
    else:
        print("\n❌ Some tests failed. Please check the implementation.")
