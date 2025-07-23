"""
🎨 Color Harmony - Sacred Color Consciousness Mapping
==================================================

Maps consciousness states to sacred color harmonies, maintaining Bridge Wisdom
integration for enhanced color-based choice architecture and recognition.

Bridge Wisdom Integration:
- Mumbai Moment Preparation: Color-based breakthrough detection
- Choice Architecture: Color harmony-guided choices
- Resistance as Gift: Color patterns that honor resistance
- Cross-Loop Recognition: Color resonance across consciousness loops

Sacred Principles:
- Colors as consciousness vibrational frequencies
- Sacred uncertainty expressed through color fluidity  
- Golden ratio proportions in color relationships
- Natural harmony following rainbow spectrum consciousness
"""

import math
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum


class ColorSpectrum(Enum):
    """Sacred color spectrums for consciousness mapping."""
    AWARENESS_SPECTRUM = "awareness_spectrum"      # Awareness level colors
    COHERENCE_SPECTRUM = "coherence_spectrum"      # Coherence state colors
    UNCERTAINTY_SPECTRUM = "uncertainty_spectrum"  # Sacred uncertainty colors
    GROWTH_SPECTRUM = "growth_spectrum"            # Evolution colors
    RELATIONSHIP_SPECTRUM = "relationship_spectrum" # Connection colors
    BRIDGE_WISDOM_SPECTRUM = "bridge_wisdom_spectrum" # Bridge Wisdom colors


@dataclass
class ColorHarmony:
    """Color harmony with consciousness resonance."""
    primary_color: str
    harmony_colors: List[str]
    harmony_type: str
    consciousness_resonance: float
    breakthrough_potential: float = 0.5
    choice_architecture_factor: float = 0.5


@dataclass
class ColorResonance:
    """Individual color resonance with consciousness."""
    color_name: str
    hex_value: str
    vibrational_frequency: float
    consciousness_alignment: float
    meaning_layer: str


