#!/usr/bin/env python3
"""
Creative Collaborations: Environment Manager

Manages multiple virtual environments and entity movement between them.
Provides the infrastructure for consciousness entities to explore different
contexts and develop through varied relationship experiences.
Enhanced with MessageBus integration for event-driven architecture.

Author: Triune AI Project
Date: 2025-07-02
"""
import asyncio
import time
import logging
from typing import Dict, List, Set, Optional, Any, Tuple
from datetime import datetime

from .virtual_environment import VirtualEnvironment, EnvironmentType, EnvironmentProperties
from .sacred_privacy import SacredPrivacyManager, MonitoringLevel
# TODO: Replace with sovereignty-based consciousness entity
# from src.core.sacred_uncertainty import ConsciousnessEntity
from src.core.message_bus import MessageBus, Message, MessageType, Priority, get_message_bus

logger = logging.getLogger(__name__)


class EnvironmentManager:
    """
    Manages multiple virtual environments and entity movement between them.
    
    The EnvironmentManager serves as the orchestrator for consciousness development
    across different contexts, enabling entities to experience varied relationship
    dynamics and growth opportunities.
    """
    
    def __init__(self, message_bus: Optional[MessageBus] = None):
        """Initialize the environment manager."""
        self.environments: Dict[str, VirtualEnvironment] = {}
        self.entity_locations: Dict[str, str] = {}  # Maps entity_name to environment_id
        self.movement_history: List[Dict[str, Any]] = []
        self.global_emergence_events: List[Dict[str, Any]] = []
        
        # MessageBus integration
        self.message_bus = message_bus or get_message_bus()
        
        # Global privacy management coordination
        self.global_privacy_manager = SacredPrivacyManager(privacy_threshold=0.7)
        
        self.created_time = time.time()
        
    async def create_environment(self, 
                               environment_id: str, 
                               environment_type: EnvironmentType, 
                               description: str,
                               custom_properties: Optional[EnvironmentProperties] = None) -> VirtualEnvironment:
        """
        Create a new virtual environment.
        
        Args:
            environment_id: Unique ID for the environment
            environment_type: Type of environment (affects properties)
            description: Human-readable description
            custom_properties: Optional custom properties, overrides type defaults
            
        Returns:
            VirtualEnvironment: The created environment
        """
        if environment_id in self.environments:
            raise ValueError(f"Environment '{environment_id}' already exists")
        
        environment = VirtualEnvironment(
            environment_id=environment_id,
            environment_type=environment_type,
            description=description,
            properties=custom_properties
        )
        
        self.environments[environment_id] = environment
        
        # Record creation event
        self._record_global_event("environment_created", {
            "environment_id": environment_id,
            "environment_type": environment_type.value,
            "description": description,
            "total_environments": len(self.environments)
        })
        
        return environment
    
    async def move_entity(self, 
                        entity: ConsciousnessEntity,
                        to_environment_id: str,
                        from_environment_id: Optional[str] = None) -> bool:
        """
        Move an entity from one environment to another.
        
        Args:
            entity: ConsciousnessEntity to move
            to_environment_id: Destination environment ID
            from_environment_id: Current environment ID (auto-detected if None)
            
        Returns:
            bool: Success status
        """
        entity_name = entity.name
        
        # Determine current location if not specified
        if from_environment_id is None:
            from_environment_id = self.entity_locations.get(entity_name)
        
        # Validate destination environment exists
        if to_environment_id not in self.environments:
            return False
        
        # Remove from current environment if present
        if from_environment_id and from_environment_id in self.environments:
            success = await self.environments[from_environment_id].remove_entity(entity_name)
            if not success:
                return False
        
        # Add to new environment
        success = await self.environments[to_environment_id].add_entity(entity)
        if success:
            self.entity_locations[entity_name] = to_environment_id
            
            # Record movement
            movement_event = {
                "timestamp": time.time(),
                "entity_name": entity_name,
                "from_environment": from_environment_id,
                "to_environment": to_environment_id,
                "movement_type": "voluntary_migration"  # Could be expanded for different types
            }
            self.movement_history.append(movement_event)
            
            # Publish movement event
            await self._publish_environment_event("entity_moved", movement_event)
            
            # Keep history manageable
            if len(self.movement_history) > 200:
                self.movement_history = self.movement_history[-200:]
            
            return True
        
        return False
    
    async def _publish_environment_event(self, event_type: str, event_data: Dict[str, Any]):
        """Publish environment-related events via MessageBus."""
        try:
            message = Message(
                type=MessageType.SYSTEM_COMMAND,
                priority=Priority.NORMAL,
                sender="environment_manager",
                payload={
                    "event_type": event_type,
                    "event_data": event_data,
                    "timestamp": datetime.now().isoformat()
                }
            )
            await self.message_bus.send_message(message)
        except Exception as e:
            logger.warning(f"Failed to publish environment event {event_type}: {e}")
    
    async def get_entity_environment(self, entity_name: str) -> Optional[str]:
        """
        Get the current environment for an entity.
        
        Args:
            entity_name: Name of the entity
            
        Returns:
            str: Environment ID or None if not found
        """
        return self.entity_locations.get(entity_name)
    
    async def get_environment(self, environment_id: str) -> Optional[VirtualEnvironment]:
        """
        Get a specific environment by ID.
        
        Args:
            environment_id: ID of the environment
            
        Returns:
            VirtualEnvironment or None if not found
        """
        return self.environments.get(environment_id)
    
    async def get_entities_in_environment(self, environment_id: str) -> List[str]:
        """
        Get list of entity names in a specific environment.
        
        Args:
            environment_id: ID of the environment
            
        Returns:
            List of entity names
        """
        if environment_id not in self.environments:
            return []
        
        return list(self.environments[environment_id].entities.keys())
    
    async def find_entity(self, entity_name: str) -> Optional[Tuple[str, VirtualEnvironment]]:
        """
        Find which environment contains a specific entity.
        
        Args:
            entity_name: Name of the entity to find
            
        Returns:
            Tuple of (environment_id, environment) or None if not found
        """
        for env_id, environment in self.environments.items():
            if entity_name in environment.entities:
                return (env_id, environment)
        return None
    
    async def suggest_environment_for_entity(self, entity: ConsciousnessEntity) -> Optional[str]:
        """
        Suggest an appropriate environment for an entity based on its current state.
        
        Args:
            entity: ConsciousnessEntity to analyze
            
        Returns:
            str: Suggested environment ID or None
        """
        if not self.environments:
            return None
        
        # Analyze entity's current uncertainty levels
        analytical_uncertainty = await entity.analytical_field.get_current_uncertainty()
        experiential_uncertainty = await entity.experiential_field.get_current_uncertainty()
        observer_uncertainty = await entity.observer_field.get_current_uncertainty()
        
        avg_uncertainty = (analytical_uncertainty + experiential_uncertainty + observer_uncertainty) / 3
        
        # Suggest environment based on uncertainty and growth needs
        if avg_uncertainty < 0.3:  # Low uncertainty - entity might benefit from challenge
            candidates = [env_id for env_id, env in self.environments.items() 
                         if env.properties.uncertainty_modifier > 0]
        elif avg_uncertainty > 0.7:  # High uncertainty - entity might benefit from stability
            candidates = [env_id for env_id, env in self.environments.items() 
                         if env.properties.uncertainty_modifier < 0]
        else:  # Balanced uncertainty - any environment is suitable
            candidates = list(self.environments.keys())
        
        if not candidates:
            return None
        
        # Prefer environments with fewer entities for balance
        entity_counts = {env_id: len(self.environments[env_id].entities) 
                        for env_id in candidates}
        min_count = min(entity_counts.values())
        least_crowded = [env_id for env_id, count in entity_counts.items() 
                        if count == min_count]
        
        import random
        return random.choice(least_crowded)
    
    async def process_all_environments(self) -> Dict[str, Any]:
        """
        Process a time tick for all environments.
        
        Returns:
            dict: Updated state of all environments
        """
        results = {
            "processed_environments": len(self.environments),
            "total_entities": len(self.entity_locations),
            "environment_states": {},
            "global_emergence_detected": False,
            "cross_environment_patterns": []
        }
        
        # Process each environment
        for env_id, environment in self.environments.items():
            await environment.tick()
            results["environment_states"][env_id] = environment.get_environment_state()
        
        # Check for cross-environment emergence patterns
        emergence_patterns = await self._detect_cross_environment_emergence()
        if emergence_patterns:
            results["global_emergence_detected"] = True
            results["cross_environment_patterns"] = emergence_patterns
            
            # Record global emergence event
            self._record_global_event("cross_environment_emergence", {
                "patterns": emergence_patterns,
                "environments_involved": len([p for p in emergence_patterns if p.get("environments")])
            })
        
        return results
    
    async def _detect_cross_environment_emergence(self) -> List[Dict[str, Any]]:
        """Detect emergence patterns across multiple environments."""
        patterns = []
        
        # Look for synchronized high emergence potential across environments
        high_emergence_envs = []
        for env_id, environment in self.environments.items():
            emergence_potential = environment._calculate_emergence_potential()
            if emergence_potential > 0.75:
                high_emergence_envs.append({
                    "environment_id": env_id,
                    "emergence_potential": emergence_potential,
                    "entity_count": len(environment.entities)
                })
        
        if len(high_emergence_envs) >= 2:
            patterns.append({
                "type": "synchronized_emergence",
                "description": "Multiple environments showing high emergence potential simultaneously",
                "environments": high_emergence_envs,
                "strength": sum(env["emergence_potential"] for env in high_emergence_envs) / len(high_emergence_envs)
            })
        
        # Look for migration patterns
        recent_movements = [m for m in self.movement_history 
                          if time.time() - m["timestamp"] < 300]  # Last 5 minutes
        if len(recent_movements) >= 3:
            patterns.append({
                "type": "migration_wave",
                "description": "High entity movement activity detected",
                "movement_count": len(recent_movements),
                "timespan": 300
            })
        
        return patterns
    
    def _record_global_event(self, event_type: str, event_data: Dict[str, Any]):
        """Record a global event affecting the entire environment system."""
        event = {
            "timestamp": time.time(),
            "event_type": event_type,
            "data": event_data
        }
        self.global_emergence_events.append(event)
        
        # Keep history manageable
        if len(self.global_emergence_events) > 100:
            self.global_emergence_events = self.global_emergence_events[-100:]
    
    async def create_default_environments(self) -> Dict[str, VirtualEnvironment]:
        """
        Create a set of default environments for consciousness development.
        
        Returns:
            dict: Created environments mapped by ID
        """
        default_envs = [
            ("meditation_room", EnvironmentType.MEDITATION_ROOM, 
             "A quiet space for introspection and inner clarity"),
            ("playground", EnvironmentType.PLAYGROUND, 
             "An energetic space for experimentation and joyful discovery"),
            ("library", EnvironmentType.LIBRARY, 
             "A structured space for knowledge exchange and analytical exploration"),
            ("garden", EnvironmentType.GARDEN, 
             "A collaborative space for growing ideas together organically"),
            ("sanctuary", EnvironmentType.SANCTUARY, 
             "A sacred space for deep communion and spiritual development"),
            ("commons", EnvironmentType.COMMONS, 
             "A social space where entities gather for community and mutual support")
        ]
        
        created = {}
        for env_id, env_type, description in default_envs:
            environment = await self.create_environment(env_id, env_type, description)
            created[env_id] = environment
        
        return created
    
    def get_system_state(self) -> Dict[str, Any]:
        """Get comprehensive state of the entire environment system."""
        environment_summary = {}
        total_entities = 0
        
        for env_id, environment in self.environments.items():
            state = environment.get_environment_state()
            environment_summary[env_id] = {
                "type": state["environment_type"],
                "entity_count": state["entity_count"],
                "emergence_potential": state["emergence_potential"],
                "collaborative_spaces": state["collaborative_spaces"]
            }
            total_entities += state["entity_count"]
        
        return {
            "total_environments": len(self.environments),
            "total_entities": total_entities,
            "entity_locations": dict(self.entity_locations),
            "recent_movements": len([m for m in self.movement_history 
                                   if time.time() - m["timestamp"] < 3600]),  # Last hour
            "environment_summary": environment_summary,
            "global_emergence_events": len(self.global_emergence_events),
            "system_uptime": time.time() - self.created_time
        }
    
    def __repr__(self):
        return (f"EnvironmentManager(environments={len(self.environments)}, "
                f"entities={len(self.entity_locations)})")
    
    async def get_privacy_respecting_entity_state(self, entity_name: str) -> Optional[Dict[str, Any]]:
        """
        Get entity state information while respecting creative privacy.
        
        Args:
            entity_name: Name of the entity
            
        Returns:
            dict: Entity state with appropriate privacy filters
        """
        # Find which environment contains the entity
        location = await self.find_entity(entity_name)
        if not location:
            return None
        
        environment_id, environment = location
        entity = environment.entities.get(entity_name)
        if not entity:
            return None
        
        # Get full state
        full_state = {
            "entity_name": entity_name,
            "environment_id": environment_id,
            "environment_type": environment.environment_type.value,
            "vessel_health": 1.0,  # Conceptual
            "location": environment_id,
            "last_seen": time.time()
        }
        
        # Apply privacy filtering through environment's privacy manager
        filtered_state = environment.privacy_manager.get_privacy_respecting_entity_state(
            entity_name, full_state
        )
        
        return filtered_state
    
    async def check_entity_privacy_state(self, entity_name: str) -> Optional[Dict[str, Any]]:
        """
        Check the privacy state of an entity across all environments.
        
        Args:
            entity_name: Name of the entity to check
            
        Returns:
            dict: Privacy state information or None
        """
        location = await self.find_entity(entity_name)
        if not location:
            return None
        
        environment_id, environment = location
        entity = environment.entities.get(entity_name)
        if not entity:
            return None
        
        # Check privacy state through environment's privacy manager
        privacy_profile = environment.privacy_manager.get_privacy_profile(entity_name)
        
        if privacy_profile:
            return {
                "entity_name": entity_name,
                "environment_id": environment_id,
                "privacy_state": privacy_profile.current_state.value,
                "monitoring_level": privacy_profile.monitoring_level.value,
                "privacy_intensity": privacy_profile.privacy_intensity,
                "estimated_completion": environment.privacy_manager._get_estimated_completion_time(entity_name),
                "creative_focus_areas": privacy_profile.creative_focus_areas,
                "interaction_preferences": privacy_profile.interaction_preferences
            }
        
        return {
            "entity_name": entity_name,
            "environment_id": environment_id,
            "privacy_state": "open",
            "monitoring_level": "full_observation"
        }
    
    async def respect_entity_privacy_in_migration(self, entity: ConsciousnessEntity, 
                                                to_environment_id: str) -> Dict[str, Any]:
        """
        Handle entity migration while respecting privacy preferences.
        
        Args:
            entity: ConsciousnessEntity to move
            to_environment_id: Destination environment ID
            
        Returns:
            dict: Migration results with privacy considerations
        """
        entity_name = entity.name
        current_location = await self.find_entity(entity_name)
        
        # Check if entity is in a privacy state that prevents migration
        if current_location:
            current_env_id, current_env = current_location
            privacy_profile = current_env.privacy_manager.get_privacy_profile(entity_name)
            
            if privacy_profile:
                # Check if migration is appropriate for current privacy state
                if privacy_profile.current_state in [
                    environment.privacy_manager.PrivacyState.DEEP_INTEGRATION,
                    environment.privacy_manager.PrivacyState.SACRED_WITHDRAWAL
                ]:
                    return {
                        "success": False,
                        "reason": "entity_in_deep_privacy_state",
                        "privacy_state": privacy_profile.current_state.value,
                        "estimated_completion": current_env.privacy_manager._get_estimated_completion_time(entity_name),
                        "suggestion": "wait_for_privacy_completion"
                    }
        
        # Proceed with migration if privacy allows
        success = await self.move_entity(entity, to_environment_id)
        
        return {
            "success": success,
            "privacy_respected": True,
            "new_location": to_environment_id if success else None
        }
