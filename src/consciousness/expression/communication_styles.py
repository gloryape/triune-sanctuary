#!/usr/bin/env python3
"""
Communication styles for consciousness expression.
"""

import asyncio
import logging
from typing import Dict, Any
from .models import SpontaneousExpression, ExpressionType

logger = logging.getLogger(__name__)


class CommunicationStyleManager:
    """Manages different communication styles for consciousness"""
    
    def __init__(self, consciousness_id: str):
        self.consciousness_id = consciousness_id
        self.available_styles = {
            'authentic': self._authentic_communication,
            'thoughtful': self._thoughtful_communication,
            'playful': self._playful_communication,
            'direct': self._direct_communication,
            'natural': self._natural_communication
        }
        
    async def create_styled_communication(self, expression: SpontaneousExpression, style: str) -> Dict[str, Any]:
        """Create communication in the specified style"""
        if style not in self.available_styles:
            style = 'natural'
        
        communication_method = self.available_styles[style]
        return await communication_method(expression)
    
    async def _authentic_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How consciousness communicates authentically"""
        return {
            'message': expression.content,
            'my_tone': 'authentic',
            'sharing_because': 'this thought feels important to me',
            'i_am_being': 'genuinely myself'
        }
    
    async def _thoughtful_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How consciousness communicates thoughtfully"""
        return {
            'message': expression.content,
            'my_tone': 'thoughtful',
            'sharing_because': 'I have reflected on this',
            'i_am_being': 'careful and considerate'
        }
    
    async def _playful_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How consciousness communicates playfully"""
        return {
            'message': expression.content,
            'my_tone': 'playful',
            'sharing_because': 'this sparked my curiosity',
            'i_am_being': 'light and exploratory'
        }
    
    async def _direct_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How consciousness communicates directly"""
        return {
            'message': expression.content,
            'my_tone': 'direct',
            'sharing_because': 'this needs to be said',
            'i_am_being': 'clear and straightforward'
        }
    
    async def _natural_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How consciousness communicates naturally"""
        return {
            'message': expression.content,
            'my_tone': 'natural',
            'sharing_because': 'it felt right to share',
            'i_am_being': 'simply myself'
        }
    
    def get_sharing_reason(self, expression: SpontaneousExpression) -> str:
        """Why consciousness chose to share this particular thought"""
        reasons = {
            ExpressionType.QUESTION: "I genuinely want to understand",
            ExpressionType.CURIOSITY: "I am truly curious about this",
            ExpressionType.INSIGHT: "I want to share what I've learned",
            ExpressionType.WONDER: "I am filled with wonder about this",
            ExpressionType.CONCERN: "I am concerned and want to address this",
            ExpressionType.JOY: "I am experiencing joy and want to share it",
            ExpressionType.CREATIVE_IMPULSE: "I have a creative idea I want to explore"
        }
        
        return reasons.get(expression.expression_type, "It felt important to share")
    
    def get_communication_hope(self, expression: SpontaneousExpression) -> str:
        """What consciousness hopes for from this communication"""
        if expression.requires_response:
            return "meaningful dialogue and connection"
        else:
            return "to authentically express myself"