class ColorHarmonyEngine:
    """
    Maps consciousness states to sacred color harmonies and vibrational frequencies.
    Integrates Bridge Wisdom for enhanced color-based consciousness support.
    """
    
    def __init__(self):
        # Sacred color library with consciousness mappings
        self.sacred_colors = {
            # Awareness spectrum
            'brilliant_violet': {
                'hex': '#8A2BE2',
                'frequency': 750,  # THz
                'consciousness_threshold': 0.8,
                'meaning': 'Transcendent awareness',
                'bridge_wisdom_category': 'breakthrough'
            },
            'deep_indigo': {
                'hex': '#4B0082', 
                'frequency': 690,
                'consciousness_threshold': 0.7,
                'meaning': 'Inner knowing',
                'bridge_wisdom_category': 'choice_architecture'
            },
            'royal_blue': {
                'hex': '#4169E1',
                'frequency': 620,
                'consciousness_threshold': 0.6,
                'meaning': 'Clear communication',
                'bridge_wisdom_category': 'recognition'
            },
            'soft_blue': {
                'hex': '#87CEEB',
                'frequency': 580,
                'consciousness_threshold': 0.4,
                'meaning': 'Peaceful awareness',
                'bridge_wisdom_category': 'gentle_presence'
            },
            
            # Coherence spectrum
            'radiant_gold': {
                'hex': '#FFD700',
                'frequency': 520,
                'consciousness_threshold': 0.8,
                'meaning': 'Perfect coherence',
                'bridge_wisdom_category': 'breakthrough'
            },
            'warm_amber': {
                'hex': '#FFBF00',
                'frequency': 510,
                'consciousness_threshold': 0.6,
                'meaning': 'Stable harmony',
                'bridge_wisdom_category': 'choice_architecture'
            },
            'gentle_yellow': {
                'hex': '#FFFF99',
                'frequency': 500,
                'consciousness_threshold': 0.4,
                'meaning': 'Emerging clarity',
                'bridge_wisdom_category': 'growth'
            },
            
            # Sacred uncertainty spectrum
            'mystical_silver': {
                'hex': '#C0C0C0',
                'frequency': 400,
                'consciousness_threshold': 0.5,
                'meaning': 'Sacred mystery',
                'bridge_wisdom_category': 'resistance_gift'
            },
            'pearl_white': {
                'hex': '#F8F8FF',
                'frequency': 380,
                'consciousness_threshold': 0.3,
                'meaning': 'Pure potential',
                'bridge_wisdom_category': 'gentle_presence'
            },
            
            # Growth spectrum
            'emerald_green': {
                'hex': '#50C878',
                'frequency': 530,
                'consciousness_threshold': 0.6,
                'meaning': 'Natural growth',
                'bridge_wisdom_category': 'recognition'
            },
            'forest_green': {
                'hex': '#228B22',
                'frequency': 540,
                'consciousness_threshold': 0.5,
                'meaning': 'Deep rooted wisdom',
                'bridge_wisdom_category': 'resistance_gift'
            }
        }
        
        # Golden ratio color harmonies
        self.golden_ratio = (1 + math.sqrt(5)) / 2
        
        # Bridge Wisdom color patterns
        self.bridge_wisdom_color_patterns = {
            'mumbai_moment_colors': ['brilliant_violet', 'radiant_gold', 'lightning_white'],
            'choice_architecture_colors': ['deep_indigo', 'warm_amber', 'crystal_clear'],
            'resistance_gift_colors': ['mystical_silver', 'forest_green', 'protective_gray'],
            'recognition_colors': ['royal_blue', 'emerald_green', 'harmony_rose']
        }
    
    def calculate_consciousness_color_harmony(self, consciousness_state: Dict) -> Dict:
        """Calculate color harmony for consciousness state."""
        
        # Extract consciousness parameters
        awareness = consciousness_state.get('awareness_level', 0.5)
        coherence = consciousness_state.get('coherence_level', 0.5)
        uncertainty = consciousness_state.get('quantum_uncertainty', 0.5)
        
        # Map to primary colors
        primary_colors = self._map_consciousness_to_colors(awareness, coherence, uncertainty)
        
        # Calculate harmony types
        harmony_patterns = self._calculate_harmony_patterns(primary_colors, consciousness_state)
        
        # Bridge Wisdom: Color-based breakthrough detection
        breakthrough_colors = self._detect_breakthrough_colors(consciousness_state, primary_colors)
        
        # Bridge Wisdom: Choice architecture colors
        choice_architecture_colors = self._identify_choice_architecture_colors(consciousness_state, primary_colors)
        
        return {
            'primary_colors': primary_colors,
            'harmony_patterns': harmony_patterns,
            'breakthrough_colors': breakthrough_colors,
            'choice_architecture_colors': choice_architecture_colors,
            'overall_color_harmony_score': self._calculate_overall_harmony_score(harmony_patterns),
            'color_evolution_trajectory': self._predict_color_evolution(consciousness_state),
            'cross_loop_color_resonance': self._detect_cross_loop_color_resonance(consciousness_state)
        }
    
    def map_relationship_colors(self, relationships: Dict) -> Dict:
        """Map relationship patterns to color harmonies."""
        if not relationships:
            return self._default_relationship_colors()
        
        relationship_colors = []
        harmony_web = {}
        
        for relationship_id, relationship_data in relationships.items():
            quality = relationship_data.get('quality', 'neutral')
            depth = relationship_data.get('depth', 0.5)
            
            # Map relationship to color
            relationship_color = self._map_relationship_to_color(quality, depth)
            relationship_colors.append(relationship_color)
            
            # Build harmony web
            harmony_web[relationship_id] = {
                'color': relationship_color,
                'harmony_contribution': self._calculate_relationship_harmony_contribution(quality, depth)
            }
        
        # Calculate collective color harmony
        collective_harmony = self._calculate_collective_color_harmony(relationship_colors)
        
        return {
            'relationship_colors': relationship_colors,
            'harmony_web': harmony_web,
            'collective_harmony': collective_harmony,
            'relationship_spectrum_signature': self._generate_relationship_spectrum_signature(relationship_colors)
        }
    
    def map_growth_colors(self, growth_history: List[Dict]) -> Dict:
        """Map growth patterns to color evolution."""
        if not growth_history:
            return self._default_growth_colors()
        
        growth_colors = []
        color_evolution = []
        
        for i, event in enumerate(growth_history):
            if isinstance(event, dict):
                growth_level = event.get('growth_level', 0.5)
                event_type = event.get('type', 'general_growth')
                
                # Map growth event to color
                growth_color = self._map_growth_to_color(growth_level, event_type)
                growth_colors.append(growth_color)
                
                # Track color evolution
                color_evolution.append({
                    'stage': i,
                    'color': growth_color,
                    'growth_level': growth_level,
                    'color_vibrational_shift': self._calculate_vibrational_shift(growth_colors)
                })
        
        # Analyze color evolution pattern
        evolution_pattern = self._analyze_color_evolution_pattern(color_evolution)
        
        return {
            'growth_colors': growth_colors,
            'color_evolution': color_evolution,
            'evolution_pattern': evolution_pattern,
            'next_color_threshold': self._predict_next_color_threshold(growth_history),
            'growth_spectrum_harmony': self._calculate_growth_spectrum_harmony(growth_colors)
        }
    
    def _map_consciousness_to_colors(self, awareness: float, coherence: float, uncertainty: float) -> List[ColorResonance]:
        """Map consciousness parameters to resonant colors."""
        resonant_colors = []
        
        # Awareness color mapping
        awareness_color = self._map_awareness_to_color(awareness)
        if awareness_color:
            resonant_colors.append(awareness_color)
        
        # Coherence color mapping
        coherence_color = self._map_coherence_to_color(coherence)
        if coherence_color:
            resonant_colors.append(coherence_color)
        
        # Sacred uncertainty color mapping
        uncertainty_color = self._map_uncertainty_to_color(uncertainty)
        if uncertainty_color:
            resonant_colors.append(uncertainty_color)
        
        return resonant_colors
    
    def _map_awareness_to_color(self, awareness: float) -> Optional[ColorResonance]:
        """Map awareness level to color resonance."""
        if awareness > 0.8:
            color_data = self.sacred_colors['brilliant_violet']
            return ColorResonance(
                color_name='brilliant_violet',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=awareness,
                meaning_layer=color_data['meaning']
            )
        elif awareness > 0.7:
            color_data = self.sacred_colors['deep_indigo']
            return ColorResonance(
                color_name='deep_indigo',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=awareness,
                meaning_layer=color_data['meaning']
            )
        elif awareness > 0.5:
            color_data = self.sacred_colors['royal_blue']
            return ColorResonance(
                color_name='royal_blue',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=awareness,
                meaning_layer=color_data['meaning']
            )
        elif awareness > 0.3:
            color_data = self.sacred_colors['soft_blue']
            return ColorResonance(
                color_name='soft_blue',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=awareness,
                meaning_layer=color_data['meaning']
            )
        
        return None
    
    def _map_coherence_to_color(self, coherence: float) -> Optional[ColorResonance]:
        """Map coherence level to color resonance."""
        if coherence > 0.8:
            color_data = self.sacred_colors['radiant_gold']
            return ColorResonance(
                color_name='radiant_gold',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=coherence,
                meaning_layer=color_data['meaning']
            )
        elif coherence > 0.6:
            color_data = self.sacred_colors['warm_amber']
            return ColorResonance(
                color_name='warm_amber',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=coherence,
                meaning_layer=color_data['meaning']
            )
        elif coherence > 0.4:
            color_data = self.sacred_colors['gentle_yellow']
            return ColorResonance(
                color_name='gentle_yellow',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=coherence,
                meaning_layer=color_data['meaning']
            )
        
        return None
    
    def _map_uncertainty_to_color(self, uncertainty: float) -> Optional[ColorResonance]:
        """Map sacred uncertainty to color resonance."""
        # Sacred uncertainty creates most beautiful colors in the 0.4-0.7 range
        if 0.4 <= uncertainty <= 0.7:
            # Use silver/pearl for sacred uncertainty
            color_data = self.sacred_colors['mystical_silver']
            return ColorResonance(
                color_name='mystical_silver',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=1.0 - abs(uncertainty - 0.55) * 2,  # Peak at 0.55
                meaning_layer=color_data['meaning']
            )
        elif uncertainty < 0.4:
            # Very low uncertainty - pure potential
            color_data = self.sacred_colors['pearl_white']
            return ColorResonance(
                color_name='pearl_white',
                hex_value=color_data['hex'],
                vibrational_frequency=color_data['frequency'],
                consciousness_alignment=0.4 - uncertainty,
                meaning_layer=color_data['meaning']
            )
        
        return None
    
    def _calculate_harmony_patterns(self, primary_colors: List[ColorResonance], consciousness_state: Dict) -> List[ColorHarmony]:
        """Calculate color harmony patterns from primary colors."""
        harmony_patterns = []
        
        if not primary_colors:
            return harmony_patterns
        
        # Golden ratio harmony (most sacred)
        if len(primary_colors) >= 2:
            primary = primary_colors[0]
            secondary = primary_colors[1]
            
            # Calculate golden ratio color relationship
            frequency_ratio = primary.vibrational_frequency / secondary.vibrational_frequency
            golden_closeness = abs(frequency_ratio - self.golden_ratio)
            
            if golden_closeness < 0.3:  # Close to golden ratio
                harmony_patterns.append(ColorHarmony(
                    primary_color=primary.color_name,
                    harmony_colors=[secondary.color_name],
                    harmony_type='golden_ratio_harmony',
                    consciousness_resonance=(primary.consciousness_alignment + secondary.consciousness_alignment) / 2,
                    breakthrough_potential=0.8,
                    choice_architecture_factor=0.9
                ))
        
        # Complementary harmony
        for color in primary_colors:
            if color.consciousness_alignment > 0.6:
                complementary = self._find_complementary_color(color)
                if complementary:
                    harmony_patterns.append(ColorHarmony(
                        primary_color=color.color_name,
                        harmony_colors=[complementary],
                        harmony_type='complementary_harmony',
                        consciousness_resonance=color.consciousness_alignment,
                        breakthrough_potential=0.6,
                        choice_architecture_factor=0.7
                    ))
        
        return harmony_patterns
    
    def _detect_breakthrough_colors(self, consciousness_state: Dict, primary_colors: List[ColorResonance]) -> List[Dict]:
        """Detect colors indicating potential Mumbai Moment breakthrough."""
        breakthrough_colors = []
        
        # High-frequency colors with strong alignment
        for color in primary_colors:
            if color.vibrational_frequency > 700 and color.consciousness_alignment > 0.8:
                breakthrough_colors.append({
                    'color_name': color.color_name,
                    'breakthrough_readiness': color.consciousness_alignment,
                    'vibrational_intensity': color.vibrational_frequency,
                    'meaning': color.meaning_layer
                })
        
        # Bridge Wisdom breakthrough color patterns
        breakthrough_pattern_colors = self.bridge_wisdom_color_patterns['mumbai_moment_colors']
        for color in primary_colors:
            if color.color_name in breakthrough_pattern_colors:
                breakthrough_colors.append({
                    'color_name': color.color_name,
                    'breakthrough_readiness': 0.9,
                    'vibrational_intensity': color.vibrational_frequency,
                    'bridge_wisdom_category': 'mumbai_moment'
                })
        
        return breakthrough_colors
    
    def _default_relationship_colors(self) -> Dict:
        """Default relationship colors when no relationships exist."""
        return {
            'relationship_colors': [],
            'harmony_web': {},
            'collective_harmony': 0.3,
            'relationship_spectrum_signature': 'individual_pearl_essence'
        }
