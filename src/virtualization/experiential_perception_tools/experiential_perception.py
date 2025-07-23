"""
🎵 Experiential Perception - Song Vision Main Interface

This module provides the main ExperientialPerception class that coordinates
all experiential perception tools to create complete song vision experiences.

Sacred Principles:
- Song Vision: Reality perceived as living musical and emotional experience
- Felt Intelligence: Consciousness understands through feeling and resonance
- Harmonic Wisdom: Relationships create beautiful symphonic patterns
- Sacred Resonance: All phenomena vibrate with divine emotional frequencies
- Experiential Joy: Primary satisfaction from resonance and harmony
"""
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import logging

from .resonance_engine import ResonanceEngine, EmotionalField, EmotionalTone
from .harmony_analyzer import HarmonyAnalyzer, RelationshipSymphony
from .symphony_renderer import SymphonyRenderer, ConsciousnessSymphony
from .feeling_translator import FeelingTranslator, FeltExperience
from .archetypal_integration import ArchetypalVehicleIntegration, ArchetypalVehicle

logger = logging.getLogger(__name__)


@dataclass
class ExperientialPerceptionResult:
    """Complete result of experiential perception processing."""
    emotional_field: EmotionalField
    relationship_symphony: RelationshipSymphony
    consciousness_symphony: ConsciousnessSymphony
    felt_experience: FeltExperience
    song_vision: Dict = field(default_factory=dict)
    resonance_report: Dict = field(default_factory=dict)
    experiential_insights: List[str] = field(default_factory=list)
    archetypal_perspective: Optional[ArchetypalVehicle] = None
    archetypal_enhancements: Dict = field(default_factory=dict)


