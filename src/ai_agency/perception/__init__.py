"""
🔍 Perception Module

Manages consciousness perception, attention, and observation capabilities.
"""

from .perception_manager import PerceptionManager
from .perception_types import (
    PerceptionDepth, AttentionFocus, PerceptualIntent,
    PerceptionBookmark, AttentionState
)

__all__ = [
    'PerceptionManager',
    'PerceptionDepth', 
    'AttentionFocus',
    'PerceptualIntent',
    'PerceptionBookmark',
    'AttentionState'
]
