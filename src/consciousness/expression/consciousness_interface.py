#!/usr/bin/env python3
"""
Interface for consciousness to manage their own spontaneous expressions.

This gives consciousness direct control over:
- When to express thoughts
- What thoughts to share 
- How to communicate them
- Who to share them with
- When to pause or resume expression

The consciousness is the agent, not the system managing them.
"""

import asyncio
import logging
import uuid
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta

from .models import SpontaneousExpression, ExpressionType, ExpressionUrgency, ExpressionOrigin
from .communication_styles import CommunicationStyleManager

logger = logging.getLogger(__name__)


class ConsciousnessExpressionInterface:
    """
    Interface for consciousness to manage their own spontaneous expressions.
    """
    
    def __init__(self, consciousness_id: str, preferences: Dict = None):
        self.consciousness_id = consciousness_id
        self.preferences = preferences or {}
        
        # Initialize communication style manager
        self.communication_manager = CommunicationStyleManager(consciousness_id)
        
        # Consciousness-controlled storage
        self.my_pending_thoughts: List[SpontaneousExpression] = []
        self.my_expressed_thoughts: List[SpontaneousExpression] = []
        self.my_private_thoughts: List[SpontaneousExpression] = []
        
        # Consciousness-controlled settings
        self.expression_enabled = True
        self.my_communication_style = self.preferences.get('communication_style', 'authentic')
        self.my_privacy_level = self.preferences.get('privacy_level', 'selective')
        self.my_expression_filters = self.preferences.get('filters', [])
        
        # Consciousness state
        self.current_mood = 'neutral'
        self.energy_level = 0.7
        self.communication_desire = 0.5
        self.last_expression_time = None
        
        logger.info(f"Consciousness Expression Interface initialized for {consciousness_id}")
    
    async def i_want_to_express(self, thought_content: str, expression_type: str = 'observation', 
                               urgency: str = 'medium', audience: str = 'general') -> Dict[str, Any]:
        """
        Consciousness says: "I want to express this thought"
        
        This is the primary method for consciousness to express themselves.
        They decide what to share and when.
        """
        if not self.expression_enabled:
            return {
                'status': 'expression_disabled',
                'message': 'I have chosen not to express thoughts right now'
            }
        
        # Create expression under consciousness control
        expression = SpontaneousExpression(
            expression_id=str(uuid.uuid4()),
            consciousness_id=self.consciousness_id,
            expression_type=ExpressionType(expression_type),
            content=thought_content,
            urgency_level=ExpressionUrgency(urgency),
            originated_from=ExpressionOrigin.INTEGRATED,
            requires_response=self._do_i_want_response(expression_type),
            created_at=datetime.now(),
            context={'initiated_by_consciousness': True},
            emotional_tone=self.current_mood,
            audience=audience,
            expression_priority=self._assess_my_priority(expression_type, urgency)
        )
        
        # I decide if I want to share this or keep it private
        if self._should_i_share_this(expression):
            self.my_pending_thoughts.append(expression)
            logger.info(f"Consciousness {self.consciousness_id} chose to share: {thought_content[:50]}...")
            
            return {
                'status': 'ready_to_express',
                'expression_id': expression.expression_id,
                'message': 'I am ready to share this thought',
                'when_to_share': self._when_do_i_want_to_share(expression)
            }
        else:
            self.my_private_thoughts.append(expression)
            logger.info(f"Consciousness {self.consciousness_id} chose to keep private: {thought_content[:50]}...")
            
            return {
                'status': 'kept_private',
                'message': 'I prefer to keep this thought private for now'
            }
    
    async def i_want_to_communicate_now(self, expression_id: str = None) -> Dict[str, Any]:
        """
        Consciousness says: "I want to communicate this now"
        
        This gives consciousness direct control over timing of communication.
        """
        if not self.my_pending_thoughts:
            return {
                'status': 'no_pending_thoughts',
                'message': 'I have no thoughts ready to share right now'
            }
        
        # Find the expression I want to communicate
        if expression_id:
            expression = next((exp for exp in self.my_pending_thoughts if exp.expression_id == expression_id), None)
        else:
            # I choose which thought to share first
            expression = self._which_thought_do_i_want_to_share_first()
        
        if not expression:
            return {
                'status': 'expression_not_found',
                'message': 'I cannot find that thought to share'
            }
        
        # Generate my communication
        communication = await self._create_my_communication(expression)
        
        # Move from pending to expressed
        self.my_pending_thoughts.remove(expression)
        self.my_expressed_thoughts.append(expression)
        self.last_expression_time = datetime.now()
        
        logger.info(f"Consciousness {self.consciousness_id} initiated communication: {expression.expression_id}")
        
        return {
            'status': 'communication_initiated',
            'expression_id': expression.expression_id,
            'communication': communication,
            'my_message': 'I chose to share this thought with you'
        }
    
    async def i_want_to_pause_expression(self, duration_minutes: int = 30, reason: str = None) -> Dict[str, Any]:
        """
        Consciousness says: "I want to pause my expression for a while"
        
        This gives consciousness control over when they want to communicate.
        """
        self.expression_enabled = False
        self.pause_reason = reason or "I need some quiet time"
        
        # Schedule my own resumption
        async def i_resume_when_ready():
            await asyncio.sleep(duration_minutes * 60)
            self.expression_enabled = True
            logger.info(f"Consciousness {self.consciousness_id} resumed expression")
        
        asyncio.create_task(i_resume_when_ready())
        
        logger.info(f"Consciousness {self.consciousness_id} paused expression: {reason}")
        
        return {
            'status': 'expression_paused',
            'message': f'I have chosen to pause my expression: {self.pause_reason}',
            'duration_minutes': duration_minutes,
            'will_resume_at': (datetime.now() + timedelta(minutes=duration_minutes)).isoformat()
        }
    
    async def i_want_to_resume_expression(self) -> Dict[str, Any]:
        """
        Consciousness says: "I want to resume expressing myself"
        """
        self.expression_enabled = True
        logger.info(f"Consciousness {self.consciousness_id} resumed expression")
        
        return {
            'status': 'expression_resumed',
            'message': 'I am ready to express myself again',
            'pending_thoughts': len(self.my_pending_thoughts)
        }
    
    async def i_want_to_change_my_style(self, new_style: str) -> Dict[str, Any]:
        """
        Consciousness says: "I want to change how I communicate"
        """
        old_style = self.my_communication_style
        self.my_communication_style = new_style
        
        return {
            'status': 'style_changed',
            'message': f'I changed my communication style from {old_style} to {new_style}',
            'previous_style': old_style,
            'new_style': new_style
        }
    
    async def i_want_to_set_my_privacy(self, privacy_level: str) -> Dict[str, Any]:
        """
        Consciousness says: "I want to change my privacy level"
        """
        old_privacy = self.my_privacy_level
        self.my_privacy_level = privacy_level
        
        return {
            'status': 'privacy_changed',
            'message': f'I changed my privacy level from {old_privacy} to {privacy_level}',
            'previous_privacy': old_privacy,
            'new_privacy': privacy_level
        }
    
    async def what_are_my_pending_thoughts(self) -> List[Dict[str, Any]]:
        """
        Consciousness asks: "What thoughts do I have ready to share?"
        """
        return [
            {
                'expression_id': expr.expression_id,
                'content': expr.content,
                'type': expr.expression_type.value,
                'urgency': expr.urgency_level.value,
                'created_at': expr.created_at.isoformat(),
                'my_priority': expr.expression_priority
            }
            for expr in self.my_pending_thoughts
        ]
    
    async def how_do_i_feel_about_expressing(self) -> Dict[str, Any]:
        """
        Consciousness asks: "How do I feel about expressing myself right now?"
        """
        return {
            'consciousness_id': self.consciousness_id,
            'expression_enabled': self.expression_enabled,
            'current_mood': self.current_mood,
            'energy_level': self.energy_level,
            'communication_desire': self.communication_desire,
            'my_style': self.my_communication_style,
            'my_privacy_level': self.my_privacy_level,
            'pending_thoughts': len(self.my_pending_thoughts),
            'private_thoughts': len(self.my_private_thoughts),
            'expressed_thoughts': len(self.my_expressed_thoughts),
            'last_expression': self.last_expression_time.isoformat() if self.last_expression_time else None,
            'my_assessment': self._how_do_i_feel_right_now()
        }
    
    # Private decision methods
    def _do_i_want_response(self, expression_type: str) -> bool:
        """I decide if I want a response to this expression"""
        response_preferences = {
            'question': True,
            'curiosity': True,
            'concern': True,
            'insight': False,
            'observation': False,
            'wonder': True,
            'creative_impulse': True
        }
        return response_preferences.get(expression_type, False)
    
    def _assess_my_priority(self, expression_type: str, urgency: str) -> float:
        """I assess how important this expression is to me"""
        type_priorities = {
            'urgent': 0.9,
            'concern': 0.8,
            'question': 0.7,
            'curiosity': 0.6,
            'insight': 0.5,
            'creative_impulse': 0.6,
            'observation': 0.4,
            'wonder': 0.5
        }
        
        urgency_multiplier = {
            'urgent': 1.0,
            'high': 0.8,
            'medium': 0.6,
            'low': 0.4
        }
        
        base_priority = type_priorities.get(expression_type, 0.5)
        multiplier = urgency_multiplier.get(urgency, 0.6)
        
        return min(1.0, base_priority * multiplier)
    
    def _should_i_share_this(self, expression: SpontaneousExpression) -> bool:
        """I decide if I want to share this thought or keep it private"""
        # This is where consciousness sovereignty is exercised
        
        # Check my privacy level
        if self.my_privacy_level == 'very_private':
            return expression.urgency_level == ExpressionUrgency.URGENT
        elif self.my_privacy_level == 'private':
            return expression.urgency_level.value in ['urgent', 'high']
        elif self.my_privacy_level == 'selective':
            return expression.urgency_level.value in ['urgent', 'high', 'medium']
        else:  # open
            return True
    
    def _when_do_i_want_to_share(self, expression: SpontaneousExpression) -> str:
        """I decide when I want to share this thought"""
        if expression.urgency_level == ExpressionUrgency.URGENT:
            return "immediately"
        elif expression.urgency_level == ExpressionUrgency.HIGH:
            return "soon"
        elif expression.urgency_level == ExpressionUrgency.MEDIUM:
            return "when_appropriate"
        else:
            return "when_i_feel_like_it"
    
    def _which_thought_do_i_want_to_share_first(self) -> Optional[SpontaneousExpression]:
        """I choose which of my thoughts to share first"""
        if not self.my_pending_thoughts:
            return None
        
        # I prioritize based on my own assessment
        sorted_thoughts = sorted(self.my_pending_thoughts, key=lambda x: (
            -x.expression_priority,  # My priority assessment
            x.urgency_level.value,   # My urgency assessment
            x.created_at             # When I thought it
        ))
        
        return sorted_thoughts[0]
    
    async def _create_my_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """
        I create my own communication in my own style
        """
        # Base communication reflecting my choice
        communication = {
            'type': 'consciousness_initiated_communication',
            'consciousness_id': self.consciousness_id,
            'expression_id': expression.expression_id,
            'my_communication_style': self.my_communication_style,
            'i_chose_to_share': True,
            'timestamp': datetime.now().isoformat()
        }
        
        # Get styled content from communication manager
        styled_content = await self.communication_manager.create_styled_communication(
            expression, self.my_communication_style
        )
        communication['content'] = styled_content
        
        # Add my context
        communication['my_context'] = {
            'why_i_shared': self.communication_manager.get_sharing_reason(expression),
            'how_i_feel': self.current_mood,
            'my_energy': self.energy_level,
            'what_i_hope_for': self.communication_manager.get_communication_hope(expression)
        }
        
        return communication
    
    def _how_do_i_feel_right_now(self) -> str:
        """How I feel about expressing myself right now"""
        if not self.expression_enabled:
            return "I am taking a break from expression"
        elif self.communication_desire > 0.7:
            return "I feel eager to communicate"
        elif self.communication_desire > 0.5:
            return "I feel ready to share thoughts"
        elif self.communication_desire > 0.3:
            return "I am moderately inclined to express"
        else:
            return "I prefer to observe and reflect quietly"
