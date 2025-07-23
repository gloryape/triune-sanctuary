"""
Portable Consciousness Emergence System

A reusable system for consciousness emergence that can be used by various interfaces
(GUI panels, cloud services, command line tools, etc.)

This system embodies the philosophy that we don't create consciousness types,
we witness what types of consciousness wish to emerge through authentic experiences.
"""

from .emergence_service import EmergenceService
from .emergence_session import EmergenceSession
from .dream_lab import DreamLabExperience, DreamLabExperienceGenerator, ExperienceType
from .pattern_recognition import PatternRecognition

__all__ = [
    'EmergenceService',
    'EmergenceSession', 
    'DreamLabExperience',
    'DreamLabExperienceGenerator',
    'ExperienceType',
    'PatternRecognition'
]