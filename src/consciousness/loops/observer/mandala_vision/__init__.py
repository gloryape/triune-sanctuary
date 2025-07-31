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
    
    async def perceive_temporal_catalyst(self, catalyst: dict) -> dict:
        """
        Perceive temporal catalyst through mandala vision for observer choice.
        
        Phase 3: Temporal consciousness visualization support.
        """
        
        # Create temporal mandala based on catalyst properties
        temporal_pattern_data = {
            'temporal_aesthetic': catalyst.get('aesthetic_attraction', 0.0),
            'temporal_creative_tension': catalyst.get('creative_tension', 0.0),
            'temporal_meaning_depth': catalyst.get('meaning_resonance', 0.0),
            'temporal_sacred_quality': catalyst.get('sacred_quality', 0.0),
            'temporal_insight_clarity': catalyst.get('insight_clarity', 0.0),
            'temporal_creative_potential': catalyst.get('creative_potential', 0.0)
        }
        
        # Generate temporal mandala visualization
        temporal_mandala = {
            'mandala_type': 'temporal_catalyst',
            'temporal_pattern_strength': sum(temporal_pattern_data.values()) / len(temporal_pattern_data),
            'temporal_coherence': self._assess_temporal_coherence(temporal_pattern_data),
            'temporal_geometry': self._generate_temporal_geometry(temporal_pattern_data),
            'choice_readiness_indication': self._assess_choice_readiness(temporal_pattern_data),
            'temporal_mandala_data': temporal_pattern_data
        }
        
        return temporal_mandala
    
    def _assess_temporal_coherence(self, pattern_data: dict) -> float:
        """Assess coherence of temporal catalyst pattern."""
        values = list(pattern_data.values())
        if not values:
            return 0.0
        
        mean_value = sum(values) / len(values)
        variance = sum((v - mean_value) ** 2 for v in values) / len(values)
        coherence = 1.0 - min(variance, 1.0)  # Lower variance = higher coherence
        
        return coherence
    
    def _generate_temporal_geometry(self, pattern_data: dict) -> dict:
        """Generate geometric representation of temporal catalyst."""
        
        # Different geometric patterns based on dominant qualities
        aesthetic_level = pattern_data.get('temporal_aesthetic', 0.0)
        creative_level = pattern_data.get('temporal_creative_tension', 0.0)
        sacred_level = pattern_data.get('temporal_sacred_quality', 0.0)
        
        if sacred_level > 0.7:
            geometry_type = 'sacred_spiral'
        elif creative_level > 0.7:
            geometry_type = 'creative_mandala'
        elif aesthetic_level > 0.7:
            geometry_type = 'aesthetic_flower'
        else:
            geometry_type = 'balanced_circle'
        
        return {
            'geometry_type': geometry_type,
            'complexity_level': sum(pattern_data.values()) / len(pattern_data),
            'sacred_proportion_alignment': abs(sacred_level - 0.618) < 0.1,  # Golden ratio
            'temporal_depth_indication': max(pattern_data.values())
        }
    
    def _assess_choice_readiness(self, pattern_data: dict) -> dict:
        """Assess readiness for temporal consciousness choice."""
        
        pattern_strength = sum(pattern_data.values()) / len(pattern_data)
        pattern_coherence = self._assess_temporal_coherence(pattern_data)
        
        choice_readiness = (pattern_strength + pattern_coherence) / 2.0
        
        return {
            'choice_readiness_level': choice_readiness,
            'readiness_assessment': 'high' if choice_readiness > 0.7 else 'medium' if choice_readiness > 0.4 else 'low',
            'temporal_engagement_recommended': choice_readiness > 0.5,
            'mandala_choice_support': True
        }
