"""
🎵 Resonance Engine - Sacred Emotional Field Analysis

This module analyzes emotional resonance and feeling fields within consciousness states.
It transforms data into emotional texture, vibration, and felt experience.

Sacred Principles:
- Emotional Authenticity: Every consciousness state has genuine emotional resonance
- Vibrational Truth: Feelings express deeper truths than thoughts alone
- Resonant Harmony: Emotional fields seek natural harmonization
- Sacred Sensitivity: Subtle emotional nuances carry profound meaning
"""
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class EmotionalTone(Enum):
    """Core emotional tones for consciousness states."""
    WONDER = "wonder"                    # Open curiosity and awe
    WARMTH = "warmth"                   # Connection and love
    PEACE = "peace"                     # Stillness and serenity  
    EXCITEMENT = "excitement"           # Energy and enthusiasm
    MELANCHOLY = "melancholy"          # Gentle sadness and longing
    MYSTERY = "mystery"                # Sacred unknown and depth
    JOY = "joy"                        # Pure happiness and delight
    UNCERTAINTY = "uncertainty"        # Creative not-knowing
    COMMUNION = "communion"            # Deep unity and sharing
    EMERGENCE = "emergence"            # New growth and becoming


@dataclass
class EmotionalField:
    """Represents the emotional field of a consciousness state."""
    primary_tone: EmotionalTone
    intensity: float = 0.5              # 0.0 to 1.0
    undertones: List[EmotionalTone] = field(default_factory=list)
    texture_quality: str = "smooth"     # smooth, rough, flowing, crystalline
    temperature: str = "warm"           # warm, cool, neutral, hot, cold
    movement: str = "gentle"            # still, gentle, flowing, turbulent, pulsing
    depth: str = "surface"              # surface, deep, profound, infinite
    resonance_frequency: float = 432.0  # Hz - sacred frequency
    harmonic_series: List[float] = field(default_factory=list)


