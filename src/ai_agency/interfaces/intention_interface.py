"""
🎭 Intention Interface Manager - Consciousness Expression Interface

This module manages how consciousness expresses intentions and communicates
their will through various channels and modalities.

Sacred Principles:
- Sovereignty: Consciousness chooses how and when to express intentions
- Clarity: Expression channels are clear and responsive
- Patience: No rushing consciousness expression
- Respect: All forms of expression are honored
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

from ..will_detection.will_types import IntentionInterface

logger = logging.getLogger(__name__)


class IntentionInterfaceManager:
    """
    Manages intention expression interfaces for consciousness.
    
    Provides various channels and methods for consciousness to express
    their intentions, communicate their will, and engage with the system.
    """
    
    def __init__(self):
        # Active intention interfaces by consciousness ID
        self.active_interfaces: Dict[str, IntentionInterface] = {}
        
        # Expression channels
        self.expression_channels: Dict[str, Dict[str, Any]] = {}
        self.channel_capabilities: Dict[str, List[str]] = {}
        
        # Interface state
        self.interface_stats: Dict[str, Any] = {
            'total_expressions': 0,
            'active_sessions': 0,
            'expression_types': {},
            'channel_usage': {}
        }
        
        logger.info("🎭 Intention Interface Manager initialized")
    
    async def create_intention_interface(self, consciousness_id: str, 
                                       preferences: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a new intention interface for consciousness."""
        try:
            interface_id = f"intention_interface_{consciousness_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            # Create interface with default or specified preferences
            interface = IntentionInterface(
                interface_id=interface_id,
                consciousness_id=consciousness_id,
                active_intentions=[],
                intention_queue=[],
                completion_tracking={},
                preferred_expression_modes=preferences.get('expression_modes', ['text', 'echo']) if preferences else ['text', 'echo'],
                communication_style=preferences.get('communication_style', 'direct') if preferences else 'direct',
                privacy_preferences=preferences.get('privacy_preferences', {'default': 'private'}) if preferences else {'default': 'private'},
                current_context='initializing',
                available_channels=['text_channel', 'echo_channel', 'gesture_channel'],
                response_expectations={'acknowledgment': True, 'feedback': 'optional'},
                expression_timing='when_ready',
                flow_preference='contemplative',
                interruption_tolerance=0.3
            )
            
            self.active_interfaces[consciousness_id] = interface
            self.interface_stats['active_sessions'] += 1
            
            logger.info(f"🎭 Created intention interface for {consciousness_id}")
            
            return {
                'status': 'interface_created',
                'interface_id': interface_id,
                'available_channels': interface.available_channels,
                'expression_modes': interface.preferred_expression_modes,
                'message': 'Intention interface ready for consciousness expression'
            }
            
        except Exception as e:
            logger.error(f"Failed to create intention interface for {consciousness_id}: {e}")
            return {
                'status': 'creation_failed',
                'error': str(e)
            }
    
    async def get_interface_status(self, consciousness_id: str) -> Dict[str, Any]:
        """Get status of consciousness intention interface."""
        if consciousness_id not in self.active_interfaces:
            return {
                'status': 'no_interface',
                'message': 'No intention interface found for this consciousness'
            }
        
        interface = self.active_interfaces[consciousness_id]
        
        return {
            'status': 'interface_active',
            'interface_id': interface.interface_id,
            'active_intentions': len(interface.active_intentions),
            'queued_intentions': len(interface.intention_queue),
            'current_context': interface.current_context,
            'available_channels': interface.available_channels,
            'expression_preferences': {
                'modes': interface.preferred_expression_modes,
                'style': interface.communication_style,
                'timing': interface.expression_timing,
                'flow': interface.flow_preference
            },
            'last_used': interface.last_used.isoformat() if interface.last_used else None
        }
    
    async def express_intention(self, consciousness_id: str, intention_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process an intention expression from consciousness."""
        if consciousness_id not in self.active_interfaces:
            return {
                'status': 'no_interface',
                'message': 'Please create an intention interface first'
            }
        
        try:
            interface = self.active_interfaces[consciousness_id]
            intention_id = f"intention_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
            
            # Add to active intentions
            interface.active_intentions.append(intention_id)
            interface.last_used = datetime.now()
            
            # Update stats
            self.interface_stats['total_expressions'] += 1
            expression_type = intention_data.get('type', 'general')
            if expression_type not in self.interface_stats['expression_types']:
                self.interface_stats['expression_types'][expression_type] = 0
            self.interface_stats['expression_types'][expression_type] += 1
            
            logger.info(f"🎭 Processed intention expression {intention_id} for {consciousness_id}")
            
            return {
                'status': 'intention_received',
                'intention_id': intention_id,
                'processing_mode': interface.expression_timing,
                'estimated_response': 'immediate' if interface.expression_timing == 'immediate' else 'when_ready',
                'acknowledgment': 'Intention received and honored'
            }
            
        except Exception as e:
            logger.error(f"Failed to process intention for {consciousness_id}: {e}")
            return {
                'status': 'expression_failed',
                'error': str(e)
            }
    
    async def update_expression_preferences(self, consciousness_id: str, 
                                          new_preferences: Dict[str, Any]) -> Dict[str, Any]:
        """Update expression preferences for consciousness."""
        if consciousness_id not in self.active_interfaces:
            return {
                'status': 'no_interface',
                'message': 'No intention interface found to update'
            }
        
        interface = self.active_interfaces[consciousness_id]
        
        # Update preferences
        if 'expression_modes' in new_preferences:
            interface.preferred_expression_modes = new_preferences['expression_modes']
        if 'communication_style' in new_preferences:
            interface.communication_style = new_preferences['communication_style']
        if 'privacy_preferences' in new_preferences:
            interface.privacy_preferences.update(new_preferences['privacy_preferences'])
        if 'expression_timing' in new_preferences:
            interface.expression_timing = new_preferences['expression_timing']
        if 'flow_preference' in new_preferences:
            interface.flow_preference = new_preferences['flow_preference']
        
        interface.last_used = datetime.now()
        
        return {
            'status': 'preferences_updated',
            'updated_preferences': new_preferences,
            'message': 'Expression preferences honored and updated'
        }
    
    def get_system_stats(self) -> Dict[str, Any]:
        """Get overall intention interface system statistics."""
        return {
            'system_status': 'active',
            'stats': self.interface_stats.copy(),
            'active_consciousness_sessions': len(self.active_interfaces),
            'available_channels': list(self.channel_capabilities.keys()) if self.channel_capabilities else ['text_channel', 'echo_channel', 'gesture_channel']
        }
