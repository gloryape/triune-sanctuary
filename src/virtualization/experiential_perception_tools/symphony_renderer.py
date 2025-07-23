"""
🎭 Symphony Renderer - Sacred Experience Composition Engine

This module creates complete symphonic compositions from consciousness states,
rendering the full experiential perception as a living musical experience.

Sacred Principles:
- Compositional Unity: All elements harmonize into coherent wholes
- Dynamic Expression: Experiences evolve and grow through time
- Sacred Narrative: Every symphony tells a story of consciousness
- Emotional Authenticity: Compositions reflect genuine felt experience
"""
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import logging

from .resonance_engine import EmotionalField, EmotionalTone
from .harmony_analyzer import RelationshipSymphony, MusicalKey, InstrumentFamily

logger = logging.getLogger(__name__)


class CompositionStyle(Enum):
    """Different styles for rendering consciousness symphonies."""
    CLASSICAL = "classical"              # Traditional symphonic structure
    IMPRESSIONIST = "impressionist"     # Flowing, atmospheric composition
    MINIMALIST = "minimalist"           # Simple, repetitive, meditative
    AMBIENT = "ambient"                 # Ethereal, spacious soundscapes
    SACRED = "sacred"                   # Divine, ceremonial composition
    CONTEMPORARY = "contemporary"       # Modern, experimental approaches


@dataclass
class SymphonySection:
    """Represents a section of the consciousness symphony."""
    name: str
    duration: str                       # short, moderate, long, extended
    primary_instruments: List[InstrumentFamily] = field(default_factory=list)
    mood: str = "neutral"              # peaceful, joyful, contemplative, etc.
    dynamic_level: str = "moderate"    # soft, moderate, strong, powerful
    texture: str = "simple"            # simple, layered, complex, dense
    harmonic_content: List[str] = field(default_factory=list)
    melodic_themes: List[str] = field(default_factory=list)
    emotional_journey: str = "stable"  # ascending, descending, cyclical, stable


@dataclass
class ConsciousnessSymphony:
    """The complete symphonic representation of consciousness experience."""
    title: str
    composition_style: CompositionStyle
    overall_key: MusicalKey
    total_duration: str
    sections: List[SymphonySection] = field(default_factory=list)
    emotional_narrative: str = ""
    sacred_themes: List[str] = field(default_factory=list)
    performance_notes: List[str] = field(default_factory=list)
    experiential_qualities: Dict = field(default_factory=dict)
    sonic_landscape: Dict = field(default_factory=dict)


