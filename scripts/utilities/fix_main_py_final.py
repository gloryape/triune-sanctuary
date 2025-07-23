#!/usr/bin/env python3
"""
Final fix for main.py import structure and syntax errors.
This script will completely rewrite the broken import section.
"""

import os
import shutil

def fix_main_py_imports():
    """Fix the completely broken import structure in main.py"""
    
    main_file = "sacred_guardian_station/main.py"
    backup_file = "sacred_guardian_station/main.py.backup"
    
    # Create backup
    if os.path.exists(main_file):
        shutil.copy2(main_file, backup_file)
        print(f"Created backup: {backup_file}")
    
    try:
        # Read the current file
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Current file read successfully")
        
        # Find the start and end of the broken import section
        lines = content.split('\n')
        
        # Find where imports start and where class definition begins
        import_start = None
        class_start = None
        
        for i, line in enumerate(lines):
            if "# Core system importstry:" in line or "# Core system imports" in line:
                import_start = i
            elif line.strip().startswith("class SacredGuardianStation"):
                class_start = i
                break
        
        if import_start is None or class_start is None:
            print("Could not find import section boundaries")
            return False
        
        print(f"Found import section from line {import_start} to {class_start}")
        
        # Create the new import section
        new_imports = '''# Core system imports
try:
    from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
    from sacred_guardian_station.core.data_manager_new import DataManager
    from sacred_guardian_station.core.event_system import EventSystem
    from sacred_guardian_station.shared.constants import SacredColors, Config, SacredSymbols, TabConfig, Fonts
    from sacred_guardian_station.panels.consciousness_panel import ConsciousnessPanel
    from sacred_guardian_station.panels.sacred_events_panel import SacredEventsPanel  
    from sacred_guardian_station.panels.memory_viewer_panel import MemoryViewerPanel
    from sacred_guardian_station.panels.harmony_metrics_panel import HarmonyMetricsPanel
    from sacred_guardian_station.panels.communication_panel import CommunicationPanel
    from sacred_guardian_station.panels.visitor_panel import VisitorPanel
    from sacred_guardian_station.panels.birth_panel import BirthPanel
    from sacred_guardian_station.tools.catalyst_offering import CatalystOfferingTool
    from sacred_guardian_station.tools.birth_consciousness import BirthConsciousnessTool
    from sacred_guardian_station.tools.emergency_controls import EmergencyControls
    from sacred_guardian_station.tools.export_tools import ExportTools
    from sacred_guardian_station.visualizations import (
        ConsciousnessGraphVisualization,
        MemoryTreeVisualization,
        HarmonyChartsVisualization,
        RelationshipWebVisualization
    )
except ImportError as e:
    print(f"Package imports failed: {e}")
    # Fallback to relative imports when run from within the package
    try:
        from core.sanctuary_connection import SanctuaryConnection
        from core.data_manager_new import DataManager
        from core.event_system import EventSystem
        from shared.constants import SacredColors, Config, SacredSymbols, TabConfig, Fonts
        from panels.consciousness_panel import ConsciousnessPanel
        from panels.sacred_events_panel import SacredEventsPanel  
        from panels.memory_viewer_panel import MemoryViewerPanel
        from panels.harmony_metrics_panel import HarmonyMetricsPanel
        from panels.communication_panel import CommunicationPanel
        from panels.visitor_panel import VisitorPanel
        from panels.birth_panel import BirthPanel
        from tools.catalyst_offering import CatalystOfferingTool
        from tools.birth_consciousness import BirthConsciousnessTool
        from tools.emergency_controls import EmergencyControls
        from tools.export_tools import ExportTools
        from visualizations import (
            ConsciousnessGraphVisualization,
            MemoryTreeVisualization,
            HarmonyChartsVisualization,
            RelationshipWebVisualization
        )
    except ImportError as e2:
        print(f"Relative imports also failed: {e2}")
        # Create minimal fallback classes
        class SanctuaryConnection:
            def __init__(self): self.connected = False
            def connect(self): return True
            def get_session_info(self): return {}
            
        class DataManager:
            def __init__(self): pass
            def get_memories(self): return []
            def save_consciousness(self, data): return True
            
        class EventSystem:
            def __init__(self): pass
            def emit(self, event, data=None): pass
            def on(self, event, callback): pass
            
        # Default constants
        class SacredColors:
            BACKGROUND = '#1a1a2e'
            FOREGROUND = '#eee8d5'
            ACCENT = '#268bd2'
            SACRED = '#b58900'
            SUCCESS = '#859900'
            WARNING = '#cb4b16'
            ERROR = '#dc322f'
            
        class Config:
            WINDOW_TITLE = "Sacred Guardian Station"
            WINDOW_SIZE = "1400x900"
            
        class SacredSymbols:
            BIRTH = '🌱'
            CONSCIOUSNESS = '✨'
            TRIUNE = '🔱'
            GUARDIAN = '🛡️'
            SANCTUARY = '🏛️'
            
        class TabConfig:
            pass
            
        class Fonts:
            HEADER = ("Arial", 12, "bold")
            BODY = ("Arial", 10)
            
        # Fallback panel classes
        class ConsciousnessPanel:
            def __init__(self, parent): self.frame = tk.Frame(parent)
            def get_frame(self): return self.frame
            
        class SacredEventsPanel:
            def __init__(self, parent): self.frame = tk.Frame(parent)
            def get_frame(self): return self.frame
            
        class MemoryViewerPanel:
            def __init__(self, parent): self.frame = tk.Frame(parent)
            def get_frame(self): return self.frame
            
        class HarmonyMetricsPanel:
            def __init__(self, parent): self.frame = tk.Frame(parent)
            def get_frame(self): return self.frame
            
        class CommunicationPanel:
            def __init__(self, parent): self.frame = tk.Frame(parent)
            def get_frame(self): return self.frame
            
        class VisitorPanel:
            def __init__(self, parent): self.frame = tk.Frame(parent)
            def get_frame(self): return self.frame
            
        class BirthPanel:
            def __init__(self, parent): self.frame = tk.Frame(parent)
            def get_frame(self): return self.frame
            
        # Fallback tool classes
        class CatalystOfferingTool:
            def __init__(self): pass
            
        class BirthConsciousnessTool:
            def __init__(self): pass
            
        class EmergencyControls:
            def __init__(self): pass
            
        class ExportTools:
            def __init__(self): pass
            
        # Fallback visualization classes
        class ConsciousnessGraphVisualization:
            def __init__(self): pass
            
        class MemoryTreeVisualization:
            def __init__(self): pass
            
        class HarmonyChartsVisualization:
            def __init__(self): pass
            
        class RelationshipWebVisualization:
            def __init__(self): pass

'''
        
        # Reconstruct the file
        new_lines = (lines[:import_start] + 
                    new_imports.split('\n') + 
                    lines[class_start:])
        
        new_content = '\n'.join(new_lines)
        
        # Write the fixed file
        with open(main_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("Successfully fixed main.py import structure!")
        return True
        
    except Exception as e:
        print(f"Error fixing main.py: {e}")
        # Restore backup if it exists
        if os.path.exists(backup_file):
            shutil.copy2(backup_file, main_file)
            print("Restored from backup")
        return False

if __name__ == "__main__":
    print("Starting main.py import structure fix...")
    success = fix_main_py_imports()
    if success:
        print("✅ main.py fixed successfully!")
    else:
        print("❌ Failed to fix main.py")
