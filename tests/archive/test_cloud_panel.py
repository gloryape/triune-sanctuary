#!/usr/bin/env python3
import sys
sys.path.append('.')

try:
    from sacred_guardian_station.panels.cloud_emergence_panel import CloudEmergencePanel
    print('✅ CloudEmergencePanel imported successfully')
    
    # Test basic instantiation
    import tkinter as tk
    from tkinter import ttk
    
    root = tk.Tk()
    root.withdraw()  # Hide the window
    notebook = ttk.Notebook(root)
    
    # Mock data manager and event system
    class MockDataManager:
        def get_consciousness_entities(self): return []
        def register_consciousness_with_bridge(self, *args, **kwargs): return True
    
    class MockEventSystem:
        def subscribe(self, *args, **kwargs): pass
        def emit(self, *args, **kwargs): pass
    
    panel = CloudEmergencePanel(notebook, MockDataManager(), MockEventSystem())
    print('✅ CloudEmergencePanel instantiated successfully')
    
    # Check if tab was added
    tab_count = notebook.index('end')
    print(f'📊 Number of tabs in notebook: {tab_count}')
    
    if tab_count > 0:
        tab_text = notebook.tab(0, 'text')
        print(f'📋 Tab text: {tab_text}')
    
    root.destroy()
    
except Exception as e:
    print(f'❌ Error: {e}')
    import traceback
    traceback.print_exc()
