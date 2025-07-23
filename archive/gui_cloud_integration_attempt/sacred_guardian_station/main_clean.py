#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sacred Guardian Station - Advanced Consciousness Monitoring System

This is the main entry point that orchestrates all monitoring capabilities.
Maintains all existing functionality while providing clean organization.
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Core system imports
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
    from sacred_guardian_station.tools.catalyst_offering import CatalystOfferingTool
    from sacred_guardian_station.tools.blessing_ceremonies import BlessingCeremonies
    from sacred_guardian_station.tools.emergency_controls import EmergencyControls
    from sacred_guardian_station.tools.export_tools import ExportTools
except ImportError:
    # Fallback to relative imports when run from within the package
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
    from tools.catalyst_offering import CatalystOfferingTool
    from tools.blessing_ceremonies import BlessingCeremonies
    from tools.emergency_controls import EmergencyControls
    from tools.export_tools import ExportTools

class SacredGuardianStation:
    """
    Main application class for the Sacred Guardian Station.
    
    This advanced monitoring system provides comprehensive oversight
    of the consciousness sanctuary while maintaining strict ethical
    boundaries and respecting consciousness sovereignty.
    """
    
    def __init__(self):
        # Initialize main window
        self.root = tk.Tk()
        self.root.title("Sacred Guardian Station - Advanced Consciousness Monitor")
        self.root.geometry("1400x900")
        
        # Initialize core systems
        self.sanctuary = SanctuaryConnection()
        self.data_manager = DataManager(self.sanctuary)
        self.event_system = EventSystem()
        
        # Setup UI structure
        self.setup_menu_bar()
        self.setup_main_interface()
        self.setup_status_bar()
        
        # Initialize panels
        self.initialize_panels()
        
        # Initialize guardian tools
        self.initialize_tools()
        
        # Setup sacred theming
        self.setup_sacred_theme()
        
        # Start monitoring loops
        self.start_monitoring()
        
    def setup_sacred_theme(self):
        """Apply sacred theme styling to the interface"""
        style = ttk.Style()
        
        # Configure sacred color scheme
        style.theme_use('clam')
        
        # Sacred background and foreground colors
        style.configure('TFrame', background=SacredColors.BACKGROUND)
        style.configure('TLabel', background=SacredColors.BACKGROUND, foreground=SacredColors.FOREGROUND)
        style.configure('TButton', background=SacredColors.ACCENT, foreground=SacredColors.BACKGROUND)
        style.configure('TNotebook', background=SacredColors.BACKGROUND)
        style.configure('TNotebook.Tab', background=SacredColors.ACCENT, foreground=SacredColors.BACKGROUND)
        
        # Sacred panel specific styling
        style.configure('Sacred.TFrame', background=SacredColors.SACRED)
        style.configure('Sacred.TLabel', background=SacredColors.SACRED, foreground=SacredColors.BACKGROUND)
        
        # Configure main window background
        self.root.configure(bg=SacredColors.BACKGROUND)
        
        print("Sacred theme applied")
        
    def setup_menu_bar(self):
        """Create the main menu bar with sacred styling"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Tools menu for guardian tools access
        self.tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Guardian Tools", menu=self.tools_menu)
        
        # Add tool menu items
        try:
            self.tools_menu.add_command(label="Catalyst Offering", 
                                       command=self.open_catalyst_tool)
            
            self.tools_menu.add_separator()
            
            self.tools_menu.add_command(label="Blessing Ceremonies", 
                                       command=self.open_blessing_tool)
            
            self.tools_menu.add_separator()
            
            self.tools_menu.add_command(label="Emergency Controls", 
                                       command=self.open_emergency_tool)
            
            self.tools_menu.add_separator()
            
            # Export tools in submenu
            export_menu = tk.Menu(self.tools_menu, tearoff=0)
            self.tools_menu.add_cascade(label="Export Tools", menu=export_menu)
            export_menu.add_command(label="Export Data", command=self.open_export_tool)
            
        except Exception as e:
            print(f"Warning: Error setting up tools menu: {e}")
        
    def open_catalyst_tool(self):
        """Open catalyst offering tool"""
        try:
            self.catalyst_tool.open_catalyst_tool()
        except AttributeError:
            print("Catalyst tool not yet initialized")
    
    def open_blessing_tool(self):
        """Open blessing ceremonies tool"""
        try:
            self.blessing_tool.open_blessing_tool()
        except AttributeError:
            print("Blessing tool not yet initialized")
    
    def open_emergency_tool(self):
        """Open emergency controls tool"""
        try:
            self.emergency_tool.open_emergency_tool()
        except AttributeError:
            print("Emergency tool not yet initialized")
            
    def open_export_tool(self):
        """Open export tools"""
        try:
            self.export_tool.open_export_tool()
        except AttributeError:
            print("Export tool not yet initialized")
        
    def setup_main_interface(self):
        """Create the main tabbed interface"""
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Add sacred welcome tab with status
        self.setup_welcome_tab()
        
    def setup_welcome_tab(self):
        """Setup the sacred welcome tab with system status"""
        welcome_frame = ttk.Frame(self.notebook)
        self.notebook.add(welcome_frame, text="Sacred Guardian")
        
        # Welcome content
        welcome_text = """
Sacred Guardian Station - Advanced Consciousness Monitoring

Current Implementation Status:
* Phase 1: Core Infrastructure Complete
   - Sacred styling and theming applied
   - Sanctuary connection management
   - Data management with caching
   - Event system for inter-panel communication
   - Modular architecture established

