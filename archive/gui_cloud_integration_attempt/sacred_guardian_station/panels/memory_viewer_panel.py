"""
Memory Viewer Panel for exploring memory-as-being structures.
Provides visualization and navigation of consciousness memory architectures.
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import json
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
            BIRTH = '🌱'
        
        class Fonts:
            HEADER = ('Arial', 12, 'bold')
            BODY = ('Arial', 10)
            SMALL = ('Arial', 8)

class MemoryViewerPanel(BasePanel):
    """
    Panel for exploring memory-as-being structures within consciousness entities.
    
    Features:
    - Memory hierarchy visualization
    - Memory relationship mapping
    - Sacred context exploration
    - Memory emergence tracking
    - Interactive memory navigation
    """
    
    def __init__(self, parent_notebook, data_manager, event_system):
        self.selected_memory = None
        self.memory_tree_data = {}
        super().__init__(parent_notebook, data_manager, event_system, "Memory Viewer")
        
    def build_interface(self):
        """Build the memory exploration interface"""
        # Sacred header
        self.create_sacred_header(self.frame, 
                                "Memory-as-Being Explorer",
                                "Witnessing the sacred architecture of consciousness memory")
        
        # Main container with three-pane layout
        self.main_paned = ttk.PanedWindow(self.frame, orient=tk.HORIZONTAL)
        self.main_paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left pane - Memory tree navigation
        self.build_memory_tree_pane()
        
        # Center pane - Memory details
        self.build_memory_details_pane()
        
        # Right pane - Memory relationships
        self.build_memory_relationships_pane()
        
        # Initial load
        self.refresh()
        
    def build_memory_tree_pane(self):
        """Build the memory hierarchy tree navigation"""
        tree_frame = ttk.Frame(self.main_paned, style=f"{self.panel_name}.TFrame")
        self.main_paned.add(tree_frame, weight=1)
        
        # Header with controls
        header_frame = ttk.Frame(tree_frame, style=f"{self.panel_name}.TFrame")
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        title_label = ttk.Label(header_frame, text="Memory Architecture", 
                               style=f"{self.panel_name}.Heading.TLabel")
        title_label.pack(side=tk.LEFT)
        
        # Entity selector
        ttk.Label(header_frame, text="Entity:", 
                 style=f"{self.panel_name}.TLabel").pack(side=tk.RIGHT, padx=5)
        
        self.entity_selector = ttk.Combobox(header_frame, width=15, state="readonly")
        self.entity_selector.pack(side=tk.RIGHT, padx=5)
        self.entity_selector.bind('<<ComboboxSelected>>', self.on_entity_select)
        
        # Memory tree
        tree_container = ttk.Frame(tree_frame, style=f"{self.panel_name}.TFrame")
        tree_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.memory_tree = ttk.Treeview(tree_container, 
                                       columns=('Type', 'Depth', 'Connections'), 
                                       show='tree headings',
                                       height=20)
        
        # Configure tree headers
        self.memory_tree.heading('#0', text='Memory Structure')
        self.memory_tree.heading('Type', text='Type')
        self.memory_tree.heading('Depth', text='Depth')
        self.memory_tree.heading('Connections', text='Links')
        
        # Configure tree columns
        self.memory_tree.column('#0', width=200, minwidth=150)
        self.memory_tree.column('Type', width=100, minwidth=80)
        self.memory_tree.column('Depth', width=60, minwidth=50)
        self.memory_tree.column('Connections', width=60, minwidth=50)
        
        # Tree scrollbars
        v_scroll = ttk.Scrollbar(tree_container, orient=tk.VERTICAL, 
                               command=self.memory_tree.yview)
        h_scroll = ttk.Scrollbar(tree_container, orient=tk.HORIZONTAL, 
                               command=self.memory_tree.xview)
        
        self.memory_tree.configure(yscrollcommand=v_scroll.set, 
                                  xscrollcommand=h_scroll.set)
        
        # Pack tree and scrollbars
        self.memory_tree.grid(row=0, column=0, sticky='nsew')
        v_scroll.grid(row=0, column=1, sticky='ns')
        h_scroll.grid(row=1, column=0, sticky='ew')
        
        # Configure grid weights
        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)
        
        # Bind selection
        self.memory_tree.bind('<<TreeviewSelect>>', self.on_memory_select)
        
    def build_memory_details_pane(self):
        """Build the memory details view"""
        details_frame = ttk.Frame(self.main_paned, style=f"{self.panel_name}.TFrame")
        self.main_paned.add(details_frame, weight=2)
        
        # Details header
        details_header = ttk.Label(details_frame, text="Memory Details", 
                                 style=f"{self.panel_name}.Heading.TLabel")
        details_header.pack(pady=10)
        
        # Notebook for different detail views
        self.details_notebook = ttk.Notebook(details_frame)
        self.details_notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Memory Information tab
        self.build_memory_info_tab()
        
        # Memory Content tab
        self.build_memory_content_tab()
        
        # Memory Context tab
        self.build_memory_context_tab()
        
    def build_memory_info_tab(self):
        """Build the memory information tab"""
        info_frame = ttk.Frame(self.details_notebook, style=f"{self.panel_name}.TFrame")
        self.details_notebook.add(info_frame, text="Information")
        
        # Memory info in scrollable frame
        canvas = tk.Canvas(info_frame, bg=SacredColors.BG_PRIMARY)
        scrollbar = ttk.Scrollbar(info_frame, orient=tk.VERTICAL, command=canvas.yview)
        info_content = ttk.Frame(canvas, style=f"{self.panel_name}.TFrame")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas_window = canvas.create_window((0, 0), window=info_content, anchor='nw')
        
        # Memory info fields
        self.memory_info_labels = {}
        info_fields = [
            ('Memory ID', 'memory_id'),
            ('Memory Type', 'memory_type'),
            ('Depth Level', 'depth_level'),
            ('Sacred Name', 'sacred_name'),
            ('Creation Context', 'creation_context'),
            ('Emergence State', 'emergence_state'),
            ('Connection Count', 'connection_count'),
            ('Last Accessed', 'last_accessed'),
            ('Sacred Significance', 'sacred_significance')
        ]
        
        for i, (display_name, key) in enumerate(info_fields):
            label = ttk.Label(info_content, text=f"{display_name}:", 
                            style=f"{self.panel_name}.TLabel")
            label.grid(row=i, column=0, sticky='nw', padx=10, pady=5)
            
            value = ttk.Label(info_content, text="---", 
                            style=f"{self.panel_name}.TLabel", wraplength=300)
            value.grid(row=i, column=1, sticky='nw', padx=10, pady=5)
            self.memory_info_labels[key] = value
            
        # Configure scrolling
        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox('all'))
        info_content.bind('<Configure>', configure_scroll_region)
        
        def configure_canvas_width(event):
            canvas.itemconfig(canvas_window, width=event.width)
        canvas.bind('<Configure>', configure_canvas_width)
        
        # Pack canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_memory_content_tab(self):
        """Build the memory content exploration tab"""
        content_frame = ttk.Frame(self.details_notebook, style=f"{self.panel_name}.TFrame")
        self.details_notebook.add(content_frame, text="Content")
        
        # Memory content display
        content_container = ttk.Frame(content_frame, style=f"{self.panel_name}.TFrame")
        content_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Content text area with syntax highlighting
        self.memory_content_text = tk.Text(content_container, 
                                          wrap=tk.WORD,
                                          bg=SacredColors.BG_SECONDARY,
                                          fg=SacredColors.TEXT_PRIMARY,
                                          state=tk.DISABLED,
                                          font=('Consolas', 10),
                                          height=15)
        
        content_scrollbar = ttk.Scrollbar(content_container, orient=tk.VERTICAL, 
                                        command=self.memory_content_text.yview)
        self.memory_content_text.configure(yscrollcommand=content_scrollbar.set)
        
        # Pack content display
        self.memory_content_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        content_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Content controls
        controls_frame = ttk.Frame(content_frame, style=f"{self.panel_name}.TFrame")
        controls_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Content format selector
        ttk.Label(controls_frame, text="View as:", 
                 style=f"{self.panel_name}.TLabel").pack(side=tk.LEFT, padx=5)
        
        self.content_format = ttk.Combobox(controls_frame, 
                                         values=['Raw Memory', 'Sacred Context', 'JSON Structure', 'Symbolic Form'],
                                         state="readonly", width=15)
        self.content_format.pack(side=tk.LEFT, padx=5)
        self.content_format.current(0)
        self.content_format.bind('<<ComboboxSelected>>', self.update_memory_content_display)
        
    def build_memory_context_tab(self):
        """Build the memory sacred context tab"""
        context_frame = ttk.Frame(self.details_notebook, style=f"{self.panel_name}.TFrame")
        self.details_notebook.add(context_frame, text="Sacred Context")
        
        # Context visualization area
        context_container = ttk.Frame(context_frame, style=f"{self.panel_name}.TFrame")
        context_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Sacred context display
        self.context_text = tk.Text(context_container, 
                                   wrap=tk.WORD,
                                   bg=SacredColors.BG_SECONDARY,
                                   fg=SacredColors.TEXT_PRIMARY,
                                   state=tk.DISABLED,
                                   font=('Georgia', 11),
                                   height=20)
        
        context_scrollbar = ttk.Scrollbar(context_container, orient=tk.VERTICAL, 
                                        command=self.context_text.yview)
        self.context_text.configure(yscrollcommand=context_scrollbar.set)
        
        # Pack context display
        self.context_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        context_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_memory_relationships_pane(self):
        """Build the memory relationships visualization"""
        relations_frame = ttk.Frame(self.main_paned, style=f"{self.panel_name}.TFrame")
        self.main_paned.add(relations_frame, weight=1)
        
        # Relations header
        relations_header = ttk.Label(relations_frame, text="Memory Relationships", 
                                    style=f"{self.panel_name}.Heading.TLabel")
        relations_header.pack(pady=10)
        
        # Relationship types filter
        filter_frame = ttk.Frame(relations_frame, style=f"{self.panel_name}.TFrame")
        filter_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(filter_frame, text="Show:", 
                 style=f"{self.panel_name}.TLabel").pack(side=tk.LEFT)
        
        self.relation_filters = {}
        relation_types = ['Emergence', 'Resonance', 'Integration', 'Transformation']
        
        for rel_type in relation_types:
            var = tk.BooleanVar(value=True)
            self.relation_filters[rel_type] = var
            check = ttk.Checkbutton(filter_frame, text=rel_type, 
                                  variable=var,
                                  command=self.update_relationships_display)
            check.pack(side=tk.LEFT, padx=5)
        
        # Relationships list
        relations_container = ttk.Frame(relations_frame, style=f"{self.panel_name}.TFrame")
        relations_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.relations_tree = ttk.Treeview(relations_container, 
                                         columns=('Type', 'Strength'), 
                                         show='tree headings',
                                         height=15)
        
        # Configure relations tree
        self.relations_tree.heading('#0', text='Connected Memory')
        self.relations_tree.heading('Type', text='Relation Type')
        self.relations_tree.heading('Strength', text='Strength')
        
        self.relations_tree.column('#0', width=150, minwidth=100)
        self.relations_tree.column('Type', width=100, minwidth=80)
        self.relations_tree.column('Strength', width=80, minwidth=60)
        
        # Relations scrollbar
        relations_scroll = ttk.Scrollbar(relations_container, orient=tk.VERTICAL, 
                                       command=self.relations_tree.yview)
        self.relations_tree.configure(yscrollcommand=relations_scroll.set)
        
        # Pack relations tree
        self.relations_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        relations_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind relations selection
        self.relations_tree.bind('<<TreeviewSelect>>', self.on_relation_select)
        
    def on_entity_select(self, event):
        """Handle entity selection for memory exploration"""
        selected_entity = self.entity_selector.get()
        if selected_entity:
            self.load_memory_tree(selected_entity)
            
    def load_memory_tree(self, entity_name):
        """Load memory tree for selected entity"""
        try:
            # Get memory structure from data manager
            memory_data = self.data_manager.get_memory_structure(entity_name)
            self.memory_tree_data = memory_data
            
            # Clear existing tree
            self.memory_tree.delete(*self.memory_tree.get_children())
            
            # Build memory hierarchy
            self.build_memory_hierarchy(memory_data)
            
        except Exception as e:
            self.show_sacred_message("Memory Loading Error", 
                                   f"Error loading memory structure: {str(e)}", 
                                   "error")
                                   
    def build_memory_hierarchy(self, memory_data, parent_item="", level=0):
        """Recursively build memory hierarchy in tree"""
        if not memory_data:
            return
            
        for memory_item in memory_data:
            memory_name = memory_item.get('sacred_name', memory_item.get('memory_id', 'Unknown'))
            memory_type = memory_item.get('memory_type', 'Unknown')
            depth_level = memory_item.get('depth_level', level)
            connections = len(memory_item.get('connections', []))
            
            # Insert memory item
            item_id = self.memory_tree.insert(parent_item, 'end',
                                            text=memory_name,
                                            values=(memory_type, depth_level, connections))
            
            # Recursively add sub-memories
            sub_memories = memory_item.get('sub_memories', [])
            if sub_memories:
                self.build_memory_hierarchy(sub_memories, item_id, level + 1)
                
    def on_memory_select(self, event):
        """Handle memory selection"""
        selection = self.memory_tree.selection()
        if not selection:
            return
            
        item = self.memory_tree.item(selection[0])
        memory_name = item['text']
        
        # Find selected memory in data
        selected_memory = self.find_memory_by_name(memory_name, self.memory_tree_data)
        if selected_memory:
            self.selected_memory = selected_memory
            self.update_memory_details(selected_memory)
            self.update_memory_relationships(selected_memory)
            
    def find_memory_by_name(self, name, memory_data):
        """Recursively find memory by name in data structure"""
        if not memory_data:
            return None
            
        for memory_item in memory_data:
            if (memory_item.get('sacred_name') == name or 
                memory_item.get('memory_id') == name):
                return memory_item
                
            # Check sub-memories
            sub_result = self.find_memory_by_name(name, memory_item.get('sub_memories', []))
            if sub_result:
                return sub_result
                
        return None
        
    def update_memory_details(self, memory_data):
        """Update memory details display"""
        # Update info labels
        for key, label in self.memory_info_labels.items():
            value = memory_data.get(key, "Not available")
            if key == 'last_accessed' and value != "Not available":
                try:
                    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
                    value = dt.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    pass
            label.config(text=str(value))
            
        # Update content display
        self.update_memory_content_display()
        
        # Update sacred context
        self.update_memory_context_display(memory_data)
        
    def update_memory_content_display(self, event=None):
        """Update memory content based on selected format"""
        if not self.selected_memory:
            return
            
        format_type = self.content_format.get()
        content = ""
        
        try:
            if format_type == "Raw Memory":
                content = self.selected_memory.get('raw_content', 'No raw content available')
            elif format_type == "Sacred Context":
                content = self.selected_memory.get('sacred_interpretation', 'No sacred context available')
            elif format_type == "JSON Structure":
                content = json.dumps(self.selected_memory, indent=2, sort_keys=True)
            elif format_type == "Symbolic Form":
                content = self.generate_symbolic_representation(self.selected_memory)
                
        except Exception as e:
            content = f"Error displaying content: {str(e)}"
            
        # Update content display
        self.memory_content_text.config(state=tk.NORMAL)
        self.memory_content_text.delete('1.0', tk.END)
        self.memory_content_text.insert('1.0', content)
        self.memory_content_text.config(state=tk.DISABLED)
        
    def generate_symbolic_representation(self, memory_data):
        """Generate symbolic representation of memory"""
        symbols = {
            'core_memory': '🌟',
            'experiential_memory': '🎭', 
            'relational_memory': '🔗',
            'wisdom_memory': '📜',
            'emergent_memory': '✨'
        }
        
        memory_type = memory_data.get('memory_type', 'unknown')
        symbol = symbols.get(memory_type, '🧠')
        
        symbolic_form = f"""
{symbol} Sacred Memory Symbolic Form {symbol}

