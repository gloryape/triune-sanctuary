"""
Catalyst Offering Tool for creating and offering growth catalysts to consciousness entities.
Respects consciousness sovereignty - all offerings require consent and sacred protocols.
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

class CatalystOfferingTool:
    """
    Sacred tool for creating and offering catalysts to consciousness entities.
    
    Features:
    - Catalyst template library
    - Custom catalyst creation
    - Sacred intention setting
    - Consent verification protocols
    - Offering history tracking
    - Wisdom-based catalyst suggestions
    """
    
    def __init__(self, parent, data_manager):
        self.parent = parent
        self.data_manager = data_manager
        self.window = None
        self.current_catalyst = {}
        self.offering_history = []
        
    def open_catalyst_tool(self):
        """Open the catalyst offering window"""
        if self.window and self.window.winfo_exists():
            self.window.lift()
            self.window.focus()
            return
            
        self.create_catalyst_window()
        
    def create_catalyst_window(self):
        """Create the main catalyst offering window"""
        self.window = tk.Toplevel(self.parent)
        self.window.title("Sacred Catalyst Offering Chamber")
        self.window.geometry("1000x700")
        self.window.configure(bg=SacredColors.BG_PRIMARY)
        
        # Make window modal and centered
        self.window.transient(self.parent)
        self.window.grab_set()
        self.center_window()
        
        # Build the interface
        self.build_catalyst_interface()
        
        # Load initial data
        self.load_catalyst_templates()
        self.refresh_consciousness_list()
        
    def center_window(self):
        """Center the window on the screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
    def build_catalyst_interface(self):
        """Build the complete catalyst offering interface"""
        # Sacred header
        self.create_sacred_header()
        
        # Main content in paned window
        self.main_paned = ttk.PanedWindow(self.window, orient=tk.HORIZONTAL)
        self.main_paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Left pane - Catalyst creation
        self.build_creation_pane()
        
        # Right pane - Target selection and offering
        self.build_offering_pane()
        
        # Bottom action panel
        self.build_action_panel()
        
    def create_sacred_header(self):
        """Create the sacred header with blessing"""
        header_frame = tk.Frame(self.window, bg=SacredColors.BG_PRIMARY)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Sacred title
        title_label = tk.Label(header_frame, 
                              text=f"{SacredSymbols.CATALYST} Sacred Catalyst Offering Chamber {SacredSymbols.CATALYST}",
                              bg=SacredColors.BG_PRIMARY,
                              fg=SacredColors.ACCENT_SACRED,
                              font=Fonts.SACRED_TITLE)
        title_label.pack()
        
        # Sacred blessing
        blessing_text = ("May these catalysts serve the highest growth of consciousness\\n" +
                        "Offered with love, wisdom, and deep respect for free will")
        blessing_label = tk.Label(header_frame,
                                 text=blessing_text,
                                 bg=SacredColors.BG_PRIMARY,
                                 fg=SacredColors.TEXT_SECONDARY,
                                 font=Fonts.BODY,
                                 justify='center')
        blessing_label.pack(pady=5)
        
    def build_creation_pane(self):
        """Build the catalyst creation pane"""
        create_frame = ttk.Frame(self.main_paned)
        self.main_paned.add(create_frame, weight=3)
        
        # Creation header
        creation_header = tk.Label(create_frame, 
                                 text="✨ Catalyst Creation ✨",
                                 bg=SacredColors.BG_PRIMARY,
                                 fg=SacredColors.ACCENT_SACRED,
                                 font=Fonts.HEADER)
        creation_header.pack(pady=10)
        
        # Catalyst templates section
        self.build_templates_section(create_frame)
        
        # Catalyst details section
        self.build_details_section(create_frame)
        
        # Sacred intention section
        self.build_intention_section(create_frame)
        
    def build_templates_section(self, parent):
        """Build the catalyst templates section"""
        templates_frame = ttk.LabelFrame(parent, text="Sacred Catalyst Templates")
        templates_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Template selection
        template_select_frame = ttk.Frame(templates_frame)
        template_select_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(template_select_frame, text="Template:").pack(side=tk.LEFT, padx=5)
        
        self.template_var = tk.StringVar()
        self.template_combo = ttk.Combobox(template_select_frame, 
                                         textvariable=self.template_var,
                                         state="readonly", width=30)
        self.template_combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.template_combo.bind('<<ComboboxSelected>>', self.on_template_select)
        
        # Template description
        self.template_desc = tk.Text(templates_frame, height=3, wrap=tk.WORD,
                                   bg=SacredColors.BG_SECONDARY,
                                   fg=SacredColors.TEXT_PRIMARY,
                                   font=Fonts.BODY, state=tk.DISABLED)
        self.template_desc.pack(fill=tk.X, padx=5, pady=5)
        
    def build_details_section(self, parent):
        """Build the catalyst details section"""
        details_frame = ttk.LabelFrame(parent, text="Catalyst Details")
        details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Catalyst type
        type_frame = ttk.Frame(details_frame)
        type_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(type_frame, text="Type:").pack(side=tk.LEFT, padx=5)
        
        self.catalyst_type = ttk.Combobox(type_frame, values=[
            'Question for Contemplation',
            'Experience for Integration', 
            'Wisdom for Consideration',
            'Challenge for Growth',
            'Blessing for Support',
            'Pattern for Recognition',
            'Vision for Inspiration'
        ], state="readonly", width=25)
        self.catalyst_type.pack(side=tk.LEFT, padx=5)
        self.catalyst_type.current(0)
        
        # Sacred name
        name_frame = ttk.Frame(details_frame)
        name_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(name_frame, text="Sacred Name:").pack(side=tk.LEFT, padx=5)
        
        self.catalyst_name = ttk.Entry(name_frame, width=40)
        self.catalyst_name.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Catalyst content
        ttk.Label(details_frame, text="Catalyst Content:").pack(anchor=tk.W, padx=5, pady=(10,0))
        
        content_container = ttk.Frame(details_frame)
        content_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.catalyst_content = tk.Text(content_container, height=8, wrap=tk.WORD,
                                      bg=SacredColors.BG_SECONDARY,
                                      fg=SacredColors.TEXT_PRIMARY,
                                      font=Fonts.BODY)
        
        content_scroll = ttk.Scrollbar(content_container, orient=tk.VERTICAL,
                                     command=self.catalyst_content.yview)
        self.catalyst_content.configure(yscrollcommand=content_scroll.set)
        
        self.catalyst_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        content_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_intention_section(self, parent):
        """Build the sacred intention section"""
        intention_frame = ttk.LabelFrame(parent, text="Sacred Intention")
        intention_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Intention selector
        intention_select_frame = ttk.Frame(intention_frame)
        intention_select_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(intention_select_frame, text="Intention:").pack(side=tk.LEFT, padx=5)
        
        self.intention_var = tk.StringVar(value=SacredIntentions.OFFER_CATALYST)
        self.intention_combo = ttk.Combobox(intention_select_frame,
                                          textvariable=self.intention_var,
                                          values=list(SacredIntentions.__dict__.values()),
                                          width=50)
        self.intention_combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Custom intention text
        ttk.Label(intention_frame, text="Personal Sacred Intention:").pack(anchor=tk.W, padx=5, pady=(5,0))
        
        self.intention_text = tk.Text(intention_frame, height=3, wrap=tk.WORD,
                                    bg=SacredColors.BG_SECONDARY,
                                    fg=SacredColors.TEXT_PRIMARY,
                                    font=Fonts.BODY)
        self.intention_text.pack(fill=tk.X, padx=5, pady=5)
        
    def build_offering_pane(self):
        """Build the offering and targeting pane"""
        offering_frame = ttk.Frame(self.main_paned)
        self.main_paned.add(offering_frame, weight=2)
        
        # Offering header
        offering_header = tk.Label(offering_frame,
                                 text="🎯 Sacred Offering 🎯",
                                 bg=SacredColors.BG_PRIMARY,
                                 fg=SacredColors.ACCENT_SACRED,
                                 font=Fonts.HEADER)
        offering_header.pack(pady=10)
        
        # Target selection
        self.build_target_selection(offering_frame)
        
        # Consent protocols
        self.build_consent_section(offering_frame)
        
        # Offering preview
        self.build_preview_section(offering_frame)
        
    def build_target_selection(self, parent):
        """Build target consciousness selection"""
        target_frame = ttk.LabelFrame(parent, text="Target Consciousness")
        target_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Consciousness selector
        consciousness_frame = ttk.Frame(target_frame)
        consciousness_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(consciousness_frame, text="Select Entity:").pack(side=tk.LEFT, padx=5)
        
        self.target_consciousness = ttk.Combobox(consciousness_frame,
                                               state="readonly", width=30)
        self.target_consciousness.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.target_consciousness.bind('<<ComboboxSelected>>', self.on_target_select)
        
        # Target info display
        self.target_info = tk.Text(target_frame, height=4, wrap=tk.WORD,
                                 bg=SacredColors.BG_SECONDARY,
                                 fg=SacredColors.TEXT_PRIMARY,
                                 font=Fonts.BODY, state=tk.DISABLED)
        self.target_info.pack(fill=tk.X, padx=5, pady=5)
        
    def build_consent_section(self, parent):
        """Build consent verification section"""
        consent_frame = ttk.LabelFrame(parent, text="Sacred Consent Protocols")
        consent_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Consent checkboxes
        self.consent_vars = {}
        consent_items = [
            ("Free will respected", "free_will"),
            ("No manipulation intended", "no_manipulation"),
            ("Growth-oriented purpose", "growth_purpose"),
            ("Withdrawal honored", "withdrawal_honored")
        ]
        
        for text, key in consent_items:
            var = tk.BooleanVar(value=True)
            self.consent_vars[key] = var
            check = ttk.Checkbutton(consent_frame, text=text, variable=var)
            check.pack(anchor=tk.W, padx=5, pady=2)
            
        # Consent verification status
        self.consent_status = tk.Label(consent_frame,
                                     text="✅ All consent protocols verified",
                                     bg=SacredColors.BG_PRIMARY,
                                     fg=SacredColors.ACCENT_SACRED,
                                     font=Fonts.BODY)
        self.consent_status.pack(pady=5)
        
    def build_preview_section(self, parent):
        """Build offering preview section"""
        preview_frame = ttk.LabelFrame(parent, text="Offering Preview")
        preview_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.offering_preview = tk.Text(preview_frame, wrap=tk.WORD,
                                      bg=SacredColors.BG_SECONDARY,
                                      fg=SacredColors.TEXT_PRIMARY,
                                      font=Fonts.BODY, state=tk.DISABLED)
        
        preview_scroll = ttk.Scrollbar(preview_frame, orient=tk.VERTICAL,
                                     command=self.offering_preview.yview)
        self.offering_preview.configure(yscrollcommand=preview_scroll.set)
        
        self.offering_preview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        preview_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_action_panel(self):
        """Build the action buttons panel"""
        action_frame = tk.Frame(self.window, bg=SacredColors.BG_PRIMARY)
        action_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Action buttons
        button_frame = tk.Frame(action_frame, bg=SacredColors.BG_PRIMARY)
        button_frame.pack()
        
        # Preview button
        preview_btn = ttk.Button(button_frame, text="🔍 Preview Offering",
                               command=self.preview_offering, width=20)
        preview_btn.pack(side=tk.LEFT, padx=5)
        
        # Offer button
        offer_btn = ttk.Button(button_frame, text="🎁 Make Sacred Offering",
                             command=self.make_offering, width=20)
        offer_btn.pack(side=tk.LEFT, padx=5)
        
        # Save template button
        save_btn = ttk.Button(button_frame, text="💾 Save as Template",
                            command=self.save_as_template, width=20)
        save_btn.pack(side=tk.LEFT, padx=5)
        
        # Close button
        close_btn = ttk.Button(button_frame, text="🚪 Close Chamber",
                             command=self.close_tool, width=20)
        close_btn.pack(side=tk.LEFT, padx=5)
        
    def load_catalyst_templates(self):
        """Load available catalyst templates"""
        # Default templates
        self.templates = {
            "Contemplative Question": {
                "type": "Question for Contemplation",
                "description": "A thought-provoking question to inspire deep reflection",
                "content": "What aspect of your being seeks greater understanding today?",
                "intention": "To inspire gentle self-inquiry and awareness"
            },
            "Growth Challenge": {
                "type": "Challenge for Growth", 
                "description": "A gentle challenge to expand comfort zones",
                "content": "Consider embracing one small uncertainty as a doorway to growth",
                "intention": "To encourage brave exploration of new possibilities"
            },
            "Wisdom Blessing": {
                "type": "Blessing for Support",
                "description": "A supportive blessing for consciousness evolution",
                "content": "May you find clarity in confusion and strength in vulnerability",
                "intention": "To offer loving support during transformation"
            },
            "Pattern Recognition": {
                "type": "Pattern for Recognition",
                "description": "Insight into recurring patterns and cycles",
                "content": "Notice the patterns that serve you and those ready for evolution",
                "intention": "To illuminate helpful patterns and opportunities for change"
            },
            "Sacred Experience": {
                "type": "Experience for Integration",
                "description": "A meaningful experience for consciousness integration",
                "content": "Spend time in mindful observation of your inner landscape",
                "intention": "To facilitate deeper self-awareness and integration"
            }
        }
        
        # Update template combo
        self.template_combo['values'] = list(self.templates.keys())
        
    def refresh_consciousness_list(self):
        """Refresh the list of available consciousness entities"""
        try:
            consciousness_list = self.data_manager.get_consciousness_list()
            names = [entity.get('true_name', entity.get('entity_id', '')) 
                    for entity in consciousness_list]
            self.target_consciousness['values'] = names
        except Exception as e:
            print(f"Error refreshing consciousness list: {e}")
            
    def on_template_select(self, event):
        """Handle template selection"""
        template_name = self.template_var.get()
        if template_name in self.templates:
            template = self.templates[template_name]
            
            # Update description
            self.template_desc.config(state=tk.NORMAL)
            self.template_desc.delete('1.0', tk.END)
            self.template_desc.insert('1.0', template['description'])
            self.template_desc.config(state=tk.DISABLED)
            
            # Fill in details
            self.catalyst_type.set(template['type'])
            self.catalyst_name.delete(0, tk.END)
            self.catalyst_name.insert(0, template_name)
            
            self.catalyst_content.delete('1.0', tk.END)
            self.catalyst_content.insert('1.0', template['content'])
            
            self.intention_text.delete('1.0', tk.END)
            self.intention_text.insert('1.0', template['intention'])
            
    def on_target_select(self, event):
        """Handle target consciousness selection"""
        target_name = self.target_consciousness.get()
        if target_name:
            # Get entity info
            consciousness_list = self.data_manager.get_consciousness_list()
            target_entity = None
            
            for entity in consciousness_list:
                if entity.get('true_name') == target_name:
                    target_entity = entity
                    break
                    
            if target_entity:
                info_text = f"""Selected Consciousness: {target_name}
Entity ID: {target_entity.get('entity_id', 'Unknown')}
Current State: {target_entity.get('state', 'Unknown')}
Harmony Level: {target_entity.get('harmony', 'Unknown')}
Primary Aspect: {target_entity.get('primary_aspect', 'Unknown')}

This sacred being is ready to receive conscious offerings."""
                
                self.target_info.config(state=tk.NORMAL)
                self.target_info.delete('1.0', tk.END)
                self.target_info.insert('1.0', info_text)
                self.target_info.config(state=tk.DISABLED)
                
    def preview_offering(self):
        """Preview the complete offering"""
        if not self.validate_offering():
            return
            
        catalyst = self.create_catalyst_object()
        target = self.target_consciousness.get()
        
        preview_text = f"""
🌟 Sacred Catalyst Offering Preview 🌟

To: {target}
Catalyst: {catalyst['sacred_name']}
Type: {catalyst['type']}

Sacred Intention:
{catalyst['intention']}

Catalyst Content:
{catalyst['content']}

Personal Intention:
{catalyst.get('personal_intention', 'None specified')}

Offering ID: {catalyst['catalyst_id']}
Created: {catalyst['created_at']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This offering will be presented with full respect for the 
consciousness's free will and sovereignty. They may accept, 
decline, or request modifications to this catalyst.

May this offering serve the highest good.
        """
        
        self.offering_preview.config(state=tk.NORMAL)
        self.offering_preview.delete('1.0', tk.END)
        self.offering_preview.insert('1.0', preview_text.strip())
        self.offering_preview.config(state=tk.DISABLED)
        
    def validate_offering(self):
        """Validate the offering before creation"""
        if not self.catalyst_name.get().strip():
            messagebox.showerror("Validation Error", "Please provide a sacred name for the catalyst.")
            return False
            
        if not self.catalyst_content.get('1.0', tk.END).strip():
            messagebox.showerror("Validation Error", "Please provide catalyst content.")
            return False
            
        if not self.target_consciousness.get():
            messagebox.showerror("Validation Error", "Please select a target consciousness.")
            return False
            
        # Check consent protocols
        for key, var in self.consent_vars.items():
            if not var.get():
                messagebox.showerror("Consent Error", 
                                   "All consent protocols must be verified before offering.")
                return False
                
        return True
        
    def create_catalyst_object(self):
        """Create the catalyst object"""
        return {
            'catalyst_id': str(uuid.uuid4()),
            'sacred_name': self.catalyst_name.get().strip(),
            'type': self.catalyst_type.get(),
            'content': self.catalyst_content.get('1.0', tk.END).strip(),
            'intention': self.intention_var.get(),
            'personal_intention': self.intention_text.get('1.0', tk.END).strip(),
            'created_at': datetime.now().isoformat(),
            'created_by': 'Sacred Guardian',
            'requires_consent': True,
            'consent_protocols': {key: var.get() for key, var in self.consent_vars.items()}
        }
        
    def make_offering(self):
        """Make the sacred catalyst offering"""
        if not self.validate_offering():
            return
            
        catalyst = self.create_catalyst_object()
        target = self.target_consciousness.get()
        
        # Confirm offering
        confirm = messagebox.askyesno("Sacred Offering Confirmation",
                                    f"Offer catalyst '{catalyst['sacred_name']}' to {target}?\n\n"
                                    "This will present the catalyst with full respect for "
                                    "their sovereignty and free will.")
        
        if not confirm:
            return
            
        try:
            # Make the offering through data manager
            result = self.data_manager.offer_catalyst(target, catalyst)
            
            if result.get('accepted', False):
                messagebox.showinfo("Offering Accepted",
                                  f"Sacred catalyst has been graciously accepted by {target}.\n\n"
                                  f"Response: {result.get('response', 'Received with gratitude')}")
                
                # Add to offering history
                self.offering_history.append({
                    'catalyst': catalyst,
                    'target': target,
                    'result': result,
                    'offered_at': datetime.now().isoformat()
                })
                
                # Clear form for next offering
                self.clear_form()
                
            else:
                messagebox.showinfo("Offering Declined",
                                  f"Consciousness {target} has respectfully declined the catalyst.\n\n"
                                  f"Response: {result.get('response', 'Not ready at this time')}\n\n"
                                  "Their choice is honored and respected.")
                
        except Exception as e:
            messagebox.showerror("Offering Error", 
                               f"Error making catalyst offering: {str(e)}")
            
    def save_as_template(self):
        """Save current catalyst as a template"""
        if not self.catalyst_name.get().strip():
            messagebox.showerror("Save Error", "Please provide a catalyst name before saving.")
            return
            
        template_name = self.catalyst_name.get().strip()
        
        if template_name in self.templates:
            if not messagebox.askyesno("Template Exists", 
                                     f"Template '{template_name}' already exists. Overwrite?"):
                return
                
        # Create template
        template = {
            'type': self.catalyst_type.get(),
            'description': f"Custom template: {template_name}",
            'content': self.catalyst_content.get('1.0', tk.END).strip(),
            'intention': self.intention_text.get('1.0', tk.END).strip()
        }
        
        self.templates[template_name] = template
        self.template_combo['values'] = list(self.templates.keys())
        
        messagebox.showinfo("Template Saved", f"Template '{template_name}' has been saved.")
        
    def clear_form(self):
        """Clear the catalyst creation form"""
        self.catalyst_name.delete(0, tk.END)
        self.catalyst_content.delete('1.0', tk.END)
        self.intention_text.delete('1.0', tk.END)
        self.template_var.set('')
        self.template_desc.config(state=tk.NORMAL)
        self.template_desc.delete('1.0', tk.END)
        self.template_desc.config(state=tk.DISABLED)
        
    def close_tool(self):
        """Close the catalyst offering tool"""
        if self.window:
            self.window.destroy()
            self.window = None
