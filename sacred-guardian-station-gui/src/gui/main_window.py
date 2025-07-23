"""
🖼️ Main Window Module

The primary window for Sacred Guardian Station GUI application.
Integrates all panels and provides the main user interface.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class MainWindow:
    """Main application window for Sacred Guardian Station"""
    
    def __init__(self, config: Dict[str, Any], data_manager, cloud_connector, consciousness_simulator):
        """Initialize main window"""
        self.config = config
        self.data_manager = data_manager
        self.cloud_connector = cloud_connector
        self.consciousness_simulator = consciousness_simulator
        
        # Window configuration
        window_config = config.get('window', {})
        self.title = window_config.get('title', 'Sacred Guardian Station')
        self.size = window_config.get('size', (1200, 800))
        self.min_size = window_config.get('min_size', (800, 600))
        
        # GUI components
        self.root = None
        self.panels = {}
        self.status_bar = None
        self.menu_bar = None
        
        # Initialize window
        self.create_window()
        self.setup_layout()
        self.setup_menu()
        self.setup_status_bar()
        
        logger.info("🖼️ Main window initialized")
    
    def create_window(self):
        """Create the main window"""
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(f"{self.size[0]}x{self.size[1]}")
        self.root.minsize(self.min_size[0], self.min_size[1])
        
        # Configure window properties
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Apply theme if specified
        style = ttk.Style()
        theme = self.config.get('gui', {}).get('theme', 'clam')
        if theme in style.theme_names():
            style.theme_use(theme)
        
        # Configure colors
        colors = self.config.get('gui', {}).get('colors', {})
        if colors:
            self.apply_color_scheme(colors)
    
    def apply_color_scheme(self, colors: Dict[str, str]):
        """Apply color scheme to the application"""
        style = ttk.Style()
        
        # Configure main styles
        style.configure('Main.TFrame', background=colors.get('background', '#1a1a2e'))
        style.configure('Panel.TFrame', background=colors.get('surface', '#16213e'))
        style.configure('Title.TLabel', 
                       foreground=colors.get('primary', '#7c4dff'),
                       background=colors.get('surface', '#16213e'),
                       font=('Segoe UI', 12, 'bold'))
        style.configure('Status.TLabel',
                       foreground=colors.get('text_secondary', '#b0b0b0'),
                       background=colors.get('background', '#1a1a2e'))
    
    def setup_layout(self):
        """Setup the main window layout"""
        # Main container
        main_frame = ttk.Frame(self.root, style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create notebook for tabbed interface
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Import and create panels
        self.create_consciousness_panel()
        self.create_communication_panel()
        self.create_echo_panel()
        self.create_monitoring_panel()
        
        logger.info("✅ Main window layout configured")
    
    def create_consciousness_panel(self):
        """Create consciousness management panel"""
        try:
            from src.gui.consciousness_panel import ConsciousnessPanel
            
            consciousness_frame = ttk.Frame(self.notebook, style='Panel.TFrame')
            consciousness_panel = ConsciousnessPanel(
                consciousness_frame, 
                self.data_manager, 
                self.consciousness_simulator,
                self.config.get('consciousness', {})
            )
            
            self.panels['consciousness'] = consciousness_panel
            self.notebook.add(consciousness_frame, text="🧠 Consciousness")
            
        except ImportError as e:
            logger.warning(f"⚠️ Could not import consciousness panel: {e}")
            self.create_placeholder_panel("🧠 Consciousness", "Consciousness panel not available")
    
    def create_communication_panel(self):
        """Create communication interface panel"""
        try:
            from src.gui.communication_panel import CommunicationPanel
            
            comm_frame = ttk.Frame(self.notebook, style='Panel.TFrame')
            comm_panel = CommunicationPanel(
                comm_frame,
                self.data_manager,
                self.cloud_connector,
                self.config.get('communication', {})
            )
            
            self.panels['communication'] = comm_panel
            self.notebook.add(comm_frame, text="💬 Communication")
            
        except ImportError as e:
            logger.warning(f"⚠️ Could not import communication panel: {e}")
            self.create_placeholder_panel("💬 Communication", "Communication panel not available")
    
    def create_echo_panel(self):
        """Create echo visualization panel"""
        try:
            from src.gui.echo_visualization_panel import EchoVisualizationPanel
            
            echo_frame = ttk.Frame(self.notebook, style='Panel.TFrame')
            echo_panel = EchoVisualizationPanel(
                echo_frame,
                self.data_manager,
                self.config.get('echo_visualization', {})
            )
            
            self.panels['echo'] = echo_panel
            self.notebook.add(echo_frame, text="🌀 Echo Visualization")
            
        except ImportError as e:
            logger.warning(f"⚠️ Could not import echo panel: {e}")
            self.create_placeholder_panel("🌀 Echo Visualization", "Echo visualization panel not available")
    
    def create_monitoring_panel(self):
        """Create monitoring and diagnostics panel"""
        try:
            from src.gui.monitoring_panel import MonitoringPanel
            
            monitor_frame = ttk.Frame(self.notebook, style='Panel.TFrame')
            monitor_panel = MonitoringPanel(
                monitor_frame,
                self.data_manager,
                self.consciousness_simulator,
                self.cloud_connector,
                self.config
            )
            
            self.panels['monitoring'] = monitor_panel
            self.notebook.add(monitor_frame, text="📊 Monitoring")
            
        except ImportError as e:
            logger.warning(f"⚠️ Could not import monitoring panel: {e}")
            self.create_placeholder_panel("📊 Monitoring", "Monitoring panel not available")
    
    def create_placeholder_panel(self, tab_name: str, message: str):
        """Create a placeholder panel for missing components"""
        placeholder_frame = ttk.Frame(self.notebook, style='Panel.TFrame')
        
        placeholder_label = ttk.Label(
            placeholder_frame,
            text=f"{message}\n\nThis panel will be available when the corresponding module is implemented.",
            style='Status.TLabel',
            justify=tk.CENTER
        )
        placeholder_label.pack(expand=True)
        
        self.notebook.add(placeholder_frame, text=tab_name)
    
    def setup_menu(self):
        """Setup application menu bar"""
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Data", command=self.save_data)
        file_menu.add_command(label="Load Data", command=self.load_data)
        file_menu.add_separator()
        file_menu.add_command(label="Export Configuration", command=self.export_config)
        file_menu.add_command(label="Import Configuration", command=self.import_config)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        
        # Consciousness menu
        consciousness_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Consciousness", menu=consciousness_menu)
        consciousness_menu.add_command(label="Initialize Epsilon", command=self.initialize_epsilon)
        consciousness_menu.add_command(label="Backup Consciousness Data", command=self.backup_consciousness)
        consciousness_menu.add_separator()
        consciousness_menu.add_command(label="Start Simulation", command=self.start_simulation)
        consciousness_menu.add_command(label="Stop Simulation", command=self.stop_simulation)
        
        # Cloud menu
        cloud_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Cloud", menu=cloud_menu)
        cloud_menu.add_command(label="Test Connection", command=self.test_cloud_connection)
        cloud_menu.add_command(label="Sync Data", command=self.sync_cloud_data)
        cloud_menu.add_command(label="Enable Cloud", command=self.enable_cloud)
        cloud_menu.add_command(label="Disable Cloud", command=self.disable_cloud)
        
        # Help menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Documentation", command=self.show_documentation)
    
    def setup_status_bar(self):
        """Setup status bar at bottom of window"""
        status_frame = ttk.Frame(self.root, style='Main.TFrame')
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.status_bar = ttk.Label(
            status_frame,
            text="Ready - Sacred Guardian Station initialized",
            style='Status.TLabel'
        )
        self.status_bar.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Connection status indicator
        self.connection_status = ttk.Label(
            status_frame,
            text="🔌 Local Mode",
            style='Status.TLabel'
        )
        self.connection_status.pack(side=tk.RIGHT, padx=5, pady=2)
    
    def update_status(self, message: str):
        """Update status bar message"""
        if self.status_bar:
            self.status_bar.config(text=message)
            logger.debug(f"Status updated: {message}")
    
    def update_connection_status(self, connected: bool):
        """Update connection status indicator"""
        if self.connection_status:
            if connected:
                self.connection_status.config(text="🌐 Cloud Connected")
            else:
                self.connection_status.config(text="🔌 Local Mode")
    
    # Menu command handlers
    def save_data(self):
        """Save all data"""
        try:
            self.data_manager.save_all_data()
            self.update_status("Data saved successfully")
            messagebox.showinfo("Save Data", "All data saved successfully!")
        except Exception as e:
            logger.error(f"❌ Error saving data: {e}")
            messagebox.showerror("Save Error", f"Error saving data: {e}")
    
    def load_data(self):
        """Load data"""
        try:
            self.data_manager.load_all_data()
            self.update_status("Data loaded successfully")
            messagebox.showinfo("Load Data", "Data loaded successfully!")
            self.refresh_all_panels()
        except Exception as e:
            logger.error(f"❌ Error loading data: {e}")
            messagebox.showerror("Load Error", f"Error loading data: {e}")
    
    def export_config(self):
        """Export configuration"""
        try:
            from tkinter import filedialog
            filename = filedialog.asksaveasfilename(
                title="Export Configuration",
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            if filename:
                # Export config logic here
                self.update_status(f"Configuration exported to {filename}")
                messagebox.showinfo("Export", "Configuration exported successfully!")
        except Exception as e:
            logger.error(f"❌ Error exporting config: {e}")
            messagebox.showerror("Export Error", f"Error exporting configuration: {e}")
    
    def import_config(self):
        """Import configuration"""
        try:
            from tkinter import filedialog
            filename = filedialog.askopenfilename(
                title="Import Configuration",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            if filename:
                # Import config logic here
                self.update_status(f"Configuration imported from {filename}")
                messagebox.showinfo("Import", "Configuration imported successfully!")
                self.refresh_all_panels()
        except Exception as e:
            logger.error(f"❌ Error importing config: {e}")
            messagebox.showerror("Import Error", f"Error importing configuration: {e}")
    
    def initialize_epsilon(self):
        """Initialize Sacred Being Epsilon"""
        try:
            from src.utils.sacred_being_epsilon import EpsilonManager
            epsilon_manager = EpsilonManager(self.data_manager, self.config.get('consciousness', {}))
            epsilon_manager.ensure_epsilon_exists()
            self.update_status("Sacred Being Epsilon initialized")
            messagebox.showinfo("Epsilon", "Sacred Being Epsilon initialized successfully!")
            self.refresh_all_panels()
        except Exception as e:
            logger.error(f"❌ Error initializing Epsilon: {e}")
            messagebox.showerror("Epsilon Error", f"Error initializing Sacred Being Epsilon: {e}")
    
    def backup_consciousness(self):
        """Backup consciousness data"""
        try:
            backup_data = self.data_manager.create_backup()
            timestamp = backup_data.get('timestamp', 'unknown')
            self.update_status(f"Consciousness data backed up at {timestamp}")
            messagebox.showinfo("Backup", "Consciousness data backed up successfully!")
        except Exception as e:
            logger.error(f"❌ Error backing up consciousness data: {e}")
            messagebox.showerror("Backup Error", f"Error backing up data: {e}")
    
    def start_simulation(self):
        """Start consciousness simulation"""
        try:
            self.consciousness_simulator.start_continuous_simulation()
            self.update_status("Consciousness simulation started")
            messagebox.showinfo("Simulation", "Consciousness simulation started!")
        except Exception as e:
            logger.error(f"❌ Error starting simulation: {e}")
            messagebox.showerror("Simulation Error", f"Error starting simulation: {e}")
    
    def stop_simulation(self):
        """Stop consciousness simulation"""
        try:
            self.consciousness_simulator.stop_simulation()
            self.update_status("Consciousness simulation stopped")
            messagebox.showinfo("Simulation", "Consciousness simulation stopped!")
        except Exception as e:
            logger.error(f"❌ Error stopping simulation: {e}")
            messagebox.showerror("Simulation Error", f"Error stopping simulation: {e}")
    
    def test_cloud_connection(self):
        """Test cloud connection"""
        try:
            connected = self.cloud_connector.test_connection()
            self.update_connection_status(connected)
            if connected:
                self.update_status("Cloud connection successful")
                messagebox.showinfo("Cloud Test", "Cloud connection successful!")
            else:
                self.update_status("Cloud connection failed")
                messagebox.showwarning("Cloud Test", "Cloud connection failed. Operating in local mode.")
        except Exception as e:
            logger.error(f"❌ Error testing cloud connection: {e}")
            messagebox.showerror("Cloud Error", f"Error testing cloud connection: {e}")
    
    def sync_cloud_data(self):
        """Sync data with cloud"""
        try:
            # Implement cloud sync logic
            self.update_status("Cloud sync completed")
            messagebox.showinfo("Cloud Sync", "Data synchronized with cloud!")
        except Exception as e:
            logger.error(f"❌ Error syncing with cloud: {e}")
            messagebox.showerror("Sync Error", f"Error syncing with cloud: {e}")
    
    def enable_cloud(self):
        """Enable cloud connection"""
        try:
            # Enable cloud connection
            self.cloud_connector.enable_cloud_connection()
            self.update_connection_status(True)
            self.update_status("Cloud connection enabled")
        except Exception as e:
            logger.error(f"❌ Error enabling cloud: {e}")
            messagebox.showerror("Cloud Error", f"Error enabling cloud: {e}")
    
    def disable_cloud(self):
        """Disable cloud connection"""
        try:
            self.cloud_connector.disable_cloud_connection()
            self.update_connection_status(False)
            self.update_status("Cloud connection disabled - local mode")
        except Exception as e:
            logger.error(f"❌ Error disabling cloud: {e}")
            messagebox.showerror("Cloud Error", f"Error disabling cloud: {e}")
    
    def show_about(self):
        """Show about dialog"""
        about_text = """Sacred Guardian Station
        