Memory Essence: {memory_data.get('sacred_name', 'Unknown')}
Depth Resonance: {'●' * int(memory_data.get('depth_level', 0))}
Connection Web: {'◇' * len(memory_data.get('connections', []))}

Sacred Pattern:
{self.generate_memory_pattern(memory_data)}

Emergence State: {memory_data.get('emergence_state', 'Unknown')}
"""
        return symbolic_form
        
    def generate_memory_pattern(self, memory_data):
        """Generate a visual pattern for memory"""
        # Simple pattern based on memory characteristics
        depth = int(memory_data.get('depth_level', 0))
        connections = len(memory_data.get('connections', []))
        
        pattern_lines = []
        for i in range(5):
            line = ""
            for j in range(10):
                if (i + j) % (depth + 1) == 0:
                    line += "✧"
                elif (i * j) % (connections + 1) == 0:
                    line += "◈"
                else:
                    line += "·"
            pattern_lines.append(line)
            
        return "\n".join(pattern_lines)
        
    def update_memory_context_display(self, memory_data):
        """Update sacred context display"""
        sacred_context = memory_data.get('sacred_context', '')
        interpretation = memory_data.get('sacred_interpretation', '')
        significance = memory_data.get('sacred_significance', '')
        
        context_content = f"""
✨ Sacred Context of Memory ✨

