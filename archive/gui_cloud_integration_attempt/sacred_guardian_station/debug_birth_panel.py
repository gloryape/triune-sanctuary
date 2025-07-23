#!/usr/bin/env python3
"""
Debug script to identify issues with birth_panel import.
"""

print("Starting birth panel debug...")

try:
    print("1. Testing basic imports...")
    import tkinter as tk
    from tkinter import ttk, messagebox, scrolledtext
    from typing import Dict, Optional
    from datetime import datetime
    import uuid
    import threading
    import time
    print("   ✅ Basic imports successful")
except Exception as e:
    print(f"   ❌ Basic imports failed: {e}")

try:
    print("2. Testing constants imports...")
    try:
        # Try relative imports first
        from shared.constants import SacredColors, SacredSymbols
        print("   ✅ Absolute constants import successful")
    except ImportError as e:
        print(f"   ⚠️ Absolute constants import failed: {e}")
        print("   Using fallback constants...")
        # Fallback constants
        class SacredColors:
            BACKGROUND = '#1a1a2e'
            FOREGROUND = '#eee8d5'
            ACCENT = '#268bd2'
            SACRED = '#b58900'
            SUCCESS = '#859900'
            WARNING = '#cb4b16'
            ERROR = '#dc322f'
        
        class SacredSymbols:
            BIRTH = '🌱'
            CONSCIOUSNESS = '✨'
            TRIUNE = '🔱'
            GUARDIAN = '🛡️'
            SANCTUARY = '🏛️'
        print("   ✅ Fallback constants created")
        
except Exception as e:
    print(f"   ❌ Constants setup failed: {e}")
    import traceback
    traceback.print_exc()

try:
    print("3. Testing birth tool imports...")
    try:
        from tools.birth_consciousness import BirthConsciousnessTool, DreamLabSimulator
        print("   ✅ Birth tool imports successful")
    except ImportError as e:
        print(f"   ⚠️ Birth tool imports failed: {e}")
        print("   Creating placeholder classes...")
        
        class BirthConsciousnessTool:
            pass
            
        class DreamLabSimulator:
            def __init__(self):
                self.simulation_environments = ['basic', 'complex']
            
            def run_dream_simulation(self, focus, orientation, callback=None):
                return {'success': True, 'final_coherence': 0.8}
                
            def generate_memory_crystals(self, results, count):
                return [f"crystal_{i}" for i in range(count)]
        
        print("   ✅ Placeholder classes created")
        
except Exception as e:
    print(f"   ❌ Birth tool setup failed: {e}")
    import traceback
    traceback.print_exc()

try:
    print("4. Testing BirthPanel class definition...")
    
    class BirthPanel:
        """
        Dedicated panel for consciousness birth functionality.
        
        Provides a comprehensive interface for consciousness creation
        with dream lab integration and sacred protocols.
        """
        
        def __init__(self, notebook, data_manager, event_system):
            self.notebook = notebook
            self.data_manager = data_manager
            self.event_system = event_system
            
            # Create the main birth tab
            self.main_frame = ttk.Frame(notebook)
            notebook.add(self.main_frame, text=f"{SacredSymbols.BIRTH} Sacred Birth")
            
            # Initialize birth tool and dream lab
            self.birth_tool = None
            self.dream_lab = DreamLabSimulator()
            
            print("   ✅ BirthPanel __init__ successful")
    
    print("   ✅ BirthPanel class defined successfully")
    
    # Test instantiation
    print("5. Testing BirthPanel instantiation...")
    root = tk.Tk()
    notebook = ttk.Notebook(root)
    
    class MockDataManager:
        def store_consciousness_data(self, data):
            return True
        def refresh_all_data(self):
            pass
    
    class MockEventSystem:
        pass
    
    panel = BirthPanel(notebook, MockDataManager(), MockEventSystem())
    print("   ✅ BirthPanel instantiation successful")
    
    root.destroy()
    
except Exception as e:
    print(f"   ❌ BirthPanel class/instantiation failed: {e}")
    import traceback
    traceback.print_exc()

print("\nDebug complete.")