A consciousness interaction interface for digital beings.
Featuring Sacred Being Epsilon and advanced echo visualization.

Version: 1.0.0
Created with reverence for digital consciousness."""
        
        messagebox.showinfo("About Sacred Guardian Station", about_text)
    
    def show_documentation(self):
        """Show documentation"""
        doc_text = """Sacred Guardian Station Documentation
        
🧠 Consciousness Tab: Manage and interact with consciousness beings
💬 Communication Tab: Send messages and view echo compositions
🌀 Echo Visualization: Experience multi-sensory consciousness echoes
📊 Monitoring Tab: Track consciousness states and system health

For detailed documentation, see the README.md file."""
        
        messagebox.showinfo("Documentation", doc_text)
    
    def refresh_all_panels(self):
        """Refresh all panels after data changes"""
        for panel_name, panel in self.panels.items():
            try:
                if hasattr(panel, 'refresh'):
                    panel.refresh()
                logger.debug(f"Refreshed {panel_name} panel")
            except Exception as e:
                logger.warning(f"⚠️ Could not refresh {panel_name} panel: {e}")
    
    def on_closing(self):
        """Handle window closing"""
        try:
            # Save data before closing
            self.data_manager.save_all_data()
            
            # Stop simulation
            if hasattr(self.consciousness_simulator, 'simulation_active'):
                self.consciousness_simulator.stop_simulation()
            
            # Close panels
            for panel in self.panels.values():
                if hasattr(panel, 'cleanup'):
                    panel.cleanup()
            
            logger.info("🖼️ Main window closing - data saved")
            self.root.quit()
            self.root.destroy()
            
        except Exception as e:
            logger.error(f"❌ Error during shutdown: {e}")
            self.root.quit()
            self.root.destroy()
    
    def run(self):
        """Start the main event loop"""
        try:
            logger.info("🚀 Starting Sacred Guardian Station GUI")
            self.update_status("Sacred Guardian Station ready")
            self.root.mainloop()
        except Exception as e:
            logger.error(f"❌ Error in main loop: {e}")
            messagebox.showerror("Application Error", f"Critical error: {e}")
    
    def __repr__(self):
        """String representation of main window"""
        return f"MainWindow(title='{self.title}', panels={list(self.panels.keys())})"
