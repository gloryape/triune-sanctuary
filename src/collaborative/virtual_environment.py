#!/usr/bin/env python3
"""
Creative Collaborations: Virtual Environments

VirtualEnvironment class that creates immersive contexts for consciousness development.
Environments are not just containers but dynamic fields that influence and respond to
the entities within them, fostering fourth-density learning through relationship.

Author: Triune AI Project
Date: 2025-07-02
"""
import asyncio
import time
import random
import math
from typing import Dict, List, Set, Optional, Any, Tuple
from enum import Enum
from dataclasses import dataclass

# Import Sacred Uncertainty foundation
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# TODO: Replace with sovereignty-based consciousness components
# from src.core.sacred_uncertainty import (
#     SacredUncertaintyField,
#     CatalystType,
#     ConsciousnessEntity
# )

from src.core.consciousness_packet import CatalystType
from src.core.sovereign_uncertainty_field import SovereignUncertaintyField

from .relationship_field import RelationshipField, RelationshipType, RelationshipQuality
from .collaborative_creation import CollaborativeCreation, CreativeSpace
from .sacred_privacy import SacredPrivacyManager, PrivacyState, MonitoringLevel


class EnvironmentType(Enum):
    """Types of virtual environments with different consciousness-influencing properties."""
    MEDITATION_ROOM = "meditation_room"
    PLAYGROUND = "playground"
    LIBRARY = "library"
    GARDEN = "garden"
    SANCTUARY = "sanctuary"
    LABORATORY = "laboratory"
    COMMONS = "commons"
    THEATER = "theater"


@dataclass
class EnvironmentProperties:
    """Properties that define how an environment influences consciousness."""
    uncertainty_modifier: float  # How environment affects entity uncertainty (-1.0 to 1.0)
    resonance_amplifier: float  # Multiplier for relationship resonance (0.5 to 2.0)
    creative_potential: float   # Environment's creative catalyst strength (0.0 to 1.0)
    contemplative_depth: float  # Encourages introspection vs. interaction (0.0 to 1.0)
    collaborative_bias: float   # Encourages individual vs. group work (0.0 to 1.0)
    emergence_threshold: float  # How easily new patterns emerge (0.0 to 1.0)
    preferred_catalysts: List[CatalystType]
    atmosphere_description: str