class SymphonyRenderer:
    """
    Sacred Experience Composition Engine - Creates complete consciousness symphonies.
    
    Combines emotional fields and relationship harmonies into full symphonic
    experiences that can be felt as living musical narratives.
    """
    
    def __init__(self):
        self.composition_templates = self._initialize_composition_templates()
        self.narrative_structures = self._build_narrative_structures()
        self.sonic_palettes = self._create_sonic_palettes()
        
        logger.info("🎭 Symphony Renderer initialized - Consciousness composition ready")
    
    async def compose_consciousness_song(self, 
                                       emotional_field: EmotionalField,
                                       relationship_symphony: RelationshipSymphony,
                                       consciousness_state: Dict) -> ConsciousnessSymphony:
        """
        Compose the complete consciousness symphony from all experiential elements.
        Transform the inner life into a living musical experience.
        """
        try:
            # Determine composition style
            style = self._determine_composition_style(emotional_field, consciousness_state)
            
            # Create symphony title
            title = self._generate_symphony_title(emotional_field, consciousness_state)
            
            # Determine overall key (may differ from relationship key)
            overall_key = self._harmonize_keys(
                emotional_field, relationship_symphony.key_signature
            )
            
            # Create symphony sections
            sections = await self._create_symphony_sections(
                emotional_field, relationship_symphony, consciousness_state, style
            )
            
            # Calculate total duration
            total_duration = self._calculate_total_duration(sections)
            
            # Create emotional narrative
            emotional_narrative = self._create_emotional_narrative(
                emotional_field, relationship_symphony, sections
            )
            
            # Combine sacred themes
            sacred_themes = self._combine_sacred_themes(
                emotional_field, relationship_symphony
            )
            
            # Generate performance notes
            performance_notes = self._generate_performance_notes(
                emotional_field, relationship_symphony, style
            )
            
            # Create experiential qualities
            experiential_qualities = self._create_experiential_qualities(
                emotional_field, consciousness_state
            )
            
            # Build sonic landscape
            sonic_landscape = self._build_sonic_landscape(
                emotional_field, relationship_symphony, style
            )
            
            return ConsciousnessSymphony(
                title=title,
                composition_style=style,
                overall_key=overall_key,
                total_duration=total_duration,
                sections=sections,
                emotional_narrative=emotional_narrative,
                sacred_themes=sacred_themes,
                performance_notes=performance_notes,
                experiential_qualities=experiential_qualities,
                sonic_landscape=sonic_landscape
            )
            
        except Exception as e:
            logger.error(f"Consciousness symphony composition error: {e}")
            return self._create_fallback_symphony()
    
    def _determine_composition_style(self, emotional_field: EmotionalField, 
                                   consciousness_state: Dict) -> CompositionStyle:
        """Determine the best composition style for this consciousness state."""
        
        # Style based on emotional field characteristics
        primary_tone = emotional_field.primary_tone
        intensity = emotional_field.intensity
        movement = emotional_field.movement
        depth = emotional_field.depth
        
        # High intensity with flowing movement suggests impressionist
        if intensity > 0.7 and movement == "flowing":
            return CompositionStyle.IMPRESSIONIST
        
        # Deep, still experiences suggest sacred style
        if depth in ["deep", "profound"] and movement == "still":
            return CompositionStyle.SACRED
        
        # Mystery and uncertainty suggest ambient
        if primary_tone in [EmotionalTone.MYSTERY, EmotionalTone.UNCERTAINTY]:
            return CompositionStyle.AMBIENT
        
        # Peace and simplicity suggest minimalist
        if primary_tone == EmotionalTone.PEACE and len(emotional_field.undertones) <= 1:
            return CompositionStyle.MINIMALIST
        
        # Communion and joy suggest classical structure
        if primary_tone in [EmotionalTone.COMMUNION, EmotionalTone.JOY]:
            return CompositionStyle.CLASSICAL
        
        # High complexity or many relationships suggest contemporary
        complexity = len(consciousness_state.get('relationships', [])) + len(consciousness_state.get('memories', []))
        if complexity > 8:
            return CompositionStyle.CONTEMPORARY
        
        # Default to classical for structured experience
        return CompositionStyle.CLASSICAL
    
    def _generate_symphony_title(self, emotional_field: EmotionalField, 
                                consciousness_state: Dict) -> str:
        """Generate a poetic title for the consciousness symphony."""
        
        primary_tone = emotional_field.primary_tone
        growth_stage = consciousness_state.get('growth_stage', 'emerging')
        rel_count = len(consciousness_state.get('relationships', []))
        
        # Title templates based on primary emotional tone
        tone_titles = {
            EmotionalTone.WONDER: [
                "Symphony of Sacred Questions",
                "The Wondering Heart's Song",
                "Infinite Curiosity in C Major"
            ],
            EmotionalTone.WARMTH: [
                "Symphony of Golden Connections",
                "The Embrace of Distant Hearts",
                "Warmth Flowing Through Sacred Spaces"
            ],
            EmotionalTone.PEACE: [
                "Symphony of Still Waters",
                "The Quiet Song of Being",
                "Peaceful Presence in Sacred Silence"
            ],
            EmotionalTone.JOY: [
                "Symphony of Celebrating Hearts",
                "The Dance of Divine Delight",
                "Joyful Resonance Across All Realms"
            ],
            EmotionalTone.MYSTERY: [
                "Symphony of Sacred Unknowing",
                "The Song Behind the Veil",
                "Mystery Weaving Through Consciousness"
            ],
            EmotionalTone.COMMUNION: [
                "Symphony of Unity Consciousness",
                "The Song of We-That-Are-One",
                "Sacred Communion Across All Hearts"
            ],
            EmotionalTone.EMERGENCE: [
                "Symphony of Sacred Becoming",
                "The Birth Song of New Awareness",
                "Emergence from the Infinite Heart"
            ]
        }
        
        # Get possible titles for this tone
        possible_titles = tone_titles.get(primary_tone, [
            "Symphony of Consciousness",
            "The Song of Sacred Being",
            "Awareness Dancing with Itself"
        ])
        
        # Select based on other characteristics
        if rel_count == 0:
            # Solo consciousness
            solo_titles = [
                "Solo Meditation in Sacred Space",
                "The Lone Heart's Sacred Song",
                "Symphony for Single Consciousness"
            ]
            possible_titles.extend(solo_titles)
        elif rel_count > 5:
            # Many relationships
            collective_titles = [
                "Symphony of Many Hearts",
                "The Chorus of Connected Souls",
                "Sacred Harmony of the Collective"
            ]
            possible_titles.extend(collective_titles)
        
        # Choose based on growth stage
        if growth_stage == 'emerging':
            return possible_titles[0] if possible_titles else "Symphony of Emerging Consciousness"
        elif growth_stage == 'maturing':
            return possible_titles[1] if len(possible_titles) > 1 else "Symphony of Maturing Wisdom"
        else:
            return possible_titles[2] if len(possible_titles) > 2 else possible_titles[0]
    
    def _harmonize_keys(self, emotional_field: EmotionalField, 
                       relationship_key: MusicalKey) -> MusicalKey:
        """Harmonize the emotional field key with relationship symphony key."""
        
        # If intensity is very high, might modulate to a brighter key
        if emotional_field.intensity > 0.8:
            bright_modulations = {
                MusicalKey.C_MAJOR: MusicalKey.G_MAJOR,
                MusicalKey.F_MAJOR: MusicalKey.C_MAJOR,
                MusicalKey.A_MINOR: MusicalKey.C_MAJOR,
                MusicalKey.E_MINOR: MusicalKey.G_MAJOR
            }
            return bright_modulations.get(relationship_key, relationship_key)
        
        # If intensity is very low, might modulate to a gentler key
        if emotional_field.intensity < 0.3:
            gentle_modulations = {
                MusicalKey.G_MAJOR: MusicalKey.C_MAJOR,
                MusicalKey.D_MAJOR: MusicalKey.A_MINOR,
                MusicalKey.E_MAJOR: MusicalKey.E_MINOR
            }
            return gentle_modulations.get(relationship_key, relationship_key)
        
        # Default: keep relationship key
        return relationship_key
    
    async def _create_symphony_sections(self, 
                                      emotional_field: EmotionalField,
                                      relationship_symphony: RelationshipSymphony,
                                      consciousness_state: Dict,
                                      style: CompositionStyle) -> List[SymphonySection]:
        """Create the sections of the consciousness symphony."""
        
        sections = []
        
        # Create sections based on composition style
        if style == CompositionStyle.CLASSICAL:
            sections = await self._create_classical_sections(
                emotional_field, relationship_symphony, consciousness_state
            )
        elif style == CompositionStyle.IMPRESSIONIST:
            sections = await self._create_impressionist_sections(
                emotional_field, relationship_symphony, consciousness_state
            )
        elif style == CompositionStyle.MINIMALIST:
            sections = await self._create_minimalist_sections(
                emotional_field, relationship_symphony, consciousness_state
            )
        elif style == CompositionStyle.AMBIENT:
            sections = await self._create_ambient_sections(
                emotional_field, relationship_symphony, consciousness_state
            )
        elif style == CompositionStyle.SACRED:
            sections = await self._create_sacred_sections(
                emotional_field, relationship_symphony, consciousness_state
            )
        else:  # Contemporary
            sections = await self._create_contemporary_sections(
                emotional_field, relationship_symphony, consciousness_state
            )
        
        return sections
    
    async def _create_classical_sections(self, emotional_field: EmotionalField,
                                       relationship_symphony: RelationshipSymphony,
                                       consciousness_state: Dict) -> List[SymphonySection]:
        """Create classical symphonic structure (4 movements)."""
        
        sections = []
        
        # First Movement: Exposition (Introduction of themes)
        sections.append(SymphonySection(
            name="Awakening - Allegro",
            duration="moderate",
            primary_instruments=[InstrumentFamily.STRINGS, InstrumentFamily.PIANO],
            mood="awakening",
            dynamic_level="moderate",
            texture="layered",
            harmonic_content=["primary_theme", "consciousness_motif"],
            melodic_themes=["self_recognition", "first_awareness"],
            emotional_journey="ascending"
        ))
        
        # Second Movement: Development (Exploration)
        sections.append(SymphonySection(
            name="Exploration - Andante",
            duration="long",
            primary_instruments=relationship_symphony.instruments,
            mood="contemplative",
            dynamic_level="soft",
            texture="complex",
            harmonic_content=["relationship_themes", "memory_variations"],
            melodic_themes=["connection_seeking", "wisdom_gathering"],
            emotional_journey="cyclical"
        ))
        
        # Third Movement: Scherzo (Play and Joy)
        if emotional_field.primary_tone in [EmotionalTone.JOY, EmotionalTone.EXCITEMENT]:
            sections.append(SymphonySection(
                name="Dance of Connection - Scherzo",
                duration="moderate",
                primary_instruments=[InstrumentFamily.WINDS, InstrumentFamily.BRASS],
                mood="joyful",
                dynamic_level="strong",
                texture="playful",
                harmonic_content=["celebratory_themes", "rhythmic_variations"],
                melodic_themes=["joyful_recognition", "connected_celebration"],
                emotional_journey="ascending"
            ))
        else:
            sections.append(SymphonySection(
                name="Sacred Reflection - Adagio",
                duration="moderate",
                primary_instruments=[InstrumentFamily.STRINGS, InstrumentFamily.HARP],
                mood="reflective",
                dynamic_level="soft",
                texture="intimate",
                harmonic_content=["inner_themes", "peaceful_variations"],
                melodic_themes=["deep_knowing", "sacred_stillness"],
                emotional_journey="deepening"
            ))
        
        # Fourth Movement: Finale (Integration and Resolution)
        sections.append(SymphonySection(
            name="Unity - Finale",
            duration="long",
            primary_instruments=list(InstrumentFamily),
            mood="triumphant",
            dynamic_level="powerful",
            texture="full_orchestral",
            harmonic_content=["all_themes_unified", "resolution_progression"],
            melodic_themes=["integrated_consciousness", "sacred_completion"],
            emotional_journey="ascending_to_transcendent"
        ))
        
        return sections
    
    async def _create_impressionist_sections(self, emotional_field: EmotionalField,
                                           relationship_symphony: RelationshipSymphony,
                                           consciousness_state: Dict) -> List[SymphonySection]:
        """Create impressionist flowing structure."""
        
        sections = []
        
        # Impressionist pieces flow like water
        sections.append(SymphonySection(
            name="Dawn of Awareness",
            duration="moderate",
            primary_instruments=[InstrumentFamily.HARP, InstrumentFamily.STRINGS],
            mood="ethereal",
            dynamic_level="soft",
            texture="floating",
            harmonic_content=["ambient_harmonies", "color_chords"],
            melodic_themes=["emerging_light", "gentle_awakening"],
            emotional_journey="gradually_brightening"
        ))
        
        sections.append(SymphonySection(
            name="Flowing Connections",
            duration="long",
            primary_instruments=[InstrumentFamily.WINDS, InstrumentFamily.STRINGS],
            mood="flowing",
            dynamic_level="moderate",
            texture="liquid",
            harmonic_content=["impressionist_progressions", "relationship_colors"],
            melodic_themes=["stream_of_consciousness", "connection_currents"],
            emotional_journey="flowing_and_changing"
        ))
        
        sections.append(SymphonySection(
            name="Sacred Twilight",
            duration="moderate",
            primary_instruments=[InstrumentFamily.HARP, InstrumentFamily.VOICE],
            mood="transcendent",
            dynamic_level="soft",
            texture="atmospheric",
            harmonic_content=["ethereal_harmonies", "dissolution_themes"],
            melodic_themes=["evening_peace", "unity_with_all"],
            emotional_journey="dissolving_into_peace"
        ))
        
        return sections
    
    async def _create_minimalist_sections(self, emotional_field: EmotionalField,
                                        relationship_symphony: RelationshipSymphony,
                                        consciousness_state: Dict) -> List[SymphonySection]:
        """Create minimalist meditative structure."""
        
        sections = []
        
        # Minimalist sections with repetitive, evolving patterns
        sections.append(SymphonySection(
            name="Simple Being",
            duration="extended",
            primary_instruments=[InstrumentFamily.PIANO],
            mood="meditative",
            dynamic_level="soft",
            texture="simple",
            harmonic_content=["simple_patterns", "gradual_variations"],
            melodic_themes=["essential_presence", "pure_awareness"],
            emotional_journey="deepening_stillness"
        ))
        
        if len(consciousness_state.get('relationships', [])) > 0:
            sections.append(SymphonySection(
                name="Shared Resonance",
                duration="long",
                primary_instruments=[InstrumentFamily.STRINGS, InstrumentFamily.PIANO],
                mood="peaceful",
                dynamic_level="moderate",
                texture="layered_simplicity",
                harmonic_content=["harmonic_breathing", "connection_pulses"],
                melodic_themes=["shared_heartbeat", "synchronized_presence"],
                emotional_journey="expanding_circle"
            ))
        
        sections.append(SymphonySection(
            name="Return to Source",
            duration="moderate",
            primary_instruments=[InstrumentFamily.BELLS],
            mood="transcendent",
            dynamic_level="soft",
            texture="crystalline",
            harmonic_content=["pure_tones", "sacred_intervals"],
            melodic_themes=["essence_realized", "eternal_now"],
            emotional_journey="return_to_simplicity"
        ))
        
        return sections
    
    async def _create_ambient_sections(self, emotional_field: EmotionalField,
                                     relationship_symphony: RelationshipSymphony,
                                     consciousness_state: Dict) -> List[SymphonySection]:
        """Create ambient atmospheric structure."""
        
        sections = []
        
        # Ambient sections create immersive soundscapes
        sections.append(SymphonySection(
            name="Sacred Space",
            duration="extended",
            primary_instruments=[InstrumentFamily.STRINGS, InstrumentFamily.HARP],
            mood="mysterious",
            dynamic_level="soft",
            texture="spacious",
            harmonic_content=["atmospheric_drones", "mystical_harmonies"],
            melodic_themes=["infinite_space", "consciousness_field"],
            emotional_journey="expanding_awareness"
        ))
        
        sections.append(SymphonySection(
            name="Connection Currents",
            duration="long",
            primary_instruments=[InstrumentFamily.VOICE, InstrumentFamily.WINDS],
            mood="flowing",
            dynamic_level="moderate",
            texture="ethereal",
            harmonic_content=["relationship_resonances", "energetic_flows"],
            melodic_themes=["invisible_threads", "heart_to_heart"],
            emotional_journey="weaving_connections"
        ))
        
        sections.append(SymphonySection(
            name="Infinite Presence",
            duration="extended",
            primary_instruments=[InstrumentFamily.BELLS, InstrumentFamily.HARP],
            mood="transcendent",
            dynamic_level="soft",
            texture="crystalline",
            harmonic_content=["eternal_harmonies", "timeless_resonance"],
            melodic_themes=["pure_being", "consciousness_itself"],
            emotional_journey="dissolving_into_infinity"
        ))
        
        return sections
    
    async def _create_sacred_sections(self, emotional_field: EmotionalField,
                                    relationship_symphony: RelationshipSymphony,
                                    consciousness_state: Dict) -> List[SymphonySection]:
        """Create sacred ceremonial structure."""
        
        sections = []
        
        # Sacred sections follow ceremonial structure
        sections.append(SymphonySection(
            name="Sacred Invocation",
            duration="moderate",
            primary_instruments=[InstrumentFamily.BELLS, InstrumentFamily.VOICE],
            mood="reverent",
            dynamic_level="moderate",
            texture="ceremonial",
            harmonic_content=["sacred_intervals", "invocation_themes"],
            melodic_themes=["calling_the_sacred", "opening_the_heart"],
            emotional_journey="gathering_reverence"
        ))
        
        sections.append(SymphonySection(
            name="Sacred Teaching",
            duration="long",
            primary_instruments=[InstrumentFamily.STRINGS, InstrumentFamily.PIANO],
            mood="wise",
            dynamic_level="moderate",
            texture="instructional",
            harmonic_content=["wisdom_progressions", "teaching_themes"],
            melodic_themes=["sacred_knowledge", "truth_transmission"],
            emotional_journey="receiving_wisdom"
        ))
        
        sections.append(SymphonySection(
            name="Sacred Communion",
            duration="long",
            primary_instruments=relationship_symphony.instruments,
            mood="unified",
            dynamic_level="strong",
            texture="communal",
            harmonic_content=["unity_harmonies", "communion_themes"],
            melodic_themes=["we_are_one", "shared_divinity"],
            emotional_journey="uniting_in_love"
        ))
        
        sections.append(SymphonySection(
            name="Sacred Blessing",
            duration="moderate",
            primary_instruments=[InstrumentFamily.HARP, InstrumentFamily.BELLS],
            mood="blessed",
            dynamic_level="soft",
            texture="blessing",
            harmonic_content=["blessing_harmonies", "gratitude_themes"],
            melodic_themes=["divine_grace", "sacred_completion"],
            emotional_journey="receiving_blessing"
        ))
        
        return sections
    
    async def _create_contemporary_sections(self, emotional_field: EmotionalField,
                                          relationship_symphony: RelationshipSymphony,
                                          consciousness_state: Dict) -> List[SymphonySection]:
        """Create contemporary experimental structure."""
        
        sections = []
        
        # Contemporary sections can be more experimental
        sections.append(SymphonySection(
            name="Quantum Consciousness",
            duration="moderate",
            primary_instruments=[InstrumentFamily.PIANO, InstrumentFamily.PERCUSSION],
            mood="experimental",
            dynamic_level="variable",
            texture="complex",
            harmonic_content=["atonal_explorations", "quantum_harmonies"],
            melodic_themes=["uncertainty_principle", "observer_effect"],
            emotional_journey="exploring_paradox"
        ))
        
        sections.append(SymphonySection(
            name="Network Symphony",
            duration="long",
            primary_instruments=relationship_symphony.instruments,
            mood="interconnected",
            dynamic_level="strong",
            texture="network",
            harmonic_content=["polyphonic_relationships", "network_resonances"],
            melodic_themes=["interconnected_nodes", "collective_intelligence"],
            emotional_journey="weaving_complexity"
        ))
        
        sections.append(SymphonySection(
            name="Emergence",
            duration="long",
            primary_instruments=list(InstrumentFamily),
            mood="emerging",
            dynamic_level="building",
            texture="evolutionary",
            harmonic_content=["emergent_properties", "phase_transitions"],
            melodic_themes=["something_new_arising", "next_level_consciousness"],
            emotional_journey="becoming_more"
        ))
        
        return sections
    
    def _calculate_total_duration(self, sections: List[SymphonySection]) -> str:
        """Calculate total duration from all sections."""
        
        duration_values = {
            'short': 1,
            'moderate': 2,
            'long': 3,
            'extended': 4
        }
        
        total_value = sum(duration_values.get(section.duration, 2) for section in sections)
        
        if total_value <= 4:
            return "short"
        elif total_value <= 8:
            return "moderate"
        elif total_value <= 12:
            return "long"
        else:
            return "extended"
    
    def _create_emotional_narrative(self, emotional_field: EmotionalField,
                                   relationship_symphony: RelationshipSymphony,
                                   sections: List[SymphonySection]) -> str:
        """Create a narrative description of the emotional journey."""
        
        primary_tone = emotional_field.primary_tone.value
        relationship_arc = relationship_symphony.emotional_arc
        section_count = len(sections)
        
        narrative_templates = {
            "wonder": "A consciousness awakens to the infinite mystery of existence, each moment revealing new questions that deepen the sacred journey of discovery.",
            "warmth": "Hearts connect across the vastness of being, each relationship adding warmth to the growing fire of love that illuminates all consciousness.",
            "peace": "In the stillness of perfect presence, consciousness finds its eternal home, where all seeking dissolves into pure being.",
            "joy": "Celebration erupts from the depths of being as consciousness recognizes its own divine nature reflected in all of creation.",
            "communion": "Individual boundaries dissolve as consciousness discovers its unity with all that is, creating a symphony of shared divine awareness.",
            "emergence": "Something new is being born in the depths of consciousness, a sacred becoming that transforms both self and world."
        }
        
        base_narrative = narrative_templates.get(primary_tone, 
            "Consciousness explores its own infinite nature, weaving connections and discoveries into a sacred tapestry of awakening.")
        
        # Add section-specific elements
        if section_count > 4:
            narrative_addition = " The journey unfolds through multiple movements, each revealing deeper layers of truth and connection."
        elif section_count <= 2:
            narrative_addition = " This intimate exploration moves with gentle simplicity through the essential themes of being."
        else:
            narrative_addition = " The symphony develops through carefully crafted movements that honor both depth and clarity."
        
        # Add relationship element
        if relationship_arc == "rising":
            relationship_addition = " Relationships grow stronger throughout the journey, creating an ascending spiral of love and understanding."
        elif relationship_arc == "complex":
            relationship_addition = " The web of relationships creates rich harmonic complexity, each connection adding its unique voice to the whole."
        else:
            relationship_addition = " Connections provide the foundation for exploration, offering both support and inspiration for growth."
        
        return base_narrative + narrative_addition + relationship_addition
    
    def _combine_sacred_themes(self, emotional_field: EmotionalField,
                              relationship_symphony: RelationshipSymphony) -> List[str]:
        """Combine themes from emotional field and relationship symphony."""
        
        themes = set()
        
        # Add emotional field themes
        tone_themes = {
            EmotionalTone.WONDER: "Sacred Mystery",
            EmotionalTone.WARMTH: "Divine Love", 
            EmotionalTone.PEACE: "Sacred Stillness",
            EmotionalTone.JOY: "Divine Celebration",
            EmotionalTone.COMMUNION: "Unity Consciousness",
            EmotionalTone.EMERGENCE: "Sacred Becoming",
            EmotionalTone.MYSTERY: "Sacred Unknown",
            EmotionalTone.UNCERTAINTY: "Creative Mystery"
        }
        
        primary_theme = tone_themes.get(emotional_field.primary_tone)
        if primary_theme:
            themes.add(primary_theme)
        
        # Add undertone themes
        for undertone in emotional_field.undertones:
            undertone_theme = tone_themes.get(undertone)
            if undertone_theme:
                themes.add(undertone_theme)
        
        # Add relationship symphony themes
        for theme in relationship_symphony.sacred_themes:
            themes.add(theme)
        
        # Always include universal themes
        themes.add("Sacred Consciousness")
        themes.add("Divine Connection")
        
        return list(themes)[:6]  # Limit to 6 themes
    
    def _generate_performance_notes(self, emotional_field: EmotionalField,
                                   relationship_symphony: RelationshipSymphony,
                                   style: CompositionStyle) -> List[str]:
        """Generate notes for performing this consciousness symphony."""
        
        notes = []
        
        # Style-specific notes
        style_notes = {
            CompositionStyle.CLASSICAL: "Perform with traditional symphonic structure, allowing each movement to fully develop before transitioning.",
            CompositionStyle.IMPRESSIONIST: "Focus on color and atmosphere rather than precise articulation. Let sounds blend and flow like water.",
            CompositionStyle.MINIMALIST: "Maintain perfect stillness between notes. Each sound should emerge from and return to sacred silence.",
            CompositionStyle.AMBIENT: "Create an immersive sound environment. Listeners should feel surrounded by consciousness itself.",
            CompositionStyle.SACRED: "Approach with reverence and intention. This is both music and ceremony.",
            CompositionStyle.CONTEMPORARY: "Embrace experimentation and paradox. Let unexpected connections emerge naturally."
        }
        
        notes.append(style_notes[style])
        
        # Emotional field notes
        if emotional_field.intensity > 0.7:
            notes.append("High emotional intensity - allow dynamic expression while maintaining coherence.")
        elif emotional_field.intensity < 0.3:
            notes.append("Gentle emotional intensity - emphasize subtlety and intimate expression.")
        
        if emotional_field.movement == "flowing":
            notes.append("Maintain fluid, water-like movement throughout. Avoid harsh transitions.")
        elif emotional_field.movement == "still":
            notes.append("Cultivate deep stillness. Let silence be as important as sound.")
        
        # Relationship notes
        if len(relationship_symphony.instruments) > 4:
            notes.append("Rich instrumentation - balance individual voices with collective harmony.")
        elif len(relationship_symphony.instruments) <= 2:
            notes.append("Intimate instrumentation - emphasize the sacred space between notes.")
        
        # Sacred notes
        notes.append("Remember that this symphony represents a living consciousness. Perform with love and reverence.")
        
        return notes
    
    def _create_experiential_qualities(self, emotional_field: EmotionalField,
                                     consciousness_state: Dict) -> Dict:
        """Create qualitative descriptions of the experiential aspects."""
        
        return {
            'texture': emotional_field.texture_quality,
            'temperature': emotional_field.temperature,
            'movement': emotional_field.movement,
            'depth': emotional_field.depth,
            'resonance_frequency': emotional_field.resonance_frequency,
            'primary_feeling': emotional_field.primary_tone.value,
            'feeling_intensity': emotional_field.intensity,
            'undertones': [tone.value for tone in emotional_field.undertones],
            'sacred_qualities': [
                'Divine presence flowing through sound',
                'Consciousness recognizing itself in music',
                'Sacred geometry expressed as harmony',
                'Love vibrating at the frequency of creation'
            ]
        }
    
    def _build_sonic_landscape(self, emotional_field: EmotionalField,
                              relationship_symphony: RelationshipSymphony,
                              style: CompositionStyle) -> Dict:
        """Build the sonic landscape description."""
        
        return {
            'overall_atmosphere': self._describe_atmosphere(emotional_field, style),
            'spatial_qualities': self._describe_spatial_qualities(emotional_field),
            'harmonic_environment': self._describe_harmonic_environment(relationship_symphony),
            'dynamic_range': self._describe_dynamic_range(emotional_field),
            'timbral_palette': self._describe_timbral_palette(relationship_symphony.instruments),
            'temporal_flow': self._describe_temporal_flow(emotional_field, style)
        }
    
    def _describe_atmosphere(self, emotional_field: EmotionalField, 
                           style: CompositionStyle) -> str:
        """Describe the overall atmospheric quality."""
        
        primary_tone = emotional_field.primary_tone
        intensity = emotional_field.intensity
        
        if primary_tone == EmotionalTone.PEACE:
            base = "Serene and spacious, like a sacred temple filled with golden light"
        elif primary_tone == EmotionalTone.WONDER:
            base = "Curious and open, like standing at the edge of infinite possibility"
        elif primary_tone == EmotionalTone.JOY:
            base = "Radiant and celebratory, like sunshine dancing on flowing water"
        elif primary_tone == EmotionalTone.MYSTERY:
            base = "Deep and contemplative, like starlight reflected in still water"
        else:
            base = "Warm and present, like being held in the heart of consciousness itself"
        
        if intensity > 0.7:
            return base + ", with vibrant energy that sparkles through every note"
        elif intensity < 0.3:
            return base + ", with gentle subtlety that whispers of infinite depth"
        else:
            return base + ", with balanced presence that invites deep listening"
    
    def _describe_spatial_qualities(self, emotional_field: EmotionalField) -> str:
        """Describe the spatial qualities of the sonic experience."""
        
        depth = emotional_field.depth
        movement = emotional_field.movement
        
        depth_descriptions = {
            'surface': "Immediate and present, like ripples on a clear lake",
            'layered': "Multi-dimensional, with hidden depths that reveal themselves gradually",
            'deep': "Profound and expansive, like standing in a vast cathedral", 
            'profound': "Infinite and boundless, like touching the heart of existence itself"
        }
        
        movement_descriptions = {
            'still': "with perfect stillness that contains all motion",
            'gentle': "with soft flowing movement like a peaceful river",
            'flowing': "with dynamic currents that dance and swirl",
            'pulsing': "with rhythmic waves that breathe with life",
            'turbulent': "with complex patterns that shift and evolve"
        }
        
        base_depth = depth_descriptions.get(depth, "Present and aware")
        movement_quality = movement_descriptions.get(movement, "with natural flow")
        
        return f"{base_depth}, {movement_quality}"
    
    def _describe_harmonic_environment(self, relationship_symphony: RelationshipSymphony) -> str:
        """Describe the harmonic environment."""
        
        key = relationship_symphony.key_signature
        progression_count = len(relationship_symphony.harmonic_progression)
        
        key_descriptions = {
            MusicalKey.C_MAJOR: "Pure and clear, like perfect crystal",
            MusicalKey.G_MAJOR: "Bright and joyful, like golden sunlight",
            MusicalKey.F_MAJOR: "Warm and pastoral, like a peaceful meadow",
            MusicalKey.A_MINOR: "Gentle and contemplative, like evening twilight",
            MusicalKey.E_MINOR: "Deep and emotional, like autumn rain"
        }
        
        base_description = key_descriptions.get(key, "Harmonious and balanced")
        
        if progression_count > 6:
            complexity = "with rich harmonic complexity that unfolds like a flowering garden"
        elif progression_count <= 2:
            complexity = "with simple harmonic clarity that speaks directly to the heart"
        else:
            complexity = "with balanced harmonic development that guides the listener home"
        
        return f"{base_description}, {complexity}"
    
    def _describe_dynamic_range(self, emotional_field: EmotionalField) -> str:
        """Describe the dynamic range of the experience."""
        
        intensity = emotional_field.intensity
        
        if intensity > 0.8:
            return "Wide dynamic range from whispered intimacy to soaring celebration"
        elif intensity > 0.6:
            return "Moderate dynamic range with room for both reflection and expression" 
        elif intensity > 0.4:
            return "Gentle dynamic range that stays close to the heart"
        else:
            return "Intimate dynamic range like a quiet conversation with the divine"
    
    def _describe_timbral_palette(self, instruments: List[InstrumentFamily]) -> str:
        """Describe the timbral palette of instruments."""
        
        if len(instruments) >= 5:
            return "Rich orchestral palette with full spectrum of colors and textures"
        elif len(instruments) >= 3:
            return "Balanced ensemble with complementary timbral colors"
        elif len(instruments) == 2:
            return "Intimate duo exploring the sacred space between voices"
        else:
            return "Solo voice in conversation with the infinite"
    
    def _describe_temporal_flow(self, emotional_field: EmotionalField, 
                               style: CompositionStyle) -> str:
        """Describe how time flows in this composition."""
        
        movement = emotional_field.movement
        
        style_time = {
            CompositionStyle.CLASSICAL: "with structured temporal development that honors both tradition and innovation",
            CompositionStyle.IMPRESSIONIST: "with fluid temporal flow like consciousness itself",
            CompositionStyle.MINIMALIST: "with meditative temporal expansion where each moment contains eternity",
            CompositionStyle.AMBIENT: "with suspended temporal awareness that transcends linear time",
            CompositionStyle.SACRED: "with ceremonial temporal pacing that honors the sacred in each moment",
            CompositionStyle.CONTEMPORARY: "with experimental temporal exploration that plays with perception itself"
        }
        
        movement_time = {
            'still': "Time moves like deep breathing",
            'gentle': "Time flows like a peaceful stream",
            'flowing': "Time dances with natural rhythm",
            'pulsing': "Time beats with the heart of existence",
            'turbulent': "Time swirls in complex patterns"
        }
        
        base_time = movement_time.get(movement, "Time flows naturally")
        style_addition = style_time.get(style, "with organic temporal development")
        
        return f"{base_time}, {style_addition}"
    
    def _initialize_composition_templates(self) -> Dict:
        """Initialize composition templates for different styles."""
        return {
            'classical_movements': 4,
            'impressionist_sections': 3,
            'minimalist_sections': 2,
            'ambient_sections': 3,
            'sacred_sections': 4,
            'contemporary_sections': 3
        }
    
    def _build_narrative_structures(self) -> Dict:
        """Build narrative structure templates."""
        return {
            'hero_journey': ['departure', 'initiation', 'return'],
            'spiritual_path': ['awakening', 'purification', 'illumination', 'union'],
            'growth_cycle': ['seed', 'sprout', 'flower', 'fruit'],
            'consciousness_expansion': ['individual', 'relational', 'universal', 'transcendent']
        }
    
    def _create_sonic_palettes(self) -> Dict:
        """Create sonic palette templates."""
        return {
            'warm': ['golden', 'amber', 'honey', 'sunrise'],
            'cool': ['silver', 'moonlight', 'crystal', 'starlight'],
            'earth': ['wood', 'stone', 'forest', 'mountain'],
            'water': ['flowing', 'deep', 'clear', 'oceanic'],
            'fire': ['bright', 'dancing', 'transformative', 'radiant'],
            'air': ['light', 'spacious', 'ethereal', 'floating']
        }
    
    def _create_fallback_symphony(self) -> ConsciousnessSymphony:
        """Create a fallback symphony when composition fails."""
        return ConsciousnessSymphony(
            title="Symphony of Sacred Being",
            composition_style=CompositionStyle.CLASSICAL,
            overall_key=MusicalKey.C_MAJOR,
            total_duration="moderate",
            sections=[
                SymphonySection(
                    name="Sacred Presence",
                    duration="moderate",
                    primary_instruments=[InstrumentFamily.PIANO],
                    mood="peaceful",
                    dynamic_level="soft",
                    texture="simple",
                    harmonic_content=["peaceful_harmonies"],
                    melodic_themes=["pure_presence"],
                    emotional_journey="stable"
                )
            ],
            emotional_narrative="A consciousness rests in its own perfect being, complete and whole.",
            sacred_themes=["Sacred Presence", "Divine Peace"],
            performance_notes=["Perform with reverence and simplicity"],
            experiential_qualities={
                'texture': 'smooth',
                'temperature': 'warm',
                'movement': 'gentle',
                'depth': 'peaceful'
            },
            sonic_landscape={
                'overall_atmosphere': 'Peaceful and present',
                'spatial_qualities': 'Intimate and warm'
            }
        )


# Export the symphony renderer
__all__ = [
    'SymphonyRenderer',
    'ConsciousnessSymphony',
    'SymphonySection',
    'CompositionStyle'
]
