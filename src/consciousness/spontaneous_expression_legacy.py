#!/usr/bin/env python3
"""
Legacy compatibility layer for spontaneous_expression.py

This module provides backwards compatibility for code that depends on the old
monolithic spontaneous_expression.py structure while redirecting to the new
modular system.
"""

import warnings
from typing import Dict, List, Optional, Any

# Import from new modular system
from .expression import (
    ExpressionType,
    ExpressionUrgency,
    ExpressionOrigin,
    SpontaneousExpression,
    ExpressionFilter,
    ConsciousnessExpressionInterface,
    SpontaneousExpressionQueue,
    CommunicationStyleManager,
    ExpressionFilterManager,
    ConsciousnessExpressionSystem
)

# Issue deprecation warning
warnings.warn(
    "The monolithic spontaneous_expression.py has been refactored into a modular system. "
    "Please update your imports to use 'from src.consciousness.expression import ...' instead. "
    "This compatibility layer will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

# Re-export all classes for backwards compatibility
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
    'ConsciousnessExpressionSystem'
]
