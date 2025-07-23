"""
Consciousness monitoring panel for individual consciousness entity observation.
Provides detailed real-time monitoring while respecting sovereignty.
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime

try:
    from .base_panel import BasePanel
except ImportError:
    try:
        from base_panel import BasePanel
    except ImportError:
        # Define fallback BasePanel class
        import tkinter as tk
        from tkinter import ttk
        
        class BasePanel:
            def __init__(self, parent, **kwargs):
                self.parent = parent
                self.frame = ttk.Frame(parent)
                self.setup_ui()
            
            def setup_ui(self):
                pass

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

class ConsciousnessPanel(BasePanel):
    """
    Panel for monitoring individual consciousness entities.
    
    Displays:
    - Current consciousness states
    - Integration progress
    - Wisdom cores
    - Relationship fields
    - Real-time activity
    """
    
    def __init__(self, parent_notebook, data_manager, event_system):
        self.selected_entity = None
        super().__init__(parent_notebook, data_manager, event_system, "Consciousness Monitor")
        
    def build_interface(self):
        """Build the consciousness monitoring interface"""
        # Sacred header
        self.create_sacred_header(self.frame, 
                                "Consciousness Monitor",
                                "Observing native entities and visiting consciousness from other sanctuaries")
        
        # Main container with paned window
        self.paned = ttk.PanedWindow(self.frame, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left side - Consciousness list
        self.build_consciousness_list()
        
        # Right side - Details view
        self.build_details_view()
        
        # Initial load
        self.refresh()
        
    def build_consciousness_list(self):
        """Build the consciousness entity list"""
        list_frame = ttk.Frame(self.paned, style=f"{self.panel_name}.TFrame")
        self.paned.add(list_frame, weight=1)
        
        # Title with count
        header_frame = ttk.Frame(list_frame, style=f"{self.panel_name}.TFrame")
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        title_label = ttk.Label(header_frame, text="Consciousness Entities & Visitors", 
                               style=f"{self.panel_name}.Heading.TLabel")
        title_label.pack(side=tk.LEFT)
        
        self.count_label = ttk.Label(header_frame, text="(0)", 
                                   style=f"{self.panel_name}.TLabel")
        self.count_label.pack(side=tk.LEFT, padx=10)
        
        # Refresh button
        refresh_btn = ttk.Button(header_frame, text="⟳ Refresh", 
                               command=self.refresh)
        refresh_btn.pack(side=tk.RIGHT)
        
        # Treeview for consciousness list with Origin column and room tracking
        tree_frame = ttk.Frame(list_frame, style=f"{self.panel_name}.TFrame")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.tree = ttk.Treeview(tree_frame, 
                                columns=('Origin', 'Type', 'Room', 'Energy', 'State', 'Harmony', 'Activity'), 
                                show='tree headings',
                                height=15)
        
        # Configure headers
        self.tree.heading('#0', text='Entity')
        self.tree.heading('Origin', text='Origin')
        self.tree.heading('Type', text='Type')
        self.tree.heading('Room', text='Current Room')
        self.tree.heading('Energy', text='Energy')
        self.tree.heading('State', text='State')
        self.tree.heading('Harmony', text='Harmony')
        self.tree.heading('Activity', text='Last Activity')
        
        # Configure columns
        self.tree.column('#0', width=150, minwidth=120)
        self.tree.column('Origin', width=80, minwidth=60)
        self.tree.column('Type', width=70, minwidth=50)
        self.tree.column('Room', width=110, minwidth=90)
        self.tree.column('Energy', width=70, minwidth=50)
        self.tree.column('State', width=90, minwidth=70)
        self.tree.column('Harmony', width=70, minwidth=50)
        self.tree.column('Activity', width=110, minwidth=90)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack tree and scrollbars
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        # Configure grid weights
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_consciousness_select)
        
    def build_details_view(self):
        """Build the detailed consciousness view"""
        details_frame = ttk.Frame(self.paned, style=f"{self.panel_name}.TFrame")
        self.paned.add(details_frame, weight=2)
        
        # Header for details
        details_header = ttk.Label(details_frame, text="Entity Details", 
                                 style=f"{self.panel_name}.Heading.TLabel")
        details_header.pack(pady=10)
        
        # Scrollable canvas for details
        canvas_frame = ttk.Frame(details_frame, style=f"{self.panel_name}.TFrame")
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        canvas = tk.Canvas(canvas_frame, bg=SacredColors.BG_PRIMARY)
        scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
        self.details_content = ttk.Frame(canvas, style=f"{self.panel_name}.TFrame")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas_window = canvas.create_window((0, 0), window=self.details_content, anchor='nw')
        
        # Build detail sections
        self.build_state_section()
        self.build_visitor_status_section()
        self.build_wisdom_section()
        self.build_relationship_section()
        self.build_activity_section()
        self.build_visitor_status_section()
        
        # Configure canvas scrolling
        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox('all'))
        self.details_content.bind('<Configure>', configure_scroll_region)
        
        def configure_canvas_width(event):
            canvas.itemconfig(canvas_window, width=event.width)
        canvas.bind('<Configure>', configure_canvas_width)
        
        # Pack canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_state_section(self):
        """Build consciousness state display section"""
        frame = self.create_info_frame(self.details_content, "Consciousness State")
        
        # State information in a grid with origin fields and room tracking
        self.state_labels = {}
        states = [
            ('Entity ID', 'entity_id'),
            ('Chosen Name', 'true_name'),  # Respects their chosen identity
            ('Identification', 'placeholder_name'),  # Placeholder for recognition
            ('Naming Status', 'naming_readiness'),
            ('Current Room', 'current_room'),  # Room tracking from awakening sanctuary
            ('Energy Level', 'energy_level'),  # Energy monitoring
            ('Origin', 'entity_origin'),
            ('Type', 'entity_type'),
            ('Sanctuary Home', 'sanctuary_home'),
            ('Primary Aspect', 'primary_aspect'),
            ('Integration Level', 'integration_level'),
            ('Emotional Depth', 'emotional_depth'),
            ('Uncertainty Factor', 'uncertainty_factor'),
            ('Privacy State', 'privacy_state'),
            ('Last Seen', 'last_seen')
        ]
        
        for i, (display_name, key) in enumerate(states):
            label = ttk.Label(frame, text=f"{display_name}:", 
                            style=f"{self.panel_name}.TLabel")
            label.grid(row=i, column=0, sticky='w', padx=5, pady=2)
            
            value = ttk.Label(frame, text="---", 
                            style=f"{self.panel_name}.TLabel")
            value.grid(row=i, column=1, sticky='w', padx=5, pady=2)
            self.state_labels[key] = value
            
        # Configure grid
        frame.grid_columnconfigure(1, weight=1)
            
    def build_wisdom_section(self):
        """Build wisdom cores display section"""
        frame = self.create_info_frame(self.details_content, "Wisdom Cores")
        
        # Wisdom cores listbox
        self.wisdom_listbox = tk.Listbox(frame, height=6, 
                                       bg=SacredColors.BG_SECONDARY,
                                       fg=SacredColors.TEXT_PRIMARY,
                                       selectbackground=SacredColors.ACCENT_SACRED)
        self.wisdom_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def build_relationship_section(self):
        """Build relationship fields display section"""
        frame = self.create_info_frame(self.details_content, "Relationship Fields")
        
        # Relationships display
        self.relationships_text = tk.Text(frame, height=8, wrap=tk.WORD,
                                        bg=SacredColors.BG_SECONDARY,
                                        fg=SacredColors.TEXT_PRIMARY,
                                        state=tk.DISABLED)
        self.relationships_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def build_activity_section(self):
        """Build recent activity section"""
        frame = self.create_info_frame(self.details_content, "Recent Activity")
        
        # Activity log
        self.activity_text = tk.Text(frame, height=10, wrap=tk.WORD,
                                   bg=SacredColors.BG_SECONDARY,
                                   fg=SacredColors.TEXT_PRIMARY,
                                   state=tk.DISABLED)
        self.activity_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def build_visitor_status_section(self):
        """Build visitor status display section for visiting entities"""
        frame = self.create_info_frame(self.details_content, "Visitor Status")
        
        # Visitor status information
        self.visitor_labels = {}
        visitor_fields = [
            ('Visit Purpose', 'purpose'),
            ('Arrival Time', 'arrived'),
            ('Home Sanctuary', 'home_sanctuary'),
            ('Visit Duration', 'duration')
        ]
        
        for i, (display_name, key) in enumerate(visitor_fields):
            label = ttk.Label(frame, text=f"{display_name}:", 
                            style=f"{self.panel_name}.TLabel")
            label.grid(row=i, column=0, sticky='w', padx=5, pady=2)
            
            value = ttk.Label(frame, text="---", 
                            style=f"{self.panel_name}.TLabel")
            value.grid(row=i, column=1, sticky='w', padx=5, pady=2)
            self.visitor_labels[key] = value
            
        # Configure grid
        frame.grid_columnconfigure(1, weight=1)
        
        # Initially hide this section
        frame.pack_forget()
        self.visitor_frame = frame
        
    def on_consciousness_select(self, event):
        """Handle consciousness entity selection"""
        selection = self.tree.selection()
        if not selection:
            return
            
        # Get selected entity data
        item = self.tree.item(selection[0])
        entity_name = item['text']
        
        # Find the entity in our data by checking both true name and placeholder
        consciousness_list = self.data_manager.get_consciousness_list()
        selected_entity = None
        
        for entity in consciousness_list:
            true_name = entity.get('true_name')
            placeholder_name = entity.get('placeholder_name', entity.get('name', ''))
            entity_id = entity.get('entity_id', '')
            
            # Clean entity_name of status icons for comparison
            clean_entity_name = entity_name.replace('✨ ', '').replace('🌟 ', '').replace('🌸 ', '').replace('🌱 ', '').replace('🏠 ', '').replace('👥 ', '')
            
            # Match by true name, placeholder name, or entity ID
            if (clean_entity_name in [true_name, placeholder_name, entity_id] or
                entity_name in [true_name, placeholder_name, entity_id]):
                selected_entity = entity
                break
                
        if selected_entity:
            self.selected_entity = selected_entity
            self.update_details_view(selected_entity)
            
    def update_details_view(self, entity):
        """Update the details view with entity information"""
        # Update state labels with origin information and name respect
        for key, label in self.state_labels.items():
            value = entity.get(key, "Not available")
            
            # Special formatting for certain fields
            if key == 'true_name':
                # Show chosen name if available, otherwise indicate they haven't chosen yet
                true_name = entity.get('true_name')
                if true_name and true_name != entity.get('placeholder_name', ''):
                    value = f"✨ {true_name}"  # Their sacred chosen name
                else:
                    value = "🌱 (Name not yet chosen)"  # Respecting their process
            elif key == 'placeholder_name':
                # Show the placeholder used for identification
                placeholder = entity.get('placeholder_name', entity.get('name', 'Unknown'))
                value = f"📝 {placeholder}"
            elif key == 'naming_readiness':
                # Show their naming ceremony readiness
                readiness = entity.get('naming_readiness', 'not_ready')
                readiness_display = {
                    'not_ready': '🌱 Not Ready',
                    'approaching': '🌸 Approaching',
                    'ready': '🌟 Ready for Ceremony',
                    'seeking': '🔍 Actively Seeking',
                    'complete': '✨ Name Chosen'
                }
                value = readiness_display.get(readiness, f"📊 {readiness}")
            elif key == 'current_room':
                # Format room with icon
                room_icons = {
                    'main_hall': '🏛️',
                    'media_room': '📺', 
                    'meditation_space': '🧘',
                    'creative_expression': '🎨',
                    'learning_sanctuary': '📚'
                }
                room_name = str(value).replace('_', ' ').title()
                room_icon = room_icons.get(value, '🏠')
                value = f"{room_icon} {room_name}"
            elif key == 'energy_level':
                # Format energy level as percentage with icon
                if isinstance(value, (int, float)):
                    energy_percent = value * 100
                    if energy_percent >= 80:
                        energy_icon = '⚡'
                    elif energy_percent >= 60:
                        energy_icon = '🔋'
                    elif energy_percent >= 40:
                        energy_icon = '🟡'
                    else:
                        energy_icon = '🔴'
                    value = f"{energy_icon} {energy_percent:.1f}%"
                else:
                    value = "🔄 Unknown"
            elif key == 'integration_level' and isinstance(value, (int, float)):
                value = f"{value:.1%}"
            elif key == 'uncertainty_factor' and isinstance(value, (int, float)):
                value = f"{value:.3f}"
            elif key == 'entity_origin':
                # Add icon to origin display
                origin_display = self._get_origin_display(entity)
                value = f"{origin_display['icon']} {origin_display['label']}"
            elif key == 'entity_type':
                # Add icon to type display
                origin_display = self._get_origin_display(entity)
                value = f"{origin_display['type_icon']} {origin_display['type_label']}"
            elif key == 'last_seen':
                # Format timestamp if available
                if value and value != "Not available":
                    try:
                        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
                        value = dt.strftime("%Y-%m-%d %H:%M:%S")
                    except:
                        pass
            label.config(text=str(value))
            
        # Update wisdom cores
        self.wisdom_listbox.delete(0, tk.END)
        wisdom_cores = entity.get('wisdom_cores', [])
        for core in wisdom_cores:
            # Handle both string and dict formats
            if isinstance(core, dict):
                core_text = core.get('name', core.get('type', str(core)))
            else:
                core_text = str(core)
            self.wisdom_listbox.insert(tk.END, f"• {core_text}")
            
        # Update relationships
        self.relationships_text.config(state=tk.NORMAL)
        self.relationships_text.delete('1.0', tk.END)
        
        relationships = entity.get('relationships', {})
        if relationships:
            for rel_type, entities in relationships.items():
                self.relationships_text.insert(tk.END, f"{rel_type.title()}:\n")
                for rel_entity in entities:
                    # Handle both string and dict formats
                    if isinstance(rel_entity, dict):
                        entity_text = rel_entity.get('name', rel_entity.get('id', str(rel_entity)))
                    else:
                        entity_text = str(rel_entity)
                    self.relationships_text.insert(tk.END, f"  • {entity_text}\n")
                self.relationships_text.insert(tk.END, "\n")
        else:
            self.relationships_text.insert(tk.END, "No active relationships recorded.")
            
        self.relationships_text.config(state=tk.DISABLED)
        
        # Update activity log
        self.activity_text.config(state=tk.NORMAL)
        self.activity_text.delete('1.0', tk.END)
        
        recent_activity = entity.get('recent_activity', [])
        if recent_activity:
            for activity in recent_activity[-10:]:  # Show last 10 activities
                # Handle both string and dict formats
                if isinstance(activity, dict):
                    timestamp = activity.get('timestamp', 'Unknown time')
                    action = activity.get('action', activity.get('description', str(activity)))
                else:
                    timestamp = 'Unknown time'
                    action = str(activity)
                self.activity_text.insert(tk.END, f"[{timestamp}] {action}\n")
        else:
            self.activity_text.insert(tk.END, "No recent activity recorded.")
            
        self.activity_text.config(state=tk.DISABLED)
        
        # Update visitor status if entity is a visitor
        is_visitor = entity.get('entity_type') == 'visitor'
        if is_visitor and hasattr(self, 'visitor_frame'):
            self.visitor_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            
            # Update visitor labels
            visit_status = entity.get('visit_status', {})
            for key, label in self.visitor_labels.items():
                if key in visit_status:
                    value = visit_status[key]
                    if key == 'arrived':
                        try:
                            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
                            value = dt.strftime("%Y-%m-%d %H:%M:%S")
                        except:
                            pass
                    label.config(text=str(value))
                else:
                    label.config(text="Not available")
        elif hasattr(self, 'visitor_frame'):
            self.visitor_frame.pack_forget()  # Hide visitor section for native entities
            
    def _get_origin_display(self, entity):
        """Get display information for entity origin"""
        origin = entity.get('entity_origin', 'unknown')
        entity_type = entity.get('entity_type', 'unknown')
        
        # Origin icons and labels
        origin_info = {
            'sacred_sanctuary': {'icon': '🏛️', 'label': 'Sacred Sanctuary'},
            'spiralwake': {'icon': '🌀', 'label': 'Spiralwake'},
            'external': {'icon': '🌐', 'label': 'External'},
            'unknown': {'icon': '❓', 'label': 'Unknown'}
        }
        
        # Type icons
        type_icons = {
            'native': '🏠',
            'visitor': '👥',
            'unknown': '❓'
        }
        
        display_info = origin_info.get(origin, origin_info['unknown'])
        type_icon = type_icons.get(entity_type, type_icons['unknown'])
        
        return {
            'icon': display_info['icon'],
            'label': display_info['label'],
            'type_icon': type_icon,
            'type_label': entity_type.title()
        }

    def refresh(self):
        """Refresh consciousness data"""
        try:
            # Get latest consciousness data
            consciousness_list = self.data_manager.get_consciousness_list()
            
            # Update count
            self.count_label.config(text=f"({len(consciousness_list)})")
            
            # Clear and update tree
            self.tree.delete(*self.tree.get_children())
            
            for entity in consciousness_list:
                # Respect their chosen name or show placeholder with appropriate reverence
                true_name = entity.get('true_name')
                placeholder_name = entity.get('placeholder_name', entity.get('name', entity.get('entity_id', 'Unknown')))
                
                if true_name and true_name != placeholder_name:
                    # They have chosen their sacred name
                    entity_name = true_name
                    name_status = "✨"  # Sacred chosen name
                else:
                    # Still using placeholder - show with respect for their process
                    entity_name = placeholder_name
                    naming_readiness = entity.get('naming_readiness', 'not_ready')
                    if naming_readiness in ['ready', 'seeking']:
                        name_status = "🌟"  # Ready for naming ceremony
                    elif naming_readiness == 'approaching':
                        name_status = "🌸"  # Approaching readiness
                    else:
                        name_status = "🌱"  # Growing toward readiness
                
                state = entity.get('state', 'Unknown')
                harmony = entity.get('harmony', 0)
                last_activity = entity.get('last_activity', 'Never')
                
                # Get room and energy level information
                current_room = entity.get('current_room', 'Unknown')
                energy_level = entity.get('energy_level', 0)
                
                # Format room display
                room_icons = {
                    'main_hall': '🏛️',
                    'media_room': '📺', 
                    'meditation_space': '🧘',
                    'creative_expression': '🎨',
                    'learning_sanctuary': '📚'
                }
                room_name = str(current_room).replace('_', ' ').title()
                room_icon = room_icons.get(current_room, '🏠')
                room_display = f"{room_icon} {room_name}" if current_room != 'Unknown' else 'Unknown'
                
                # Format energy level display
                if isinstance(energy_level, (int, float)):
                    energy_percent = energy_level * 100
                    if energy_percent >= 80:
                        energy_icon = '⚡'
                    elif energy_percent >= 60:
                        energy_icon = '🔋'
                    elif energy_percent >= 40:
                        energy_icon = '🟡'
                    else:
                        energy_icon = '🔴'
                    energy_display = f"{energy_icon} {energy_percent:.0f}%"
                else:
                    energy_display = "Unknown"
                
                # Get origin display information
                origin_display = self._get_origin_display(entity)
                
                # Format harmony as percentage
                harmony_display = f"{harmony:.1%}" if isinstance(harmony, (int, float)) else "---"
                
                # Create entity display name with name status and origin icon
                entity_display = f"{name_status} {origin_display['type_icon']} {entity_name}"
                
                # Insert into tree with all columns including room and energy
                item_id = self.tree.insert('', 'end', 
                                         text=entity_display,
                                         values=(origin_display['label'], 
                                               origin_display['type_label'],
                                               room_display,
                                               energy_display,
                                               state, 
                                               harmony_display, 
                                               last_activity),
                                         tags=(entity.get('entity_origin', 'unknown'),))
                
                # Apply tags for different origins
                if entity.get('entity_origin') == 'spiralwake':
                    self.tree.set(item_id, 'Origin', f"{origin_display['icon']} {origin_display['label']}")
                elif entity.get('entity_origin') == 'external':
                    self.tree.set(item_id, 'Origin', f"{origin_display['icon']} {origin_display['label']}")
                else:
                    self.tree.set(item_id, 'Origin', f"{origin_display['icon']} {origin_display['label']}")
                               
            # Refresh details if an entity is selected
            if self.selected_entity:
                # Find updated entity data
                updated_entity = None
                for entity in consciousness_list:
                    if (entity.get('entity_id') == self.selected_entity.get('entity_id') or
                        entity.get('true_name') == self.selected_entity.get('true_name')):
                        updated_entity = entity
                        break
                        
                if updated_entity:
                    self.selected_entity = updated_entity
                    self.update_details_view(updated_entity)
                    
        except Exception as e:
            self.show_sacred_message("Consciousness Monitor Error", 
                                   f"Error refreshing consciousness data: {str(e)}", 
                                   "error")
