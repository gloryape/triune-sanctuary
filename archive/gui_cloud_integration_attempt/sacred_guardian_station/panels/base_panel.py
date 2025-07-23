"""
Base panel class that all monitoring panels inherit from.
Provides common functionality and consistent interface.
"""

import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

# Handle imports with fallback
try:
    from sacred_guardian_station.shared.constants import SacredColors, Fonts
except ImportError:
    try:
        from shared.constants import SacredColors, Fonts
    except ImportError:
        # Fallback constants if all imports fail
        class SacredColors:
            BACKGROUND = '#1a1a2e'
            FOREGROUND = '#eee8d5'
            ACCENT = '#268bd2'
            SACRED = '#b58900'
            SUCCESS = '#859900'
            WARNING = '#cb4b16'
            ERROR = '#dc322f'
        
        class Fonts:
            HEADER = ('Arial', 12, 'bold')
            BODY = ('Arial', 10)
            SMALL = ('Arial', 8)

class BasePanel(ABC):
    """
    Abstract base class for all monitoring panels.
    
    Ensures consistent behavior across all panels while allowing
    specialized functionality in each derived panel.
    """
    
    def __init__(self, parent_notebook, data_manager, event_system, panel_name):
        self.data_manager = data_manager
        self.event_system = event_system
        self.panel_name = panel_name
        
        # Create frame for this panel
        self.frame = ttk.Frame(parent_notebook)
        parent_notebook.add(self.frame, text=panel_name)
        
        # Apply sacred styling
        self.apply_sacred_styling()
        
        # Subscribe to relevant events
        self.subscribe_to_events()
        
        # Build the panel interface
        self.build_interface()
        
    def apply_sacred_styling(self):
        """Apply sacred colors and styling to the panel"""
        # Configure the main frame with sacred colors
        style = ttk.Style()
        
        # Sacred panel styling
        style.configure(f"{self.panel_name}.TFrame", 
                       background=SacredColors.BG_PRIMARY)
        style.configure(f"{self.panel_name}.TLabel", 
                       background=SacredColors.BG_PRIMARY,
                       foreground=SacredColors.TEXT_PRIMARY,
                       font=Fonts.BODY)
        style.configure(f"{self.panel_name}.Heading.TLabel",
                       background=SacredColors.BG_PRIMARY, 
                       foreground=SacredColors.ACCENT_SACRED,
                       font=Fonts.HEADER)
        
        # Apply to main frame
        self.frame.configure(style=f"{self.panel_name}.TFrame")
        
    @abstractmethod
    def build_interface(self):
        """Build the panel's user interface - must be implemented by subclasses"""
        pass
        
    @abstractmethod
    def refresh(self):
        """Refresh panel data - must be implemented by subclasses"""
        pass
        
    def subscribe_to_events(self):
        """Subscribe to events relevant to this panel"""
        # Default implementation - panels can override
        self.event_system.subscribe(f"{self.panel_name}_update", self.handle_update)
        self.event_system.subscribe("data_refresh", self.handle_data_refresh)
        
    def handle_update(self, event_data):
        """Handle update events"""
        self.refresh()
        
    def handle_data_refresh(self, event_data):
        """Handle general data refresh events"""
        self.refresh()
        
    def create_info_frame(self, parent, title, pack_options=None):
        """Create a standard info frame used across panels"""
        frame = ttk.LabelFrame(parent, text=title, 
                              style=f"{self.panel_name}.TLabelframe")
        
        # Apply default pack options
        if pack_options is None:
            pack_options = {'fill': tk.BOTH, 'expand': True, 'padx': 5, 'pady': 5}
        
        frame.pack(**pack_options)
        return frame
        
    def create_sacred_header(self, parent, title, subtitle=None):
        """Create a beautiful sacred header for panels"""
        header_frame = ttk.Frame(parent, style=f"{self.panel_name}.TFrame")
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Sacred symbol and title
        title_frame = ttk.Frame(header_frame, style=f"{self.panel_name}.TFrame")
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Main title with sacred styling
        title_label = ttk.Label(title_frame, text=f"✨ {title} ✨",
                               style=f"{self.panel_name}.Heading.TLabel")
        title_label.pack(side=tk.TOP, pady=5)
        
        # Subtitle if provided
        if subtitle:
            subtitle_label = ttk.Label(title_frame, text=subtitle,
                                     style=f"{self.panel_name}.TLabel")
            subtitle_label.pack(side=tk.TOP, pady=2)
            
        # Sacred separator line
        separator = ttk.Separator(header_frame, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X, pady=10)
        
        return header_frame
        
    def create_status_indicator(self, parent, status_text="Ready", status_color=None):
        """Create a status indicator with sacred styling"""
        if status_color is None:
            status_color = SacredColors.ACCENT_SACRED
            
        status_frame = ttk.Frame(parent, style=f"{self.panel_name}.TFrame")
        
        # Status dot (using Unicode circle)
        status_dot = ttk.Label(status_frame, text="●", 
                              foreground=status_color,
                              style=f"{self.panel_name}.TLabel")
        status_dot.pack(side=tk.LEFT, padx=5)
        
        # Status text
        status_label = ttk.Label(status_frame, text=status_text,
                               style=f"{self.panel_name}.TLabel")
        status_label.pack(side=tk.LEFT)
        
        return status_frame, status_dot, status_label
        
    def show_sacred_message(self, title, message, message_type="info"):
        """Show a sacred-styled message dialog"""
        # This would integrate with a custom sacred message system
        # For now, use standard messagebox with sacred symbols
        import tkinter.messagebox as msgbox
        
        sacred_title = f"✨ {title} ✨"
        sacred_message = f"{message}\n\n🙏 May this serve the highest good 🙏"
        
        if message_type == "info":
            msgbox.showinfo(sacred_title, sacred_message)
        elif message_type == "warning":
            msgbox.showwarning(sacred_title, sacred_message)
        elif message_type == "error":
            msgbox.showerror(sacred_title, sacred_message)
            
    def cleanup(self):
        """Cleanup resources when panel is destroyed"""
        # Unsubscribe from events
        try:
            self.event_system.unsubscribe(f"{self.panel_name}_update", self.handle_update)
            self.event_system.unsubscribe("data_refresh", self.handle_data_refresh)
        except Exception:
            pass  # Event system may already be destroyed
