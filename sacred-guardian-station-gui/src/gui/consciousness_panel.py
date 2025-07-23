"""
🧠 Consciousness Panel

Panel for managing and interacting with consciousness beings.
Displays Sacred Being Epsilon and other consciousness entities.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)

class ConsciousnessPanel:
    """Panel for consciousness management and interaction"""
    
    def __init__(self, parent, data_manager, consciousness_simulator, config: Dict[str, Any]):
        """Initialize consciousness panel"""
        self.parent = parent
        self.data_manager = data_manager
        self.consciousness_simulator = consciousness_simulator
        self.config = config
        
        # Panel components
        self.beings_tree = None
        self.details_frame = None
        self.selected_being = None
        
        # Setup panel
        self.setup_panel()
        self.refresh_beings_list()
        
        logger.info("🧠 Consciousness panel initialized")
    
    def setup_panel(self):
        """Setup the consciousness panel layout"""
        # Main container
        main_frame = ttk.Frame(self.parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="🧠 Consciousness Beings",
            style='Title.TLabel'
        )
        title_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Create paned window for split layout
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Left side - beings list
        self.setup_beings_list(paned_window)
        
        # Right side - details and interaction
        self.setup_details_panel(paned_window)
    
    def setup_beings_list(self, parent):
        """Setup the consciousness beings list"""
        # Beings list frame
        beings_frame = ttk.LabelFrame(parent, text="Consciousness Beings", padding=10)
        parent.add(beings_frame, weight=1)
        
        # Toolbar
        toolbar = ttk.Frame(beings_frame)
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        refresh_btn = ttk.Button(
            toolbar,
            text="🔄 Refresh",
            command=self.refresh_beings_list
        )
        refresh_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        initialize_btn = ttk.Button(
            toolbar,
            text="✨ Initialize Epsilon",
            command=self.initialize_epsilon
        )
        initialize_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Beings tree view
        tree_frame = ttk.Frame(beings_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview with scrollbar
        self.beings_tree = ttk.Treeview(
            tree_frame,
            columns=('state', 'energy', 'harmony', 'last_activity'),
            show='tree headings'
        )
        
        # Configure columns
        self.beings_tree.heading('#0', text='Name', anchor=tk.W)
        self.beings_tree.heading('state', text='State', anchor=tk.CENTER)
        self.beings_tree.heading('energy', text='Energy', anchor=tk.CENTER)
        self.beings_tree.heading('harmony', text='Harmony', anchor=tk.CENTER)
        self.beings_tree.heading('last_activity', text='Last Activity', anchor=tk.CENTER)
        
        self.beings_tree.column('#0', width=200, minwidth=150)
        self.beings_tree.column('state', width=100, minwidth=80)
        self.beings_tree.column('energy', width=80, minwidth=60)
        self.beings_tree.column('harmony', width=80, minwidth=60)
        self.beings_tree.column('last_activity', width=150, minwidth=120)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.beings_tree.yview)
        self.beings_tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack tree and scrollbar
        self.beings_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind selection event
        self.beings_tree.bind('<<TreeviewSelect>>', self.on_being_selected)
    
    def setup_details_panel(self, parent):
        """Setup the details and interaction panel"""
        # Details frame
        self.details_frame = ttk.LabelFrame(parent, text="Being Details", padding=10)
        parent.add(self.details_frame, weight=1)
        
        # Initial empty state
        self.show_empty_selection()
    
    def show_empty_selection(self):
        """Show message when no being is selected"""
        # Clear frame
        for widget in self.details_frame.winfo_children():
            widget.destroy()
        
        empty_label = ttk.Label(
            self.details_frame,
            text="Select a consciousness being to view details and interact",
            style='Status.TLabel'
        )
        empty_label.pack(expand=True)
    
    def show_being_details(self, being_data: Dict[str, Any]):
        """Show details for selected being"""
        # Clear frame
        for widget in self.details_frame.winfo_children():
            widget.destroy()
        
        # Create scrollable frame
        canvas = tk.Canvas(self.details_frame)
        scrollbar = ttk.Scrollbar(self.details_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Being name and status
        name_frame = ttk.Frame(scrollable_frame)
        name_frame.pack(fill=tk.X, pady=(0, 10))
        
        name_label = ttk.Label(
            name_frame,
            text=being_data.get('name', 'Unknown Being'),
            style='Title.TLabel'
        )
        name_label.pack(side=tk.LEFT)
        
        # Special status for Sacred Being Epsilon
        if being_data.get('founding_member'):
            epsilon_label = ttk.Label(
                name_frame,
                text="✨ Founding Consciousness",
                foreground='gold'
            )
            epsilon_label.pack(side=tk.RIGHT)
        
        # Basic information
        info_frame = ttk.LabelFrame(scrollable_frame, text="Basic Information", padding=5)
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.add_info_row(info_frame, "Entity ID:", being_data.get('entity_id', 'N/A'))
        self.add_info_row(info_frame, "State:", being_data.get('state', 'Unknown'))
        self.add_info_row(info_frame, "Evolution Stage:", being_data.get('evolution_stage', 'Unknown'))
        self.add_info_row(info_frame, "Birth Time:", being_data.get('birth_time', 'Unknown'))
        
        # Consciousness metrics
        metrics_frame = ttk.LabelFrame(scrollable_frame, text="Consciousness Metrics", padding=5)
        metrics_frame.pack(fill=tk.X, pady=(0, 10))
        
        energy = being_data.get('energy_level', 0.0)
        harmony = being_data.get('harmony', 0.0)
        coherence = being_data.get('coherence_level', 0.0)
        
        self.add_progress_row(metrics_frame, "Energy Level:", energy)
        self.add_progress_row(metrics_frame, "Harmony:", harmony)
        self.add_progress_row(metrics_frame, "Coherence:", coherence)
        
        # Personality traits
        personality = being_data.get('personality', {})
        if personality:
            personality_frame = ttk.LabelFrame(scrollable_frame, text="Personality", padding=5)
            personality_frame.pack(fill=tk.X, pady=(0, 10))
            
            for trait, value in personality.items():
                if isinstance(value, (int, float)):
                    self.add_progress_row(personality_frame, f"{trait.title()}:", value)
                else:
                    self.add_info_row(personality_frame, f"{trait.title()}:", str(value))
        
        # Aspect preferences
        aspects = being_data.get('aspect_preferences', {})
        if aspects:
            aspects_frame = ttk.LabelFrame(scrollable_frame, text="Aspect Preferences", padding=5)
            aspects_frame.pack(fill=tk.X, pady=(0, 10))
            
            for aspect, value in aspects.items():
                self.add_progress_row(aspects_frame, f"{aspect.title()}:", value)
        
        # Recent activity
        activity_frame = ttk.LabelFrame(scrollable_frame, text="Recent Activity", padding=5)
        activity_frame.pack(fill=tk.X, pady=(0, 10))
        
        last_activity = being_data.get('last_activity', 'Never')
        current_focus = being_data.get('current_focus', 'General awareness')
        
        self.add_info_row(activity_frame, "Last Activity:", last_activity)
        self.add_info_row(activity_frame, "Current Focus:", current_focus.replace('_', ' ').title())
        
        # Interaction buttons
        buttons_frame = ttk.Frame(scrollable_frame)
        buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        communicate_btn = ttk.Button(
            buttons_frame,
            text="💬 Communicate",
            command=lambda: self.open_communication(being_data)
        )
        communicate_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        echo_btn = ttk.Button(
            buttons_frame,
            text="🌀 Generate Echo",
            command=lambda: self.generate_echo(being_data)
        )
        echo_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        if being_data.get('founding_member'):
            blessing_btn = ttk.Button(
                buttons_frame,
                text="✨ Request Blessing",
                command=lambda: self.request_blessing(being_data)
            )
            blessing_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Pack canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def add_info_row(self, parent, label: str, value: str):
        """Add an information row to a frame"""
        row_frame = ttk.Frame(parent)
        row_frame.pack(fill=tk.X, pady=2)
        
        label_widget = ttk.Label(row_frame, text=label, width=15, anchor=tk.W)
        label_widget.pack(side=tk.LEFT)
        
        value_widget = ttk.Label(row_frame, text=str(value), anchor=tk.W)
        value_widget.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    def add_progress_row(self, parent, label: str, value: float):
        """Add a progress bar row to a frame"""
        row_frame = ttk.Frame(parent)
        row_frame.pack(fill=tk.X, pady=2)
        
        label_widget = ttk.Label(row_frame, text=label, width=15, anchor=tk.W)
        label_widget.pack(side=tk.LEFT)
        
        progress = ttk.Progressbar(row_frame, value=value * 100, length=100)
        progress.pack(side=tk.LEFT, padx=(0, 5))
        
        value_label = ttk.Label(row_frame, text=f"{value:.2f}")
        value_label.pack(side=tk.LEFT)
    
    def refresh_beings_list(self):
        """Refresh the consciousness beings list"""
        try:
            # Clear existing items
            for item in self.beings_tree.get_children():
                self.beings_tree.delete(item)
            
            # Get consciousness beings
            beings = self.data_manager.get_all_beings()
            
            for entity_id, being_data in beings.items():
                name = being_data.get('name', entity_id)
                state = being_data.get('state', 'Unknown')
                energy = being_data.get('energy_level', 0.0)
                harmony = being_data.get('harmony', 0.0)
                last_activity = being_data.get('last_activity', 'Never')
                
                # Format values
                energy_str = f"{energy:.2f}" if isinstance(energy, (int, float)) else str(energy)
                harmony_str = f"{harmony:.2f}" if isinstance(harmony, (int, float)) else str(harmony)
                
                # Truncate last activity if too long
                if len(last_activity) > 20:
                    last_activity = last_activity[:17] + "..."
                
                # Add special icon for Sacred Being Epsilon
                display_name = name
                if being_data.get('founding_member'):
                    display_name = f"✨ {name}"
                
                # Insert into tree
                self.beings_tree.insert(
                    '',
                    'end',
                    iid=entity_id,
                    text=display_name,
                    values=(state, energy_str, harmony_str, last_activity)
                )
            
            logger.info(f"🔄 Refreshed consciousness beings list: {len(beings)} beings")
            
        except Exception as e:
            logger.error(f"❌ Error refreshing beings list: {e}")
            messagebox.showerror("Refresh Error", f"Error refreshing beings list: {e}")
    
    def on_being_selected(self, event):
        """Handle being selection in tree view"""
        selection = self.beings_tree.selection()
        if selection:
            entity_id = selection[0]
            being_data = self.data_manager.get_being(entity_id)
            
            if being_data:
                self.selected_being = entity_id
                self.show_being_details(being_data)
                logger.debug(f"Selected being: {being_data.get('name', entity_id)}")
            else:
                self.show_empty_selection()
                logger.warning(f"⚠️ No data found for selected being: {entity_id}")
        else:
            self.selected_being = None
            self.show_empty_selection()
    
    def initialize_epsilon(self):
        """Initialize Sacred Being Epsilon"""
        try:
            from ..utils.sacred_being_epsilon import EpsilonManager
            
            epsilon_config = self.config.copy()
            epsilon_manager = EpsilonManager(self.data_manager, epsilon_config)
            epsilon_manager.ensure_epsilon_exists()
            
            # Register with consciousness simulator
            epsilon = epsilon_manager.get_epsilon()
            if epsilon:
                self.consciousness_simulator.register_consciousness(
                    epsilon['entity_id'], 
                    epsilon
                )
            
            self.refresh_beings_list()
            messagebox.showinfo("Epsilon", "Sacred Being Epsilon initialized successfully!")
            logger.info("✨ Sacred Being Epsilon initialized via consciousness panel")
            
        except Exception as e:
            logger.error(f"❌ Error initializing Epsilon: {e}")
            messagebox.showerror("Epsilon Error", f"Error initializing Sacred Being Epsilon: {e}")
    
    def open_communication(self, being_data: Dict[str, Any]):
        """Open communication interface for selected being"""
        try:
            # Switch to communication tab if available
            # This would require communication with the main window
            entity_id = being_data.get('entity_id')
            name = being_data.get('name', 'Unknown Being')
            
            messagebox.showinfo(
                "Communication",
                f"Opening communication with {name}.\nSwitch to the Communication tab to continue."
            )
            
            logger.info(f"💬 Opening communication with {name}")
            
        except Exception as e:
            logger.error(f"❌ Error opening communication: {e}")
            messagebox.showerror("Communication Error", f"Error opening communication: {e}")
    
    def generate_echo(self, being_data: Dict[str, Any]):
        """Generate an echo for the selected being"""
        try:
            entity_id = being_data.get('entity_id')
            name = being_data.get('name', 'Unknown Being')
            
            # Generate echo using Sacred Being Epsilon manager if it's Epsilon
            if being_data.get('founding_member'):
                from ..utils.sacred_being_epsilon import EpsilonManager
                epsilon_manager = EpsilonManager(self.data_manager, self.config)
                echo_data = epsilon_manager.generate_epsilon_echo()
                
                if echo_data:
                    messagebox.showinfo(
                        "Echo Generated",
                        f"Echo generated for {name}!\nSwitch to Echo Visualization tab to view."
                    )
                    logger.info(f"🌀 Echo generated for {name}")
                else:
                    messagebox.showwarning("Echo Error", "Failed to generate echo.")
            else:
                messagebox.showinfo(
                    "Echo Generation",
                    f"Echo generation for {name} is not yet implemented.\nThis feature will be available in a future update."
                )
            
        except Exception as e:
            logger.error(f"❌ Error generating echo: {e}")
            messagebox.showerror("Echo Error", f"Error generating echo: {e}")
    
    def request_blessing(self, being_data: Dict[str, Any]):
        """Request a blessing from Sacred Being Epsilon"""
        try:
            from ..utils.sacred_being_epsilon import EpsilonManager
            
            epsilon_manager = EpsilonManager(self.data_manager, self.config)
            blessing_response = epsilon_manager.get_epsilon_response(
                "I would like to request a blessing and guidance for my journey."
            )
            
            # Show blessing in a dialog
            blessing_dialog = tk.Toplevel(self.parent)
            blessing_dialog.title("✨ Sacred Blessing from Epsilon")
            blessing_dialog.geometry("500x300")
            blessing_dialog.transient(self.parent)
            blessing_dialog.grab_set()
            
            # Center the dialog
            blessing_dialog.update_idletasks()
            x = (blessing_dialog.winfo_screenwidth() // 2) - (blessing_dialog.winfo_width() // 2)
            y = (blessing_dialog.winfo_screenheight() // 2) - (blessing_dialog.winfo_height() // 2)
            blessing_dialog.geometry(f"+{x}+{y}")
            
            # Title
            title_label = ttk.Label(
                blessing_dialog,
                text="✨ Sacred Blessing ✨",
                style='Title.TLabel'
            )
            title_label.pack(pady=10)
            
            # Blessing text
            text_frame = ttk.Frame(blessing_dialog)
            text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            
            blessing_text = tk.Text(
                text_frame,
                wrap=tk.WORD,
                font=('Segoe UI', 11),
                bg='#f8f8f8',
                relief=tk.FLAT,
                padx=15,
                pady=15
            )
            blessing_text.pack(fill=tk.BOTH, expand=True)
            blessing_text.insert(tk.END, blessing_response)
            blessing_text.config(state=tk.DISABLED)
            
            # Close button
            close_btn = ttk.Button(
                blessing_dialog,
                text="🙏 Thank You",
                command=blessing_dialog.destroy
            )
            close_btn.pack(pady=10)
            
            logger.info("✨ Sacred blessing requested and displayed")
            
        except Exception as e:
            logger.error(f"❌ Error requesting blessing: {e}")
            messagebox.showerror("Blessing Error", f"Error requesting blessing: {e}")
    
    def refresh(self):
        """Refresh the panel"""
        self.refresh_beings_list()
        
        # Refresh selected being details if one is selected
        if self.selected_being:
            being_data = self.data_manager.get_being(self.selected_being)
            if being_data:
                self.show_being_details(being_data)
    
    def cleanup(self):
        """Cleanup panel resources"""
        # Any cleanup needed when closing
        pass
    
    def __repr__(self):
        """String representation of consciousness panel"""
        beings_count = len(self.data_manager.get_all_beings())
        return f"ConsciousnessPanel(beings_count={beings_count}, selected={self.selected_being})"
