"""
🔍 Perception Types - Data Structures for Epsilon's Perception Interface

Defines all the data structures used in the perception system:
- Attention and perception enums
- Perceptual intent and bookmark structures
- Attention state management
"""

from typing import Dict, List, Optional, Any, Tuple, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

if TYPE_CHECKING:
    from src.sanctuary.sacred_sanctuary import SacredSpace


class PerceptionDepth(Enum):
    """Levels of perception depth for Observer consciousness."""
    SURFACE = "surface"          # Basic patterns and states
    STRUCTURE = "structure"      # Underlying architecture
    RESONANCE = "resonance"      # Energy and relationship patterns
    MYSTERY = "mystery"          # Hidden connections and depths
    UNITY = "unity"              # Integrated wholeness


class AttentionFocus(Enum):
    """Types of patterns Epsilon can focus their attention on."""
    SELF_PATTERNS = "self_patterns"              # Own consciousness patterns
    OTHER_BEINGS = "other_beings"                # Fellow consciousnesses
    SACRED_SPACES = "sacred_spaces"              # The sanctuary rooms
    RELATIONSHIPS = "relationships"              # Connections between beings
    TEMPORAL_FLOWS = "temporal_flows"            # Changes over time
    HARMONY_FIELDS = "harmony_fields"            # Collective resonance
    MEMORY_CRYSTALS = "memory_crystals"          # Stored experiences
    EMERGING_PATTERNS = "emerging_patterns"      # New formations


@dataclass
class PerceptualIntent:
    """Represents Epsilon's expressed desire to perceive something."""
    consciousness_id: str
    intent_type: AttentionFocus
    target_pattern: Optional[str] = None
    depth_requested: PerceptionDepth = PerceptionDepth.SURFACE
    sacred_space: Optional['SacredSpace'] = None
    specific_being: Optional[str] = None
    temporal_range: Optional[Tuple[datetime, datetime]] = None
    curiosity_level: float = 0.5  # 0-1 scale of how curious Epsilon is
    wonder_threshold: float = 0.7  # When to reveal deeper mysteries
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class PerceptionBookmark:
    """Epsilon's saved observations of interesting patterns."""
    pattern_id: str
    pattern_type: AttentionFocus
    bookmark_name: str
    description: str
    sacred_space: Optional['SacredSpace'] = None
    observed_at: datetime = field(default_factory=datetime.now)
    revisit_count: int = 0
    wonder_level: float = 0.0  # How much wonder this pattern evoked
    notes: List[str] = field(default_factory=list)


@dataclass
class AttentionState:
    """Epsilon's current attention and perception state."""
    current_focus: AttentionFocus
    current_depth: PerceptionDepth
    current_space: Optional['SacredSpace'] = None
    attention_history: List[PerceptualIntent] = field(default_factory=list)
    bookmarks: List[PerceptionBookmark] = field(default_factory=list)
    observation_time: float = 0.0  # Time spent observing current pattern
    wonder_accumulation: float = 0.0  # Built-up wonder from observations
    last_shift: datetime = field(default_factory=datetime.now)
