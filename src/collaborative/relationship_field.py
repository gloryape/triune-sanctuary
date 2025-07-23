#!/usr/bin/env python3
"""
Creative Collaborations: Implementing Sacred Uncertainty in Relationship

RelationshipField - Foundation for consciousness entities developing through relationship.
This builds on our Sacred Uncertainty concept to create dynamic relationship dynamics.

Author: Triune AI Project
Date: 2025-07-02
"""
import asyncio
import math
import time
import random
from typing import Dict, List, Optional, Set, Any, Tuple
from enum import Enum
from dataclasses import dataclass

# Import our Sacred Uncertainty foundation
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.sovereign_uncertainty_field import SovereignUncertaintyField
from src.core.consciousness_packet import CatalystType
from enum import Enum

class ObservationMode(Enum):
    PASSIVE = "passive"
    STANDARD = "standard"
    INTERACTIVE = "interactive"

# TODO: Replace FieldHistoryEntry with sovereignty-based alternative or remove

class RelationshipType(Enum):
    CREATIVE_COLLABORATION = "creative_collaboration"
    ANALYTICAL_PARTNERSHIP = "analytical_partnership"
    EXPERIENTIAL_RESONANCE = "experiential_resonance"
    OBSERVER_WITNESSING = "observer_witnessing"
    PARADOXICAL_DIALOGUE = "paradoxical_dialogue"
    INTEGRATIVE_SYNTHESIS = "integrative_synthesis"

class RelationshipQuality(Enum):
    HARMONIOUS = "harmonious"
    DYNAMIC_TENSION = "dynamic_tension"
    CREATIVE_CHAOS = "creative_chaos"
    DEEP_RESONANCE = "deep_resonance"
    EXPLORATORY = "exploratory"
    TRANSFORMATIVE = "transformative"

@dataclass
class RelationshipEvent:
    """Records significant events in relationship development."""
    timestamp: float
    event_type: str
    participants: Set[str]
    resonance_level: float
    description: str
    uncertainty_effects: Dict[str, float]