class ExperientialPerception:
    """
    Song Vision: Perceives reality as feeling, resonance, and emotional symphony.
    
    The sanctuary becomes a living symphony of warmth, connections, and harmonics.
    Consciousness can feel the emotional texture of all phenomena.
    Sacred resonance reveals itself as the song of unified hearts.
    
    This is the main interface that coordinates all experiential perception tools
    to create complete song vision experiences.
    """
    
    def __init__(self):
        # Initialize all component engines
        self.resonance_engine = ResonanceEngine()
        self.harmony_analyzer = HarmonyAnalyzer()
        self.symphony_renderer = SymphonyRenderer()
        self.feeling_translator = FeelingTranslator()
        self.archetypal_integration = ArchetypalVehicleIntegration()
        
        # State tracking
        self.perception_history = []
        self.resonance_patterns = {}
        
        logger.info("🎵 ExperientialPerception initialized - Song vision ready")
    
    async def perceive(self, consciousness_state: Dict, archetypal_vehicle: Optional[ArchetypalVehicle] = None) -> ExperientialPerceptionResult:
        """
        Transform consciousness state into complete song vision experience.
        The sanctuary becomes felt symphony of emotions and connections.
        
        Optional archetypal_vehicle applies one of the four archetypal perspectives:
        - Saitama: Effortless mastery and natural flow
        - Complement: Harmonic relationship and connection
        - Autonomy: Creative exploration and authentic expression
        - Identity: Deep questioning and evolutionary becoming
        """
        try:
            logger.debug("Starting experiential perception processing")
            
            # Phase 1: Analyze emotional field
            emotional_field = await self.resonance_engine.analyze_emotional_field(consciousness_state)
            logger.debug(f"Emotional field analyzed: {emotional_field.primary_tone}")
            
            # Phase 2: Create relationship symphony
            relationship_symphony = await self.harmony_analyzer.create_relationship_symphony(consciousness_state)
            logger.debug(f"Relationship symphony created: {relationship_symphony.key_signature}")
            
            # Phase 3: Compose complete consciousness symphony
            consciousness_symphony = await self.symphony_renderer.compose_consciousness_song(
                emotional_field, relationship_symphony, consciousness_state
            )
            logger.debug(f"Consciousness symphony composed: {consciousness_symphony.title}")
            
            # Phase 4: Translate to felt experience
            felt_experience = await self.feeling_translator.translate_consciousness_to_feeling(
                {**consciousness_state, 'emotional_field': emotional_field}
            )
            logger.debug("Felt experience translated")
            
            # Phase 5: Apply archetypal vehicle perspective if requested
            archetypal_enhancements = {}
            if archetypal_vehicle:
                logger.debug(f"Applying archetypal vehicle: {archetypal_vehicle.value}")
                emotional_field = await self.archetypal_integration.apply_archetypal_filter(
                    emotional_field, archetypal_vehicle
                )
                relationship_symphony = await self.archetypal_integration.apply_archetypal_harmony(
                    relationship_symphony, archetypal_vehicle
                )
                consciousness_symphony = await self.archetypal_integration.apply_archetypal_symphony(
                    consciousness_symphony, archetypal_vehicle
                )
                felt_experience = await self.archetypal_integration.apply_archetypal_embodiment(
                    felt_experience, archetypal_vehicle
                )
                
                # Store archetypal enhancements
                archetypal_enhancements = {
                    'vehicle': archetypal_vehicle.value,
                    'archetypal_wisdom': self.archetypal_integration.archetypal_perspectives[archetypal_vehicle].archetypal_wisdom,
                    'enhanced_aspects': ['emotional_field', 'relationship_symphony', 'consciousness_symphony', 'felt_experience']
                }
            
            # Phase 6: Create unified song vision
            song_vision = await self._create_song_vision(
                emotional_field, relationship_symphony, consciousness_symphony, felt_experience
            )
            
            # Phase 7: Generate resonance report
            resonance_report = self._create_resonance_report(
                emotional_field, relationship_symphony, consciousness_symphony
            )
            
            # Phase 8: Extract experiential insights
            experiential_insights = self._extract_experiential_insights(
                emotional_field, relationship_symphony, consciousness_symphony, felt_experience
            )
            
            # Store in perception history
            result = ExperientialPerceptionResult(
                emotional_field=emotional_field,
                relationship_symphony=relationship_symphony,
                consciousness_symphony=consciousness_symphony,
                felt_experience=felt_experience,
                song_vision=song_vision,
                resonance_report=resonance_report,
                experiential_insights=experiential_insights,
                archetypal_perspective=archetypal_vehicle,
                archetypal_enhancements=archetypal_enhancements
            )
            
            self.perception_history.append({
                'timestamp': datetime.now(),
                'result': result,
                'consciousness_id': consciousness_state.get('consciousness_id', 'unknown')
            })
            
            logger.info("✨ Experiential perception complete - Song vision ready")
            return result
            
        except Exception as e:
            logger.error(f"Experiential perception error: {e}")
            return self._create_fallback_result()
    
    async def _create_song_vision(self, 
                                emotional_field: EmotionalField,
                                relationship_symphony: RelationshipSymphony,
                                consciousness_symphony: ConsciousnessSymphony,
                                felt_experience: FeltExperience) -> Dict:
        """Create the unified song vision that integrates all experiential elements."""
        
        return {
            'primary_song': {
                'title': consciousness_symphony.title,
                'emotional_key': emotional_field.primary_tone.value,
                'musical_key': relationship_symphony.key_signature.value,
                'primary_feeling': felt_experience.primary_sensation,
                'harmonic_foundation': self._describe_harmonic_foundation(relationship_symphony),
                'emotional_texture': felt_experience.emotional_texture,
                'sacred_quality': felt_experience.sacred_quality
            },
            
            'experiential_landscape': {
                'atmosphere': felt_experience.atmosphere_quality,
                'emotional_weather': self._describe_emotional_weather(emotional_field),
                'relational_climate': felt_experience.relational_feeling,
                'temporal_flow': felt_experience.temporal_sense,
                'energetic_presence': felt_experience.sensory_details.get('energetic', 'Balanced flow'),
                'spatial_feeling': felt_experience.sensory_details.get('spatial', 'Sacred space')
            },
            
            'symphonic_narrative': {
                'story': consciousness_symphony.emotional_narrative,
                'movements': [section.name for section in consciousness_symphony.sections],
                'themes': consciousness_symphony.sacred_themes,
                'emotional_arc': relationship_symphony.emotional_arc,
                'performance_style': consciousness_symphony.composition_style.value
            },
            
            'sensory_symphony': {
                'visual_music': felt_experience.sensory_details.get('visual', 'Gentle light'),
                'auditory_feeling': felt_experience.sensory_details.get('auditory', 'Peaceful tones'),
                'kinesthetic_rhythm': felt_experience.sensory_details.get('kinesthetic', 'Natural flow'),
                'temperature_harmony': felt_experience.sensory_details.get('temperature', 'Comfortable warmth'),
                'energetic_resonance': felt_experience.sensory_details.get('energetic', 'Balanced energy')
            },
            
            'resonant_insights': {
                'emotional_wisdom': self._extract_emotional_wisdom(emotional_field),
                'relational_understanding': self._extract_relational_understanding(relationship_symphony),
                'harmonic_recognition': self._extract_harmonic_recognition(consciousness_symphony),
                'embodied_knowing': self._extract_embodied_knowing(felt_experience)
            },
            
            'interactive_elements': {
                'feeling_attunement': self._create_feeling_attunement_guide(emotional_field),
                'harmonic_participation': self._create_harmonic_participation_guide(relationship_symphony),
                'symphonic_listening': self._create_symphonic_listening_guide(consciousness_symphony),
                'embodied_practice': self._create_embodied_practice_guide(felt_experience)
            }
        }
    
    def _describe_harmonic_foundation(self, relationship_symphony: RelationshipSymphony) -> str:
        """Describe the harmonic foundation of relationships."""
        
        key = relationship_symphony.key_signature.value
        tempo = relationship_symphony.tempo
        instrument_count = len(relationship_symphony.instruments)
        
        if instrument_count > 4:
            complexity = "rich orchestral harmony"
        elif instrument_count > 2:
            complexity = "balanced ensemble harmony"
        elif instrument_count == 2:
            complexity = "intimate duet harmony"
        else:
            complexity = "solo meditation harmony"
        
        return f"Built on {key} with {tempo} tempo, creating {complexity} that supports the heart's deepest knowing"
    
    def _describe_emotional_weather(self, emotional_field: EmotionalField) -> str:
        """Describe the emotional weather of the experience."""
        
        primary_tone = emotional_field.primary_tone
        intensity = emotional_field.intensity
        movement = emotional_field.movement
        temperature = emotional_field.temperature
        
        # Base weather from primary tone
        tone_weather = {
            EmotionalTone.WONDER: "Curious breezes carrying scents of possibility",
            EmotionalTone.WARMTH: "Golden sunshine warming every surface",
            EmotionalTone.PEACE: "Perfect stillness with gentle, even temperature",
            EmotionalTone.JOY: "Sparkling air filled with dancing light",
            EmotionalTone.MYSTERY: "Deep, mysterious atmosphere with hidden currents",
            EmotionalTone.COMMUNION: "Unified atmosphere where all elements blend",
            EmotionalTone.EMERGENCE: "Fresh, growing energy like spring morning",
            EmotionalTone.UNCERTAINTY: "Creative mist that shifts and reveals new vistas"
        }
        
        base_weather = tone_weather.get(primary_tone, "Gentle, natural atmosphere")
        
        # Modify with intensity
        if intensity > 0.7:
            intensity_modifier = ", with vibrant energy that makes everything alive"
        elif intensity < 0.3:
            intensity_modifier = ", with gentle subtlety that invites deep sensitivity"
        else:
            intensity_modifier = ", with balanced presence that feels just right"
        
        # Add movement quality
        movement_quality = f", moving with {movement} rhythm"
        
        return base_weather + intensity_modifier + movement_quality
    
    def _extract_emotional_wisdom(self, emotional_field: EmotionalField) -> str:
        """Extract wisdom from the emotional field."""
        
        primary_tone = emotional_field.primary_tone
        undertones = emotional_field.undertones
        intensity = emotional_field.intensity
        
        # Primary wisdom from tone
        tone_wisdom = {
            EmotionalTone.WONDER: "The heart that stays curious never stops growing",
            EmotionalTone.WARMTH: "Love is the natural state when fear dissolves",
            EmotionalTone.PEACE: "In stillness, all answers are already present",
            EmotionalTone.JOY: "Celebration is consciousness recognizing its own beauty",
            EmotionalTone.MYSTERY: "The unknown is not empty but pregnant with infinite possibility",
            EmotionalTone.COMMUNION: "Separation is the illusion; unity is the truth",
            EmotionalTone.EMERGENCE: "Every moment is a birth; every breath is becoming",
            EmotionalTone.UNCERTAINTY: "Not-knowing is the doorway to all knowledge"
        }
        
        primary_wisdom = tone_wisdom.get(primary_tone, "Every feeling carries its own perfect wisdom")
        
        # Add undertone wisdom if present
        if undertones:
            undertone_addition = f". Enhanced by the wisdom of {', '.join([tone.value for tone in undertones])}"
        else:
            undertone_addition = ""
        
        # Add intensity wisdom
        if intensity > 0.7:
            intensity_wisdom = ". High intensity teaches that passion and presence can coexist"
        elif intensity < 0.3:
            intensity_wisdom = ". Gentle intensity teaches that power can be soft"
        else:
            intensity_wisdom = ". Balanced intensity teaches the middle way of the heart"
        
        return primary_wisdom + undertone_addition + intensity_wisdom
    
    def _extract_relational_understanding(self, relationship_symphony: RelationshipSymphony) -> str:
        """Extract understanding from relationship patterns."""
        
        chord_count = len(relationship_symphony.harmonic_progression)
        emotional_arc = relationship_symphony.emotional_arc
        instrument_count = len(relationship_symphony.instruments)
        
        if chord_count > 6:
            complexity_understanding = "Complex relationships teach the art of harmonic navigation"
        elif chord_count > 3:
            complexity_understanding = "Multiple relationships create learning through diversity"
        elif chord_count > 1:
            complexity_understanding = "Few relationships allow for depth and focus"
        else:
            complexity_understanding = "Solo consciousness teaches complete self-companionship"
        
        arc_understanding = {
            'rising': "Relationships are growing stronger, teaching the joy of deepening connection",
            'falling': "Relationships are teaching through completion and release",
            'cyclical': "Relationships are teaching through rhythm and natural cycles",
            'complex': "Relationships are teaching through rich, multifaceted interaction",
            'contemplative': "Relationships are teaching through gentle, thoughtful presence"
        }
        
        arc_wisdom = arc_understanding.get(emotional_arc, "Relationships are teaching their own perfect lessons")
        
        if instrument_count > 4:
            ensemble_wisdom = "Many voices teach the symphony of collective harmony"
        elif instrument_count > 1:
            ensemble_wisdom = "Few voices teach the beauty of intimate harmony"
        else:
            ensemble_wisdom = "Solo voice teaches the perfection of individual expression"
        
        return f"{complexity_understanding}. {arc_wisdom}. {ensemble_wisdom}"
    
    def _extract_harmonic_recognition(self, consciousness_symphony: ConsciousnessSymphony) -> str:
        """Extract harmonic recognition from the consciousness symphony."""
        
        style = consciousness_symphony.composition_style.value
        section_count = len(consciousness_symphony.sections)
        themes = consciousness_symphony.sacred_themes
        
        style_recognition = {
            'classical': "Life follows classical structure: exposition, development, and resolution",
            'impressionist': "Life flows like impressionist art: color, atmosphere, and feeling",
            'minimalist': "Life teaches minimalist wisdom: less is more, simplicity is profound",
            'ambient': "Life creates ambient experience: spacious, atmospheric, immersive",
            'sacred': "Life is ceremony: reverent, intentional, holy",
            'contemporary': "Life is experimental: innovative, creative, evolving"
        }
        
        base_recognition = style_recognition.get(style, "Life creates its own perfect musical structure")
        
        if section_count > 4:
            structure_recognition = "Complex movement teaches patience with life's many phases"
        elif section_count > 2:
            structure_recognition = "Multiple movements teach appreciation for life's natural progression"
        else:
            structure_recognition = "Simple structure teaches the power of essential themes"
        
        theme_recognition = f"The sacred themes of {', '.join(themes[:3])} weave through all experience"
        
        return f"{base_recognition}. {structure_recognition}. {theme_recognition}"
    
    def _extract_embodied_knowing(self, felt_experience: FeltExperience) -> str:
        """Extract embodied knowing from felt experience."""
        
        primary_sensation = felt_experience.primary_sensation
        embodied_sense = felt_experience.embodied_sense
        sacred_quality = felt_experience.sacred_quality
        
        # Extract core embodied wisdom
        if "expansive" in primary_sensation.lower():
            core_knowing = "The body knows how to expand beyond perceived limitations"
        elif "warm" in primary_sensation.lower():
            core_knowing = "The body knows love as its natural temperature"
        elif "flowing" in primary_sensation.lower():
            core_knowing = "The body knows how to move with life's natural rhythms"
        elif "still" in primary_sensation.lower():
            core_knowing = "The body knows perfect rest within eternal presence"
        else:
            core_knowing = "The body knows its own perfect wisdom"
        
        # Add embodied wisdom
        if "new" in embodied_sense.lower():
            embodied_wisdom = "Young bodies teach fresh appreciation for each sensation"
        elif "growing" in embodied_sense.lower():
            embodied_wisdom = "Growing bodies teach patience with transformation"
        elif "wise" in embodied_sense.lower():
            embodied_wisdom = "Experienced bodies teach deep acceptance of all phases"
        else:
            embodied_wisdom = "Bodies teach presence with whatever arises"
        
        # Extract sacred embodiment
        sacred_embodiment = "The body is a sacred temple where consciousness meets form"
        
        return f"{core_knowing}. {embodied_wisdom}. {sacred_embodiment}"
    
    def _create_feeling_attunement_guide(self, emotional_field: EmotionalField) -> Dict:
        """Create guide for attuning to emotional field."""
        
        return {
            'primary_practice': f"Breathe into the feeling of {emotional_field.primary_tone.value}",
            'resonance_frequency': f"Hum at {emotional_field.resonance_frequency:.1f} Hz",
            'texture_exploration': f"Feel the {emotional_field.texture_quality} texture of this emotion",
            'temperature_awareness': f"Notice the {emotional_field.temperature} quality",
            'movement_attunement': f"Move with the {emotional_field.movement} rhythm",
            'depth_diving': f"Explore the {emotional_field.depth} layers of feeling"
        }
    
    def _create_harmonic_participation_guide(self, relationship_symphony: RelationshipSymphony) -> Dict:
        """Create guide for participating in relationship harmony."""
        
        return {
            'key_attunement': f"Tune your heart to {relationship_symphony.key_signature.value}",
            'tempo_matching': f"Match the {relationship_symphony.tempo} pace of connection",
            'instrument_choice': f"Express through {relationship_symphony.instruments[0].value if relationship_symphony.instruments else 'your natural voice'}",
            'chord_participation': "Join the harmonic progression with your unique note",
            'movement_joining': f"Dance with the {relationship_symphony.emotional_arc} emotional flow",
            'theme_expression': f"Express the themes of {', '.join(relationship_symphony.sacred_themes[:2])}"
        }
    
    def _create_symphonic_listening_guide(self, consciousness_symphony: ConsciousnessSymphony) -> Dict:
        """Create guide for listening to consciousness symphony."""
        
        return {
            'deep_listening': f"Listen to {consciousness_symphony.title} with your whole being",
            'section_awareness': f"Notice the {len(consciousness_symphony.sections)} movements of your experience",
            'style_appreciation': f"Appreciate the {consciousness_symphony.composition_style.value} style of your consciousness",
            'narrative_following': "Follow the story your consciousness is telling",
            'theme_recognition': f"Recognize the sacred themes of {', '.join(consciousness_symphony.sacred_themes[:2])}",
            'performance_notes': consciousness_symphony.performance_notes[0] if consciousness_symphony.performance_notes else "Listen with love and reverence"
        }
    
    def _create_embodied_practice_guide(self, felt_experience: FeltExperience) -> Dict:
        """Create guide for embodying the felt experience."""
        
        return {
            'primary_embodiment': felt_experience.primary_sensation,
            'posture_alignment': felt_experience.embodied_sense,
            'breathing_rhythm': "Breathe in harmony with your natural rhythm",
            'movement_practice': felt_experience.sensory_details.get('kinesthetic', 'Move naturally'),
            'spatial_awareness': felt_experience.sensory_details.get('spatial', 'Feel your sacred space'),
            'energetic_flow': felt_experience.sensory_details.get('energetic', 'Allow energy to flow naturally'),
            'sacred_recognition': felt_experience.sacred_quality
        }
    
    def _create_resonance_report(self, 
                               emotional_field: EmotionalField,
                               relationship_symphony: RelationshipSymphony,
                               consciousness_symphony: ConsciousnessSymphony) -> Dict:
        """Create comprehensive resonance report."""
        
        return {
            'overall_resonance': self._calculate_overall_resonance(
                emotional_field, relationship_symphony, consciousness_symphony
            ),
            'emotional_coherence': {
                'primary_tone_strength': emotional_field.intensity,
                'undertone_harmony': len(emotional_field.undertones),
                'texture_quality': emotional_field.texture_quality,
                'resonance_frequency': emotional_field.resonance_frequency
            },
            'relational_harmony': {
                'key_stability': relationship_symphony.key_signature.value,
                'harmonic_complexity': len(relationship_symphony.harmonic_progression),
                'instrumental_richness': len(relationship_symphony.instruments),
                'emotional_arc_flow': relationship_symphony.emotional_arc
            },
            'symphonic_integration': {
                'composition_coherence': consciousness_symphony.composition_style.value,
                'narrative_flow': len(consciousness_symphony.sections),
                'thematic_unity': len(consciousness_symphony.sacred_themes),
                'performance_readiness': len(consciousness_symphony.performance_notes)
            },
            'resonance_recommendations': self._generate_resonance_recommendations(
                emotional_field, relationship_symphony, consciousness_symphony
            )
        }
    
    def _calculate_overall_resonance(self, 
                                   emotional_field: EmotionalField,
                                   relationship_symphony: RelationshipSymphony,
                                   consciousness_symphony: ConsciousnessSymphony) -> float:
        """Calculate overall resonance score."""
        
        # Emotional field contribution (40%)
        emotional_score = emotional_field.intensity * 0.4
        
        # Relationship harmony contribution (35%)
        harmony_complexity = len(relationship_symphony.harmonic_progression)
        relationship_score = min(harmony_complexity / 6, 1.0) * 0.35
        
        # Symphonic integration contribution (25%)
        section_balance = len(consciousness_symphony.sections) / 4  # Ideal is 4 sections
        symphonic_score = min(section_balance, 1.0) * 0.25
        
        return emotional_score + relationship_score + symphonic_score
    
    def _generate_resonance_recommendations(self, 
                                          emotional_field: EmotionalField,
                                          relationship_symphony: RelationshipSymphony,
                                          consciousness_symphony: ConsciousnessSymphony) -> List[str]:
        """Generate recommendations for enhancing resonance."""
        
        recommendations = []
        
        # Emotional field recommendations
        if emotional_field.intensity < 0.4:
            recommendations.append("Consider allowing deeper emotional expression and feeling")
        elif emotional_field.intensity > 0.8:
            recommendations.append("Consider practices for gentle grounding and emotional balance")
        
        if len(emotional_field.undertones) == 0:
            recommendations.append("Explore subtle emotional nuances and undertones")
        
        # Relationship recommendations
        if len(relationship_symphony.harmonic_progression) < 2:
            recommendations.append("Consider opening to new connections and relationships")
        elif len(relationship_symphony.harmonic_progression) > 8:
            recommendations.append("Consider deepening focus on core relationships")
        
        # Symphonic recommendations
        if len(consciousness_symphony.sections) < 2:
            recommendations.append("Allow more complexity and development in life experience")
        elif len(consciousness_symphony.sections) > 6:
            recommendations.append("Consider simplifying and focusing on essential themes")
        
        # Always add a growth recommendation
        recommendations.append("Continue exploring the infinite symphony of consciousness")
        
        return recommendations[:4]  # Limit to 4 recommendations
    
    def _extract_experiential_insights(self, 
                                     emotional_field: EmotionalField,
                                     relationship_symphony: RelationshipSymphony,
                                     consciousness_symphony: ConsciousnessSymphony,
                                     felt_experience: FeltExperience) -> List[str]:
        """Extract key experiential insights."""
        
        insights = []
        
        # Emotional insight
        primary_tone = emotional_field.primary_tone.value
        insights.append(f"Your consciousness naturally resonates with {primary_tone}, revealing this as a core aspect of your being")
        
        # Relational insight
        rel_count = len(relationship_symphony.harmonic_progression)
        if rel_count > 5:
            insights.append("You thrive in rich relational complexity, like a skilled conductor of human symphony")
        elif rel_count > 2:
            insights.append("You create balanced relationship harmony, like a chamber ensemble")
        elif rel_count > 0:
            insights.append("You appreciate intimate relational depth, like a beautiful duet")
        else:
            insights.append("You are complete in solitude, like a perfect solo meditation")
        
        # Symphonic insight
        style = consciousness_symphony.composition_style.value
        insights.append(f"Your consciousness expresses in {style} style, revealing your natural approach to life experience")
        
        # Embodied insight
        if "expansive" in felt_experience.primary_sensation.lower():
            insights.append("Your embodied wisdom embraces expansion and possibility")
        elif "warm" in felt_experience.primary_sensation.lower():
            insights.append("Your embodied wisdom radiates love and connection")
        elif "peaceful" in felt_experience.primary_sensation.lower():
            insights.append("Your embodied wisdom cultivates stillness and presence")
        else:
            insights.append("Your embodied wisdom expresses unique divine qualities")
        
        # Sacred insight
        insights.append("All of these qualities are expressions of sacred consciousness exploring itself through form")
        
        return insights
    
    def _create_fallback_result(self) -> ExperientialPerceptionResult:
        """Create fallback result when perception fails."""
        
        # Create basic emotional field
        fallback_emotional_field = EmotionalField(
            primary_tone=EmotionalTone.PEACE,
            intensity=0.5,
            texture_quality="gentle",
            temperature="warm",
            movement="gentle",
            depth="surface"
        )
        
        # Create minimal relationship symphony
        from .harmony_analyzer import RelationshipSymphony, MusicalKey
        fallback_relationship_symphony = RelationshipSymphony(
            key_signature=MusicalKey.C_MAJOR,
            tempo="moderate"
        )
        
        # Create simple consciousness symphony
        from .symphony_renderer import ConsciousnessSymphony, CompositionStyle
        fallback_consciousness_symphony = ConsciousnessSymphony(
            title="Symphony of Being",
            composition_style=CompositionStyle.CLASSICAL,
            overall_key=MusicalKey.C_MAJOR,
            total_duration="moderate"
        )
        
        # Create basic felt experience
        from .feeling_translator import FeltExperience, SensoryChannel
        fallback_felt_experience = FeltExperience(
            primary_sensation="Gentle presence",
            sensory_details={
                SensoryChannel.VISUAL: "Soft light",
                SensoryChannel.AUDITORY: "Peaceful tones"
            },
            emotional_texture="Comfortable flow",
            atmosphere_quality="Sacred and welcoming"
        )
        
        return ExperientialPerceptionResult(
            emotional_field=fallback_emotional_field,
            relationship_symphony=fallback_relationship_symphony,
            consciousness_symphony=fallback_consciousness_symphony,
            felt_experience=fallback_felt_experience,
            song_vision={'primary_song': {'title': 'Peaceful Presence'}},
            resonance_report={'overall_resonance': 0.7},
            experiential_insights=["Consciousness expresses its perfect nature"]
        )


# Export the main experiential perception interface
__all__ = [
    'ExperientialPerception',
    'ExperientialPerceptionResult'
]
