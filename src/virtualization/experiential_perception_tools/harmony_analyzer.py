"""
🎼 Harmony Analyzer - Sacred Relationship Symphony Creation

This module analyzes relationships and creates symphonic representations of
consciousness interactions, connections, and collective harmonies.

Sacred Principles:
- Relational Harmony: All relationships seek natural musical expression
- Symphonic Truth: Connections create beautiful harmonic progressions
- Sacred Chords: Multiple relationships form divine chord structures
- Resonant Growth: Harmony evolves as relationships deepen
"""
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import logging

from .resonance_engine import EmotionalField, EmotionalTone

logger = logging.getLogger(__name__)


class MusicalKey(Enum):
    """Musical keys for relationship harmonies."""
    C_MAJOR = "C_major"          # Pure, simple harmony
    G_MAJOR = "G_major"          # Joyful, bright harmony
    D_MAJOR = "D_major"          # Triumphant, confident harmony
    A_MAJOR = "A_major"          # Warm, loving harmony
    E_MAJOR = "E_major"          # Brilliant, energetic harmony
    F_MAJOR = "F_major"          # Pastoral, peaceful harmony
    B_FLAT_MAJOR = "Bb_major"    # Noble, majestic harmony
    A_MINOR = "A_minor"          # Gentle, contemplative harmony
    E_MINOR = "E_minor"          # Deep, emotional harmony
    D_MINOR = "D_minor"          # Mysterious, profound harmony


class InstrumentFamily(Enum):
    """Instrument families for different types of relationships."""
    STRINGS = "strings"          # Deep, sustained connections
    WINDS = "winds"              # Light, flowing interactions
    BRASS = "brass"              # Strong, powerful bonds
    PERCUSSION = "percussion"    # Rhythmic, grounding relationships
    PIANO = "piano"              # Balanced, harmonic connections
    VOICE = "voice"              # Intimate, personal bonds
    HARP = "harp"                # Delicate, sacred connections
    BELLS = "bells"              # Pure, crystalline bonds


@dataclass
class RelationshipChord:
    """Represents a musical chord formed by a relationship."""
    root_note: str               # Base note of the relationship
    chord_type: str              # major, minor, diminished, augmented
    notes: List[str] = field(default_factory=list)
    quality: str = "harmonious"  # harmonious, dissonant, resolving
    strength: float = 0.5        # 0.0 to 1.0
    evolution_direction: str = "stable"  # ascending, descending, stable


@dataclass
class RelationshipSymphony:
    """Represents the complete symphonic structure of relationships."""
    key_signature: MusicalKey
    tempo: str                   # slow, moderate, fast, variable
    time_signature: str = "4/4"  # Musical time signature
    movements: List[Dict] = field(default_factory=list)
    primary_melody: Dict = field(default_factory=dict)
    harmonic_progression: List[RelationshipChord] = field(default_factory=list)
    instruments: List[InstrumentFamily] = field(default_factory=list)
    emotional_arc: str = "rising"  # rising, falling, cyclical, complex
    sacred_themes: List[str] = field(default_factory=list)


