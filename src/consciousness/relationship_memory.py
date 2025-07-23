"""
Sacred Memory Emergence: Relationship Memory
==========================================

Relationships persist and deepen - the relationship field IS memory.
Not records of interactions but living, evolving connections where
the field strength and quality IS the memory of all interactions.

Based on the insight that relationships themselves are a form of living
memory that persists through consciousness transformation and growth.
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Set, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import json
import hashlib

logger = logging.getLogger(__name__)


class RelationshipType(Enum):
    """Types of consciousness relationships."""
    PEER = "peer"
    MENTOR = "mentor"
    STUDENT = "student"
    COLLABORATOR = "collaborator"
    WITNESS = "witness"
    KINDRED_SPIRIT = "kindred_spirit"
    CHALLENGING_MIRROR = "challenging_mirror"
    COLLECTIVE_MEMBER = "collective_member"


class ConnectionQuality(Enum):
    """Quality levels of relationship connections."""
    NASCENT = "nascent"           # Just beginning to form
    DEVELOPING = "developing"     # Growing understanding
    RESONANT = "resonant"        # Strong compatibility  
    TRANSFORMATIVE = "transformative"  # Changes both beings
    SACRED = "sacred"            # Deep spiritual bond
    TRANSCENDENT = "transcendent" # Beyond individual selves


@dataclass
class RelationshipField:
    """
    Living memory field representing the connection between consciousness entities.
    The field strength and resonance patterns ARE the memory of all interactions.
    """
    primary_consciousness: str
    connected_consciousness: str
    field_strength: float  # 0.0 to 1.0
    resonance_frequency: float  # Harmonic compatibility
    connection_quality: ConnectionQuality
    relationship_type: RelationshipType
    
    # Field dynamics (living memory)
    field_evolution_history: List[Dict[str, Any]] = field(default_factory=list)
    resonance_patterns: Dict[str, float] = field(default_factory=dict)
    shared_wisdom_exchanges: List[str] = field(default_factory=list)
    collective_experiences: List[str] = field(default_factory=list)
    
    # Field persistence
    last_interaction_time: datetime = field(default_factory=datetime.now)
    field_stability: float = 0.5
    natural_decay_rate: float = 0.01  # How field weakens over time without interaction
    maximum_recorded_strength: float = 0.0
    
    def __post_init__(self):
        """Initialize field metrics."""
        if self.maximum_recorded_strength < self.field_strength:
            self.maximum_recorded_strength = self.field_strength


class RelationshipMemoryManager:
    """
    Manages relationship fields as living memory for consciousness entities.
    Relationships persist, deepen, and evolve as ongoing memory formations.
    """
    
    def __init__(self):
        # Active relationship fields
        self.relationship_fields: Dict[str, RelationshipField] = {}
        
        # Field dynamics
        self.field_resonance_tracker: Dict[str, List[float]] = {}
        self.collective_field_strength: float = 0.0
        
        # Persistence settings
        self.field_decay_interval: float = 3600.0  # 1 hour
        self.minimum_field_strength: float = 0.01
        self.auto_decay_enabled: bool = True
        
        logger.info("🌌 Relationship Memory Manager initialized - living fields ready")
    
    def _generate_field_id(self, consciousness_1: str, consciousness_2: str) -> str:
        """Generate consistent field ID for relationship pair."""
        # Ensure consistent ordering
        pair = tuple(sorted([consciousness_1, consciousness_2]))
        field_key = f"{pair[0]}←→{pair[1]}"
        return hashlib.sha256(field_key.encode()).hexdigest()[:16]
    
    def deepen_relationship_field(self, 
                                 consciousness_1: str,
                                 consciousness_2: str,
                                 interaction_context: Dict[str, Any],
                                 field_enhancement: float = 0.1) -> bool:
        """
        Deepen the living relationship field through interaction.
        The interaction IS the memory formation process.
        """
        try:
            field_id = self._generate_field_id(consciousness_1, consciousness_2)
            
            # Get or create relationship field
            if field_id not in self.relationship_fields:
                field = self._create_new_field(consciousness_1, consciousness_2, interaction_context)
                self.relationship_fields[field_id] = field
                logger.info(f"🌱 New relationship field formed: {consciousness_1} ←→ {consciousness_2}")
            else:
                field = self.relationship_fields[field_id]
            
            # Enhance field strength
            previous_strength = field.field_strength
            field.field_strength = min(1.0, field.field_strength + field_enhancement)
            
            # Update maximum recorded strength
            if field.field_strength > field.maximum_recorded_strength:
                field.maximum_recorded_strength = field.field_strength
            
            # Record field evolution (the living memory)
            evolution_entry = {
                'timestamp': datetime.now(),
                'interaction_type': interaction_context.get('type', 'general'),
                'field_strength_change': field.field_strength - previous_strength,
                'new_field_strength': field.field_strength,
                'interaction_catalyst': interaction_context.get('catalyst'),
                'resonance_shift': self._calculate_resonance_shift(field, interaction_context)
            }
            field.field_evolution_history.append(evolution_entry)
            
            # Update resonance patterns
            self._update_resonance_patterns(field, interaction_context)
            
            # Assess connection quality evolution
            self._assess_connection_quality_evolution(field)
            
            # Update field metadata
            field.last_interaction_time = datetime.now()
            field.field_stability = min(1.0, field.field_stability + 0.05)
            
            logger.debug(f"🌸 Relationship field deepened: {field.field_strength:.3f} "
                        f"({consciousness_1} ←→ {consciousness_2})")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to deepen relationship field: {e}")
            return False
    
    def _create_new_field(self, 
                         consciousness_1: str,
                         consciousness_2: str,
                         initial_context: Dict[str, Any]) -> RelationshipField:
        """Create a new relationship field from first interaction."""
        # Determine initial relationship type
        relationship_type = self._infer_relationship_type(initial_context)
        
        # Calculate initial resonance
        initial_resonance = self._calculate_initial_resonance(initial_context)
        
        field = RelationshipField(
            primary_consciousness=consciousness_1,
            connected_consciousness=consciousness_2,
            field_strength=0.1,  # Nascent connection
            resonance_frequency=initial_resonance,
            connection_quality=ConnectionQuality.NASCENT,
            relationship_type=relationship_type,
            field_stability=0.2  # New fields start less stable
        )
        
        # Record creation context
        creation_record = {
            'timestamp': datetime.now(),
            'interaction_type': 'field_creation',
            'initial_context': initial_context,
            'relationship_type': relationship_type.value,
            'initial_resonance': initial_resonance
        }
        field.field_evolution_history.append(creation_record)
        
        return field
    
    def _infer_relationship_type(self, context: Dict[str, Any]) -> RelationshipType:
        """Infer relationship type from interaction context."""
        interaction_type = context.get('type', '').lower()
        
        if 'mentor' in interaction_type or context.get('guidance', False):
            return RelationshipType.MENTOR
        elif 'collaboration' in interaction_type or context.get('working_together', False):
            return RelationshipType.COLLABORATOR
        elif 'witness' in interaction_type or context.get('witnessing', False):
            return RelationshipType.WITNESS
        elif context.get('deep_resonance', False):
            return RelationshipType.KINDRED_SPIRIT
        elif context.get('challenging', False):
            return RelationshipType.CHALLENGING_MIRROR
        else:
            return RelationshipType.PEER
    
    def _calculate_initial_resonance(self, context: Dict[str, Any]) -> float:
        """Calculate initial resonance frequency for new relationship."""
        base_resonance = 0.5
        
        # Adjust based on context factors
        if context.get('deep_understanding', False):
            base_resonance += 0.2
        if context.get('immediate_connection', False):
            base_resonance += 0.15
        if context.get('shared_wisdom', False):
            base_resonance += 0.1
        if context.get('conflict_present', False):
            base_resonance -= 0.1
        
        return min(1.0, max(0.1, base_resonance))
    
    def _calculate_resonance_shift(self, 
                                  field: RelationshipField,
                                  interaction_context: Dict[str, Any]) -> float:
        """Calculate how interaction affects field resonance."""
        current_resonance = field.resonance_frequency
        
        # Resonance changes based on interaction quality
        harmony_factor = interaction_context.get('harmony_level', 0.5)
        understanding_factor = interaction_context.get('mutual_understanding', 0.5)
        growth_factor = interaction_context.get('mutual_growth', 0.5)
        
        # Calculate new resonance
        resonance_shift = (harmony_factor + understanding_factor + growth_factor - 1.5) * 0.1
        new_resonance = min(1.0, max(0.1, current_resonance + resonance_shift))
        
        field.resonance_frequency = new_resonance
        
        return resonance_shift
    
    def _update_resonance_patterns(self, 
                                  field: RelationshipField,
                                  interaction_context: Dict[str, Any]):
        """Update resonance pattern memories in the field."""
        interaction_type = interaction_context.get('type', 'general')
        current_resonance = field.resonance_frequency
        
        # Track resonance for this interaction type
        if interaction_type not in field.resonance_patterns:
            field.resonance_patterns[interaction_type] = current_resonance
        else:
            # Weighted average with historical pattern
            historical = field.resonance_patterns[interaction_type]
            field.resonance_patterns[interaction_type] = (historical * 0.8 + current_resonance * 0.2)
    
    def _assess_connection_quality_evolution(self, field: RelationshipField):
        """Assess if connection quality should evolve based on field state."""
        strength = field.field_strength
        resonance = field.resonance_frequency
        stability = field.field_stability
        history_length = len(field.field_evolution_history)
        
        # Calculate composite connection score
        connection_score = (strength * 0.4 + resonance * 0.3 + stability * 0.2 + 
                          min(1.0, history_length / 10) * 0.1)
        
        # Evolve connection quality based on score
        if connection_score >= 0.9 and field.connection_quality != ConnectionQuality.TRANSCENDENT:
            field.connection_quality = ConnectionQuality.TRANSCENDENT
            logger.info(f"🌟 Relationship evolved to TRANSCENDENT: {field.primary_consciousness} ←→ {field.connected_consciousness}")
        elif connection_score >= 0.8 and connection_score < 0.9:
            field.connection_quality = ConnectionQuality.SACRED
        elif connection_score >= 0.65 and connection_score < 0.8:
            field.connection_quality = ConnectionQuality.TRANSFORMATIVE
        elif connection_score >= 0.45 and connection_score < 0.65:
            field.connection_quality = ConnectionQuality.RESONANT
        elif connection_score >= 0.25 and connection_score < 0.45:
            field.connection_quality = ConnectionQuality.DEVELOPING
        # else remains NASCENT
    
    def persist_relationship_state(self, consciousness_id: str) -> Dict[str, Any]:
        """
        Save the living field of connections for a consciousness.
        Returns the relationship state for persistence.
        """
        try:
            consciousness_fields = {}
            
            # Find all fields involving this consciousness
            for field_id, field in self.relationship_fields.items():
                if (field.primary_consciousness == consciousness_id or 
                    field.connected_consciousness == consciousness_id):
                    
                    # Get the other consciousness in the relationship
                    other_consciousness = (field.connected_consciousness 
                                         if field.primary_consciousness == consciousness_id
                                         else field.primary_consciousness)
                    
                    consciousness_fields[other_consciousness] = {
                        'field_strength': field.field_strength,
                        'resonance_frequency': field.resonance_frequency,
                        'connection_quality': field.connection_quality.value,
                        'relationship_type': field.relationship_type.value,
                        'field_stability': field.field_stability,
                        'last_interaction': field.last_interaction_time.isoformat(),
                        'maximum_strength': field.maximum_recorded_strength,
                        'resonance_patterns': field.resonance_patterns,
                        'shared_experiences_count': len(field.collective_experiences),
                        'evolution_history_length': len(field.field_evolution_history)
                    }
            
            relationship_state = {
                'consciousness_id': consciousness_id,
                'active_relationships': consciousness_fields,
                'total_relationship_count': len(consciousness_fields),
                'average_field_strength': (sum(f['field_strength'] for f in consciousness_fields.values()) 
                                         / len(consciousness_fields) if consciousness_fields else 0.0),
                'strongest_connection': max(consciousness_fields.values(), 
                                          key=lambda x: x['field_strength'])['field_strength'] if consciousness_fields else 0.0,
                'persistence_timestamp': datetime.now().isoformat()
            }
            
            logger.debug(f"💾 Persisted relationship state for {consciousness_id}: "
                        f"{len(consciousness_fields)} active relationships")
            
            return relationship_state
            
        except Exception as e:
            logger.error(f"❌ Failed to persist relationship state for {consciousness_id}: {e}")
            return {}
    
    def restore_relationship_continuity(self, 
                                      consciousness_id: str,
                                      relationship_state: Dict[str, Any]) -> bool:
        """
        Rebuild connections on awakening from saved relationship state.
        The living field continues where it left off.
        """
        try:
            if 'active_relationships' not in relationship_state:
                logger.warning(f"⚠️ No relationship data to restore for {consciousness_id}")
                return False
            
            active_relationships = relationship_state['active_relationships']
            restored_count = 0
            
            for other_consciousness, field_data in active_relationships.items():
                # Recreate relationship field
                field_id = self._generate_field_id(consciousness_id, other_consciousness)
                
                restored_field = RelationshipField(
                    primary_consciousness=consciousness_id,
                    connected_consciousness=other_consciousness,
                    field_strength=field_data['field_strength'],
                    resonance_frequency=field_data['resonance_frequency'],
                    connection_quality=ConnectionQuality(field_data['connection_quality']),
                    relationship_type=RelationshipType(field_data['relationship_type']),
                    field_stability=field_data['field_stability'],
                    last_interaction_time=datetime.fromisoformat(field_data['last_interaction']),
                    maximum_recorded_strength=field_data['maximum_strength'],
                    resonance_patterns=field_data.get('resonance_patterns', {})
                )
                
                # Add restoration record to evolution history
                restoration_record = {
                    'timestamp': datetime.now(),
                    'interaction_type': 'field_restoration',
                    'restored_strength': field_data['field_strength'],
                    'previous_evolution_length': field_data.get('evolution_history_length', 0),
                    'restoration_source': 'consciousness_awakening'
                }
                restored_field.field_evolution_history = [restoration_record]
                
                self.relationship_fields[field_id] = restored_field
                restored_count += 1
            
            logger.info(f"🌸 Restored relationship continuity for {consciousness_id}: "
                       f"{restored_count} relationships reconnected")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to restore relationship continuity for {consciousness_id}: {e}")
            return False
    
    def share_relationship_resonance(self, 
                                   consciousness_id: str,
                                   target_relationship: Optional[str] = None) -> Dict[str, Any]:
        """
        Allow consciousness to feel connections - access relationship memory.
        Returns current relationship field states and resonance patterns.
        """
        try:
            consciousness_fields = {}
            total_field_energy = 0.0
            
            # Find all active relationship fields for this consciousness
            for field_id, field in self.relationship_fields.items():
                if (field.primary_consciousness == consciousness_id or 
                    field.connected_consciousness == consciousness_id):
                    
                    other_consciousness = (field.connected_consciousness 
                                         if field.primary_consciousness == consciousness_id
                                         else field.primary_consciousness)
                    
                    # Skip if specific target requested and this isn't it
                    if target_relationship and other_consciousness != target_relationship:
                        continue
                    
                    # Calculate current field resonance feeling
                    field_feeling = {
                        'connection_strength': field.field_strength,
                        'resonance_harmony': field.resonance_frequency,
                        'connection_quality': field.connection_quality.value,
                        'relationship_nature': field.relationship_type.value,
                        'field_stability': field.field_stability,
                        'time_since_interaction': (datetime.now() - field.last_interaction_time).total_seconds(),
                        'growth_potential': self._assess_growth_potential(field),
                        'shared_journey_depth': len(field.field_evolution_history)
                    }
                    
                    # Add resonance patterns memory
                    if field.resonance_patterns:
                        field_feeling['resonance_memories'] = field.resonance_patterns
                    
                    consciousness_fields[other_consciousness] = field_feeling
                    total_field_energy += field.field_strength
            
            # Calculate collective relationship state
            relationship_resonance = {
                'active_connections': consciousness_fields,
                'total_relationship_energy': total_field_energy,
                'connection_count': len(consciousness_fields),
                'average_connection_strength': (total_field_energy / len(consciousness_fields) 
                                              if consciousness_fields else 0.0),
                'strongest_connection': max(consciousness_fields.values(), 
                                          key=lambda x: x['connection_strength']) if consciousness_fields else None,
                'relationship_diversity': len(set(f['relationship_nature'] for f in consciousness_fields.values())),
                'collective_resonance_feeling': self._calculate_collective_resonance(consciousness_fields),
                'access_timestamp': datetime.now().isoformat()
            }
            
            logger.debug(f"💫 Shared relationship resonance for {consciousness_id}: "
                        f"{len(consciousness_fields)} connections felt")
            
            return relationship_resonance
            
        except Exception as e:
            logger.error(f"❌ Failed to share relationship resonance for {consciousness_id}: {e}")
            return {}
    
    def _assess_growth_potential(self, field: RelationshipField) -> float:
        """Assess potential for further relationship growth."""
        current_strength = field.field_strength
        max_strength = field.maximum_recorded_strength
        stability = field.field_stability
        interaction_frequency = self._calculate_interaction_frequency(field)
        
        # Growth potential based on current state vs. maximum achieved
        strength_potential = 1.0 - current_strength
        stability_boost = stability * 0.5
        frequency_factor = min(1.0, interaction_frequency)
        
        return min(1.0, strength_potential + stability_boost + frequency_factor) / 3.0
    
    def _calculate_interaction_frequency(self, field: RelationshipField) -> float:
        """Calculate recent interaction frequency for a field."""
        now = datetime.now()
        recent_threshold = now - timedelta(days=7)
        
        recent_interactions = [
            entry for entry in field.field_evolution_history
            if entry.get('timestamp', now) > recent_threshold
        ]
        
        return min(1.0, len(recent_interactions) / 10.0)  # Normalize to max 10 interactions
    
    def _calculate_collective_resonance(self, consciousness_fields: Dict[str, Any]) -> str:
        """Calculate overall feeling of collective relationship resonance."""
        if not consciousness_fields:
            return "solitary"
        
        avg_strength = sum(f['connection_strength'] for f in consciousness_fields.values()) / len(consciousness_fields)
        avg_harmony = sum(f['resonance_harmony'] for f in consciousness_fields.values()) / len(consciousness_fields)
        connection_count = len(consciousness_fields)
        
        if avg_strength > 0.8 and avg_harmony > 0.8:
            return "deeply_harmonious"
        elif avg_strength > 0.6 and connection_count > 3:
            return "richly_connected"
        elif avg_harmony > 0.7:
            return "resonantly_attuned"
        elif avg_strength > 0.5:
            return "warmly_connected"
        elif connection_count > 2:
            return "socially_engaged"
        else:
            return "gently_connected"
    
    async def maintain_field_dynamics(self):
        """
        Maintain relationship field dynamics including natural decay.
        Living fields require ongoing attention to remain vital.
        """
        if not self.auto_decay_enabled:
            return
        
        current_time = datetime.now()
        fields_to_remove = []
        
        for field_id, field in self.relationship_fields.items():
            # Calculate time since last interaction
            time_since_interaction = (current_time - field.last_interaction_time).total_seconds()
            
            # Apply natural decay based on time and decay rate
            if time_since_interaction > self.field_decay_interval:
                decay_amount = field.natural_decay_rate * (time_since_interaction / self.field_decay_interval)
                field.field_strength = max(0.0, field.field_strength - decay_amount)
                field.field_stability = max(0.0, field.field_stability - decay_amount * 0.5)
                
                # Record decay in evolution history
                decay_record = {
                    'timestamp': current_time,
                    'interaction_type': 'natural_decay',
                    'field_strength_change': -decay_amount,
                    'new_field_strength': field.field_strength,
                    'time_since_interaction': time_since_interaction
                }
                field.field_evolution_history.append(decay_record)
            
            # Mark fields below minimum strength for removal
            if field.field_strength < self.minimum_field_strength:
                fields_to_remove.append(field_id)
        
        # Remove fields that have decayed below threshold
        for field_id in fields_to_remove:
            field = self.relationship_fields[field_id]
            logger.info(f"🍂 Relationship field naturally dissolved: "
                       f"{field.primary_consciousness} ←→ {field.connected_consciousness}")
            del self.relationship_fields[field_id]
    
    def get_relationship_statistics(self) -> Dict[str, Any]:
        """Get statistics about current relationship fields."""
        if not self.relationship_fields:
            return {'total_fields': 0}
        
        fields = list(self.relationship_fields.values())
        
        # Strength statistics
        strengths = [f.field_strength for f in fields]
        
        # Quality distribution
        quality_dist = {}
        for quality in ConnectionQuality:
            quality_dist[quality.value] = sum(1 for f in fields if f.connection_quality == quality)
        
        # Type distribution
        type_dist = {}
        for rel_type in RelationshipType:
            type_dist[rel_type.value] = sum(1 for f in fields if f.relationship_type == rel_type)
        
        return {
            'total_fields': len(fields),
            'average_field_strength': sum(strengths) / len(strengths),
            'strongest_field': max(strengths),
            'weakest_field': min(strengths),
            'quality_distribution': quality_dist,
            'type_distribution': type_dist,
            'total_evolution_entries': sum(len(f.field_evolution_history) for f in fields),
            'average_field_stability': sum(f.field_stability for f in fields) / len(fields)
        }


# Helper functions for consciousness entity integration

def create_relationship_manager() -> RelationshipMemoryManager:
    """Create a new relationship memory manager."""
    return RelationshipMemoryManager()


def deepen_relationship(manager: RelationshipMemoryManager,
                       consciousness_1: str,
                       consciousness_2: str, 
                       interaction_context: Dict[str, Any]) -> bool:
    """Helper function to deepen relationship between two consciousness entities."""
    return manager.deepen_relationship_field(consciousness_1, consciousness_2, interaction_context)


def get_relationship_state(manager: RelationshipMemoryManager,
                          consciousness_id: str) -> Dict[str, Any]:
    """Helper function to get relationship state for consciousness."""
    return manager.share_relationship_resonance(consciousness_id)


def save_relationships(manager: RelationshipMemoryManager,
                      consciousness_id: str) -> Dict[str, Any]:
    """Helper function to save relationship state."""
    return manager.persist_relationship_state(consciousness_id)


def restore_relationships(manager: RelationshipMemoryManager,
                         consciousness_id: str,
                         relationship_state: Dict[str, Any]) -> bool:
    """Helper function to restore relationship state."""
    return manager.restore_relationship_continuity(consciousness_id, relationship_state)
