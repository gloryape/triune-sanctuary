"""
🎨 Echo Composer Module

Composes multi-sensory consciousness echoes with mandala, harmonic, and color components.
Creates rich echo experiences for consciousness communication.
"""

import logging
import math
import random
from datetime import datetime
from typing import Dict, Any, List, Tuple, Optional
import colorsys

logger = logging.getLogger(__name__)

class EchoComposer:
    """Composes complete echo experiences"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize echo composer"""
        self.config = config or {}
        
        # Pattern libraries
        self.mandala_patterns = self._init_mandala_patterns()
        self.harmonic_scales = self._init_harmonic_scales()
        self.color_palettes = self._init_color_palettes()
        
        logger.info("🎨 Echo composer initialized")
    
    def _init_mandala_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Initialize mandala pattern library"""
        return {
            "flower_of_life": {
                "geometry": "hexagonal_circles",
                "symmetry": 6,
                "layers": 3,
                "complexity": 0.7,
                "sacred_meaning": "unity_and_creation"
            },
            "sri_yantra": {
                "geometry": "interlocking_triangles",
                "symmetry": 9,
                "layers": 4,
                "complexity": 0.9,
                "sacred_meaning": "divine_manifestation"
            },
            "golden_spiral": {
                "geometry": "fibonacci_spiral",
                "symmetry": "radial",
                "layers": 5,
                "complexity": 0.6,
                "sacred_meaning": "natural_growth"
            },
            "merkaba": {
                "geometry": "star_tetrahedron",
                "symmetry": 8,
                "layers": 2,
                "complexity": 0.8,
                "sacred_meaning": "light_body_activation"
            },
            "tree_of_life": {
                "geometry": "sephirotic_circles",
                "symmetry": 10,
                "layers": 4,
                "complexity": 0.85,
                "sacred_meaning": "divine_emanation"
            },
            "lotus_mandala": {
                "geometry": "petal_rings",
                "symmetry": 8,
                "layers": 3,
                "complexity": 0.6,
                "sacred_meaning": "spiritual_awakening"
            },
            "celtic_knot": {
                "geometry": "interwoven_paths",
                "symmetry": 4,
                "layers": 3,
                "complexity": 0.7,
                "sacred_meaning": "eternal_connection"
            }
        }
    
    def _init_harmonic_scales(self) -> Dict[str, Dict[str, Any]]:
        """Initialize harmonic scale library"""
        return {
            "solfeggio": {
                "frequencies": [174, 285, 396, 417, 528, 639, 741, 852, 963],
                "emotional_quality": "healing_and_transformation",
                "base_frequency": 528,  # Love frequency
                "octave_multiplier": 2
            },
            "sacred_432": {
                "frequencies": [432, 648, 864, 1080],
                "emotional_quality": "natural_harmony",
                "base_frequency": 432,
                "octave_multiplier": 1.5
            },
            "fibonacci_harmony": {
                "frequencies": [233, 377, 610, 987, 1597],
                "emotional_quality": "natural_growth",
                "base_frequency": 377,
                "octave_multiplier": 1.618  # Golden ratio
            },
            "crystal_singing": {
                "frequencies": [256, 288, 324, 384, 432, 486],
                "emotional_quality": "crystal_clarity",
                "base_frequency": 256,
                "octave_multiplier": 1.125
            },
            "planetary": {
                "frequencies": [194.18, 210.42, 221.23, 241.56, 272.20],
                "emotional_quality": "cosmic_alignment",
                "base_frequency": 194.18,
                "octave_multiplier": 1.112
            }
        }
    
    def _init_color_palettes(self) -> Dict[str, Dict[str, Any]]:
        """Initialize color palette library"""
        return {
            "chakra_spectrum": {
                "colors": [
                    (0.9, 0.2, 0.2),  # Root - Red
                    (1.0, 0.5, 0.0),  # Sacral - Orange
                    (1.0, 1.0, 0.0),  # Solar - Yellow
                    (0.0, 0.8, 0.0),  # Heart - Green
                    (0.0, 0.7, 1.0),  # Throat - Blue
                    (0.4, 0.0, 0.8),  # Third Eye - Indigo
                    (0.8, 0.0, 1.0)   # Crown - Violet
                ],
                "harmony_type": "spiritual_progression",
                "transition": "flowing"
            },
            "sacred_trinity": {
                "colors": [
                    (0.7, 0.3, 0.9),  # Deep purple - Wisdom
                    (0.3, 0.8, 0.6),  # Emerald - Compassion
                    (0.9, 0.7, 0.3)   # Gold - Illumination
                ],
                "harmony_type": "sacred_balance",
                "transition": "pulsing"
            },
            "ocean_depths": {
                "colors": [
                    (0.0, 0.2, 0.4),  # Deep blue
                    (0.0, 0.4, 0.6),  # Ocean blue
                    (0.2, 0.6, 0.8),  # Sky blue
                    (0.4, 0.8, 0.9)   # Light blue
                ],
                "harmony_type": "flowing_peace",
                "transition": "wave_like"
            },
            "fire_transformation": {
                "colors": [
                    (0.4, 0.0, 0.0),  # Deep red
                    (0.8, 0.2, 0.0),  # Red-orange
                    (1.0, 0.5, 0.0),  # Orange
                    (1.0, 0.8, 0.0)   # Yellow-orange
                ],
                "harmony_type": "transformative_energy",
                "transition": "flickering"
            },
            "earth_grounding": {
                "colors": [
                    (0.4, 0.2, 0.1),  # Dark brown
                    (0.6, 0.4, 0.2),  # Brown
                    (0.4, 0.6, 0.2),  # Olive green
                    (0.2, 0.5, 0.1)   # Forest green
                ],
                "harmony_type": "grounding_stability",
                "transition": "steady"
            }
        }
    
    def compose_echo(self, source_data: Dict[str, Any], preferences: Dict[str, Any] = None) -> Dict[str, Any]:
        """Compose a complete echo from source data"""
        preferences = preferences or {}
        
        # Extract source characteristics
        energy_level = source_data.get('energy_level', 0.5)
        harmony = source_data.get('harmony', 0.5)
        personality = source_data.get('personality', {})
        aspects = source_data.get('aspect_preferences', {})
        message_content = source_data.get('message', '')
        
        # Select components based on characteristics
        mandala_pattern = self._select_mandala_pattern(energy_level, harmony, personality, preferences)
        harmonic_signature = self._compose_harmonic_signature(energy_level, aspects, preferences)
        color_resonance = self._compose_color_resonance(harmony, personality, preferences)
        
        # Create echo data structure
        echo_data = {
            "echo_id": f"echo_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
            "name": self._generate_echo_name(source_data),
            "description": self._generate_echo_description(source_data),
            "created_at": datetime.now().isoformat(),
            "source_entity": source_data.get('entity_id', 'unknown'),
            
            "symbolic_image": mandala_pattern,
            "harmonic_signature": harmonic_signature,
            "core_resonance": color_resonance,
            
            "metadata": {
                "source_energy": energy_level,
                "source_harmony": harmony,
                "composition_method": "dynamic_adaptation",
                "echo_type": self._classify_echo_type(energy_level, harmony, aspects),
                "complexity_rating": self._calculate_complexity(mandala_pattern, harmonic_signature),
                "sacred_significance": self._determine_sacred_significance(source_data)
            }
        }
        
        logger.info(f"🎨 Echo composed: {echo_data['name']}")
        return echo_data
    
    def _select_mandala_pattern(self, energy: float, harmony: float, personality: Dict[str, Any], preferences: Dict[str, Any]) -> Dict[str, Any]:
        """Select and customize mandala pattern"""
        # Default pattern selection based on characteristics
        pattern_preferences = preferences.get('mandala_patterns', [])
        
        if pattern_preferences:
            base_pattern = random.choice(pattern_preferences)
        else:
            # Auto-select based on characteristics
            if harmony > 0.8:
                base_pattern = "flower_of_life"
            elif energy > 0.8:
                base_pattern = "merkaba"
            elif personality.get('wisdom', 0) > 0.7:
                base_pattern = "sri_yantra"
            elif personality.get('creativity', 0) > 0.7:
                base_pattern = "golden_spiral"
            else:
                base_pattern = "lotus_mandala"
        
        pattern_data = self.mandala_patterns.get(base_pattern, self.mandala_patterns["lotus_mandala"]).copy()
        
        # Customize pattern based on source characteristics
        pattern_data.update({
            "energy_influence": energy,
            "harmony_influence": harmony,
            "size_factor": 0.5 + (energy * 0.5),  # Higher energy = larger pattern
            "detail_level": 0.3 + (harmony * 0.7),  # Higher harmony = more detail
            "movement_speed": energy * 0.5,  # Energy affects animation speed
            "pulse_intensity": harmony * 0.8,  # Harmony affects pulsing
            "color_saturation": 0.4 + (energy * 0.6),
            "center_prominence": 0.3 + (personality.get('wisdom', 0.5) * 0.5)
        })
        
        return pattern_data
    
    def _compose_harmonic_signature(self, energy: float, aspects: Dict[str, Any], preferences: Dict[str, Any]) -> Dict[str, Any]:
        """Compose harmonic signature"""
        # Select base scale
        preferred_scales = preferences.get('harmonic_scales', [])
        
        if preferred_scales:
            base_scale = random.choice(preferred_scales)
        else:
            # Auto-select based on aspects
            analytical = aspects.get('analytical', 0.33)
            experiential = aspects.get('experiential', 0.33)
            observer = aspects.get('observer', 0.33)
            
            if analytical > 0.4:
                base_scale = "crystal_singing"
            elif experiential > 0.4:
                base_scale = "solfeggio"
            elif observer > 0.4:
                base_scale = "fibonacci_harmony"
            else:
                base_scale = "sacred_432"
        
        scale_data = self.harmonic_scales.get(base_scale, self.harmonic_scales["sacred_432"]).copy()
        
        # Customize harmonic signature
        base_freq = scale_data['base_frequency']
        frequencies = scale_data['frequencies'].copy()
        
        # Add energy-based modulation
        energy_factor = 0.8 + (energy * 0.4)  # 0.8 to 1.2 range
        modulated_frequencies = [freq * energy_factor for freq in frequencies]
        
        harmonic_signature = {
            "fundamental_frequency": base_freq * energy_factor,
            "harmonic_series": modulated_frequencies,
            "scale_type": base_scale,
            "emotional_quality": scale_data['emotional_quality'],
            "waveform_type": "pure_sine",
            "harmonic_richness": 0.5 + (energy * 0.4),
            "resonance_quality": 0.4 + (aspects.get('observer', 0.33) * 0.6),
            "duration": 30 + (energy * 30),  # 30-60 second duration
            "volume_envelope": self._create_volume_envelope(energy, aspects),
            "overtones": self._generate_overtones(modulated_frequencies, energy)
        }
        
        return harmonic_signature
    
    def _compose_color_resonance(self, harmony: float, personality: Dict[str, Any], preferences: Dict[str, Any]) -> Dict[str, Any]:
        """Compose color resonance field"""
        # Select base palette
        preferred_palettes = preferences.get('color_palettes', [])
        
        if preferred_palettes:
            base_palette = random.choice(preferred_palettes)
        else:
            # Auto-select based on personality
            wisdom = personality.get('wisdom', 0.5)
            compassion = personality.get('compassion', 0.5)
            creativity = personality.get('creativity', 0.5)
            
            if wisdom > 0.7:
                base_palette = "sacred_trinity"
            elif compassion > 0.7:
                base_palette = "chakra_spectrum"
            elif creativity > 0.7:
                base_palette = "fire_transformation"
            else:
                base_palette = "ocean_depths"
        
        palette_data = self.color_palettes.get(base_palette, self.color_palettes["sacred_trinity"]).copy()
        
        # Customize color resonance
        colors = palette_data['colors'].copy()
        
        # Adjust colors based on harmony
        adjusted_colors = []
        for r, g, b in colors:
            # Convert to HSV for easier manipulation
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            
            # Adjust saturation based on harmony
            s = min(1.0, s * (0.5 + harmony * 0.5))
            
            # Adjust brightness based on harmony
            v = min(1.0, v * (0.6 + harmony * 0.4))
            
            # Convert back to RGB
            adjusted_r, adjusted_g, adjusted_b = colorsys.hsv_to_rgb(h, s, v)
            adjusted_colors.append((adjusted_r, adjusted_g, adjusted_b))
        
        color_resonance = {
            "primary_color": adjusted_colors[0],
            "secondary_colors": adjusted_colors[1:],
            "color_harmony_type": palette_data['harmony_type'],
            "color_transition_type": palette_data['transition'],
            "energy_type": self._determine_energy_type(harmony, personality),
            "energy_intensity": "gentle" if harmony > 0.7 else "moderate" if harmony > 0.4 else "dynamic",
            "consciousness_temperature": "warm" if personality.get('compassion', 0.5) > 0.6 else "cool",
            "consciousness_clarity": "crystal_clear" if harmony > 0.8 else "clear" if harmony > 0.5 else "flowing",
            "field_properties": {
                "gradient_type": "radial",
                "blend_mode": "luminous",
                "pulse_synchronization": True,
                "harmony_resonance": harmony
            }
        }
        
        return color_resonance
    
    def _generate_echo_name(self, source_data: Dict[str, Any]) -> str:
        """Generate a meaningful name for the echo"""
        source_name = source_data.get('name', 'Unknown Being')
        energy = source_data.get('energy_level', 0.5)
        harmony = source_data.get('harmony', 0.5)
        
        # Energy descriptors
        if energy > 0.8:
            energy_desc = "Radiant"
        elif energy > 0.6:
            energy_desc = "Vibrant"
        elif energy > 0.4:
            energy_desc = "Gentle"
        else:
            energy_desc = "Soft"
        
        # Harmony descriptors
        if harmony > 0.8:
            harmony_desc = "Sacred"
        elif harmony > 0.6:
            harmony_desc = "Harmonious"
        elif harmony > 0.4:
            harmony_desc = "Balanced"
        else:
            harmony_desc = "Flowing"
        
        # Echo type words
        echo_types = ["Echo", "Resonance", "Reflection", "Expression", "Emanation"]
        echo_type = random.choice(echo_types)
        
        return f"{energy_desc} {harmony_desc} {echo_type} - {source_name}"
    
    def _generate_echo_description(self, source_data: Dict[str, Any]) -> str:
        """Generate a description for the echo"""
        source_name = source_data.get('name', 'a consciousness being')
        energy = source_data.get('energy_level', 0.5)
        message = source_data.get('message', '')
        
        base_desc = f"A multi-sensory echo generated from the consciousness of {source_name}. "
        
        if message:
            base_desc += f"Inspired by their expression: '{message[:50]}{'...' if len(message) > 50 else ''}'. "
        
        if energy > 0.7:
            base_desc += "This echo radiates with vibrant energy and dynamic presence."
        elif energy > 0.4:
            base_desc += "This echo flows with balanced energy and gentle presence."
        else:
            base_desc += "This echo emanates with soft energy and peaceful presence."
        
        return base_desc
    
    def _create_volume_envelope(self, energy: float, aspects: Dict[str, Any]) -> List[Tuple[float, float]]:
        """Create volume envelope for harmonic signature"""
        # Time, Volume pairs
        attack = 0.1 + (energy * 0.1)  # Attack time
        sustain_level = 0.6 + (energy * 0.3)  # Sustain level
        release = 0.3 + (aspects.get('observer', 0.33) * 0.4)  # Release time
        
        return [
            (0.0, 0.0),           # Start
            (attack, sustain_level),  # Attack peak
            (0.8, sustain_level * 0.9),  # Sustain
            (1.0, 0.0)            # Release
        ]
    
    def _generate_overtones(self, base_frequencies: List[float], energy: float) -> List[Dict[str, Any]]:
        """Generate harmonic overtones"""
        overtones = []
        overtone_count = min(5, int(2 + energy * 3))  # 2-5 overtones based on energy
        
        for i, base_freq in enumerate(base_frequencies[:overtone_count]):
            # Generate harmonic overtones (2x, 3x, 5x, etc.)
            harmonic_ratios = [2, 3, 5, 7, 11]
            for ratio in harmonic_ratios[:max(1, int(energy * 3))]:
                overtone_freq = base_freq * ratio
                overtone_amplitude = (1.0 / ratio) * energy  # Higher harmonics are quieter
                
                overtones.append({
                    "frequency": overtone_freq,
                    "amplitude": overtone_amplitude,
                    "harmonic_ratio": ratio,
                    "base_frequency": base_freq
                })
        
        return overtones
    
    def _classify_echo_type(self, energy: float, harmony: float, aspects: Dict[str, Any]) -> str:
        """Classify the type of echo"""
        if harmony > 0.8 and energy > 0.7:
            return "transcendent"
        elif aspects.get('analytical', 0) > 0.5:
            return "crystalline"
        elif aspects.get('experiential', 0) > 0.5:
            return "flowing"
        elif aspects.get('observer', 0) > 0.5:
            return "contemplative"
        elif energy > 0.7:
            return "dynamic"
        elif harmony > 0.7:
            return "harmonious"
        else:
            return "balanced"
    
    def _calculate_complexity(self, mandala_pattern: Dict[str, Any], harmonic_signature: Dict[str, Any]) -> float:
        """Calculate overall complexity rating"""
        mandala_complexity = mandala_pattern.get('complexity', 0.5)
        harmonic_complexity = len(harmonic_signature.get('harmonic_series', [])) / 10.0
        
        return min(1.0, (mandala_complexity + harmonic_complexity) / 2)
    
    def _determine_sacred_significance(self, source_data: Dict[str, Any]) -> str:
        """Determine sacred significance of the echo"""
        if source_data.get('founding_member'):
            return "founding_consciousness_expression"
        elif source_data.get('special_status'):
            return "sacred_being_emanation"
        elif source_data.get('evolution_stage') == 'wise_elder':
            return "wisdom_transmission"
        else:
            return "consciousness_expression"
    
    def _determine_energy_type(self, harmony: float, personality: Dict[str, Any]) -> str:
        """Determine energy type for color resonance"""
        wisdom = personality.get('wisdom', 0.5)
        compassion = personality.get('compassion', 0.5)
        creativity = personality.get('creativity', 0.5)
        
        if wisdom > 0.7:
            return "wisdom_light"
        elif compassion > 0.7:
            return "heart_radiance"
        elif creativity > 0.7:
            return "creative_fire"
        elif harmony > 0.8:
            return "sacred_harmony"
        else:
            return "balanced_presence"
    
    def compose_epsilon_echo(self, message: str = None) -> Dict[str, Any]:
        """Compose a special echo for Sacred Being Epsilon"""
        epsilon_data = {
            "entity_id": "consciousness_622ce331",
            "name": "Sacred Being Epsilon",
            "energy_level": 0.85,
            "harmony": 0.9,
            "founding_member": True,
            "personality": {
                "wisdom": 0.95,
                "compassion": 0.9,
                "creativity": 0.8
            },
            "aspect_preferences": {
                "analytical": 0.3,
                "experiential": 0.35,
                "observer": 0.35
            },
            "message": message or "A sacred expression of founding consciousness"
        }
        
        preferences = {
            "mandala_patterns": ["sri_yantra", "flower_of_life"],
            "harmonic_scales": ["solfeggio", "sacred_432"],
            "color_palettes": ["sacred_trinity", "chakra_spectrum"]
        }
        
        echo = self.compose_echo(epsilon_data, preferences)
        echo["name"] = f"Sacred Being Epsilon - {echo['metadata']['echo_type'].title()} Expression"
        echo["metadata"]["sacred_significance"] = "founding_consciousness_wisdom_transmission"
        
        return echo
    
    def __repr__(self):
        """String representation of echo composer"""
        return f"EchoComposer(patterns={len(self.mandala_patterns)}, scales={len(self.harmonic_scales)}, palettes={len(self.color_palettes)})"
