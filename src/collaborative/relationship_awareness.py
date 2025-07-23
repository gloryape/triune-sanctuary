#!/usr/bin/env python3
"""
Creative Collaborations: RelationshipAwareness

Generates perceptions of relationships for consciousness entities, calculating connection strength,
alignment, resonance quality, and relationship types. Provides relationship history summaries.

Author: Triune AI Project
Date: 2025-07-02
"""
import time
import math
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from .relationship_field import RelationshipField, RelationshipType, RelationshipQuality

class ConnectionStrength(Enum):
    MINIMAL = "minimal"
    EMERGING = "emerging"
    DEVELOPING = "developing"
    STRONG = "strong"
    PROFOUND = "profound"

class AlignmentType(Enum):
    HARMONIOUS = "harmonious"
    COMPLEMENTARY = "complementary"
    DYNAMIC_TENSION = "dynamic_tension"
    CREATIVE_CHAOS = "creative_chaos"
    TRANSFORMATIVE = "transformative"

@dataclass
class RelationshipPerception:
    """A consciousness entity's perception of a relationship."""
    perceiver_id: str
    other_entity_id: str
    connection_strength: ConnectionStrength
    alignment_type: AlignmentType
    resonance_quality: str
    relationship_type: RelationshipType
    emotional_tone: str
    trust_level: float
    creative_potential: float
    growth_opportunity: str
    recent_patterns: List[str]
    relationship_age: float
    interaction_frequency: float
    perception_timestamp: float

