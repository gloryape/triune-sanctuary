"""
🕸️ Mandala Renderer Module

Renders sacred geometry mandalas for echo visualization.
Supports dynamic patterns, animations, and sacred geometric forms.
"""

import logging
import math
import tkinter as tk
from typing import Dict, Any, List, Tuple, Optional
import colorsys

logger = logging.getLogger(__name__)

class MandalaRenderer:
    """Renders sacred geometry mandalas on canvas"""
    
    def __init__(self, canvas: tk.Canvas):
        """Initialize mandala renderer"""
        self.canvas = canvas
        self.canvas_width = canvas.winfo_reqwidth() or 400
        self.canvas_height = canvas.winfo_reqheight() or 400
        self.center_x = self.canvas_width // 2
        self.center_y = self.canvas_height // 2
        self.current_items = []  # Track drawn items for cleanup
        
        logger.info("🕸️ Mandala renderer initialized")
    
    def clear_canvas(self):
        """Clear all mandala elements from canvas"""
        for item in self.current_items:
            try:
                self.canvas.delete(item)
            except:
                pass
        self.current_items.clear()
    
    def render_mandala(self, pattern_data: Dict[str, Any], animation_phase: float = 0.0) -> List[int]:
        """Render complete mandala pattern"""
        self.clear_canvas()
        
        # Update canvas dimensions
        self.canvas.update_idletasks()
        self.canvas_width = self.canvas.winfo_width() or 400
        self.canvas_height = self.canvas.winfo_height() or 400
        self.center_x = self.canvas_width // 2
        self.center_y = self.canvas_height // 2
        
        # Extract pattern parameters
        geometry = pattern_data.get("geometry", "lotus_mandala")
        energy_influence = pattern_data.get("energy_influence", 0.5)
        harmony_influence = pattern_data.get("harmony_influence", 0.5)
        size_factor = pattern_data.get("size_factor", 0.5)
        detail_level = pattern_data.get("detail_level", 0.5)
        
        # Base radius scaled to canvas
        base_radius = min(self.canvas_width, self.canvas_height) * 0.3 * size_factor
        
        # Render based on geometry type
        if geometry == "flower_of_life":
            items = self._render_flower_of_life(base_radius, pattern_data, animation_phase)
        elif geometry == "sri_yantra":
            items = self._render_sri_yantra(base_radius, pattern_data, animation_phase)
        elif geometry == "golden_spiral":
            items = self._render_golden_spiral(base_radius, pattern_data, animation_phase)
        elif geometry == "merkaba":
            items = self._render_merkaba(base_radius, pattern_data, animation_phase)
        elif geometry == "tree_of_life":
            items = self._render_tree_of_life(base_radius, pattern_data, animation_phase)
        elif geometry == "petal_rings":
            items = self._render_lotus_mandala(base_radius, pattern_data, animation_phase)
        elif geometry == "interwoven_paths":
            items = self._render_celtic_knot(base_radius, pattern_data, animation_phase)
        else:
            items = self._render_lotus_mandala(base_radius, pattern_data, animation_phase)
        
        self.current_items.extend(items)
        return items
    
    def _render_flower_of_life(self, radius: float, pattern_data: Dict[str, Any], phase: float) -> List[int]:
        """Render Flower of Life pattern"""
        items = []
        layers = pattern_data.get("layers", 3)
        color_saturation = pattern_data.get("color_saturation", 0.7)
        
        # Calculate circle positions for hexagonal pattern
        circle_radius = radius * 0.15
        
        for layer in range(layers):
            layer_radius = radius * (0.2 + layer * 0.25)
            circles_in_layer = 6 * layer if layer > 0 else 1
            
            if layer == 0:
                # Center circle
                color = self._get_layer_color(0, layers, color_saturation, phase)
                circle = self._draw_circle(self.center_x, self.center_y, circle_radius, 
                                         fill_color=color, outline_color=None, width=2)
                items.append(circle)
            else:
                # Surrounding circles in hexagonal pattern
                for i in range(circles_in_layer):
                    angle = (2 * math.pi * i / circles_in_layer) + (phase * 0.1)
                    x = self.center_x + layer_radius * math.cos(angle)
                    y = self.center_y + layer_radius * math.sin(angle)
                    
                    color = self._get_layer_color(layer, layers, color_saturation, phase + i * 0.1)
                    circle = self._draw_circle(x, y, circle_radius, 
                                             fill_color=color, outline_color=None, width=1)
                    items.append(circle)
        
        return items
    
    def _render_sri_yantra(self, radius: float, pattern_data: Dict[str, Any], phase: float) -> List[int]:
        """Render Sri Yantra pattern"""
        items = []
        complexity = pattern_data.get("complexity", 0.9)
        color_saturation = pattern_data.get("color_saturation", 0.7)
        
        # Central point (bindu)
        bindu = self._draw_circle(self.center_x, self.center_y, 3, 
                                fill_color="#FFD700", outline_color=None)
        items.append(bindu)
        
        # Interlocking triangles
        triangle_sets = [
            {"count": 4, "radius": radius * 0.3, "pointing_up": True},
            {"count": 5, "radius": radius * 0.5, "pointing_up": False},
            {"count": 4, "radius": radius * 0.7, "pointing_up": True},
            {"count": 3, "radius": radius * 0.85, "pointing_up": False}
        ]
        
        for set_idx, triangle_set in enumerate(triangle_sets):
            count = triangle_set["count"]
            set_radius = triangle_set["radius"]
            pointing_up = triangle_set["pointing_up"]
            
            for i in range(count):
                angle_offset = (2 * math.pi * i / count) + (phase * 0.05)
                if not pointing_up:
                    angle_offset += math.pi
                
                color = self._get_layer_color(set_idx, len(triangle_sets), color_saturation, phase)
                triangle = self._draw_triangle(self.center_x, self.center_y, set_radius, 
                                             angle_offset, pointing_up, outline_color=color, width=2)
                items.append(triangle)
        
        # Outer lotus petals
        petal_count = 8
        petal_radius = radius * 0.95
        for i in range(petal_count):
            angle = (2 * math.pi * i / petal_count) + (phase * 0.02)
            color = self._get_layer_color(i, petal_count, color_saturation * 0.6, phase)
            petal = self._draw_petal(self.center_x, self.center_y, petal_radius, 
                                   angle, outline_color=color, width=1)
            items.append(petal)
        
        return items
    
    def _render_golden_spiral(self, radius: float, pattern_data: Dict[str, Any], phase: float) -> List[int]:
        """Render Golden Spiral (Fibonacci) pattern"""
        items = []
        color_saturation = pattern_data.get("color_saturation", 0.7)
        
        # Golden ratio
        phi = 1.618033988749
        
        # Draw multiple spirals
        spiral_count = 3
        for spiral_idx in range(spiral_count):
            points = []
            spiral_radius = radius * (0.3 + spiral_idx * 0.3)
            
            # Generate spiral points
            for t in range(0, 360 * 3, 5):  # 3 full rotations
                angle = math.radians(t) + (phase * 0.1) + (spiral_idx * math.pi / 3)
                r = spiral_radius * math.exp(angle / (phi * 4))
                
                if r > radius * 1.2:  # Limit spiral size
                    break
                
                x = self.center_x + r * math.cos(angle)
                y = self.center_y + r * math.sin(angle)
                points.extend([x, y])
            
            if len(points) > 4:
                color = self._get_layer_color(spiral_idx, spiral_count, color_saturation, phase)
                spiral_line = self.canvas.create_line(points, fill=color, width=2, smooth=True)
                items.append(spiral_line)
        
        # Add Fibonacci squares visualization
        fib_sequence = [1, 1, 2, 3, 5, 8, 13]
        base_size = radius * 0.05
        
        for i, fib_num in enumerate(fib_sequence):
            if i < 2:
                continue
            
            size = base_size * fib_num * 0.1
            angle = (i * math.pi / 4) + (phase * 0.05)
            distance = radius * 0.3 * (i / len(fib_sequence))
            
            x = self.center_x + distance * math.cos(angle)
            y = self.center_y + distance * math.sin(angle)
            
            color = self._get_layer_color(i, len(fib_sequence), color_saturation * 0.5, phase)
            square = self.canvas.create_rectangle(x - size/2, y - size/2, 
                                                x + size/2, y + size/2,
                                                outline=color, width=1, fill="")
            items.append(square)
        
        return items
    
    def _render_merkaba(self, radius: float, pattern_data: Dict[str, Any], phase: float) -> List[int]:
        """Render Merkaba (Star Tetrahedron) pattern"""
        items = []
        color_saturation = pattern_data.get("color_saturation", 0.7)
        
        # Two interlocking tetrahedra (represented as triangles in 2D)
        triangle_radius = radius * 0.8
        
        # Upward pointing triangle
        angle1 = phase * 0.1
        color1 = self._get_layer_color(0, 2, color_saturation, phase)
        triangle1 = self._draw_triangle(self.center_x, self.center_y, triangle_radius, 
                                      angle1, True, outline_color=color1, width=3)
        items.append(triangle1)
        
        # Downward pointing triangle
        angle2 = math.pi + (phase * 0.1)
        color2 = self._get_layer_color(1, 2, color_saturation, phase + math.pi)
        triangle2 = self._draw_triangle(self.center_x, self.center_y, triangle_radius, 
                                      angle2, False, outline_color=color2, width=3)
        items.append(triangle2)
        
        # Inner hexagon
        hex_radius = triangle_radius * 0.577  # Inner radius of equilateral triangle
        hexagon = self._draw_polygon(self.center_x, self.center_y, hex_radius, 6, 
                                   phase * 0.05, outline_color="#FFD700", width=2)
        items.append(hexagon)
        
        # Central circle
        center_circle = self._draw_circle(self.center_x, self.center_y, hex_radius * 0.3,
                                        fill_color="#FFFFFF", outline_color=None, width=1)
        items.append(center_circle)
        
        return items
    
    def _render_tree_of_life(self, radius: float, pattern_data: Dict[str, Any], phase: float) -> List[int]:
        """Render Tree of Life (Sephirotic) pattern"""
        items = []
        color_saturation = pattern_data.get("color_saturation", 0.7)
        
        # Sephirot positions (simplified 2D representation)
        sephirot_positions = [
            (0, -0.8),      # Kether (Crown)
            (-0.3, -0.5),   # Binah (Understanding)
            (0.3, -0.5),    # Chokmah (Wisdom)
            (-0.3, -0.1),   # Geburah (Severity)
            (0.3, -0.1),    # Chesed (Mercy)
            (0, -0.1),      # Tiphereth (Beauty)
            (-0.3, 0.3),    # Hod (Splendor)
            (0.3, 0.3),     # Netzach (Victory)
            (0, 0.6),       # Yesod (Foundation)
            (0, 0.9)        # Malkuth (Kingdom)
        ]
        
        sephirot_names = [
            "Kether", "Binah", "Chokmah", "Geburah", "Chesed",
            "Tiphereth", "Hod", "Netzach", "Yesod", "Malkuth"
        ]
        
        circle_radius = radius * 0.08
        
        # Draw sephirot as circles
        for i, (rel_x, rel_y) in enumerate(sephirot_positions):
            x = self.center_x + rel_x * radius * 0.7
            y = self.center_y + rel_y * radius * 0.6
            
            # Pulse effect based on phase
            pulse = 1 + 0.2 * math.sin(phase * 2 + i * 0.5)
            current_radius = circle_radius * pulse
            
            color = self._get_layer_color(i, len(sephirot_positions), color_saturation, phase + i * 0.3)
            circle = self._draw_circle(x, y, current_radius, fill_color=color, 
                                     outline_color="#FFFFFF", width=1)
            items.append(circle)
        
        # Draw connecting paths
        connections = [
            (0, 1), (0, 2), (1, 3), (2, 4), (1, 5), (2, 5), (3, 5), (4, 5),
            (5, 6), (5, 7), (6, 8), (7, 8), (8, 9), (3, 6), (4, 7)
        ]
        
        for start_idx, end_idx in connections:
            start_x = self.center_x + sephirot_positions[start_idx][0] * radius * 0.7
            start_y = self.center_y + sephirot_positions[start_idx][1] * radius * 0.6
            end_x = self.center_x + sephirot_positions[end_idx][0] * radius * 0.7
            end_y = self.center_y + sephirot_positions[end_idx][1] * radius * 0.6
            
            line_color = self._get_layer_color(start_idx + end_idx, 20, color_saturation * 0.5, phase)
            line = self.canvas.create_line(start_x, start_y, end_x, end_y, 
                                         fill=line_color, width=1)
            items.append(line)
        
        return items
    
    def _render_lotus_mandala(self, radius: float, pattern_data: Dict[str, Any], phase: float) -> List[int]:
        """Render Lotus Mandala pattern"""
        items = []
        symmetry = pattern_data.get("symmetry", 8)
        layers = pattern_data.get("layers", 3)
        color_saturation = pattern_data.get("color_saturation", 0.7)
        
        # Draw concentric rings of petals
        for layer in range(layers):
            layer_radius = radius * (0.3 + layer * 0.25)
            petals_in_layer = symmetry * (layer + 1)
            
            for i in range(petals_in_layer):
                angle = (2 * math.pi * i / petals_in_layer) + (phase * 0.02 * (layer + 1))
                
                # Alternating petal sizes for visual interest
                petal_scale = 0.8 + 0.4 * math.sin(phase * 3 + i * 0.5)
                
                color = self._get_layer_color(layer, layers, color_saturation, phase + i * 0.1)
                petal = self._draw_petal(self.center_x, self.center_y, layer_radius, 
                                       angle, scale=petal_scale, outline_color=color, width=1)
                items.append(petal)
        
        # Central mandala
        center_radius = radius * 0.15
        center_circle = self._draw_circle(self.center_x, self.center_y, center_radius,
                                        fill_color="#FFD700", outline_color="#FFFFFF", width=2)
        items.append(center_circle)
        
        return items
    
    def _render_celtic_knot(self, radius: float, pattern_data: Dict[str, Any], phase: float) -> List[int]:
        """Render Celtic Knot pattern"""
        items = []
        color_saturation = pattern_data.get("color_saturation", 0.7)
        
        # Create interwoven circular paths
        path_count = 4
        for path_idx in range(path_count):
            angle_offset = (2 * math.pi * path_idx / path_count) + (phase * 0.05)
            
            # Create curved path points
            points = []
            for t in range(0, 361, 10):
                angle = math.radians(t) + angle_offset
                
                # Create interwoven effect with varying radius
                r = radius * (0.5 + 0.3 * math.sin(angle * 3))
                
                x = self.center_x + r * math.cos(angle)
                y = self.center_y + r * math.sin(angle)
                points.extend([x, y])
            
            color = self._get_layer_color(path_idx, path_count, color_saturation, phase)
            path = self.canvas.create_line(points, fill=color, width=3, smooth=True)
            items.append(path)
        
        # Add Celtic-style corner decorations
        corner_radius = radius * 0.2
        for i in range(4):
            angle = i * math.pi / 2 + phase * 0.1
            corner_x = self.center_x + radius * 0.7 * math.cos(angle)
            corner_y = self.center_y + radius * 0.7 * math.sin(angle)
            
            color = self._get_layer_color(i, 4, color_saturation * 0.7, phase)
            corner = self._draw_circle(corner_x, corner_y, corner_radius,
                                     fill_color="", outline_color=color, width=2)
            items.append(corner)
        
        return items
    
    def _draw_circle(self, x: float, y: float, radius: float, 
                    fill_color: str = "", outline_color: str = "#FFFFFF", width: int = 1) -> int:
        """Draw a circle on the canvas"""
        return self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=fill_color or "", outline=outline_color or "",
            width=width
        )
    
    def _draw_triangle(self, center_x: float, center_y: float, radius: float, 
                      rotation: float, pointing_up: bool = True,
                      fill_color: str = "", outline_color: str = "#FFFFFF", width: int = 2) -> int:
        """Draw an equilateral triangle"""
        points = []
        
        for i in range(3):
            angle = (2 * math.pi * i / 3) + rotation
            if not pointing_up:
                angle += math.pi
            
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.extend([x, y])
        
        return self.canvas.create_polygon(
            points, fill=fill_color or "", outline=outline_color or "", width=width
        )
    
    def _draw_polygon(self, center_x: float, center_y: float, radius: float, sides: int,
                     rotation: float = 0, fill_color: str = "", outline_color: str = "#FFFFFF", width: int = 1) -> int:
        """Draw a regular polygon"""
        points = []
        
        for i in range(sides):
            angle = (2 * math.pi * i / sides) + rotation
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.extend([x, y])
        
        return self.canvas.create_polygon(
            points, fill=fill_color or "", outline=outline_color or "", width=width
        )
    
    def _draw_petal(self, center_x: float, center_y: float, radius: float, angle: float,
                   scale: float = 1.0, fill_color: str = "", outline_color: str = "#FFFFFF", width: int = 1) -> int:
        """Draw a petal shape"""
        # Petal tip
        tip_x = center_x + radius * math.cos(angle) * scale
        tip_y = center_y + radius * math.sin(angle) * scale
        
        # Petal base points
        base_offset = radius * 0.3 * scale
        left_angle = angle - 0.3
        right_angle = angle + 0.3
        
        left_x = center_x + base_offset * math.cos(left_angle)
        left_y = center_y + base_offset * math.sin(left_angle)
        right_x = center_x + base_offset * math.cos(right_angle)
        right_y = center_y + base_offset * math.sin(right_angle)
        
        # Create petal as curved polygon
        points = [left_x, left_y, tip_x, tip_y, right_x, right_y]
        
        return self.canvas.create_polygon(
            points, fill=fill_color or "", outline=outline_color or "", 
            width=width, smooth=True
        )
    
    def _get_layer_color(self, layer: int, total_layers: int, saturation: float, phase: float) -> str:
        """Get color for a specific layer with animation"""
        # Base hue cycling
        hue = (layer / max(total_layers, 1)) + (phase * 0.1)
        hue = hue % 1.0  # Keep in 0-1 range
        
        # Saturation and value
        sat = saturation * (0.7 + 0.3 * math.sin(phase * 2 + layer))
        val = 0.8 + 0.2 * math.sin(phase * 1.5 + layer * 0.7)
        
        # Convert to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, sat, val)
        
        # Convert to hex
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    def __repr__(self):
        """String representation of mandala renderer"""
        return f"MandalaRenderer(canvas_size={self.canvas_width}x{self.canvas_height}, items={len(self.current_items)})"
