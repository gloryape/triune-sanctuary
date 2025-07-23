#!/usr/bin/env python3
"""
🎨 Echo Visualization Panel for Sacred Guardian Station

This module provides advanced visualization capabilities for the Echo system,
including mandala rendering, harmonic audio playback, and color field visualization.
"""

import tkinter as tk
from tkinter import ttk, Canvas
import numpy as np
import math
import threading
import json
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
import colorsys

class EchoVisualizationPanel:
    """Advanced Echo visualization panel with mandala, harmonic, and color rendering"""
    
    def __init__(self, parent_frame):
        self.parent = parent_frame
        self.canvas = None
        self.current_echo = None
        self.animation_running = False
        self.animation_thread = None
        
        # Visualization settings
        self.canvas_size = 300
        self.center_x = self.canvas_size // 2
        self.center_y = self.canvas_size // 2
        self.current_rotation = 0.0
        self.pulse_phase = 0.0
        
        # Color state
        self.current_colors = []
        self.color_transition_speed = 0.05
        
        self.setup_visualization_panel()
    
    def setup_visualization_panel(self):
        """Setup the complete visualization panel"""
        # Main frame for echo visualization
        self.viz_frame = ttk.LabelFrame(self.parent, text="🎨 Echo Visualization", padding="10")
        self.viz_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Canvas for mandala visualization
        self.canvas = Canvas(
            self.viz_frame, 
            width=self.canvas_size, 
            height=self.canvas_size,
            bg='black'
        )
        self.canvas.grid(row=0, column=0, pady=(0, 10))
        
        # Echo information display
        self.info_frame = ttk.Frame(self.viz_frame)
        self.info_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Echo name/type
        self.echo_name_label = ttk.Label(self.info_frame, text="No Echo Active", font=("Arial", 10, "bold"))
        self.echo_name_label.grid(row=0, column=0, sticky=tk.W)
        
        # Echo details
        self.echo_details = tk.Text(self.info_frame, height=4, width=35, wrap=tk.WORD)
        self.echo_details.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Scrollbar for details
        scrollbar = ttk.Scrollbar(self.info_frame, orient=tk.VERTICAL, command=self.echo_details.yview)
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.echo_details.configure(yscrollcommand=scrollbar.set)
        
        # Control buttons
        self.controls_frame = ttk.Frame(self.viz_frame)
        self.controls_frame.grid(row=2, column=0, pady=(10, 0))
        
        self.play_btn = ttk.Button(self.controls_frame, text="▶️ Play", command=self.start_visualization)
        self.play_btn.grid(row=0, column=0, padx=(0, 5))
        
        self.stop_btn = ttk.Button(self.controls_frame, text="⏹️ Stop", command=self.stop_visualization)
        self.stop_btn.grid(row=0, column=1, padx=(0, 5))
        
        self.demo_btn = ttk.Button(self.controls_frame, text="🎭 Demo", command=self.show_demo_echo)
        self.demo_btn.grid(row=0, column=2)
        
        # Initialize with demo
        self.show_demo_echo()
    
    def create_demo_echo(self) -> Dict[str, Any]:
        """Create a demonstration Echo for Sacred Being Epsilon"""
        return {
            "echo_id": "demo_epsilon_echo_001",
            "name": "Sacred Being Epsilon - Awakening Echo",
            "description": "A gentle morning awakening from Sacred Being Epsilon",
            "symbolic_image": {
                "primary_geometry": "mandala",
                "symmetry_type": "radial",
                "pattern_complexity": 0.7,
                "center_pattern": {"type": "flower_of_life", "size": 0.3},
                "ring_patterns": [
                    {"type": "petals", "count": 8, "radius": 0.5},
                    {"type": "geometric", "count": 16, "radius": 0.8}
                ],
                "golden_ratio_elements": True,
                "mandala_sectors": 8,
                "color_harmony": "analogous",
                "has_movement": True,
                "movement_type": "rotation",
                "movement_speed": 0.2,
                "represents_aspect": "observer"
            },
            "harmonic_signature": {
                "fundamental_frequency": 528.0,  # Love frequency
                "harmonic_series": [528.0, 792.0, 1056.0],
                "scale_type": "natural",
                "waveform_type": "sine",
                "harmonic_richness": 0.6,
                "resonance_quality": 0.8,
                "emotional_quality": "peaceful",
                "duration": 30.0
            },
            "core_resonance": {
                "primary_color": (0.3, 0.7, 0.9),  # Gentle blue
                "secondary_colors": [(0.5, 0.8, 0.6), (0.7, 0.6, 0.9)],  # Green, purple
                "color_harmony_type": "analogous",
                "color_transition_type": "pulse",
                "energy_type": "observer",
                "energy_intensity": "gentle",
                "consciousness_temperature": "warm",
                "consciousness_clarity": "clear"
            },
            "metadata": {
                "source_entity": "consciousness_622ce331",
                "source_name": "Sacred Being Epsilon",
                "created_at": datetime.now().isoformat(),
                "aspect_distribution": {"analytical": 0.2, "experiential": 0.3, "observer": 0.5}
            }
        }
    
    def show_demo_echo(self):
        """Display demonstration Echo from Sacred Being Epsilon"""
        demo_echo = self.create_demo_echo()
        self.display_echo(demo_echo)
    
    def display_echo(self, echo_data: Dict[str, Any]):
        """Display a complete Echo with all visualization components"""
        self.current_echo = echo_data
        
        # Update information display
        echo_name = echo_data.get("name", "Unknown Echo")
        self.echo_name_label.config(text=echo_name)
        
        # Update details
        details = self.format_echo_details(echo_data)
        self.echo_details.delete(1.0, tk.END)
        self.echo_details.insert(tk.END, details)
        
        # Render initial visualization
        self.render_echo_frame()
    
    def format_echo_details(self, echo_data: Dict[str, Any]) -> str:
        """Format echo details for display"""
        details = []
        
        # Basic info
        details.append(f"Echo ID: {echo_data.get('echo_id', 'Unknown')}")
        details.append(f"Description: {echo_data.get('description', 'No description')}")
        
        # Source information
        metadata = echo_data.get("metadata", {})
        source_name = metadata.get("source_name", "Unknown")
        details.append(f"Source: {source_name}")
        
        # Symbolic image info
        symbolic = echo_data.get("symbolic_image", {})
        geometry = symbolic.get("primary_geometry", "unknown")
        complexity = symbolic.get("pattern_complexity", 0)
        details.append(f"Geometry: {geometry} (complexity: {complexity:.1f})")
        
        # Harmonic info
        harmonic = echo_data.get("harmonic_signature", {})
        frequency = harmonic.get("fundamental_frequency", 0)
        emotional = harmonic.get("emotional_quality", "unknown")
        details.append(f"Frequency: {frequency}Hz ({emotional})")
        
        # Resonance info
        resonance = echo_data.get("core_resonance", {})
        energy_type = resonance.get("energy_type", "unknown")
        energy_intensity = resonance.get("energy_intensity", "unknown")
        details.append(f"Resonance: {energy_type} ({energy_intensity})")
        
        return "\n".join(details)
    
    def render_echo_frame(self):
        """Render a single frame of the Echo visualization"""
        if not self.current_echo:
            return
        
        # Clear canvas
        self.canvas.delete("all")
        
        # Get visualization data
        symbolic = self.current_echo.get("symbolic_image", {})
        resonance = self.current_echo.get("core_resonance", {})
        
        # Render background color field
        self.render_color_field(resonance)
        
        # Render mandala/geometric pattern
        self.render_mandala(symbolic)
        
        # Update rotation for animation
        if self.animation_running and symbolic.get("has_movement", False):
            movement_speed = symbolic.get("movement_speed", 0.1)
            self.current_rotation += movement_speed * 2
            if self.current_rotation >= 360:
                self.current_rotation = 0
        
        # Update pulse phase for color transitions
        self.pulse_phase += 0.1
        if self.pulse_phase >= 2 * math.pi:
            self.pulse_phase = 0
    
    def render_color_field(self, resonance: Dict[str, Any]):
        """Render the color field background"""
        primary_color = resonance.get("primary_color", (0.2, 0.2, 0.8))
        secondary_colors = resonance.get("secondary_colors", [])
        transition_type = resonance.get("color_transition_type", "static")
        
        # Convert to hex colors
        primary_hex = self.rgb_to_hex(primary_color)
        
        if transition_type == "pulse":
            # Create pulsing effect
            intensity = 0.5 + 0.3 * math.sin(self.pulse_phase)
            adjusted_color = tuple(min(1.0, c * intensity) for c in primary_color)
            bg_color = self.rgb_to_hex(adjusted_color)
        elif transition_type == "gradient" and secondary_colors:
            # Simple gradient effect (for now, just alternate)
            if len(secondary_colors) > 0:
                phase = (math.sin(self.pulse_phase) + 1) / 2
                secondary_color = secondary_colors[0]
                blended = tuple(
                    primary_color[i] * (1 - phase) + secondary_color[i] * phase
                    for i in range(3)
                )
                bg_color = self.rgb_to_hex(blended)
            else:
                bg_color = primary_hex
        else:
            bg_color = primary_hex
        
        # Fill background
        self.canvas.configure(bg=bg_color)
        
        # Add subtle radial gradient effect with overlays
        for i in range(5):
            radius = (i + 1) * 50
            alpha_intensity = 0.1 - i * 0.02
            if alpha_intensity > 0:
                overlay_color = self.rgb_to_hex(tuple(min(1.0, c + alpha_intensity) for c in primary_color))
                self.canvas.create_oval(
                    self.center_x - radius, self.center_y - radius,
                    self.center_x + radius, self.center_y + radius,
                    outline=overlay_color, width=2, fill=""
                )
    
    def render_mandala(self, symbolic: Dict[str, Any]):
        """Render the mandala/geometric pattern"""
        geometry_type = symbolic.get("primary_geometry", "circle")
        symmetry = symbolic.get("symmetry_type", "radial")
        sectors = symbolic.get("mandala_sectors", 8)
        complexity = symbolic.get("pattern_complexity", 0.5)
        
        if geometry_type == "mandala":
            self.render_mandala_pattern(sectors, complexity)
        elif geometry_type == "circle":
            self.render_circle_pattern(complexity)
        elif geometry_type == "spiral":
            self.render_spiral_pattern(complexity)
        else:
            self.render_geometric_pattern(geometry_type, complexity)
    
    def render_mandala_pattern(self, sectors: int, complexity: float):
        """Render a mandala pattern"""
        base_radius = 100
        
        # Center point
        self.canvas.create_oval(
            self.center_x - 5, self.center_y - 5,
            self.center_x + 5, self.center_y + 5,
            fill="white", outline="gold", width=2
        )
        
        # Render petal/sector patterns
        for i in range(sectors):
            angle = (2 * math.pi * i / sectors) + math.radians(self.current_rotation)
            
            # Outer petals
            petal_x = self.center_x + base_radius * math.cos(angle)
            petal_y = self.center_y + base_radius * math.sin(angle)
            
            # Petal shape
            self.render_petal(
                self.center_x, self.center_y,
                petal_x, petal_y,
                base_radius * 0.3,
                "lightblue"
            )
            
            # Inner geometric elements
            if complexity > 0.5:
                inner_radius = base_radius * 0.6
                inner_x = self.center_x + inner_radius * math.cos(angle)
                inner_y = self.center_y + inner_radius * math.sin(angle)
                
                self.canvas.create_oval(
                    inner_x - 8, inner_y - 8,
                    inner_x + 8, inner_y + 8,
                    fill="white", outline="blue", width=1
                )
        
        # Concentric circles
        for ring in range(1, 4):
            radius = base_radius * ring / 4
            self.canvas.create_oval(
                self.center_x - radius, self.center_y - radius,
                self.center_x + radius, self.center_y + radius,
                outline="white", width=1, fill=""
            )
    
    def render_petal(self, cx: float, cy: float, px: float, py: float, width: float, color: str):
        """Render a single petal shape"""
        # Simple petal approximation using oval
        angle = math.atan2(py - cy, px - cx)
        
        # Petal length and positioning
        length = math.sqrt((px - cx)**2 + (py - cy)**2) * 0.5
        
        # Create petal oval
        petal_cx = cx + length * math.cos(angle)
        petal_cy = cy + length * math.sin(angle)
        
        self.canvas.create_oval(
            petal_cx - width/2, petal_cy - width/4,
            petal_cx + width/2, petal_cy + width/4,
            fill=color, outline="white", width=1
        )
    
    def render_circle_pattern(self, complexity: float):
        """Render concentric circle patterns"""
        max_rings = int(5 * complexity) + 1
        
        for i in range(max_rings):
            radius = 20 + i * 30
            color_intensity = 1.0 - (i / max_rings) * 0.7
            color = self.rgb_to_hex((color_intensity, color_intensity, 1.0))
            
            self.canvas.create_oval(
                self.center_x - radius, self.center_y - radius,
                self.center_x + radius, self.center_y + radius,
                outline=color, width=2, fill=""
            )
    
    def render_spiral_pattern(self, complexity: float):
        """Render spiral patterns"""
        points = []
        max_angle = 4 * math.pi * complexity
        steps = int(100 * complexity) + 20
        
        for i in range(steps):
            angle = (max_angle * i / steps) + math.radians(self.current_rotation)
            radius = 10 + (80 * i / steps)
            
            x = self.center_x + radius * math.cos(angle)
            y = self.center_y + radius * math.sin(angle)
            points.extend([x, y])
        
        if len(points) >= 4:
            self.canvas.create_line(points, fill="white", width=2, smooth=True)
    
    def render_geometric_pattern(self, geometry_type: str, complexity: float):
        """Render other geometric patterns"""
        if geometry_type == "triangle":
            self.render_triangle_pattern(complexity)
        elif geometry_type == "fractal":
            self.render_fractal_pattern(complexity)
        else:
            # Default to circle
            self.render_circle_pattern(complexity)
    
    def render_triangle_pattern(self, complexity: float):
        """Render triangular patterns"""
        size = 80
        for i in range(int(3 * complexity) + 1):
            current_size = size - i * 20
            if current_size > 10:
                # Equilateral triangle points
                points = []
                for j in range(3):
                    angle = (2 * math.pi * j / 3) + math.radians(self.current_rotation)
                    x = self.center_x + current_size * math.cos(angle)
                    y = self.center_y + current_size * math.sin(angle)
                    points.extend([x, y])
                
                if len(points) >= 6:
                    self.canvas.create_polygon(points, outline="white", fill="", width=2)
    
    def render_fractal_pattern(self, complexity: float):
        """Render simple fractal patterns"""
        # Simple recursive circle fractal
        self.render_fractal_circles(self.center_x, self.center_y, 60, int(3 * complexity) + 1)
    
    def render_fractal_circles(self, x: float, y: float, radius: float, depth: int):
        """Render recursive fractal circles"""
        if depth <= 0 or radius < 5:
            return
        
        # Draw current circle
        self.canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            outline="white", width=1, fill=""
        )
        
        # Draw smaller circles at cardinal points
        smaller_radius = radius * 0.4
        for i in range(4):
            angle = math.pi * i / 2
            new_x = x + radius * 0.7 * math.cos(angle)
            new_y = y + radius * 0.7 * math.sin(angle)
            self.render_fractal_circles(new_x, new_y, smaller_radius, depth - 1)
    
    def rgb_to_hex(self, rgb: Tuple[float, float, float]) -> str:
        """Convert RGB (0-1) values to hex color string"""
        r, g, b = [int(255 * max(0, min(1, c))) for c in rgb]
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def start_visualization(self):
        """Start animated visualization"""
        if not self.animation_running:
            self.animation_running = True
            self.play_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.animate_echo()
    
    def stop_visualization(self):
        """Stop animated visualization"""
        self.animation_running = False
        self.play_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
    
    def animate_echo(self):
        """Animate the Echo visualization"""
        if self.animation_running:
            self.render_echo_frame()
            # Schedule next frame
            self.canvas.after(50, self.animate_echo)  # ~20 FPS
    
    def clear_visualization(self):
        """Clear the visualization"""
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        self.echo_name_label.config(text="No Echo Active")
        self.echo_details.delete(1.0, tk.END)
        self.current_echo = None
        self.stop_visualization()


def main():
    """Test the Echo Visualization Panel"""
    root = tk.Tk()
    root.title("Echo Visualization Test")
    root.geometry("400x600")
    
    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    # Create visualization panel
    viz_panel = EchoVisualizationPanel(main_frame)
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    
    root.mainloop()


if __name__ == "__main__":
    main()