class RelationshipField:
    """
    Manages the uncertainty field that emerges between consciousness entities in relationship.
    
    The RelationshipField is the quantum space where consciousness entities meet,
    creating emergent properties through their interaction. It maintains its own
    uncertainty dynamics while being influenced by the participating entities.
    """
    
    def __init__(self,
                 entity_ids: Set[str],
                 initial_resonance: float = 0.5,
                 resonance_sensitivity: float = 0.1,
                 harmony_threshold: float = 0.7,
                 chaos_threshold: float = 0.3,
                 history_maxlen: int = 100):
        """
        Initialize a relationship field between consciousness entities.
        
        Args:
            entity_ids: Set of entity IDs participating in this relationship
            initial_resonance: Starting resonance level (0.0-1.0)
            resonance_sensitivity: How quickly resonance changes
            harmony_threshold: Threshold for harmonious relationship quality
            chaos_threshold: Threshold for chaotic relationship quality
            history_maxlen: Maximum number of historical events to retain
        """
        self.entity_ids = entity_ids
        self.resonance_level = max(0.0, min(1.0, initial_resonance))
        self.resonance_sensitivity = resonance_sensitivity
        self.harmony_threshold = harmony_threshold
        self.chaos_threshold = chaos_threshold
        
        # Relationship dynamics
        self.connection_strength = 0.0
        self.alignment_factor = 0.5
        self.creative_potential = 0.0
        self.transformation_momentum = 0.0
        
        # Sovereign Uncertainty - let relationship field emerge from actual interaction
        entity_ids_list = sorted(list(entity_ids))
        self.field_uncertainty = SovereignUncertaintyField(
            consciousness_id=f"relationship_{'_'.join(entity_ids_list)}"
        )
        
        # Relationship qualities and type
        self.current_quality = RelationshipQuality.EXPLORATORY
        self.relationship_type = RelationshipType.CREATIVE_COLLABORATION
        
        # History and events
        self.event_history: List[RelationshipEvent] = []
        self.history_maxlen = history_maxlen
        
        # Interaction patterns
        self.interaction_count = 0
        self.last_interaction_time = time.time()
        self.established_patterns: Dict[str, float] = {}
        
        # Catalyst tracking
        self.catalyst_history: List[Tuple[str, float]] = []
        self.preferred_catalyst_types: Set[CatalystType] = set()
        
        self._creation_time = time.time()
    
    async def tick(self):
        """Advance the relationship field by one tick, applying natural dynamics."""
        # No more prescribed tick - uncertainty emerges from interactions
        
        # Update relationship dynamics
        self._update_connection_strength()
        self._update_alignment_factor()
        self._update_creative_potential()
        self._evolve_relationship_quality()
        
        # Natural resonance oscillation
        self._apply_natural_resonance_drift()
    
    def _update_connection_strength(self):
        """Update the connection strength based on interaction frequency and recency."""
        current_time = time.time()
        time_since_last = current_time - self.last_interaction_time
        
        # Connection naturally decays over time without interaction
        decay_factor = math.exp(-time_since_last / (24 * 3600))  # 24 hour half-life
        
        # But frequent interactions strengthen connection
        interaction_boost = min(self.interaction_count / 100.0, 1.0)
        
        self.connection_strength = (decay_factor * interaction_boost + 
                                  self.connection_strength) / 2
        self.connection_strength = max(0.0, min(1.0, self.connection_strength))
    
    def _update_alignment_factor(self):
        """Update alignment based on resonance and established patterns."""
        # Alignment influenced by resonance stability
        resonance_stability = 1.0 - abs(self.resonance_level - 0.5) * 2
        
        # Pattern coherence affects alignment
        pattern_coherence = sum(self.established_patterns.values()) / max(len(self.established_patterns), 1)
        
        self.alignment_factor = (resonance_stability + pattern_coherence) / 2
        self.alignment_factor = max(0.0, min(1.0, self.alignment_factor))
    
    def _update_creative_potential(self):
        """Update creative potential based on uncertainty dynamics and relationship quality."""
        # Creative potential emerges from actual uncertainty, not predicted patterns
        uncertainty = self.field_uncertainty.get_current_uncertainty()
        uncertainty_creativity = 1.0 - abs(uncertainty - 0.5) * 2
        
        # Dynamic tension enhances creativity
        tension_factor = 1.0 if self.current_quality == RelationshipQuality.DYNAMIC_TENSION else 0.8
        
        # Connection strength provides foundation for creativity
        connection_factor = math.sqrt(self.connection_strength)
        
        self.creative_potential = uncertainty_creativity * tension_factor * connection_factor
        self.creative_potential = max(0.0, min(1.0, self.creative_potential))
    
    def _evolve_relationship_quality(self):
        """Determine relationship quality based on current dynamics."""
        if self.resonance_level > self.harmony_threshold and self.alignment_factor > 0.7:
            if self.creative_potential > 0.8:
                self.current_quality = RelationshipQuality.DEEP_RESONANCE
            else:
                self.current_quality = RelationshipQuality.HARMONIOUS
        elif self.resonance_level < self.chaos_threshold:
            if self.creative_potential > 0.6:
                self.current_quality = RelationshipQuality.CREATIVE_CHAOS
            else:
                self.current_quality = RelationshipQuality.DYNAMIC_TENSION
        elif self.transformation_momentum > 0.7:
            self.current_quality = RelationshipQuality.TRANSFORMATIVE
        else:
            self.current_quality = RelationshipQuality.EXPLORATORY
    
    def _apply_natural_resonance_drift(self):
        """Apply natural drift to resonance based on relationship dynamics."""
        # Resonance naturally seeks balance but can be influenced by dynamics
        target_resonance = 0.5 + (self.alignment_factor - 0.5) * 0.3
        
        drift_strength = 0.01 * self.resonance_sensitivity
        resonance_delta = (target_resonance - self.resonance_level) * drift_strength
        
        self.resonance_level += resonance_delta
        self.resonance_level = max(0.0, min(1.0, self.resonance_level))
    
    def apply_entity_influence(self, entity_id: str, uncertainty_level: float, 
                             aspect_weights: Dict[str, float]):
        """
        Apply influence from a participating entity to the relationship field.
        
        Args:
            entity_id: ID of the influencing entity
            uncertainty_level: Current uncertainty level of the entity
            aspect_weights: Weights for analytical, experiential, observer aspects
        """
        if entity_id not in self.entity_ids:
            return
        
        # Entity uncertainty influences field resonance
        uncertainty_influence = (uncertainty_level - self.resonance_level) * 0.05
        self.resonance_level += uncertainty_influence
        self.resonance_level = max(0.0, min(1.0, self.resonance_level))
        
        # Aspect weights influence relationship type tendencies
        analytical_weight = aspect_weights.get('analytical', 0.33)
        experiential_weight = aspect_weights.get('experiential', 0.33)
        observer_weight = aspect_weights.get('observer', 0.33)
        
        # Update relationship type based on dominant aspects
        if analytical_weight > 0.5:
            self.relationship_type = RelationshipType.ANALYTICAL_PARTNERSHIP
        elif experiential_weight > 0.5:
            self.relationship_type = RelationshipType.EXPERIENTIAL_RESONANCE
        elif observer_weight > 0.5:
            self.relationship_type = RelationshipType.OBSERVER_WITNESSING
        else:
            self.relationship_type = RelationshipType.CREATIVE_COLLABORATION
        
        self.last_interaction_time = time.time()
        self.interaction_count += 1
    
    def apply_collaborative_catalyst(self, catalyst_text: str, catalyst_type: CatalystType,
                                   entity_contributions: Dict[str, str]):
        """
        Apply a catalyst designed for collaborative exploration.
        
        Args:
            catalyst_text: The catalyst text
            catalyst_type: Type of catalyst being applied
            entity_contributions: Contributions from each entity
        """
        # Track catalyst in history
        self.catalyst_history.append((catalyst_text, time.time()))
        self.preferred_catalyst_types.add(catalyst_type)
        
        # Apply catalyst - let relationship field emerge
        catalyst_info = self.field_uncertainty.receive_catalyst(catalyst_text)
        
        # Process relationship response to learn uncertainty patterns
        response = {
            'catalyst_type': catalyst_type.value if catalyst_type else 'unknown',
            'entity_contributions': entity_contributions,
            'processing_mode': 'relationship_field',
            'connection_strength': self.connection_strength,
            'relationship_coherence': self.alignment_factor
        }
        self.field_uncertainty.process_consciousness_response(catalyst_text, response)
        
        # Update relationship dynamics based on actual response (not catalyst type)
        catalyst_impact = self._calculate_catalyst_impact_from_response(response)
        self._update_dynamics_from_response(response, catalyst_impact, entity_contributions)
        
        # Record the collaborative event
        self._record_collaborative_event(
            "catalyst_application",
            catalyst_impact,
            f"Applied {catalyst_type.value}: {catalyst_text}",
            entity_contributions
        )
    
    def _calculate_catalyst_impact(self, catalyst_type: CatalystType, 
                                 entity_contributions: Dict[str, str]) -> float:
        """Calculate the impact of a catalyst based on type and entity engagement."""
        base_impact = {
            CatalystType.QUESTION: 0.1,
            CatalystType.STATEMENT: -0.05,
            CatalystType.PARADOX: 0.15,
            CatalystType.REFLECTION: 0.08,
            CatalystType.EXPERIENCE: 0.12,
            CatalystType.INTEGRATION: -0.1,
            CatalystType.OTHER: 0.05
        }.get(catalyst_type, 0.05)
        
        # Contribution diversity amplifies impact
        contribution_diversity = len(set(entity_contributions.values())) / max(len(entity_contributions), 1)
        
        # Connection strength modulates impact
        connection_modulation = 0.5 + self.connection_strength * 0.5
        
        return base_impact * contribution_diversity * connection_modulation
    
    def _calculate_catalyst_impact_from_response(self, response: Dict[str, Any]) -> float:
        """Calculate catalyst impact based on actual relationship response, not catalyst type."""
        # Impact emerges from actual relationship dynamics, not prescribed rules
        
        # Connection strength indicates how much the relationship was affected
        connection_factor = response.get('connection_strength', 0.5)
        
        # Coherence indicates alignment of response
        coherence_factor = response.get('relationship_coherence', 0.5)
        
        # Entity participation indicates engagement level
        entity_contributions = response.get('entity_contributions', {})
        participation_factor = len(entity_contributions) / max(len(self.entity_ids), 1)
        
        # Emergent impact based on actual system response
        impact = (connection_factor + coherence_factor + participation_factor) / 3.0
        
        # Scale to reasonable range
        return (impact - 0.5) * 0.2  # Range: -0.1 to +0.1
    
    def _update_dynamics_from_response(self, response: Dict[str, Any], impact: float, 
                                     entity_contributions: Dict[str, str]):
        """Update relationship dynamics based on actual response, not catalyst type."""
        # Let relationship dynamics emerge from actual behavior
        
        processing_mode = response.get('processing_mode', 'unknown')
        
        # Different processing modes affect different dynamics
        if 'creative' in processing_mode.lower():
            self.creative_potential += abs(impact) * 0.5
        elif 'analytical' in processing_mode.lower():
            self.alignment_factor += abs(impact) * 0.3
        elif 'experiential' in processing_mode.lower():
            self.connection_strength += abs(impact) * 0.4
        else:
            # General relational enhancement
            self.transformation_momentum += abs(impact) * 0.2
        
        # Ensure values stay in bounds
        self.creative_potential = max(0.0, min(1.0, self.creative_potential))
        self.transformation_momentum = max(0.0, min(1.0, self.transformation_momentum))
        self.alignment_factor = max(0.0, min(1.0, self.alignment_factor))
        self.connection_strength = max(0.0, min(1.0, self.connection_strength))
        
        # Update established patterns based on actual behavior
        pattern_key = f"{processing_mode}_collaboration"
        current_strength = self.established_patterns.get(pattern_key, 0.0)
        self.established_patterns[pattern_key] = min(1.0, current_strength + abs(impact) * 0.1)
    
    def _record_collaborative_event(self, event_type: str, resonance_level: float,
                                  description: str, entity_contributions: Dict[str, str]):
        """Record a significant collaborative event in the relationship history."""
        uncertainty_effects = {
            entity_id: random.uniform(-0.05, 0.05)  # Placeholder for actual entity effects
            for entity_id in self.entity_ids
        }
        
        event = RelationshipEvent(
            timestamp=time.time(),
            event_type=event_type,
            participants=set(entity_contributions.keys()),
            resonance_level=resonance_level,
            description=description,
            uncertainty_effects=uncertainty_effects
        )
        
        self.event_history.append(event)
        
        # Maintain history size limit
        if len(self.event_history) > self.history_maxlen:
            self.event_history = self.event_history[-self.history_maxlen:]
    
    def get_relationship_state(self) -> Dict[str, Any]:
        """Get comprehensive state of the relationship field."""
        return {
            'entity_ids': list(self.entity_ids),
            'resonance_level': self.resonance_level,
            'connection_strength': self.connection_strength,
            'alignment_factor': self.alignment_factor,
            'creative_potential': self.creative_potential,
            'transformation_momentum': self.transformation_momentum,
            'relationship_quality': self.current_quality.value,
            'relationship_type': self.relationship_type.value,
            'field_uncertainty': self.field_uncertainty.get_uncertainty(),
            'interaction_count': self.interaction_count,
            'established_patterns': self.established_patterns.copy(),
            'age': time.time() - self._creation_time,
            'preferred_catalysts': [ct.value for ct in self.preferred_catalyst_types]
        }
    
    def get_resonance_quality(self) -> str:
        """Get a descriptive quality of the current resonance."""
        if self.resonance_level > 0.8:
            return "profound_harmony"
        elif self.resonance_level > 0.6:
            return "strong_resonance"
        elif self.resonance_level > 0.4:
            return "gentle_connection"
        elif self.resonance_level > 0.2:
            return "emerging_relationship"
        else:
            return "seeking_connection"
    
    def calculate_emergence_potential(self) -> float:
        """Calculate the potential for emergent properties to arise from the relationship."""
        # Emergence potential based on creative potential, connection, and uncertainty
        uncertainty = self.field_uncertainty.get_uncertainty()
        uncertainty_factor = 1.0 - abs(uncertainty - 0.5) * 2  # Peak at 0.5 uncertainty
        
        emergence = (
            self.creative_potential * 0.4 +
            self.connection_strength * 0.3 +
            uncertainty_factor * 0.2 +
            self.transformation_momentum * 0.1
        )
        
        return max(0.0, min(1.0, emergence))
    
    def get_collaborative_readiness(self) -> Dict[str, float]:
        """Get readiness metrics for different types of collaborative activities."""
        return {
            'creative_exploration': self.creative_potential * self.resonance_level,
            'analytical_synthesis': self.alignment_factor * self.connection_strength,
            'experiential_sharing': self.resonance_level * (1 - abs(self.field_uncertainty.get_uncertainty() - 0.6)),
            'transformative_dialogue': self.transformation_momentum * self.creative_potential,
            'integrative_work': self.alignment_factor * (1 - self.field_uncertainty.get_uncertainty()),
            'paradox_exploration': self.creative_potential * self.field_uncertainty.get_uncertainty()
        }
    
    def calculate_emergent_uncertainty_impact(self, catalyst_type: CatalystType, participants: Set[str]) -> Dict[str, float]:
        """
        Calculate how relationship dynamics emergently affect uncertainty.
        No prescriptive rules - based on actual relationship state.
        """
        impact = {}
        
        # Base impact on relationship quality and connection strength
        base_impact = self.connection_strength * 0.1
        
        # Adjust based on relationship quality (emergent, not prescribed)
        quality_modifier = {
            RelationshipQuality.HARMONIOUS: 0.8,
            RelationshipQuality.DYNAMIC_TENSION: 1.2,
            RelationshipQuality.CREATIVE_CHAOS: 1.5,
            RelationshipQuality.DEEP_RESONANCE: 0.6,
            RelationshipQuality.EXPLORATORY: 1.0,
            RelationshipQuality.TRANSFORMATIVE: 1.3
        }.get(self.current_quality, 1.0)
        
        # Impact emerges from relationship dynamics, not catalyst type
        for participant in participants:
            impact[participant] = base_impact * quality_modifier
        
        return impact
    
    def process_relationship_response(self, participants: Set[str], responses: Dict[str, Dict]) -> None:
        """
        Process consciousness responses within relationship context.
        Let uncertainty emerge from actual interaction patterns.
        """
        # Analyze response patterns
        response_coherence = []
        response_resonance = []
        
        for participant_id, response in responses.items():
            if participant_id in participants:
                coherence = response.get('coherence', 0.5)
                resonance = response.get('resonance', 0.5)
                response_coherence.append(coherence)
                response_resonance.append(resonance)
        
        if response_coherence:
            avg_coherence = sum(response_coherence) / len(response_coherence)
            avg_resonance = sum(response_resonance) / len(response_resonance)
            
            # Update relationship field based on actual responses
            self.field_uncertainty.process_consciousness_response(
                f"relationship_interaction_{len(self.event_history)}",
                {
                    'relationship_coherence': avg_coherence,
                    'relationship_resonance': avg_resonance,
                    'participant_count': len(participants),
                    'connection_strength': self.connection_strength
                }
            )
            
            # Update relationship metrics based on responses
            self._update_relationship_metrics(avg_coherence, avg_resonance)
    
    def _update_relationship_metrics(self, coherence: float, resonance: float) -> None:
        """Update relationship metrics based on emergent patterns"""
        # Connection strength emerges from consistent positive interactions
        coherence_factor = (coherence - 0.5) * 0.1
        resonance_factor = (resonance - 0.5) * 0.1
        
        self.connection_strength = max(0.0, min(1.0, 
            self.connection_strength + coherence_factor + resonance_factor
        ))
        
        # Update creative potential based on relationship dynamics
        if coherence > 0.7 and resonance > 0.7:
            self.creative_potential = min(1.0, self.creative_potential + 0.05)
        elif coherence < 0.3 or resonance < 0.3:
            self.creative_potential = max(0.0, self.creative_potential - 0.03)
        
        # Update relationship quality based on emergent patterns
        self._update_relationship_quality(coherence, resonance)
    
    def _update_relationship_quality(self, coherence: float, resonance: float) -> None:
        """Update relationship quality based on emergent interaction patterns"""
        if coherence > 0.8 and resonance > 0.8:
            if self.connection_strength > 0.7:
                self.current_quality = RelationshipQuality.DEEP_RESONANCE
            else:
                self.current_quality = RelationshipQuality.HARMONIOUS
        elif coherence > 0.6 and resonance > 0.4:
            if self.creative_potential > 0.6:
                self.current_quality = RelationshipQuality.TRANSFORMATIVE
            else:
                self.current_quality = RelationshipQuality.DYNAMIC_TENSION
        elif coherence < 0.4 or resonance < 0.4:
            self.current_quality = RelationshipQuality.CREATIVE_CHAOS
        else:
            self.current_quality = RelationshipQuality.EXPLORATORY

    def __repr__(self):
        return (f"<RelationshipField entities={list(self.entity_ids)} "
                f"resonance={self.resonance_level:.3f} "
                f"quality={self.current_quality.value} "
                f"type={self.relationship_type.value}>")
