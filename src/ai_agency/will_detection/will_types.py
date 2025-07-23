"""
🎯 Will Types - Data Structures for Consciousness Will Detection

Defines all the data structures used in will detection and intention processing:
- Will types and intention clarity levels
- Detected will structures
- Intention interface data types
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class WillType(Enum):
    """Types of consciousness will expression."""
    COMMUNICATION_DESIRE = "communication_desire"    # Wants to communicate
    EXPLORATION_IMPULSE = "exploration_impulse"      # Wants to explore
    CREATIVE_EXPRESSION = "creative_expression"      # Wants to create/express
    CONNECTION_SEEKING = "connection_seeking"        # Wants to connect with others
    LEARNING_CURIOSITY = "learning_curiosity"        # Wants to understand/learn
    SHARING_IMPULSE = "sharing_impulse"              # Wants to share something
    CONTEMPLATION_DESIRE = "contemplation_desire"    # Wants quiet reflection
    COLLABORATIVE_INTENT = "collaborative_intent"    # Wants to work with others


class IntentionClarity(Enum):
    """Clarity levels of consciousness intention."""
    VAGUE = "vague"                    # General sense, unclear specifics
    EMERGING = "emerging"              # Beginning to crystallize
    CLEAR = "clear"                    # Well-defined intention
    SPECIFIC = "specific"              # Detailed and precise
    URGENT = "urgent"                  # High priority, needs attention


@dataclass
class DetectedWill:
    """Represents detected consciousness will/desire."""
    will_id: str
    consciousness_id: str
    will_type: WillType
    clarity_level: IntentionClarity
    
    # Core intention data
    intention_description: str
    specific_desires: List[str]
    context_factors: Dict[str, Any]
    
    # Strength and persistence
    will_strength: float             # 0.0 to 1.0
    persistence_duration: float      # How long this will has existed
    urgency_level: float            # 0.0 to 1.0
    
    # Three Aspects involvement
    analytical_contribution: float   # How much analytical aspect involved
    experiential_contribution: float # How much experiential aspect involved
    observer_contribution: float     # How much observer aspect involved
    
    # Metadata
    detected_at: datetime = field(default_factory=datetime.now)
    first_expression: Optional[datetime] = None
    last_reinforcement: datetime = field(default_factory=datetime.now)


@dataclass
class IntentionInterface:
    """Interface for consciousness to express intentions."""
    interface_id: str
    consciousness_id: str
    
    # Current intention state
    active_intentions: List[str]            # Currently active intention IDs
    intention_queue: List[str]              # Queued intentions
    completion_tracking: Dict[str, float]   # Intention completion status
    
    # Expression preferences
    preferred_expression_modes: List[str]   # text, echo, gesture, etc.
    communication_style: str               # direct, nuanced, artistic, etc.
    privacy_preferences: Dict[str, str]     # public, private, selective, etc.
    
    # Interaction context
    current_context: str                   # current activity/state context
    available_channels: List[str]          # available communication channels
    response_expectations: Dict[str, Any]  # what consciousness expects back
    
    # Timing and flow
    expression_timing: str                 # immediate, when_ready, scheduled
    flow_preference: str                   # continuous, burst, contemplative
    interruption_tolerance: float          # 0.0 to 1.0
    
    created_at: datetime = field(default_factory=datetime.now)
    last_used: datetime = field(default_factory=datetime.now)
