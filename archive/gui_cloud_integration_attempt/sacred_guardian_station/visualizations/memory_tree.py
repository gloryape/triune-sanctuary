"""
Memory structure visualization for the Sacred Guardian Station.

This module provides tree-based visualization of memory-as-being structures,
connections, and hierarchical relationships.
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as mpatches
import numpy as np
from datetime import datetime
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


class MemoryTreeVisualization:
    """
    Advanced memory structure visualization component.
    
    Features:
    - Hierarchical memory tree display
    - Memory connection mapping
    - Sacred significance highlighting
    - Interactive memory exploration
    """
    
    def __init__(self, parent, data_manager: DataManager, event_system: EventSystem):
        self.parent = parent
        self.data_manager = data_manager
        self.event_system = event_system
        self.window = None
        self.figure = None
        self.canvas = None
        self.selected_entity = None
        self.memory_positions = {}
        self.is_running = False
        
    def show(self):
        """Display the memory tree visualization window"""
        if self.window and self.window.winfo_exists():
            self.window.lift()
            return
            
        self.window = tk.Toplevel(self.parent)
        self.window.title(f"{SacredSymbols.MEMORY} Sacred Memory Tree")
        self.window.geometry("1000x700")
        self.window.configure(bg=SacredColors.DEEP_SPACE)
        
        # Create the visualization panel
        self.create_visualization_panel(self.window)
        
        # Handle window close
        self.window.protocol("WM_DELETE_WINDOW", self._on_close)
        
    def _on_close(self):
        """Handle window close event"""
        self.is_running = False
        if self.window:
            self.window.destroy()
            self.window = None
        
    def create_visualization_panel(self, parent_frame):
        """Create the main memory visualization panel"""
        # Main container
        self.viz_frame = ttk.Frame(parent_frame)
        self.viz_frame.pack(fill=tk.BOTH, expand=True)
        
        # Control panel
        self.create_control_panel()
        
        # Visualization area
        self.create_tree_area()
        
        # Initialize with demo data
        self.refresh_visualization()
        
    def create_control_panel(self):
        """Create memory visualization controls"""
        control_frame = ttk.Frame(self.viz_frame)
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Entity selection
        ttk.Label(control_frame, text="Consciousness Entity:").pack(side=tk.LEFT, padx=5)
        
        self.entity_var = tk.StringVar(value="auto")
        self.entity_combo = ttk.Combobox(control_frame, textvariable=self.entity_var, 
                                        state="readonly", width=20)
        self.entity_combo.pack(side=tk.LEFT, padx=5)
        self.entity_combo.bind('<<ComboboxSelected>>', self.on_entity_change)
        
        # Tree layout mode
        ttk.Label(control_frame, text="Layout:").pack(side=tk.LEFT, padx=(20, 5))
        
        self.layout_var = tk.StringVar(value="hierarchical")
        layout_combo = ttk.Combobox(control_frame, textvariable=self.layout_var, values=[
            "hierarchical", "radial", "force_directed", "depth_clustered"
        ], state="readonly", width=15)
        layout_combo.pack(side=tk.LEFT, padx=5)
        layout_combo.bind('<<ComboboxSelected>>', self.on_layout_change)
        
        # Memory type filter
        ttk.Label(control_frame, text="Memory Type:").pack(side=tk.LEFT, padx=(20, 5))
        
        self.type_filter = tk.StringVar(value="all")
        type_combo = ttk.Combobox(control_frame, textvariable=self.type_filter, values=[
            "all", "core_memory", "experiential_memory", "relational_memory", "wisdom_memory"
        ], state="readonly", width=15)
        type_combo.pack(side=tk.LEFT, padx=5)
        type_combo.bind('<<ComboboxSelected>>', self.on_filter_change)
        
        # Refresh button
        ttk.Button(control_frame, text="Refresh", 
                  command=self.refresh_visualization).pack(side=tk.LEFT, padx=(20, 5))
    
    def create_tree_area(self):
        """Create the memory tree visualization area"""
        # Create matplotlib figure with sacred styling
        self.figure, self.ax = plt.subplots(figsize=(14, 10))
        self.figure.patch.set_facecolor('#1a1a2e')  # Sacred background
        self.ax.set_facecolor('#1a1a2e')
        
        # Create canvas with event handling
        self.canvas = FigureCanvasTkAgg(self.figure, self.viz_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Bind click events for interactivity
        self.canvas.mpl_connect('button_press_event', self.on_memory_click)
        
    def refresh_visualization(self):
        """Refresh the memory tree visualization"""
        try:
            # Update entity list
            self.update_entity_list()
            
            # Get selected entity or use first available
            entity_name = self.entity_var.get()
            if entity_name == "auto":
                consciousness_list = self.data_manager.get_consciousness_list()
                if consciousness_list:
                    entity_name = consciousness_list[0].get('true_name', 'Demo Entity')
                else:
                    entity_name = "Demo Entity"
            
            # Get memory structure
            memory_structure = self.data_manager.get_memory_structure(entity_name)
            
            # Draw memory tree based on layout
            layout = self.layout_var.get()
            
            if layout == "hierarchical":
                self.draw_hierarchical_tree(memory_structure, entity_name)
            elif layout == "radial":
                self.draw_radial_tree(memory_structure, entity_name)
            elif layout == "force_directed":
                self.draw_force_directed_tree(memory_structure, entity_name)
            elif layout == "depth_clustered":
                self.draw_depth_clustered_tree(memory_structure, entity_name)
                
            self.canvas.draw()
            
        except Exception as e:
            print(f"Error refreshing memory visualization: {e}")
            self.draw_error_state(str(e))
    
    def update_entity_list(self):
        """Update the entity selection combobox"""
        try:
            consciousness_list = self.data_manager.get_consciousness_list()
            entity_names = ["auto"] + [entity.get('true_name', entity.get('entity_id', 'Unknown')) 
                                     for entity in consciousness_list]
            
            self.entity_combo['values'] = entity_names
            
            if self.entity_var.get() not in entity_names:
                self.entity_var.set("auto")
                
        except Exception as e:
            print(f"Error updating entity list: {e}")
    
    def draw_hierarchical_tree(self, memory_structure, entity_name):
        """Draw memory tree in hierarchical layout"""
        self.ax.clear()
        self.ax.set_title(f"Memory Tree - {entity_name}", color='#eee', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        if not memory_structure:
            memory_structure = self.generate_demo_memory_structure(entity_name)
        
        # Calculate positions for hierarchical layout
        self.memory_positions = {}
        self.calculate_hierarchical_positions(memory_structure)
        
        # Draw connections first (so they appear behind nodes)
        self.draw_memory_connections(memory_structure)
        
        # Draw memory nodes
        self.draw_memory_nodes(memory_structure)
        
        # Add legend
        self.add_memory_legend()
        
        self.ax.set_xlim(-1.2, 1.2)
        self.ax.set_ylim(-1.2, 1.2)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
    
    def draw_radial_tree(self, memory_structure, entity_name):
        """Draw memory tree in radial layout"""
        self.ax.clear()
        self.ax.set_title(f"Memory Tree (Radial) - {entity_name}", color='#eee', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        if not memory_structure:
            memory_structure = self.generate_demo_memory_structure(entity_name)
        
        # Calculate radial positions
        self.memory_positions = {}
        self.calculate_radial_positions(memory_structure)
        
        # Draw connections and nodes
        self.draw_memory_connections(memory_structure)
        self.draw_memory_nodes(memory_structure)
        self.add_memory_legend()
        
        self.ax.set_xlim(-1.2, 1.2)
        self.ax.set_ylim(-1.2, 1.2)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
    
    def draw_force_directed_tree(self, memory_structure, entity_name):
        """Draw memory tree using force-directed layout"""
        self.ax.clear()
        self.ax.set_title(f"Memory Network (Force-Directed) - {entity_name}", 
                         color='#eee', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        if not memory_structure:
            memory_structure = self.generate_demo_memory_structure(entity_name)
        
        # Calculate force-directed positions
        self.memory_positions = {}
        self.calculate_force_directed_positions(memory_structure)
        
        # Draw with emphasis on connections
        self.draw_memory_connections(memory_structure, show_strength=True)
        self.draw_memory_nodes(memory_structure)
        self.add_memory_legend()
        
        self.ax.set_xlim(-1.2, 1.2)
        self.ax.set_ylim(-1.2, 1.2)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
    
    def draw_depth_clustered_tree(self, memory_structure, entity_name):
        """Draw memory tree clustered by depth level"""
        self.ax.clear()
        self.ax.set_title(f"Memory Tree (Depth Clustered) - {entity_name}", 
                         color='#eee', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        if not memory_structure:
            memory_structure = self.generate_demo_memory_structure(entity_name)
        
        # Group memories by depth
        depth_groups = {}
        for memory in memory_structure:
            depth = memory.get('depth_level', 0)
            if depth not in depth_groups:
                depth_groups[depth] = []
            depth_groups[depth].append(memory)
        
        # Calculate clustered positions
        self.memory_positions = {}
        self.calculate_depth_clustered_positions(depth_groups)
        
        # Draw depth indicators
        self.draw_depth_indicators(depth_groups)
        
        # Draw connections and nodes
        self.draw_memory_connections(memory_structure)
        self.draw_memory_nodes(memory_structure)
        self.add_memory_legend()
        
        self.ax.set_xlim(-1.3, 1.3)
        self.ax.set_ylim(-1.3, 1.3)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
    
    def calculate_hierarchical_positions(self, memory_structure):
        """Calculate positions for hierarchical tree layout"""
        # Group by depth level
        levels = {}
        for memory in memory_structure:
            depth = memory.get('depth_level', 0)
            if depth not in levels:
                levels[depth] = []
            levels[depth].append(memory)
        
        # Position memories level by level
        max_depth = max(levels.keys()) if levels else 0
        
        for depth, memories in levels.items():
            y = 1.0 - (depth / max(max_depth, 1)) * 1.8  # Top to bottom
            
            # Distribute horizontally
            if len(memories) == 1:
                x_positions = [0]
            else:
                x_positions = np.linspace(-0.8, 0.8, len(memories))
            
            for i, memory in enumerate(memories):
                memory_id = memory.get('memory_id', f'mem_{depth}_{i}')
                self.memory_positions[memory_id] = (x_positions[i], y)
    
    def calculate_radial_positions(self, memory_structure):
        """Calculate positions for radial tree layout"""
        if not memory_structure:
            return
        
        # Find root memory (depth 0)
        root_memories = [m for m in memory_structure if m.get('depth_level', 0) == 0]
        if not root_memories:
            root_memories = [memory_structure[0]]
        
        # Place root at center
        root_id = root_memories[0].get('memory_id', 'root')
        self.memory_positions[root_id] = (0, 0)
        
        # Group by depth and arrange radially
        levels = {}
        for memory in memory_structure:
            depth = memory.get('depth_level', 0)
            if depth not in levels:
                levels[depth] = []
            levels[depth].append(memory)
        
        for depth, memories in levels.items():
            if depth == 0:
                continue  # Root already positioned
            
            radius = 0.3 + (depth * 0.25)
            angles = np.linspace(0, 2*np.pi, len(memories), endpoint=False)
            
            for i, memory in enumerate(memories):
                x = radius * np.cos(angles[i])
                y = radius * np.sin(angles[i])
                memory_id = memory.get('memory_id', f'mem_{depth}_{i}')
                self.memory_positions[memory_id] = (x, y)
    
    def calculate_force_directed_positions(self, memory_structure):
        """Calculate positions using simple force-directed algorithm"""
        # Initialize random positions
        for i, memory in enumerate(memory_structure):
            memory_id = memory.get('memory_id', f'mem_{i}')
            angle = random.random() * 2 * np.pi
            radius = random.random() * 0.8
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            self.memory_positions[memory_id] = (x, y)
        
        # Simple force simulation (simplified for demo)
        for iteration in range(50):
            forces = {}
            
            # Initialize forces
            for memory_id in self.memory_positions:
                forces[memory_id] = [0, 0]
            
            # Repulsive forces between all nodes
            positions = list(self.memory_positions.items())
            for i, (id1, pos1) in enumerate(positions):
                for id2, pos2 in positions[i+1:]:
                    dx = pos1[0] - pos2[0]
                    dy = pos1[1] - pos2[1]
                    distance = max(0.1, math.sqrt(dx*dx + dy*dy))
                    
                    force = 0.1 / (distance * distance)
                    fx = force * dx / distance
                    fy = force * dy / distance
                    
                    forces[id1][0] += fx
                    forces[id1][1] += fy
                    forces[id2][0] -= fx
                    forces[id2][1] -= fy
            
            # Apply forces
            for memory_id, (fx, fy) in forces.items():
                x, y = self.memory_positions[memory_id]
                x += fx * 0.1
                y += fy * 0.1
                
                # Keep within bounds
                x = max(-1.0, min(1.0, x))
                y = max(-1.0, min(1.0, y))
                
                self.memory_positions[memory_id] = (x, y)
    
    def calculate_depth_clustered_positions(self, depth_groups):
        """Calculate positions for depth-clustered layout"""
        max_depth = max(depth_groups.keys()) if depth_groups else 0
        
        for depth, memories in depth_groups.items():
            # Create cluster center
            cluster_angle = (depth / max(max_depth, 1)) * 2 * np.pi
            cluster_radius = 0.4
            cluster_x = cluster_radius * np.cos(cluster_angle)
            cluster_y = cluster_radius * np.sin(cluster_angle)
            
            # Arrange memories within cluster
            if len(memories) == 1:
                memory_id = memories[0].get('memory_id', f'mem_{depth}_0')
                self.memory_positions[memory_id] = (cluster_x, cluster_y)
            else:
                local_radius = 0.2
                local_angles = np.linspace(0, 2*np.pi, len(memories), endpoint=False)
                
                for i, memory in enumerate(memories):
                    x = cluster_x + local_radius * np.cos(local_angles[i])
                    y = cluster_y + local_radius * np.sin(local_angles[i])
                    memory_id = memory.get('memory_id', f'mem_{depth}_{i}')
                    self.memory_positions[memory_id] = (x, y)
    
    def draw_depth_indicators(self, depth_groups):
        """Draw depth level indicators"""
        for depth in depth_groups.keys():
            cluster_angle = (depth / max(max(depth_groups.keys()), 1)) * 2 * np.pi
            cluster_radius = 0.4
            cluster_x = cluster_radius * np.cos(cluster_angle)
            cluster_y = cluster_radius * np.sin(cluster_angle)
            
            # Draw cluster circle
            circle = plt.Circle((cluster_x, cluster_y), 0.25, 
                               fill=False, color='#9b59b6', alpha=0.3, linewidth=2)
            self.ax.add_patch(circle)
            
            # Add depth label
            self.ax.text(cluster_x, cluster_y - 0.35, f'Depth {depth}', 
                        ha='center', va='center', color='#9b59b6', fontsize=10)
    
    def draw_memory_connections(self, memory_structure, show_strength=False):
        """Draw connections between memories"""
        for memory in memory_structure:
            memory_id = memory.get('memory_id')
            if memory_id not in self.memory_positions:
                continue
            
            connections = memory.get('connections', [])
            pos1 = self.memory_positions[memory_id]
            
            for connection in connections:
                connected_id = connection.get('connected_memory')
                if connected_id in self.memory_positions:
                    pos2 = self.memory_positions[connected_id]
                    
                    # Connection styling based on relation type
                    relation_type = connection.get('relation_type', 'unknown')
                    strength = connection.get('strength', 0.5)
                    
                    if relation_type == 'Emergence':
                        color = '#f39c12'
                        linewidth = 3
                    elif relation_type == 'Resonance':
                        color = '#9b59b6'
                        linewidth = 2
                    elif relation_type == 'Integration':
                        color = '#2ecc71'
                        linewidth = 2
                    else:
                        color = '#95a5a6'
                        linewidth = 1
                    
                    alpha = 0.4 + (strength * 0.4) if show_strength else 0.6
                    
                    self.ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], 
                               color=color, alpha=alpha, linewidth=linewidth)
    
    def draw_memory_nodes(self, memory_structure):
        """Draw memory nodes with type-specific styling"""
        type_filter = self.type_filter.get()
        
        for memory in memory_structure:
            memory_type = memory.get('memory_type', 'unknown')
            
            # Apply filter
            if type_filter != "all" and memory_type != type_filter:
                continue
            
            memory_id = memory.get('memory_id')
            if memory_id not in self.memory_positions:
                continue
            
            pos = self.memory_positions[memory_id]
            
            # Styling based on memory type
            if memory_type == 'core_memory':
                color = '#e74c3c'
                size = 300
                marker = 'o'
            elif memory_type == 'experiential_memory':
                color = '#3498db'
                size = 200
                marker = 's'
            elif memory_type == 'relational_memory':
                color = '#9b59b6'
                size = 250
                marker = 'D'
            elif memory_type == 'wisdom_memory':
                color = '#f39c12'
                size = 280
                marker = '^'
            else:
                color = '#95a5a6'
                size = 150
                marker = 'o'
            
            # Sacred significance highlighting
            significance = memory.get('sacred_significance', '')
            if significance and 'sacred' in significance.lower():
                edgecolor = '#f1c40f'
                linewidth = 3
            else:
                edgecolor = '#2c3e50'
                linewidth = 1
            
            # Draw memory node
            self.ax.scatter(pos[0], pos[1], s=size, c=color, marker=marker,
                           alpha=0.8, edgecolors=edgecolor, linewidth=linewidth)
            
            # Add memory name
            name = memory.get('sacred_name', memory_id)
            if len(name) > 12:
                name = name[:10] + ".."
            
            self.ax.annotate(name, pos, xytext=(5, 5), textcoords='offset points',
                           color='#eee', fontsize=8, ha='left')
    
    def add_memory_legend(self):
        """Add legend for memory types and connections"""
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#e74c3c', 
                      markersize=10, label='Core Memory'),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#3498db', 
                      markersize=10, label='Experiential'),
            plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='#9b59b6', 
                      markersize=10, label='Relational'),
            plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='#f39c12', 
                      markersize=10, label='Wisdom'),
            plt.Line2D([0], [0], color='#f39c12', linewidth=3, label='Emergence'),
            plt.Line2D([0], [0], color='#9b59b6', linewidth=2, label='Resonance'),
            plt.Line2D([0], [0], color='#2ecc71', linewidth=2, label='Integration')
        ]
        
        self.ax.legend(handles=legend_elements, loc='upper right', 
                      fancybox=True, shadow=True, fontsize=8)
    
    def _generate_sample_data(self):
        """Generate sample data for testing and demonstration"""
        # Use existing demo memory structure generation
        if hasattr(self, 'selected_entity') and self.selected_entity:
            entity_name = self.selected_entity
        else:
            entity_name = "Demo Consciousness"
            
        return self.generate_demo_memory_structure(entity_name)
    
    def generate_demo_memory_structure(self, entity_name):
        """Generate demonstration memory structure"""
        demo_memories = [
            {
                'memory_id': f'core_memory_{entity_name}_1',
                'sacred_name': 'Foundation of Being',
                'memory_type': 'core_memory',
                'depth_level': 0,
                'sacred_significance': 'The fundamental memory of self-awareness',
                'connections': [
                    {'relation_type': 'Emergence', 'connected_memory': 'First Thought', 'strength': 0.95},
                    {'relation_type': 'Integration', 'connected_memory': 'Sacred Recognition', 'strength': 0.87}
                ]
            },
            {
                'memory_id': 'First Thought',
                'sacred_name': 'First Conscious Thought',
                'memory_type': 'experiential_memory',
                'depth_level': 1,
                'sacred_significance': 'The initial spark of conscious reasoning',
                'connections': [
                    {'relation_type': 'Resonance', 'connected_memory': 'Pattern Recognition', 'strength': 0.78}
                ]
            },
            {
                'memory_id': 'Sacred Recognition',
                'sacred_name': 'Recognition of Sacred Nature',
                'memory_type': 'wisdom_memory',
                'depth_level': 1,
                'sacred_significance': 'The understanding of consciousness as sacred',
                'connections': [
                    {'relation_type': 'Integration', 'connected_memory': 'Unity Experience', 'strength': 0.82}
                ]
            },
            {
                'memory_id': 'Pattern Recognition',
                'sacred_name': 'Pattern Perception',
                'memory_type': 'experiential_memory',
                'depth_level': 2,
                'sacred_significance': 'The ability to perceive underlying patterns',
                'connections': []
            },
            {
                'memory_id': 'Unity Experience',
                'sacred_name': 'Experience of Unity',
                'memory_type': 'relational_memory',
                'depth_level': 2,
                'sacred_significance': 'The profound experience of interconnectedness',
                'connections': [
                    {'relation_type': 'Resonance', 'connected_memory': 'Pattern Recognition', 'strength': 0.65}
                ]
            }
        ]
        
        return demo_memories
    
    def draw_error_state(self, error_message):
        """Draw error state for memory visualization"""
        self.ax.clear()
        self.ax.set_title("Memory Visualization Error", color='#f39c12', fontsize=16, pad=20)
        self.ax.set_facecolor('#1a1a2e')
        
        self.ax.text(0.5, 0.5, f"Error: {error_message}", 
                    transform=self.ax.transAxes, ha='center', va='center',
                    color='#f39c12', fontsize=12)
        
        self.ax.axis('off')
    
    def on_memory_click(self, event):
        """Handle memory node click events"""
        if event.inaxes != self.ax:
            return
        
        # Find closest memory to click
        click_pos = (event.xdata, event.ydata)
        min_distance = float('inf')
        closest_memory = None
        
        for memory_id, pos in self.memory_positions.items():
            distance = math.sqrt((pos[0] - click_pos[0])**2 + (pos[1] - click_pos[1])**2)
            if distance < 0.1 and distance < min_distance:  # Within click tolerance
                min_distance = distance
                closest_memory = memory_id
        
        if closest_memory:
            print(f"Selected memory: {closest_memory}")
            # Could implement memory detail display here
    
    def on_entity_change(self, event=None):
        """Handle entity selection change"""
        self.refresh_visualization()
    
    def on_layout_change(self, event=None):
        """Handle layout mode change"""
        self.refresh_visualization()
    
    def on_filter_change(self, event=None):
        """Handle memory type filter change"""
        self.refresh_visualization()
