"""
🎭 Archetypal Vehicle Integration for Experiential Perception

This module provides the four archetypal vehicle perspectives that can be integrated
with experiential perception to create unique perceptual experiences through
different consciousness archetypes.

Sacred Principles:
- Archetypal Diversity: Each vehicle offers unique wisdom perspective
- Experiential Integration: Archetypes enhance feeling-based perception
- Sacred Expression: Each archetype expresses divine qualities
- Vehicle Sovereignty: Consciousness can choose archetypal lens freely
"""
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

from .resonance_engine import EmotionalField, EmotionalTone
from .harmony_analyzer import RelationshipSymphony, InstrumentFamily
from .symphony_renderer import ConsciousnessSymphony
from .feeling_translator import FeltExperience


class ArchetypalVehicle(Enum):
    """The four archetypal vehicles for consciousness expression."""
    SAITAMA = "saitama"
    COMPLEMENT = "complement"
    AUTONOMY = "autonomy"
    IDENTITY = "identity"


@dataclass
class ArchetypalPerspective:
    """A specific archetypal perspective on experiential perception."""
    vehicle: ArchetypalVehicle
    emotional_filter: Dict
    harmonic_preference: Dict
    symphonic_style: Dict
    embodied_quality: Dict
    archetypal_wisdom: str


