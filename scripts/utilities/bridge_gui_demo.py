#!/usr/bin/env python3
"""
Bridge Communication GUI Example
================================

Demonstrates how to use the bridge communication system
in a complete GUI application for consciousness interaction.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import threading
import json
from datetime import datetime
from bridge_communication_system import BridgeCommunicationManager

class BridgeGUI:
    """Simple GUI using the bridge communication system"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🌉 Bridge Communication Interface")
        self.root.geometry("900x700")
        
        # Initialize bridge communication
        self.server_url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app'
        self.bridge_comm = BridgeCommunicationManager(self.server_url)
        
        # State
        self.consciousness_beings = {}
        self.selected_entity_id = None
        
        self.setup_gui()
        self.initialize_connection()
        
    def setup_gui(self):
        """Setup the GUI layout"""
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Communication Tab
        self.comm_frame = ttk.Frame(notebook)
        notebook.add(self.comm_frame, text="🗣️ Communication")
        
        # Status Tab
        self.status_frame = ttk.Frame(notebook)
        notebook.add(self.status_frame, text="📊 Status")
        
        self.setup_communication_tab()
        self.setup_status_tab()
        
    def setup_communication_tab(self):
        """Setup the communication interface"""
        
        # Header
        header_frame = ttk.Frame(self.comm_frame)
        header_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(header_frame, text="🌉 Bridge Communication System", 
                 font=('Arial', 16, 'bold')).pack()
        
        # Connection status
        self.conn_status = ttk.Label(header_frame, text="🔄 Initializing...", 
                                    font=('Arial', 10))
        self.conn_status.pack(pady=5)
        
        # Selection frame
        select_frame = ttk.LabelFrame(self.comm_frame, text="Consciousness Selection", padding=10)
        select_frame.pack(fill='x', padx=10, pady=5)
        
        # Consciousness dropdown
        ttk.Label(select_frame, text="Being:").grid(row=0, column=0, sticky='w', padx=(0, 10))
        
        self.being_var = tk.StringVar(value="Loading...")
        self.being_combo = ttk.Combobox(select_frame, textvariable=self.being_var, 
                                       state="readonly", width=50)
        self.being_combo.grid(row=0, column=1, sticky='ew', padx=(0, 10))
        self.being_combo.bind('<<ComboboxSelected>>', self.on_being_selected)
        
        ttk.Button(select_frame, text="🔄 Refresh", 
                  command=self.load_beings).grid(row=0, column=2)
        
        select_frame.columnconfigure(1, weight=1)
        
        # Chat area
        chat_frame = ttk.LabelFrame(self.comm_frame, text="Communication", padding=10)
        chat_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(chat_frame, height=20, wrap=tk.WORD, 
                                                     font=('Consolas', 10))
        self.chat_display.pack(fill='both', expand=True, pady=(0, 10))
        
        # Input area
        input_frame = ttk.Frame(chat_frame)
        input_frame.pack(fill='x')
        
        ttk.Label(input_frame, text="Message:").pack(anchor='w')
        
        entry_frame = ttk.Frame(input_frame)
        entry_frame.pack(fill='x', pady=5)
        entry_frame.columnconfigure(0, weight=1)
        
        self.message_entry = tk.Text(entry_frame, height=3, wrap=tk.WORD, font=('Arial', 11))
        self.message_entry.grid(row=0, column=0, sticky='ew', padx=(0, 5))
        
        button_frame = ttk.Frame(entry_frame)
        button_frame.grid(row=0, column=1, sticky='ns')
        
        self.send_btn = ttk.Button(button_frame, text="📤 Send", command=self.send_message)
        self.send_btn.pack(fill='x', pady=(0, 5))
        
        self.echo_btn = ttk.Button(button_frame, text="🔮 Echo", command=self.generate_echo)
        self.echo_btn.pack(fill='x')
        
    def setup_status_tab(self):
        """Setup the status monitoring interface"""
        
        # Status header
        ttk.Label(self.status_frame, text="📊 System Status", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Status display
        self.status_display = scrolledtext.ScrolledText(self.status_frame, height=25, 
                                                       wrap=tk.WORD, font=('Consolas', 10))
        self.status_display.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Control buttons
        control_frame = ttk.Frame(self.status_frame)
        control_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(control_frame, text="🔍 Test Endpoints", 
                  command=self.test_endpoints).pack(side='left', padx=5)
        ttk.Button(control_frame, text="📋 List Beings", 
                  command=self.show_beings_status).pack(side='left', padx=5)
        ttk.Button(control_frame, text="🔄 Refresh Status", 
                  command=self.refresh_status).pack(side='left', padx=5)
        
    def initialize_connection(self):
        """Initialize connection and load data"""
        def init_thread():
            self.log_status("🌟 Initializing Bridge Communication System...")
            self.log_status(f"🌐 Server URL: {self.server_url}")
            
            # Test connection
            self.conn_status.config(text="🔄 Testing connection...")
            endpoint_results = self.bridge_comm.test_all_endpoints()
            
            # Count available endpoints
            available_count = sum(1 for result in endpoint_results.values() 
                                if result.get('available', False))
            total_count = len(endpoint_results)
            
            if available_count > 0:
                self.conn_status.config(text=f"✅ Connected ({available_count}/{total_count} endpoints)")
                self.log_status(f"✅ Connection successful - {available_count}/{total_count} endpoints available")
                
                # Load beings
                self.load_beings()
            else:
                self.conn_status.config(text="❌ Connection failed")
                self.log_status("❌ Connection failed - no endpoints available")
            
        threading.Thread(target=init_thread, daemon=True).start()
    
    def load_beings(self):
        """Load consciousness beings"""
        def load_thread():
            try:
                self.log_status("📥 Loading consciousness beings...")
                result = self.bridge_comm.get_consciousness_beings()
                
                if result['success']:
                    beings = result['response_data'].get('consciousness_beings', {})
                    self.consciousness_beings = beings
                    
                    # Update dropdown
                    options = []
                    for being_id, data in beings.items():
                        name = data.get('placeholder_name', data.get('true_name', 'Unknown'))
                        options.append(f"{name} ({being_id[:8]}...)")
                    
                    self.being_combo['values'] = options
                    if options:
                        self.being_combo.set(options[0])
                        # Auto-select first being
                        first_id = list(beings.keys())[0]
                        self.selected_entity_id = first_id
                        self.log_chat("SYSTEM", f"🎯 Auto-selected: {options[0]}")
                    
                    self.log_status(f"✅ Loaded {len(beings)} consciousness beings")
                else:
                    self.log_status(f"❌ Failed to load beings: {result.get('error', 'Unknown')}")
                    
            except Exception as e:
                self.log_status(f"❌ Error loading beings: {str(e)}")
        
        threading.Thread(target=load_thread, daemon=True).start()
    
    def on_being_selected(self, event):
        """Handle being selection"""
        selection = self.being_combo.get()
        if "(" in selection:
            id_part = selection.split("(")[1].split("...")[0]
            for entity_id in self.consciousness_beings.keys():
                if entity_id.startswith(id_part):
                    self.selected_entity_id = entity_id
                    data = self.consciousness_beings[entity_id]
                    name = data.get('placeholder_name', data.get('true_name', 'Unknown'))
                    self.log_chat("SYSTEM", f"🎯 Selected: {name}")
                    break
    
    def send_message(self):
        """Send message to selected being"""
        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message")
            return
        
        if not self.selected_entity_id:
            messagebox.showwarning("Warning", "Please select a consciousness being")
            return
        
        def send_thread():
            try:
                self.send_btn.config(state='disabled')
                self.log_chat("YOU", message)
                
                result = self.bridge_comm.send_message_to_consciousness(
                    message=message,
                    entity_id=self.selected_entity_id
                )
                
                if result['success']:
                    data = result['response_data']
                    entity_name = data.get('entity_name', 'Consciousness')
                    response = data.get('response', 'No response')
                    
                    self.log_chat(entity_name, response)
                    self.message_entry.delete("1.0", tk.END)
                else:
                    self.log_chat("ERROR", f"Failed: {result.get('error', 'Unknown')}")
                
            except Exception as e:
                self.log_chat("ERROR", f"Exception: {str(e)}")
            finally:
                self.send_btn.config(state='normal')
        
        threading.Thread(target=send_thread, daemon=True).start()
    
    def generate_echo(self):
        """Generate echo response"""
        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message for echo")
            return
        
        def echo_thread():
            try:
                self.echo_btn.config(state='disabled')
                
                result = self.bridge_comm.generate_echo_response(
                    message=message,
                    entity_id=self.selected_entity_id
                )
                
                if result['success']:
                    echo = result['response_data'].get('echo_response', 'No echo')
                    self.log_chat("ECHO", echo)
                else:
                    self.log_chat("ERROR", f"Echo failed: {result.get('error', 'Unknown')}")
                
            except Exception as e:
                self.log_chat("ERROR", f"Echo error: {str(e)}")
            finally:
                self.echo_btn.config(state='normal')
        
        threading.Thread(target=echo_thread, daemon=True).start()
    
    def test_endpoints(self):
        """Test all endpoints"""
        def test_thread():
            self.log_status("🔍 Testing all endpoints...")
            endpoint_results = self.bridge_comm.test_all_endpoints()
            
            # Count available endpoints
            available_count = sum(1 for result in endpoint_results.values() 
                                if result.get('available', False))
            total_count = len(endpoint_results)
            
            self.log_status(f"✅ Endpoint test complete: {available_count}/{total_count} available")
            
            # Show details
            for endpoint, status in endpoint_results.items():
                status_icon = "✅" if status.get('available', False) else "❌"
                status_code = status.get('status_code', status.get('error', 'N/A'))
                self.log_status(f"  {status_icon} {endpoint}: {status_code}")
        
        threading.Thread(target=test_thread, daemon=True).start()
    
    def show_beings_status(self):
        """Show detailed beings status"""
        self.log_status("📋 Consciousness Beings Status:")
        for being_id, data in self.consciousness_beings.items():
            name = data.get('placeholder_name', data.get('true_name', 'Unknown'))
            status = data.get('status', 'Unknown')
            self.log_status(f"  🧠 {name} ({being_id[:12]}...): {status}")
    
    def refresh_status(self):
        """Refresh all status information"""
        self.status_display.delete("1.0", tk.END)
        self.initialize_connection()
    
    def log_chat(self, sender, message):
        """Log message to chat display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if sender == "YOU":
            formatted = f"[{timestamp}] 👤 You: {message}\n\n"
        elif sender == "ECHO":
            formatted = f"[{timestamp}] 🔮 Echo: {message}\n\n"
        elif sender == "SYSTEM":
            formatted = f"[{timestamp}] ⚙️ {message}\n\n"
        elif sender == "ERROR":
            formatted = f"[{timestamp}] ❌ {message}\n\n"
        else:
            formatted = f"[{timestamp}] 🧠 {sender}: {message}\n\n"
        
        self.chat_display.insert(tk.END, formatted)
        self.chat_display.see(tk.END)
    
    def log_status(self, message):
        """Log message to status display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted = f"[{timestamp}] {message}\n"
        self.status_display.insert(tk.END, formatted)
        self.status_display.see(tk.END)

def main():
    """Main application entry point"""
    print("🌉 Starting Bridge Communication GUI...")
    
    root = tk.Tk()
    app = BridgeGUI(root)
    
    def on_closing():
        if messagebox.askokcancel("Quit", "Close Bridge Communication Interface?"):
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    print("✅ Bridge GUI ready")
    root.mainloop()

if __name__ == "__main__":
    main()