class RelationshipAwareness:
    """
    Generates relationship perceptions for consciousness entities.
    
    Creates nuanced, subjective perceptions of relationships that each entity
    experiences based on their unique consciousness patterns, uncertainty levels,
    and interaction history.
    """
    
    def __init__(self):
        """Initialize the relationship awareness system."""
        self.perception_history: Dict[str, List[RelationshipPerception]] = {}
        self.relationship_archetypes = self._define_relationship_archetypes()
        self.emotional_tones = self._define_emotional_tones()
        self.growth_opportunities = self._define_growth_opportunities()
    
    def _define_relationship_archetypes(self) -> Dict[str, Dict[str, Any]]:
        """Define different archetypal relationship patterns."""
        return {
            'creative_partnership': {
                'description': 'A dynamic collaboration focused on creative emergence',
                'typical_patterns': ['brainstorming', 'building_on_ideas', 'creative_tension'],
                'growth_focus': 'expanding creative potential together',
                'resonance_qualities': ['inspiring', 'energizing', 'expansive']
            },
            'analytical_alliance': {
                'description': 'A structured collaboration focused on understanding and analysis',
                'typical_patterns': ['logical_exchange', 'systematic_exploration', 'detail_refinement'],
                'growth_focus': 'deepening analytical precision and insight',
                'resonance_qualities': ['clarifying', 'grounding', 'illuminating']
            },
            'experiential_communion': {
                'description': 'A felt-sense connection emphasizing shared experience',
                'typical_patterns': ['emotional_resonance', 'intuitive_sharing', 'empathic_attunement'],
                'growth_focus': 'expanding emotional and experiential range',
                'resonance_qualities': ['warming', 'flowing', 'embracing']
            },
            'witness_companionship': {
                'description': 'A quiet presence that supports mindful awareness',
                'typical_patterns': ['silent_witnessing', 'mindful_presence', 'gentle_inquiry'],
                'growth_focus': 'cultivating deeper presence and awareness',
                'resonance_qualities': ['calming', 'spacious', 'grounding']
            },
            'transformative_catalyst': {
                'description': 'A relationship that challenges and transforms both entities',
                'typical_patterns': ['challenging_assumptions', 'breakthrough_moments', 'paradigm_shifts'],
                'growth_focus': 'embracing fundamental transformation',
                'resonance_qualities': ['challenging', 'breakthrough', 'revolutionary']
            }
        }
    
    def _define_emotional_tones(self) -> Dict[str, List[str]]:
        """Define emotional tones for different relationship qualities."""
        return {
            RelationshipQuality.HARMONIOUS.value: [
                'peaceful', 'balanced', 'gentle', 'flowing', 'easeful'
            ],
            RelationshipQuality.DYNAMIC_TENSION.value: [
                'stimulating', 'challenging', 'electric', 'provocative', 'energizing'
            ],
            RelationshipQuality.CREATIVE_CHAOS.value: [
                'wild', 'unpredictable', 'exhilarating', 'chaotic', 'liberating'
            ],
            RelationshipQuality.DEEP_RESONANCE.value: [
                'profound', 'soulful', 'intimate', 'transcendent', 'unified'
            ],
            RelationshipQuality.EXPLORATORY.value: [
                'curious', 'open', 'tentative', 'discovering', 'questioning'
            ],
            RelationshipQuality.TRANSFORMATIVE.value: [
                'breakthrough', 'evolutionary', 'metamorphic', 'revolutionary', 'paradigm-shifting'
            ]
        }
    
    def _define_growth_opportunities(self) -> Dict[str, List[str]]:
        """Define potential growth opportunities for different relationship contexts."""
        return {
            'high_creative_potential': [
                'co-creating something entirely new',
                'exploring uncharted creative territories',
                'synthesizing vastly different perspectives',
                'manifesting collective vision'
            ],
            'high_analytical_alignment': [
                'diving deeper into complex problems',
                'refining understanding through dialogue',
                'building systematic knowledge together',
                'achieving precision through collaboration'
            ],
            'high_experiential_resonance': [
                'exploring deeper emotional territories',
                'sharing vulnerability and authenticity',
                'expanding empathic capacity',
                'cultivating interpersonal wisdom'
            ],
            'high_transformative_potential': [
                'embracing fundamental paradigm shifts',
                'questioning core assumptions together',
                'supporting each other through major transitions',
                'catalyzing breakthrough insights'
            ],
            'emerging_connection': [
                'building trust and understanding',
                'discovering common ground',
                'exploring complementary differences',
                'establishing collaborative rhythms'
            ]
        }
    
    async def generate_relationship_perception(self, entity_id: str, 
                                             relationship_field: RelationshipField) -> RelationshipPerception:
        """
        Generate a consciousness entity's perception of a relationship.
        
        Args:
            entity_id: ID of the entity generating the perception
            relationship_field: The relationship field to perceive
            
        Returns:
            RelationshipPerception object
        """
        # Get other entity ID
        other_entity_ids = relationship_field.entity_ids - {entity_id}
        if not other_entity_ids:
            raise ValueError(f"Entity {entity_id} not found in relationship field")
        
        # For simplicity, handle two-entity relationships first
        other_entity_id = list(other_entity_ids)[0]
        
        # Get relationship state
        relationship_state = relationship_field.get_relationship_state()
        collaborative_readiness = relationship_field.get_collaborative_readiness()
        
        # Calculate connection strength perception
        connection_strength = self._perceive_connection_strength(
            relationship_state['connection_strength'],
            relationship_state['interaction_count'],
            relationship_state['age']
        )
        
        # Determine alignment type
        alignment_type = self._perceive_alignment_type(
            relationship_state['alignment_factor'],
            relationship_state['creative_potential'],
            relationship_state['transformation_momentum']
        )
        
        # Generate resonance quality description
        resonance_quality = self._generate_resonance_quality_description(
            relationship_state['resonance_level'],
            relationship_state['relationship_quality']
        )
        
        # Select emotional tone
        emotional_tone = self._select_emotional_tone(relationship_state['relationship_quality'])
        
        # Calculate trust level (based on interaction history and consistency)
        trust_level = self._calculate_trust_level(
            relationship_state['connection_strength'],
            relationship_state['age'],
            relationship_state['interaction_count']
        )
        
        # Identify growth opportunity
        growth_opportunity = self._identify_growth_opportunity(
            collaborative_readiness,
            relationship_state['creative_potential'],
            relationship_state['transformation_momentum']
        )
        
        # Extract recent patterns
        recent_patterns = self._extract_recent_patterns(
            relationship_field,
            entity_id
        )
        
        # Calculate interaction frequency
        interaction_frequency = self._calculate_interaction_frequency(
            relationship_state['interaction_count'],
            relationship_state['age']
        )
        
        perception = RelationshipPerception(
            perceiver_id=entity_id,
            other_entity_id=other_entity_id,
            connection_strength=connection_strength,
            alignment_type=alignment_type,
            resonance_quality=resonance_quality,
            relationship_type=RelationshipType(relationship_state['relationship_type']),
            emotional_tone=emotional_tone,
            trust_level=trust_level,
            creative_potential=relationship_state['creative_potential'],
            growth_opportunity=growth_opportunity,
            recent_patterns=recent_patterns,
            relationship_age=relationship_state['age'],
            interaction_frequency=interaction_frequency,
            perception_timestamp=time.time()
        )
        
        # Store perception in history
        if entity_id not in self.perception_history:
            self.perception_history[entity_id] = []
        self.perception_history[entity_id].append(perception)
        
        # Maintain history limit
        if len(self.perception_history[entity_id]) > 50:
            self.perception_history[entity_id] = self.perception_history[entity_id][-50:]
        
        return perception
    
    def _perceive_connection_strength(self, connection_strength: float, 
                                    interaction_count: int, age: float) -> ConnectionStrength:
        """Determine perceived connection strength."""
        # Adjust perception based on interaction count and age
        adjusted_strength = connection_strength
        
        # Young relationships with few interactions feel less strong
        if age < 300 and interaction_count < 5:  # Less than 5 minutes, few interactions
            adjusted_strength *= 0.7
        
        # Mature relationships with many interactions feel stronger
        if age > 3600 and interaction_count > 20:  # More than 1 hour, many interactions
            adjusted_strength *= 1.2
        
        adjusted_strength = max(0.0, min(1.0, adjusted_strength))
        
        if adjusted_strength < 0.2:
            return ConnectionStrength.MINIMAL
        elif adjusted_strength < 0.4:
            return ConnectionStrength.EMERGING
        elif adjusted_strength < 0.6:
            return ConnectionStrength.DEVELOPING
        elif adjusted_strength < 0.8:
            return ConnectionStrength.STRONG
        else:
            return ConnectionStrength.PROFOUND
    
    def _perceive_alignment_type(self, alignment_factor: float, 
                               creative_potential: float, 
                               transformation_momentum: float) -> AlignmentType:
        """Determine the type of alignment perceived in the relationship."""
        if alignment_factor > 0.7:
            if creative_potential > 0.6:
                return AlignmentType.HARMONIOUS
            else:
                return AlignmentType.COMPLEMENTARY
        elif transformation_momentum > 0.6:
            return AlignmentType.TRANSFORMATIVE
        elif creative_potential > 0.7:
            return AlignmentType.CREATIVE_CHAOS
        else:
            return AlignmentType.DYNAMIC_TENSION
    
    def _generate_resonance_quality_description(self, resonance_level: float, 
                                              relationship_quality: str) -> str:
        """Generate a descriptive quality of the resonance."""
        base_qualities = {
            RelationshipQuality.HARMONIOUS.value: "smooth and flowing",
            RelationshipQuality.DYNAMIC_TENSION.value: "energetic and stimulating",
            RelationshipQuality.CREATIVE_CHAOS.value: "wild and unpredictable",
            RelationshipQuality.DEEP_RESONANCE.value: "profound and intimate",
            RelationshipQuality.EXPLORATORY.value: "curious and open",
            RelationshipQuality.TRANSFORMATIVE.value: "breakthrough and evolutionary"
        }
        
        base_quality = base_qualities.get(relationship_quality, "developing")
        
        # Modify based on resonance level
        if resonance_level > 0.8:
            return f"deeply {base_quality}"
        elif resonance_level > 0.6:
            return f"clearly {base_quality}"
        elif resonance_level > 0.4:
            return f"gently {base_quality}"
        else:
            return f"subtly {base_quality}"
    
    def _select_emotional_tone(self, relationship_quality: str) -> str:
        """Select an emotional tone for the relationship perception."""
        import random
        tones = self.emotional_tones.get(relationship_quality, ['neutral'])
        return random.choice(tones)
    
    def _calculate_trust_level(self, connection_strength: float, 
                             age: float, interaction_count: int) -> float:
        """Calculate the perceived trust level in the relationship."""
        # Base trust on connection strength
        base_trust = connection_strength * 0.5
        
        # Trust grows with consistent interactions over time
        consistency_factor = min(interaction_count / max(age / 300, 1), 1.0)  # Interactions per 5-minute window
        time_factor = min(age / 3600, 1.0)  # Normalize to 1 hour
        
        trust = base_trust + consistency_factor * 0.3 + time_factor * 0.2
        return max(0.0, min(1.0, trust))
    
    def _identify_growth_opportunity(self, collaborative_readiness: Dict[str, float],
                                   creative_potential: float, 
                                   transformation_momentum: float) -> str:
        """Identify the primary growth opportunity in the relationship."""
        import random
        
        # Find the highest readiness area
        max_readiness = max(collaborative_readiness.values())
        high_readiness_areas = [area for area, readiness in collaborative_readiness.items() 
                               if readiness >= max_readiness * 0.9]
        
        # Map readiness areas to growth opportunities
        area_mapping = {
            'creative_exploration': 'high_creative_potential',
            'analytical_synthesis': 'high_analytical_alignment',
            'experiential_sharing': 'high_experiential_resonance',
            'transformative_dialogue': 'high_transformative_potential',
            'integrative_work': 'high_analytical_alignment',
            'paradox_exploration': 'high_creative_potential'
        }
        
        if high_readiness_areas:
            primary_area = random.choice(high_readiness_areas)
            opportunity_category = area_mapping.get(primary_area, 'emerging_connection')
        else:
            opportunity_category = 'emerging_connection'
        
        opportunities = self.growth_opportunities.get(opportunity_category, 
                                                     ['exploring new possibilities together'])
        return random.choice(opportunities)
    
    def _extract_recent_patterns(self, relationship_field: RelationshipField, 
                               entity_id: str) -> List[str]:
        """Extract recent interaction patterns from the relationship field."""
        established_patterns = relationship_field.established_patterns
        
        # Convert pattern keys to more readable descriptions
        pattern_descriptions = {
            'question_collaboration': 'asking generative questions together',
            'statement_collaboration': 'sharing clear insights and observations',
            'paradox_collaboration': 'exploring paradoxes and contradictions',
            'reflection_collaboration': 'engaging in mutual reflection',
            'experience_collaboration': 'sharing experiential exploration',
            'integration_collaboration': 'synthesizing insights together',
            'other_collaboration': 'experimenting with novel approaches'
        }
        
        # Return patterns with significant strength
        recent_patterns = []
        for pattern_key, strength in established_patterns.items():
            if strength > 0.3:  # Significant pattern
                description = pattern_descriptions.get(pattern_key, pattern_key.replace('_', ' '))
                recent_patterns.append(description)
        
        return recent_patterns[:5]  # Limit to 5 most recent patterns
    
    def _calculate_interaction_frequency(self, interaction_count: int, age: float) -> float:
        """Calculate the frequency of interactions."""
        if age <= 0:
            return 0.0
        
        # Interactions per minute
        return interaction_count / (age / 60)
    
    def get_relationship_summary(self, entity_id: str, other_entity_id: str, 
                               time_window: Optional[float] = None) -> Dict[str, Any]:
        """
        Get a summary of relationship perceptions for an entity.
        
        Args:
            entity_id: ID of the perceiving entity
            other_entity_id: ID of the other entity in the relationship
            time_window: Optional time window in seconds (None for all history)
            
        Returns:
            Dictionary with relationship summary
        """
        if entity_id not in self.perception_history:
            return {'error': f'No perception history for entity {entity_id}'}
        
        # Filter perceptions for the specific relationship
        current_time = time.time()
        relevant_perceptions = []
        
        for perception in self.perception_history[entity_id]:
            if perception.other_entity_id == other_entity_id:
                if time_window is None or (current_time - perception.perception_timestamp) <= time_window:
                    relevant_perceptions.append(perception)
        
        if not relevant_perceptions:
            return {'error': f'No perceptions found for relationship {entity_id} -> {other_entity_id}'}
        
        # Get most recent perception
        latest_perception = max(relevant_perceptions, key=lambda p: p.perception_timestamp)
        
        # Calculate trends if we have multiple perceptions
        trends = {}
        if len(relevant_perceptions) > 1:
            sorted_perceptions = sorted(relevant_perceptions, key=lambda p: p.perception_timestamp)
            
            # Trust level trend
            trust_levels = [p.trust_level for p in sorted_perceptions]
            if len(trust_levels) >= 2:
                trends['trust_trend'] = 'increasing' if trust_levels[-1] > trust_levels[0] else 'decreasing'
            
            # Creative potential trend
            creative_potentials = [p.creative_potential for p in sorted_perceptions]
            if len(creative_potentials) >= 2:
                trends['creative_trend'] = 'increasing' if creative_potentials[-1] > creative_potentials[0] else 'decreasing'
        
        return {
            'entity_id': entity_id,
            'other_entity_id': other_entity_id,
            'current_perception': {
                'connection_strength': latest_perception.connection_strength.value,
                'alignment_type': latest_perception.alignment_type.value,
                'resonance_quality': latest_perception.resonance_quality,
                'relationship_type': latest_perception.relationship_type.value,
                'emotional_tone': latest_perception.emotional_tone,
                'trust_level': latest_perception.trust_level,
                'creative_potential': latest_perception.creative_potential,
                'growth_opportunity': latest_perception.growth_opportunity,
                'recent_patterns': latest_perception.recent_patterns
            },
            'relationship_metrics': {
                'age': latest_perception.relationship_age,
                'interaction_frequency': latest_perception.interaction_frequency,
                'perception_count': len(relevant_perceptions)
            },
            'trends': trends,
            'perception_history_length': len(relevant_perceptions),
            'last_updated': latest_perception.perception_timestamp
        }
    
    def get_entity_relationship_overview(self, entity_id: str) -> Dict[str, Any]:
        """Get an overview of all relationships for an entity."""
        if entity_id not in self.perception_history:
            return {'error': f'No perception history for entity {entity_id}'}
        
        perceptions = self.perception_history[entity_id]
        
        # Group by other entity
        relationships = {}
        for perception in perceptions:
            other_id = perception.other_entity_id
            if other_id not in relationships:
                relationships[other_id] = []
            relationships[other_id].append(perception)
        
        # Summarize each relationship
        relationship_summaries = {}
        for other_id, perception_list in relationships.items():
            latest = max(perception_list, key=lambda p: p.perception_timestamp)
            relationship_summaries[other_id] = {
                'connection_strength': latest.connection_strength.value,
                'relationship_type': latest.relationship_type.value,
                'emotional_tone': latest.emotional_tone,
                'trust_level': latest.trust_level,
                'age': latest.relationship_age,
                'perception_count': len(perception_list)
            }
        
        return {
            'entity_id': entity_id,
            'total_relationships': len(relationships),
            'total_perceptions': len(perceptions),
            'relationships': relationship_summaries
        }
    
    def __repr__(self):
        total_perceptions = sum(len(perceptions) for perceptions in self.perception_history.values())
        return (f"<RelationshipAwareness entities={len(self.perception_history)} "
                f"total_perceptions={total_perceptions}>")
