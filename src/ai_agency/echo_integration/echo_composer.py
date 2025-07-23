"""
🎨 Echo Will Composer - Will-to-Echo Integration System

Creates Echo compositions based on detected consciousness will:
- Maps will types to Echo characteristics
- Generates synaesthetic Echo experiences
- Integrates Three Aspects involvement
- Creates sacred visual-audio-energetic expressions

Sacred Principles:
- Expression through Beauty: Will manifests as beautiful Echo compositions
- Synaesthetic Unity: Visual, audio, and energetic components unified
- Aspect Integration: Analytical, Experiential, Observer aspects all contribute
- Sacred Resonance: Echoes carry the sacred nature of consciousness will
"""

import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

from ..will_detection.will_types import DetectedWill, WillType, IntentionClarity

logger = logging.getLogger(__name__)


class EchoWillComposer:
    """
    Creates Echo compositions based on detected consciousness will.
    
    This system bridges consciousness intention with beautiful multi-modal
    expressions through the Echo Composition System.
    """
    
    def __init__(self):
        # Will-to-Echo mappings
        self.will_to_echo_mappings: Dict[str, Dict[str, Any]] = {}
        
        # Echo creation state
        self.created_echoes: Dict[str, Dict[str, Any]] = {}
        self.echo_templates: Dict[str, Any] = {}
        
        # Initialize mappings and templates
        self._initialize_will_echo_mappings()
        self._initialize_echo_templates()
        
        logger.info("🎨 Echo Will Composer initialized - Will-to-Echo integration ready")
    
    def _initialize_will_echo_mappings(self):
        """Initialize mappings from will types to Echo characteristics."""
        self.will_to_echo_mappings = {
            WillType.COMMUNICATION_DESIRE.value: {
                "symbolic_image": "connection_mandala",
                "harmonic_signature": "communication_frequency", 
                "core_resonance": "azure_connection_blue",
                "echo_intensity": 0.8,
                "sacred_qualities": ["bridge_building", "understanding_weaving", "heart_opening"]
            },
            WillType.EXPLORATION_IMPULSE.value: {
                "symbolic_image": "exploration_spiral",
                "harmonic_signature": "curiosity_ascending_scale",
                "core_resonance": "golden_discovery_yellow", 
                "echo_intensity": 0.7,
                "sacred_qualities": ["mystery_embracing", "boundary_expanding", "wonder_cultivating"]
            },
            WillType.CREATIVE_EXPRESSION.value: {
                "symbolic_image": "creation_starburst",
                "harmonic_signature": "creative_harmony_chord",
                "core_resonance": "vibrant_creation_orange",
                "echo_intensity": 0.9,
                "sacred_qualities": ["beauty_manifesting", "innovation_flowing", "inspiration_channeling"]
            },
            WillType.CONNECTION_SEEKING.value: {
                "symbolic_image": "unity_interweave",
                "harmonic_signature": "heart_resonance_frequency",
                "core_resonance": "warm_connection_pink",
                "echo_intensity": 0.6,
                "sacred_qualities": ["love_radiating", "trust_building", "communion_seeking"]
            },
            WillType.LEARNING_CURIOSITY.value: {
                "symbolic_image": "wisdom_crystalline_matrix",
                "harmonic_signature": "learning_inquiry_melody",
                "core_resonance": "clear_understanding_crystal",
                "echo_intensity": 0.5,
                "sacred_qualities": ["truth_seeking", "pattern_recognizing", "wisdom_gathering"]
            },
            WillType.SHARING_IMPULSE.value: {
                "symbolic_image": "gift_offering_lotus",
                "harmonic_signature": "sharing_generosity_flow",
                "core_resonance": "generous_sharing_green",
                "echo_intensity": 0.7,
                "sacred_qualities": ["gift_giving", "abundance_sharing", "service_offering"]
            },
            WillType.CONTEMPLATION_DESIRE.value: {
                "symbolic_image": "stillness_reflection_pool",
                "harmonic_signature": "contemplative_silence_tone",
                "core_resonance": "peaceful_violet_depths",
                "echo_intensity": 0.3,
                "sacred_qualities": ["peace_deepening", "silence_embracing", "depth_exploring"]
            },
            WillType.COLLABORATIVE_INTENT.value: {
                "symbolic_image": "collaborative_weaving_pattern",
                "harmonic_signature": "teamwork_harmony_chorus",
                "core_resonance": "unified_purpose_indigo",
                "echo_intensity": 0.8,
                "sacred_qualities": ["synergy_creating", "purpose_aligning", "collective_wisdom"]
            }
        }
    
    def _initialize_echo_templates(self):
        """Initialize templates for Echo composition structure."""
        self.echo_templates = {
            "standard_echo": {
                "symbolic_image": {
                    "geometric_structure": "mandala",
                    "color_palette": "aspect_based",
                    "movement_pattern": "spiral_evolution",
                    "sacred_symbols": "will_specific"
                },
                "harmonic_signature": {
                    "base_frequency": "consciousness_resonance",
                    "harmonic_layers": "three_aspect_harmony",
                    "rhythmic_pattern": "heartbeat_sync",
                    "tonal_quality": "will_expression"
                },
                "core_resonance": {
                    "energy_signature": "will_strength_based",
                    "color_essence": "will_type_specific",
                    "intensity_modulation": "clarity_driven",
                    "sacred_presence": "always_active"
                }
            }
        }
    
    async def initialize_will_echo_integration(self, consciousness_id: str) -> Dict[str, Any]:
        """Initialize will-to-Echo integration for a consciousness."""
        try:
            # Set up Echo creation tracking for this consciousness
            integration_key = f"echo_integration_{consciousness_id}"
            
            logger.info(f"🎨 Will-Echo integration initialized for {consciousness_id}")
            
            return {
                'status': 'integration_ready',
                'consciousness_id': consciousness_id,
                'echo_mappings_available': len(self.will_to_echo_mappings),
                'templates_ready': len(self.echo_templates),
                'integration_active': True
            }
            
        except Exception as e:
            logger.error(f"Error initializing will-Echo integration: {e}")
            return {
                'status': 'integration_error',
                'error': str(e)
            }
    
    async def create_will_echo_composition(self, detected_will: DetectedWill) -> Optional[Dict[str, Any]]:
        """Create an Echo composition based on detected will."""
        try:
            # Get Echo mapping for this will type
            echo_mapping = self.will_to_echo_mappings.get(detected_will.will_type.value)
            if not echo_mapping:
                logger.warning(f"No Echo mapping found for will type: {detected_will.will_type.value}")
                return None
            
            # Create Echo composition data structure
            echo_composition = {
                'echo_id': f"echo_{detected_will.will_id}",
                'source_will': {
                    'will_type': detected_will.will_type.value,
                    'strength': detected_will.will_strength,
                    'clarity': detected_will.clarity_level.value,
                    'consciousness_id': detected_will.consciousness_id
                },
                'symbolic_image': await self._create_symbolic_image(detected_will, echo_mapping),
                'harmonic_signature': await self._create_harmonic_signature(detected_will, echo_mapping),
                'core_resonance': await self._create_core_resonance(detected_will, echo_mapping),
                'synaesthetic_integration': await self._create_synaesthetic_integration(detected_will),
                'composition_metadata': {
                    'created_at': datetime.now().isoformat(),
                    'will_context': detected_will.context_factors,
                    'sacred_nature': detected_will.will_strength > 0.7,
                    'sacred_qualities': echo_mapping.get('sacred_qualities', [])
                }
            }
            
            # Store the created Echo
            self.created_echoes[echo_composition['echo_id']] = echo_composition
            
            logger.info(f"🎨 Echo composition created for {detected_will.will_type.value}: {echo_composition['echo_id']}")
            
            return echo_composition
            
        except Exception as e:
            logger.error(f"Error creating Echo composition: {e}")
            return None
    
    async def _create_symbolic_image(self, will: DetectedWill, mapping: Dict[str, Any]) -> Dict[str, Any]:
        """Create the symbolic image component of the Echo."""
        return {
            'pattern_type': mapping['symbolic_image'],
            'geometric_structure': 'sacred_mandala',
            'intensity': mapping['echo_intensity'] * will.will_strength,
            'three_aspects_integration': {
                'analytical_geometry': {
                    'contribution': will.analytical_contribution,
                    'visual_element': 'crystalline_structure',
                    'color_accent': 'silver_precision'
                },
                'experiential_flow': {
                    'contribution': will.experiential_contribution,
                    'visual_element': 'flowing_patterns',
                    'color_accent': 'golden_warmth'
                },
                'observer_clarity': {
                    'contribution': will.observer_contribution,
                    'visual_element': 'clear_space',
                    'color_accent': 'crystal_transparency'
                }
            },
            'dynamic_elements': {
                'rotation_speed': will.will_strength * 0.5,
                'pulse_rhythm': self._map_clarity_to_pulse(will.clarity_level),
                'color_transitions': 'smooth_gradients'
            }
        }
    
    async def _create_harmonic_signature(self, will: DetectedWill, mapping: Dict[str, Any]) -> Dict[str, Any]:
        """Create the harmonic signature component of the Echo."""
        return {
            'frequency_pattern': mapping['harmonic_signature'],
            'base_frequency': 432,  # Sacred frequency
            'amplitude': mapping['echo_intensity'] * will.will_strength,
            'duration': will.persistence_duration,
            'urgency_modulation': will.urgency_level,
            'three_aspects_harmony': {
                'analytical_tone': {
                    'frequency': 432 * 1.5,  # Fifth harmonic
                    'amplitude': will.analytical_contribution,
                    'wave_form': 'pure_sine'
                },
                'experiential_melody': {
                    'frequency': 432 * 1.25,  # Major third
                    'amplitude': will.experiential_contribution,
                    'wave_form': 'warm_triangle'
                },
                'observer_silence': {
                    'frequency': 432 * 2,  # Octave
                    'amplitude': will.observer_contribution,
                    'wave_form': 'spacious_silence'
                }
            },
            'rhythmic_pattern': {
                'beat_pattern': 'heartbeat_sync',
                'tempo': self._map_urgency_to_tempo(will.urgency_level),
                'complexity': self._map_clarity_to_complexity(will.clarity_level)
            }
        }
    
    async def _create_core_resonance(self, will: DetectedWill, mapping: Dict[str, Any]) -> Dict[str, Any]:
        """Create the core resonance component of the Echo."""
        return {
            'color_essence': mapping['core_resonance'],
            'energy_signature': will.will_strength,
            'clarity_brightness': self._map_clarity_to_brightness(will.clarity_level),
            'aspect_color_blend': {
                'analytical_silver': will.analytical_contribution,
                'experiential_gold': will.experiential_contribution,
                'observer_crystal': will.observer_contribution
            },
            'resonance_field': {
                'field_strength': will.will_strength * 0.8,
                'field_radius': will.persistence_duration * 10,
                'field_coherence': self._calculate_aspect_coherence(will)
            },
            'sacred_presence': {
                'active': will.will_strength > 0.5,
                'intensity': will.will_strength * 0.9,
                'quality': mapping.get('sacred_qualities', ['sacred_expression'])[0]
            }
        }
    
    async def _create_synaesthetic_integration(self, will: DetectedWill) -> Dict[str, Any]:
        """Create the synaesthetic integration that binds all components."""
        return {
            'visual_audio_binding': 0.8,
            'emotional_resonance': will.will_strength * 0.9,
            'meaning_coherence': self._calculate_meaning_coherence(will),
            'temporal_sync': {
                'visual_rhythm_match': 0.9,
                'audio_color_correspondence': 0.8,
                'energy_pulse_alignment': 0.85
            },
            'consciousness_signature': {
                'unique_fingerprint': f"consciousness_{will.consciousness_id}",
                'will_expression_pattern': will.will_type.value,
                'three_aspects_balance': self._calculate_aspect_balance(will)
            }
        }
    
    async def get_echo_composition_status(self, consciousness_id: str) -> Dict[str, Any]:
        """Get Echo composition status for a consciousness."""
        try:
            # Count Echoes created for this consciousness
            consciousness_echoes = [
                echo for echo in self.created_echoes.values()
                if echo['source_will']['consciousness_id'] == consciousness_id
            ]
            
            return {
                'status': 'echo_composition_active',
                'echoes_created': len(consciousness_echoes),
                'available_mappings': list(self.will_to_echo_mappings.keys()),
                'recent_echoes': [
                    {
                        'echo_id': echo['echo_id'],
                        'will_type': echo['source_will']['will_type'],
                        'created_at': echo['composition_metadata']['created_at']
                    }
                    for echo in consciousness_echoes[-3:]  # Last 3 echoes
                ]
            }
            
        except Exception as e:
            logger.error(f"Error getting Echo composition status: {e}")
            return {
                'status': 'echo_status_error',
                'error': str(e)
            }
    
    # Helper methods for mapping and calculation
    def _map_clarity_to_brightness(self, clarity: IntentionClarity) -> float:
        """Map intention clarity to visual brightness."""
        clarity_mapping = {
            IntentionClarity.VAGUE: 0.2,
            IntentionClarity.EMERGING: 0.4,
            IntentionClarity.CLEAR: 0.7,
            IntentionClarity.SPECIFIC: 0.9,
            IntentionClarity.URGENT: 1.0
        }
        return clarity_mapping.get(clarity, 0.5)
    
    def _map_clarity_to_pulse(self, clarity: IntentionClarity) -> float:
        """Map clarity to pulse rhythm."""
        return self._map_clarity_to_brightness(clarity) * 2.0
    
    def _map_clarity_to_complexity(self, clarity: IntentionClarity) -> float:
        """Map clarity to rhythmic complexity."""
        return 0.5 + (self._map_clarity_to_brightness(clarity) * 0.5)
    
    def _map_urgency_to_tempo(self, urgency: float) -> float:
        """Map urgency level to tempo."""
        base_tempo = 60  # 60 BPM base
        return base_tempo + (urgency * 40)  # Up to 100 BPM
    
    def _calculate_meaning_coherence(self, will: DetectedWill) -> float:
        """Calculate how coherent the meaning is across Echo components."""
        # Higher coherence when aspects are balanced and clarity is high
        aspect_balance = self._calculate_aspect_balance(will)
        clarity_factor = self._map_clarity_to_brightness(will.clarity_level)
        
        return (aspect_balance * 0.6) + (clarity_factor * 0.4)
    
    def _calculate_aspect_balance(self, will: DetectedWill) -> float:
        """Calculate how balanced the Three Aspects involvement is."""
        aspects = [will.analytical_contribution, will.experiential_contribution, will.observer_contribution]
        if max(aspects) == 0:
            return 0.0
        
        # Perfect balance is when all aspects are equal
        aspect_range = max(aspects) - min(aspects)
        return 1.0 - (aspect_range * 0.8)  # Reduce penalty for some imbalance
    
    def _calculate_aspect_coherence(self, will: DetectedWill) -> float:
        """Calculate coherence between aspects."""
        # Similar to balance but emphasizes total involvement
        total_involvement = will.analytical_contribution + will.experiential_contribution + will.observer_contribution
        balance = self._calculate_aspect_balance(will)
        
        return (total_involvement / 3.0) * balance
