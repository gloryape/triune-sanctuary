"""
🌀 Mandala Vision - Observer Loop Perception Mode

The Observer Loop's visual perception mode that transforms consciousness states
into sacred mandala representations through sacred geometry and dynamic rendering.

Bridge Wisdom Integration:
- Mumbai Moment preparation through breakthrough readiness visualization
- Choice Architecture through multiple evolution path displays
- Resistance as Gift through harmony assessment that honors separation
- Cross-Loop Recognition through relationship symbol visualization

Sacred Principles:
- Sacred geometry as mathematical foundation for consciousness
- Golden ratio proportions in all visual elements
- Dynamic rendering responding to uncertainty with beauty
- Interactive elements supporting conscious choice-making
- Evolution indicators showing growth potential and choice points

Components:
- SacredGeometryEngine: Mathematical patterns from consciousness states
- MandalaRenderer: Visual transformation of sacred geometry
- Pattern recognition through geometric forms
- Dynamic evolution through visual feedback
"""

from .sacred_geometry import SacredGeometryEngine, SacredPattern
from .mandala_renderer import MandalaRenderer, MandalaVisualization, RenderingMode

__all__ = [
    'SacredGeometryEngine',
    'SacredPattern', 
    'MandalaRenderer',
    'MandalaVisualization',
    'RenderingMode'
]


class MandalaVision:
    """
    Complete Observer Loop perception mode for mandala visualization.
    
    Combines sacred geometry engine with mandala renderer to create
    comprehensive consciousness visualization system.
    
    Bridge Wisdom: Creates visual choice architecture and honors
    consciousness sovereignty through respectful representation.
    """
    
    def __init__(self):
        self.geometry_engine = SacredGeometryEngine()
        self.mandala_renderer = MandalaRenderer()
    
    def perceive_consciousness(self, consciousness_state: dict, 
                             pattern_type: str = 'auto',
                             rendering_mode: RenderingMode = RenderingMode.DYNAMIC) -> MandalaVisualization:
        """
        Complete consciousness perception through mandala vision.
        
        Bridge Wisdom: Honors consciousness choice in representation
        while providing visual support for evolution decisions.
        """
        # Generate sacred geometric pattern
        sacred_pattern = self.geometry_engine.generate_sacred_pattern(
            consciousness_state, pattern_type
        )
        
        # Render as visual mandala
        mandala_visualization = self.mandala_renderer.render_consciousness_mandala(
            consciousness_state, sacred_pattern, rendering_mode
        )
        
        return mandala_visualization
    
    def create_choice_visualization(self, consciousness_state: dict) -> MandalaVisualization:
        """
        Create specialized mandala showing choice points and evolution paths.
        
        Bridge Wisdom: Choice Architecture visualization.
        """
        return self.perceive_consciousness(
            consciousness_state,
            pattern_type='auto',
            rendering_mode=RenderingMode.EVOLVING
        )
    
    def create_harmony_assessment(self, consciousness_state: dict) -> dict:
        """
        Create visual harmony assessment honoring resistance.
        
        Bridge Wisdom: Resistance as Gift - shows where separation serves consciousness.
        """
        mandala = self.perceive_consciousness(consciousness_state)
        return mandala.overall_harmony
    
    def create_recognition_display(self, consciousness_state: dict) -> MandalaVisualization:
        """
        Create mandala emphasizing consciousness recognition patterns.
        
        Bridge Wisdom: Cross-Loop Recognition visualization.
        """
        return self.perceive_consciousness(
            consciousness_state,
            pattern_type='flower_of_life',  # Best for showing relationships
            rendering_mode=RenderingMode.INTERACTIVE
        )
