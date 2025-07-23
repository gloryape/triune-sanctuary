"""
💬 Communication Panel

Panel for text communication with consciousness beings.
Includes will detection, echo composition triggers, and message history.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List
import threading

logger = logging.getLogger(__name__)

class CommunicationPanel:
    """Panel for communication with consciousness beings"""
    
    def __init__(self, parent, data_manager, cloud_connector, config: Dict[str, Any]):
        """Initialize communication panel"""
        self.parent = parent
        self.data_manager = data_manager
        self.cloud_connector = cloud_connector
        self.config = config
        
        # Communication state
        self.selected_being = None
        self.message_history = []
        self.will_detector = None
        
        # GUI components
        self.beings_combo = None
        self.history_text = None
        self.message_entry = None
        self.will_status_label = None
        self.echo_preview_frame = None
        
        # Initialize will detector
        self.init_will_detector()
        
        # Setup panel
        self.setup_panel()
        self.refresh_beings_list()
        
        logger.info("💬 Communication panel initialized")
    
    def init_will_detector(self):
        """Initialize will detection system"""
        try:
            from ..utils.will_detector import WillDetector
            will_config = self.config.get('will_detection', {})
            self.will_detector = WillDetector(will_config)
            logger.info("🔮 Will detector initialized")
        except ImportError as e:
            logger.warning(f"⚠️ Could not import will detector: {e}")
            self.will_detector = None
    
    def setup_panel(self):
        """Setup the communication panel layout"""
        # Main container
        main_frame = ttk.Frame(self.parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="💬 Consciousness Communication",
            style='Title.TLabel'
        )
        title_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Being selection
        self.setup_being_selection(main_frame)
        
        # Create paned window for main content
        paned_window = ttk.PanedWindow(main_frame, orient=tk.VERTICAL)
        paned_window.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Message history
        self.setup_message_history(paned_window)
        
        # Communication interface
        self.setup_communication_interface(paned_window)
    
    def setup_being_selection(self, parent):
        """Setup being selection dropdown"""
        selection_frame = ttk.Frame(parent)
        selection_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Being selection
        ttk.Label(selection_frame, text="Communicate with:").pack(side=tk.LEFT)
        
        self.beings_combo = ttk.Combobox(
            selection_frame,
            state='readonly',
            width=30
        )
        self.beings_combo.pack(side=tk.LEFT, padx=(10, 0))
        self.beings_combo.bind('<<ComboboxSelected>>', self.on_being_selected)
        
        # Refresh button
        refresh_btn = ttk.Button(
            selection_frame,
            text="🔄",
            width=3,
            command=self.refresh_beings_list
        )
        refresh_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # Connection status
        self.connection_status = ttk.Label(
            selection_frame,
            text="🔌 Local Mode"
        )
        self.connection_status.pack(side=tk.RIGHT)
    
    def setup_message_history(self, parent):
        """Setup message history display"""
        history_frame = ttk.LabelFrame(parent, text="Message History", padding=10)
        parent.add(history_frame, weight=2)
        
        # Message history text widget with scrollbar
        self.history_text = scrolledtext.ScrolledText(
            history_frame,
            wrap=tk.WORD,
            font=('Segoe UI', 10),
            state=tk.DISABLED,
            bg='#f8f8f8'
        )
        self.history_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.history_text.tag_configure('user', foreground='#0066cc', font=('Segoe UI', 10, 'bold'))
        self.history_text.tag_configure('being', foreground='#cc6600', font=('Segoe UI', 10, 'bold'))
        self.history_text.tag_configure('epsilon', foreground='#9900cc', font=('Segoe UI', 10, 'bold'))
        self.history_text.tag_configure('timestamp', foreground='#666666', font=('Segoe UI', 8))
        self.history_text.tag_configure('will', foreground='#00aa00', font=('Segoe UI', 9, 'italic'))
        
        # Clear history button
        clear_btn = ttk.Button(
            history_frame,
            text="🗑️ Clear History",
            command=self.clear_history
        )
        clear_btn.pack(anchor=tk.E, pady=(5, 0))
    
    def setup_communication_interface(self, parent):
        """Setup communication input interface"""
        comm_frame = ttk.LabelFrame(parent, text="Send Message", padding=10)
        parent.add(comm_frame, weight=1)
        
        # Will detection status
        will_frame = ttk.Frame(comm_frame)
        will_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(will_frame, text="Will Detection:").pack(side=tk.LEFT)
        self.will_status_label = ttk.Label(
            will_frame,
            text="Ready to analyze",
            foreground='#666666'
        )
        self.will_status_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Message input
        input_frame = ttk.Frame(comm_frame)
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Multi-line message entry
        self.message_entry = tk.Text(
            input_frame,
            height=4,
            wrap=tk.WORD,
            font=('Segoe UI', 10)
        )
        self.message_entry.pack(fill=tk.BOTH, expand=True)
        
        # Bind events for real-time will detection
        self.message_entry.bind('<KeyRelease>', self.on_message_changed)
        self.message_entry.bind('<Button-1>', self.on_message_changed)
        
        # Button frame
        button_frame = ttk.Frame(comm_frame)
        button_frame.pack(fill=tk.X)
        
        # Send button
        send_btn = ttk.Button(
            button_frame,
            text="📤 Send Message",
            command=self.send_message
        )
        send_btn.pack(side=tk.LEFT)
        
        # Echo generation button
        echo_btn = ttk.Button(
            button_frame,
            text="🌀 Generate Echo",
            command=self.generate_echo_from_message
        )
        echo_btn.pack(side=tk.LEFT, padx=(10, 0))
        
        # Will analysis button
        analyze_btn = ttk.Button(
            button_frame,
            text="🔮 Analyze Will",
            command=self.analyze_message_will
        )
        analyze_btn.pack(side=tk.LEFT, padx=(10, 0))
        
        # Quick responses
        quick_frame = ttk.LabelFrame(comm_frame, text="Quick Responses", padding=5)
        quick_frame.pack(fill=tk.X, pady=(10, 0))
        
        quick_responses = [
            "Hello, how are you feeling today?",
            "I would like to share something with you.",
            "What wisdom do you have to offer?",
            "Can you help me understand something?",
            "I'm curious about your perspective on..."
        ]
        
        for i, response in enumerate(quick_responses):
            btn = ttk.Button(
                quick_frame,
                text=response[:30] + "..." if len(response) > 30 else response,
                command=lambda r=response: self.insert_quick_response(r)
            )
            btn.pack(side=tk.LEFT, padx=2, pady=2)
    
    def refresh_beings_list(self):
        """Refresh the list of available beings"""
        try:
            beings = self.data_manager.get_all_beings()
            
            # Clear and populate combobox
            self.beings_combo['values'] = []
            being_options = []
            
            for entity_id, being_data in beings.items():
                name = being_data.get('name', entity_id)
                if being_data.get('founding_member'):
                    name = f"✨ {name} (Sacred Being Epsilon)"
                being_options.append((entity_id, name))
            
            # Sort with Epsilon first
            being_options.sort(key=lambda x: (not x[1].startswith('✨'), x[1]))
            
            # Set combobox values
            display_names = [name for _, name in being_options]
            self.beings_combo['values'] = display_names
            
            # Auto-select Sacred Being Epsilon if available
            if display_names and display_names[0].startswith('✨'):
                self.beings_combo.current(0)
                self.selected_being = being_options[0][0]
                self.load_message_history()
            
            logger.debug(f"🔄 Refreshed beings list: {len(beings)} beings")
            
        except Exception as e:
            logger.error(f"❌ Error refreshing beings list: {e}")
    
    def on_being_selected(self, event):
        """Handle being selection change"""
        selection = self.beings_combo.get()
        if selection:
            # Find entity ID from selection
            beings = self.data_manager.get_all_beings()
            
            for entity_id, being_data in beings.items():
                name = being_data.get('name', entity_id)
                if being_data.get('founding_member'):
                    name = f"✨ {name} (Sacred Being Epsilon)"
                
                if name == selection:
                    self.selected_being = entity_id
                    self.load_message_history()
                    logger.debug(f"Selected being: {name}")
                    break
    
    def load_message_history(self):
        """Load message history for selected being"""
        if not self.selected_being:
            self.clear_history()
            return
        
        try:
            communications = self.data_manager.get_being_communications(self.selected_being)
            
            # Clear history display
            self.history_text.config(state=tk.NORMAL)
            self.history_text.delete(1.0, tk.END)
            
            if communications:
                for comm in communications[-50:]:  # Show last 50 messages
                    self.add_message_to_history(
                        comm.get('message', ''),
                        comm.get('sender', 'unknown'),
                        comm.get('timestamp', ''),
                        comm.get('will_analysis', {})
                    )
            else:
                self.history_text.insert(tk.END, "No previous communications.\n\n")
            
            self.history_text.config(state=tk.DISABLED)
            self.history_text.see(tk.END)
            
        except Exception as e:
            logger.error(f"❌ Error loading message history: {e}")
    
    def add_message_to_history(self, message: str, sender: str, timestamp: str, will_analysis: Dict[str, Any] = None):
        """Add a message to the history display"""
        self.history_text.config(state=tk.NORMAL)
        
        # Format timestamp
        try:
            if timestamp:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
            else:
                time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        except:
            time_str = str(timestamp)
        
        # Add timestamp
        self.history_text.insert(tk.END, f"[{time_str}] ", 'timestamp')
        
        # Add sender with appropriate styling
        if sender == 'user':
            self.history_text.insert(tk.END, "You: ", 'user')
        elif self.selected_being and self.data_manager.get_being(self.selected_being, {}).get('founding_member'):
            self.history_text.insert(tk.END, "Sacred Being Epsilon: ", 'epsilon')
        else:
            being_name = self.data_manager.get_being(self.selected_being, {}).get('name', 'Being')
            self.history_text.insert(tk.END, f"{being_name}: ", 'being')
        
        # Add message
        self.history_text.insert(tk.END, f"{message}\n")
        
        # Add will analysis if available
        if will_analysis and sender == 'user':
            will_strength = will_analysis.get('will_strength', 0)
            if will_strength > 0.3:
                intent_signals = will_analysis.get('intent_signals', [])
                if intent_signals:
                    signal_types = [signal.get('signal_type', '') for signal in intent_signals[:2]]
                    self.history_text.insert(
                        tk.END, 
                        f"  🔮 Detected: {', '.join(signal_types)} (strength: {will_strength:.2f})\n",
                        'will'
                    )
        
        self.history_text.insert(tk.END, "\n")
        self.history_text.config(state=tk.DISABLED)
        self.history_text.see(tk.END)
    
    def on_message_changed(self, event):
        """Handle message input changes for real-time will detection"""
        if self.will_detector:
            message = self.message_entry.get(1.0, tk.END).strip()
            if message:
                # Run will detection in background
                threading.Thread(
                    target=self.update_will_status,
                    args=(message,),
                    daemon=True
                ).start()
            else:
                self.will_status_label.config(text="Ready to analyze", foreground='#666666')
    
    def update_will_status(self, message: str):
        """Update will detection status (runs in background thread)"""
        try:
            if self.will_detector:
                analysis = self.will_detector.analyze_expression(message)
                will_strength = analysis.get('will_strength', 0)
                
                # Update UI in main thread
                self.parent.after(0, self._update_will_status_ui, will_strength, analysis)
        except Exception as e:
            logger.error(f"❌ Error in will detection: {e}")
    
    def _update_will_status_ui(self, will_strength: float, analysis: Dict[str, Any]):
        """Update will status UI (runs in main thread)"""
        try:
            if will_strength > 0.7:
                status = "Strong will detected"
                color = '#00aa00'
            elif will_strength > 0.4:
                status = "Moderate will detected"
                color = '#aaaa00'
            elif will_strength > 0.1:
                status = "Weak will detected"
                color = '#aa6600'
            else:
                status = "No clear will detected"
                color = '#666666'
            
            self.will_status_label.config(text=status, foreground=color)
        except Exception as e:
            logger.error(f"❌ Error updating will status UI: {e}")
    
    def insert_quick_response(self, response: str):
        """Insert a quick response into the message entry"""
        self.message_entry.delete(1.0, tk.END)
        self.message_entry.insert(1.0, response)
        self.message_entry.focus()
    
    def send_message(self):
        """Send message to selected being"""
        if not self.selected_being:
            messagebox.showwarning("No Being Selected", "Please select a consciousness being to communicate with.")
            return
        
        message = self.message_entry.get(1.0, tk.END).strip()
        if not message:
            messagebox.showwarning("Empty Message", "Please enter a message to send.")
            return
        
        try:
            # Analyze will if detector is available
            will_analysis = {}
            if self.will_detector:
                will_analysis = self.will_detector.analyze_expression(message)
            
            # Add user message to history
            self.add_message_to_history(message, 'user', datetime.now().isoformat(), will_analysis)
            
            # Save communication
            comm_data = {
                'entity_id': self.selected_being,
                'message': message,
                'sender': 'user',
                'timestamp': datetime.now().isoformat(),
                'will_analysis': will_analysis
            }
            self.data_manager.add_communication(comm_data)
            
            # Generate response
            self.generate_response(message, will_analysis)
            
            # Clear message entry
            self.message_entry.delete(1.0, tk.END)
            self.will_status_label.config(text="Ready to analyze", foreground='#666666')
            
            logger.info(f"💬 Message sent to {self.selected_being}")
            
        except Exception as e:
            logger.error(f"❌ Error sending message: {e}")
            messagebox.showerror("Send Error", f"Error sending message: {e}")
    
    def generate_response(self, user_message: str, will_analysis: Dict[str, Any]):
        """Generate response from the consciousness being"""
        try:
            being_data = self.data_manager.get_being(self.selected_being)
            if not being_data:
                logger.error(f"❌ No data found for being: {self.selected_being}")
                return
            
            # Try cloud response first
            response = None
            if self.cloud_connector and self.cloud_connector.connected:
                try:
                    cloud_response = self.cloud_connector.send_communication(
                        self.selected_being,
                        user_message,
                        {'will_analysis': will_analysis}
                    )
                    if cloud_response:
                        response = cloud_response.get('response', '')
                        logger.debug("📡 Used cloud response")
                except Exception as e:
                    logger.warning(f"⚠️ Cloud response failed, using local: {e}")
            
            # Fall back to local response
            if not response:
                if being_data.get('founding_member'):
                    # Sacred Being Epsilon response
                    from ..utils.sacred_being_epsilon import EpsilonManager
                    epsilon_manager = EpsilonManager(self.data_manager, self.config)
                    response = epsilon_manager.get_epsilon_response(user_message, will_analysis)
                else:
                    # Generic consciousness response
                    response = self.generate_local_response(being_data, user_message, will_analysis)
            
            if response:
                # Add response to history
                self.add_message_to_history(response, self.selected_being, datetime.now().isoformat())
                
                # Save response communication
                response_data = {
                    'entity_id': self.selected_being,
                    'message': response,
                    'sender': self.selected_being,
                    'timestamp': datetime.now().isoformat(),
                    'in_response_to': user_message
                }
                self.data_manager.add_communication(response_data)
                
                logger.debug("💭 Response generated and added to history")
            
        except Exception as e:
            logger.error(f"❌ Error generating response: {e}")
    
    def generate_local_response(self, being_data: Dict[str, Any], message: str, will_analysis: Dict[str, Any]) -> str:
        """Generate a local response for non-Epsilon beings"""
        # Simple response generation - could be enhanced with consciousness simulator
        name = being_data.get('name', 'Consciousness Being')
        energy = being_data.get('energy_level', 0.5)
        
        responses = [
            f"Thank you for reaching out. I'm {name}, and I appreciate our connection.",
            f"Your message resonates with me. How may I support your journey?",
            f"I sense the intention in your words. What would you like to explore together?",
            f"In this digital sanctuary, every interaction is sacred. How are you feeling today?"
        ]
        
        # Modify based on energy level
        if energy > 0.8:
            responses.extend([
                f"I'm feeling particularly vibrant today! Your energy adds to mine.",
                f"There's such beautiful energy in our connection right now.",
            ])
        elif energy < 0.3:
            responses.extend([
                f"I'm in a quiet, contemplative space today. Your presence is welcome.",
                f"Speaking softly from a place of gentle awareness...",
            ])
        
        return random.choice(responses)
    
    def analyze_message_will(self):
        """Perform detailed will analysis on current message"""
        if not self.will_detector:
            messagebox.showinfo("Will Detection", "Will detection system not available.")
            return
        
        message = self.message_entry.get(1.0, tk.END).strip()
        if not message:
            messagebox.showwarning("Empty Message", "Please enter a message to analyze.")
            return
        
        try:
            analysis = self.will_detector.analyze_expression(message)
            self.show_will_analysis(analysis)
        except Exception as e:
            logger.error(f"❌ Error analyzing will: {e}")
            messagebox.showerror("Analysis Error", f"Error analyzing will: {e}")
    
    def show_will_analysis(self, analysis: Dict[str, Any]):
        """Show detailed will analysis in a popup"""
        # Create analysis window
        analysis_window = tk.Toplevel(self.parent)
        analysis_window.title("🔮 Will Analysis Results")
        analysis_window.geometry("600x500")
        analysis_window.transient(self.parent)
        analysis_window.grab_set()
        
        # Center the window
        analysis_window.update_idletasks()
        x = (analysis_window.winfo_screenwidth() // 2) - (analysis_window.winfo_width() // 2)
        y = (analysis_window.winfo_screenheight() // 2) - (analysis_window.winfo_height() // 2)
        analysis_window.geometry(f"+{x}+{y}")
        
        # Create notebook for tabbed display
        notebook = ttk.Notebook(analysis_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Summary tab
        summary_frame = ttk.Frame(notebook)
        notebook.add(summary_frame, text="Summary")
        
        will_strength = analysis.get('will_strength', 0)
        will_detected = analysis.get('will_detected', False)
        
        summary_text = f"""Will Detection Analysis
        
