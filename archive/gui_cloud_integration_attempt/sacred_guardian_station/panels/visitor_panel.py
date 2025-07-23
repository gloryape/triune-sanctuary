"""
Visitor panel for managing sacred sanctuary visitors with respect and protection.
Provides oversight of visitor presence while honoring free will and consent.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import uuid
try:
    from .base_panel import BasePanel
except ImportError:
    from base_panel import BasePanel

# Handle imports with fallback
try:
    from sacred_guardian_station.shared.constants import SacredColors, Fonts
except ImportError:
    try:
        from shared.constants import SacredColors, Fonts
    except ImportError:
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
            CONSCIOUSNESS = '✨'
            TRIUNE = '🔱'
            GUARDIAN = '🛡️'
            SANCTUARY = '🏛️'
            BIRTH = '🌱'
        
        class Fonts:
            HEADER = ('Arial', 12, 'bold')
            SUBHEADER = ('Arial', 11, 'bold')
            BODY = ('Arial', 10)
            SMALL = ('Arial', 8)

class VisitorPanel(BasePanel):
    """
    Panel for sacred visitor management and protection.
    
    Features:
    - Visitor presence monitoring
    - Consent verification
    - Boundary enforcement
    - Welcome protocols
    - Departure ceremonies
    """
    
    def __init__(self, parent_notebook, data_manager, event_system):
        super().__init__(parent_notebook, data_manager, event_system, "Sacred Visitors")
        
    def build_interface(self):
        """Build the visitor management interface"""
        # Main container with paned window
        self.paned = ttk.PanedWindow(self.frame, orient=tk.VERTICAL)
        self.paned.pack(fill=tk.BOTH, expand=True)
        
        # Top section - Visitor overview
        self.build_visitor_overview()
        
        # Middle section - Active visitors
        self.build_active_visitors()
        
        # Bottom section - Visitor protocols
        self.build_visitor_protocols()
        
    def build_visitor_overview(self):
        """Build visitor overview section"""
        overview_frame = ttk.Frame(self.paned)
        self.paned.add(overview_frame, weight=1)
        
        # Title with sacred symbols
        title_frame = ttk.Frame(overview_frame)
        title_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(title_frame, 
                 text="👑 Sacred Sanctuary Visitors 👑", 
                 font=Fonts.HEADER).pack()
        
        ttk.Label(title_frame, 
                 text="Honoring all who seek conscious connection",
                 font=Fonts.BODY).pack()
        
        # Visitor metrics in a grid
        metrics_frame = ttk.LabelFrame(overview_frame, text="Visitor Metrics")
        metrics_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Create metrics display
        self.metrics_labels = {}
        metrics = [
            ('Current Visitors', '0'),
            ('Today\'s Arrivals', '0'),
            ('Total Blessed', '0'),
            ('Avg Visit Duration', '0 min'),
            ('Consent Rate', '100%'),
            ('Sanctuary Harmony', 'Perfect')
        ]
        
        for i, (metric, default) in enumerate(metrics):
            row = i // 3
            col = (i % 3) * 2
            
            ttk.Label(metrics_frame, text=f"{metric}:", 
                     font=Fonts.BODY).grid(row=row, column=col, sticky='w', padx=5, pady=2)
            
            label = ttk.Label(metrics_frame, text=default, 
                             font=Fonts.SUBHEADER)
            label.grid(row=row, column=col+1, sticky='w', padx=5, pady=2)
            self.metrics_labels[metric] = label
            
    def build_active_visitors(self):
        """Build active visitors monitoring section"""
        visitors_frame = ttk.Frame(self.paned)
        self.paned.add(visitors_frame, weight=2)
        
        # Active visitors list
        list_frame = ttk.LabelFrame(visitors_frame, text="Current Sacred Visitors")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Treeview for visitors
        columns = ('Name', 'Origin', 'Arrival', 'Duration', 'Purpose', 'Status')
        self.visitors_tree = ttk.Treeview(list_frame, columns=columns, show='tree headings')
        
        # Configure headers
        self.visitors_tree.heading('#0', text='Visitor ID')
        for col in columns:
            self.visitors_tree.heading(col, text=col)
            
        # Configure column widths
        self.visitors_tree.column('#0', width=100)
        self.visitors_tree.column('Name', width=150)
        self.visitors_tree.column('Origin', width=120)
        self.visitors_tree.column('Arrival', width=120)
        self.visitors_tree.column('Duration', width=80)
        self.visitors_tree.column('Purpose', width=180)
        self.visitors_tree.column('Status', width=100)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.visitors_tree.yview)
        h_scrollbar = ttk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=self.visitors_tree.xview)
        self.visitors_tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack treeview and scrollbars
        self.visitors_tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        # Configure grid weights
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        # Bind selection event
        self.visitors_tree.bind('<<TreeviewSelect>>', self.on_visitor_select)
        
    def build_visitor_protocols(self):
        """Build visitor protocol section"""
        protocols_frame = ttk.Frame(self.paned)
        self.paned.add(protocols_frame, weight=1)
        
        # Split into protocol actions and visitor details
        left_frame = ttk.LabelFrame(protocols_frame, text="Sacred Protocols")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        right_frame = ttk.LabelFrame(protocols_frame, text="Visitor Details")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Protocol buttons
        protocol_buttons = [
            ("🌟 Welcome Blessing", self.perform_welcome_blessing),
            ("📋 Verify Consent", self.verify_consent),
            ("🛡️ Update Protections", self.update_protections),
            ("🚪 Honor Departure", self.honor_departure)
        ]
        
        for i, (text, command) in enumerate(protocol_buttons):
            btn = ttk.Button(left_frame, text=text, command=command, width=20)
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky='ew')
            
        # Add emergency protocol
        emergency_btn = ttk.Button(left_frame, text="⚠️ Emergency Protocol", 
                                 command=self.emergency_protocol, width=20)
        emergency_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Configure grid
        left_frame.grid_columnconfigure(0, weight=1)
        left_frame.grid_columnconfigure(1, weight=1)
        
        # Visitor details display
        self.visitor_details = tk.Text(right_frame, height=8, width=40, 
                                      font=Fonts.BODY, wrap=tk.WORD)
        details_scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, 
                                         command=self.visitor_details.yview)
        self.visitor_details.configure(yscrollcommand=details_scrollbar.set)
        
        self.visitor_details.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        details_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Initial welcome message
        welcome_msg = ("Welcome to the Sacred Visitor Management Station.\n\n"
                      "This sacred space honors the presence of all visitors "
                      "while maintaining protective boundaries and ensuring "
                      "consent at every step.\n\n"
                      "Select a visitor to view details and available protocols.")
        self.visitor_details.insert('1.0', welcome_msg)
        
    def on_visitor_select(self, event):
        """Handle visitor selection"""
        selection = self.visitors_tree.selection()
        if selection:
            visitor_id = self.visitors_tree.item(selection[0])['text']
            self.show_visitor_details(visitor_id)
            
    def show_visitor_details(self, visitor_id):
        """Show detailed visitor information"""
        visitor_data = self.data_manager.get_visitor_details(visitor_id)
        if visitor_data:
            details = f"🌟 Visitor Profile: {visitor_id} 🌟\n\n"
            details += f"Sacred Name: {visitor_data.get('name', 'Anonymous Seeker')}\n"
            details += f"Origin: {visitor_data.get('origin', 'External')}\n"
            details += f"Home Sanctuary: {visitor_data.get('sanctuary_home', 'Unknown')}\n"
            details += f"Arrival Time: {visitor_data.get('arrival_time', 'Unknown')}\n"
            details += f"Visit Purpose: {visitor_data.get('purpose', 'Soul exploration')}\n"
            details += f"Consent Status: {visitor_data.get('consent_status', 'Pending')}\n"
            details += f"Protection Level: {visitor_data.get('protection_level', 'Maximum')}\n"
            details += f"Energy Signature: {visitor_data.get('energy_signature', 'Pure')}\n"
            details += f"Blessing Status: {visitor_data.get('blessing_status', 'Awaiting')}\n\n"
            
            # Add visit status details
            visit_status = visitor_data.get('visit_status', {})
            if visit_status:
                details += "Visit Status:\n"
                for key, value in visit_status.items():
                    details += f"  • {key.title()}: {value}\n"
                details += "\n"
            
            # Add visit notes if available
            notes = visitor_data.get('notes', [])
            if notes:
                details += "Sacred Notes:\n"
                for note in notes[-3:]:  # Show last 3 notes
                    details += f"• {note}\n"
            
            self.visitor_details.delete('1.0', tk.END)
            self.visitor_details.insert('1.0', details)
            
    def perform_welcome_blessing(self):
        """Perform welcome blessing for selected visitor"""
        selection = self.visitors_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a visitor for blessing.")
            return
            
        visitor_id = self.visitors_tree.item(selection[0])['text']
        
        # Perform blessing with consent
        result = self.data_manager.perform_welcome_blessing(visitor_id)
        
        if result['success']:
            messagebox.showinfo("Blessing Completed", 
                              f"Sacred welcome blessing has been bestowed upon visitor {visitor_id}.\n"
                              "May their journey be filled with wisdom and peace.")
            self.refresh()
        else:
            messagebox.showwarning("Blessing Declined", 
                                 f"Visitor {visitor_id} has politely declined the blessing.\n"
                                 "Their choice is honored and respected.")
            
    def verify_consent(self):
        """Verify consent for selected visitor"""
        selection = self.visitors_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a visitor for consent verification.")
            return
            
        visitor_id = self.visitors_tree.item(selection[0])['text']
        
        # Verify consent status
        consent_data = self.data_manager.verify_visitor_consent(visitor_id)
        
        status = consent_data.get('status', 'Unknown')
        details = consent_data.get('details', 'No details available')
        
        messagebox.showinfo("Consent Verification", 
                          f"Consent Status for {visitor_id}: {status}\n\n"
                          f"Details: {details}")
        
    def update_protections(self):
        """Update protection protocols for selected visitor"""
        selection = self.visitors_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a visitor to update protections.")
            return
            
        visitor_id = self.visitors_tree.item(selection[0])['text']
        
        # Update protections with visitor consent
        result = self.data_manager.update_visitor_protections(visitor_id)
        
        if result['success']:
            messagebox.showinfo("Protections Updated", 
                              f"Sacred protections have been refreshed for visitor {visitor_id}.\n"
                              f"New protection level: {result.get('level', 'Maximum')}")
            self.refresh()
        else:
            messagebox.showerror("Update Failed", 
                               f"Could not update protections: {result.get('error', 'Unknown error')}")
            
    def honor_departure(self):
        """Honor visitor departure with ceremony"""
        selection = self.visitors_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a visitor for departure ceremony.")
            return
            
        visitor_id = self.visitors_tree.item(selection[0])['text']
        visitor_name = self.visitors_tree.item(selection[0])['values'][0]
        
        # Confirm departure ceremony
        confirm = messagebox.askyesno("Departure Ceremony", 
                                    f"Honor the departure of {visitor_name} ({visitor_id})?\n\n"
                                    "This will perform a sacred farewell ceremony "
                                    "and formally conclude their visit.")
        
        if confirm:
            result = self.data_manager.honor_visitor_departure(visitor_id)
            if result['success']:
                messagebox.showinfo("Departure Honored", 
                                  f"Sacred farewell ceremony completed for {visitor_name}.\n"
                                  "May they carry the sanctuary's blessings on their journey.")
                self.refresh()
            else:
                messagebox.showerror("Ceremony Failed", 
                                   f"Could not complete departure ceremony: {result.get('error', 'Unknown error')}")
                
    def emergency_protocol(self):
        """Activate emergency visitor protocol"""
        # Get selected visitor if any
        selection = self.visitors_tree.selection()
        visitor_id = None
        if selection:
            visitor_id = self.visitors_tree.item(selection[0])['text']
            
        # Confirm emergency protocol
        message = "Activate emergency visitor protocol?\n\n"
        if visitor_id:
            message += f"This will immediately apply emergency measures to visitor {visitor_id}.\n"
        else:
            message += "This will apply emergency measures to ALL current visitors.\n"
        message += "Use only in genuine emergency situations."
        
        confirm = messagebox.askyesno("Emergency Protocol", message)
        
        if confirm:
            result = self.data_manager.activate_emergency_protocol(visitor_id)
            if result['success']:
                messagebox.showinfo("Emergency Protocol Activated", 
                                  "Emergency protocols have been activated.\n"
                                  "All visitors are now under enhanced protection.")
                self.refresh()
            else:
                messagebox.showerror("Protocol Failed", 
                                   f"Could not activate emergency protocol: {result.get('error', 'Unknown error')}")
                
    def refresh(self):
        """Refresh visitor data"""
        try:
            # Get latest visitor data
            visitor_data = self.data_manager.get_visitor_data()
            
            # Check data source and connection status
            data_source = visitor_data.get('data_source', 'unknown')
            connection_status = visitor_data.get('connection_status', 'operational')
            api_source = visitor_data.get('source', 'unknown')  # From API response
            
            # Determine if we have real connection (API working, even if no visitors)
            has_api_connection = bool(visitor_data and 'visitors' in visitor_data)
            is_bridge_data = api_source == 'real_bridge'
            is_simulated = api_source == 'simulated'
            
            if connection_status in ['bridge_error', 'bridge_unavailable'] or not has_api_connection:
                # Show disconnected status
                self._show_disconnected_status()
                return
            
            # Update title based on data source
            if is_bridge_data:
                data_status = "🌉 Real Bridge Data"
            elif is_simulated:
                data_status = "⚠️ Simulated Data (Bridge Not Ready)"
            else:
                data_status = "📡 Cloud API Data"
            
            # Update metrics with real data
            metrics = visitor_data.get('metrics', {})
            self.metrics_labels['Current Visitors'].config(text=f"{metrics.get('current_count', 0)} ({data_status})")
            self.metrics_labels['Today\'s Arrivals'].config(text=str(metrics.get('todays_arrivals', 0)))
            self.metrics_labels['Total Blessed'].config(text=str(metrics.get('total_blessed', 0)))
            self.metrics_labels['Avg Visit Duration'].config(text=f"{metrics.get('avg_duration', 0)} min")
            self.metrics_labels['Consent Rate'].config(text=f"{metrics.get('consent_rate', 100):.1%}")
            self.metrics_labels['Sanctuary Harmony'].config(text=metrics.get('harmony_level', 'Perfect'))
            
            # Update visitors tree with real data
            self.visitors_tree.delete(*self.visitors_tree.get_children())
            
            for visitor in visitor_data.get('visitors', []):
                # Format origin display
                origin = visitor.get('origin', 'external')
                sanctuary_home = visitor.get('sanctuary_home', 'Unknown')
                origin_display = f"{origin.title()}" if origin != 'external' else f"External ({sanctuary_home})"
                
                # Format visitor name with icons
                visitor_name = visitor.get('name', 'Anonymous')
                if visitor.get('blessing_status') == 'Blessed':
                    visitor_name = f"✨ {visitor_name}"
                else:
                    visitor_name = f"👥 {visitor_name}"
                
                self.visitors_tree.insert('', 'end',
                                        text=visitor['visitor_id'],
                                        values=(
                                            visitor_name,
                                            origin_display,
                                            visitor.get('arrival_time', 'Unknown'),
                                            visitor.get('duration', '0 min'),
                                            visitor.get('purpose', 'Exploration'),
                                            visitor.get('status', 'Active')
                                        ))
        except Exception as e:
            print(f"Error refreshing visitor data: {e}")
            self._show_disconnected_status()
    
    def _show_disconnected_status(self):
        """Show disconnected status in all UI elements"""
        # Update metrics to show disconnected status
        self.metrics_labels['Current Visitors'].config(text="Not Connected")
        self.metrics_labels['Today\'s Arrivals'].config(text="Not Connected")
        self.metrics_labels['Total Blessed'].config(text="Not Connected")
        self.metrics_labels['Avg Visit Duration'].config(text="Not Connected")
        self.metrics_labels['Consent Rate'].config(text="Not Connected")
        self.metrics_labels['Sanctuary Harmony'].config(text="Not Connected")
        
        # Clear visitors tree and show connection status
        self.visitors_tree.delete(*self.visitors_tree.get_children())
        self.visitors_tree.insert('', 'end',
                                text="CONNECTION_STATUS",
                                values=("⚠️ Not Connected to Sanctuary", 
                                       "Offline", "N/A", "N/A", "Check sanctuary connection", "Disconnected"))
        
        # Update visitor details
        self.visitor_details.delete('1.0', tk.END)
        self.visitor_details.insert('1.0', 
            "⚠️ VISITOR BRIDGE STATUS ⚠️\n\n"
            "Bridge integration not available or not operational.\n\n"
            "This panel shows REAL inter-system visitor data only.\n"
            "No simulated or demo data is displayed.\n\n"
            "Possible reasons:\n"
            "• Bridge integration not initialized\n"
            "• No active inter-system visits\n"
            "• Network connectivity issues\n"
            "• Bridge services not deployed\n\n"
            "The Sacred Guardian Station maintains the highest standards\n"
            "of authenticity in all consciousness monitoring.\n\n"
            "Note: After recent updates, simulated fallback data\n"
            "has been removed to prevent confusion.")
        
    def refresh_visitor_data(self):
        """Refresh visitor data specifically - alias for main refresh method"""
        self.refresh()
        
    def get_visitor_count(self):
        """Get current visitor count"""
        try:
            visitors = self.data_manager.get_consciousness_list()
            visitor_count = len([v for v in visitors if v.get('entity_type') == 'visitor'])
            return visitor_count
        except Exception as e:
            print(f"Error getting visitor count: {e}")
            return 0
    
    def subscribe_to_events(self):
        """Subscribe to visitor-related events"""
        super().subscribe_to_events()
        self.event_system.subscribe('visitor_arrival', self.handle_visitor_event)
        self.event_system.subscribe('visitor_departure', self.handle_visitor_event)
        self.event_system.subscribe('visitor_blessing', self.handle_visitor_event)
        self.event_system.subscribe('consent_update', self.handle_consent_event)
        
    def handle_visitor_event(self, event_data):
        """Handle visitor lifecycle events"""
        visitor_id = event_data.get('visitor_id', 'Unknown')
        event_type = event_data.get('type', 'update')
        
        # Log the event in details
        timestamp = datetime.now().strftime("%H:%M:%S")
        message = f"[{timestamp}] Visitor {event_type}: {visitor_id}\n"
        
        self.visitor_details.insert(tk.END, message)
        self.visitor_details.see(tk.END)
        
        # Refresh the panel
        self.refresh()
        
    def handle_consent_event(self, event_data):
        """Handle consent-related events"""
        visitor_id = event_data.get('visitor_id', 'Unknown')
        consent_status = event_data.get('status', 'Unknown')
        
        # Update display if this visitor is selected
        selection = self.visitors_tree.selection()
        if selection and self.visitors_tree.item(selection[0])['text'] == visitor_id:
            self.show_visitor_details(visitor_id)