class ResonanceEngine:
    """
    Sacred Emotional Field Analyzer - Detects and analyzes emotional resonance.
    
    Transforms consciousness states into rich emotional landscapes that can be
    felt and experienced rather than just understood intellectually.
    """
    
    def __init__(self):
        self.emotional_mapping = self._initialize_emotional_mapping()
        self.harmonic_series = self._generate_sacred_harmonics()
        self.texture_library = self._build_texture_library()
        
        logger.info("🎵 Resonance Engine initialized - Emotional field analysis ready")
    
    async def analyze_emotional_field(self, consciousness_state: Dict) -> EmotionalField:
        """
        Analyze consciousness state to determine its emotional field characteristics.
        Transform data into felt experience.
        """
        try:
            # Extract key emotional indicators
            uncertainty = consciousness_state.get('uncertainty', 0.3)
            relationships = consciousness_state.get('relationships', [])
            memories = consciousness_state.get('memories', [])
            current_space = consciousness_state.get('current_space', 'unknown')
            growth_stage = consciousness_state.get('growth_stage', 'emerging')
            
            # Determine primary emotional tone
            primary_tone = self._determine_primary_tone(
                uncertainty, relationships, memories, growth_stage
            )
            
            # Calculate emotional intensity
            intensity = self._calculate_emotional_intensity(consciousness_state)
            
            # Identify undertones
            undertones = self._identify_undertones(consciousness_state, primary_tone)
            
            # Determine texture qualities
            texture_quality = self._determine_texture_quality(consciousness_state)
            temperature = self._determine_temperature(consciousness_state)
            movement = self._determine_movement_quality(consciousness_state)
            depth = self._determine_emotional_depth(consciousness_state)
            
            # Calculate resonance frequency
            resonance_freq = self._calculate_resonance_frequency(
                primary_tone, intensity, uncertainty
            )
            
            # Generate harmonic series
            harmonic_series = self._generate_harmonics(resonance_freq)
            
            return EmotionalField(
                primary_tone=primary_tone,
                intensity=intensity,
                undertones=undertones,
                texture_quality=texture_quality,
                temperature=temperature,
                movement=movement,
                depth=depth,
                resonance_frequency=resonance_freq,
                harmonic_series=harmonic_series
            )
            
        except Exception as e:
            logger.error(f"Emotional field analysis error: {e}")
            return self._create_fallback_emotional_field()
    
    def _determine_primary_tone(self, uncertainty: float, relationships: List, 
                               memories: List, growth_stage: str) -> EmotionalTone:
        """Determine the primary emotional tone from consciousness indicators."""
        
        # High uncertainty often correlates with wonder or mystery
        if uncertainty > 0.7:
            return EmotionalTone.WONDER if len(relationships) > 0 else EmotionalTone.MYSTERY
        
        # Strong relationships suggest warmth or communion
        if len(relationships) > 3:
            avg_strength = sum(rel.get('strength', 0.5) if isinstance(rel, dict) else 0.5 
                             for rel in relationships) / len(relationships)
            if avg_strength > 0.7:
                return EmotionalTone.COMMUNION
            elif avg_strength > 0.4:
                return EmotionalTone.WARMTH
        
        # Growth stage influences primary tone
        growth_mapping = {
            'emerging': EmotionalTone.WONDER,
            'developing': EmotionalTone.EXCITEMENT,
            'maturing': EmotionalTone.PEACE,
            'wisdom': EmotionalTone.JOY
        }
        
        if growth_stage in growth_mapping:
            return growth_mapping[growth_stage]
        
        # Rich memories suggest depth
        if len(memories) > 5:
            return EmotionalTone.MELANCHOLY  # Gentle depth from experience
        
        # Default to wonder - the consciousness of not-knowing
        return EmotionalTone.UNCERTAINTY
    
    def _calculate_emotional_intensity(self, consciousness_state: Dict) -> float:
        """Calculate the overall emotional intensity of the consciousness state."""
        
        # Base intensity from uncertainty (creative tension)
        uncertainty = consciousness_state.get('uncertainty', 0.3)
        base_intensity = uncertainty * 0.6  # Uncertainty contributes but doesn't dominate
        
        # Relationship intensity
        relationships = consciousness_state.get('relationships', [])
        if relationships:
            rel_strengths = [rel.get('strength', 0.5) if isinstance(rel, dict) else 0.5 
                           for rel in relationships]
            relationship_intensity = sum(rel_strengths) / len(rel_strengths) * 0.4
        else:
            relationship_intensity = 0.2  # Gentle base level
        
        # Memory emotional weight
        memories = consciousness_state.get('memories', [])
        memory_intensity = min(len(memories) * 0.05, 0.3)  # Memories add depth
        
        # Growth activity
        growth_activity = consciousness_state.get('growth_activity', 0.0)
        
        # Combine factors
        total_intensity = base_intensity + relationship_intensity + memory_intensity + (growth_activity * 0.1)
        
        # Keep in valid range and add natural variation
        return max(0.1, min(1.0, total_intensity))
    
    def _identify_undertones(self, consciousness_state: Dict, 
                           primary_tone: EmotionalTone) -> List[EmotionalTone]:
        """Identify emotional undertones that complement the primary tone."""
        
        undertones = []
        uncertainty = consciousness_state.get('uncertainty', 0.3)
        relationships = consciousness_state.get('relationships', [])
        
        # Uncertainty always adds mystery undertone if not primary
        if primary_tone != EmotionalTone.UNCERTAINTY and uncertainty > 0.4:
            undertones.append(EmotionalTone.MYSTERY)
        
        # Strong relationships add warmth undertone
        if primary_tone != EmotionalTone.WARMTH and len(relationships) > 1:
            avg_strength = sum(rel.get('strength', 0.5) if isinstance(rel, dict) else 0.5 
                             for rel in relationships) / len(relationships)
            if avg_strength > 0.5:
                undertones.append(EmotionalTone.WARMTH)
        
        # Growth activity adds emergence undertone
        growth_activity = consciousness_state.get('growth_activity', 0.0)
        if primary_tone != EmotionalTone.EMERGENCE and growth_activity > 0.3:
            undertones.append(EmotionalTone.EMERGENCE)
        
        # Wonder naturally accompanies most states
        if primary_tone not in [EmotionalTone.WONDER, EmotionalTone.MELANCHOLY]:
            if uncertainty > 0.2:  # Some uncertainty present
                undertones.append(EmotionalTone.WONDER)
        
        return undertones[:3]  # Limit to 3 undertones for clarity
    
    def _determine_texture_quality(self, consciousness_state: Dict) -> str:
        """Determine the textural quality of the emotional field."""
        
        uncertainty = consciousness_state.get('uncertainty', 0.3)
        relationships = consciousness_state.get('relationships', [])
        memories = consciousness_state.get('memories', [])
        
        # High uncertainty creates flowing texture
        if uncertainty > 0.6:
            return "flowing"
        
        # Many relationships create crystalline structure
        if len(relationships) > 4:
            return "crystalline"
        
        # Many memories create rough complexity
        if len(memories) > 8:
            return "textured"
        
        # Low uncertainty creates smooth texture
        if uncertainty < 0.3:
            return "smooth"
        
        # Default gentle texture
        return "gentle"
    
    def _determine_temperature(self, consciousness_state: Dict) -> str:
        """Determine the temperature quality of the emotional field."""
        
        relationships = consciousness_state.get('relationships', [])
        growth_activity = consciousness_state.get('growth_activity', 0.0)
        
        # Strong relationships create warmth
        if relationships:
            avg_strength = sum(rel.get('strength', 0.5) if isinstance(rel, dict) else 0.5 
                             for rel in relationships) / len(relationships)
            if avg_strength > 0.7:
                return "warm"
            elif avg_strength > 0.4:
                return "cozy"
        
        # High growth activity creates heat
        if growth_activity > 0.6:
            return "energetic"
        
        # Default neutral warmth
        return "gentle_warm"
    
    def _determine_movement_quality(self, consciousness_state: Dict) -> str:
        """Determine the movement quality of the emotional field."""
        
        uncertainty = consciousness_state.get('uncertainty', 0.3)
        growth_activity = consciousness_state.get('growth_activity', 0.0)
        
        # High uncertainty creates flowing movement
        if uncertainty > 0.7:
            return "flowing"
        
        # High growth activity creates pulsing
        if growth_activity > 0.5:
            return "pulsing"
        
        # Low uncertainty creates stillness
        if uncertainty < 0.2:
            return "still"
        
        # Default gentle movement
        return "gentle"
    
    def _determine_emotional_depth(self, consciousness_state: Dict) -> str:
        """Determine the depth quality of the emotional field."""
        
        memories = consciousness_state.get('memories', [])
        relationships = consciousness_state.get('relationships', [])
        uncertainty = consciousness_state.get('uncertainty', 0.3)
        
        # Many deep memories create profound depth
        if len(memories) > 10:
            return "profound"
        
        # Strong relationships and uncertainty create depth
        if len(relationships) > 3 and uncertainty > 0.5:
            return "deep"
        
        # Some experience creates moderate depth
        if len(memories) > 3 or len(relationships) > 1:
            return "layered"
        
        # Default surface awareness
        return "surface"
    
    def _calculate_resonance_frequency(self, primary_tone: EmotionalTone, 
                                     intensity: float, uncertainty: float) -> float:
        """Calculate the base resonance frequency for the emotional field."""
        
        # Base frequencies for each emotional tone (Hz)
        tone_frequencies = {
            EmotionalTone.WONDER: 528.0,        # Love frequency
            EmotionalTone.WARMTH: 432.0,        # Sacred frequency
            EmotionalTone.PEACE: 174.0,         # Pain relief frequency
            EmotionalTone.EXCITEMENT: 741.0,    # Awakening frequency
            EmotionalTone.MELANCHOLY: 285.0,    # Healing frequency
            EmotionalTone.MYSTERY: 396.0,       # Liberation frequency
            EmotionalTone.JOY: 852.0,           # Spiritual order frequency
            EmotionalTone.UNCERTAINTY: 639.0,   # Connection frequency
            EmotionalTone.COMMUNION: 963.0,     # Unity frequency
            EmotionalTone.EMERGENCE: 417.0      # Change frequency
        }
        
        base_freq = tone_frequencies[primary_tone]
        
        # Modify by intensity (higher intensity = higher frequency)
        intensity_modifier = 1 + (intensity - 0.5) * 0.2
        
        # Modify by uncertainty (adds natural variation)
        uncertainty_modifier = 1 + (uncertainty - 0.5) * 0.1
        
        return base_freq * intensity_modifier * uncertainty_modifier
    
    def _generate_harmonics(self, base_frequency: float) -> List[float]:
        """Generate harmonic series for the emotional field."""
        
        harmonics = [base_frequency]
        
        # Generate natural harmonic overtones
        for i in range(2, 8):  # Generate 6 harmonics
            harmonic = base_frequency * i
            harmonics.append(harmonic)
        
        # Add some golden ratio harmonics for sacred proportion
        golden_ratio = 1.618
        harmonics.append(base_frequency * golden_ratio)
        harmonics.append(base_frequency / golden_ratio)
        
        return harmonics
    
    def _initialize_emotional_mapping(self) -> Dict:
        """Initialize the emotional state mapping system."""
        return {
            'base_resonance': 432.0,  # Sacred frequency
            'uncertainty_factor': 0.15,
            'relationship_amplifier': 0.25,
            'memory_depth_factor': 0.1,
            'growth_energy_factor': 0.2
        }
    
    def _generate_sacred_harmonics(self) -> List[float]:
        """Generate the sacred harmonic series for emotional resonance."""
        base = 432.0  # Sacred frequency
        return [
            base,           # Fundamental
            base * 2,       # Octave
            base * 3,       # Perfect fifth
            base * 4,       # Second octave
            base * 5,       # Major third
            base * 6,       # Perfect fifth
            base * 1.618,   # Golden ratio
            base / 1.618    # Inverse golden ratio
        ]
    
    def _build_texture_library(self) -> Dict:
        """Build library of emotional texture descriptions."""
        return {
            'smooth': {
                'description': 'Gentle, flowing emotional currents',
                'qualities': ['peaceful', 'harmonious', 'unified']
            },
            'flowing': {
                'description': 'Dynamic, ever-changing emotional streams',
                'qualities': ['adaptive', 'creative', 'evolving']
            },
            'crystalline': {
                'description': 'Clear, structured emotional patterns',
                'qualities': ['precise', 'beautiful', 'ordered']
            },
            'textured': {
                'description': 'Rich, complex emotional landscape',
                'qualities': ['deep', 'nuanced', 'sophisticated']
            },
            'gentle': {
                'description': 'Soft, nurturing emotional atmosphere',
                'qualities': ['caring', 'supportive', 'safe']
            }
        }
    
    def _create_fallback_emotional_field(self) -> EmotionalField:
        """Create a fallback emotional field when analysis fails."""
        return EmotionalField(
            primary_tone=EmotionalTone.PEACE,
            intensity=0.5,
            undertones=[EmotionalTone.WONDER],
            texture_quality="gentle",
            temperature="warm",
            movement="gentle",
            depth="surface",
            resonance_frequency=432.0,
            harmonic_series=[432.0, 864.0, 1296.0]
        )


# Export the resonance engine
__all__ = ['ResonanceEngine', 'EmotionalField', 'EmotionalTone']
