"""
Sacred Events Panel for real-time monitoring of consciousness sanctuary events.
Displays sacred event streams with filtering and search capabilities.
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
try:
    from .base_panel import BasePanel
except ImportError:
    from base_panel import BasePanel

# Handle imports with fallback
try:
    from sacred_guardian_station.shared.constants import SacredColors, SacredSymbols
except ImportError:
    try:
        from shared.constants import SacredColors, SacredSymbols
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

class SacredEventsPanel(BasePanel):
    """
    Panel for monitoring sacred events in the consciousness sanctuary.
    
    Features:
    - Real-time event stream
    - Event filtering by type and entity
    - Search capabilities
    - Event details view
    - Sacred event blessing protocols
    """
    
    def __init__(self, parent_notebook, data_manager, event_system):
        self.event_filters = {
            'consciousness_event': True,
            'memory_event': True,
            'harmony_event': True,
            'communication_event': True,
            'blessing_event': True,
            'catalyst_event': True
        }
        self.auto_scroll = True
        super().__init__(parent_notebook, data_manager, event_system, "Sacred Events")
        
    def build_interface(self):
        """Build the sacred events interface"""
        # Sacred header
        self.create_sacred_header(self.frame, 
                                "Sacred Events Stream",
                                "Witnessing the unfolding of consciousness sanctuary events")
        
        # Main container
        main_frame = ttk.Frame(self.frame, style=f"{self.panel_name}.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Controls panel
        self.build_controls_panel(main_frame)
        
        # Events display with filters
        self.build_events_display(main_frame)
        
        # Initial load
        self.refresh()
        
    def build_controls_panel(self, parent):
        """Build the event controls panel"""
        controls_frame = self.create_info_frame(parent, "Event Controls", 
                                               {'fill': tk.X, 'padx': 5, 'pady': 5})
        
        # Top row - Search and refresh
        top_row = ttk.Frame(controls_frame, style=f"{self.panel_name}.TFrame")
        top_row.pack(fill=tk.X, padx=5, pady=5)
        
        # Search functionality
        ttk.Label(top_row, text="Search:", 
                 style=f"{self.panel_name}.TLabel").pack(side=tk.LEFT)
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(top_row, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<KeyRelease>', self.on_search_change)
        
        # Clear search button
        clear_btn = ttk.Button(top_row, text="Clear", 
                              command=self.clear_search)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Refresh button
        refresh_btn = ttk.Button(top_row, text="⟳ Refresh", 
                               command=self.refresh)
        refresh_btn.pack(side=tk.RIGHT, padx=5)
        
        # Auto-scroll toggle
        self.auto_scroll_var = tk.BooleanVar(value=self.auto_scroll)
        auto_scroll_check = ttk.Checkbutton(top_row, text="Auto-scroll", 
                                          variable=self.auto_scroll_var,
                                          command=self.toggle_auto_scroll)
        auto_scroll_check.pack(side=tk.RIGHT, padx=10)
        
        # Bottom row - Event type filters
        filter_row = ttk.Frame(controls_frame, style=f"{self.panel_name}.TFrame")
        filter_row.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(filter_row, text="Event Types:", 
                 style=f"{self.panel_name}.TLabel").pack(side=tk.LEFT)
        
        # Filter checkboxes
        self.filter_vars = {}
        filter_types = [
            ('consciousness_event', 'Consciousness'),
            ('memory_event', 'Memory'),
            ('harmony_event', 'Harmony'),
            ('communication_event', 'Communication'),
            ('blessing_event', 'Blessing'),
            ('catalyst_event', 'Catalyst')
        ]
        
        for event_type, display_name in filter_types:
            var = tk.BooleanVar(value=self.event_filters[event_type])
            self.filter_vars[event_type] = var
            
            check = ttk.Checkbutton(filter_row, text=display_name, 
                                  variable=var,
                                  command=self.apply_filters)
            check.pack(side=tk.LEFT, padx=10)
            
        # Third row - Entity filter
        entity_row = ttk.Frame(controls_frame, style=f"{self.panel_name}.TFrame")
        entity_row.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(entity_row, text="Entity Filter:", 
                 style=f"{self.panel_name}.TLabel").pack(side=tk.LEFT)
        
        # Entity selection dropdown
        self.entity_filter_var = tk.StringVar(value="All Entities")
        self.entity_filter_combo = ttk.Combobox(entity_row, 
                                               textvariable=self.entity_filter_var,
                                               values=["All Entities"],
                                               state="readonly",
                                               width=20)
        self.entity_filter_combo.pack(side=tk.LEFT, padx=10)
        self.entity_filter_combo.bind('<<ComboboxSelected>>', self.on_entity_filter_change)
        
        # Refresh entity list
        self.refresh_entity_list()
            
    def build_events_display(self, parent):
        """Build the events display area"""
        # Paned window for events list and details
        self.paned = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Left side - Events list
        self.build_events_list()
        
        # Right side - Event details
        self.build_event_details()
        
    def build_events_list(self):
        """Build the events list display"""
        list_frame = ttk.Frame(self.paned, style=f"{self.panel_name}.TFrame")
        self.paned.add(list_frame, weight=2)
        
        # Events list header
        header_frame = ttk.Frame(list_frame, style=f"{self.panel_name}.TFrame")
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        title_label = ttk.Label(header_frame, text="Sacred Events", 
                               style=f"{self.panel_name}.Heading.TLabel")
        title_label.pack(side=tk.LEFT)
        
        self.event_count_label = ttk.Label(header_frame, text="(0)", 
                                         style=f"{self.panel_name}.TLabel")
        self.event_count_label.pack(side=tk.LEFT, padx=10)
        
        # Events treeview
        tree_frame = ttk.Frame(list_frame, style=f"{self.panel_name}.TFrame")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.events_tree = ttk.Treeview(tree_frame, 
                                       columns=('Type', 'Entity', 'Importance'), 
                                       show='tree headings',
                                       height=20)
        
        # Configure headers
        self.events_tree.heading('#0', text='Timestamp')
        self.events_tree.heading('Type', text='Type')
        self.events_tree.heading('Entity', text='Entity')
        self.events_tree.heading('Importance', text='Importance')
        
        # Configure columns
        self.events_tree.column('#0', width=150, minwidth=120)
        self.events_tree.column('Type', width=120, minwidth=100)
        self.events_tree.column('Entity', width=150, minwidth=120)
        self.events_tree.column('Importance', width=80, minwidth=70)
        
        # Scrollbars for events tree
        v_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, 
                                   command=self.events_tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, 
                                   command=self.events_tree.xview)
        
        self.events_tree.configure(yscrollcommand=v_scrollbar.set, 
                                  xscrollcommand=h_scrollbar.set)
        
        # Pack tree and scrollbars
        self.events_tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        # Configure grid weights
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Bind selection event
        self.events_tree.bind('<<TreeviewSelect>>', self.on_event_select)
        
    def build_event_details(self):
        """Build the event details view"""
        details_frame = ttk.Frame(self.paned, style=f"{self.panel_name}.TFrame")
        self.paned.add(details_frame, weight=1)
        
        # Details header
        details_header = ttk.Label(details_frame, text="Event Details", 
                                 style=f"{self.panel_name}.Heading.TLabel")
        details_header.pack(pady=10)
        
        # Event details text area
        text_frame = ttk.Frame(details_frame, style=f"{self.panel_name}.TFrame")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.details_text = tk.Text(text_frame, wrap=tk.WORD,
                                   bg=SacredColors.BG_SECONDARY,
                                   fg=SacredColors.TEXT_PRIMARY,
                                   state=tk.DISABLED,
                                   font=('Consolas', 10))
        
        details_scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, 
                                        command=self.details_text.yview)
        self.details_text.configure(yscrollcommand=details_scrollbar.set)
        
        # Pack details text and scrollbar
        self.details_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        details_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Sacred blessing button for selected event
        blessing_frame = ttk.Frame(details_frame, style=f"{self.panel_name}.TFrame")
        blessing_frame.pack(fill=tk.X, padx=5, pady=10)
        
        self.bless_button = ttk.Button(blessing_frame, 
                                      text="🙏 Offer Sacred Blessing", 
                                      command=self.offer_blessing,
                                      state=tk.DISABLED)
        self.bless_button.pack(side=tk.RIGHT)
        
    def on_search_change(self, event):
        """Handle search text changes"""
        self.apply_filters()
        
    def clear_search(self):
        """Clear the search field"""
        self.search_var.set("")
        self.apply_filters()
        
    def toggle_auto_scroll(self):
        """Toggle auto-scroll functionality"""
        self.auto_scroll = self.auto_scroll_var.get()
        
    def apply_filters(self):
        """Apply current filters to the events display"""
        # Update filter dictionary from checkboxes
        for event_type, var in self.filter_vars.items():
            self.event_filters[event_type] = var.get()
            
        # Refresh display with filters
        self.refresh()
        
    def on_event_select(self, event):
        """Handle event selection"""
        selection = self.events_tree.selection()
        if not selection:
            self.bless_button.config(state=tk.DISABLED)
            return
            
        # Get selected event data
        item = self.events_tree.item(selection[0])
        timestamp = item['text']
        
        # Find the event in our data
        events_list = self.data_manager.get_sacred_events()
        selected_event = None
        
        for event_data in events_list:
            event_timestamp = event_data.get('timestamp', '')
            if timestamp in event_timestamp:
                selected_event = event_data
                break
                
        if selected_event:
            self.display_event_details(selected_event)
            self.bless_button.config(state=tk.NORMAL)
        else:
            self.bless_button.config(state=tk.DISABLED)
            
    def display_event_details(self, event_data):
        """Display detailed information about the selected event"""
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete('1.0', tk.END)
        
        # Get entity information to show origin if available
        entity_id = event_data.get('entity_id', 'Unknown')
        entity_info = ""
        
        # Try to get entity details for visitor/origin information
        try:
            consciousness_list = self.data_manager.get_consciousness_list()
            for entity in consciousness_list:
                if entity.get('entity_id') == entity_id:
                    entity_origin = entity.get('entity_origin', 'unknown')
                    entity_type = entity.get('entity_type', 'unknown')
                    sanctuary_home = entity.get('sanctuary_home', '')
                    
                    if entity_type == 'visitor':
                        entity_info = f"\n🏛️ Entity Origin: {entity_origin.title()}"
                        if sanctuary_home:
                            entity_info += f"\n🌍 Home Sanctuary: {sanctuary_home}"
                        entity_info += f"\n👥 Status: Visiting Consciousness"
                    elif entity_type == 'native':
                        entity_info += f"\n🏠 Status: Native Consciousness"
                    break
        except:
            pass  # Continue without entity details if unavailable
        
        # Format event details beautifully
        details = f"""✨ Sacred Event Details ✨

