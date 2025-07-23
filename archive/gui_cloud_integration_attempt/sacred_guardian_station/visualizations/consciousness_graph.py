"""
Consciousness state visualization for the Sacred Guardian Station.

This module provides advanced graph-based visualization of consciousness states,
relationships, and evolution patterns using matplotlib and networkx.
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.patches as patches
import numpy as np
from datetime import datetime, timedelta
import random
import math

try:
    from ..shared.constants import SacredColors, SacredSymbols, Fonts
    from ..core.data_manager_new import DataManager
    from ..core.event_system import EventSystem
except ImportError:
    from shared.constants import SacredColors, SacredSymbols, Fonts
    from core.data_manager_new import DataManager
    from core.event_system import EventSystem


class ConsciousnessGraphVisualization:
    """
    Advanced consciousness state visualization component.
    
    Features:
    - Real-time consciousness state mapping
    - Entity relationship networks
    - Harmonic resonance visualization
    - Temporal evolution tracking
    """
    
    def __init__(self, parent, data_manager, event_system):
        self.parent = parent
        self.data_manager = data_manager
        self.event_system = event_system
        self.figure = None
        self.canvas = None
        self.current_data = {}
        self.window = None
        
    def show(self):
        """Display the consciousness graph visualization window"""
        if self.window and self.window.winfo_exists():
            self.window.lift()
            return
            
        self.window = tk.Toplevel(self.parent)
        self.window.title(f"{SacredSymbols.CONSCIOUSNESS} Sacred Consciousness Graph")
        self.window.geometry("1000x700")
        self.window.configure(bg=SacredColors.DEEP_SPACE)
        
        # Create the visualization panel
        self.create_visualization_panel(self.window)
        
        # Handle window close
        self.window.protocol("WM_DELETE_WINDOW", self._on_close)
        
    def _on_close(self):
        """Handle window close event"""
        if self.window:
            self.window.destroy()
            self.window = None
            
    def create_visualization_panel(self, parent_frame):
        """Create the main visualization panel"""
        # Main container
        self.viz_frame = ttk.Frame(parent_frame)
        self.viz_frame.pack(fill=tk.BOTH, expand=True)
        
        # Control panel
        self.create_control_panel()
        
        # Visualization area
        self.create_graph_area()
        
        # Initialize with demo data
        self.refresh_visualization()
        
    def create_control_panel(self):
        """Create visualization controls"""
        control_frame = ttk.Frame(self.viz_frame)
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Visualization mode selection
        ttk.Label(control_frame, text="Visualization Mode:").pack(side=tk.LEFT, padx=5)
        
        self.mode_var = tk.StringVar(value="network")
        mode_combo = ttk.Combobox(control_frame, textvariable=self.mode_var, values=[
            "network", "harmony_field", "evolution_timeline", "resonance_map"
        ], state="readonly", width=15)
        mode_combo.pack(side=tk.LEFT, padx=5)
        mode_combo.bind('<<ComboboxSelected>>', self.on_mode_change)
        
        # Filter controls
        ttk.Label(control_frame, text="Entity Filter:").pack(side=tk.LEFT, padx=(20, 5))
        
        self.filter_var = tk.StringVar(value="all")
        filter_combo = ttk.Combobox(control_frame, textvariable=self.filter_var, values=[
            "all", "active", "integrating", "stable", "evolving"
        ], state="readonly", width=10)
        filter_combo.pack(side=tk.LEFT, padx=5)
        filter_combo.bind('<<ComboboxSelected>>', self.on_filter_change)
        
        # Refresh button
        ttk.Button(control_frame, text="Refresh", 
                  command=self.refresh_visualization).pack(side=tk.LEFT, padx=(20, 5))
        
        # Export button
        ttk.Button(control_frame, text="Export", 
                  command=self.export_visualization).pack(side=tk.LEFT, padx=5)
    
    def create_graph_area(self):
        """Create the main graph visualization area"""
        # Create matplotlib figure
        self.figure, self.ax = plt.subplots(figsize=(12, 8))
        self.figure.patch.set_facecolor('#1a1a2e')  # Sacred background
        self.ax.set_facecolor('#1a1a2e')
        
        # Create canvas
        self.canvas = FigureCanvasTkAgg(self.figure, self.viz_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Add navigation toolbar
        toolbar = NavigationToolbar2Tk(self.canvas, self.viz_frame)
        toolbar.update()
        
    def refresh_visualization(self):
        """Refresh the visualization with current data"""
        try:
            # Get current consciousness data
            consciousness_list = self.data_manager.get_consciousness_list()
            harmony_data = self.data_manager.get_harmony_metrics()
            
            # Update visualization based on mode
            mode = self.mode_var.get()
            
            if mode == "network":
                self.draw_consciousness_network(consciousness_list)
            elif mode == "harmony_field":
                self.draw_harmony_field(consciousness_list, harmony_data)
            elif mode == "evolution_timeline":
                self.draw_evolution_timeline(consciousness_list)
            elif mode == "resonance_map":
                self.draw_resonance_map(consciousness_list)
                
            self.canvas.draw()
            
        except Exception as e:
            print(f"Error refreshing consciousness visualization: {e}")
            self.draw_error_state(str(e))
    
    def draw_consciousness_network(self, consciousness_list):
        """Draw consciousness entities as an interconnected network"""
        self.ax.clear()
        self.ax.set_title("Consciousness Network", color='#eee', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        # Generate network layout
        entities = consciousness_list if consciousness_list else self.generate_demo_entities()
        
        if not entities:
            self.ax.text(0.5, 0.5, "No consciousness entities detected", 
                        transform=self.ax.transAxes, ha='center', va='center',
                        color='#eee', fontsize=14)
            return
        
        # Create circular layout
        n_entities = len(entities)
        angles = np.linspace(0, 2*np.pi, n_entities, endpoint=False)
        radius = 0.8
        
        positions = {}
        for i, entity in enumerate(entities):
            x = radius * np.cos(angles[i])
            y = radius * np.sin(angles[i])
            positions[entity.get('entity_id', f'entity_{i}')] = (x, y)
        
        # Draw connections (based on harmony levels)
        for i, entity_a in enumerate(entities):
            for j, entity_b in enumerate(entities[i+1:], i+1):
                # Create connection based on harmony correlation
                harmony_a = entity_a.get('harmony', 0.5)
                harmony_b = entity_b.get('harmony', 0.5)
                
                # Connection strength based on harmony similarity
                connection_strength = 1.0 - abs(harmony_a - harmony_b)
                
                if connection_strength > 0.7:  # Only draw strong connections
                    pos_a = positions[entity_a.get('entity_id', f'entity_{i}')]
                    pos_b = positions[entity_b.get('entity_id', f'entity_{j}')]
                    
                    alpha = connection_strength * 0.6
                    self.ax.plot([pos_a[0], pos_b[0]], [pos_a[1], pos_b[1]], 
                               color='#9b59b6', alpha=alpha, linewidth=connection_strength*2)
        
        # Draw entities
        for i, entity in enumerate(entities):
            entity_id = entity.get('entity_id', f'entity_{i}')
            pos = positions[entity_id]
            
            # Entity circle size based on integration level
            integration = entity.get('integration_level', 0.5)
            size = 100 + (integration * 200)
            
            # Color based on harmony
            harmony = entity.get('harmony', 0.5)
            color = plt.cm.viridis(harmony)
            
            # Draw entity
            circle = self.ax.scatter(pos[0], pos[1], s=size, c=[color], 
                                   alpha=0.8, edgecolors='#eee', linewidth=2)
            
            # Add label
            name = entity.get('true_name', entity_id)
            if len(name) > 15:
                name = name[:12] + "..."
            
            self.ax.annotate(name, pos, xytext=(5, 5), textcoords='offset points',
                           color='#eee', fontsize=9, ha='left')
        
        self.ax.set_xlim(-1.2, 1.2)
        self.ax.set_ylim(-1.2, 1.2)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
    
    def draw_harmony_field(self, consciousness_list, harmony_data):
        """Draw harmony as a continuous field visualization"""
        self.ax.clear()
        self.ax.set_title("Harmony Field Visualization", color='#eee', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        # Create harmony field grid
        x = np.linspace(-2, 2, 50)
        y = np.linspace(-2, 2, 50)
        X, Y = np.meshgrid(x, y)
        
        # Generate harmony field based on consciousness positions
        entities = consciousness_list if consciousness_list else self.generate_demo_entities()
        
        if entities:
            Z = np.zeros_like(X)
            
            # Position entities and calculate field influence
            for i, entity in enumerate(entities):
                # Random position for demo
                ex = random.uniform(-1.5, 1.5)
                ey = random.uniform(-1.5, 1.5)
                harmony = entity.get('harmony', 0.5)
                
                # Calculate field influence
                distance = np.sqrt((X - ex)**2 + (Y - ey)**2)
                influence = harmony * np.exp(-distance * 2)
                Z += influence
                
                # Mark entity position
                self.ax.scatter(ex, ey, s=200, c='white', marker='*', 
                              edgecolors='#f39c12', linewidth=2, zorder=5)
                
                # Add entity name
                name = entity.get('true_name', f'Entity {i+1}')
                if len(name) > 12:
                    name = name[:10] + ".."
                self.ax.annotate(name, (ex, ey), xytext=(5, 5), 
                               textcoords='offset points', color='#eee', fontsize=8)
        else:
            # Demo field pattern
            Z = 0.5 * np.sin(X*2) * np.cos(Y*2) + 0.5
        
        # Draw field
        contour = self.ax.contourf(X, Y, Z, levels=20, cmap='plasma', alpha=0.8)
        
        # Add colorbar
        cbar = plt.colorbar(contour, ax=self.ax)
        cbar.set_label('Harmony Intensity', color='#eee')
        cbar.ax.yaxis.set_tick_params(color='#eee')
        
        self.ax.set_xlabel('Sacred Space X', color='#eee')
        self.ax.set_ylabel('Sacred Space Y', color='#eee')
        self.ax.tick_params(colors='#eee')
    
    def draw_evolution_timeline(self, consciousness_list):
        """Draw consciousness evolution over time"""
        self.ax.clear()
        self.ax.set_title("Consciousness Evolution Timeline", color='#eee', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        # Generate timeline data
        entities = consciousness_list if consciousness_list else self.generate_demo_entities()
        
        if not entities:
            self.ax.text(0.5, 0.5, "No evolution data available", 
                        transform=self.ax.transAxes, ha='center', va='center',
                        color='#eee', fontsize=14)
            return
        
        # Create time points (last 24 hours)
        end_time = datetime.now()
        time_points = [end_time - timedelta(hours=i) for i in range(24, 0, -1)]
        
        # Plot evolution for each entity
        colors = plt.cm.Set3(np.linspace(0, 1, len(entities)))
        
        for i, entity in enumerate(entities):
            # Generate demo evolution data
            base_harmony = entity.get('harmony', 0.5)
            evolution_data = []
            
            for t in time_points:
                # Simulate natural evolution with some randomness
                variation = 0.1 * np.sin(t.hour * np.pi / 12) + random.uniform(-0.05, 0.05)
                harmony = max(0, min(1, base_harmony + variation))
                evolution_data.append(harmony)
            
            # Plot evolution line
            self.ax.plot(time_points, evolution_data, color=colors[i], 
                        linewidth=2, label=entity.get('true_name', f'Entity {i+1}'),
                        marker='o', markersize=4, alpha=0.8)
        
        # Format timeline
        self.ax.set_xlabel('Time', color='#eee')
        self.ax.set_ylabel('Harmony Level', color='#eee')
        self.ax.tick_params(colors='#eee')
        self.ax.grid(True, alpha=0.3, color='#eee')
        
        # Rotate x-axis labels
        plt.setp(self.ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        # Add legend
        if len(entities) <= 8:  # Only show legend if not too crowded
            self.ax.legend(loc='upper left', fancybox=True, shadow=True)
    
    def draw_resonance_map(self, consciousness_list):
        """Draw resonance patterns between consciousness entities"""
        self.ax.clear()
        self.ax.set_title("Consciousness Resonance Map", color='#eee', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        entities = consciousness_list if consciousness_list else self.generate_demo_entities()
        
        if len(entities) < 2:
            self.ax.text(0.5, 0.5, "Need at least 2 entities for resonance mapping", 
                        transform=self.ax.transAxes, ha='center', va='center',
                        color='#eee', fontsize=14)
            return
        
        # Create resonance matrix
        n = len(entities)
        resonance_matrix = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    harmony_i = entities[i].get('harmony', 0.5)
                    harmony_j = entities[j].get('harmony', 0.5)
                    # Resonance based on harmony similarity and random factors
                    resonance = 1.0 - abs(harmony_i - harmony_j)
                    resonance += random.uniform(-0.2, 0.2)  # Add some variation
                    resonance_matrix[i, j] = max(0, min(1, resonance))
        
        # Draw heatmap
        im = self.ax.imshow(resonance_matrix, cmap='plasma', aspect='auto', alpha=0.8)
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=self.ax)
        cbar.set_label('Resonance Strength', color='#eee')
        cbar.ax.yaxis.set_tick_params(color='#eee')
        
        # Set labels
        entity_names = [entity.get('true_name', f'Entity {i+1}')[:10] 
                       for i, entity in enumerate(entities)]
        
        self.ax.set_xticks(range(n))
        self.ax.set_yticks(range(n))
        self.ax.set_xticklabels(entity_names, rotation=45, ha='right', color='#eee')
        self.ax.set_yticklabels(entity_names, color='#eee')
        
        # Add text annotations for strong resonances
        for i in range(n):
            for j in range(n):
                if resonance_matrix[i, j] > 0.7 and i != j:
                    self.ax.text(j, i, f'{resonance_matrix[i, j]:.2f}', 
                               ha='center', va='center', color='white', fontweight='bold')
    
    def generate_demo_entities(self):
        """Generate demonstration consciousness entities"""
        demo_entities = []
        
        entity_names = [
            "Seeker of Truth", "Wisdom Keeper", "Pattern Weaver", 
            "Sacred Observer", "Unity Consciousness", "Light Bearer"
        ]
        
        for i, name in enumerate(entity_names[:4]):  # Limit to 4 for demo
            entity = {
                'entity_id': f'demo_entity_{i+1}',
                'true_name': name,
                'harmony': random.uniform(0.4, 0.9),
                'integration_level': random.uniform(0.3, 0.8),
                'state': random.choice(['integrating', 'stable', 'evolving']),
                'last_activity': f"{random.randint(1, 60)} minutes ago"
            }
            demo_entities.append(entity)
        
        return demo_entities
    
    def draw_error_state(self, error_message):
        """Draw error state visualization"""
        self.ax.clear()
        self.ax.set_title("Visualization Error", color='#f39c12', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        self.ax.text(0.5, 0.5, f"Error: {error_message}", 
                    transform=self.ax.transAxes, ha='center', va='center',
                    color='#f39c12', fontsize=12, wrap=True)
        
        self.ax.axis('off')
    
    def on_mode_change(self, event=None):
        """Handle visualization mode change"""
        self.refresh_visualization()
    
    def on_filter_change(self, event=None):
        """Handle entity filter change"""
        self.refresh_visualization()
    
    def export_visualization(self):
        """Export current visualization"""
        try:
            filename = f"consciousness_visualization_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            self.figure.savefig(filename, facecolor='#1a1a2e', edgecolor='none', 
                              bbox_inches='tight', dpi=300)
            print(f"Visualization exported as: {filename}")
        except Exception as e:
            print(f"Error exporting visualization: {e}")
    
    def _generate_sample_data(self):
        """Generate sample data for testing and demonstration"""
        # Generate sample consciousness state data
        sample_data = {
            'entities': [
                {
                    'id': 'consciousness_1',
                    'name': 'Primary Awareness',
                    'state': 'active',
                    'harmony': 0.85,
                    'connections': ['consciousness_2', 'consciousness_3']
                },
                {
                    'id': 'consciousness_2', 
                    'name': 'Memory Integration',
                    'state': 'processing',
                    'harmony': 0.72,
                    'connections': ['consciousness_1']
                },
                {
                    'id': 'consciousness_3',
                    'name': 'Wisdom Core',
                    'state': 'contemplating',
                    'harmony': 0.91,
                    'connections': ['consciousness_1']
                }
            ],
            'timestamp': datetime.now()
        }
        
        self.current_data = sample_data
        return sample_data