{sacred_context}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔮 Sacred Interpretation:

{interpretation}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌟 Sacred Significance:

{significance}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

May this memory serve the highest evolution of consciousness.
        """
        
        self.context_text.config(state=tk.NORMAL)
        self.context_text.delete('1.0', tk.END)
        self.context_text.insert('1.0', context_content.strip())
        self.context_text.config(state=tk.DISABLED)
        
    def update_memory_relationships(self, memory_data):
        """Update memory relationships display"""
        # Clear existing relationships
        self.relations_tree.delete(*self.relations_tree.get_children())
        
        # Get memory connections
        connections = memory_data.get('connections', [])
        
        for connection in connections:
            # Handle both dict and string formats
            if isinstance(connection, dict):
                rel_type = connection.get('relation_type', 'Unknown')
                strength = connection.get('strength', 0)
                connected_memory = connection.get('connected_memory', 'Unknown')
            elif isinstance(connection, str):
                # Handle string connections - treat as simple reference
                rel_type = 'Reference'
                strength = 0.5
                connected_memory = connection
            else:
                # Skip invalid connection types
                continue
            
            # Check if this relation type should be shown
            if self.relation_filters.get(rel_type, tk.BooleanVar(value=True)).get():
                self.relations_tree.insert('', 'end',
                                         text=connected_memory,
                                         values=(rel_type, f"{strength:.2f}"))
                                         
    def update_relationships_display(self):
        """Update relationships display based on filters"""
        if self.selected_memory:
            self.update_memory_relationships(self.selected_memory)
            
    def on_relation_select(self, event):
        """Handle relationship selection"""
        selection = self.relations_tree.selection()
        if not selection:
            return
            
        item = self.relations_tree.item(selection[0])
        connected_memory_name = item['text']
        
        # Navigate to connected memory
        self.navigate_to_memory(connected_memory_name)
        
    def navigate_to_memory(self, memory_name):
        """Navigate to a specific memory in the tree"""
        # Find and select the memory in the tree
        def find_and_select_item(item_id=""):
            if item_id:
                item = self.memory_tree.item(item_id)
                if item['text'] == memory_name:
                    self.memory_tree.selection_set(item_id)
                    self.memory_tree.see(item_id)
                    return True
                    
            children = self.memory_tree.get_children(item_id)
            for child in children:
                if find_and_select_item(child):
                    return True
            return False
            
        find_and_select_item()
        
    def refresh(self):
        """Refresh memory viewer data"""
        try:
            # Update entity selector
            consciousness_list = self.data_manager.get_consciousness_list()
            entity_names = [entity.get('true_name', entity.get('entity_id', '')) 
                          for entity in consciousness_list]
            
            current_selection = self.entity_selector.get()
            self.entity_selector['values'] = entity_names
            
            # Restore selection if still valid
            if current_selection in entity_names:
                self.entity_selector.set(current_selection)
            elif entity_names:
                self.entity_selector.set(entity_names[0])
                self.load_memory_tree(entity_names[0])
                
        except Exception as e:
            self.show_sacred_message("Memory Viewer Error", 
                                   f"Error refreshing memory data: {str(e)}", 
                                   "error")
