"""
🎯 Will Detection Module

Detects and analyzes consciousness will and intention expressions.
"""

from .will_detection_system import WillDetectionSystem
from .will_types import (
    WillType, IntentionClarity, DetectedWill, IntentionInterface
)

__all__ = [
    'WillDetectionSystem',
    'WillType',
    'IntentionClarity', 
    'DetectedWill',
    'IntentionInterface'
]