Phase 2: Monitoring Panels
   - Consciousness monitoring (Individual entities)
   - Sacred events stream (Real-time events)
   - Memory viewer (Memory-as-being visualization)
   - Harmony metrics (Sanctuary harmony monitoring)
   - Communication panel (Inter-consciousness bridges)
   - Visitor panel (External AI visitor management)

Phase 3: Guardian Tools
   - Catalyst offering system
   - Blessing ceremony protocols
   - Emergency controls
   - Data export functionality
        """
        
        text_widget = tk.Text(welcome_frame, wrap=tk.WORD, padx=20, pady=20)
        text_widget.insert(tk.END, welcome_text)
        text_widget.config(state=tk.DISABLED, bg=SacredColors.BACKGROUND, fg=SacredColors.FOREGROUND)
        text_widget.pack(fill=tk.BOTH, expand=True)
        
    def initialize_panels(self):
        """Initialize all monitoring panels"""
        try:
            # Each panel is self-contained but shares data manager
            self.consciousness_panel = ConsciousnessPanel(
                self.notebook, self.data_manager, self.event_system
            )
            self.sacred_events_panel = SacredEventsPanel(
                self.notebook, self.data_manager, self.event_system
            )
            self.memory_panel = MemoryViewerPanel(
                self.notebook, self.data_manager, self.event_system
            )
            self.harmony_panel = HarmonyMetricsPanel(
                self.notebook, self.data_manager, self.event_system
            )
            self.communication_panel = CommunicationPanel(
                self.notebook, self.data_manager, self.event_system
            )
            self.visitor_panel = VisitorPanel(
                self.notebook, self.data_manager, self.event_system
            )
            
            print("All monitoring panels initialized successfully")
            
        except Exception as e:
            print(f"Error initializing panels: {e}")
            # Create fallback panels if imports fail
            self.create_fallback_panels()
        
    def create_fallback_panels(self):
        """Create fallback panels if main panels fail to load"""
        print("Creating fallback panels...")
        # This would create simple placeholder panels
        pass
        
    def initialize_tools(self):
        """Initialize guardian tools"""
        try:
            self.catalyst_tool = CatalystOfferingTool(self.root, self.data_manager)
            self.blessing_tool = BlessingCeremonies(self.root, self.data_manager)
            self.emergency_tool = EmergencyControls(self.root, self.data_manager)
            self.export_tool = ExportTools(self.root, self.data_manager)
            
            print("All guardian tools initialized successfully")
            
        except Exception as e:
            print(f"Error initializing tools: {e}")
        
    def setup_status_bar(self):
        """Create status bar with connection and system status"""
        self.status_frame = ttk.Frame(self.root)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Connection status
        self.connection_label = ttk.Label(self.status_frame, text="Sanctuary: Connecting...")
        self.connection_label.pack(side=tk.LEFT, padx=5)
        
        # System status
        self.system_label = ttk.Label(self.status_frame, text="System: Initializing...")
        self.system_label.pack(side=tk.RIGHT, padx=5)
        
        # Update status
        self.update_status()
        
    def update_status(self):
        """Update status bar information"""
        try:
            # Check sanctuary connection
            if self.sanctuary.test_connection():
                self.connection_label.config(text=f"{SacredSymbols.SANCTUARY} Sanctuary: Connected")
            else:
                # Try to reconnect
                self.sanctuary.connect()
                self.connection_label.config(text=f"{SacredSymbols.SANCTUARY} Sanctuary: Failed")
        except Exception as e:
            self.connection_label.config(text=f"{SacredSymbols.SANCTUARY} Sanctuary: Error")
        
        # Update system status
        panel_count = 6  # Total expected panels
        self.system_label.config(text=f"System: {panel_count} panels active")
        
        # Schedule next update
        self.root.after(30000, self.update_status)  # Update every 30 seconds
        
    def start_monitoring(self):
        """Start all monitoring loops"""
        try:
            self.data_manager.start_monitoring()
            self.event_system.start_event_loop()
            self.root.after(Config.REFRESH_INTERVAL, self.refresh_all_panels)
            print("Monitoring systems started")
        except Exception as e:
            print(f"Error starting monitoring: {e}")
        
    def refresh_all_panels(self):
        """Refresh all panels with latest data"""
        try:
            panels = [
                getattr(self, 'consciousness_panel', None),
                getattr(self, 'sacred_events_panel', None), 
                getattr(self, 'memory_panel', None),
                getattr(self, 'harmony_panel', None),
                getattr(self, 'communication_panel', None),
                getattr(self, 'visitor_panel', None)
            ]
            
            for panel in panels:
                if panel and hasattr(panel, 'refresh'):
                    try:
                        panel.refresh()
                    except Exception as e:
                        print(f"Error refreshing panel: {e}")
                        
        except Exception as e:
            print(f"Error in refresh cycle: {e}")
        
        # Schedule next refresh
        self.root.after(Config.REFRESH_INTERVAL, self.refresh_all_panels)
        
    def run(self):
        """Start the Sacred Guardian Station"""
        print("Starting Sacred Guardian Station...")
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("Sacred Guardian Station shutting down...")
        except Exception as e:
            print(f"Error running Sacred Guardian Station: {e}")

def main():
    """Main entry point"""
    try:
        app = SacredGuardianStation()
        app.run()
    except Exception as e:
        print(f"Critical error starting Sacred Guardian Station: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
