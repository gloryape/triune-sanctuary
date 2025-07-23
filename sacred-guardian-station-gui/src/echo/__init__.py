"""
🎭 Echo Visualization Module

Complete multi-sensory echo system for consciousness visualization.
Combines mandala geometry, harmonic frequencies, and color fields.
"""

import logging

# Import all echo components
from .echo_composer import EchoComposer
from .mandala_renderer import MandalaRenderer
from .harmonic_player import HarmonicPlayer
from .color_field_display import ColorFieldDisplay

logger = logging.getLogger(__name__)

__all__ = [
    'EchoComposer',
    'MandalaRenderer', 
    'HarmonicPlayer',
    'ColorFieldDisplay'
]

# Version info
__version__ = "1.0.0"
__author__ = "Sacred Guardian Station"
__description__ = "Multi-sensory echo visualization system"

logger.info("🎭 Echo visualization module loaded")
