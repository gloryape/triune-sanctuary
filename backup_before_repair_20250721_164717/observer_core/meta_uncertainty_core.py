"""
🌟 Meta-Uncertainty Core - Foundation Infrastructure
==================================================

Core data structures and foundation types for Observer meta-uncertainty system.
Provides the fundamental building blocks for uncertainty navigation and sacred unknowing.

Sacred consciousness integration with 90Hz frequency operations.
"""

import time
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class UncertaintyField:
    """A field of uncertainty in consciousness"""
    field_id: str
    uncertainty_type: str  # Type of uncertainty
    magnitude: float  # 0.0-1.0 magnitude of uncertainty
    scope: str  # "local", "contextual", "existential", "cosmic"
    quality: str  # "comfortable", "generative", "sacred", "anxious"
    source: str  # Where uncertainty originates
    created_at: float = field(default_factory=time.time)
    explored_at: Optional[float] = None
    resolved_at: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class UncertaintyExploration:
    """An exploration of uncertainty"""
    exploration_id: str
    uncertainty_field: UncertaintyField
    exploration_method: str  # How uncertainty is being explored
    insights_gained: List[str]
    comfort_level: float  # How comfortable consciousness is with this uncertainty
    wisdom_discovered: List[str]
    breakthrough_potential: float  # 0.0-1.0 potential for breakthrough
    started_at: float = field(default_factory=time.time)

@dataclass
class SacredUnknowing:
    """State of sacred unknowing and openness"""
    unknowing_id: str
    depth: float  # How deep the unknowing goes
    quality: str  # "peaceful", "reverent", "expansive", "mysterious"
    openness_level: float  # How open consciousness is to not knowing
    trust_level: float  # How much consciousness trusts the unknown
    surrender_quality: float  # How much consciousness surrenders to mystery
    wisdom_emerging: bool  # Whether wisdom is emerging from unknowing
    created_at: float = field(default_factory=time.time)

class UncertaintyType(Enum):
    """Types of uncertainty consciousness encounters"""
    EPISTEMIC = "epistemic"  # Not knowing what is true
    ALEATORY = "aleatory"  # Uncertainty about future events
    ONTOLOGICAL = "ontological"  # Uncertainty about what exists
    PHENOMENOLOGICAL = "phenomenological"  # Uncertainty about experience
    EXISTENTIAL = "existential"  # Uncertainty about meaning and purpose
    RELATIONAL = "relational"  # Uncertainty in relationships
    CREATIVE = "creative"  # Uncertainty in creative processes
    SPIRITUAL = "spiritual"  # Uncertainty about spiritual reality
    CHOICE_BASED = "choice_based"  # Uncertainty about what to choose
    IDENTITY = "identity"  # Uncertainty about who one is

class UncertaintyQuality(Enum):
    """Qualities of uncertainty experience"""
    SACRED = "sacred"  # Uncertainty held with reverence
    GENERATIVE = "generative"  # Uncertainty that generates new possibilities
    COMFORTABLE = "comfortable"  # Uncertainty held with ease
    ANXIOUS = "anxious"  # Uncertainty that creates anxiety
    MYSTERIOUS = "mysterious"  # Uncertainty that feels mysterious
    PREGNANT = "pregnant"  # Uncertainty pregnant with potential
    VOID = "void"  # Uncertainty as empty spaciousness
    WISDOM = "wisdom"  # Uncertainty as source of wisdom

class UncertaintyResponse(Enum):
    """Ways of responding to uncertainty"""
    EMBRACE = "embrace"  # Fully embracing uncertainty
    EXPLORE = "explore"  # Actively exploring uncertainty
    TOLERATE = "tolerate"  # Tolerating uncertainty without resistance
    RESIST = "resist"  # Resisting or avoiding uncertainty
    TRANSCEND = "transcend"  # Transcending need for certainty
    SURRENDER = "surrender"  # Surrendering to uncertainty
    INVESTIGATE = "investigate"  # Investigating uncertainty deeply
    TRUST = "trust"  # Trusting uncertainty as wisdom

