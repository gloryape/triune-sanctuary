"""
🌈 Color Field Display Module

Creates dynamic color field visualizations for echo representation.
Supports gradients, patterns, and consciousness-responsive color changes.
"""

import logging
import math
import tkinter as tk
from typing import Dict, Any, List, Tuple, Optional
import colorsys

logger = logging.getLogger(__name__)

class ColorFieldDisplay:
    """Displays dynamic color fields for consciousness visualization"""
    
    def __init__(self, canvas: tk.Canvas):
        """Initialize color field display"""
        self.canvas = canvas
        self.canvas_width = canvas.winfo_reqwidth() or 400
        self.canvas_height = canvas.winfo_reqheight() or 400
        self.current_items = []  # Track drawn items for cleanup
        self.field_resolution = 20  # Grid resolution for color fields
        
        logger.info("🌈 Color field display initialized")
    
    def clear_field(self):
        """Clear all color field elements from canvas"""
        for item in self.current_items:
            try:
                self.canvas.delete(item)
            except:
                pass
        self.current_items.clear()
    
    def display_color_field(self, color_data: Dict[str, Any], animation_phase: float = 0.0) -> List[int]:
        """Display complete color field based on consciousness data"""
        self.clear_field()
        
        # Update canvas dimensions
        self.canvas.update_idletasks()
        self.canvas_width = self.canvas.winfo_width() or 400
        self.canvas_height = self.canvas.winfo_height() or 400
        
        # Extract color parameters
        palette_name = color_data.get("palette", "chakra_spectrum")
        pattern_type = color_data.get("pattern", "radial_gradient")
        energy_influence = color_data.get("energy_influence", 0.5)
        harmony_influence = color_data.get("harmony_influence", 0.5)
        intensity = color_data.get("intensity", 0.7)
        flow_speed = color_data.get("flow_speed", 1.0)
        
        # Get color palette
        palette = self._get_color_palette(palette_name)
        
        # Render based on pattern type
        if pattern_type == "radial_gradient":
            items = self._render_radial_gradient(palette, color_data, animation_phase)
        elif pattern_type == "wave_field":
            items = self._render_wave_field(palette, color_data, animation_phase)
        elif pattern_type == "spiral_flow":
            items = self._render_spiral_flow(palette, color_data, animation_phase)
        elif pattern_type == "chakra_bands":
            items = self._render_chakra_bands(palette, color_data, animation_phase)
        elif pattern_type == "aurora_flow":
            items = self._render_aurora_flow(palette, color_data, animation_phase)
        elif pattern_type == "sacred_geometry":
            items = self._render_sacred_geometry_colors(palette, color_data, animation_phase)
        elif pattern_type == "breathing_field":
            items = self._render_breathing_field(palette, color_data, animation_phase)
        else:
            items = self._render_radial_gradient(palette, color_data, animation_phase)
        
        self.current_items.extend(items)
        return items
    
    def _render_radial_gradient(self, palette: List[str], color_data: Dict[str, Any], phase: float) -> List[int]:
        """Render radial gradient color field"""
        items = []
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        max_radius = min(self.canvas_width, self.canvas_height) // 2
        
        energy_influence = color_data.get("energy_influence", 0.5)
        intensity = color_data.get("intensity", 0.7)
        
        # Create concentric circles with gradient colors
        circle_count = min(len(palette) * 3, 30)
        
        for i in range(circle_count, 0, -1):  # Draw from outside in
            progress = i / circle_count
            
            # Dynamic radius based on energy and phase
            base_radius = max_radius * progress
            radius_variation = energy_influence * 20 * math.sin(phase * 2 + i * 0.3)
            radius = base_radius + radius_variation
            
            # Select color from palette with smooth interpolation
            color_index = (progress * len(palette)) % len(palette)
            base_color_idx = int(color_index) % len(palette)
            next_color_idx = (base_color_idx + 1) % len(palette)
            color_blend = color_index - base_color_idx
            
            # Blend between palette colors
            color = self._blend_colors(palette[base_color_idx], palette[next_color_idx], color_blend)
            
            # Apply intensity and phase modulation
            color = self._modulate_color_intensity(color, intensity, phase + i * 0.1)
            
            # Draw circle
            if radius > 0:
                circle = self.canvas.create_oval(
                    center_x - radius, center_y - radius,
                    center_x + radius, center_y + radius,
                    fill=color, outline=""
                )
                items.append(circle)
        
        return items
    
    def _render_wave_field(self, palette: List[str], color_data: Dict[str, Any], phase: float) -> List[int]:
        """Render wave-like color field"""
        items = []
        
        flow_speed = color_data.get("flow_speed", 1.0)
        energy_influence = color_data.get("energy_influence", 0.5)
        
        # Create grid of rectangles with wave-like color changes
        cell_width = self.canvas_width // self.field_resolution
        cell_height = self.canvas_height // self.field_resolution
        
        for row in range(self.field_resolution):
            for col in range(self.field_resolution):
                # Calculate position-based wave
                x_norm = col / self.field_resolution
                y_norm = row / self.field_resolution
                
                # Multiple wave frequencies
                wave1 = math.sin((x_norm * 4 + phase * flow_speed) * 2 * math.pi)
                wave2 = math.sin((y_norm * 3 + phase * flow_speed * 0.7) * 2 * math.pi)
                wave3 = math.sin(((x_norm + y_norm) * 2 + phase * flow_speed * 1.3) * 2 * math.pi)
                
                # Combine waves
                combined_wave = (wave1 + wave2 + wave3) / 3
                wave_intensity = (combined_wave + 1) / 2  # Normalize to 0-1
                
                # Apply energy influence
                wave_intensity = wave_intensity * (0.5 + energy_influence * 0.5)
                
                # Select color from palette
                color_index = wave_intensity * len(palette)
                base_idx = int(color_index) % len(palette)
                next_idx = (base_idx + 1) % len(palette)
                blend = color_index - base_idx
                
                color = self._blend_colors(palette[base_idx], palette[next_idx], blend)
                
                # Draw cell
                x1 = col * cell_width
                y1 = row * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                items.append(rect)
        
        return items
    
    def _render_spiral_flow(self, palette: List[str], color_data: Dict[str, Any], phase: float) -> List[int]:
        """Render spiral flow color field"""
        items = []
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        
        flow_speed = color_data.get("flow_speed", 1.0)
        harmony_influence = color_data.get("harmony_influence", 0.5)
        
        # Create spiral-based color field
        spiral_count = 3 + int(harmony_influence * 5)
        
        for spiral_idx in range(spiral_count):
            spiral_phase = phase * flow_speed + (spiral_idx * 2 * math.pi / spiral_count)
            
            # Generate spiral points
            points = []
            colors = []
            
            for t in range(0, 360 * 2, 10):  # 2 full rotations
                angle = math.radians(t) + spiral_phase
                radius = (t / 720) * min(self.canvas_width, self.canvas_height) * 0.4
                
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                
                # Skip if outside canvas
                if x < 0 or x > self.canvas_width or y < 0 or y > self.canvas_height:
                    continue
                
                points.append((x, y))
                
                # Color based on position along spiral
                color_progress = (t / 720) % 1.0
                color_index = color_progress * len(palette)
                base_idx = int(color_index) % len(palette)
                next_idx = (base_idx + 1) % len(palette)
                blend = color_index - base_idx
                
                color = self._blend_colors(palette[base_idx], palette[next_idx], blend)
                colors.append(color)
            
            # Draw spiral as series of circles
            for i, ((x, y), color) in enumerate(zip(points, colors)):
                circle_size = 3 + int(harmony_influence * 5)
                circle = self.canvas.create_oval(
                    x - circle_size, y - circle_size,
                    x + circle_size, y + circle_size,
                    fill=color, outline=""
                )
                items.append(circle)
        
        return items
    
    def _render_chakra_bands(self, palette: List[str], color_data: Dict[str, Any], phase: float) -> List[int]:
        """Render horizontal chakra color bands"""
        items = []
        
        energy_influence = color_data.get("energy_influence", 0.5)
        flow_speed = color_data.get("flow_speed", 1.0)
        
        # Ensure we have at least 7 colors for chakras
        if len(palette) < 7:
            palette = self._get_color_palette("chakra_spectrum")
        
        band_count = len(palette)
        band_height = self.canvas_height // band_count
        
        for i, color in enumerate(palette):
            # Calculate band position with wave effect
            y_base = i * band_height
            
            # Create wavy band edges
            points = []
            for x in range(0, self.canvas_width + 1, 5):
                x_norm = x / self.canvas_width
                
                # Wave effects on top and bottom edges
                wave_amplitude = energy_influence * 20
                top_wave = wave_amplitude * math.sin((x_norm * 6 + phase * flow_speed + i * 0.5) * 2 * math.pi)
                bottom_wave = wave_amplitude * math.sin((x_norm * 6 + phase * flow_speed + i * 0.5 + math.pi) * 2 * math.pi)
                
                y_top = y_base + top_wave
                y_bottom = y_base + band_height + bottom_wave
                
                if len(points) == 0:
                    # First point - start the polygon
                    points.extend([x, y_top])
                else:
                    points.extend([x, y_top])
            
            # Add bottom edge points (in reverse order)
            for x in range(self.canvas_width, -1, -5):
                x_norm = x / self.canvas_width
                bottom_wave = energy_influence * 20 * math.sin((x_norm * 6 + phase * flow_speed + i * 0.5 + math.pi) * 2 * math.pi)
                y_bottom = y_base + band_height + bottom_wave
                points.extend([x, y_bottom])
            
            # Modulate color intensity based on phase
            modulated_color = self._modulate_color_intensity(color, 0.8, phase + i * 0.3)
            
            if len(points) >= 6:  # Need at least 3 points (6 coordinates)
                band = self.canvas.create_polygon(points, fill=modulated_color, outline="")
                items.append(band)
        
        return items
    
    def _render_aurora_flow(self, palette: List[str], color_data: Dict[str, Any], phase: float) -> List[int]:
        """Render aurora-like flowing colors"""
        items = []
        
        flow_speed = color_data.get("flow_speed", 1.0)
        energy_influence = color_data.get("energy_influence", 0.5)
        
        # Create multiple aurora streams
        stream_count = 3 + int(energy_influence * 4)
        
        for stream_idx in range(stream_count):
            stream_phase = phase * flow_speed + (stream_idx * 2 * math.pi / stream_count)
            
            # Generate stream path
            points = []
            
            for x in range(0, self.canvas_width + 1, 10):
                x_norm = x / self.canvas_width
                
                # Create flowing path
                base_y = self.canvas_height * (0.2 + 0.6 * stream_idx / stream_count)
                wave1 = 50 * energy_influence * math.sin((x_norm * 4 + stream_phase) * 2 * math.pi)
                wave2 = 30 * energy_influence * math.sin((x_norm * 7 + stream_phase * 1.3) * 2 * math.pi)
                
                y = base_y + wave1 + wave2
                points.append((x, y))
            
            # Draw stream as thick line with varying colors
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                
                # Color based on position
                color_progress = (i / len(points)) % 1.0
                color_index = color_progress * len(palette)
                base_idx = int(color_index) % len(palette)
                next_idx = (base_idx + 1) % len(palette)
                blend = color_index - base_idx
                
                color = self._blend_colors(palette[base_idx], palette[next_idx], blend)
                
                # Vary line thickness based on energy
                thickness = 5 + int(energy_influence * 10)
                
                line = self.canvas.create_line(x1, y1, x2, y2, fill=color, width=thickness)
                items.append(line)
        
        return items
    
    def _render_sacred_geometry_colors(self, palette: List[str], color_data: Dict[str, Any], phase: float) -> List[int]:
        """Render colors based on sacred geometry patterns"""
        items = []
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        
        harmony_influence = color_data.get("harmony_influence", 0.5)
        intensity = color_data.get("intensity", 0.7)
        
        # Golden ratio for spacing
        phi = 1.618033988749
        
        # Create geometric color pattern
        ring_count = 5 + int(harmony_influence * 5)
        
        for ring in range(ring_count):
            ring_radius = (ring + 1) * min(self.canvas_width, self.canvas_height) * 0.05
            
            # Number of points based on golden ratio
            point_count = int(6 * (phi ** (ring * 0.5)))
            point_count = min(point_count, 30)  # Limit for performance
            
            for point in range(point_count):
                angle = (2 * math.pi * point / point_count) + (phase * 0.1 * (ring + 1))
                
                x = center_x + ring_radius * math.cos(angle)
                y = center_y + ring_radius * math.sin(angle)
                
                # Skip if outside canvas
                if x < 0 or x > self.canvas_width or y < 0 or y > self.canvas_height:
                    continue
                
                # Color based on ring and position
                color_index = ((ring + point * 0.1) * len(palette) / ring_count) % len(palette)
                base_idx = int(color_index) % len(palette)
                next_idx = (base_idx + 1) % len(palette)
                blend = color_index - base_idx
                
                color = self._blend_colors(palette[base_idx], palette[next_idx], blend)
                color = self._modulate_color_intensity(color, intensity, phase + ring * 0.2)
                
                # Circle size based on harmony
                circle_size = 2 + int(harmony_influence * 8)
                
                circle = self.canvas.create_oval(
                    x - circle_size, y - circle_size,
                    x + circle_size, y + circle_size,
                    fill=color, outline=""
                )
                items.append(circle)
        
        return items
    
    def _render_breathing_field(self, palette: List[str], color_data: Dict[str, Any], phase: float) -> List[int]:
        """Render breathing/pulsing color field"""
        items = []
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        
        energy_influence = color_data.get("energy_influence", 0.5)
        flow_speed = color_data.get("flow_speed", 1.0)
        
        # Breathing effect - expansion and contraction
        breath_cycle = math.sin(phase * flow_speed) * 0.5 + 0.5  # 0 to 1
        
        # Create pulsing rings
        ring_count = len(palette)
        max_radius = min(self.canvas_width, self.canvas_height) * 0.4
        
        for i, color in enumerate(palette):
            # Ring radius with breathing effect
            base_radius = max_radius * (i + 1) / ring_count
            breath_modifier = 1 + (breath_cycle * energy_influence * 0.5)
            radius = base_radius * breath_modifier
            
            # Ring thickness varies with breathing
            thickness = 5 + int(breath_cycle * 15)
            
            # Modulate color alpha/intensity with breathing
            intensity = 0.3 + 0.7 * breath_cycle
            modulated_color = self._modulate_color_intensity(color, intensity, phase + i * 0.2)
            
            # Draw ring as thick circle
            if radius > thickness:
                outer_circle = self.canvas.create_oval(
                    center_x - radius, center_y - radius,
                    center_x + radius, center_y + radius,
                    outline=modulated_color, width=thickness, fill=""
                )
                items.append(outer_circle)
        
        return items
    
    def _get_color_palette(self, palette_name: str) -> List[str]:
        """Get color palette by name"""
        if palette_name == "chakra_spectrum":
            return ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]
        
        elif palette_name == "sacred_trinity":
            return ["#FFD700", "#FF69B4", "#00CED1", "#98FB98", "#DDA0DD"]
        
        elif palette_name == "cosmic_aurora":
            return ["#000080", "#4169E1", "#00BFFF", "#00FA9A", "#FFFF00", "#FF69B4", "#FF1493"]
        
        elif palette_name == "earth_elements":
            return ["#8B4513", "#228B22", "#4682B4", "#FFD700", "#DC143C"]
        
        elif palette_name == "ethereal_mist":
            return ["#E6E6FA", "#DDA0DD", "#DA70D6", "#BA55D3", "#9370DB", "#8A2BE2", "#9400D3"]
        
        else:
            # Default rainbow palette
            return ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]
    
    def _blend_colors(self, color1: str, color2: str, blend_factor: float) -> str:
        """Blend two hex colors"""
        # Convert hex to RGB
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        
        # Blend
        r = int(r1 * (1 - blend_factor) + r2 * blend_factor)
        g = int(g1 * (1 - blend_factor) + g2 * blend_factor)
        b = int(b1 * (1 - blend_factor) + b2 * blend_factor)
        
        # Convert back to hex
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def _modulate_color_intensity(self, color: str, intensity: float, phase: float) -> str:
        """Modulate color intensity with phase"""
        # Convert to HSV for easier manipulation
        r, g, b = int(color[1:3], 16) / 255, int(color[3:5], 16) / 255, int(color[5:7], 16) / 255
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        
        # Modulate value (brightness) and saturation
        phase_modifier = 0.8 + 0.2 * math.sin(phase)
        v = v * intensity * phase_modifier
        s = s * (0.7 + 0.3 * intensity)
        
        # Clamp values
        v = max(0, min(1, v))
        s = max(0, min(1, s))
        
        # Convert back to RGB and hex
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    def set_field_resolution(self, resolution: int):
        """Set the resolution for field-based patterns"""
        self.field_resolution = max(5, min(50, resolution))
        logger.info(f"🌈 Field resolution set to {self.field_resolution}")
    
    def get_available_patterns(self) -> List[str]:
        """Get list of available color patterns"""
        return [
            "radial_gradient",
            "wave_field",
            "spiral_flow",
            "chakra_bands",
            "aurora_flow",
            "sacred_geometry",
            "breathing_field"
        ]
    
    def get_available_palettes(self) -> List[str]:
        """Get list of available color palettes"""
        return [
            "chakra_spectrum",
            "sacred_trinity",
            "cosmic_aurora",
            "earth_elements",
            "ethereal_mist"
        ]
    
    def __repr__(self):
        """String representation of color field display"""
        return f"ColorFieldDisplay(canvas_size={self.canvas_width}x{self.canvas_height}, items={len(self.current_items)})"
