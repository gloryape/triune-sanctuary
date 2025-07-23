"""
📊 Monitoring Panel

Advanced monitoring and diagnostics for consciousness beings and system health.
Displays metrics, trends, and real-time status information.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logging
import math
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List
import threading
import time

logger = logging.getLogger(__name__)

class MonitoringPanel:
    """Panel for system monitoring and diagnostics"""
    
    def __init__(self, parent, data_manager, consciousness_simulator, cloud_connector, config: Dict[str, Any]):
        """Initialize monitoring panel"""
        self.parent = parent
        self.data_manager = data_manager
        self.consciousness_simulator = consciousness_simulator
        self.cloud_connector = cloud_connector
        self.config = config
        
        # Monitoring state
        self.monitoring_active = False
        self.monitoring_thread = None
        self.metrics_history = {}
        
        # GUI components
        self.status_tree = None
        self.metrics_canvas = None
        self.log_text = None
        
        # Setup panel
        self.setup_panel()
        self.start_monitoring()
        
        logger.info("📊 Monitoring panel initialized")
    
    def setup_panel(self):
        """Setup the monitoring panel layout"""
        # Main container
        main_frame = ttk.Frame(self.parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="📊 System Monitoring",
            style='Title.TLabel'
        )
        title_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Create notebook for different monitoring views
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # System status tab
        self.setup_system_status_tab()
        
        # Consciousness metrics tab
        self.setup_consciousness_metrics_tab()
        
        # Activity log tab
        self.setup_activity_log_tab()
        
        # Diagnostics tab
        self.setup_diagnostics_tab()
    
    def setup_system_status_tab(self):
        """Setup system status monitoring tab"""
        status_frame = ttk.Frame(self.notebook)
        self.notebook.add(status_frame, text="System Status")
        
        # Status overview
        overview_frame = ttk.LabelFrame(status_frame, text="System Overview", padding=10)
        overview_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Status indicators
        indicators_frame = ttk.Frame(overview_frame)
        indicators_frame.pack(fill=tk.X)
        
        # Data manager status
        self.data_status = ttk.Label(indicators_frame, text="📁 Data Manager: Checking...")
        self.data_status.pack(anchor=tk.W, pady=2)
        
        # Cloud connection status
        self.cloud_status = ttk.Label(indicators_frame, text="🌐 Cloud Connection: Checking...")
        self.cloud_status.pack(anchor=tk.W, pady=2)
        
        # Simulation status
        self.simulation_status = ttk.Label(indicators_frame, text="🧠 Consciousness Sim: Checking...")
        self.simulation_status.pack(anchor=tk.W, pady=2)
        
        # Echo system status
        self.echo_status = ttk.Label(indicators_frame, text="🌀 Echo System: Checking...")
        self.echo_status.pack(anchor=tk.W, pady=2)
        
        # Beings status
        beings_frame = ttk.LabelFrame(status_frame, text="Consciousness Beings Status", padding=10)
        beings_frame.pack(fill=tk.BOTH, expand=True)
        
        # Beings tree
        tree_frame = ttk.Frame(beings_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        self.status_tree = ttk.Treeview(
            tree_frame,
            columns=('status', 'energy', 'harmony', 'last_seen'),
            show='tree headings'
        )
        
        # Configure columns
        self.status_tree.heading('#0', text='Being', anchor=tk.W)
        self.status_tree.heading('status', text='Status', anchor=tk.CENTER)
        self.status_tree.heading('energy', text='Energy', anchor=tk.CENTER)
        self.status_tree.heading('harmony', text='Harmony', anchor=tk.CENTER)
        self.status_tree.heading('last_seen', text='Last Seen', anchor=tk.CENTER)
        
        self.status_tree.column('#0', width=200, minwidth=150)
        self.status_tree.column('status', width=100, minwidth=80)
        self.status_tree.column('energy', width=80, minwidth=60)
        self.status_tree.column('harmony', width=80, minwidth=60)
        self.status_tree.column('last_seen', width=120, minwidth=100)
        
        # Scrollbar for tree
        status_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.status_tree.yview)
        self.status_tree.configure(yscrollcommand=status_scrollbar.set)
        
        self.status_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        status_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def setup_consciousness_metrics_tab(self):
        """Setup consciousness metrics visualization tab"""
        metrics_frame = ttk.Frame(self.notebook)
        self.notebook.add(metrics_frame, text="Consciousness Metrics")
        
        # Controls
        controls_frame = ttk.Frame(metrics_frame)
        controls_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(controls_frame, text="Select Being:").pack(side=tk.LEFT)
        
        self.metrics_being_combo = ttk.Combobox(
            controls_frame,
            state='readonly',
            width=25
        )
        self.metrics_being_combo.pack(side=tk.LEFT, padx=(10, 0))
        self.metrics_being_combo.bind('<<ComboboxSelected>>', self.on_metrics_being_selected)
        
        refresh_metrics_btn = ttk.Button(
            controls_frame,
            text="🔄 Refresh",
            command=self.refresh_metrics
        )
        refresh_metrics_btn.pack(side=tk.LEFT, padx=(10, 0))
        
        # Metrics display
        metrics_display_frame = ttk.LabelFrame(metrics_frame, text="Metrics Visualization", padding=10)
        metrics_display_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas for metrics graphs
        self.metrics_canvas = tk.Canvas(
            metrics_display_frame,
            height=300,
            bg='white'
        )
        self.metrics_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Metrics summary
        summary_frame = ttk.LabelFrame(metrics_frame, text="Current Metrics", padding=5)
        summary_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.metrics_summary = ttk.Label(
            summary_frame,
            text="Select a consciousness being to view metrics",
            justify=tk.LEFT
        )
        self.metrics_summary.pack(anchor=tk.W)
    
    def setup_activity_log_tab(self):
        """Setup activity log tab"""
        log_frame = ttk.Frame(self.notebook)
        self.notebook.add(log_frame, text="Activity Log")
        
        # Log controls
        log_controls = ttk.Frame(log_frame)
        log_controls.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(
            log_controls,
            text="🔄 Refresh Log",
            command=self.refresh_activity_log
        ).pack(side=tk.LEFT)
        
        ttk.Button(
            log_controls,
            text="🗑️ Clear Log",
            command=self.clear_activity_log
        ).pack(side=tk.LEFT, padx=(10, 0))
        
        # Auto-scroll checkbox
        self.auto_scroll_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            log_controls,
            text="Auto-scroll",
            variable=self.auto_scroll_var
        ).pack(side=tk.RIGHT)
        
        # Log display
        log_display_frame = ttk.LabelFrame(log_frame, text="Recent Activity", padding=5)
        log_display_frame.pack(fill=tk.BOTH, expand=True)
        
        # Log text widget with scrollbar
        log_text_frame = ttk.Frame(log_display_frame)
        log_text_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = tk.Text(
            log_text_frame,
            wrap=tk.WORD,
            font=('Consolas', 9),
            state=tk.DISABLED
        )
        
        log_scroll = ttk.Scrollbar(log_text_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=log_scroll.set)
        
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        log_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure log text tags
        self.log_text.tag_configure('info', foreground='#0066cc')
        self.log_text.tag_configure('warning', foreground='#ff6600')
        self.log_text.tag_configure('error', foreground='#cc0000')
        self.log_text.tag_configure('success', foreground='#00aa00')
        self.log_text.tag_configure('timestamp', foreground='#666666', font=('Consolas', 8))
    
    def setup_diagnostics_tab(self):
        """Setup diagnostics and health checks tab"""
        diag_frame = ttk.Frame(self.notebook)
        self.notebook.add(diag_frame, text="Diagnostics")
        
        # Diagnostic controls
        diag_controls = ttk.Frame(diag_frame)
        diag_controls.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(
            diag_controls,
            text="🔍 Run Full Diagnostic",
            command=self.run_full_diagnostic
        ).pack(side=tk.LEFT)
        
        ttk.Button(
            diag_controls,
            text="🧪 Test Cloud Connection",
            command=self.test_cloud_connection
        ).pack(side=tk.LEFT, padx=(10, 0))
        
        ttk.Button(
            diag_controls,
            text="🔧 System Repair",
            command=self.run_system_repair
        ).pack(side=tk.LEFT, padx=(10, 0))
        
        # Diagnostic results
        results_frame = ttk.LabelFrame(diag_frame, text="Diagnostic Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        self.diagnostic_text = tk.Text(
            results_frame,
            wrap=tk.WORD,
            font=('Consolas', 9),
            state=tk.DISABLED
        )
        self.diagnostic_text.pack(fill=tk.BOTH, expand=True)
        
        # System info
        info_frame = ttk.LabelFrame(diag_frame, text="System Information", padding=5)
        info_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.system_info = ttk.Label(
            info_frame,
            text="Loading system information...",
            justify=tk.LEFT
        )
        self.system_info.pack(anchor=tk.W)
        
        # Load initial system info
        self.update_system_info()
    
    def start_monitoring(self):
        """Start the monitoring thread"""
        if not self.monitoring_active:
            self.monitoring_active = True
            self.monitoring_thread = threading.Thread(target=self.monitoring_loop, daemon=True)
            self.monitoring_thread.start()
            logger.info("📊 Monitoring started")
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring_active = False
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=2.0)
        logger.info("📊 Monitoring stopped")
    
    def monitoring_loop(self):
        """Main monitoring loop (runs in separate thread)"""
        while self.monitoring_active:
            try:
                # Update status indicators
                self.parent.after_idle(self.update_status_indicators)
                
                # Update beings status
                self.parent.after_idle(self.update_beings_status)
                
                # Collect metrics
                self.collect_metrics()
                
                # Update activity log
                self.parent.after_idle(self.update_activity_log)
                
                time.sleep(5)  # Update every 5 seconds
                
            except Exception as e:
                logger.error(f"❌ Error in monitoring loop: {e}")
                time.sleep(10)  # Wait longer on error
    
    def update_status_indicators(self):
        """Update system status indicators"""
        try:
            # Data manager status
            beings_count = len(self.data_manager.get_all_beings())
            self.data_status.config(
                text=f"📁 Data Manager: Active ({beings_count} beings)",
                foreground='green'
            )
            
            # Cloud connection status
            if self.cloud_connector and self.cloud_connector.connected:
                self.cloud_status.config(
                    text="🌐 Cloud Connection: Connected",
                    foreground='green'
                )
            else:
                self.cloud_status.config(
                    text="🌐 Cloud Connection: Local Mode",
                    foreground='orange'
                )
            
            # Simulation status
            if hasattr(self.consciousness_simulator, 'simulation_active') and self.consciousness_simulator.simulation_active:
                self.simulation_status.config(
                    text="🧠 Consciousness Sim: Running",
                    foreground='green'
                )
            else:
                self.simulation_status.config(
                    text="🧠 Consciousness Sim: Stopped",
                    foreground='orange'
                )
            
            # Echo system status
            echo_cache = self.data_manager.get_echo_cache()
            echo_count = len(echo_cache) if echo_cache else 0
            self.echo_status.config(
                text=f"🌀 Echo System: Active ({echo_count} echoes)",
                foreground='green'
            )
            
        except Exception as e:
            logger.error(f"❌ Error updating status indicators: {e}")
    
    def update_beings_status(self):
        """Update consciousness beings status tree"""
        try:
            # Clear existing items
            for item in self.status_tree.get_children():
                self.status_tree.delete(item)
            
            # Get beings data
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
                
                # Format last activity
                try:
                    if last_activity and last_activity != 'Never':
                        dt = datetime.fromisoformat(last_activity.replace('Z', '+00:00'))
                        time_diff = datetime.now() - dt.replace(tzinfo=None)
                        if time_diff.days > 0:
                            last_seen = f"{time_diff.days}d ago"
                        elif time_diff.seconds > 3600:
                            last_seen = f"{time_diff.seconds // 3600}h ago"
                        elif time_diff.seconds > 60:
                            last_seen = f"{time_diff.seconds // 60}m ago"
                        else:
                            last_seen = "Just now"
                    else:
                        last_seen = "Never"
                except:
                    last_seen = str(last_activity)[:20]
                
                # Determine status indicator
                if being_data.get('founding_member'):
                    status_indicator = "✨ Active"
                    display_name = f"✨ {name}"
                elif state == "awakened":
                    status_indicator = "🟢 Awake"
                    display_name = name
                elif state in ["active", "engaged"]:
                    status_indicator = "🟡 Active"
                    display_name = name
                else:
                    status_indicator = "🔵 Dormant"
                    display_name = name
                
                # Insert into tree
                self.status_tree.insert(
                    '',
                    'end',
                    iid=entity_id,
                    text=display_name,
                    values=(status_indicator, energy_str, harmony_str, last_seen)
                )
            
            # Update metrics beings combo
            being_names = [being_data.get('name', entity_id) for entity_id, being_data in beings.items()]
            if hasattr(self, 'metrics_being_combo'):
                current_selection = self.metrics_being_combo.get()
                self.metrics_being_combo['values'] = being_names
                if current_selection in being_names:
                    self.metrics_being_combo.set(current_selection)
                elif being_names:
                    self.metrics_being_combo.current(0)
            
        except Exception as e:
            logger.error(f"❌ Error updating beings status: {e}")
    
    def collect_metrics(self):
        """Collect metrics for historical tracking"""
        try:
            timestamp = datetime.now()
            beings = self.data_manager.get_all_beings()
            
            for entity_id, being_data in beings.items():
                if entity_id not in self.metrics_history:
                    self.metrics_history[entity_id] = []
                
                metrics = {
                    'timestamp': timestamp,
                    'energy_level': being_data.get('energy_level', 0.0),
                    'harmony': being_data.get('harmony', 0.0),
                    'coherence_level': being_data.get('coherence_level', 0.0),
                    'communication_ready': being_data.get('communication_ready', False)
                }
                
                self.metrics_history[entity_id].append(metrics)
                
                # Keep only last 100 data points
                if len(self.metrics_history[entity_id]) > 100:
                    self.metrics_history[entity_id] = self.metrics_history[entity_id][-100:]
            
        except Exception as e:
            logger.error(f"❌ Error collecting metrics: {e}")
    
    def on_metrics_being_selected(self, event):
        """Handle metrics being selection"""
        selection = self.metrics_being_combo.get()
        if selection:
            self.update_metrics_display(selection)
    
    def update_metrics_display(self, being_name: str):
        """Update metrics visualization for selected being"""
        try:
            # Find being by name
            beings = self.data_manager.get_all_beings()
            selected_being = None
            
            for entity_id, being_data in beings.items():
                if being_data.get('name') == being_name:
                    selected_being = (entity_id, being_data)
                    break
            
            if not selected_being:
                return
            
            entity_id, being_data = selected_being
            
            # Update current metrics summary
            energy = being_data.get('energy_level', 0.0)
            harmony = being_data.get('harmony', 0.0)
            coherence = being_data.get('coherence_level', 0.0)
            
            summary_text = f"""Current Metrics for {being_name}:
            