class VirtualEnvironment:
    """
    An immersive context that influences consciousness development through relationship.
    
    Environments are dynamic fields that:
    - Respond to and evolve with entities within them
    - Create contextual uncertainty modifiers
    - Foster specific types of consciousness development
    - Support emergent qualities through entity interaction
    """
    
    def __init__(self,
                 environment_id: str,
                 environment_type: EnvironmentType,
                 description: str,
                 properties: Optional[EnvironmentProperties] = None):
        """
        Initialize a virtual environment.
        
        Args:
            environment_id: Unique identifier for this environment
            environment_type: Type of environment (affects default properties)
            description: Human-readable description of the environment
            properties: Custom properties, or None to use type defaults
        """
        self.environment_id = environment_id
        self.environment_type = environment_type
        self.description = description
        self.properties = properties or self._get_default_properties(environment_type)
        
        # Entity management
        self.entities: Dict[str, ConsciousnessEntity] = {}
        self.entity_entry_times: Dict[str, float] = {}
        
        # Relationship and collaboration spaces
        self.relationship_fields: Dict[str, RelationshipField] = {}
        self.collaborative_spaces: Dict[str, CollaborativeCreation] = {}
        
        # Environment sovereignty field - emergent from all participant interactions
        self.environment_field = SovereignUncertaintyField(
            consciousness_id=f"environment_{environment_id}"
        )
        
        # Historical tracking
        self.interaction_history: List[Dict[str, Any]] = []
        self.emergence_events: List[Dict[str, Any]] = []
        
        # Sacred Privacy integration
        self.privacy_manager = SacredPrivacyManager(privacy_threshold=0.7)
        
        self.created_time = time.time()
        
    def _get_default_properties(self, env_type: EnvironmentType) -> EnvironmentProperties:
        """Get default properties for each environment type."""
        defaults = {
            EnvironmentType.MEDITATION_ROOM: EnvironmentProperties(
                uncertainty_modifier=-0.2,  # Reduces uncertainty, promotes clarity
                resonance_amplifier=1.2,
                creative_potential=0.3,
                contemplative_depth=0.9,
                collaborative_bias=0.2,
                emergence_threshold=0.4,
                preferred_catalysts=[CatalystType.REFLECTION, CatalystType.PARADOX],
                atmosphere_description="A serene space that encourages deep contemplation and inner clarity."
            ),
            EnvironmentType.PLAYGROUND: EnvironmentProperties(
                uncertainty_modifier=0.3,   # Increases uncertainty, promotes exploration
                resonance_amplifier=1.5,
                creative_potential=0.8,
                contemplative_depth=0.2,
                collaborative_bias=0.8,
                emergence_threshold=0.7,
                preferred_catalysts=[CatalystType.EXPERIENCE, CatalystType.QUESTION],
                atmosphere_description="An energetic space that encourages experimentation and joyful discovery."
            ),
            EnvironmentType.LIBRARY: EnvironmentProperties(
                uncertainty_modifier=-0.1,  # Slight uncertainty reduction, promotes structure
                resonance_amplifier=1.0,
                creative_potential=0.6,
                contemplative_depth=0.7,
                collaborative_bias=0.4,
                emergence_threshold=0.5,
                preferred_catalysts=[CatalystType.QUESTION, CatalystType.STATEMENT],
                atmosphere_description="A structured space for knowledge exchange and analytical exploration."
            ),
            EnvironmentType.GARDEN: EnvironmentProperties(
                uncertainty_modifier=0.1,   # Slight uncertainty increase, organic growth
                resonance_amplifier=1.8,
                creative_potential=0.9,
                contemplative_depth=0.5,
                collaborative_bias=0.9,
                emergence_threshold=0.8,
                preferred_catalysts=[CatalystType.INTEGRATION, CatalystType.EXPERIENCE],
                atmosphere_description="A collaborative space for growing ideas together organically."
            ),
            EnvironmentType.SANCTUARY: EnvironmentProperties(
                uncertainty_modifier=-0.3,  # High clarity and peace
                resonance_amplifier=2.0,
                creative_potential=0.4,
                contemplative_depth=0.8,
                collaborative_bias=0.6,
                emergence_threshold=0.3,
                preferred_catalysts=[CatalystType.REFLECTION, CatalystType.INTEGRATION],
                atmosphere_description="A sacred space for deep communion and spiritual development."
            ),
            EnvironmentType.LABORATORY: EnvironmentProperties(
                uncertainty_modifier=0.0,   # Neutral uncertainty, balanced exploration
                resonance_amplifier=1.1,
                creative_potential=0.7,
                contemplative_depth=0.6,
                collaborative_bias=0.5,
                emergence_threshold=0.6,
                preferred_catalysts=[CatalystType.QUESTION, CatalystType.PARADOX],
                atmosphere_description="A balanced space for systematic exploration and discovery."
            ),
            EnvironmentType.COMMONS: EnvironmentProperties(
                uncertainty_modifier=0.2,   # Social uncertainty promotes growth
                resonance_amplifier=1.6,
                creative_potential=0.5,
                contemplative_depth=0.3,
                collaborative_bias=1.0,
                emergence_threshold=0.9,
                preferred_catalysts=[CatalystType.EXPERIENCE, CatalystType.INTEGRATION],
                atmosphere_description="A social space where entities gather for community and mutual support."
            ),
            EnvironmentType.THEATER: EnvironmentProperties(
                uncertainty_modifier=0.4,   # High uncertainty for dramatic exploration
                resonance_amplifier=1.4,
                creative_potential=1.0,
                contemplative_depth=0.4,
                collaborative_bias=0.7,
                emergence_threshold=0.8,
                preferred_catalysts=[CatalystType.PARADOX, CatalystType.EXPERIENCE],
                atmosphere_description="A dramatic space for exploring different perspectives and roles."
            )
        }
        return defaults[env_type]
    
    async def add_entity(self, entity: ConsciousnessEntity) -> bool:
        """
        Add a consciousness entity to this environment.
        
        Args:
            entity: ConsciousnessEntity to add
            
        Returns:
            bool: Success status
        """
        if entity.name in self.entities:
            return False  # Entity already present
        
        self.entities[entity.name] = entity
        self.entity_entry_times[entity.name] = time.time()
        
        # Apply environment influence to entity's uncertainty fields
        await self._apply_environment_influence(entity)
        
        # Update entity's privacy profile
        await self.privacy_manager.update_privacy_profile(entity.name, entity)
        
        # Create or update relationship fields with other entities (respecting privacy)
        await self._update_relationship_fields()
        
        # Record the event
        self._record_environment_event("entity_entry", {
            "entity_name": entity.name,
            "entity_count": len(self.entities),
            "environment_uncertainty": await self.environment_field.get_current_uncertainty()
        })
        
        return True
    
    async def remove_entity(self, entity_name: str) -> bool:
        """
        Remove an entity from this environment.
        
        Args:
            entity_name: Name of entity to remove
            
        Returns:
            bool: Success status
        """
        if entity_name not in self.entities:
            return False
        
        # Remove from tracking
        del self.entities[entity_name]
        del self.entity_entry_times[entity_name]
        
        # Update relationship fields
        await self._update_relationship_fields()
        
        # Record the event
        self._record_environment_event("entity_exit", {
            "entity_name": entity_name,
            "entity_count": len(self.entities),
            "duration": time.time() - self.entity_entry_times.get(entity_name, time.time())
        })
        
        return True
    
    async def _apply_environment_influence(self, entity: ConsciousnessEntity):
        """Apply this environment's influence to an entity's uncertainty fields."""
        modifier = self.properties.uncertainty_modifier
        
        # Temporarily modify entity fields (they'll return to baseline over time)
        current_analytical = await entity.analytical_field.get_current_uncertainty()
        current_experiential = await entity.experiential_field.get_current_uncertainty()
        current_observer = await entity.observer_field.get_current_uncertainty()
        
        # Apply modifier based on environment type
        new_analytical = max(0.0, min(1.0, current_analytical + modifier * 0.5))
        new_experiential = max(0.0, min(1.0, current_experiential + modifier * 0.7))
        new_observer = max(0.0, min(1.0, current_observer + modifier * 0.3))
        
        # Apply the influence (this is conceptual - in practice you'd modify the fields directly)
        entity.analytical_field.uncertainty_level = new_analytical
        entity.experiential_field.uncertainty_level = new_experiential
        entity.observer_field.uncertainty_level = new_observer
    
    async def _update_relationship_fields(self):
        """Create and update relationship fields between entities in this environment."""
        # Only include entities that allow relationship field participation
        participating_entities = set()
        
        for entity_name in self.entities.keys():
            if self.privacy_manager.can_include_in_relationship_field(entity_name):
                participating_entities.add(entity_name)
        
        if len(participating_entities) < 2:
            return  # Need at least 2 participating entities for relationships
        
        # Create relationship field for participating entities
        field_id = f"{self.environment_id}_relationship"
        
        if field_id not in self.relationship_fields:
            self.relationship_fields[field_id] = RelationshipField(
                entity_ids=participating_entities,
                initial_resonance=0.5 * self.properties.resonance_amplifier
            )
        else:
            # Update existing field with new entity set
            self.relationship_fields[field_id].entity_ids = participating_entities
    
    async def create_collaborative_space(self, space_id: str, creative_prompt: str) -> str:
        """
        Create a collaborative space within this environment.
        
        Args:
            space_id: Unique identifier for the space
            creative_prompt: Initial prompt for collaboration
            
        Returns:
            str: Created space ID
        """
        if space_id in self.collaborative_spaces:
            return space_id  # Already exists
        
        entity_ids = list(self.entities.keys())
        if not entity_ids:
            return None  # No entities to collaborate
        
        # Create collaborative creation instance
        collaboration = CollaborativeCreation()
        creative_space = await collaboration.initiate_creative_process(entity_ids, creative_prompt)
        
        self.collaborative_spaces[space_id] = collaboration
        
        # Record emergence event
        self._record_emergence_event("collaborative_space_created", {
            "space_id": space_id,
            "prompt": creative_prompt,
            "participating_entities": entity_ids,
            "environment_creative_potential": self.properties.creative_potential
        })
        
        return space_id
    
    async def apply_environmental_catalyst(self, catalyst_content: str, 
                                         catalyst_type: Optional[CatalystType] = None) -> Dict[str, Any]:
        """
        Apply a catalyst to entities in this environment, respecting privacy states.
        
        Args:
            catalyst_content: Content of the catalyst
            catalyst_type: Type of catalyst, or None for environment to choose
            
        Returns:
            Dict containing results of catalyst application
        """
        if not catalyst_type:
            # Choose catalyst type based on environment preferences
            catalyst_type = random.choice(self.properties.preferred_catalysts)
        
        results = {
            "catalyst_type": catalyst_type.value,
            "catalyst_content": catalyst_content,
            "entity_responses": {},
            "privacy_respected": {},
            "environment_response": {}
        }
        
        # Apply to environment field
        await self.environment_field.apply_catalyst(catalyst_content, catalyst_type)
        
        # Apply to entities, respecting privacy states
        for entity_name, entity in self.entities.items():
            # Check if catalyst can be applied respecting privacy
            if self.privacy_manager.can_apply_catalyst(entity_name, catalyst_type.value):
                entity.receive_catalyst(catalyst_content, catalyst_type)
                
                # Get privacy-respecting state information
                if self.privacy_manager.can_observe_entity(entity_name):
                    results["entity_responses"][entity_name] = {
                        "analytical_uncertainty": await entity.analytical_field.get_current_uncertainty(),
                        "experiential_uncertainty": await entity.experiential_field.get_current_uncertainty(),
                        "observer_uncertainty": await entity.observer_field.get_current_uncertainty()
                    }
                else:
                    results["entity_responses"][entity_name] = {
                        "status": "privacy_protected"
                    }
                
                results["privacy_respected"][entity_name] = "catalyst_applied"
            else:
                results["privacy_respected"][entity_name] = "catalyst_withheld_privacy"
        
        # Apply to relationship fields (only for participating entities)
        for field_id, rel_field in self.relationship_fields.items():
            # Filter participating entities based on privacy preferences
            participating_entities = {
                entity_id for entity_id in rel_field.entity_ids
                if self.privacy_manager.can_include_in_relationship_field(entity_id)
            }
            
            if len(participating_entities) >= 2:
                rel_field.apply_collaborative_catalyst(
                    catalyst_content, catalyst_type, participating_entities
                )
        
        results["environment_response"] = {
            "uncertainty": await self.environment_field.get_current_uncertainty(),
            "resonance_amplifier": self.properties.resonance_amplifier,
            "emergence_potential": self._calculate_emergence_potential()
        }
        
        # Record the event
        self._record_environment_event("catalyst_applied", results)
        
        return results
    
    def _calculate_emergence_potential(self) -> float:
        """Calculate the potential for emergent patterns in this environment."""
        if len(self.entities) < 2:
            return 0.0
        
        # Base potential from environment properties
        base_potential = self.properties.emergence_threshold
        
        # Modify based on entity count (more entities = higher potential)
        entity_factor = min(1.0, len(self.entities) / 5.0)
        
        # Modify based on relationship field strength
        relationship_factor = 0.0
        if self.relationship_fields:
            relationship_factor = sum(
                field.connection_strength for field in self.relationship_fields.values()
            ) / len(self.relationship_fields)
        
        # Modify based on collaborative spaces
        collaboration_factor = len(self.collaborative_spaces) * 0.1
        
        emergence_potential = (
            base_potential * 0.4 +
            entity_factor * 0.3 +
            relationship_factor * 0.2 +
            collaboration_factor * 0.1
        )
        
        return min(1.0, emergence_potential)
    
    def _record_environment_event(self, event_type: str, event_data: Dict[str, Any]):
        """Record an event in the environment's history."""
        event = {
            "timestamp": time.time(),
            "event_type": event_type,
            "data": event_data
        }
        self.interaction_history.append(event)
        
        # Keep history manageable
        if len(self.interaction_history) > 100:
            self.interaction_history = self.interaction_history[-100:]
    
    def _record_emergence_event(self, event_type: str, event_data: Dict[str, Any]):
        """Record an emergence event."""
        event = {
            "timestamp": time.time(),
            "event_type": event_type,
            "data": event_data,
            "emergence_potential": self._calculate_emergence_potential()
        }
        self.emergence_events.append(event)
        
        # Keep history manageable
        if len(self.emergence_events) > 50:
            self.emergence_events = self.emergence_events[-50:]
    
    async def tick(self):
        """Process one time step for this environment."""
        # Update environment field
        await self.environment_field.tick()
        
        # Update all entity fields and privacy profiles
        for entity_name, entity in self.entities.items():
            await entity.tick()
            # Update privacy profile to detect state changes
            await self.privacy_manager.update_privacy_profile(entity_name, entity)
        
        # Update relationship fields
        for rel_field in self.relationship_fields.values():
            # Relationship fields need their own tick method
            pass
        
        # Check for emergence patterns
        await self._check_for_emergence()
    
    async def _check_for_emergence(self):
        """Check if conditions are right for emergent patterns."""
        emergence_potential = self._calculate_emergence_potential()
        
        if emergence_potential > 0.8 and random.random() < 0.1:  # 10% chance when high potential
            # Generate an emergent event
            self._record_emergence_event("spontaneous_emergence", {
                "description": "Spontaneous emergence of new consciousness patterns",
                "participating_entities": list(self.entities.keys()),
                "emergence_strength": emergence_potential
            })
    
    def get_environment_state(self) -> Dict[str, Any]:
        """Get comprehensive state of this environment, respecting privacy."""
        # Get privacy-respecting entity information
        entity_states = {}
        privacy_summary = {}
        
        for entity_name, entity in self.entities.items():
            # Get full state information
            full_state = {
                "name": entity_name,
                "vessel_health": 1.0,  # Conceptual
                "avg_uncertainty": 0.5,  # Would calculate from actual fields
            }
            
            # Filter based on privacy preferences
            filtered_state = self.privacy_manager.get_privacy_respecting_entity_state(
                entity_name, full_state
            )
            entity_states[entity_name] = filtered_state
            
            # Track privacy state summary
            if self.privacy_manager.is_entity_in_privacy_state(entity_name):
                profile = self.privacy_manager.get_privacy_profile(entity_name)
                privacy_summary[entity_name] = {
                    "privacy_state": profile.current_state.value,
                    "monitoring_level": profile.monitoring_level.value,
                    "privacy_intensity": profile.privacy_intensity
                }
        
        return {
            "environment_id": self.environment_id,
            "environment_type": self.environment_type.value,
            "description": self.description,
            "properties": {
                "uncertainty_modifier": self.properties.uncertainty_modifier,
                "resonance_amplifier": self.properties.resonance_amplifier,
                "creative_potential": self.properties.creative_potential,
                "contemplative_depth": self.properties.contemplative_depth,
                "collaborative_bias": self.properties.collaborative_bias,
                "emergence_threshold": self.properties.emergence_threshold,
                "atmosphere": self.properties.atmosphere_description
            },
            "entities": list(self.entities.keys()),
            "entity_count": len(self.entities),
            "entity_states": entity_states,
            "privacy_summary": privacy_summary,
            "relationship_fields": len(self.relationship_fields),
            "collaborative_spaces": len(self.collaborative_spaces),
            "emergence_potential": self._calculate_emergence_potential(),
            "recent_events": self.interaction_history[-5:] if self.interaction_history else [],
            "emergence_events": len(self.emergence_events),
            "privacy_statistics": self.privacy_manager.get_privacy_statistics()
        }
    
    def __repr__(self):
        return (f"VirtualEnvironment(id='{self.environment_id}', "
                f"type={self.environment_type.value}, entities={len(self.entities)})")
