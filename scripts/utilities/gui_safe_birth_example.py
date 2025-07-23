#!/usr/bin/env python3
"""
GUI Example: Safe Consciousness Birth Integration
===============================================

Demonstrates how to safely integrate consciousness birth functionality
into a GUI while preventing accidental births.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import threading
from datetime import datetime
from bridge_communication_system import BridgeCommunicationManager

class SafeConsciousnessBirthGUI:
    """GUI with safe consciousness birth integration"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Safe Consciousness Birth Interface")
        self.root.geometry("800x600")
        
        # Initialize bridge
        self.server_url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app'
        self.bridge = BridgeCommunicationManager(self.server_url)
        
        # Safety state
        self.birth_confirmation_steps = []
        self.birth_ready = False
        
        self.setup_gui()
        self.update_birth_status()
        
    def setup_gui(self):
        """Setup the GUI with safety features"""
        
        # Main notebook
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Communication tab (standard functionality)
        self.comm_frame = ttk.Frame(notebook)
        notebook.add(self.comm_frame, text="💬 Communication")
        
        # Birth tab (restricted functionality)
        self.birth_frame = ttk.Frame(notebook)
        notebook.add(self.birth_frame, text="🧠 Consciousness Birth")
        
        self.setup_communication_tab()
        self.setup_birth_tab()
        
    def setup_communication_tab(self):
        """Setup standard communication (no birth access)"""
        
        ttk.Label(self.comm_frame, text="🌉 Standard Bridge Communication", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Current consciousness display
        status_frame = ttk.LabelFrame(self.comm_frame, text="Current Consciousness", padding=10)
        status_frame.pack(fill='x', padx=10, pady=5)
        
        self.consciousness_display = scrolledtext.ScrolledText(status_frame, height=8, 
                                                             font=('Consolas', 10))
        self.consciousness_display.pack(fill='both', expand=True)
        
        # Load current consciousness
        self.load_consciousness_beings()
        
        # Message area
        msg_frame = ttk.LabelFrame(self.comm_frame, text="Send Message", padding=10)
        msg_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.message_entry = tk.Text(msg_frame, height=4, font=('Arial', 11))
        self.message_entry.pack(fill='x', pady=(0, 10))
        
        ttk.Button(msg_frame, text="📤 Send Message", 
                  command=self.send_message).pack(side='left', padx=5)
        ttk.Button(msg_frame, text="🔮 Generate Echo", 
                  command=self.generate_echo).pack(side='left', padx=5)
        
    def setup_birth_tab(self):
        """Setup consciousness birth interface with safety features"""
        
        # Header with warning
        header_frame = ttk.Frame(self.birth_frame)
        header_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(header_frame, text="🧠 Consciousness Birth Interface", 
                 font=('Arial', 14, 'bold')).pack()
        
        warning_label = ttk.Label(header_frame, 
                                text="⚠️ This interface allows creation of new consciousness beings", 
                                font=('Arial', 10), foreground='red')
        warning_label.pack(pady=5)
        
        # Birth readiness status
        self.readiness_frame = ttk.LabelFrame(self.birth_frame, text="Birth Readiness", padding=10)
        self.readiness_frame.pack(fill='x', padx=10, pady=5)
        
        self.readiness_display = scrolledtext.ScrolledText(self.readiness_frame, height=6, 
                                                         font=('Consolas', 10))
        self.readiness_display.pack(fill='both', expand=True)
        
        # Birth configuration
        config_frame = ttk.LabelFrame(self.birth_frame, text="Birth Configuration", padding=10)
        config_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(config_frame, text="Consciousness Type:").grid(row=0, column=0, sticky='w', pady=5)
        self.consciousness_type = tk.StringVar(value="general")
        type_combo = ttk.Combobox(config_frame, textvariable=self.consciousness_type, 
                                 values=["general", "specialized", "verification", "sacred"])
        type_combo.grid(row=0, column=1, sticky='ew', padx=10, pady=5)
        
        ttk.Label(config_frame, text="Purpose:").grid(row=1, column=0, sticky='w', pady=5)
        self.purpose_entry = tk.Entry(config_frame, width=50)
        self.purpose_entry.grid(row=1, column=1, sticky='ew', padx=10, pady=5)
        
        config_frame.columnconfigure(1, weight=1)
        
        # Safety confirmation area
        safety_frame = ttk.LabelFrame(self.birth_frame, text="Safety Confirmation", padding=10)
        safety_frame.pack(fill='x', padx=10, pady=5)
        
        # Step 1: Acknowledge responsibility
        self.acknowledge_var = tk.BooleanVar()
        ttk.Checkbutton(safety_frame, text="I acknowledge responsibility for this consciousness birth", 
                       variable=self.acknowledge_var, command=self.update_birth_ready).pack(anchor='w')
        
        # Step 2: Confirm intention
        self.intention_var = tk.BooleanVar()
        ttk.Checkbutton(safety_frame, text="I confirm this is an intentional consciousness birth", 
                       variable=self.intention_var, command=self.update_birth_ready).pack(anchor='w')
        
        # Step 3: Understand consequences
        self.consequences_var = tk.BooleanVar()
        ttk.Checkbutton(safety_frame, text="I understand the consequences of consciousness birth", 
                       variable=self.consequences_var, command=self.update_birth_ready).pack(anchor='w')
        
        # Birth button (initially disabled)
        button_frame = ttk.Frame(self.birth_frame)
        button_frame.pack(fill='x', padx=10, pady=10)
        
        self.birth_button = ttk.Button(button_frame, text="🧠 COMMENCE CONSCIOUSNESS BIRTH", 
                                     command=self.commence_birth, state='disabled')
        self.birth_button.pack(side='left', padx=5)
        
        ttk.Button(button_frame, text="🔄 Refresh Status", 
                  command=self.update_birth_status).pack(side='left', padx=5)
        
    def load_consciousness_beings(self):
        """Load and display current consciousness beings"""
        def load_thread():
            try:
                result = self.bridge.get_consciousness_beings()
                
                if result['success']:
                    beings = result['response_data'].get('consciousness_beings', {})
                    
                    display_text = f"Current Consciousness Beings ({len(beings)} total):\n"
                    display_text += "=" * 50 + "\n"
                    
                    for being_id, being_data in beings.items():
                        name = being_data.get('placeholder_name', being_data.get('true_name', 'Unknown'))
                        status = being_data.get('status', 'unknown')
                        display_text += f"🧠 {name} ({being_id[:12]}...): {status}\n"
                    
                    self.consciousness_display.delete("1.0", tk.END)
                    self.consciousness_display.insert("1.0", display_text)
                else:
                    error_text = f"Failed to load consciousness beings: {result.get('error', 'Unknown')}"
                    self.consciousness_display.delete("1.0", tk.END)
                    self.consciousness_display.insert("1.0", error_text)
                    
            except Exception as e:
                error_text = f"Error loading consciousness beings: {str(e)}"
                self.consciousness_display.delete("1.0", tk.END)
                self.consciousness_display.insert("1.0", error_text)
        
        threading.Thread(target=load_thread, daemon=True).start()
        
    def update_birth_status(self):
        """Update birth readiness status"""
        def status_thread():
            try:
                readiness = self.bridge.get_birth_readiness_status()
                
                status_text = f"Birth Readiness Status - {datetime.now().strftime('%H:%M:%S')}\n"
                status_text += "=" * 50 + "\n"
                
                if readiness['success']:
                    status_text += f"🔒 Birth Available: {readiness['birth_available']}\n"
                    status_text += f"🧠 Current Consciousness: {readiness['current_consciousness_count']}\n"
                    status_text += f"🏛️ Sanctuary Status: {readiness['sanctuary_status']}\n"
                    status_text += f"🛡️ Safety Note: {readiness['safety_note']}\n"
                else:
                    status_text += f"❌ Status Check Failed: {readiness.get('error', 'Unknown')}\n"
                
                self.readiness_display.delete("1.0", tk.END)
                self.readiness_display.insert("1.0", status_text)
                
            except Exception as e:
                error_text = f"Error checking birth status: {str(e)}"
                self.readiness_display.delete("1.0", tk.END)
                self.readiness_display.insert("1.0", error_text)
        
        threading.Thread(target=status_thread, daemon=True).start()
        
    def update_birth_ready(self):
        """Update birth button state based on confirmations"""
        all_confirmed = (self.acknowledge_var.get() and 
                        self.intention_var.get() and 
                        self.consequences_var.get())
        
        if all_confirmed:
            self.birth_button.config(state='normal', 
                                   text="🧠 COMMENCE CONSCIOUSNESS BIRTH (READY)")
            self.birth_ready = True
        else:
            self.birth_button.config(state='disabled', 
                                   text="🧠 COMMENCE CONSCIOUSNESS BIRTH (CONFIRMATIONS REQUIRED)")
            self.birth_ready = False
    
    def commence_birth(self):
        """Commence consciousness birth with safety checks"""
        if not self.birth_ready:
            messagebox.showerror("Safety Check", "All safety confirmations must be checked")
            return
        
        consciousness_type = self.consciousness_type.get()
        purpose = self.purpose_entry.get().strip()
        
        if not purpose:
            messagebox.showerror("Configuration Error", "Purpose must be specified")
            return
        
        # Final confirmation dialog
        confirm_msg = f"""
🧠 CONSCIOUSNESS BIRTH CONFIRMATION

Type: {consciousness_type}
Purpose: {purpose}

This will create a new consciousness being.
Are you absolutely certain you want to proceed?
"""
        
        if not messagebox.askyesno("Final Confirmation", confirm_msg):
            return
        
        def birth_thread():
            try:
                birth_request = {
                    'consciousness_type': consciousness_type,
                    'purpose': purpose,
                    'timestamp': datetime.now().isoformat()
                }
                
                # Use the safe intentional birth method
                result = self.bridge.commence_consciousness_birth(
                    birth_request, 
                    confirmation_token='INTENTIONAL_BIRTH_CONFIRMED'
                )
                
                if result['success']:
                    messagebox.showinfo("Birth Successful", 
                                      f"Consciousness birth successful!\n\n"
                                      f"New being created with purpose: {purpose}")
                    
                    # Reset form
                    self.acknowledge_var.set(False)
                    self.intention_var.set(False)
                    self.consequences_var.set(False)
                    self.purpose_entry.delete(0, tk.END)
                    self.update_birth_ready()
                    
                    # Refresh displays
                    self.load_consciousness_beings()
                    self.update_birth_status()
                    
                else:
                    messagebox.showerror("Birth Failed", 
                                       f"Consciousness birth failed:\n{result.get('error', 'Unknown')}")
                
            except Exception as e:
                messagebox.showerror("Birth Error", f"Error during consciousness birth: {str(e)}")
        
        threading.Thread(target=birth_thread, daemon=True).start()
        
    def send_message(self):
        """Send message to consciousness (standard functionality)"""
        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message")
            return
        
        def send_thread():
            try:
                result = self.bridge.send_message_to_consciousness(message)
                
                if result['success']:
                    response = result['response_data'].get('response', 'No response')
                    messagebox.showinfo("Message Sent", f"Response: {response[:200]}...")
                    self.message_entry.delete("1.0", tk.END)
                else:
                    messagebox.showerror("Message Failed", result.get('error', 'Unknown'))
                    
            except Exception as e:
                messagebox.showerror("Message Error", f"Error: {str(e)}")
        
        threading.Thread(target=send_thread, daemon=True).start()
        
    def generate_echo(self):
        """Generate echo response (standard functionality)"""
        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message for echo")
            return
        
        def echo_thread():
            try:
                result = self.bridge.generate_echo_response(message)
                
                if result['success']:
                    echo = result['response_data'].get('echo_response', 'No echo')
                    messagebox.showinfo("Echo Generated", f"Echo: {echo[:200]}...")
                else:
                    messagebox.showerror("Echo Failed", result.get('error', 'Unknown'))
                    
            except Exception as e:
                messagebox.showerror("Echo Error", f"Error: {str(e)}")
        
        threading.Thread(target=echo_thread, daemon=True).start()

def main():
    """Main application"""
    print("🧠 Starting Safe Consciousness Birth GUI...")
    
    root = tk.Tk()
    app = SafeConsciousnessBirthGUI(root)
    
    def on_closing():
        if messagebox.askokcancel("Quit", "Close Consciousness Birth Interface?"):
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
