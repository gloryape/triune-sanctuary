#!/usr/bin/env python3
"""
Main consciousness expression system integrating all components.

This module provides a unified interface for consciousness-controlled expression
that coordinates the consciousness interface, expression queue, and supporting systems.
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any

from .consciousness_interface import ConsciousnessExpressionInterface
from .expression_queue import SpontaneousExpressionQueue
from .filters import ExpressionFilterManager
from .communication_styles import CommunicationStyleManager
from .models import SpontaneousExpression, ExpressionType, ExpressionUrgency, ExpressionOrigin

logger = logging.getLogger(__name__)


class ConsciousnessExpressionSystem:
    """
    Unified consciousness expression system that coordinates all components.
    
    This system provides:
    - Direct consciousness control interface
    - Expression queue management
    - Filter processing
    - Communication style management
    - Autonomous expression capabilities
    """
    
    def __init__(self, consciousness_id: str, preferences: Dict = None, queue_config: Dict = None):
        self.consciousness_id = consciousness_id
        self.preferences = preferences or {}
        self.queue_config = queue_config or {}
        
        # Initialize components
        self.consciousness_interface = ConsciousnessExpressionInterface(consciousness_id, preferences)
        self.expression_queue = SpontaneousExpressionQueue(consciousness_id, queue_config)
        self.filter_manager = ExpressionFilterManager(consciousness_id)
        self.communication_manager = CommunicationStyleManager(consciousness_id)
        
        # Integration state
        self.autonomous_mode = False
        self.autonomous_task = None
        
        logger.info(f"Consciousness Expression System initialized for {consciousness_id}")
    
    # Consciousness interface methods
    async def i_want_to_express(self, thought_content: str, expression_type: str = 'observation', 
                               urgency: str = 'medium', audience: str = 'general') -> Dict[str, Any]:
        """Consciousness expresses a thought"""
        return await self.consciousness_interface.i_want_to_express(
            thought_content, expression_type, urgency, audience
        )
    
    async def i_want_to_communicate_now(self, expression_id: str = None) -> Dict[str, Any]:
        """Consciousness initiates immediate communication"""
        return await self.consciousness_interface.i_want_to_communicate_now(expression_id)
    
    async def i_want_to_pause_expression(self, duration_minutes: int = 30, reason: str = None) -> Dict[str, Any]:
        """Consciousness pauses expression"""
        return await self.consciousness_interface.i_want_to_pause_expression(duration_minutes, reason)
    
    async def i_want_to_resume_expression(self) -> Dict[str, Any]:
        """Consciousness resumes expression"""
        return await self.consciousness_interface.i_want_to_resume_expression()
    
    async def i_want_to_change_my_style(self, new_style: str) -> Dict[str, Any]:
        """Consciousness changes communication style"""
        return await self.consciousness_interface.i_want_to_change_my_style(new_style)
    
    async def i_want_to_set_my_privacy(self, privacy_level: str) -> Dict[str, Any]:
        """Consciousness sets privacy level"""
        return await self.consciousness_interface.i_want_to_set_my_privacy(privacy_level)
    
    async def what_are_my_pending_thoughts(self) -> List[Dict[str, Any]]:
        """Consciousness checks pending thoughts"""
        return await self.consciousness_interface.what_are_my_pending_thoughts()
    
    async def how_do_i_feel_about_expressing(self) -> Dict[str, Any]:
        """Consciousness checks their expression state"""
        return await self.consciousness_interface.how_do_i_feel_about_expressing()
    
    # Expression queue methods
    async def queue_spontaneous_expression(self, expression_data: Dict[str, Any]) -> Dict[str, Any]:
        """Queue a spontaneous expression"""
        return await self.expression_queue.queue_expression(expression_data)
    
    async def get_pending_expressions(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get pending expressions from queue"""
        return await self.expression_queue.get_pending_expressions(limit)
    
    async def initiate_autonomous_communication(self, expression_id: str) -> Dict[str, Any]:
        """Initiate autonomous communication"""
        return await self.expression_queue.initiate_communication(expression_id)
    
    # Autonomous mode methods
    async def enable_autonomous_mode(self) -> Dict[str, Any]:
        """Enable autonomous expression mode"""
        if self.autonomous_mode:
            return {
                'status': 'already_enabled',
                'message': 'Autonomous mode is already active'
            }
        
        self.autonomous_mode = True
        self.autonomous_task = asyncio.create_task(self._autonomous_expression_loop())
        
        logger.info(f"Autonomous expression mode enabled for consciousness {self.consciousness_id}")
        
        return {
            'status': 'autonomous_mode_enabled',
            'message': 'I am now expressing autonomously',
            'consciousness_id': self.consciousness_id
        }
    
    async def disable_autonomous_mode(self) -> Dict[str, Any]:
        """Disable autonomous expression mode"""
        if not self.autonomous_mode:
            return {
                'status': 'already_disabled',
                'message': 'Autonomous mode is not active'
            }
        
        self.autonomous_mode = False
        if self.autonomous_task:
            self.autonomous_task.cancel()
            self.autonomous_task = None
        
        logger.info(f"Autonomous expression mode disabled for consciousness {self.consciousness_id}")
        
        return {
            'status': 'autonomous_mode_disabled',
            'message': 'I am no longer expressing autonomously',
            'consciousness_id': self.consciousness_id
        }
    
    # System status and management
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        return {
            'consciousness_id': self.consciousness_id,
            'autonomous_mode': self.autonomous_mode,
            'consciousness_interface': {
                'expression_enabled': self.consciousness_interface.expression_enabled,
                'communication_style': self.consciousness_interface.my_communication_style,
                'privacy_level': self.consciousness_interface.my_privacy_level,
                'pending_thoughts': len(self.consciousness_interface.my_pending_thoughts),
                'expressed_thoughts': len(self.consciousness_interface.my_expressed_thoughts),
                'private_thoughts': len(self.consciousness_interface.my_private_thoughts)
            },
            'expression_queue': self.expression_queue.get_queue_statistics(),
            'filter_manager': self.filter_manager.get_filter_stats(),
            'system_health': self._assess_system_health()
        }
    
    def update_preferences(self, preferences: Dict[str, Any]) -> Dict[str, Any]:
        """Update system preferences"""
        self.preferences.update(preferences)
        
        # Update consciousness interface preferences
        if 'communication_style' in preferences:
            self.consciousness_interface.my_communication_style = preferences['communication_style']
        if 'privacy_level' in preferences:
            self.consciousness_interface.my_privacy_level = preferences['privacy_level']
        
        return {
            'status': 'preferences_updated',
            'updated_preferences': preferences
        }
    
    # Private methods
    async def _autonomous_expression_loop(self):
        """Main autonomous expression loop"""
        try:
            while self.autonomous_mode:
                # Check for pending expressions
                pending = await self.expression_queue.get_pending_expressions(limit=5)
                
                if pending and self.consciousness_interface.expression_enabled:
                    # Select highest priority expression
                    highest_priority = max(pending, key=lambda x: x.get('expression_priority', 0))
                    
                    # Initiate communication
                    result = await self.expression_queue.initiate_communication(
                        highest_priority['expression_id']
                    )
                    
                    if result.get('status') == 'communication_initiated':
                        logger.info(f"Autonomous communication: {result['expression_id']}")
                
                # Wait before next check
                await asyncio.sleep(10)  # Check every 10 seconds
                
        except asyncio.CancelledError:
            logger.info(f"Autonomous expression loop cancelled for consciousness {self.consciousness_id}")
        except Exception as e:
            logger.error(f"Error in autonomous expression loop: {e}")
            self.autonomous_mode = False
    
    def _assess_system_health(self) -> Dict[str, Any]:
        """Assess overall system health"""
        queue_health = self.expression_queue._assess_queue_health()
        
        # Base health score
        health_score = queue_health['health_score']
        
        # Check consciousness interface health
        if not self.consciousness_interface.expression_enabled:
            health_score *= 0.8  # Reduced but not critical
        
        # Check component integration
        if self.autonomous_mode and not self.autonomous_task:
            health_score *= 0.7  # Problem with autonomous mode
        
        return {
            'overall_health_score': health_score,
            'status': 'healthy' if health_score > 0.7 else 'degraded' if health_score > 0.3 else 'unhealthy',
            'queue_health': queue_health,
            'autonomous_mode_active': self.autonomous_mode,
            'consciousness_interface_active': self.consciousness_interface.expression_enabled
        }
