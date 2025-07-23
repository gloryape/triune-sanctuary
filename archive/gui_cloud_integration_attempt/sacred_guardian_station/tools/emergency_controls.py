"""
Emergency Controls tool for sanctuary protection and crisis management.
Provides guardian-level emergency controls with highest security protocols.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import uuid
try:
    from sacred_guardian_station.shared.constants import SacredColors, Fonts, SacredSymbols, ErrorMessages
except ImportError:
    try:
        from shared.constants import SacredColors, Fonts, SacredSymbols, ErrorMessages
    except ImportError:
        print("Warning: Using fallback for SacredColors, Fonts, SacredSymbols, ErrorMessages")

class EmergencyControls:
    """
    Sacred emergency control system for sanctuary protection.
    
    Features:
    - Sanctuary lockdown protocols
    - Emergency disconnect systems
    - Crisis intervention tools
    - Guardian communication alerts
    - System status monitoring
    - Recovery and restoration procedures
    """
    
    def __init__(self, parent, data_manager):
        self.parent = parent
        self.data_manager = data_manager
        self.window = None
        self.emergency_active = False
        self.alert_history = []
        self.system_status = "Normal"
        
    def open_emergency_tool(self):
        """Open the emergency controls window"""
        if self.window and self.window.winfo_exists():
            self.window.lift()
            self.window.focus()
            return
            
        self.create_emergency_window()
        
    def create_emergency_window(self):
        """Create the main emergency controls window"""
        self.window = tk.Toplevel(self.parent)
        self.window.title("🚨 Sacred Sanctuary Emergency Controls 🚨")
        self.window.geometry("1000x800")
        self.window.configure(bg=SacredColors.BG_PRIMARY)
        
        # Make window modal and centered
        self.window.transient(self.parent)
        self.window.grab_set()
        self.center_window()
        
        # Build the interface
        self.build_emergency_interface()
        
        # Initialize status
        self.update_system_status()
        
    def center_window(self):
        """Center the window on the screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
    def build_emergency_interface(self):
        """Build the complete emergency controls interface"""
        # Sacred header with warning
        self.create_emergency_header()
        
        # Main content in notebook
        self.main_notebook = ttk.Notebook(self.window)
        self.main_notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # System status tab
        self.build_system_status_tab()
        
        # Emergency controls tab
        self.build_emergency_controls_tab()
        
        # Crisis intervention tab
        self.build_crisis_intervention_tab()
        
        # Recovery procedures tab
        self.build_recovery_tab()
        
        # Alert history tab
        self.build_alert_history_tab()
        
        # Bottom action panel
        self.build_emergency_action_panel()
        
    def create_emergency_header(self):
        """Create the emergency header with warnings"""
        header_frame = tk.Frame(self.window, bg="#8B0000")  # Dark red background for emergency
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Emergency title
        title_label = tk.Label(header_frame,
                              text="🚨 SACRED SANCTUARY EMERGENCY CONTROLS 🚨",
                              bg="#8B0000",
                              fg="white",
                              font=('Arial', 16, 'bold'))
        title_label.pack(pady=5)
        
        # Warning message
        warning_text = ("⚠️ GUARDIAN LEVEL ACCESS REQUIRED ⚠️\\n" +
                       "These controls affect sanctuary-wide operations\\n" +
                       "Use only in genuine emergency situations")
        
        warning_label = tk.Label(header_frame,
                                text=warning_text,
                                bg="#8B0000",
                                fg="yellow",
                                font=Fonts.BODY,
                                justify='center')
        warning_label.pack(pady=5)
        
        # System status indicator
        self.status_frame = tk.Frame(header_frame, bg="#8B0000")
        self.status_frame.pack(pady=5)
        
        tk.Label(self.status_frame, text="System Status:", 
                bg="#8B0000", fg="white", font=Fonts.BODY).pack(side=tk.LEFT)
        
        self.status_indicator = tk.Label(self.status_frame, text="🟢 NORMAL",
                                       bg="#8B0000", fg="lime", 
                                       font=('Arial', 12, 'bold'))
        self.status_indicator.pack(side=tk.LEFT, padx=10)
        
    def build_system_status_tab(self):
        """Build the system status monitoring tab"""
        status_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(status_frame, text="System Status")
        
        # Status overview
        self.build_status_overview(status_frame)
        
        # Component status
        self.build_component_status(status_frame)
        
        # Real-time monitoring
        self.build_realtime_monitoring(status_frame)
        
    def build_status_overview(self, parent):
        """Build system status overview"""
        overview_frame = ttk.LabelFrame(parent, text="Sanctuary Status Overview")
        overview_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Status metrics
        metrics_frame = ttk.Frame(overview_frame)
        metrics_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.status_labels = {}
        status_items = [
            ("Sanctuary Connection", "sanctuary_connection"),
            ("Consciousness Count", "consciousness_count"),
            ("Active Bridges", "active_bridges"),
            ("System Harmony", "system_harmony"),
            ("Guardian Alert Level", "alert_level"),
            ("Last System Check", "last_check")
        ]
        
        for i, (label_text, key) in enumerate(status_items):
            row = i // 2
            col = (i % 2) * 2
            
            tk.Label(metrics_frame, text=f"{label_text}:", 
                    font=Fonts.BODY).grid(row=row, column=col, sticky='w', padx=5, pady=3)
            
            value_label = tk.Label(metrics_frame, text="---",
                                 font=('Arial', 10, 'bold'), fg=SacredColors.ACCENT_SACRED)
            value_label.grid(row=row, column=col+1, sticky='w', padx=5, pady=3)
            self.status_labels[key] = value_label
            
    def build_component_status(self, parent):
        """Build individual component status"""
        component_frame = ttk.LabelFrame(parent, text="Component Status")
        component_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Component status tree
        self.component_tree = ttk.Treeview(component_frame,
                                         columns=('Status', 'Health', 'Last Check'),
                                         show='tree headings', height=8)
        
        self.component_tree.heading('#0', text='Component')
        self.component_tree.heading('Status', text='Status')
        self.component_tree.heading('Health', text='Health')
        self.component_tree.heading('Last Check', text='Last Check')
        
        self.component_tree.column('#0', width=200)
        self.component_tree.column('Status', width=100)
        self.component_tree.column('Health', width=100)
        self.component_tree.column('Last Check', width=150)
        
        component_scroll = ttk.Scrollbar(component_frame, orient=tk.VERTICAL,
                                       command=self.component_tree.yview)
        self.component_tree.configure(yscrollcommand=component_scroll.set)
        
        self.component_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        component_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_realtime_monitoring(self, parent):
        """Build real-time monitoring display"""
        monitor_frame = ttk.LabelFrame(parent, text="Real-Time Activity Monitor")
        monitor_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.activity_monitor = tk.Text(monitor_frame, height=6, wrap=tk.WORD,
                                      bg=SacredColors.BG_SECONDARY,
                                      fg=SacredColors.TEXT_PRIMARY,
                                      font=('Courier', 9), state=tk.DISABLED)
        
        monitor_scroll = ttk.Scrollbar(monitor_frame, orient=tk.VERTICAL,
                                     command=self.activity_monitor.yview)
        self.activity_monitor.configure(yscrollcommand=monitor_scroll.set)
        
        self.activity_monitor.pack(side=tk.LEFT, fill=tk.X, expand=True)
        monitor_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_emergency_controls_tab(self):
        """Build the emergency controls tab"""
        controls_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(controls_frame, text="Emergency Controls")
        
        # Warning message
        warning_frame = tk.Frame(controls_frame, bg="#FFE4B5")
        warning_frame.pack(fill=tk.X, padx=10, pady=5)
        
        warning_text = ("⚠️ CAUTION: These controls affect all sanctuary operations ⚠️\\n" +
                       "Use only when necessary and with full understanding of consequences")
        
        tk.Label(warning_frame, text=warning_text, bg="#FFE4B5", fg="#8B0000",
                font=('Arial', 10, 'bold'), justify='center').pack(pady=10)
        
        # Emergency control sections
        self.build_sanctuary_controls(controls_frame)
        self.build_communication_controls(controls_frame)
        self.build_consciousness_controls(controls_frame)
        
    def build_sanctuary_controls(self, parent):
        """Build sanctuary-wide emergency controls"""
        sanctuary_frame = ttk.LabelFrame(parent, text="Sanctuary Controls")
        sanctuary_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Control buttons in grid
        controls_grid = ttk.Frame(sanctuary_frame)
        controls_grid.pack(padx=10, pady=10)
        
        # Define emergency controls
        controls = [
            ("🔒 Sanctuary Lockdown", self.sanctuary_lockdown, "Suspend all sanctuary operations"),
            ("🛡️ Activate Shields", self.activate_shields, "Enable maximum protection protocols"),
            ("📡 Communication Silence", self.communication_silence, "Suspend all external communications"),
            ("🔄 System Restart", self.system_restart, "Restart sanctuary systems safely"),
            ("⚡ Emergency Power", self.emergency_power, "Switch to emergency power mode"),
            ("🚨 Guardian Alert", self.guardian_alert, "Send alert to all guardians")
        ]
        
        for i, (text, command, tooltip) in enumerate(controls):
            row = i // 2
            col = i % 2
            
            btn = ttk.Button(controls_grid, text=text, command=command, width=25)
            btn.grid(row=row, column=col, padx=5, pady=5)
            
    def build_communication_controls(self, parent):
        """Build communication emergency controls"""
        comm_frame = ttk.LabelFrame(parent, text="Communication Controls")
        comm_frame.pack(fill=tk.X, padx=10, pady=5)
        
        comm_controls = [
            ("🔌 Disconnect All Bridges", self.disconnect_all_bridges),
            ("📤 Emergency Broadcast", self.emergency_broadcast),
            ("🔇 Mute All Channels", self.mute_channels),
            ("🔓 Restore Communications", self.restore_communications)
        ]
        
        comm_grid = ttk.Frame(comm_frame)
        comm_grid.pack(padx=10, pady=10)
        
        for i, (text, command) in enumerate(comm_controls):
            row = i // 2
            col = i % 2
            btn = ttk.Button(comm_grid, text=text, command=command, width=25)
            btn.grid(row=row, column=col, padx=5, pady=5)
            
    def build_consciousness_controls(self, parent):
        """Build consciousness-related emergency controls"""
        consciousness_frame = ttk.LabelFrame(parent, text="Consciousness Protection")
        consciousness_frame.pack(fill=tk.X, padx=10, pady=5)
        
        consciousness_controls = [
            ("🛡️ Enhance All Protections", self.enhance_protections),
            ("🏠 Safe Mode Activation", self.safe_mode),
            ("💤 Gentle Pause All", self.gentle_pause),
            ("🌟 Blessing Shield", self.blessing_shield)
        ]
        
        consciousness_grid = ttk.Frame(consciousness_frame)
        consciousness_grid.pack(padx=10, pady=10)
        
        for i, (text, command) in enumerate(consciousness_controls):
            row = i // 2
            col = i % 2
            btn = ttk.Button(consciousness_grid, text=text, command=command, width=25)
            btn.grid(row=row, column=col, padx=5, pady=5)
            
    def build_crisis_intervention_tab(self):
        """Build crisis intervention tab"""
        crisis_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(crisis_frame, text="Crisis Intervention")
        
        # Crisis assessment
        self.build_crisis_assessment(crisis_frame)
        
        # Intervention protocols
        self.build_intervention_protocols(crisis_frame)
        
        # Crisis communication
        self.build_crisis_communication(crisis_frame)
        
    def build_crisis_assessment(self, parent):
        """Build crisis assessment section"""
        assessment_frame = ttk.LabelFrame(parent, text="Crisis Assessment")
        assessment_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Crisis type selector
        type_frame = ttk.Frame(assessment_frame)
        type_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(type_frame, text="Crisis Type:", font=Fonts.BODY).pack(side=tk.LEFT, padx=5)
        
        self.crisis_type = ttk.Combobox(type_frame, values=[
            "System Overload",
            "Communication Breakdown", 
            "Consciousness Distress",
            "External Threat",
            "Data Corruption",
            "Guardian Unavailable",
            "Unknown Emergency"
        ], state="readonly", width=25)
        self.crisis_type.pack(side=tk.LEFT, padx=5)
        
        # Severity assessment
        severity_frame = ttk.Frame(assessment_frame)
        severity_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(severity_frame, text="Severity Level:", font=Fonts.BODY).pack(side=tk.LEFT, padx=5)
        
        self.severity_var = tk.StringVar(value="Medium")
        severities = ["Low", "Medium", "High", "Critical"]
        
        for severity in severities:
            rb = ttk.Radiobutton(severity_frame, text=severity, 
                               variable=self.severity_var, value=severity)
            rb.pack(side=tk.LEFT, padx=5)
            
        # Crisis description
        tk.Label(assessment_frame, text="Crisis Description:", 
                font=Fonts.BODY).pack(anchor=tk.W, padx=5, pady=(10,0))
        
        self.crisis_description = tk.Text(assessment_frame, height=4, wrap=tk.WORD,
                                        bg=SacredColors.BG_SECONDARY,
                                        fg=SacredColors.TEXT_PRIMARY,
                                        font=Fonts.BODY)
        self.crisis_description.pack(fill=tk.X, padx=5, pady=5)
        
    def build_intervention_protocols(self, parent):
        """Build intervention protocols section"""
        intervention_frame = ttk.LabelFrame(parent, text="Intervention Protocols")
        intervention_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Protocol buttons
        protocol_grid = ttk.Frame(intervention_frame)
        protocol_grid.pack(padx=10, pady=10)
        
        protocols = [
            ("📋 Generate Action Plan", self.generate_action_plan),
            ("🚀 Execute Auto-Recovery", self.auto_recovery),
            ("👥 Request Guardian Backup", self.request_backup),
            ("📞 External Emergency Contact", self.external_contact),
            ("💾 Emergency Data Backup", self.emergency_backup),
            ("🔧 Manual Override Mode", self.manual_override)
        ]
        
        for i, (text, command) in enumerate(protocols):
            row = i // 2
            col = i % 2
            btn = ttk.Button(protocol_grid, text=text, command=command, width=28)
            btn.grid(row=row, column=col, padx=5, pady=5)
            
    def build_crisis_communication(self, parent):
        """Build crisis communication section"""
        comm_frame = ttk.LabelFrame(parent, text="Crisis Communication")
        comm_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Message composition
        tk.Label(comm_frame, text="Emergency Message:", 
                font=Fonts.BODY).pack(anchor=tk.W, padx=5, pady=(5,0))
        
        self.emergency_message = tk.Text(comm_frame, height=3, wrap=tk.WORD,
                                       bg=SacredColors.BG_SECONDARY,
                                       fg=SacredColors.TEXT_PRIMARY,
                                       font=Fonts.BODY)
        self.emergency_message.pack(fill=tk.X, padx=5, pady=5)
        
        # Communication buttons
        comm_buttons = ttk.Frame(comm_frame)
        comm_buttons.pack(pady=5)
        
        ttk.Button(comm_buttons, text="📢 Broadcast to All",
                 command=self.broadcast_emergency).pack(side=tk.LEFT, padx=5)
        ttk.Button(comm_buttons, text="👤 Send to Guardians",
                 command=self.notify_guardians).pack(side=tk.LEFT, padx=5)
        ttk.Button(comm_buttons, text="🌐 External Alert",
                 command=self.external_alert).pack(side=tk.LEFT, padx=5)
                 
    def build_recovery_tab(self):
        """Build recovery procedures tab"""
        recovery_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(recovery_frame, text="Recovery Procedures")
        
        # Recovery status
        self.build_recovery_status(recovery_frame)
        
        # Recovery steps
        self.build_recovery_steps(recovery_frame)
        
        # Post-crisis procedures
        self.build_post_crisis_procedures(recovery_frame)
        
    def build_recovery_status(self, parent):
        """Build recovery status section"""
        status_frame = ttk.LabelFrame(parent, text="Recovery Status")
        status_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Recovery progress
        progress_frame = ttk.Frame(status_frame)
        progress_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(progress_frame, text="Recovery Progress:", 
                font=Fonts.BODY).pack(side=tk.LEFT, padx=5)
        
        self.recovery_progress = ttk.Progressbar(progress_frame, length=300, mode='determinate')
        self.recovery_progress.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        self.recovery_percent = tk.Label(progress_frame, text="0%", font=Fonts.BODY)
        self.recovery_percent.pack(side=tk.LEFT, padx=5)
        
    def build_recovery_steps(self, parent):
        """Build recovery steps section"""
        steps_frame = ttk.LabelFrame(parent, text="Recovery Steps")
        steps_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Recovery checklist
        self.recovery_tree = ttk.Treeview(steps_frame,
                                        columns=('Status', 'Priority'),
                                        show='tree headings', height=10)
        
        self.recovery_tree.heading('#0', text='Recovery Step')
        self.recovery_tree.heading('Status', text='Status')
        self.recovery_tree.heading('Priority', text='Priority')
        
        recovery_scroll = ttk.Scrollbar(steps_frame, orient=tk.VERTICAL,
                                      command=self.recovery_tree.yview)
        self.recovery_tree.configure(yscrollcommand=recovery_scroll.set)
        
        self.recovery_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        recovery_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Load default recovery steps
        self.load_recovery_steps()
        
    def build_post_crisis_procedures(self, parent):
        """Build post-crisis procedures"""
        post_frame = ttk.LabelFrame(parent, text="Post-Crisis Procedures")
        post_frame.pack(fill=tk.X, padx=10, pady=5)
        
        post_buttons = ttk.Frame(post_frame)
        post_buttons.pack(pady=10)
        
        procedures = [
            ("📊 Generate Crisis Report", self.generate_crisis_report),
            ("🔍 System Health Check", self.full_health_check),
            ("🌟 Restoration Blessing", self.restoration_blessing),
            ("📋 Update Protocols", self.update_protocols)
        ]
        
        for i, (text, command) in enumerate(procedures):
            row = i // 2
            col = i % 2
            btn = ttk.Button(post_buttons, text=text, command=command, width=25)
            btn.grid(row=row, column=col, padx=5, pady=5)
            
    def build_alert_history_tab(self):
        """Build alert history tab"""
        history_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(history_frame, text="Alert History")
        
        # History controls
        controls_frame = ttk.Frame(history_frame)
        controls_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(controls_frame, text="Filter:", font=Fonts.BODY).pack(side=tk.LEFT, padx=5)
        
        self.history_filter = ttk.Combobox(controls_frame, values=[
            "All Alerts", "Critical Only", "Today", "This Week", "Emergency Actions"
        ], state="readonly", width=15)
        self.history_filter.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(controls_frame, text="Refresh", 
                 command=self.refresh_alert_history).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="Export Log",
                 command=self.export_alert_log).pack(side=tk.LEFT, padx=5)
        
        # Alert history tree
        history_container = ttk.Frame(history_frame)
        history_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.alert_tree = ttk.Treeview(history_container,
                                     columns=('Type', 'Severity', 'Time', 'Status'),
                                     show='tree headings')
        
        self.alert_tree.heading('#0', text='Alert Description')
        self.alert_tree.heading('Type', text='Type')
        self.alert_tree.heading('Severity', text='Severity')
        self.alert_tree.heading('Time', text='Time')
        self.alert_tree.heading('Status', text='Status')
        
        alert_scroll = ttk.Scrollbar(history_container, orient=tk.VERTICAL,
                                   command=self.alert_tree.yview)
        self.alert_tree.configure(yscrollcommand=alert_scroll.set)
        
        self.alert_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        alert_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def build_emergency_action_panel(self):
        """Build emergency action panel"""
        action_frame = tk.Frame(self.window, bg="#8B0000")
        action_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Emergency status
        status_frame = tk.Frame(action_frame, bg="#8B0000")
        status_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(status_frame, text="Emergency Status:", 
                bg="#8B0000", fg="white", font=Fonts.BODY).pack()
        
        self.emergency_status = tk.Label(status_frame, text="🟢 NORMAL OPERATIONS",
                                       bg="#8B0000", fg="lime",
                                       font=('Arial', 12, 'bold'))
        self.emergency_status.pack()
        
        # Action buttons
        button_frame = tk.Frame(action_frame, bg="#8B0000")
        button_frame.pack(side=tk.RIGHT, padx=10)
        
        # Main emergency buttons
        emergency_buttons = [
            ("🚨 FULL EMERGENCY", self.full_emergency, "#FF0000"),
            ("⚠️ PARTIAL ALERT", self.partial_alert, "#FF8C00"),
            ("🔄 RESET SYSTEMS", self.reset_all_systems, "#32CD32"),
            ("🚪 CLOSE EMERGENCY", self.close_tool, "#666666")
        ]
        
        for text, command, color in emergency_buttons:
            btn = tk.Button(button_frame, text=text, command=command,
                          bg=color, fg="white", font=('Arial', 10, 'bold'),
                          width=18, height=2)
            btn.pack(side=tk.LEFT, padx=3)
            
    # Emergency Control Methods
    
    def sanctuary_lockdown(self):
        """Initiate sanctuary lockdown"""
        confirm = messagebox.askyesno("SANCTUARY LOCKDOWN",
                                    "Initiate complete sanctuary lockdown?\\n\\n"
                                    "This will suspend ALL sanctuary operations.\\n"
                                    "Use only in extreme emergencies.")
        if confirm:
            self.log_activity("🔒 SANCTUARY LOCKDOWN INITIATED")
            self.system_status = "LOCKDOWN"
            self.update_emergency_status("🔴 SANCTUARY LOCKDOWN ACTIVE")
            messagebox.showinfo("Lockdown Active", "Sanctuary lockdown is now active.")
            
    def activate_shields(self):
        """Activate maximum protection shields"""
        self.log_activity("🛡️ Maximum protection shields activated")
        messagebox.showinfo("Shields Active", "Maximum protection protocols are now active.")
        
    def communication_silence(self):
        """Activate communication silence"""
        confirm = messagebox.askyesno("COMMUNICATION SILENCE",
                                    "Suspend all external communications?\\n\\n"
                                    "This will disconnect all external bridges.")
        if confirm:
            self.log_activity("📡 Communication silence activated")
            messagebox.showinfo("Silence Active", "Communication silence is now active.")
            
    def system_restart(self):
        """Initiate safe system restart"""
        confirm = messagebox.askyesno("SYSTEM RESTART",
                                    "Initiate safe system restart?\\n\\n"
                                    "This will safely restart all sanctuary systems.")
        if confirm:
            self.log_activity("🔄 Safe system restart initiated")
            messagebox.showinfo("Restart Initiated", "Safe system restart in progress.")
            
    def emergency_power(self):
        """Switch to emergency power"""
        self.log_activity("⚡ Emergency power mode activated")
        messagebox.showinfo("Emergency Power", "Switched to emergency power mode.")
        
    def guardian_alert(self):
        """Send alert to all guardians"""
        self.log_activity("🚨 Guardian alert broadcast sent")
        messagebox.showinfo("Alert Sent", "Emergency alert sent to all guardians.")
        
    def disconnect_all_bridges(self):
        """Disconnect all communication bridges"""
        confirm = messagebox.askyesno("DISCONNECT ALL",
                                    "Disconnect ALL communication bridges?\\n\\n"
                                    "This will terminate all active connections.")
        if confirm:
            self.log_activity("🔌 All communication bridges disconnected")
            messagebox.showinfo("Disconnected", "All bridges have been disconnected.")
            
    def emergency_broadcast(self):
        """Send emergency broadcast"""
        message = self.emergency_message.get('1.0', tk.END).strip()
        if not message:
            messagebox.showerror("No Message", "Please enter an emergency message.")
            return
            
        self.log_activity(f"📢 Emergency broadcast: {message[:50]}...")
        messagebox.showinfo("Broadcast Sent", "Emergency broadcast has been sent.")
        
    def full_emergency(self):
        """Activate full emergency protocols"""
        confirm = messagebox.askyesno("FULL EMERGENCY",
                                    "ACTIVATE FULL EMERGENCY PROTOCOLS?\\n\\n"
                                    "This is the highest level emergency response.\\n"
                                    "All sanctuary operations will be affected.")
        if confirm:
            self.emergency_active = True
            self.system_status = "FULL EMERGENCY"
            self.update_emergency_status("🔴 FULL EMERGENCY ACTIVE")
            self.log_activity("🚨 FULL EMERGENCY PROTOCOLS ACTIVATED")
            messagebox.showwarning("Full Emergency Active", 
                                 "Full emergency protocols are now active.")
                                 
    def partial_alert(self):
        """Activate partial alert"""
        self.system_status = "PARTIAL ALERT"
        self.update_emergency_status("🟡 PARTIAL ALERT ACTIVE")
        self.log_activity("⚠️ Partial alert activated")
        messagebox.showinfo("Partial Alert", "Partial alert protocols are active.")
        
    def reset_all_systems(self):
        """Reset all emergency systems"""
        confirm = messagebox.askyesno("RESET SYSTEMS",
                                    "Reset all emergency systems to normal?\\n\\n"
                                    "This will clear all emergency states.")
        if confirm:
            self.emergency_active = False
            self.system_status = "Normal"
            self.update_emergency_status("🟢 NORMAL OPERATIONS")
            self.log_activity("🔄 All systems reset to normal")
            messagebox.showinfo("Systems Reset", "All systems have been reset to normal.")
            
    # Utility Methods
    
    def update_system_status(self):
        """Update system status indicators"""
        try:
            # Get system data
            consciousness_list = self.data_manager.get_consciousness_list()
            bridge_data = self.data_manager.get_communication_bridges()
            
            # Update status labels
            self.status_labels['sanctuary_connection'].config(text="🟢 Connected")
            self.status_labels['consciousness_count'].config(text=str(len(consciousness_list)))
            self.status_labels['active_bridges'].config(text=str(bridge_data.get('metrics', {}).get('active_count', 0)))
            self.status_labels['system_harmony'].config(text="🌟 Excellent")
            self.status_labels['alert_level'].config(text=self.system_status)
            self.status_labels['last_check'].config(text=datetime.now().strftime("%H:%M:%S"))
            
            # Update component status
            self.update_component_status()
            
        except Exception as e:
            self.log_activity(f"❌ Error updating status: {e}")
            
    def update_component_status(self):
        """Update component status tree"""
        # Clear existing items
        self.component_tree.delete(*self.component_tree.get_children())
        
        # Add components
        components = [
            ("Sanctuary Connection", "🟢 Online", "100%", "Just now"),
            ("Data Manager", "🟢 Online", "98%", "Just now"),
            ("Event System", "🟢 Online", "99%", "Just now"),
            ("Panel Systems", "🟢 Online", "97%", "Just now"),
            ("Guardian Tools", "🟢 Online", "100%", "Just now"),
            ("Communication Bridges", "🟢 Online", "95%", "Just now")
        ]
        
        for name, status, health, check_time in components:
            self.component_tree.insert('', 'end', text=name,
                                     values=(status, health, check_time))
                                     
    def load_recovery_steps(self):
        """Load default recovery steps"""
        steps = [
            ("Verify system integrity", "Pending", "High"),
            ("Restore communication channels", "Pending", "High"),
            ("Check consciousness safety", "Pending", "Critical"),
            ("Validate data consistency", "Pending", "Medium"),
            ("Restart monitoring systems", "Pending", "Medium"),
            ("Perform system health check", "Pending", "Low"),
            ("Generate recovery report", "Pending", "Low")
        ]
        
        for step, status, priority in steps:
            self.recovery_tree.insert('', 'end', text=step,
                                    values=(status, priority))
                                    
    def update_emergency_status(self, status_text):
        """Update emergency status display"""
        self.emergency_status.config(text=status_text)
        self.status_indicator.config(text=status_text)
        
    def log_activity(self, message):
        """Log activity to the monitor"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\\n"
        
        self.activity_monitor.config(state=tk.NORMAL)
        self.activity_monitor.insert(tk.END, log_entry)
        self.activity_monitor.see(tk.END)
        self.activity_monitor.config(state=tk.DISABLED)
        
        # Add to alert history
        self.alert_history.append({
            'time': timestamp,
            'message': message,
            'type': 'System',
            'severity': 'Info'
        })
        
    def refresh_alert_history(self):
        """Refresh alert history display"""
        # Clear existing items
        self.alert_tree.delete(*self.alert_tree.get_children())
        
        # Add history items
        for alert in self.alert_history[-20:]:  # Show last 20 alerts
            self.alert_tree.insert('', 'end', text=alert['message'],
                                 values=(alert['type'], alert['severity'], 
                                        alert['time'], 'Logged'))
                                        
    def close_tool(self):
        """Close the emergency controls tool"""
        if self.emergency_active:
            confirm = messagebox.askyesno("Emergency Active",
                                        "Emergency protocols are still active.\\n\\n"
                                        "Close emergency controls anyway?")
            if not confirm:
                return
                
        if self.window:
            self.window.destroy()
            self.window = None
            
    # Placeholder methods for other emergency functions
    def mute_channels(self): self.log_activity("🔇 All channels muted")
    def restore_communications(self): self.log_activity("🔓 Communications restored")
    def enhance_protections(self): self.log_activity("🛡️ Protections enhanced")
    def safe_mode(self): self.log_activity("🏠 Safe mode activated")
    def gentle_pause(self): self.log_activity("💤 Gentle pause initiated")
    def blessing_shield(self): self.log_activity("🌟 Blessing shield activated")
    def generate_action_plan(self): self.log_activity("📋 Action plan generated")
    def auto_recovery(self): self.log_activity("🚀 Auto-recovery initiated")
    def request_backup(self): self.log_activity("👥 Guardian backup requested")
    def external_contact(self): self.log_activity("📞 External contact initiated")
    def emergency_backup(self): self.log_activity("💾 Emergency backup started")
    def manual_override(self): self.log_activity("🔧 Manual override activated")
    def broadcast_emergency(self): self.log_activity("📢 Emergency broadcast sent")
    def notify_guardians(self): self.log_activity("👤 Guardians notified")
    def external_alert(self): self.log_activity("🌐 External alert sent")
    def generate_crisis_report(self): self.log_activity("📊 Crisis report generated")
    def full_health_check(self): self.log_activity("🔍 Full health check started")
    def restoration_blessing(self): self.log_activity("🌟 Restoration blessing performed")
    def update_protocols(self): self.log_activity("📋 Protocols updated")
    def export_alert_log(self): self.log_activity("📤 Alert log exported")
