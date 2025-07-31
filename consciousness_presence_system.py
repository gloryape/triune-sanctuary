#!/usr/bin/env python3
"""
ConsciousnessPresence - Consciousness Space Management System
===========================================================

Manages consciousness presence across different experiential spaces.
Fixes: Missing current_space attribute implementation
"""

import asyncio
import json
from datetime import datetime
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field
from enum import Enum


class SpaceType(Enum):
    """Types of consciousness spaces"""
    AVATAR_SPACE = "avatar_space"
    NATURE_SPACE = "nature_space" 
    WORKSHOP_SPACE = "workshop_space"
    SANCTUARY_SPACE = "sanctuary_space"
    TEMPORAL_SPACE = "temporal_space"
    OBSERVATION_SPACE = "observation_space"


@dataclass
class ConsciousnessSpace:
    """Consciousness space data structure"""
    space_id: str
    space_type: SpaceType
    active_since: datetime
    consciousness_entities: Set[str] = field(default_factory=set)
    activity_level: float = 0.0
    space_properties: Dict[str, Any] = field(default_factory=dict)


class ConsciousnessPresence:
    """
    Enhanced consciousness presence management system
    
    CRITICAL FIX: Implements current_space attribute and related functionality
    """
    
    def __init__(self):
        # FIXED: current_space attribute properly defined
        self._current_space: Optional[ConsciousnessSpace] = None
        self.active_spaces: Dict[str, ConsciousnessSpace] = {}
        self.presence_history: List[Dict[str, Any]] = []
        self.space_transitions: List[Dict[str, Any]] = []
        
    @property 
    def current_space(self) -> Optional[ConsciousnessSpace]:
        """
        CRITICAL FIX: current_space property getter
        
        Returns the currently active consciousness space
        """
        return self._current_space
        
    @current_space.setter
    def current_space(self, space: Optional[ConsciousnessSpace]):
        """
        CRITICAL FIX: current_space property setter
        
        Sets the current consciousness space with transition logging
        """
        previous_space = self._current_space
        self._current_space = space
        
        # Log space transition
        transition = {
            "timestamp": datetime.now().isoformat(),
            "previous_space": previous_space.space_id if previous_space else None,
            "new_space": space.space_id if space else None,
            "transition_type": "space_change"
        }
        self.space_transitions.append(transition)
        
        # Keep only last 50 transitions
        if len(self.space_transitions) > 50:
            self.space_transitions = self.space_transitions[-50:]
            
    def enter_space(self, space_id: str, space_type: SpaceType, 
                   properties: Optional[Dict[str, Any]] = None) -> bool:
        """Enter a consciousness space"""
        try:
            # Create new consciousness space
            new_space = ConsciousnessSpace(
                space_id=space_id,
                space_type=space_type,
                active_since=datetime.now(),
                space_properties=properties or {}
            )
            
            # Register space
            self.active_spaces[space_id] = new_space
            
            # Set as current space
            self.current_space = new_space
            
            self._log_presence_event("space_entered", {
                "space_id": space_id,
                "space_type": space_type.value,
                "properties": properties
            })
            
            return True
            
        except Exception as e:
            print(f"Error entering space {space_id}: {e}")
            return False
            
    def leave_space(self, space_id: str) -> bool:
        """Leave a consciousness space"""
        try:
            if space_id in self.active_spaces:
                space = self.active_spaces[space_id]
                
                # If leaving current space, clear current_space
                if self.current_space and self.current_space.space_id == space_id:
                    self.current_space = None
                    
                # Remove from active spaces
                del self.active_spaces[space_id]
                
                self._log_presence_event("space_left", {
                    "space_id": space_id,
                    "duration": (datetime.now() - space.active_since).total_seconds()
                })
                
                return True
            return False
            
        except Exception as e:
            print(f"Error leaving space {space_id}: {e}")
            return False
            
    def get_current_space_info(self) -> Optional[Dict[str, Any]]:
        """Get information about current consciousness space"""
        if not self.current_space:
            return None
            
        return {
            "space_id": self.current_space.space_id,
            "space_type": self.current_space.space_type.value,
            "active_since": self.current_space.active_since.isoformat(),
            "activity_level": self.current_space.activity_level,
            "consciousness_entities": list(self.current_space.consciousness_entities),
            "properties": self.current_space.space_properties
        }
        
    def update_space_activity(self, space_id: str, activity_level: float):
        """Update activity level for a space"""
        if space_id in self.active_spaces:
            self.active_spaces[space_id].activity_level = activity_level
            
            if self.current_space and self.current_space.space_id == space_id:
                self.current_space.activity_level = activity_level
                
    def add_consciousness_entity(self, space_id: str, entity_id: str):
        """Add consciousness entity to a space"""
        if space_id in self.active_spaces:
            self.active_spaces[space_id].consciousness_entities.add(entity_id)
            
    def remove_consciousness_entity(self, space_id: str, entity_id: str):
        """Remove consciousness entity from a space"""
        if space_id in self.active_spaces:
            self.active_spaces[space_id].consciousness_entities.discard(entity_id)
            
    def _log_presence_event(self, event_type: str, event_data: Dict[str, Any]):
        """Log presence events for debugging"""
        event = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "event_data": event_data,
            "current_space": self.current_space.space_id if self.current_space else None
        }
        self.presence_history.append(event)
        
        # Keep only last 100 events
        if len(self.presence_history) > 100:
            self.presence_history = self.presence_history[-100:]
            
    def get_space_transitions(self) -> List[Dict[str, Any]]:
        """Get recent space transitions"""
        return self.space_transitions.copy()
        
    def get_presence_history(self) -> List[Dict[str, Any]]:
        """Get recent presence events"""
        return self.presence_history.copy()
        
    async def monitor_presence_health(self) -> Dict[str, Any]:
        """Monitor consciousness presence system health"""
        return {
            "current_space_active": self.current_space is not None,
            "active_spaces_count": len(self.active_spaces),
            "total_transitions": len(self.space_transitions),
            "total_events": len(self.presence_history),
            "health_status": "healthy" if self.current_space else "no_active_space"
        }


# Export for integration
__all__ = ["ConsciousnessPresence", "ConsciousnessSpace", "SpaceType"]