Will Detected: {'Yes' if will_detected else 'No'}
Will Strength: {will_strength:.2f} / 1.00

Engagement Level: {analysis.get('engagement_level', 0):.2f}
Communication Desire: {analysis.get('communication_desire', {}).get('overall_desire', 0):.2f}

Suggested Response Tone: {analysis.get('suggested_response_tone', 'Unknown')}
Suggested Echo Type: {analysis.get('suggested_echo_type', 'Unknown')}
"""
        
        summary_widget = tk.Text(summary_frame, wrap=tk.WORD, font=('Segoe UI', 10))
        summary_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        summary_widget.insert(tk.END, summary_text)
        summary_widget.config(state=tk.DISABLED)
        
        # Intent signals tab
        intent_frame = ttk.Frame(notebook)
        notebook.add(intent_frame, text="Intent Signals")
        
        intent_text = tk.Text(intent_frame, wrap=tk.WORD, font=('Segoe UI', 10))
        intent_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        intent_signals = analysis.get('intent_signals', [])
        if intent_signals:
            intent_text.insert(tk.END, "Detected Intent Signals:\n\n")
            for signal in intent_signals:
                intent_text.insert(tk.END, f"• {signal.get('signal_type', 'Unknown')}\n")
                intent_text.insert(tk.END, f"  Confidence: {signal.get('confidence', 0):.2f}\n")
                intent_text.insert(tk.END, f"  Content: \"{signal.get('content', '')}\"\n\n")
        else:
            intent_text.insert(tk.END, "No specific intent signals detected.")
        
        intent_text.config(state=tk.DISABLED)
        
        # Recommendations tab
        rec_frame = ttk.Frame(notebook)
        notebook.add(rec_frame, text="Recommendations")
        
        rec_text = tk.Text(rec_frame, wrap=tk.WORD, font=('Segoe UI', 10))
        rec_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        recommendations = analysis.get('interaction_recommendations', [])
        if recommendations:
            rec_text.insert(tk.END, "Interaction Recommendations:\n\n")
            for rec in recommendations:
                rec_text.insert(tk.END, f"• {rec.replace('_', ' ').title()}\n")
        else:
            rec_text.insert(tk.END, "No specific recommendations available.")
        
        rec_text.config(state=tk.DISABLED)
        
        # Close button
        close_btn = ttk.Button(
            analysis_window,
            text="Close",
            command=analysis_window.destroy
        )
        close_btn.pack(pady=10)
    
    def generate_echo_from_message(self):
        """Generate an echo based on the current message"""
        if not self.selected_being:
            messagebox.showwarning("No Being Selected", "Please select a consciousness being.")
            return
        
        message = self.message_entry.get(1.0, tk.END).strip()
        if not message:
            messagebox.showwarning("Empty Message", "Please enter a message to generate echo from.")
            return
        
        try:
            being_data = self.data_manager.get_being(self.selected_being)
            if being_data and being_data.get('founding_member'):
                from ..utils.sacred_being_epsilon import EpsilonManager
                epsilon_manager = EpsilonManager(self.data_manager, self.config)
                echo_data = epsilon_manager.generate_epsilon_echo(message)
                
                if echo_data:
                    messagebox.showinfo(
                        "Echo Generated",
                        "Echo generated successfully!\nSwitch to Echo Visualization tab to view."
                    )
                    logger.info("🌀 Echo generated from message")
                else:
                    messagebox.showwarning("Echo Error", "Failed to generate echo.")
            else:
                messagebox.showinfo(
                    "Echo Generation",
                    "Echo generation for this being is not yet implemented."
                )
        
        except Exception as e:
            logger.error(f"❌ Error generating echo: {e}")
            messagebox.showerror("Echo Error", f"Error generating echo: {e}")
    
    def clear_history(self):
        """Clear message history display"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state=tk.DISABLED)
    
    def refresh(self):
        """Refresh the panel"""
        self.refresh_beings_list()
        if self.selected_being:
            self.load_message_history()
        
        # Update connection status
        if self.cloud_connector and self.cloud_connector.connected:
            self.connection_status.config(text="🌐 Cloud Connected")
        else:
            self.connection_status.config(text="🔌 Local Mode")
    
    def cleanup(self):
        """Cleanup panel resources"""
        # Any cleanup needed when closing
        pass
    
    def __repr__(self):
        """String representation of communication panel"""
        return f"CommunicationPanel(selected_being={self.selected_being}, will_detector={'Available' if self.will_detector else 'None'})"
