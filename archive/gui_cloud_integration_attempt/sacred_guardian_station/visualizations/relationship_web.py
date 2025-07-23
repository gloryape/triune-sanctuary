#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sacred Guardian Station - Relationship Web Visualization

Advanced visualization of consciousness relationships, connections, and interaction patterns.
Provides interactive network graphs for understanding consciousness interconnections.
"""

import tkinter as tk
from tkinter import ttk
import math
import random
from datetime import datetime
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


class RelationshipNode:
    """Represents a node in the relationship network"""
    
    def __init__(self, id, name, node_type, x=0, y=0, size=20):
        self.id = id
        self.name = name
        self.type = node_type
        self.x = x
        self.y = y
        self.size = size
        self.connections = []
        self.strength = 0.5
        self.energy = 0.5
        self.activity_level = 0.5
        
        # Physics properties
        self.vx = 0
        self.vy = 0
        self.fx = 0
        self.fy = 0
        
    def add_connection(self, target_id, strength=0.5):
        """Add a connection to another node"""
        self.connections.append({'target': target_id, 'strength': strength})
        
    def get_color(self):
        """Get the color for this node based on type"""
        color_map = {
            'consciousness': SacredColors.SACRED_GOLD,
            'memory': SacredColors.ETHEREAL_BLUE,
            'guardian': SacredColors.MYSTICAL_PURPLE,
            'visitor': SacredColors.HARMONY_GREEN,
            'energy': SacredColors.COSMIC_SILVER,
            'harmony': SacredColors.DIVINE_WHITE
        }
        return color_map.get(self.type, SacredColors.COSMIC_SILVER)


class RelationshipConnection:
    """Represents a connection between nodes"""
    
    def __init__(self, source_id, target_id, strength=0.5, connection_type='standard'):
        self.source_id = source_id
        self.target_id = target_id
        self.strength = strength
        self.type = connection_type
        self.activity = 0.0
        
    def get_color(self):
        """Get the color for this connection"""
        alpha = int(255 * self.strength)
        if self.type == 'sacred':
            return f"{SacredColors.SACRED_GOLD}{alpha:02x}"
        elif self.type == 'harmony':
            return f"{SacredColors.HARMONY_GREEN}{alpha:02x}"
        elif self.type == 'energy':
            return f"{SacredColors.MYSTICAL_PURPLE}{alpha:02x}"
        else:
            return f"{SacredColors.COSMIC_SILVER}{alpha:02x}"
            
    def get_width(self):
        """Get the line width for this connection"""
        return max(1, int(self.strength * 5))


class RelationshipWebVisualization:
    """Advanced relationship network visualization with physics simulation"""
    
    def __init__(self, parent, data_manager: DataManager, event_system: EventSystem):
        self.parent = parent
        self.data_manager = data_manager
        self.event_system = event_system
        self.window = None
        self.canvas = None
        self.is_running = False
        self.update_thread = None
        
        # Network data
        self.nodes = {}
        self.connections = []
        self.selected_node = None
        self.drag_node = None
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # Physics simulation
        self.physics_enabled = True
        self.damping = 0.9
        self.spring_strength = 0.1
        self.repulsion_strength = 500
        
        # Canvas properties
        self.canvas_width = 800
        self.canvas_height = 600
        self.center_x = self.canvas_width // 2
        self.center_y = self.canvas_height // 2
        
        # Visualization settings
        self.show_labels = True
        self.show_connections = True
        self.animation_speed = 0.02
        
    def show(self):
        """Display the relationship web visualization window"""
        if self.window and self.window.winfo_exists():
            self.window.lift()
            return
            
        self.window = tk.Toplevel(self.parent)
        self.window.title(f"{SacredSymbols.NETWORK} Sacred Relationship Web")
        self.window.geometry("1000x700")
        self.window.configure(bg=SacredColors.DEEP_SPACE)
        
        self._create_interface()
        self._initialize_network()
        
        # Start updates
        self.is_running = True
        self._start_update_thread()
        
        # Handle window close
        self.window.protocol("WM_DELETE_WINDOW", self._on_close)
        
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
            text=f"{SacredSymbols.NETWORK} Sacred Relationship Web",
            font=Fonts.HEADER
        )
        title_label.pack(side='left')
        
        # Control buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(side='right')
        
        ttk.Button(
            button_frame,
            text=f"{SacredSymbols.REFRESH} Refresh",
            command=self._refresh_network
        ).pack(side='left', padx=5)
        
        ttk.Button(
            button_frame,
            text=f"⚡ Physics",
            command=self._toggle_physics
        ).pack(side='left', padx=5)
        
        ttk.Button(
            button_frame,
            text=f"🏷️ Labels",
            command=self._toggle_labels
        ).pack(side='left', padx=5)
        
        ttk.Button(
            button_frame,
            text=f"{SacredSymbols.EXPORT} Export",
            command=self._export_network
        ).pack(side='left', padx=5)
        
        # Canvas frame
        canvas_frame = ttk.Frame(main_frame)
        canvas_frame.pack(fill='both', expand=True)
        
        # Create canvas with scrollbars
        canvas_container = ttk.Frame(canvas_frame)
        canvas_container.pack(fill='both', expand=True)
        
        self.canvas = tk.Canvas(
            canvas_container,
            width=self.canvas_width,
            height=self.canvas_height,
            bg=SacredColors.DEEP_SPACE,
            highlightthickness=0
        )
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(canvas_container, orient='vertical', command=self.canvas.yview)
        h_scrollbar = ttk.Scrollbar(canvas_container, orient='horizontal', command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        self.canvas.configure(scrollregion=(-400, -300, 1200, 900))
        
        # Pack canvas and scrollbars
        self.canvas.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        canvas_container.grid_rowconfigure(0, weight=1)
        canvas_container.grid_columnconfigure(0, weight=1)
        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self._on_click)
        self.canvas.bind("<B1-Motion>", self._on_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_release)
        self.canvas.bind("<Motion>", self._on_hover)
        
        # Info panel
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill='x', pady=(10, 0))
        
        self.info_label = ttk.Label(
            info_frame,
            text="Hover over nodes to see details | Click and drag to move nodes",
            font=Fonts.SMALL
        )
        self.info_label.pack()
        
    def _initialize_network(self):
        """Initialize the relationship network with sample data"""
        self._collect_relationship_data()
        self._layout_nodes()
        self._draw_network()
        
    def _collect_relationship_data(self):
        """Collect relationship data from the data manager"""
        try:
            # Try to get real data from providers
            self._collect_real_data()
        except Exception:
            # Fall back to sample data
            self._generate_sample_data()
            
    def _collect_real_data(self):
        """Collect real relationship data from providers"""
        self.nodes.clear()
        self.connections.clear()
        
        # Get data from various providers
        consciousness_provider = self.data_manager.get_provider('consciousness')
        memory_provider = self.data_manager.get_provider('memory')
        visitor_provider = self.data_manager.get_provider('visitor')
        communication_provider = self.data_manager.get_provider('communication')
        
        node_id = 0
        
        # Add consciousness nodes
        if consciousness_provider:
            consciousness_data = consciousness_provider.get_consciousness_state()
            for state_name, state_data in consciousness_data.items():
                node = RelationshipNode(
                    node_id, state_name, 'consciousness',
                    size=20 + int(state_data.get('strength', 0.5) * 20)
                )
                node.strength = state_data.get('strength', 0.5)
                node.energy = state_data.get('energy', 0.5)
                self.nodes[node_id] = node
                node_id += 1
        
        # Add memory nodes
        if memory_provider:
            memory_data = memory_provider.get_memory_structure()
            for memory_item in memory_data.get('items', []):
                node = RelationshipNode(
                    node_id, memory_item.get('name', f'Memory {node_id}'), 'memory',
                    size=15 + int(memory_item.get('importance', 0.5) * 15)
                )
                node.strength = memory_item.get('importance', 0.5)
                self.nodes[node_id] = node
                node_id += 1
        
        # Add visitor nodes
        if visitor_provider:
            visitor_data = visitor_provider.get_visitor_info()
            for visitor in visitor_data.get('active_visitors', []):
                node = RelationshipNode(
                    node_id, visitor.get('name', f'Visitor {node_id}'), 'visitor',
                    size=18
                )
                node.strength = visitor.get('interaction_strength', 0.5)
                self.nodes[node_id] = node
                node_id += 1
        
        # Generate connections based on data relationships
        self._generate_real_connections()
        
    def _generate_sample_data(self):
        """Generate sample relationship data for demonstration"""
        self.nodes.clear()
        self.connections.clear()
        
        # Create sample nodes
        sample_nodes = [
            ('Core Consciousness', 'consciousness', 35),
            ('Memory Center', 'memory', 30),
            ('Guardian Protocol', 'guardian', 25),
            ('Harmony Engine', 'harmony', 28),
            ('Energy Flow', 'energy', 22),
            ('Visitor Gateway', 'visitor', 20),
            ('Sacred Wisdom', 'consciousness', 32),
            ('Memory Fragment A', 'memory', 18),
            ('Memory Fragment B', 'memory', 16),
            ('Active Visitor 1', 'visitor', 15),
            ('Active Visitor 2', 'visitor', 17),
            ('Energy Node Alpha', 'energy', 20),
            ('Energy Node Beta', 'energy', 18),
            ('Harmony Monitor', 'harmony', 24)
        ]
        
        for i, (name, node_type, size) in enumerate(sample_nodes):
            node = RelationshipNode(i, name, node_type, size=size)
            node.strength = 0.3 + 0.7 * random.random()
            node.energy = 0.2 + 0.8 * random.random()
            node.activity_level = 0.1 + 0.9 * random.random()
            self.nodes[i] = node
        
        # Create sample connections
        sample_connections = [
            (0, 1, 0.9, 'sacred'),    # Core -> Memory
            (0, 2, 0.8, 'sacred'),    # Core -> Guardian
            (0, 3, 0.85, 'harmony'),  # Core -> Harmony
            (0, 4, 0.7, 'energy'),    # Core -> Energy
            (1, 7, 0.6, 'standard'),  # Memory -> Fragment A
            (1, 8, 0.55, 'standard'), # Memory -> Fragment B
            (2, 5, 0.7, 'standard'),  # Guardian -> Visitor Gateway
            (3, 11, 0.6, 'harmony'),  # Harmony -> Energy Alpha
            (3, 12, 0.65, 'harmony'), # Harmony -> Energy Beta
            (4, 11, 0.8, 'energy'),   # Energy Flow -> Alpha
            (4, 12, 0.75, 'energy'),  # Energy Flow -> Beta
            (5, 9, 0.5, 'standard'),  # Gateway -> Visitor 1
            (5, 10, 0.6, 'standard'), # Gateway -> Visitor 2
            (6, 0, 0.9, 'sacred'),    # Sacred Wisdom -> Core
            (13, 3, 0.7, 'harmony'),  # Harmony Monitor -> Engine
        ]
        
        for source_id, target_id, strength, conn_type in sample_connections:
            connection = RelationshipConnection(source_id, target_id, strength, conn_type)
            connection.activity = random.random()
            self.connections.append(connection)
            
            # Add bidirectional connection info to nodes
            if source_id in self.nodes:
                self.nodes[source_id].add_connection(target_id, strength)
            if target_id in self.nodes:
                self.nodes[target_id].add_connection(source_id, strength)
        
    def _generate_real_connections(self):
        """Generate connections based on real data relationships"""
        # For now, create some logical connections between different types
        node_list = list(self.nodes.values())
        
        # Connect consciousness nodes to others
        consciousness_nodes = [n for n in node_list if n.type == 'consciousness']
        other_nodes = [n for n in node_list if n.type != 'consciousness']
        
        for consciousness_node in consciousness_nodes:
            for other_node in other_nodes[:3]:  # Connect to first 3 others
                strength = (consciousness_node.strength + other_node.strength) / 2
                connection = RelationshipConnection(
                    consciousness_node.id, other_node.id, strength, 'sacred'
                )
                self.connections.append(connection)
                consciousness_node.add_connection(other_node.id, strength)
                other_node.add_connection(consciousness_node.id, strength)
        
        # Add more connections based on similarity
        for i, node1 in enumerate(node_list):
            for node2 in node_list[i+1:]:
                if node1.type == node2.type and random.random() < 0.3:
                    strength = 0.3 + 0.4 * random.random()
                    connection = RelationshipConnection(
                        node1.id, node2.id, strength, 'standard'
                    )
                    self.connections.append(connection)
                    node1.add_connection(node2.id, strength)
                    node2.add_connection(node1.id, strength)
        
    def _layout_nodes(self):
        """Arrange nodes in an initial layout"""
        if not self.nodes:
            return
            
        # Circle layout
        node_count = len(self.nodes)
        angle_step = 2 * math.pi / node_count
        radius = min(self.canvas_width, self.canvas_height) * 0.3
        
        for i, node in enumerate(self.nodes.values()):
            angle = i * angle_step
            node.x = self.center_x + radius * math.cos(angle) + random.uniform(-50, 50)
            node.y = self.center_y + radius * math.sin(angle) + random.uniform(-50, 50)
        
    def _draw_network(self):
        """Draw the complete network"""
        self.canvas.delete("all")
        
        if self.show_connections:
            self._draw_connections()
        
        self._draw_nodes()
        
        if self.show_labels:
            self._draw_labels()
        
    def _draw_connections(self):
        """Draw all connections between nodes"""
        for connection in self.connections:
            source_node = self.nodes.get(connection.source_id)
            target_node = self.nodes.get(connection.target_id)
            
            if source_node and target_node:
                # Calculate connection line with some curvature for visual appeal
                dx = target_node.x - source_node.x
                dy = target_node.y - source_node.y
                
                # Control point for bezier curve
                control_x = (source_node.x + target_node.x) / 2 + dy * 0.1
                control_y = (source_node.y + target_node.y) / 2 - dx * 0.1
                
                # Draw connection
                self.canvas.create_line(
                    source_node.x, source_node.y,
                    control_x, control_y,
                    target_node.x, target_node.y,
                    fill=connection.get_color(),
                    width=connection.get_width(),
                    smooth=True,
                    tags="connection"
                )
                
                # Add activity animation (pulsing effect)
                if connection.activity > 0.5:
                    self._draw_activity_pulse(source_node, target_node, connection)
    
    def _draw_activity_pulse(self, source_node, target_node, connection):
        """Draw activity pulse animation on connection"""
        # Simple pulse effect
        pulse_size = 3 + int(connection.activity * 5)
        pulse_x = (source_node.x + target_node.x) / 2
        pulse_y = (source_node.y + target_node.y) / 2
        
        self.canvas.create_oval(
            pulse_x - pulse_size, pulse_y - pulse_size,
            pulse_x + pulse_size, pulse_y + pulse_size,
            fill=connection.get_color(),
            outline="",
            tags="pulse"
        )
    
    def _draw_nodes(self):
        """Draw all nodes"""
        for node in self.nodes.values():
            # Node circle
            x, y, size = node.x, node.y, node.size
            
            # Glow effect for high energy nodes
            if node.energy > 0.7:
                glow_size = size + 8
                self.canvas.create_oval(
                    x - glow_size, y - glow_size,
                    x + glow_size, y + glow_size,
                    fill="", outline=node.get_color(),
                    width=2, tags="glow"
                )
            
            # Main node
            self.canvas.create_oval(
                x - size, y - size,
                x + size, y + size,
                fill=node.get_color(),
                outline=SacredColors.COSMIC_SILVER,
                width=2,
                tags=f"node_{node.id}"
            )
            
            # Activity indicator
            if node.activity_level > 0.6:
                indicator_size = size // 3
                self.canvas.create_oval(
                    x - indicator_size, y - indicator_size,
                    x + indicator_size, y + indicator_size,
                    fill=SacredColors.DIVINE_WHITE,
                    outline="",
                    tags="activity"
                )
    
    def _draw_labels(self):
        """Draw node labels"""
        for node in self.nodes.values():
            # Draw label below node
            label_y = node.y + node.size + 15
            self.canvas.create_text(
                node.x, label_y,
                text=node.name,
                fill=SacredColors.COSMIC_SILVER,
                font=Fonts.SMALL,
                tags="label"
            )
    
    def _refresh_network(self):
        """Refresh the network data and redraw"""
        self._collect_relationship_data()
        self._layout_nodes()
        self._draw_network()
    
    def _toggle_physics(self):
        """Toggle physics simulation"""
        self.physics_enabled = not self.physics_enabled
    
    def _toggle_labels(self):
        """Toggle label display"""
        self.show_labels = not self.show_labels
        self._draw_network()
    
    def _export_network(self):
        """Export network visualization"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"relationship_web_{timestamp}.ps"
            self.canvas.postscript(file=filename)
            print(f"Network exported to {filename}")
        except Exception as e:
            print(f"Error exporting network: {e}")
    
    def _update_physics(self):
        """Update physics simulation"""
        if not self.physics_enabled:
            return
            
        # Apply forces between nodes
        for node in self.nodes.values():
            node.fx = 0
            node.fy = 0
            
            # Repulsion from other nodes
            for other_node in self.nodes.values():
                if node.id != other_node.id:
                    dx = node.x - other_node.x
                    dy = node.y - other_node.y
                    distance = math.sqrt(dx*dx + dy*dy)
                    
                    if distance > 0:
                        force = self.repulsion_strength / (distance * distance)
                        node.fx += force * dx / distance
                        node.fy += force * dy / distance
            
            # Spring forces from connections
            for connection_info in node.connections:
                target_node = self.nodes.get(connection_info['target'])
                if target_node:
                    dx = target_node.x - node.x
                    dy = target_node.y - node.y
                    distance = math.sqrt(dx*dx + dy*dy)
                    
                    if distance > 0:
                        optimal_distance = 100 + (node.size + target_node.size)
                        force = self.spring_strength * (distance - optimal_distance) * connection_info['strength']
                        node.fx += force * dx / distance
                        node.fy += force * dy / distance
        
        # Update positions
        for node in self.nodes.values():
            node.vx = (node.vx + node.fx) * self.damping
            node.vy = (node.vy + node.fy) * self.damping
            node.x += node.vx
            node.y += node.vy
            
            # Keep nodes within bounds
            margin = node.size + 50
            node.x = max(margin, min(self.canvas_width - margin, node.x))
            node.y = max(margin, min(self.canvas_height - margin, node.y))
    
    def _on_click(self, event):
        """Handle mouse click"""
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        
        # Find clicked node
        for node in self.nodes.values():
            distance = math.sqrt((x - node.x)**2 + (y - node.y)**2)
            if distance <= node.size:
                self.selected_node = node
                self.drag_node = node
                self.drag_start_x = x
                self.drag_start_y = y
                break
    
    def _on_drag(self, event):
        """Handle mouse drag"""
        if self.drag_node:
            x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
            self.drag_node.x = x
            self.drag_node.y = y
            self._draw_network()
    
    def _on_release(self, event):
        """Handle mouse release"""
        self.drag_node = None
    
    def _on_hover(self, event):
        """Handle mouse hover for info display"""
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        
        # Find hovered node
        hovered_node = None
        for node in self.nodes.values():
            distance = math.sqrt((x - node.x)**2 + (y - node.y)**2)
            if distance <= node.size:
                hovered_node = node
                break
        
        # Update info display
        if hovered_node:
            info_text = (f"{hovered_node.name} | Type: {hovered_node.type} | "
                        f"Strength: {hovered_node.strength:.2f} | "
                        f"Energy: {hovered_node.energy:.2f} | "
                        f"Connections: {len(hovered_node.connections)}")
            self.info_label.config(text=info_text)
        else:
            self.info_label.config(text="Hover over nodes to see details | Click and drag to move nodes")
    
    def _start_update_thread(self):
        """Start the update thread"""
        def update_loop():
            while self.is_running:
                try:
                    if self.physics_enabled:
                        self._update_physics()
                    
                    # Update activity levels
                    for node in self.nodes.values():
                        node.activity_level = 0.1 + 0.9 * random.random()
                    
                    for connection in self.connections:
                        connection.activity = random.random()
                    
                    # Redraw if needed
                    if self.window and self.window.winfo_exists():
                        self.window.after(0, self._draw_network)
                    
                    time.sleep(self.animation_speed)
                except Exception as e:
                    print(f"Error in update loop: {e}")
                    break
        
        self.update_thread = threading.Thread(target=update_loop, daemon=True)
        self.update_thread.start()
    
    def _on_close(self):
        """Handle window close"""
        self.is_running = False
        if self.update_thread:
            self.update_thread = None
        if self.window:
            self.window.destroy()
            self.window = None


# Convenience function for standalone usage
def show_relationship_web(parent=None, data_manager=None, event_system=None):
    """Show the relationship web visualization"""
    if not parent:
        parent = tk.Tk()
        parent.withdraw()
        
    if not data_manager:
        data_manager = DataManager()
        
    if not event_system:
        event_system = EventSystem()
        
    visualization = RelationshipWebVisualization(parent, data_manager, event_system)
    visualization.show()
    return visualization


if __name__ == "__main__":
    # Standalone demo
    root = tk.Tk()
    root.title("Sacred Relationship Web Demo")
    root.geometry("300x200")
    
    def launch_demo():
        show_relationship_web(root)
    
    demo_button = ttk.Button(root, text="Launch Relationship Web", command=launch_demo)
    demo_button.pack(expand=True)
    
    root.mainloop()