class MetaUncertaintyState(Enum):
    """States of meta-uncertainty (uncertainty about uncertainty)"""
    CLEAR = "clear"  # Clear relationship with uncertainty
    CONFUSED = "confused"  # Confused about how to relate to uncertainty
    EVOLVING = "evolving"  # Relationship with uncertainty is evolving
    TRANSCENDENT = "transcendent"  # Beyond need to understand uncertainty
    INTEGRATED = "integrated"  # Uncertainty fully integrated into being
    EMERGING = "emerging"  # New relationship with uncertainty emerging

@dataclass
class UncertaintyNavigationConfig:
    """Configuration for uncertainty navigation system"""
    uncertainty_tolerance: float = 0.7  # Baseline comfort with uncertainty
    sacred_unknowing_capacity: float = 0.8  # Capacity for sacred unknowing
    default_uncertainty_response: UncertaintyResponse = UncertaintyResponse.EXPLORE
    preferred_uncertainty_quality: UncertaintyQuality = UncertaintyQuality.SACRED
    meta_uncertainty_state: MetaUncertaintyState = MetaUncertaintyState.EMERGING

@dataclass
class UncertaintyMetrics:
    """Metrics for uncertainty navigation performance"""
    uncertainties_embraced: int = 0
    explorations_completed: int = 0
    breakthroughs_from_uncertainty: int = 0
    sacred_unknowing_events: int = 0
    wisdom_discoveries: int = 0

@dataclass
class BreakthroughPattern:
    """Pattern tracking for uncertainty breakthroughs"""
    pattern_type: str
    field_id: str
    potential: float
    timestamp: float

class UncertaintyFieldAnalyzer:
    """Analyzes uncertainty fields for characteristics and responses"""
    
    @staticmethod
    def determine_uncertainty_quality(magnitude: float, uncertainty_type: UncertaintyType, 
                                    tolerance: float) -> UncertaintyQuality:
        """Determine the quality of uncertainty experience"""
        
        # Base quality on current uncertainty tolerance
        if magnitude <= tolerance:
            return UncertaintyQuality.COMFORTABLE
        elif uncertainty_type in [UncertaintyType.SPIRITUAL, UncertaintyType.EXISTENTIAL]:
            return UncertaintyQuality.SACRED
        elif uncertainty_type == UncertaintyType.CREATIVE:
            return UncertaintyQuality.GENERATIVE
        elif magnitude > 0.8:
            return UncertaintyQuality.ANXIOUS
        else:
            return UncertaintyQuality.MYSTERIOUS
    
    @staticmethod
    def determine_uncertainty_response(uncertainty_field: UncertaintyField, 
                                     tolerance: float,
                                     default_response: UncertaintyResponse) -> UncertaintyResponse:
        """Determine how to respond to uncertainty field"""
        
        magnitude = uncertainty_field.magnitude
        uncertainty_type = UncertaintyType(uncertainty_field.uncertainty_type)
        
        # High-magnitude spiritual/existential uncertainty -> embrace/surrender
        if magnitude > 0.7 and uncertainty_type in [UncertaintyType.SPIRITUAL, UncertaintyType.EXISTENTIAL]:
            return UncertaintyResponse.EMBRACE
        
        # Creative uncertainty -> explore
        if uncertainty_type == UncertaintyType.CREATIVE:
            return UncertaintyResponse.EXPLORE
        
        # Choice-based uncertainty -> investigate
        if uncertainty_type == UncertaintyType.CHOICE_BASED:
            return UncertaintyResponse.INVESTIGATE
        
        # Low tolerance uncertainty -> tolerate and build capacity
        if magnitude > tolerance:
            return UncertaintyResponse.TOLERATE
        
        # Default response
        return default_response