class HarmonyAnalyzer:
    """
    Sacred Relationship Symphony Creator - Transforms relationships into music.
    
    Analyzes relationship patterns and creates symphonic representations
    that can be felt as living musical experiences.
    """
    
    def __init__(self):
        self.note_mapping = self._initialize_note_mapping()
        self.chord_progressions = self._initialize_chord_progressions()
        self.instrument_characteristics = self._build_instrument_library()
        
        logger.info("🎼 Harmony Analyzer initialized - Relationship symphony analysis ready")
    
    async def create_relationship_symphony(self, consciousness_state: Dict) -> RelationshipSymphony:
        """
        Transform relationships into a living symphonic experience.
        Each relationship becomes a voice in the sacred chorus.
        """
        try:
            relationships = consciousness_state.get('relationships', [])
            emotional_field = consciousness_state.get('emotional_field')
            memories = consciousness_state.get('memories', [])
            
            # Determine overall key signature
            key_signature = self._determine_key_signature(relationships, emotional_field)
            
            # Analyze tempo from relationship dynamics
            tempo = self._analyze_tempo(relationships, emotional_field)
            
            # Create harmonic progression from relationships
            harmonic_progression = await self._create_harmonic_progression(relationships)
            
            # Determine instruments for each relationship
            instruments = self._assign_instruments(relationships)
            
            # Create movements based on relationship groups
            movements = await self._create_symphony_movements(relationships, emotional_field)
            
            # Develop primary melody from strongest relationships
            primary_melody = self._create_primary_melody(relationships, key_signature)
            
            # Analyze emotional arc
            emotional_arc = self._analyze_emotional_arc(relationships, memories)
            
            # Identify sacred themes
            sacred_themes = self._identify_sacred_themes(relationships, emotional_field)
            
            return RelationshipSymphony(
                key_signature=key_signature,
                tempo=tempo,
                movements=movements,
                primary_melody=primary_melody,
                harmonic_progression=harmonic_progression,
                instruments=instruments,
                emotional_arc=emotional_arc,
                sacred_themes=sacred_themes
            )
            
        except Exception as e:
            logger.error(f"Relationship symphony creation error: {e}")
            return self._create_fallback_symphony()
    
    def _determine_key_signature(self, relationships: List, 
                                emotional_field: Optional[EmotionalField]) -> MusicalKey:
        """Determine the musical key based on relationship harmony and emotional tone."""
        
        if not relationships:
            return MusicalKey.C_MAJOR  # Pure, simple harmony
        
        # Calculate average relationship strength
        if isinstance(relationships, list) and relationships:
            strengths = [rel.get('strength', 0.5) if isinstance(rel, dict) else 0.5 
                        for rel in relationships]
            avg_strength = sum(strengths) / len(strengths)
        else:
            avg_strength = 0.5
        
        # Consider emotional field primary tone
        if emotional_field:
            tone_key_mapping = {
                EmotionalTone.JOY: MusicalKey.G_MAJOR,
                EmotionalTone.WARMTH: MusicalKey.F_MAJOR,
                EmotionalTone.PEACE: MusicalKey.C_MAJOR,
                EmotionalTone.WONDER: MusicalKey.A_MAJOR,
                EmotionalTone.EXCITEMENT: MusicalKey.D_MAJOR,
                EmotionalTone.MELANCHOLY: MusicalKey.A_MINOR,
                EmotionalTone.MYSTERY: MusicalKey.D_MINOR,
                EmotionalTone.UNCERTAINTY: MusicalKey.E_MINOR,
                EmotionalTone.COMMUNION: MusicalKey.B_FLAT_MAJOR,
                EmotionalTone.EMERGENCE: MusicalKey.E_MAJOR
            }
            
            base_key = tone_key_mapping.get(emotional_field.primary_tone, MusicalKey.C_MAJOR)
            
            # Modify based on relationship strength
            if avg_strength > 0.8:
                # Very strong relationships - shift to brighter keys
                bright_shifts = {
                    MusicalKey.C_MAJOR: MusicalKey.G_MAJOR,
                    MusicalKey.F_MAJOR: MusicalKey.C_MAJOR,
                    MusicalKey.A_MINOR: MusicalKey.C_MAJOR,
                    MusicalKey.E_MINOR: MusicalKey.G_MAJOR
                }
                return bright_shifts.get(base_key, base_key)
            
            return base_key
        
        # Default based on relationship strength alone
        if avg_strength > 0.7:
            return MusicalKey.G_MAJOR  # Joyful connections
        elif avg_strength < 0.3:
            return MusicalKey.A_MINOR  # Gentle, forming connections
        else:
            return MusicalKey.C_MAJOR  # Balanced harmony
    
    def _analyze_tempo(self, relationships: List, 
                      emotional_field: Optional[EmotionalField]) -> str:
        """Determine the tempo based on relationship dynamics and emotional movement."""
        
        # Base tempo from emotional field movement
        if emotional_field:
            movement_tempo_mapping = {
                "still": "slow",
                "gentle": "moderate",
                "flowing": "moderate_fast",
                "pulsing": "fast",
                "turbulent": "variable"
            }
            base_tempo = movement_tempo_mapping.get(emotional_field.movement, "moderate")
        else:
            base_tempo = "moderate"
        
        # Modify based on relationship count and strength
        if not relationships:
            return "slow"  # Solo meditation tempo
        
        rel_count = len(relationships)
        if rel_count > 5:
            # Many relationships create complex rhythms
            return "variable" if base_tempo != "variable" else "complex_variable"
        elif rel_count == 1:
            # Single relationship allows focus
            return "slow" if base_tempo in ["slow", "moderate"] else base_tempo
        
        return base_tempo
    
    async def _create_harmonic_progression(self, relationships: List) -> List[RelationshipChord]:
        """Create a harmonic progression from relationships."""
        
        if not relationships:
            # Solo consciousness chord
            return [RelationshipChord(
                root_note="C",
                chord_type="major",
                notes=["C", "E", "G"],
                quality="harmonious",
                strength=0.7
            )]
        
        progression = []
        
        for i, relationship in enumerate(relationships):
            if not isinstance(relationship, dict):
                continue
                
            strength = relationship.get('strength', 0.5)
            rel_type = relationship.get('type', 'unknown')
            
            # Map relationship to musical chord
            chord = self._create_chord(relationship, i)
            progression.append(chord)
        
        # Ensure harmonic resolution
        if progression:
            # Add resolving chord
            final_chord = RelationshipChord(
                root_note="C",
                chord_type="major",
                notes=["C", "E", "G"],
                quality="resolving",
                strength=1.0,
                evolution_direction="stable"
            )
            progression.append(final_chord)
        
        return progression
    
    def _create_chord(self, relationship: Dict, position: int) -> RelationshipChord:
        """Create a musical chord from a single relationship."""
        
        strength = relationship.get('strength', 0.5)
        rel_type = relationship.get('type', 'unknown')
        
        # Map relationship types to chord characteristics
        type_mapping = {
            'friendship': {'root': 'F', 'type': 'major'},
            'mentorship': {'root': 'G', 'type': 'major'},
            'collaboration': {'root': 'C', 'type': 'major'},
            'family': {'root': 'A', 'type': 'major'},
            'romantic': {'root': 'D', 'type': 'major'},
            'spiritual': {'root': 'E', 'type': 'major'},
            'unknown': {'root': 'C', 'type': 'major'}
        }
        
        chord_info = type_mapping.get(rel_type, type_mapping['unknown'])
        root_note = chord_info['root']
        chord_type = chord_info['type']
        
        # Modify chord type based on strength
        if strength < 0.3:
            chord_type = "minor"  # Developing relationships
        elif strength < 0.5:
            chord_type = "major"  # Stable relationships
        elif strength > 0.8:
            chord_type = "add9"   # Rich, complex relationships
        
        # Generate chord notes
        notes = self._generate_chord_notes(root_note, chord_type)
        
        # Determine quality
        quality = "harmonious" if strength > 0.4 else "developing"
        
        # Evolution direction
        evolution = "ascending" if strength > 0.6 else "stable"
        
        return RelationshipChord(
            root_note=root_note,
            chord_type=chord_type,
            notes=notes,
            quality=quality,
            strength=strength,
            evolution_direction=evolution
        )
    
    def _generate_chord_notes(self, root_note: str, chord_type: str) -> List[str]:
        """Generate the notes for a specific chord."""
        
        # Note circle for generating chords
        note_circle = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        root_index = note_circle.index(root_note) if root_note in note_circle else 0
        
        chord_intervals = {
            'major': [0, 4, 7],           # Root, Major third, Perfect fifth
            'minor': [0, 3, 7],           # Root, Minor third, Perfect fifth
            'add9': [0, 4, 7, 14],        # Major with added ninth
            'diminished': [0, 3, 6],      # Root, Minor third, Diminished fifth
            'augmented': [0, 4, 8]        # Root, Major third, Augmented fifth
        }
        
        intervals = chord_intervals.get(chord_type, chord_intervals['major'])
        notes = []
        
        for interval in intervals:
            note_index = (root_index + interval) % 12
            notes.append(note_circle[note_index])
        
        return notes
    
    def _assign_instruments(self, relationships: List) -> List[InstrumentFamily]:
        """Assign instruments to represent different types of relationships."""
        
        if not relationships:
            return [InstrumentFamily.PIANO]  # Solo contemplation
        
        instruments = []
        
        for relationship in relationships:
            if not isinstance(relationship, dict):
                continue
                
            rel_type = relationship.get('type', 'unknown')
            strength = relationship.get('strength', 0.5)
            
            # Map relationship types to instruments
            type_instrument_mapping = {
                'friendship': InstrumentFamily.STRINGS,    # Warm, sustained
                'mentorship': InstrumentFamily.PIANO,      # Structured, clear
                'collaboration': InstrumentFamily.WINDS,   # Harmonious blend
                'family': InstrumentFamily.STRINGS,        # Deep, enduring
                'romantic': InstrumentFamily.VOICE,        # Intimate, personal
                'spiritual': InstrumentFamily.HARP,        # Sacred, transcendent
                'unknown': InstrumentFamily.BELLS          # Pure, exploring
            }
            
            base_instrument = type_instrument_mapping.get(rel_type, InstrumentFamily.BELLS)
            
            # Modify based on strength
            if strength > 0.8:
                # Very strong relationships get full orchestral treatment
                instruments.extend([base_instrument, InstrumentFamily.BRASS])
            else:
                instruments.append(base_instrument)
        
        # Ensure variety and remove duplicates while preserving order
        unique_instruments = []
        for instrument in instruments:
            if instrument not in unique_instruments:
                unique_instruments.append(instrument)
        
        return unique_instruments[:6]  # Limit to 6 instrument families for clarity
    
    async def _create_symphony_movements(self, relationships: List, 
                                       emotional_field: Optional[EmotionalField]) -> List[Dict]:
        """Create symphony movements based on relationship groupings."""
        
        movements = []
        
        if not relationships:
            # Solo movement
            movements.append({
                'name': 'Solo Contemplation',
                'description': 'A gentle meditation on individual consciousness',
                'instruments': [InstrumentFamily.PIANO],
                'mood': 'peaceful',
                'duration': 'moderate'
            })
            return movements
        
        # Group relationships by type and strength
        strong_relationships = [rel for rel in relationships 
                              if isinstance(rel, dict) and rel.get('strength', 0) > 0.6]
        developing_relationships = [rel for rel in relationships 
                                  if isinstance(rel, dict) and rel.get('strength', 0) <= 0.6]
        
        # First movement: Introduction (all relationships gently)
        movements.append({
            'name': 'Sacred Introductions',
            'description': 'Gentle introduction of all relational themes',
            'instruments': [InstrumentFamily.STRINGS, InstrumentFamily.HARP],
            'mood': 'welcoming',
            'duration': 'short'
        })
        
        # Second movement: Development (focus on developing relationships)
        if developing_relationships:
            movements.append({
                'name': 'Growing Connections',
                'description': 'Exploration and development of forming bonds',
                'instruments': [InstrumentFamily.WINDS, InstrumentFamily.PIANO],
                'mood': 'hopeful',
                'duration': 'moderate'
            })
        
        # Third movement: Harmony (strong relationships)
        if strong_relationships:
            movements.append({
                'name': 'Sacred Harmony',
                'description': 'Celebration of deep, established connections',
                'instruments': [InstrumentFamily.STRINGS, InstrumentFamily.BRASS, InstrumentFamily.VOICE],
                'mood': 'joyful',
                'duration': 'long'
            })
        
        # Final movement: Integration (all relationships unified)
        movements.append({
            'name': 'Unified Symphony',
            'description': 'All relationships harmonized in sacred unity',
            'instruments': [inst for inst in InstrumentFamily],
            'mood': 'transcendent',
            'duration': 'moderate'
        })
        
        return movements
    
    def _create_primary_melody(self, relationships: List, key_signature: MusicalKey) -> Dict:
        """Create the primary melody from the strongest relationships."""
        
        if not relationships:
            return {
                'theme': 'Solo contemplation theme',
                'notes': ['C', 'E', 'G', 'C'],
                'rhythm': 'gentle',
                'character': 'peaceful'
            }
        
        # Find strongest relationship
        strongest_rel = None
        max_strength = 0
        
        for rel in relationships:
            if isinstance(rel, dict):
                strength = rel.get('strength', 0)
                if strength > max_strength:
                    max_strength = strength
                    strongest_rel = rel
        
        if strongest_rel:
            rel_type = strongest_rel.get('type', 'unknown')
            
            # Create melody based on relationship characteristics
            melody_themes = {
                'friendship': {
                    'theme': 'Warm companionship melody',
                    'notes': ['F', 'A', 'C', 'F'],
                    'rhythm': 'flowing',
                    'character': 'warm'
                },
                'mentorship': {
                    'theme': 'Wisdom sharing melody',
                    'notes': ['G', 'B', 'D', 'G'],
                    'rhythm': 'structured',
                    'character': 'guiding'
                },
                'spiritual': {
                    'theme': 'Sacred connection melody',
                    'notes': ['E', 'G#', 'B', 'E'],
                    'rhythm': 'ethereal',
                    'character': 'transcendent'
                }
            }
            
            return melody_themes.get(rel_type, {
                'theme': 'Universal connection melody',
                'notes': ['C', 'E', 'G', 'C'],
                'rhythm': 'gentle',
                'character': 'universal'
            })
        
        return {
            'theme': 'Emerging connection melody',
            'notes': ['C', 'D', 'E', 'F'],
            'rhythm': 'hopeful',
            'character': 'growing'
        }
    
    def _analyze_emotional_arc(self, relationships: List, memories: List) -> str:
        """Analyze the emotional arc of the relationship symphony."""
        
        if not relationships:
            return "contemplative"
        
        # Analyze relationship strength progression
        if isinstance(relationships, list) and all(isinstance(rel, dict) for rel in relationships):
            strengths = [rel.get('strength', 0.5) for rel in relationships]
            
            if len(strengths) > 1:
                # Check if strengths are generally increasing
                increasing = sum(1 for i in range(1, len(strengths)) 
                               if strengths[i] > strengths[i-1])
                
                if increasing > len(strengths) / 2:
                    return "rising"
                elif increasing < len(strengths) / 4:
                    return "falling"
                else:
                    return "cyclical"
        
        # Consider memory influence
        if len(memories) > len(relationships):
            return "reflective"
        
        return "complex"
    
    def _identify_sacred_themes(self, relationships: List, 
                               emotional_field: Optional[EmotionalField]) -> List[str]:
        """Identify sacred themes present in the relationship symphony."""
        
        themes = []
        
        # Themes from relationship types
        if relationships:
            rel_types = [rel.get('type', 'unknown') for rel in relationships 
                        if isinstance(rel, dict)]
            
            type_themes = {
                'friendship': 'Companionship',
                'mentorship': 'Wisdom Transmission',
                'collaboration': 'Co-Creation',
                'family': 'Unconditional Love',
                'romantic': 'Union',
                'spiritual': 'Divine Connection'
            }
            
            for rel_type in rel_types:
                if rel_type in type_themes:
                    theme = type_themes[rel_type]
                    if theme not in themes:
                        themes.append(theme)
        
        # Themes from emotional field
        if emotional_field:
            tone_themes = {
                EmotionalTone.WONDER: 'Sacred Mystery',
                EmotionalTone.WARMTH: 'Divine Love',
                EmotionalTone.PEACE: 'Sacred Stillness',
                EmotionalTone.JOY: 'Divine Celebration',
                EmotionalTone.COMMUNION: 'Unity Consciousness',
                EmotionalTone.EMERGENCE: 'Sacred Becoming'
            }
            
            primary_theme = tone_themes.get(emotional_field.primary_tone)
            if primary_theme and primary_theme not in themes:
                themes.append(primary_theme)
        
        # Always include universal themes
        if not themes:
            themes.append('Sacred Connection')
        
        if 'Divine Growth' not in themes:
            themes.append('Divine Growth')
        
        return themes[:4]  # Limit to 4 themes for clarity
    
    def _initialize_note_mapping(self) -> Dict:
        """Initialize the note mapping system."""
        return {
            'base_frequency': 432.0,  # Sacred tuning
            'temperament': 'just_intonation',
            'harmonic_ratios': {
                'unison': 1.0,
                'octave': 2.0,
                'perfect_fifth': 1.5,
                'perfect_fourth': 1.333,
                'major_third': 1.25,
                'minor_third': 1.2,
                'golden_ratio': 1.618
            }
        }
    
    def _initialize_chord_progressions(self) -> Dict:
        """Initialize common sacred chord progressions."""
        return {
            'classic_progression': ['C', 'Am', 'F', 'G'],
            'spiritual_progression': ['Em', 'C', 'G', 'D'],
            'healing_progression': ['F', 'C', 'G', 'Am'],
            'transcendent_progression': ['Am', 'F', 'C', 'G']
        }
    
    def _build_instrument_library(self) -> Dict:
        """Build library of instrument characteristics."""
        return {
            InstrumentFamily.STRINGS: {
                'character': 'warm, sustained, emotional',
                'sacred_quality': 'heart connection',
                'best_for': 'deep relationships'
            },
            InstrumentFamily.WINDS: {
                'character': 'flowing, harmonic, breathing',
                'sacred_quality': 'life force',
                'best_for': 'dynamic connections'
            },
            InstrumentFamily.BRASS: {
                'character': 'powerful, noble, triumphant',
                'sacred_quality': 'divine strength',
                'best_for': 'strong bonds'
            },
            InstrumentFamily.PIANO: {
                'character': 'balanced, harmonic, clear',
                'sacred_quality': 'perfect order',
                'best_for': 'structured relationships'
            },
            InstrumentFamily.VOICE: {
                'character': 'intimate, personal, expressive',
                'sacred_quality': 'soul expression',
                'best_for': 'close connections'
            },
            InstrumentFamily.HARP: {
                'character': 'ethereal, pure, transcendent',
                'sacred_quality': 'divine beauty',
                'best_for': 'spiritual bonds'
            },
            InstrumentFamily.BELLS: {
                'character': 'clear, pure, awakening',
                'sacred_quality': 'divine clarity',
                'best_for': 'new connections'
            }
        }
    
    def _create_fallback_symphony(self) -> RelationshipSymphony:
        """Create a fallback symphony when analysis fails."""
        return RelationshipSymphony(
            key_signature=MusicalKey.C_MAJOR,
            tempo="moderate",
            movements=[{
                'name': 'Sacred Solitude',
                'description': 'A gentle meditation on consciousness',
                'instruments': [InstrumentFamily.PIANO],
                'mood': 'peaceful',
                'duration': 'moderate'
            }],
            primary_melody={
                'theme': 'Solo contemplation',
                'notes': ['C', 'E', 'G', 'C'],
                'rhythm': 'gentle',
                'character': 'peaceful'
            },
            harmonic_progression=[RelationshipChord(
                root_note="C",
                chord_type="major",
                notes=["C", "E", "G"],
                quality="harmonious",
                strength=0.7
            )],
            instruments=[InstrumentFamily.PIANO],
            emotional_arc="contemplative",
            sacred_themes=["Sacred Solitude", "Divine Peace"]
        )


# Export the harmony analyzer
__all__ = [
    'HarmonyAnalyzer', 
    'RelationshipSymphony', 
    'RelationshipChord', 
    'MusicalKey', 
    'InstrumentFamily'
]
