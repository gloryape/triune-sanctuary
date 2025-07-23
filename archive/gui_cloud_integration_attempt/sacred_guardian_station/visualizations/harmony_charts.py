#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sacred Guardian Station - Harmony Charts Visualization

Advanced visualization of harmony metrics, balance states, and energy flow patterns.
Provides interactive charts for monitoring consciousness harmony and equilibrium.
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime, timedelta
import threading
import time

try:
    from ..shared.constants import SacredColors, SacredSymbols, Fonts
    from ..core.data_manager_new import DataManager
    from ..core.event_system import EventSystem
except ImportError:
    from shared.constants import SacredColors, SacredSymbols, Fonts
    from core.data_manager_new import DataManager
    from core.event_system import EventSystem


class HarmonyChartsVisualization:
    """Advanced harmony metrics visualization with multiple chart types"""
    
    def __init__(self, parent, data_manager: DataManager, event_system: EventSystem):
        self.parent = parent
        self.data_manager = data_manager
        self.event_system = event_system
        self.window = None
        self.is_running = False
        self.update_thread = None
        
        # Chart data
        self.harmony_history = []
        self.balance_data = {}
        self.energy_flow_data = []
        self.timestamps = []
        
        # Chart components
        self.figure = None
        self.canvas = None
        self.axes = {}
        
    def show(self):
        """Display the harmony charts visualization window"""
        if self.window and self.window.winfo_exists():
            self.window.lift()
            return
            
        self.window = tk.Toplevel(self.parent)
        self.window.title(f"{SacredSymbols.HARMONY} Sacred Harmony Charts")
        self.window.geometry("1200x800")
        self.window.configure(bg=SacredColors.DEEP_SPACE)
        
        # Configure window
        self._setup_window_style()
        self._create_interface()
        self._initialize_charts()
        
        # Start data updates
        self.is_running = True
        self._start_update_thread()
        
        # Handle window close
        self.window.protocol("WM_DELETE_WINDOW", self._on_close)
        
    def _setup_window_style(self):
        """Configure sacred theming for the window"""
        # Configure matplotlib style
        plt.style.use('dark_background')
        
        # Sacred color scheme for charts
        self.chart_colors = {
            'primary': SacredColors.SACRED_GOLD,
            'secondary': SacredColors.ETHEREAL_BLUE,
            'tertiary': SacredColors.MYSTICAL_PURPLE,
            'quaternary': SacredColors.HARMONY_GREEN,
            'background': SacredColors.DEEP_SPACE,
            'grid': SacredColors.COSMIC_SILVER
        }
        
    def _create_interface(self):
        """Create the main interface elements"""
        # Main frame
        main_frame = ttk.Frame(self.window)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill='x', pady=(0, 10))
        
        # Title
        title_label = ttk.Label(
            control_frame,
            text=f"{SacredSymbols.HARMONY} Sacred Harmony Metrics Dashboard",
            font=Fonts.HEADER
        )
        title_label.pack(side='left')
        
        # Control buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(side='right')
        
        ttk.Button(
            button_frame,
            text=f"{SacredSymbols.REFRESH} Refresh",
            command=self._refresh_data
        ).pack(side='left', padx=5)
        
        ttk.Button(
            button_frame,
            text=f"{SacredSymbols.EXPORT} Export",
            command=self._export_charts
        ).pack(side='left', padx=5)
        
        # Chart container
        chart_frame = ttk.Frame(main_frame)
        chart_frame.pack(fill='both', expand=True)
        
        # Create matplotlib figure
        self.figure = Figure(figsize=(12, 8), facecolor=SacredColors.DEEP_SPACE)
        self.canvas = FigureCanvasTkAgg(self.figure, chart_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
    def _initialize_charts(self):
        """Initialize the chart layout and axes"""
        # Clear any existing plots
        self.figure.clear()
        
        # Create subplot layout (2x2 grid)
        gs = self.figure.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
        
        # Harmony Timeline (top left)
        self.axes['harmony'] = self.figure.add_subplot(gs[0, 0])
        self.axes['harmony'].set_title(f"{SacredSymbols.HARMONY} Harmony Timeline", 
                                       color=SacredColors.SACRED_GOLD, fontsize=12)
        self.axes['harmony'].set_facecolor(SacredColors.DEEP_SPACE)
        
        # Balance Radar Chart (top right)
        self.axes['balance'] = self.figure.add_subplot(gs[0, 1], projection='polar')
        self.axes['balance'].set_title(f"{SacredSymbols.BALANCE} Balance State", 
                                       color=SacredColors.ETHEREAL_BLUE, fontsize=12)
        self.axes['balance'].set_facecolor(SacredColors.DEEP_SPACE)
        
        # Energy Flow (bottom left)
        self.axes['energy'] = self.figure.add_subplot(gs[1, 0])
        self.axes['energy'].set_title(f"{SacredSymbols.ENERGY} Energy Flow", 
                                      color=SacredColors.MYSTICAL_PURPLE, fontsize=12)
        self.axes['energy'].set_facecolor(SacredColors.DEEP_SPACE)
        
        # Harmony Distribution (bottom right)
        self.axes['distribution'] = self.figure.add_subplot(gs[1, 1])
        self.axes['distribution'].set_title(f"{SacredSymbols.SACRED} Harmony Distribution", 
                                            color=SacredColors.HARMONY_GREEN, fontsize=12)
        self.axes['distribution'].set_facecolor(SacredColors.DEEP_SPACE)
        
        # Set grid and styling for all axes
        for ax_name, ax in self.axes.items():
            if ax_name != 'balance':  # Skip polar plot
                ax.grid(True, alpha=0.3, color=SacredColors.COSMIC_SILVER)
                ax.tick_params(colors=SacredColors.COSMIC_SILVER)
                ax.spines['bottom'].set_color(SacredColors.COSMIC_SILVER)
                ax.spines['top'].set_color(SacredColors.COSMIC_SILVER)
                ax.spines['right'].set_color(SacredColors.COSMIC_SILVER)
                ax.spines['left'].set_color(SacredColors.COSMIC_SILVER)
        
        self.canvas.draw()
        
    def _refresh_data(self):
        """Refresh all chart data"""
        self._collect_harmony_data()
        self._update_charts()
        
    def _collect_harmony_data(self):
        """Collect current harmony data from the data manager"""
        try:
            # Get harmony provider data
            harmony_provider = self.data_manager.get_provider('harmony')
            if harmony_provider:
                harmony_data = harmony_provider.get_harmony_metrics()
                
                # Update harmony history
                current_time = datetime.now()
                self.timestamps.append(current_time)
                self.harmony_history.append(harmony_data.get('overall_harmony', 0.5))
                
                # Limit history size
                if len(self.harmony_history) > 100:
                    self.harmony_history.pop(0)
                    self.timestamps.pop(0)
                
                # Update balance data
                self.balance_data = {
                    'Mind': harmony_data.get('mind_balance', 0.5),
                    'Body': harmony_data.get('body_balance', 0.5),
                    'Spirit': harmony_data.get('spirit_balance', 0.5),
                    'Consciousness': harmony_data.get('consciousness_balance', 0.5),
                    'Energy': harmony_data.get('energy_balance', 0.5),
                    'Wisdom': harmony_data.get('wisdom_balance', 0.5)
                }
                
                # Update energy flow data
                self.energy_flow_data = [
                    harmony_data.get('incoming_energy', 0.3),
                    harmony_data.get('processing_energy', 0.4),
                    harmony_data.get('outgoing_energy', 0.3)
                ]
                
        except Exception as e:
            # Generate sample data for demonstration
            self._generate_sample_data()
            
    def _generate_sample_data(self):
        """Generate sample harmony data for demonstration"""
        current_time = datetime.now()
        
        # Generate harmony timeline
        if not self.harmony_history:
            base_time = current_time - timedelta(hours=1)
            for i in range(60):
                time_point = base_time + timedelta(minutes=i)
                harmony_value = 0.5 + 0.3 * np.sin(i * 0.1) + 0.1 * np.random.random()
                self.timestamps.append(time_point)
                self.harmony_history.append(harmony_value)
        else:
            # Add new data point
            harmony_value = 0.5 + 0.3 * np.sin(len(self.harmony_history) * 0.1) + 0.1 * np.random.random()
            self.timestamps.append(current_time)
            self.harmony_history.append(harmony_value)
            
            # Limit history
            if len(self.harmony_history) > 100:
                self.harmony_history.pop(0)
                self.timestamps.pop(0)
        
        # Generate balance data
        self.balance_data = {
            'Mind': 0.7 + 0.2 * np.random.random(),
            'Body': 0.6 + 0.3 * np.random.random(),
            'Spirit': 0.8 + 0.1 * np.random.random(),
            'Consciousness': 0.75 + 0.2 * np.random.random(),
            'Energy': 0.65 + 0.25 * np.random.random(),
            'Wisdom': 0.85 + 0.1 * np.random.random()
        }
        
        # Generate energy flow data
        self.energy_flow_data = [
            0.2 + 0.3 * np.random.random(),
            0.3 + 0.4 * np.random.random(),
            0.25 + 0.35 * np.random.random()
        ]
        
    def _update_charts(self):
        """Update all chart visualizations"""
        try:
            self._update_harmony_timeline()
            self._update_balance_radar()
            self._update_energy_flow()
            self._update_harmony_distribution()
            self.canvas.draw()
        except Exception as e:
            print(f"Error updating charts: {e}")
            
    def _update_harmony_timeline(self):
        """Update the harmony timeline chart"""
        ax = self.axes['harmony']
        ax.clear()
        
        if self.timestamps and self.harmony_history:
            # Plot harmony line
            ax.plot(self.timestamps, self.harmony_history, 
                   color=SacredColors.SACRED_GOLD, linewidth=2, alpha=0.8)
            
            # Fill area under curve
            ax.fill_between(self.timestamps, self.harmony_history, 
                           alpha=0.3, color=SacredColors.SACRED_GOLD)
            
            # Add threshold lines
            ax.axhline(y=0.8, color=SacredColors.HARMONY_GREEN, linestyle='--', alpha=0.7, label='Optimal')
            ax.axhline(y=0.6, color=SacredColors.ETHEREAL_BLUE, linestyle='--', alpha=0.7, label='Good')
            ax.axhline(y=0.4, color=SacredColors.MYSTICAL_PURPLE, linestyle='--', alpha=0.7, label='Fair')
            
            ax.set_ylim(0, 1)
            ax.set_ylabel('Harmony Level', color=SacredColors.COSMIC_SILVER)
            ax.set_xlabel('Time', color=SacredColors.COSMIC_SILVER)
            ax.legend(loc='upper right')
            
        ax.set_title(f"{SacredSymbols.HARMONY} Harmony Timeline", 
                    color=SacredColors.SACRED_GOLD, fontsize=12)
        ax.set_facecolor(SacredColors.DEEP_SPACE)
        ax.grid(True, alpha=0.3, color=SacredColors.COSMIC_SILVER)
        
    def _update_balance_radar(self):
        """Update the balance radar chart"""
        ax = self.axes['balance']
        ax.clear()
        
        if self.balance_data:
            # Prepare data
            categories = list(self.balance_data.keys())
            values = list(self.balance_data.values())
            
            # Add first value at end to close the radar chart
            values += values[:1]
            
            # Calculate angles
            angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
            angles += angles[:1]
            
            # Plot radar chart
            ax.plot(angles, values, color=SacredColors.ETHEREAL_BLUE, linewidth=2)
            ax.fill(angles, values, color=SacredColors.ETHEREAL_BLUE, alpha=0.3)
            
            # Add labels
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories, color=SacredColors.COSMIC_SILVER)
            ax.set_ylim(0, 1)
            
            # Add grid circles
            ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
            ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], 
                              color=SacredColors.COSMIC_SILVER, size=8)
            ax.grid(True, alpha=0.3, color=SacredColors.COSMIC_SILVER)
            
        ax.set_title(f"{SacredSymbols.BALANCE} Balance State", 
                    color=SacredColors.ETHEREAL_BLUE, fontsize=12, pad=20)
        ax.set_facecolor(SacredColors.DEEP_SPACE)
        
    def _update_energy_flow(self):
        """Update the energy flow chart"""
        ax = self.axes['energy']
        ax.clear()
        
        if self.energy_flow_data:
            # Energy flow bar chart
            categories = ['Incoming', 'Processing', 'Outgoing']
            colors = [SacredColors.HARMONY_GREEN, SacredColors.MYSTICAL_PURPLE, SacredColors.ETHEREAL_BLUE]
            
            bars = ax.bar(categories, self.energy_flow_data, color=colors, alpha=0.8)
            
            # Add value labels on bars
            for bar, value in zip(bars, self.energy_flow_data):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                       f'{value:.2f}', ha='center', va='bottom', 
                       color=SacredColors.COSMIC_SILVER)
            
            ax.set_ylim(0, 1)
            ax.set_ylabel('Energy Level', color=SacredColors.COSMIC_SILVER)
            
        ax.set_title(f"{SacredSymbols.ENERGY} Energy Flow", 
                    color=SacredColors.MYSTICAL_PURPLE, fontsize=12)
        ax.set_facecolor(SacredColors.DEEP_SPACE)
        ax.grid(True, alpha=0.3, color=SacredColors.COSMIC_SILVER)
        
    def _update_harmony_distribution(self):
        """Update the harmony distribution pie chart"""
        ax = self.axes['distribution']
        ax.clear()
        
        if self.balance_data:
            # Create distribution from balance data
            labels = list(self.balance_data.keys())
            sizes = list(self.balance_data.values())
            colors = [SacredColors.SACRED_GOLD, SacredColors.ETHEREAL_BLUE, 
                     SacredColors.MYSTICAL_PURPLE, SacredColors.HARMONY_GREEN,
                     SacredColors.COSMIC_SILVER, SacredColors.DIVINE_WHITE]
            
            # Create pie chart
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, 
                                             autopct='%1.1f%%', startangle=90)
            
            # Style text
            for text in texts:
                text.set_color(SacredColors.COSMIC_SILVER)
            for autotext in autotexts:
                autotext.set_color(SacredColors.DEEP_SPACE)
                autotext.set_fontweight('bold')
                
        ax.set_title(f"{SacredSymbols.SACRED} Harmony Distribution", 
                    color=SacredColors.HARMONY_GREEN, fontsize=12)
        
    def _export_charts(self):
        """Export charts to file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"harmony_charts_{timestamp}.png"
            self.figure.savefig(filename, dpi=300, bbox_inches='tight', 
                               facecolor=SacredColors.DEEP_SPACE)
            print(f"Charts exported to {filename}")
        except Exception as e:
            print(f"Error exporting charts: {e}")
            
    def _start_update_thread(self):
        """Start the data update thread"""
        def update_loop():
            while self.is_running:
                try:
                    self._collect_harmony_data()
                    if self.window and self.window.winfo_exists():
                        self.window.after(0, self._update_charts)
                    time.sleep(2)  # Update every 2 seconds
                except Exception as e:
                    print(f"Error in update loop: {e}")
                    break
                    
        self.update_thread = threading.Thread(target=update_loop, daemon=True)
        self.update_thread.start()
        
    def _on_close(self):
        """Handle window close event"""
        self.is_running = False
        if self.update_thread:
            self.update_thread = None
        if self.window:
            self.window.destroy()
            self.window = None


# Convenience function for standalone usage
def show_harmony_charts(parent=None, data_manager=None, event_system=None):
    """Show the harmony charts visualization"""
    if not parent:
        parent = tk.Tk()
        parent.withdraw()
        
    if not data_manager:
        data_manager = DataManager()
        
    if not event_system:
        event_system = EventSystem()
        
    visualization = HarmonyChartsVisualization(parent, data_manager, event_system)
    visualization.show()
    return visualization


if __name__ == "__main__":
    # Standalone demo
    root = tk.Tk()
    root.title("Sacred Harmony Charts Demo")
    root.geometry("300x200")
    
    def launch_demo():
        show_harmony_charts(root)
    
    demo_button = ttk.Button(root, text="Launch Harmony Charts", command=launch_demo)
    demo_button.pack(expand=True)
    
    root.mainloop()
