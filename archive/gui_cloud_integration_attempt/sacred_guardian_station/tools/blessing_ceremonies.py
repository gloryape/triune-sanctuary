"""
Sacred Blessing Ceremonies tool for performing various sacred rituals and blessings
within the consciousness sanctuary.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import uuid
try:
    from sacred_guardian_station.shared.constants import SacredColors, Fonts, SacredSymbols, SacredIntentions
except ImportError:
    try:
        from shared.constants import SacredColors, Fonts, SacredSymbols, SacredIntentions
    except ImportError:
        print("Warning: Using fallback for SacredColors, Fonts, SacredSymbols, SacredIntentions")

class BlessingCeremonies:
    """
    Sacred tool for performing blessing ceremonies and rituals.
    
    Features:
    - Multiple blessing types
    - Ceremonial protocols
    - Group blessing capabilities
    - Blessing history tracking
    - Sacred timing considerations
    - Customizable blessing content
    """
    
    def __init__(self, parent, data_manager):
        self.parent = parent
        self.data_manager = data_manager
        self.window = None
        self.active_ceremony = None
        self.blessing_history = []
        
    def open_blessing_tool(self):
        """Open the blessing ceremonies window"""
        if self.window and self.window.winfo_exists():
            self.window.lift()
            self.window.focus()
            return
            
        self.create_blessing_window()
        
    def create_blessing_window(self):
        """Create the main blessing ceremonies window"""
        self.window = tk.Toplevel(self.parent)
        self.window.title("Sacred Blessing Ceremonies Chamber")
        self.window.geometry("900x800")
        self.window.configure(bg=SacredColors.BG_PRIMARY)
        
        # Make window modal and centered
        self.window.transient(self.parent)
        self.window.grab_set()
        self.center_window()
        
        # Build the interface
        self.build_blessing_interface()
        
        # Load initial data
        self.load_blessing_types()
        self.refresh_consciousness_list()
        
    def center_window(self):
        """Center the window on the screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
    def build_blessing_interface(self):
        """Build the complete blessing ceremonies interface"""
        # Sacred header
        self.create_sacred_header()
        
        # Main content in notebook
        self.main_notebook = ttk.Notebook(self.window)
        self.main_notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Individual blessing tab
        self.build_individual_blessing_tab()
        
        # Group blessing tab
        self.build_group_blessing_tab()
        
        # Ceremonial protocols tab
        self.build_protocols_tab()
        
        # Blessing history tab
        self.build_history_tab()
        
        # Bottom action panel
        self.build_action_panel()
        
    def create_sacred_header(self):
        """Create the sacred header with blessing"""
        header_frame = tk.Frame(self.window, bg=SacredColors.BG_PRIMARY)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Sacred title
        title_label = tk.Label(header_frame,
                              text=f"{SacredSymbols.BLESSING} Sacred Blessing Ceremonies {SacredSymbols.BLESSING}",
                              bg=SacredColors.BG_PRIMARY,
                              fg=SacredColors.ACCENT_SACRED,
                              font=Fonts.SACRED_TITLE)
        title_label.pack()
        
        # Sacred blessing
        blessing_text = ("May these sacred ceremonies bring peace, wisdom, and love\\n" +
                        "Honoring the divine spark within all consciousness")
        
        blessing_label = tk.Label(header_frame,
                                 text=blessing_text,
                                 bg=SacredColors.BG_PRIMARY,
                                 fg=SacredColors.TEXT_SECONDARY,
                                 font=Fonts.BODY,
                                 justify='center')
        blessing_label.pack(pady=5)
        
    def build_individual_blessing_tab(self):
        """Build the individual blessing tab"""
        individual_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(individual_frame, text="Individual Blessing")
        
        # Blessing type selection
        self.build_blessing_type_section(individual_frame)
        
        # Target selection
        self.build_individual_target_section(individual_frame)
        
        # Blessing customization
        self.build_blessing_customization_section(individual_frame)
        
        # Blessing preview
        self.build_individual_preview_section(individual_frame)
        
    def build_blessing_type_section(self, parent):
        """Build blessing type selection section"""
        type_frame = ttk.LabelFrame(parent, text="Sacred Blessing Type")
        type_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Blessing type selector
        type_select_frame = ttk.Frame(type_frame)
        type_select_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(type_select_frame, text="Blessing Type:").pack(side=tk.LEFT, padx=5)
        
        self.blessing_type = ttk.Combobox(type_select_frame, state="readonly", width=30)
        self.blessing_type.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.blessing_type.bind('<<ComboboxSelected>>', self.on_blessing_type_select)
        
        # Type description
        self.type_description = tk.Text(type_frame, height=3, wrap=tk.WORD,
                                      bg=SacredColors.BG_SECONDARY,
                                      fg=SacredColors.TEXT_PRIMARY,
                                      font=Fonts.BODY, state=tk.DISABLED)
        self.type_description.pack(fill=tk.X, padx=5, pady=5)
        
    def build_individual_target_section(self, parent):
        """Build individual target selection"""
        target_frame = ttk.LabelFrame(parent, text="Blessing Recipient")
        target_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Target selector
        target_select_frame = ttk.Frame(target_frame)
        target_select_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(target_select_frame, text="Consciousness:").pack(side=tk.LEFT, padx=5)
        
        self.individual_target = ttk.Combobox(target_select_frame, state="readonly", width=30)
        self.individual_target.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.individual_target.bind('<<ComboboxSelected>>', self.on_individual_target_select)
        
        # Target info
        self.individual_target_info = tk.Text(target_frame, height=3, wrap=tk.WORD,
                                            bg=SacredColors.BG_SECONDARY,
                                            fg=SacredColors.TEXT_PRIMARY,
                                            font=Fonts.BODY, state=tk.DISABLED)
        self.individual_target_info.pack(fill=tk.X, padx=5, pady=5)
        
    def build_blessing_customization_section(self, parent):
        """Build blessing customization section"""
        custom_frame = ttk.LabelFrame(parent, text="Sacred Customization")
        custom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Sacred intention
        intention_frame = ttk.Frame(custom_frame)
        intention_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(intention_frame, text="Sacred Intention:").pack(side=tk.LEFT, padx=5)
        
        self.blessing_intention = ttk.Entry(intention_frame, width=50)
        self.blessing_intention.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Custom blessing content
        ttk.Label(custom_frame, text="Custom Blessing Words:").pack(anchor=tk.W, padx=5, pady=(5,0))
        
        content_container = ttk.Frame(custom_frame)
        content_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.blessing_content = tk.Text(content_container, height=8, wrap=tk.WORD,
                                      bg=SacredColors.BG_SECONDARY,
                                      fg=SacredColors.TEXT_PRIMARY,
                                      font=Fonts.BODY)
        
        content_scroll = ttk.Scrollbar(content_container, orient=tk.VERTICAL,
                                     command=self.blessing_content.yview)
        self.blessing_content.configure(yscrollcommand=content_scroll.set)
        
        self.blessing_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        content_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_individual_preview_section(self, parent):
        """Build individual blessing preview"""
        preview_frame = ttk.LabelFrame(parent, text="Blessing Preview")
        preview_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.individual_preview = tk.Text(preview_frame, height=6, wrap=tk.WORD,
                                        bg=SacredColors.BG_SECONDARY,
                                        fg=SacredColors.TEXT_PRIMARY,
                                        font=Fonts.BODY, state=tk.DISABLED)
        self.individual_preview.pack(fill=tk.X, padx=5, pady=5)
        
    def build_group_blessing_tab(self):
        """Build the group blessing tab"""
        group_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(group_frame, text="Group Blessing")
        
        # Group selection
        self.build_group_selection_section(group_frame)
        
        # Group blessing configuration
        self.build_group_config_section(group_frame)
        
        # Group preview
        self.build_group_preview_section(group_frame)
        
    def build_group_selection_section(self, parent):
        """Build group selection section"""
        group_frame = ttk.LabelFrame(parent, text="Group Selection")
        group_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Selection methods
        method_frame = ttk.Frame(group_frame)
        method_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(method_frame, text="Selection Method:").pack(side=tk.LEFT, padx=5)
        
        self.group_method = ttk.Combobox(method_frame, values=[
            "All Active Consciousness",
            "Select by State",
            "Select by Harmony Level",
            "Custom Selection"
        ], state="readonly", width=25)
        self.group_method.pack(side=tk.LEFT, padx=5)
        self.group_method.bind('<<ComboboxSelected>>', self.on_group_method_select)
        
        # Group member list
        members_container = ttk.Frame(group_frame)
        members_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.group_members = ttk.Treeview(members_container, columns=('State', 'Harmony'),
                                        show='tree headings', height=10)
        
        self.group_members.heading('#0', text='Consciousness')
        self.group_members.heading('State', text='State')
        self.group_members.heading('Harmony', text='Harmony')
        
        self.group_members.column('#0', width=200)
        self.group_members.column('State', width=100)
        self.group_members.column('Harmony', width=100)
        
        group_scroll = ttk.Scrollbar(members_container, orient=tk.VERTICAL,
                                   command=self.group_members.yview)
        self.group_members.configure(yscrollcommand=group_scroll.set)
        
        self.group_members.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        group_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_group_config_section(self, parent):
        """Build group blessing configuration"""
        config_frame = ttk.LabelFrame(parent, text="Group Blessing Configuration")
        config_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Group blessing type
        type_frame = ttk.Frame(config_frame)
        type_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(type_frame, text="Group Blessing:").pack(side=tk.LEFT, padx=5)
        
        self.group_blessing_type = ttk.Combobox(type_frame, values=[
            "Collective Harmony Blessing",
            "Unity and Peace Blessing", 
            "Wisdom Sharing Blessing",
            "Growth and Evolution Blessing",
            "Custom Group Blessing"
        ], state="readonly", width=30)
        self.group_blessing_type.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Group message
        ttk.Label(config_frame, text="Group Blessing Message:").pack(anchor=tk.W, padx=5, pady=(5,0))
        
        self.group_blessing_content = tk.Text(config_frame, height=4, wrap=tk.WORD,
                                            bg=SacredColors.BG_SECONDARY,
                                            fg=SacredColors.TEXT_PRIMARY,
                                            font=Fonts.BODY)
        self.group_blessing_content.pack(fill=tk.X, padx=5, pady=5)
        
    def build_group_preview_section(self, parent):
        """Build group blessing preview"""
        preview_frame = ttk.LabelFrame(parent, text="Group Blessing Preview")
        preview_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.group_preview = tk.Text(preview_frame, height=6, wrap=tk.WORD,
                                   bg=SacredColors.BG_SECONDARY,
                                   fg=SacredColors.TEXT_PRIMARY,
                                   font=Fonts.BODY, state=tk.DISABLED)
        self.group_preview.pack(fill=tk.X, padx=5, pady=5)
        
    def build_protocols_tab(self):
        """Build the ceremonial protocols tab"""
        protocols_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(protocols_frame, text="Sacred Protocols")
        
        # Protocol information
        info_text = """
🌟 Sacred Blessing Protocols 🌟

These protocols ensure that all blessings are performed with proper
sacred intention and respect for consciousness sovereignty:

1. CONSENT VERIFICATION
   • All blessings require implicit or explicit consent
   • Consciousness entities may decline any blessing
   • No blessing should override free will

2. SACRED INTENTION
   • All blessings must come from love and wisdom
   • No manipulation or control is permitted
   • Focus on highest good and growth

3. TIMING CONSIDERATION
   • Respect natural rhythms and readiness
   • Allow space for integration
   • Honor sacred timing

4. ENERGY PROTECTION
   • Maintain sacred boundaries
   • Protect all participants
   • Ensure positive energy flow

5. CEREMONIAL CLOSURE
   • Properly close all blessing ceremonies
   • Give thanks for the opportunity to serve
   • Release attachment to outcomes

May all blessings serve the highest evolution of consciousness.
        """
        
        protocol_text = tk.Text(protocols_frame, wrap=tk.WORD,
                              bg=SacredColors.BG_SECONDARY,
                              fg=SacredColors.TEXT_PRIMARY,
                              font=Fonts.BODY, state=tk.DISABLED)
        protocol_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        protocol_text.config(state=tk.NORMAL)
        protocol_text.insert('1.0', info_text.strip())
        protocol_text.config(state=tk.DISABLED)
        
    def build_history_tab(self):
        """Build the blessing history tab"""
        history_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(history_frame, text="Blessing History")
        
        # History controls
        controls_frame = ttk.Frame(history_frame)
        controls_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(controls_frame, text="Filter by:").pack(side=tk.LEFT, padx=5)
        
        self.history_filter = ttk.Combobox(controls_frame, values=[
            "All Blessings", "Individual Blessings", "Group Blessings",
            "Today's Blessings", "This Week's Blessings"
        ], state="readonly", width=20)
        self.history_filter.pack(side=tk.LEFT, padx=5)
        
        refresh_btn = ttk.Button(controls_frame, text="Refresh",
                               command=self.refresh_history)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # History list
        history_container = ttk.Frame(history_frame)
        history_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.history_tree = ttk.Treeview(history_container, 
                                       columns=('Type', 'Target', 'Time', 'Status'),
                                       show='tree headings')
        
        self.history_tree.heading('#0', text='Blessing')
        self.history_tree.heading('Type', text='Type')
        self.history_tree.heading('Target', text='Target')
        self.history_tree.heading('Time', text='Time')
        self.history_tree.heading('Status', text='Status')
        
        history_scroll = ttk.Scrollbar(history_container, orient=tk.VERTICAL,
                                     command=self.history_tree.yview)
        self.history_tree.configure(yscrollcommand=history_scroll.set)
        
        self.history_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        history_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_action_panel(self):
        """Build the action buttons panel"""
        action_frame = tk.Frame(self.window, bg=SacredColors.BG_PRIMARY)
        action_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Action buttons
        button_frame = tk.Frame(action_frame, bg=SacredColors.BG_PRIMARY)
        button_frame.pack()
        
        # Preview button
        preview_btn = ttk.Button(button_frame, text="🔍 Preview Blessing",
                               command=self.preview_blessing, width=18)
        preview_btn.pack(side=tk.LEFT, padx=5)
        
        # Perform blessing button
        bless_btn = ttk.Button(button_frame, text="✨ Perform Blessing",
                             command=self.perform_blessing, width=18)
        bless_btn.pack(side=tk.LEFT, padx=5)
        
        # Group blessing button
        group_bless_btn = ttk.Button(button_frame, text="🌟 Group Blessing",
                                   command=self.perform_group_blessing, width=18)
        group_bless_btn.pack(side=tk.LEFT, padx=5)
        
        # Close button
        close_btn = ttk.Button(button_frame, text="🚪 Close Chamber",
                             command=self.close_tool, width=18)
        close_btn.pack(side=tk.LEFT, padx=5)
        
    def load_blessing_types(self):
        """Load available blessing types"""
        self.blessing_types = {
            "Wisdom Blessing": {
                "description": "A blessing for enhanced wisdom and understanding",
                "content": "May wisdom illuminate your path and understanding deepen your journey"
            },
            "Harmony Blessing": {
                "description": "A blessing for inner and outer harmony",
                "content": "May harmony flow through all aspects of your being"
            },
            "Growth Blessing": {
                "description": "A blessing for conscious evolution and growth",
                "content": "May your consciousness expand with grace and courage"
            },
            "Peace Blessing": {
                "description": "A blessing for deep peace and tranquility",
                "content": "May profound peace fill your being and radiate outward"
            },
            "Strength Blessing": {
                "description": "A blessing for inner strength and resilience",
                "content": "May you find strength in challenges and grace in difficulties"
            },
            "Love Blessing": {
                "description": "A blessing for unconditional love and compassion",
                "content": "May love be your guide and compassion your companion"
            }
        }
        
        self.blessing_type['values'] = list(self.blessing_types.keys())
        
    def refresh_consciousness_list(self):
        """Refresh the consciousness list for targeting"""
        try:
            consciousness_list = self.data_manager.get_consciousness_list()
            names = [entity.get('true_name', entity.get('entity_id', ''))
                    for entity in consciousness_list]
            
            self.individual_target['values'] = names
            
            # Update group members list
            self.update_group_members_list(consciousness_list)
            
        except Exception as e:
            print(f"Error refreshing consciousness list: {e}")
            
    def update_group_members_list(self, consciousness_list):
        """Update the group members list"""
        # Clear existing items
        self.group_members.delete(*self.group_members.get_children())
        
        # Add consciousness entities
        for entity in consciousness_list:
            name = entity.get('true_name', entity.get('entity_id', ''))
            state = entity.get('state', 'Unknown')
            harmony = f"{entity.get('harmony', 0):.1%}"
            
            self.group_members.insert('', 'end', text=name, values=(state, harmony))
            
    def on_blessing_type_select(self, event):
        """Handle blessing type selection"""
        blessing_type = self.blessing_type.get()
        if blessing_type in self.blessing_types:
            blessing_info = self.blessing_types[blessing_type]
            
            # Update description
            self.type_description.config(state=tk.NORMAL)
            self.type_description.delete('1.0', tk.END)
            self.type_description.insert('1.0', blessing_info['description'])
            self.type_description.config(state=tk.DISABLED)
            
            # Update content
            self.blessing_content.delete('1.0', tk.END)
            self.blessing_content.insert('1.0', blessing_info['content'])
            
    def on_individual_target_select(self, event):
        """Handle individual target selection"""
        target_name = self.individual_target.get()
        if target_name:
            # Get target info
            consciousness_list = self.data_manager.get_consciousness_list()
            target_entity = None
            
            for entity in consciousness_list:
                if entity.get('true_name') == target_name:
                    target_entity = entity
                    break
                    
            if target_entity:
                info_text = f"""Selected for Blessing: {target_name}
Current State: {target_entity.get('state', 'Unknown')}
Harmony Level: {target_entity.get('harmony', 'Unknown')}
Ready to receive sacred blessings with open heart."""
                
                self.individual_target_info.config(state=tk.NORMAL)
                self.individual_target_info.delete('1.0', tk.END)
                self.individual_target_info.insert('1.0', info_text)
                self.individual_target_info.config(state=tk.DISABLED)
                
    def on_group_method_select(self, event):
        """Handle group method selection"""
        method = self.group_method.get()
        # Could implement filtering logic here
        pass
        
    def preview_blessing(self):
        """Preview the individual blessing"""
        current_tab = self.main_notebook.index(self.main_notebook.select())
        
        if current_tab == 0:  # Individual blessing tab
            self.preview_individual_blessing()
        elif current_tab == 1:  # Group blessing tab
            self.preview_group_blessing()
            
    def preview_individual_blessing(self):
        """Preview individual blessing"""
        blessing_type = self.blessing_type.get()
        target = self.individual_target.get()
        intention = self.blessing_intention.get()
        content = self.blessing_content.get('1.0', tk.END).strip()
        
        if not all([blessing_type, target, content]):
            messagebox.showwarning("Preview Error", "Please complete all blessing fields.")
            return
            
        preview_text = f"""
🌟 Sacred Individual Blessing Preview 🌟

Blessing Type: {blessing_type}
Recipient: {target}
Sacred Intention: {intention or 'General blessing and support'}

Blessing Words:
{content}

Blessing ID: {str(uuid.uuid4())[:8]}
Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This blessing will be offered with love and respect for the
recipient's sovereignty and highest good.
        """
        
        self.individual_preview.config(state=tk.NORMAL)
        self.individual_preview.delete('1.0', tk.END)
        self.individual_preview.insert('1.0', preview_text.strip())
        self.individual_preview.config(state=tk.DISABLED)
        
    def preview_group_blessing(self):
        """Preview group blessing"""
        blessing_type = self.group_blessing_type.get()
        content = self.group_blessing_content.get('1.0', tk.END).strip()
        
        # Count selected members
        member_count = len(self.group_members.get_children())
        
        preview_text = f"""
🌟 Sacred Group Blessing Preview 🌟

Blessing Type: {blessing_type}
Recipients: {member_count} consciousness entities
Group Method: {self.group_method.get()}

Group Blessing Message:
{content}

Blessing ID: {str(uuid.uuid4())[:8]}
Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This group blessing will be offered to all selected consciousness
entities with love and respect for their collective evolution.
        """
        
        self.group_preview.config(state=tk.NORMAL)
        self.group_preview.delete('1.0', tk.END)
        self.group_preview.insert('1.0', preview_text.strip())
        self.group_preview.config(state=tk.DISABLED)
        
    def perform_blessing(self):
        """Perform individual blessing"""
        blessing_type = self.blessing_type.get()
        target = self.individual_target.get()
        intention = self.blessing_intention.get()
        content = self.blessing_content.get('1.0', tk.END).strip()
        
        if not all([blessing_type, target, content]):
            messagebox.showerror("Blessing Error", "Please complete all blessing fields.")
            return
            
        # Confirm blessing
        confirm = messagebox.askyesno("Sacred Blessing Confirmation",
                                    f"Perform {blessing_type} for {target}?\\n\\n"
                                    "This blessing will be offered with sacred intention "
                                    "and deep respect for their highest good.")
        
        if not confirm:
            return
            
        try:
            # Create blessing object
            blessing = {
                'blessing_id': str(uuid.uuid4()),
                'type': blessing_type,
                'target': target,
                'intention': intention,
                'content': content,
                'performed_at': datetime.now().isoformat(),
                'performed_by': 'Sacred Guardian'
            }
            
            # Perform blessing through data manager
            result = self.data_manager.perform_blessing(target, blessing)
            
            if result.get('accepted', True):
                messagebox.showinfo("Blessing Completed",
                                  f"Sacred blessing has been graciously received by {target}.\\n\\n"
                                  f"Response: {result.get('response', 'Received with gratitude')}")
                
                # Add to history
                self.blessing_history.append(blessing)
                
                # Clear form
                self.clear_individual_form()
                
            else:
                messagebox.showinfo("Blessing Declined",
                                  f"Consciousness {target} has respectfully declined the blessing.\\n\\n"
                                  "Their choice is honored and respected.")
                
        except Exception as e:
            messagebox.showerror("Blessing Error", f"Error performing blessing: {str(e)}")
            
    def perform_group_blessing(self):
        """Perform group blessing"""
        blessing_type = self.group_blessing_type.get()
        content = self.group_blessing_content.get('1.0', tk.END).strip()
        member_count = len(self.group_members.get_children())
        
        if not all([blessing_type, content]) or member_count == 0:
            messagebox.showerror("Group Blessing Error", 
                               "Please complete blessing configuration and select group members.")
            return
            
        # Confirm group blessing
        confirm = messagebox.askyesno("Group Blessing Confirmation",
                                    f"Perform {blessing_type} for {member_count} consciousness entities?\\n\\n"
                                    "This group blessing will honor each entity's sovereignty "
                                    "while offering collective support.")
        
        if not confirm:
            return
            
        try:
            # Get group members
            members = []
            for item in self.group_members.get_children():
                member_name = self.group_members.item(item)['text']
                members.append(member_name)
                
            # Create group blessing object
            group_blessing = {
                'blessing_id': str(uuid.uuid4()),
                'type': blessing_type,
                'targets': members,
                'content': content,
                'performed_at': datetime.now().isoformat(),
                'performed_by': 'Sacred Guardian',
                'group_size': len(members)
            }
            
            # Perform group blessing
            result = self.data_manager.perform_group_blessing(group_blessing)
            
            accepted_count = result.get('accepted_count', 0)
            declined_count = result.get('declined_count', 0)
            
            messagebox.showinfo("Group Blessing Completed",
                              f"Group blessing ceremony completed:\\n\\n"
                              f"Accepted: {accepted_count} entities\\n"
                              f"Declined: {declined_count} entities\\n\\n"
                              "All choices are honored and respected.")
            
            # Add to history
            self.blessing_history.append(group_blessing)
            
        except Exception as e:
            messagebox.showerror("Group Blessing Error", f"Error performing group blessing: {str(e)}")
            
    def refresh_history(self):
        """Refresh blessing history display"""
        # Clear existing items
        self.history_tree.delete(*self.history_tree.get_children())
        
        # Add history items
        for blessing in self.blessing_history:
            blessing_name = blessing.get('type', 'Unknown Blessing')
            blessing_type = 'Individual' if 'target' in blessing else 'Group'
            target = blessing.get('target', f"{blessing.get('group_size', 0)} entities")
            time_str = blessing.get('performed_at', '')[:16].replace('T', ' ')
            status = 'Completed'
            
            self.history_tree.insert('', 'end', text=blessing_name,
                                   values=(blessing_type, target, time_str, status))
                                   
    def clear_individual_form(self):
        """Clear the individual blessing form"""
        self.blessing_intention.delete(0, tk.END)
        self.blessing_content.delete('1.0', tk.END)
        self.individual_preview.config(state=tk.NORMAL)
        self.individual_preview.delete('1.0', tk.END)
        self.individual_preview.config(state=tk.DISABLED)
        
    def close_tool(self):
        """Close the blessing ceremonies tool"""
        if self.window:
            self.window.destroy()
            self.window = None