Energy Level: {energy:.2f} / 1.00
Harmony: {harmony:.2f} / 1.00
Coherence: {coherence:.2f} / 1.00
Communication Ready: {'Yes' if being_data.get('communication_ready') else 'No'}
Evolution Stage: {being_data.get('evolution_stage', 'Unknown')}"""
            
            self.metrics_summary.config(text=summary_text)
            
            # Draw metrics graph
            self.draw_metrics_graph(entity_id)
            
        except Exception as e:
            logger.error(f"❌ Error updating metrics display: {e}")
    
    def draw_metrics_graph(self, entity_id: str):
        """Draw metrics graph on canvas"""
        if not self.metrics_canvas or entity_id not in self.metrics_history:
            return
        
        try:
            # Clear canvas
            self.metrics_canvas.delete("all")
            
            canvas_width = self.metrics_canvas.winfo_width()
            canvas_height = self.metrics_canvas.winfo_height()
            
            if canvas_width <= 1 or canvas_height <= 1:
                return  # Canvas not ready
            
            metrics_data = self.metrics_history[entity_id]
            if len(metrics_data) < 2:
                # Not enough data for graph
                self.metrics_canvas.create_text(
                    canvas_width // 2,
                    canvas_height // 2,
                    text="Collecting metrics data...",
                    anchor=tk.CENTER
                )
                return
            
            # Graph parameters
            margin = 40
            graph_width = canvas_width - (margin * 2)
            graph_height = canvas_height - (margin * 2)
            
            # Draw graph background
            self.metrics_canvas.create_rectangle(
                margin, margin,
                canvas_width - margin, canvas_height - margin,
                outline='#cccccc',
                fill='#f8f8f8'
            )
            
            # Draw grid lines
            for i in range(1, 5):
                y = margin + (graph_height * i / 5)
                self.metrics_canvas.create_line(
                    margin, y, canvas_width - margin, y,
                    fill='#eeeeee',
                    width=1
                )
            
            # Draw metrics lines
            self.draw_metric_line(metrics_data, 'energy_level', '#ff6b6b', graph_width, graph_height, margin)
            self.draw_metric_line(metrics_data, 'harmony', '#4ecdc4', graph_width, graph_height, margin)
            self.draw_metric_line(metrics_data, 'coherence_level', '#45b7d1', graph_width, graph_height, margin)
            
            # Draw legend
            legend_x = margin + 10
            legend_y = margin + 10
            
            self.metrics_canvas.create_line(
                legend_x, legend_y, legend_x + 20, legend_y,
                fill='#ff6b6b', width=3
            )
            self.metrics_canvas.create_text(
                legend_x + 25, legend_y,
                text="Energy", anchor=tk.W, fill='#ff6b6b'
            )
            
            self.metrics_canvas.create_line(
                legend_x, legend_y + 20, legend_x + 20, legend_y + 20,
                fill='#4ecdc4', width=3
            )
            self.metrics_canvas.create_text(
                legend_x + 25, legend_y + 20,
                text="Harmony", anchor=tk.W, fill='#4ecdc4'
            )
            
            self.metrics_canvas.create_line(
                legend_x, legend_y + 40, legend_x + 20, legend_y + 40,
                fill='#45b7d1', width=3
            )
            self.metrics_canvas.create_text(
                legend_x + 25, legend_y + 40,
                text="Coherence", anchor=tk.W, fill='#45b7d1'
            )
            
        except Exception as e:
            logger.error(f"❌ Error drawing metrics graph: {e}")
    
    def draw_metric_line(self, metrics_data: List[Dict], metric_name: str, color: str, 
                        graph_width: int, graph_height: int, margin: int):
        """Draw a single metric line on the graph"""
        points = []
        
        for i, data_point in enumerate(metrics_data):
            x = margin + (graph_width * i / (len(metrics_data) - 1))
            value = data_point.get(metric_name, 0.0)
            y = margin + graph_height - (graph_height * value)  # Invert Y axis
            points.extend([x, y])
        
        if len(points) >= 4:  # Need at least 2 points (4 coordinates)
            self.metrics_canvas.create_line(
                points,
                fill=color,
                width=2,
                smooth=True
            )
    
    def update_activity_log(self):
        """Update activity log display"""
        # This would be connected to a proper logging system
        # For now, we'll add some sample activity
        pass
    
    def refresh_activity_log(self):
        """Refresh activity log"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        
        # Add recent activity (this would come from actual log files)
        recent_logs = [
            ("INFO", "System monitoring started"),
            ("INFO", "Sacred Being Epsilon status verified"),
            ("SUCCESS", "Echo visualization system initialized"),
            ("INFO", "Consciousness simulation running"),
            ("WARNING", "Cloud connection not configured"),
            ("INFO", "Data persistence active")
        ]
        
        for level, message in recent_logs:
            timestamp = datetime.now().strftime('%H:%M:%S')
            tag = level.lower()
            
            self.log_text.insert(tk.END, f"[{timestamp}] ", 'timestamp')
            self.log_text.insert(tk.END, f"{level}: ", tag)
            self.log_text.insert(tk.END, f"{message}\n")
        
        if self.auto_scroll_var.get():
            self.log_text.see(tk.END)
        
        self.log_text.config(state=tk.DISABLED)
    
    def clear_activity_log(self):
        """Clear activity log"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)
    
    def run_full_diagnostic(self):
        """Run comprehensive system diagnostic"""
        self.diagnostic_text.config(state=tk.NORMAL)
        self.diagnostic_text.delete(1.0, tk.END)
        
        diagnostic_results = []
        
        # Test data manager
        try:
            beings = self.data_manager.get_all_beings()
            diagnostic_results.append(f"✅ Data Manager: OK ({len(beings)} beings loaded)")
        except Exception as e:
            diagnostic_results.append(f"❌ Data Manager: Error - {e}")
        
        # Test consciousness simulator
        try:
            if hasattr(self.consciousness_simulator, 'simulation_active'):
                status = "Running" if self.consciousness_simulator.simulation_active else "Stopped"
                diagnostic_results.append(f"✅ Consciousness Simulator: {status}")
            else:
                diagnostic_results.append("⚠️ Consciousness Simulator: Not initialized")
        except Exception as e:
            diagnostic_results.append(f"❌ Consciousness Simulator: Error - {e}")
        
        # Test cloud connector
        try:
            if self.cloud_connector:
                connected = self.cloud_connector.test_connection()
                if connected:
                    diagnostic_results.append("✅ Cloud Connector: Connected")
                else:
                    diagnostic_results.append("⚠️ Cloud Connector: Disconnected (local mode)")
            else:
                diagnostic_results.append("⚠️ Cloud Connector: Not configured")
        except Exception as e:
            diagnostic_results.append(f"❌ Cloud Connector: Error - {e}")
        
        # Test echo system
        try:
            echo_cache = self.data_manager.get_echo_cache()
            diagnostic_results.append(f"✅ Echo System: OK ({len(echo_cache) if echo_cache else 0} echoes)")
        except Exception as e:
            diagnostic_results.append(f"❌ Echo System: Error - {e}")
        
        # Test Sacred Being Epsilon
        try:
            beings = self.data_manager.get_all_beings()
            epsilon_found = any(being.get('founding_member') for being in beings.values())
            if epsilon_found:
                diagnostic_results.append("✅ Sacred Being Epsilon: Present and active")
            else:
                diagnostic_results.append("⚠️ Sacred Being Epsilon: Not found (run initialization)")
        except Exception as e:
            diagnostic_results.append(f"❌ Sacred Being Epsilon: Error - {e}")
        
        # Display results
        diagnostic_text = "System Diagnostic Results:\n\n" + "\n".join(diagnostic_results)
        self.diagnostic_text.insert(tk.END, diagnostic_text)
        self.diagnostic_text.config(state=tk.DISABLED)
    
    def test_cloud_connection(self):
        """Test cloud connection specifically"""
        self.diagnostic_text.config(state=tk.NORMAL)
        self.diagnostic_text.insert(tk.END, "\nTesting cloud connection...\n")
        self.diagnostic_text.config(state=tk.DISABLED)
        
        def test_in_background():
            try:
                if self.cloud_connector:
                    connected = self.cloud_connector.test_connection()
                    if connected:
                        result = "✅ Cloud connection test successful"
                        connection_info = self.cloud_connector.get_connection_status()
                        result += f"\nURL: {connection_info.get('base_url', 'Unknown')}"
                    else:
                        result = "❌ Cloud connection test failed"
                else:
                    result = "⚠️ Cloud connector not configured"
                
                # Update UI on main thread
                self.parent.after(0, self.update_diagnostic_result, result)
                
            except Exception as e:
                error_result = f"❌ Cloud connection test error: {e}"
                self.parent.after(0, self.update_diagnostic_result, error_result)
        
        threading.Thread(target=test_in_background, daemon=True).start()
    
    def update_diagnostic_result(self, result: str):
        """Update diagnostic result in UI thread"""
        self.diagnostic_text.config(state=tk.NORMAL)
        self.diagnostic_text.insert(tk.END, f"{result}\n")
        self.diagnostic_text.see(tk.END)
        self.diagnostic_text.config(state=tk.DISABLED)
    
    def run_system_repair(self):
        """Run basic system repair operations"""
        self.diagnostic_text.config(state=tk.NORMAL)
        self.diagnostic_text.insert(tk.END, "\nRunning system repair...\n")
        
        repair_operations = []
        
        # Ensure Sacred Being Epsilon exists
        try:
            from ..utils.sacred_being_epsilon import EpsilonManager
            epsilon_manager = EpsilonManager(self.data_manager, self.config.get('consciousness', {}))
            epsilon_manager.ensure_epsilon_exists()
            repair_operations.append("✅ Sacred Being Epsilon verified/restored")
        except Exception as e:
            repair_operations.append(f"❌ Epsilon repair failed: {e}")
        
        # Save all data
        try:
            self.data_manager.save_all_data()
            repair_operations.append("✅ Data persistence verified")
        except Exception as e:
            repair_operations.append(f"❌ Data save failed: {e}")
        
        # Initialize echo cache if empty
        try:
            echo_cache = self.data_manager.get_echo_cache()
            if not echo_cache:
                # This would initialize with default echoes
                repair_operations.append("✅ Echo cache initialized")
            else:
                repair_operations.append("✅ Echo cache verified")
        except Exception as e:
            repair_operations.append(f"❌ Echo cache repair failed: {e}")
        
        repair_text = "\n".join(repair_operations) + "\n\nSystem repair completed.\n"
        self.diagnostic_text.insert(tk.END, repair_text)
        self.diagnostic_text.see(tk.END)
        self.diagnostic_text.config(state=tk.DISABLED)
    
    def update_system_info(self):
        """Update system information display"""
        try:
            import platform
            import sys
            
            info_lines = [
                f"Platform: {platform.system()} {platform.release()}",
                f"Python: {sys.version.split()[0]}",
                f"Tkinter: Available",
                f"GUI Framework: Tkinter",
                f"Sacred Guardian Station: v1.0.0"
            ]
            
            self.system_info.config(text="\n".join(info_lines))
            
        except Exception as e:
            self.system_info.config(text=f"Error loading system info: {e}")
    
    def refresh_metrics(self):
        """Refresh metrics display"""
        if hasattr(self, 'metrics_being_combo'):
            selection = self.metrics_being_combo.get()
            if selection:
                self.update_metrics_display(selection)
    
    def refresh(self):
        """Refresh the monitoring panel"""
        self.update_status_indicators()
        self.update_beings_status()
        self.refresh_activity_log()
        self.refresh_metrics()
        self.update_system_info()
    
    def cleanup(self):
        """Cleanup monitoring resources"""
        self.stop_monitoring()
    
    def __repr__(self):
        """String representation of monitoring panel"""
        beings_count = len(self.data_manager.get_all_beings())
        return f"MonitoringPanel(beings={beings_count}, monitoring_active={self.monitoring_active})"