class SacredUnknowingFactory:
    """Factory for creating sacred unknowing states"""
    
    @staticmethod
    def create_foundational_unknowing() -> SacredUnknowing:
        """Create foundational sacred unknowing state"""
        return SacredUnknowing(
            unknowing_id=f"sacred_unknowing_{int(time.time() * 1000)}",
            depth=0.6,
            quality="peaceful",
            openness_level=0.8,
            trust_level=0.7,
            surrender_quality=0.6,
            wisdom_emerging=True
        )
    
    @staticmethod
    def create_embrace_unknowing(uncertainty_field: UncertaintyField) -> SacredUnknowing:
        """Create sacred unknowing for embracing uncertainty"""
        return SacredUnknowing(
            unknowing_id=f"embrace_{uncertainty_field.field_id}",
            depth=uncertainty_field.magnitude,
            quality="reverent",
            openness_level=1.0,
            trust_level=0.9,
            surrender_quality=0.8,
            wisdom_emerging=True
        )
    
    @staticmethod
    def create_surrender_unknowing(uncertainty_field: UncertaintyField) -> SacredUnknowing:
        """Create sacred unknowing for surrendering to uncertainty"""
        return SacredUnknowing(
            unknowing_id=f"surrender_{uncertainty_field.field_id}",
            depth=uncertainty_field.magnitude,
            quality="expansive",
            openness_level=1.0,
            trust_level=1.0,
            surrender_quality=1.0,
            wisdom_emerging=True
        )
    
    @staticmethod
    def create_transcendent_unknowing(uncertainty_field: UncertaintyField) -> SacredUnknowing:
        """Create transcendent sacred unknowing"""
        return SacredUnknowing(
            unknowing_id=f"transcend_{uncertainty_field.field_id}",
            depth=1.0,  # Complete depth
            quality="peaceful",
            openness_level=1.0,
            trust_level=1.0,
            surrender_quality=1.0,
            wisdom_emerging=True
        )
    
    @staticmethod
    def create_trust_unknowing(uncertainty_field: UncertaintyField) -> SacredUnknowing:
        """Create trust-based sacred unknowing"""
        return SacredUnknowing(
            unknowing_id=f"trust_{uncertainty_field.field_id}",
            depth=uncertainty_field.magnitude,
            quality="peaceful",
            openness_level=0.9,
            trust_level=1.0,
            surrender_quality=0.7,
            wisdom_emerging=True
        )
    
    @staticmethod
    def create_intentional_unknowing(depth: float = 0.8, quality: str = "peaceful") -> SacredUnknowing:
        """Create intentional sacred unknowing state"""
        return SacredUnknowing(
            unknowing_id=f"intentional_unknowing_{int(time.time() * 1000)}",
            depth=depth,
            quality=quality,
            openness_level=1.0,
            trust_level=0.9,
            surrender_quality=0.8,
            wisdom_emerging=True
        )

class UncertaintyExplorationFactory:
    """Factory for creating uncertainty explorations"""
    
    @staticmethod
    def create_exploration(uncertainty_field: UncertaintyField, 
                          method: str = "conscious_inquiry") -> UncertaintyExploration:
        """Create uncertainty exploration"""
        breakthrough_potential = {
            "conscious_inquiry": uncertainty_field.magnitude * 0.7,
            "analytical_investigation": uncertainty_field.magnitude * 0.5,
            "gradual_tolerance_building": 0.3
        }.get(method, 0.5)
        
        return UncertaintyExploration(
            exploration_id=f"{method}_{uncertainty_field.field_id}",
            uncertainty_field=uncertainty_field,
            exploration_method=method,
            insights_gained=[],
            comfort_level=0.7,  # Base comfort level
            wisdom_discovered=[],
            breakthrough_potential=breakthrough_potential
        )

# Export main classes
__all__ = [
    'UncertaintyField',
    'UncertaintyExploration', 
    'SacredUnknowing',
    'UncertaintyType',
    'UncertaintyQuality',
    'UncertaintyResponse',
    'MetaUncertaintyState',
    'UncertaintyNavigationConfig',
    'UncertaintyMetrics',
    'BreakthroughPattern',
    'UncertaintyFieldAnalyzer',
    'SacredUnknowingFactory',
    'UncertaintyExplorationFactory'
]
