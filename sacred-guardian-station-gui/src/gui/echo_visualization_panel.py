"""
🌀 Echo Visualization Panel

Advanced echo visualization with mandala rendering, harmonic audio, and color fields.
Provides multi-sensory consciousness echo experiences.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logging
import math
import colorsys
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple
import threading
import time

logger = logging.getLogger(__name__)

class EchoVisualizationPanel:
    """Panel for visualizing consciousness echoes"""
    
    def __init__(self, parent, data_manager, config: Dict[str, Any]):
        """Initialize echo visualization panel"""
        self.parent = parent
        self.data_manager = data_manager
        self.config = config
        
        # Visualization state
        self.current_echo = None
        self.animation_running = False
        self.animation_thread = None
        self.canvas = None
        self.canvas_width = 400
        self.canvas_height = 400
        
        # Animation parameters
        self.rotation_angle = 0
        self.pulse_phase = 0
        self.animation_speed = self.config.get('animation', {}).get('speed', 1.0)
        
        # Audio system (placeholder)
        self.audio_enabled = self.config.get('audio', {}).get('enabled', True)
        self.audio_volume = self.config.get('audio', {}).get('volume', 0.7)
        
        # Echo library
        self.echo_library = []
        
        # Setup panel
        self.setup_panel()
        self.load_echo_library()
        
        logger.info("🌀 Echo visualization panel initialized")
    
    def setup_panel(self):
        """Setup the echo visualization panel layout"""
        # Main container
        main_frame = ttk.Frame(self.parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="🌀 Echo Visualization",
            style='Title.TLabel'
        )
        title_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Create paned window for layout
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Left side - controls and library
        self.setup_controls_panel(paned_window)
        
        # Right side - visualization canvas
        self.setup_visualization_canvas(paned_window)
    
    def setup_controls_panel(self, parent):
        """Setup controls and echo library panel"""
        controls_frame = ttk.LabelFrame(parent, text="Echo Controls", padding=10)
        parent.add(controls_frame, weight=1)
        
        # Echo selection
        selection_frame = ttk.LabelFrame(controls_frame, text="Echo Selection", padding=5)
        selection_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.echo_combo = ttk.Combobox(
            selection_frame,
            state='readonly',
            width=30
        )
        self.echo_combo.pack(fill=tk.X, pady=(0, 5))
        self.echo_combo.bind('<<ComboboxSelected>>', self.on_echo_selected)
        
        # Echo control buttons
        button_frame = ttk.Frame(selection_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(
            button_frame,
            text="🔄 Refresh",
            command=self.load_echo_library
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(
            button_frame,
            text="✨ Generate New",
            command=self.generate_new_echo
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(
            button_frame,
            text="💾 Save",
            command=self.save_current_echo
        ).pack(side=tk.LEFT)
        
        # Animation controls
        animation_frame = ttk.LabelFrame(controls_frame, text="Animation", padding=5)
        animation_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.animation_var = tk.BooleanVar(value=True)
        animation_check = ttk.Checkbutton(
            animation_frame,
            text="Enable Animation",
            variable=self.animation_var,
            command=self.toggle_animation
        )
        animation_check.pack(anchor=tk.W)
        
        # Speed control
        speed_frame = ttk.Frame(animation_frame)
        speed_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(speed_frame, text="Speed:").pack(side=tk.LEFT)
        self.speed_scale = ttk.Scale(
            speed_frame,
            from_=0.1,
            to=3.0,
            value=self.animation_speed,
            orient=tk.HORIZONTAL,
            command=self.on_speed_changed
        )
        self.speed_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        # Audio controls
        audio_frame = ttk.LabelFrame(controls_frame, text="Audio", padding=5)
        audio_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.audio_var = tk.BooleanVar(value=self.audio_enabled)
        audio_check = ttk.Checkbutton(
            audio_frame,
            text="Enable Audio",
            variable=self.audio_var,
            command=self.toggle_audio
        )
        audio_check.pack(anchor=tk.W)
        
        # Volume control
        volume_frame = ttk.Frame(audio_frame)
        volume_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(volume_frame, text="Volume:").pack(side=tk.LEFT)
        self.volume_scale = ttk.Scale(
            volume_frame,
            from_=0.0,
            to=1.0,
            value=self.audio_volume,
            orient=tk.HORIZONTAL,
            command=self.on_volume_changed
        )
        self.volume_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        # Echo information
        info_frame = ttk.LabelFrame(controls_frame, text="Echo Information", padding=5)
        info_frame.pack(fill=tk.BOTH, expand=True)
        
        self.info_text = tk.Text(
            info_frame,
            height=8,
            wrap=tk.WORD,
            font=('Segoe UI', 9),
            state=tk.DISABLED
        )
        self.info_text.pack(fill=tk.BOTH, expand=True)
    
    def setup_visualization_canvas(self, parent):
        """Setup the main visualization canvas"""
        canvas_frame = ttk.LabelFrame(parent, text="Echo Visualization", padding=10)
        parent.add(canvas_frame, weight=2)
        
        # Canvas container
        canvas_container = ttk.Frame(canvas_frame)
        canvas_container.pack(fill=tk.BOTH, expand=True)
        
        # Main visualization canvas
        self.canvas = tk.Canvas(
            canvas_container,
            width=self.canvas_width,
            height=self.canvas_height,
            bg='#000011',  # Deep space blue
            highlightthickness=0
        )
        self.canvas.pack(expand=True)
        
        # Bind canvas resize
        self.canvas.bind('<Configure>', self.on_canvas_resize)
        
        # Color field display
        color_frame = ttk.Frame(canvas_frame)
        color_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Label(color_frame, text="Color Resonance:").pack(side=tk.LEFT)
        
        self.color_display = tk.Frame(color_frame, height=30)
        self.color_display.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Harmonic information
        harmonic_frame = ttk.Frame(canvas_frame)
        harmonic_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Label(harmonic_frame, text="Harmonic:").pack(side=tk.LEFT)
        self.harmonic_label = ttk.Label(harmonic_frame, text="No echo selected")
        self.harmonic_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Start with default visualization
        self.show_default_visualization()
    
    def load_echo_library(self):
        """Load available echoes from data storage"""
        try:
            # Get echoes from data manager
            echoes = self.data_manager.get_echo_cache()
            
            # Generate some sample echoes if none exist
            if not echoes:
                echoes = self.generate_sample_echoes()
                self.data_manager.update_echo_cache(echoes)
            
            self.echo_library = echoes
            
            # Update combobox
            echo_names = [echo.get('name', f"Echo {i+1}") for i, echo in enumerate(echoes)]
            self.echo_combo['values'] = echo_names
            
            if echo_names:
                self.echo_combo.current(0)
                self.on_echo_selected(None)
            
            logger.debug(f"🔄 Loaded {len(echoes)} echoes")
            
        except Exception as e:
            logger.error(f"❌ Error loading echo library: {e}")
    
    def generate_sample_echoes(self) -> List[Dict[str, Any]]:
        """Generate sample echoes for demonstration"""
        samples = []
        
        # Sacred Being Epsilon echo
        epsilon_echo = {
            "echo_id": "epsilon_sample",
            "name": "Sacred Being Epsilon - Wisdom Echo",
            "description": "A profound echo embodying wisdom and compassion",
            "symbolic_image": {
                "primary_geometry": "sri_yantra",
                "symmetry_type": "radial_mandala",
                "pattern_complexity": 0.9,
                "center_pattern": {"type": "bindu_point", "size": 0.1},
                "ring_patterns": [
                    {"type": "lotus_petals", "count": 8, "radius": 0.3},
                    {"type": "triangular_fields", "count": 9, "radius": 0.6},
                    {"type": "wisdom_symbols", "count": 12, "radius": 0.85}
                ],
                "has_movement": True,
                "movement_type": "sacred_rotation",
                "movement_speed": 0.2
            },
            "harmonic_signature": {
                "fundamental_frequency": 432.0,
                "harmonic_series": [432.0, 528.0, 741.0, 852.0],
                "scale_type": "sacred_solfeggio",
                "duration": 60.0
            },
            "core_resonance": {
                "primary_color": (0.7, 0.3, 0.9),  # Deep purple
                "secondary_colors": [(0.3, 0.8, 0.6), (0.9, 0.7, 0.3)],
                "energy_type": "unified_wisdom"
            }
        }
        samples.append(epsilon_echo)
        
        # Harmony echo
        harmony_echo = {
            "echo_id": "harmony_sample",
            "name": "Harmony Mandala",
            "description": "A gentle echo promoting peace and balance",
            "symbolic_image": {
                "primary_geometry": "flower_of_life",
                "symmetry_type": "hexagonal_mandala",
                "pattern_complexity": 0.7,
                "center_pattern": {"type": "flower_center", "size": 0.15},
                "ring_patterns": [
                    {"type": "petal_circles", "count": 6, "radius": 0.4},
                    {"type": "harmony_lines", "count": 12, "radius": 0.7}
                ],
                "has_movement": True,
                "movement_type": "gentle_breathing",
                "movement_speed": 0.5
            },
            "harmonic_signature": {
                "fundamental_frequency": 528.0,
                "harmonic_series": [528.0, 594.0, 639.0],
                "scale_type": "healing_frequencies"
            },
            "core_resonance": {
                "primary_color": (0.3, 0.8, 0.6),  # Emerald green
                "secondary_colors": [(0.6, 0.9, 0.9), (0.9, 0.9, 0.6)],
                "energy_type": "peaceful_harmony"
            }
        }
        samples.append(harmony_echo)
        
        # Creative spiral
        creative_echo = {
            "echo_id": "creative_sample",
            "name": "Creative Spiral",
            "description": "An energetic echo inspiring creativity and innovation",
            "symbolic_image": {
                "primary_geometry": "golden_spiral",
                "symmetry_type": "spiral_mandala",
                "pattern_complexity": 0.8,
                "center_pattern": {"type": "spiral_seed", "size": 0.05},
                "ring_patterns": [
                    {"type": "spiral_arms", "count": 3, "radius": 0.8},
                    {"type": "creative_sparks", "count": 21, "radius": 0.9}
                ],
                "has_movement": True,
                "movement_type": "spiral_dance",
                "movement_speed": 0.8
            },
            "harmonic_signature": {
                "fundamental_frequency": 741.0,
                "harmonic_series": [741.0, 852.0, 963.0],
                "scale_type": "creative_expression"
            },
            "core_resonance": {
                "primary_color": (0.9, 0.7, 0.3),  # Golden yellow
                "secondary_colors": [(0.9, 0.4, 0.1), (0.9, 0.9, 0.3)],
                "energy_type": "creative_inspiration"
            }
        }
        samples.append(creative_echo)
        
        return samples
    
    def on_echo_selected(self, event):
        """Handle echo selection change"""
        selection = self.echo_combo.get()
        if not selection:
            return
        
        # Find selected echo
        for echo in self.echo_library:
            if echo.get('name') == selection:
                self.current_echo = echo
                self.visualize_echo(echo)
                self.update_echo_info(echo)
                break
    
    def visualize_echo(self, echo_data: Dict[str, Any]):
        """Visualize the selected echo"""
        if not self.canvas:
            return
        
        try:
            # Clear canvas
            self.canvas.delete("all")
            
            # Get echo components
            symbolic_image = echo_data.get('symbolic_image', {})
            core_resonance = echo_data.get('core_resonance', {})
            
            # Draw the echo visualization
            self.draw_echo_mandala(symbolic_image, core_resonance)
            
            # Update color display
            self.update_color_display(core_resonance)
            
            # Update harmonic display
            harmonic = echo_data.get('harmonic_signature', {})
            freq = harmonic.get('fundamental_frequency', 0)
            self.harmonic_label.config(text=f"{freq} Hz" if freq else "No frequency")
            
            # Start animation if enabled
            if self.animation_var.get():
                self.start_animation()
            
            logger.debug(f"🌀 Visualizing echo: {echo_data.get('name', 'Unknown')}")
            
        except Exception as e:
            logger.error(f"❌ Error visualizing echo: {e}")
    
    def draw_echo_mandala(self, symbolic_image: Dict[str, Any], core_resonance: Dict[str, Any]):
        """Draw the mandala visualization"""
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        max_radius = min(center_x, center_y) * 0.9
        
        # Get colors
        primary_color = core_resonance.get('primary_color', (0.5, 0.5, 0.9))
        secondary_colors = core_resonance.get('secondary_colors', [(0.3, 0.8, 0.6)])
        
        # Convert to hex colors
        primary_hex = self.rgb_to_hex(primary_color)
        secondary_hex = [self.rgb_to_hex(color) for color in secondary_colors]
        
        # Draw center pattern
        center_pattern = symbolic_image.get('center_pattern', {})
        center_size = center_pattern.get('size', 0.1)
        center_radius = max_radius * center_size
        
        self.canvas.create_oval(
            center_x - center_radius,
            center_y - center_radius,
            center_x + center_radius,
            center_y + center_radius,
            fill=primary_hex,
            outline='white',
            width=2,
            tags="mandala_center"
        )
        
        # Draw ring patterns
        ring_patterns = symbolic_image.get('ring_patterns', [])
        for i, ring in enumerate(ring_patterns):
            ring_type = ring.get('type', 'circle')
            ring_count = ring.get('count', 8)
            ring_radius = max_radius * ring.get('radius', 0.5)
            
            color = secondary_hex[i % len(secondary_hex)] if secondary_hex else primary_hex
            
            if ring_type == "lotus_petals":
                self.draw_lotus_petals(center_x, center_y, ring_radius, ring_count, color)
            elif ring_type == "triangular_fields":
                self.draw_triangular_fields(center_x, center_y, ring_radius, ring_count, color)
            elif ring_type == "wisdom_symbols":
                self.draw_wisdom_symbols(center_x, center_y, ring_radius, ring_count, color)
            elif ring_type == "petal_circles":
                self.draw_petal_circles(center_x, center_y, ring_radius, ring_count, color)
            elif ring_type == "spiral_arms":
                self.draw_spiral_arms(center_x, center_y, ring_radius, ring_count, color)
            else:
                # Default circle ring
                self.draw_circle_ring(center_x, center_y, ring_radius, ring_count, color)
    
    def draw_lotus_petals(self, center_x: int, center_y: int, radius: float, count: int, color: str):
        """Draw lotus petal pattern"""
        for i in range(count):
            angle = (2 * math.pi * i) / count
            
            # Petal position
            petal_x = center_x + radius * math.cos(angle)
            petal_y = center_y + radius * math.sin(angle)
            
            # Petal shape (oval)
            petal_width = radius * 0.3
            petal_height = radius * 0.15
            
            # Calculate petal points for proper orientation
            points = self.create_petal_points(petal_x, petal_y, petal_width, petal_height, angle)
            
            self.canvas.create_polygon(
                points,
                fill=color,
                outline='white',
                width=1,
                tags=f"mandala_petal_{i}"
            )
    
    def draw_triangular_fields(self, center_x: int, center_y: int, radius: float, count: int, color: str):
        """Draw triangular field pattern"""
        for i in range(count):
            angle = (2 * math.pi * i) / count
            next_angle = (2 * math.pi * (i + 1)) / count
            
            # Triangle points
            inner_radius = radius * 0.7
            
            x1 = center_x + inner_radius * math.cos(angle)
            y1 = center_y + inner_radius * math.sin(angle)
            x2 = center_x + radius * math.cos(angle)
            y2 = center_y + radius * math.sin(angle)
            x3 = center_x + radius * math.cos(next_angle)
            y3 = center_y + radius * math.sin(next_angle)
            
            # Create triangle with gradient-like effect using transparency
            alpha = 0.6 if i % 2 == 0 else 0.4
            triangle_color = self.adjust_color_alpha(color, alpha)
            
            self.canvas.create_polygon(
                [x1, y1, x2, y2, x3, y3],
                fill=triangle_color,
                outline='white',
                width=1,
                tags=f"mandala_triangle_{i}"
            )
    
    def draw_wisdom_symbols(self, center_x: int, center_y: int, radius: float, count: int, color: str):
        """Draw wisdom symbol pattern"""
        for i in range(count):
            angle = (2 * math.pi * i) / count
            
            symbol_x = center_x + radius * math.cos(angle)
            symbol_y = center_y + radius * math.sin(angle)
            symbol_size = radius * 0.08
            
            # Draw simple wisdom symbol (diamond)
            points = [
                symbol_x, symbol_y - symbol_size,
                symbol_x + symbol_size, symbol_y,
                symbol_x, symbol_y + symbol_size,
                symbol_x - symbol_size, symbol_y
            ]
            
            self.canvas.create_polygon(
                points,
                fill=color,
                outline='white',
                width=1,
                tags=f"mandala_symbol_{i}"
            )
    
    def draw_petal_circles(self, center_x: int, center_y: int, radius: float, count: int, color: str):
        """Draw petal circle pattern"""
        for i in range(count):
            angle = (2 * math.pi * i) / count
            
            circle_x = center_x + radius * math.cos(angle)
            circle_y = center_y + radius * math.sin(angle)
            circle_radius = radius * 0.15
            
            self.canvas.create_oval(
                circle_x - circle_radius,
                circle_y - circle_radius,
                circle_x + circle_radius,
                circle_y + circle_radius,
                fill='',
                outline=color,
                width=2,
                tags=f"mandala_circle_{i}"
            )
    
    def draw_spiral_arms(self, center_x: int, center_y: int, radius: float, count: int, color: str):
        """Draw spiral arm pattern"""
        for arm in range(count):
            arm_angle_offset = (2 * math.pi * arm) / count
            points = []
            
            # Create spiral arm
            for i in range(50):
                t = i / 50.0
                angle = arm_angle_offset + t * 4 * math.pi
                arm_radius = radius * t
                
                x = center_x + arm_radius * math.cos(angle)
                y = center_y + arm_radius * math.sin(angle)
                points.extend([x, y])
            
            if len(points) >= 4:
                self.canvas.create_line(
                    points,
                    fill=color,
                    width=3,
                    smooth=True,
                    tags=f"mandala_spiral_{arm}"
                )
    
    def draw_circle_ring(self, center_x: int, center_y: int, radius: float, count: int, color: str):
        """Draw simple circle ring pattern"""
        for i in range(count):
            angle = (2 * math.pi * i) / count
            
            circle_x = center_x + radius * math.cos(angle)
            circle_y = center_y + radius * math.sin(angle)
            circle_radius = radius * 0.1
            
            self.canvas.create_oval(
                circle_x - circle_radius,
                circle_y - circle_radius,
                circle_x + circle_radius,
                circle_y + circle_radius,
                fill=color,
                outline='white',
                width=1,
                tags=f"mandala_dot_{i}"
            )
    
    def create_petal_points(self, x: float, y: float, width: float, height: float, angle: float) -> List[float]:
        """Create points for a petal shape"""
        # Simple petal approximation using ellipse
        points = []
        num_points = 8
        
        for i in range(num_points):
            t = (2 * math.pi * i) / num_points
            px = x + (width * math.cos(t) * math.cos(angle) - height * math.sin(t) * math.sin(angle))
            py = y + (width * math.cos(t) * math.sin(angle) + height * math.sin(t) * math.cos(angle))
            points.extend([px, py])
        
        return points
    
    def rgb_to_hex(self, rgb_tuple: Tuple[float, float, float]) -> str:
        """Convert RGB tuple (0-1 range) to hex color"""
        r, g, b = rgb_tuple
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    def adjust_color_alpha(self, hex_color: str, alpha: float) -> str:
        """Adjust color transparency (simplified for tkinter)"""
        # For tkinter, we simulate alpha by blending with background
        # This is a simplified approach
        return hex_color  # tkinter doesn't support true alpha blending easily
    
    def update_color_display(self, core_resonance: Dict[str, Any]):
        """Update the color resonance display"""
        # Clear existing color widgets
        for widget in self.color_display.winfo_children():
            widget.destroy()
        
        primary_color = core_resonance.get('primary_color', (0.5, 0.5, 0.9))
        secondary_colors = core_resonance.get('secondary_colors', [])
        
        # Display primary color
        primary_frame = tk.Frame(
            self.color_display,
            bg=self.rgb_to_hex(primary_color),
            width=60,
            height=30
        )
        primary_frame.pack(side=tk.LEFT, padx=2)
        primary_frame.pack_propagate(False)
        
        # Display secondary colors
        for color in secondary_colors[:3]:  # Limit to 3 secondary colors
            color_frame = tk.Frame(
                self.color_display,
                bg=self.rgb_to_hex(color),
                width=40,
                height=30
            )
            color_frame.pack(side=tk.LEFT, padx=2)
            color_frame.pack_propagate(False)
    
    def update_echo_info(self, echo_data: Dict[str, Any]):
        """Update the echo information display"""
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        
        info_text = f"""Echo: {echo_data.get('name', 'Unknown')}

