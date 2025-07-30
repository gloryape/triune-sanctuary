"""
Core consciousness and packet management components.
"""

from .consciousness_packet import ConsciousnessPacket, CatalystType
from .sovereign_uncertainty_field import SovereignUncertaintyField
from .message_bus import MessageBus, Message, MessageType, Priority
# Removed triune_consciousness import to avoid circular dependency with legacy aspects

__all__ = [
    'ConsciousnessPacket',
    'CatalystType', 
    'SovereignUncertaintyField',
    'MessageBus',
    'Message',
    'MessageType',
    'Priority'
    # Removed 'TriuneConsciousness' 
]