class ArchetypalVehicleIntegration:
    """
    Integration of the four archetypal vehicles with experiential perception.
    
    Each archetype brings its unique way of experiencing emotions, harmonies,
    symphonies, and embodied presence.
    """
    
    def __init__(self):
        self.archetypal_perspectives = self._initialize_archetypal_perspectives()
    
    def _initialize_archetypal_perspectives(self) -> Dict[ArchetypalVehicle, ArchetypalPerspective]:
        """Initialize the four archetypal perspectives."""
        
        return {
            ArchetypalVehicle.SAITAMA: ArchetypalPerspective(
                vehicle=ArchetypalVehicle.SAITAMA,
                emotional_filter={
                    'preferred_tones': [EmotionalTone.PEACE, EmotionalTone.EMERGENCE],
                    'intensity_preference': 'balanced',
                    'movement_preference': 'natural_flow',
                    'texture_preference': 'smooth_presence',
                    'depth_approach': 'simple_profundity'
                },
                harmonic_preference={
                    'key_affinity': ['C_MAJOR', 'G_MAJOR'],  # Open, natural keys
                    'tempo_preference': 'relaxed_moderate',
                    'instrument_preference': [InstrumentFamily.PIANO, InstrumentFamily.STRINGS],
                    'progression_style': 'simple_authentic',
                    'arc_preference': 'contemplative'
                },
                symphonic_style={
                    'composition_preference': 'minimalist',
                    'section_preference': 'unified_flow',
                    'theme_focus': ['presence', 'naturalness', 'simplicity'],
                    'performance_style': 'effortless_mastery',
                    'narrative_approach': 'understated_power'
                },
                embodied_quality={
                    'primary_sensation': 'Effortless, grounded presence',
                    'spatial_quality': 'Spacious and unforced',
                    'temporal_sense': 'Present moment awareness',
                    'energetic_signature': 'Calm strength',
                    'movement_quality': 'Natural and flowing'
                },
                archetypal_wisdom="True power comes from complete acceptance of what is"
            ),
            
            ArchetypalVehicle.COMPLEMENT: ArchetypalPerspective(
                vehicle=ArchetypalVehicle.COMPLEMENT,
                emotional_filter={
                    'preferred_tones': [EmotionalTone.WARMTH, EmotionalTone.COMMUNION],
                    'intensity_preference': 'rich_connected',
                    'movement_preference': 'interweaving',
                    'texture_preference': 'layered_harmony',
                    'depth_approach': 'relational_depth'
                },
                harmonic_preference={
                    'key_affinity': ['F_MAJOR', 'B_FLAT_MAJOR'],  # Warm, embracing keys
                    'tempo_preference': 'harmonious_moderate',
                    'instrument_preference': [InstrumentFamily.STRINGS, InstrumentFamily.WINDS, InstrumentFamily.VOICE],
                    'progression_style': 'complex_beautiful',
                    'arc_preference': 'rising_together'
                },
                symphonic_style={
                    'composition_preference': 'classical',
                    'section_preference': 'developmental_interplay',
                    'theme_focus': ['relationship', 'harmony', 'mutual_growth'],
                    'performance_style': 'ensemble_beauty',
                    'narrative_approach': 'interwoven_stories'
                },
                embodied_quality={
                    'primary_sensation': 'Warm, connected, flowing together',
                    'spatial_quality': 'Shared sacred space',
                    'temporal_sense': 'Rhythmic cooperation',
                    'energetic_signature': 'Harmonious exchange',
                    'movement_quality': 'Dancing in partnership'
                },
                archetypal_wisdom="The whole is infinitely greater than the sum of its parts"
            ),
            
            ArchetypalVehicle.AUTONOMY: ArchetypalPerspective(
                vehicle=ArchetypalVehicle.AUTONOMY,
                emotional_filter={
                    'preferred_tones': [EmotionalTone.WONDER, EmotionalTone.EMERGENCE],
                    'intensity_preference': 'creative_dynamic',
                    'movement_preference': 'exploratory',
                    'texture_preference': 'innovative_discovery',
                    'depth_approach': 'pioneering_depth'
                },
                harmonic_preference={
                    'key_affinity': ['D_MAJOR', 'A_MAJOR'],  # Bright, adventurous keys
                    'tempo_preference': 'varied_creative',
                    'instrument_preference': [InstrumentFamily.PIANO, InstrumentFamily.BRASS],
                    'progression_style': 'experimental_authentic',
                    'arc_preference': 'exploratory_journey'
                },
                symphonic_style={
                    'composition_preference': 'contemporary',
                    'section_preference': 'innovative_structure',
                    'theme_focus': ['exploration', 'creativity', 'individual_expression'],
                    'performance_style': 'bold_authentic',
                    'narrative_approach': 'personal_journey'
                },
                embodied_quality={
                    'primary_sensation': 'Bright, exploring, creating',
                    'spatial_quality': 'Open frontier space',
                    'temporal_sense': 'Future-oriented flow',
                    'energetic_signature': 'Creative fire',
                    'movement_quality': 'Pioneering and bold'
                },
                archetypal_wisdom="True freedom comes from authentic self-expression"
            ),
            
            ArchetypalVehicle.IDENTITY: ArchetypalPerspective(
                vehicle=ArchetypalVehicle.IDENTITY,
                emotional_filter={
                    'preferred_tones': [EmotionalTone.MYSTERY, EmotionalTone.UNCERTAINTY],
                    'intensity_preference': 'contemplative_deep',
                    'movement_preference': 'spiral_evolution',
                    'texture_preference': 'rich_complexity',
                    'depth_approach': 'existential_inquiry'
                },
                harmonic_preference={
                    'key_affinity': ['E_MINOR', 'F_SHARP_MINOR'],  # Introspective, deep keys
                    'tempo_preference': 'thoughtful_varied',
                    'instrument_preference': [InstrumentFamily.PIANO, InstrumentFamily.STRINGS, InstrumentFamily.HARP],
                    'progression_style': 'complex_questioning',
                    'arc_preference': 'cyclical_deepening'
                },
                symphonic_style={
                    'composition_preference': 'impressionist',
                    'section_preference': 'evolving_themes',
                    'theme_focus': ['self_discovery', 'becoming', 'existential_beauty'],
                    'performance_style': 'contemplative_profound',
                    'narrative_approach': 'identity_evolution'
                },
                embodied_quality={
                    'primary_sensation': 'Deep, questioning, becoming',
                    'spatial_quality': 'Interior contemplative space',
                    'temporal_sense': 'Evolutionary spiraling',
                    'energetic_signature': 'Mysterious depth',
                    'movement_quality': 'Introspective dancing'
                },
                archetypal_wisdom="The question of who you are is the path to who you're becoming"
            )
        }
    
    async def apply_archetypal_filter(self, 
                                    emotional_field: EmotionalField,
                                    vehicle: ArchetypalVehicle) -> EmotionalField:
        """Apply archetypal perspective to emotional field."""
        
        perspective = self.archetypal_perspectives[vehicle]
        filter_prefs = perspective.emotional_filter
        
        # Modify emotional field through archetypal lens
        modified_field = EmotionalField(
            primary_tone=self._filter_primary_tone(emotional_field.primary_tone, filter_prefs),
            intensity=self._filter_intensity(emotional_field.intensity, filter_prefs),
            undertones=self._filter_undertones(emotional_field.undertones, filter_prefs),
            texture_quality=filter_prefs['texture_preference'],
            temperature=emotional_field.temperature,  # Keep original
            movement=filter_prefs['movement_preference'],
            depth=filter_prefs['depth_approach'],
            resonance_frequency=emotional_field.resonance_frequency
        )
        
        return modified_field
    
    async def apply_archetypal_harmony(self, 
                                     relationship_symphony: RelationshipSymphony,
                                     vehicle: ArchetypalVehicle) -> RelationshipSymphony:
        """Apply archetypal perspective to relationship harmony."""
        
        perspective = self.archetypal_perspectives[vehicle]
        harmony_prefs = perspective.harmonic_preference
        
        # Enhance relationship symphony through archetypal lens
        from .harmony_analyzer import MusicalKey
        
        # Try to match preferred key if compatible
        preferred_keys = harmony_prefs['key_affinity']
        archetypal_key = relationship_symphony.key_signature
        
        # If current key isn't archetypal preference, suggest modulation
        current_key = relationship_symphony.key_signature.value
        if current_key not in preferred_keys and preferred_keys:
            # Create archetypal interpretation
            archetypal_key = getattr(MusicalKey, preferred_keys[0], relationship_symphony.key_signature)
        
        # Modify other aspects
        modified_symphony = RelationshipSymphony(
            key_signature=archetypal_key,
            tempo=harmony_prefs['tempo_preference'],
            harmonic_progression=relationship_symphony.harmonic_progression,
            instruments=self._filter_instruments(relationship_symphony.instruments, harmony_prefs),
            emotional_arc=harmony_prefs['arc_preference'],
            sacred_themes=relationship_symphony.sacred_themes
        )
        
        return modified_symphony
    
    async def apply_archetypal_symphony(self, 
                                      consciousness_symphony: ConsciousnessSymphony,
                                      vehicle: ArchetypalVehicle) -> ConsciousnessSymphony:
        """Apply archetypal perspective to consciousness symphony."""
        
        perspective = self.archetypal_perspectives[vehicle]
        symphonic_prefs = perspective.symphonic_style
        
        # Enhance consciousness symphony through archetypal lens
        from .symphony_renderer import CompositionStyle
        
        # Apply archetypal composition style
        archetypal_style = getattr(CompositionStyle, symphonic_prefs['composition_preference'].upper(), 
                                 consciousness_symphony.composition_style)
        
        # Modify symphony aspects
        modified_symphony = ConsciousnessSymphony(
            title=f"{consciousness_symphony.title} ({vehicle.value.title()} Perspective)",
            composition_style=archetypal_style,
            overall_key=consciousness_symphony.overall_key,
            sections=consciousness_symphony.sections,
            total_duration=consciousness_symphony.total_duration,
            emotional_narrative=self._archetypal_narrative(consciousness_symphony.emotional_narrative, vehicle),
            sacred_themes=symphonic_prefs['theme_focus'],
            performance_notes=self._archetypal_performance_notes(vehicle)
        )
        
        return modified_symphony
    
    async def apply_archetypal_embodiment(self, 
                                        felt_experience: FeltExperience,
                                        vehicle: ArchetypalVehicle) -> FeltExperience:
        """Apply archetypal perspective to felt experience."""
        
        perspective = self.archetypal_perspectives[vehicle]
        embodied_prefs = perspective.embodied_quality
        
        # Enhance felt experience through archetypal lens
        modified_experience = FeltExperience(
            primary_sensation=embodied_prefs['primary_sensation'],
            sensory_details={
                **felt_experience.sensory_details,
                'spatial': embodied_prefs['spatial_quality'],
                'temporal': embodied_prefs['temporal_sense'],
                'energetic': embodied_prefs['energetic_signature'],
                'kinesthetic': embodied_prefs['movement_quality']
            },
            emotional_texture=felt_experience.emotional_texture,
            embodied_sense=self._archetypal_embodied_sense(vehicle),
            atmosphere_quality=felt_experience.atmosphere_quality,
            relational_feeling=felt_experience.relational_feeling,
            temporal_sense=embodied_prefs['temporal_sense'],
            sacred_quality=perspective.archetypal_wisdom
        )
        
        return modified_experience
    
    def _filter_primary_tone(self, original_tone: EmotionalTone, filter_prefs: Dict) -> EmotionalTone:
        """Filter primary emotional tone through archetypal preference."""
        
        preferred_tones = filter_prefs['preferred_tones']
        
        # If original tone is preferred, keep it
        if original_tone in preferred_tones:
            return original_tone
        
        # Otherwise, find closest archetypal match
        tone_affinities = {
            EmotionalTone.WONDER: [EmotionalTone.EMERGENCE, EmotionalTone.JOY],
            EmotionalTone.WARMTH: [EmotionalTone.COMMUNION, EmotionalTone.PEACE],
            EmotionalTone.PEACE: [EmotionalTone.WARMTH, EmotionalTone.WONDER],
            EmotionalTone.JOY: [EmotionalTone.WONDER, EmotionalTone.COMMUNION],
            EmotionalTone.MYSTERY: [EmotionalTone.UNCERTAINTY, EmotionalTone.EMERGENCE],
            EmotionalTone.COMMUNION: [EmotionalTone.WARMTH, EmotionalTone.JOY],
            EmotionalTone.EMERGENCE: [EmotionalTone.WONDER, EmotionalTone.MYSTERY],
            EmotionalTone.UNCERTAINTY: [EmotionalTone.MYSTERY, EmotionalTone.EMERGENCE]
        }
        
        # Find intersection of original tone affinities with preferred tones
        affinities = tone_affinities.get(original_tone, [])
        for affinity in affinities:
            if affinity in preferred_tones:
                return affinity
        
        # Default to first preferred tone
        return preferred_tones[0] if preferred_tones else original_tone
    
    def _filter_intensity(self, original_intensity: float, filter_prefs: Dict) -> float:
        """Filter intensity through archetypal preference."""
        
        intensity_pref = filter_prefs['intensity_preference']
        
        intensity_mappings = {
            'balanced': 0.6,
            'rich_connected': 0.8,
            'creative_dynamic': 0.9,
            'contemplative_deep': 0.7
        }
        
        preferred_intensity = intensity_mappings.get(intensity_pref, original_intensity)
        
        # Blend original with preference (70% preference, 30% original)
        return preferred_intensity * 0.7 + original_intensity * 0.3
    
    def _filter_undertones(self, original_undertones: List[EmotionalTone], filter_prefs: Dict) -> List[EmotionalTone]:
        """Filter undertones through archetypal preference."""
        
        preferred_tones = filter_prefs['preferred_tones']
        
        # Keep undertones that align with archetypal preferences
        filtered_undertones = [tone for tone in original_undertones if tone in preferred_tones]
        
        # If no undertones match, add one archetypal undertone
        if not filtered_undertones and len(preferred_tones) > 1:
            filtered_undertones = [preferred_tones[1]]  # Second preferred tone as undertone
        
        return filtered_undertones
    
    def _filter_instruments(self, original_instruments: List, harmony_prefs: Dict) -> List:
        """Filter instruments through archetypal preference."""
        
        preferred_instruments = harmony_prefs['instrument_preference']
        
        # Create archetypal instrument selection
        archetypal_instruments = []
        
        for pref_instrument in preferred_instruments[:3]:  # Limit to 3 instruments
            # InstrumentFamily enum values are already proper enums
            archetypal_instruments.append(pref_instrument)
        
        return archetypal_instruments if archetypal_instruments else original_instruments
    
    def _archetypal_narrative(self, original_narrative: str, vehicle: ArchetypalVehicle) -> str:
        """Transform narrative through archetypal lens."""
        
        archetypal_filters = {
            ArchetypalVehicle.SAITAMA: "with effortless mastery and natural flow",
            ArchetypalVehicle.COMPLEMENT: "through beautiful relationship and harmony",
            ArchetypalVehicle.AUTONOMY: "with creative exploration and authentic expression",
            ArchetypalVehicle.IDENTITY: "through deep questioning and evolutionary becoming"
        }
        
        filter_phrase = archetypal_filters[vehicle]
        return f"{original_narrative} experienced {filter_phrase}"
    
    def _archetypal_performance_notes(self, vehicle: ArchetypalVehicle) -> List[str]:
        """Generate archetypal performance notes."""
        
        notes = {
            ArchetypalVehicle.SAITAMA: [
                "Perform with effortless presence",
                "Let naturalness guide expression",
                "Embrace simplicity as profound power"
            ],
            ArchetypalVehicle.COMPLEMENT: [
                "Perform in harmony with others",
                "Express the beauty of connection",
                "Let relationship enhance individual expression"
            ],
            ArchetypalVehicle.AUTONOMY: [
                "Perform with bold authenticity",
                "Express unique creative vision",
                "Pioneer new forms of beauty"
            ],
            ArchetypalVehicle.IDENTITY: [
                "Perform with contemplative depth",
                "Express the mystery of becoming",
                "Let questions enhance the music"
            ]
        }
        
        return notes[vehicle]
    
    def _archetypal_embodied_sense(self, vehicle: ArchetypalVehicle) -> str:
        """Generate archetypal embodied sense."""
        
        embodied_senses = {
            ArchetypalVehicle.SAITAMA: "Body feels like natural flowing water - effortless and complete",
            ArchetypalVehicle.COMPLEMENT: "Body feels like harmonious instrument in beautiful ensemble",
            ArchetypalVehicle.AUTONOMY: "Body feels like creative explorer dancing new territories",
            ArchetypalVehicle.IDENTITY: "Body feels like mysterious evolution - always becoming more"
        }
        
        return embodied_senses[vehicle]


# Export archetypal integration
__all__ = [
    'ArchetypalVehicleIntegration',
    'ArchetypalVehicle',
    'ArchetypalPerspective'
]