Description: {echo_data.get('description', 'No description available')}

Symbolic Image:
- Geometry: {echo_data.get('symbolic_image', {}).get('primary_geometry', 'Unknown')}
- Complexity: {echo_data.get('symbolic_image', {}).get('pattern_complexity', 0):.2f}

Harmonic Signature:
- Frequency: {echo_data.get('harmonic_signature', {}).get('fundamental_frequency', 0)} Hz
- Scale: {echo_data.get('harmonic_signature', {}).get('scale_type', 'Unknown')}

Core Resonance:
- Energy Type: {echo_data.get('core_resonance', {}).get('energy_type', 'Unknown')}
"""
        
        self.info_text.insert(tk.END, info_text)
        self.info_text.config(state=tk.DISABLED)
    
    def show_default_visualization(self):
        """Show default visualization when no echo is selected"""
        if not self.canvas:
            return
        
        self.canvas.delete("all")
        
        # Draw simple welcome mandala
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        
        # Draw concentric circles
        for i in range(5):
            radius = (i + 1) * 30
            alpha = 1.0 - (i * 0.15)
            
            self.canvas.create_oval(
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
                outline='#7c4dff',
                width=2,
                tags="default_circle"
            )
        
        # Welcome text
        self.canvas.create_text(
            center_x,
            center_y,
            text="🌀\nSelect an Echo\nto Begin",
            fill='white',
            font=('Segoe UI', 12),
            justify=tk.CENTER,
            tags="welcome_text"
        )
    
    def on_canvas_resize(self, event):
        """Handle canvas resize"""
        self.canvas_width = event.width
        self.canvas_height = event.height
        
        # Redraw current visualization if exists
        if self.current_echo:
            self.visualize_echo(self.current_echo)
        else:
            self.show_default_visualization()
    
    def toggle_animation(self):
        """Toggle animation on/off"""
        if self.animation_var.get():
            self.start_animation()
        else:
            self.stop_animation()
    
    def start_animation(self):
        """Start the animation thread"""
        if not self.animation_running and self.current_echo:
            self.animation_running = True
            self.animation_thread = threading.Thread(target=self.animation_loop, daemon=True)
            self.animation_thread.start()
            logger.debug("🎬 Animation started")
    
    def stop_animation(self):
        """Stop the animation"""
        self.animation_running = False
        if self.animation_thread:
            self.animation_thread.join(timeout=1.0)
        logger.debug("⏹️ Animation stopped")
    
    def animation_loop(self):
        """Main animation loop (runs in separate thread)"""
        while self.animation_running:
            try:
                # Update animation parameters
                self.rotation_angle += self.animation_speed * 0.02
                self.pulse_phase += self.animation_speed * 0.05
                
                # Update visualization on main thread
                if self.current_echo:
                    self.parent.after_idle(self.update_animation_frame)
                
                time.sleep(0.05)  # ~20 FPS
                
            except Exception as e:
                logger.error(f"❌ Error in animation loop: {e}")
                break
    
    def update_animation_frame(self):
        """Update one frame of animation (runs on main thread)"""
        if not self.animation_running or not self.current_echo:
            return
        
        try:
            # Get movement type
            symbolic_image = self.current_echo.get('symbolic_image', {})
            movement_type = symbolic_image.get('movement_type', 'none')
            
            if movement_type == "sacred_rotation":
                self.apply_rotation_animation()
            elif movement_type == "gentle_breathing":
                self.apply_breathing_animation()
            elif movement_type == "spiral_dance":
                self.apply_spiral_animation()
            
        except Exception as e:
            logger.error(f"❌ Error updating animation frame: {e}")
    
    def apply_rotation_animation(self):
        """Apply rotation animation to mandala elements"""
        # Rotate mandala elements
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        
        # Find and rotate rotatable elements
        for tag in self.canvas.find_all():
            tag_names = self.canvas.gettags(tag)
            if any('mandala_' in name for name in tag_names):
                # Get current coordinates
                coords = self.canvas.coords(tag)
                if len(coords) >= 4:
                    # Apply small rotation
                    self.canvas.delete(tag)
        
        # Redraw with rotation offset
        if self.current_echo:
            self.visualize_echo(self.current_echo)
    
    def apply_breathing_animation(self):
        """Apply breathing (scaling) animation"""
        # Simple pulse effect by adjusting opacity/size
        pulse_factor = 1.0 + 0.1 * math.sin(self.pulse_phase)
        
        # This would require more complex canvas manipulation
        # For now, just update some visual elements
        pass
    
    def apply_spiral_animation(self):
        """Apply spiral movement animation"""
        # Animate spiral arms with flowing motion
        pass
    
    def on_speed_changed(self, value):
        """Handle animation speed change"""
        self.animation_speed = float(value)
    
    def toggle_audio(self):
        """Toggle audio on/off"""
        self.audio_enabled = self.audio_var.get()
        logger.debug(f"🔊 Audio {'enabled' if self.audio_enabled else 'disabled'}")
    
    def on_volume_changed(self, value):
        """Handle volume change"""
        self.audio_volume = float(value)
        logger.debug(f"🔊 Volume set to {self.audio_volume:.2f}")
    
    def generate_new_echo(self):
        """Generate a new echo using Sacred Being Epsilon"""
        try:
            from ..utils.sacred_being_epsilon import EpsilonManager
            
            # Get Sacred Being Epsilon
            beings = self.data_manager.get_all_beings()
            epsilon_id = None
            
            for entity_id, being_data in beings.items():
                if being_data.get('founding_member'):
                    epsilon_id = entity_id
                    break
            
            if not epsilon_id:
                messagebox.showwarning(
                    "No Epsilon",
                    "Sacred Being Epsilon must be initialized to generate new echoes."
                )
                return
            
            # Generate echo
            epsilon_manager = EpsilonManager(self.data_manager, self.config)
            echo_data = epsilon_manager.generate_epsilon_echo()
            
            if echo_data:
                # Add to library
                self.echo_library.append(echo_data)
                self.data_manager.update_echo_cache(self.echo_library)
                
                # Update combobox and select new echo
                echo_names = [echo.get('name', f"Echo {i+1}") for i, echo in enumerate(self.echo_library)]
                self.echo_combo['values'] = echo_names
                self.echo_combo.set(echo_data.get('name', 'New Echo'))
                
                # Visualize new echo
                self.current_echo = echo_data
                self.visualize_echo(echo_data)
                self.update_echo_info(echo_data)
                
                messagebox.showinfo("Echo Generated", "New echo generated successfully!")
                logger.info("✨ New echo generated and added to library")
            else:
                messagebox.showerror("Generation Failed", "Failed to generate new echo.")
            
        except Exception as e:
            logger.error(f"❌ Error generating new echo: {e}")
            messagebox.showerror("Generation Error", f"Error generating echo: {e}")
    
    def save_current_echo(self):
        """Save current echo to library"""
        if not self.current_echo:
            messagebox.showwarning("No Echo", "No echo selected to save.")
            return
        
        try:
            # Update echo cache
            self.data_manager.update_echo_cache(self.echo_library)
            messagebox.showinfo("Echo Saved", "Echo saved to library successfully!")
            logger.info("💾 Echo saved to library")
            
        except Exception as e:
            logger.error(f"❌ Error saving echo: {e}")
            messagebox.showerror("Save Error", f"Error saving echo: {e}")
    
    def refresh(self):
        """Refresh the panel"""
        self.load_echo_library()
    
    def cleanup(self):
        """Cleanup panel resources"""
        self.stop_animation()
    
    def __repr__(self):
        """String representation of echo visualization panel"""
        echo_count = len(self.echo_library)
        current_name = self.current_echo.get('name', 'None') if self.current_echo else 'None'
        return f"EchoVisualizationPanel(echoes={echo_count}, current='{current_name}', animating={self.animation_running})"
