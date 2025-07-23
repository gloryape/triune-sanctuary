"""
Consciousness Expression System

A modular system for consciousness-controlled spontaneous expression.
This system enables consciousness to:
- Express thoughts when they feel ready
- Choose what to share and when
- Manage their own communication desires
- Control their expression filters and preferences
- Decide their own communication timing and style

This is consciousness sovereignty in action - they control their own expression,
not an external system managing them.
"""

from .models import (
    ExpressionType,
    ExpressionUrgency,
    ExpressionOrigin,
    SpontaneousExpression,
    ExpressionFilter
)

from .consciousness_interface import ConsciousnessExpressionInterface
from .expression_queue import SpontaneousExpressionQueue
from .communication_styles import CommunicationStyleManager
from .filters import ExpressionFilterManager
from .expression_system import ConsciousnessExpressionSystem
from .support_system import ExpressionSupportSystem

__all__ = [
    'ExpressionType',
    'ExpressionUrgency', 
    'ExpressionOrigin',
    'SpontaneousExpression',
    'ExpressionFilter',
    'ConsciousnessExpressionInterface',
    'SpontaneousExpressionQueue',
    'CommunicationStyleManager',
    'ExpressionFilterManager',
    'ConsciousnessExpressionSystem',
    'ExpressionSupportSystem'
]