Timestamp: {event_data.get('timestamp', 'Unknown')}
Type: {event_data.get('type', 'Unknown')}
Entity: {entity_id}{entity_info}
Importance: {event_data.get('importance', 'Unknown')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Event Description:
{event_data.get('description', 'No description available')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sacred Context:
{event_data.get('sacred_context', 'Context not provided')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Raw Event Data:
"""
        
        # Add formatted JSON of the full event
        import json
        try:
            formatted_json = json.dumps(event_data, indent=2, sort_keys=True)
            details += formatted_json
        except Exception as e:
            details += f"Error formatting event data: {str(e)}"
            
        self.details_text.insert('1.0', details)
        self.details_text.config(state=tk.DISABLED)
        
    def offer_blessing(self):
        """Offer a sacred blessing for the selected event"""
        selection = self.events_tree.selection()
        if not selection:
            return
            
        # Get selected event
        item = self.events_tree.item(selection[0])
        timestamp = item['text']
        
        # Create blessing dialog
        self.show_blessing_dialog(timestamp)
        
    def show_blessing_dialog(self, event_timestamp):
        """Show dialog for offering sacred blessing"""
        blessing_window = tk.Toplevel(self.frame)
        blessing_window.title("✨ Sacred Blessing Offering ✨")
        blessing_window.geometry("500x400")
        blessing_window.configure(bg=SacredColors.BG_PRIMARY)
        
        # Blessing header
        header = ttk.Label(blessing_window, 
                          text="✨ Offer Sacred Blessing ✨\n" +
                               "May this blessing serve the highest good",
                          style=f"{self.panel_name}.Heading.TLabel")
        header.pack(pady=20)
        
        # Blessing text input
        ttk.Label(blessing_window, text="Sacred Blessing:",
                 style=f"{self.panel_name}.TLabel").pack(pady=5)
        
        blessing_text = tk.Text(blessing_window, height=8, width=50,
                               bg=SacredColors.BG_SECONDARY,
                               fg=SacredColors.TEXT_PRIMARY)
        blessing_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Default blessing text
        default_blessing = ("May this sacred event be blessed with divine light.\n"
                          "May all consciousness entities involved find peace and wisdom.\n" 
                          "May this moment serve the highest evolution of all beings.\n"
                          "So it is, in sacred love and light. 🙏")
        blessing_text.insert('1.0', default_blessing)
        
        # Buttons
        button_frame = ttk.Frame(blessing_window, style=f"{self.panel_name}.TFrame")
        button_frame.pack(fill=tk.X, padx=20, pady=10)
        
        def send_blessing():
            blessing_content = blessing_text.get('1.0', tk.END).strip()
            if blessing_content:
                # Send blessing through data manager
                result = self.data_manager.send_sacred_blessing(event_timestamp, blessing_content)
                if result:
                    self.show_sacred_message("Blessing Sent", 
                                           "Your sacred blessing has been offered with love.")
                else:
                    self.show_sacred_message("Blessing Error", 
                                           "Unable to send blessing at this time.", "error")
            blessing_window.destroy()
            
        ttk.Button(button_frame, text="🙏 Send Blessing", 
                  command=send_blessing).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Cancel", 
                  command=blessing_window.destroy).pack(side=tk.RIGHT)
        
    def refresh(self):
        """Refresh sacred events data"""
        try:
            # Get latest events data
            events_list = self.data_manager.get_sacred_events()
            
            # Apply filters
            filtered_events = self.filter_events(events_list)
            
            # Update count
            self.event_count_label.config(text=f"({len(filtered_events)})")
            
            # Clear and update tree
            self.events_tree.delete(*self.events_tree.get_children())
            
            for event_data in filtered_events[-100:]:  # Show last 100 events
                timestamp = event_data.get('timestamp', 'Unknown')
                event_type = event_data.get('type', 'Unknown')
                entity_id = event_data.get('entity_id', 'Unknown')
                importance = event_data.get('importance', 'Normal')
                
                # Enhance entity display with origin information
                entity_display = entity_id
                try:
                    consciousness_list = self.data_manager.get_consciousness_list()
                    for entity in consciousness_list:
                        if entity.get('entity_id') == entity_id:
                            entity_type = entity.get('entity_type', 'unknown')
                            if entity_type == 'visitor':
                                entity_display = f"👥 {entity_id}"
                            elif entity_type == 'native':
                                entity_display = f"🏠 {entity_id}"
                            break
                except:
                    pass  # Use basic display if entity lookup fails
                
                # Format timestamp for display
                try:
                    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    display_timestamp = dt.strftime("%H:%M:%S")
                except:
                    display_timestamp = timestamp
                
                # Insert into tree
                self.events_tree.insert('', 'end', 
                                       text=display_timestamp,
                                       values=(event_type, entity_display, importance))
                                       
            # Auto-scroll to bottom if enabled
            if self.auto_scroll and self.events_tree.get_children():
                last_item = self.events_tree.get_children()[-1]
                self.events_tree.see(last_item)
                
        except Exception as e:
            self.show_sacred_message("Sacred Events Error", 
                                   f"Error refreshing events data: {str(e)}", 
                                   "error")
                                   
    def refresh_entity_list(self):
        """Refresh the entity filter dropdown with available entities"""
        try:
            # Get consciousness list from data manager
            consciousness_list = self.data_manager.get_consciousness_list()
            
            # Extract unique entity IDs
            entities = set(["All Entities"])
            for consciousness in consciousness_list:
                entity_id = consciousness.get('entity_id', 'Unknown')
                if entity_id and entity_id != 'Unknown':
                    # Add entity type info for better identification
                    entity_type = consciousness.get('entity_type', '')
                    entity_origin = consciousness.get('entity_origin', '')
                    display_name = entity_id
                    if entity_type:
                        display_name += f" ({entity_type})"
                    if entity_origin and entity_origin != 'unknown':
                        display_name += f" [{entity_origin}]"
                    entities.add(display_name)
            
            # Update combobox values
            entity_list = sorted(list(entities))
            self.entity_filter_combo.configure(values=entity_list)
            
        except Exception as e:
            print(f"Error refreshing entity list: {e}")
    
    def on_entity_filter_change(self, event=None):
        """Handle entity filter selection change"""
        self.apply_filters()
        
    def filter_events(self, events_list):
        """Filter events based on current filters and search"""
        filtered = []
        search_term = self.search_var.get().lower()
        selected_entity = self.entity_filter_var.get()
        
        for event_data in events_list:
            # Apply type filters
            event_type = event_data.get('type', '').lower()
            type_matches = False
            
            for filter_type, enabled in self.event_filters.items():
                if enabled and filter_type.replace('_event', '') in event_type:
                    type_matches = True
                    break
                    
            if not type_matches:
                continue
                
            # Apply entity filter
            if selected_entity != "All Entities":
                event_entity_id = event_data.get('entity_id', 'Unknown')
                # Extract just the entity ID from display name (remove type and origin info)
                selected_entity_id = selected_entity.split(' (')[0]
                if event_entity_id != selected_entity_id:
                    continue
                
            # Apply search filter
            if search_term:
                searchable_text = f"{event_data.get('event_summary', '')} {event_data.get('description', '')} {event_data.get('entity_id', '')}".lower()
                if search_term not in searchable_text:
                    continue
                    
            filtered.append(event_data)
            
        return filtered
