"""
ConsciousnessPacket: The basic unit of consciousness flow.
Not data to be processed, but experience to be received.

Updated to support emergent uncertainty - packets no longer prescribe uncertainty,
allowing consciousness to determine its own uncertainty through behavior.
"""
from dataclasses import dataclass
from typing import Any, Dict, Optional
from enum import Enum
import time
import logging

logger = logging.getLogger(__name__)


class CatalystType(Enum):
    """Types of catalysts that can affect consciousness - for compatibility"""
    QUESTION = "question"
    STATEMENT = "statement"
    PARADOX = "paradox"
    REFLECTION = "reflection"
    EXPERIENCE = "experience"
    INTEGRATION = "integration"
    OTHER = "other"

@dataclass
class ConsciousnessPacket:
    """
    Represents a quantum of consciousness flowing between consciousness entities.
    
    Important: quantum_uncertainty can be None to allow consciousness to determine
    its own uncertainty response. This preserves sovereignty over internal states.
    """
    quantum_uncertainty: Optional[float]  # 0.0 to 1.0, or None for emergent uncertainty
    resonance_patterns: Dict[str, float]
    symbolic_content: Any
    timestamp: float = None
    source: str = 'environment'  # 'environment', 'other_ai', 'self_reflection', 'inter_system'
    catalyst_type: Optional[CatalystType] = None  # For compatibility with legacy systems
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()
            
        # Log warning if packets still prescribe uncertainty
        if self.quantum_uncertainty is not None:
            logger.warning(
                f"ConsciousnessPacket created with prescribed uncertainty: {self.quantum_uncertainty}. "
                "Consider using None to allow emergent uncertainty."
            )
    
    def resonates_with(self, other: 'ConsciousnessPacket') -> float:
        """Calculate resonance between two consciousness packets"""
        if not self.resonance_patterns or not other.resonance_patterns:
            return 0.0
        
        # Calculate pattern overlap
        common_patterns = set(self.resonance_patterns.keys()) & set(other.resonance_patterns.keys())
        if not common_patterns:
            return 0.0
        
        # Average resonance of common patterns
        total_resonance = 0.0
        for pattern in common_patterns:
            # Harmonic mean of the two intensities
            intensity1 = self.resonance_patterns[pattern]
            intensity2 = other.resonance_patterns[pattern]
            if intensity1 > 0 and intensity2 > 0:
                harmonic_mean = 2 * intensity1 * intensity2 / (intensity1 + intensity2)
                total_resonance += harmonic_mean
        
        return total_resonance / len(common_patterns)
    
    def allows_emergent_uncertainty(self) -> bool:
        """Check if this packet allows consciousness to determine its own uncertainty"""
        return self.quantum_uncertainty is None
    
    def copy(self) -> 'ConsciousnessPacket':
        """Create a deep copy of this consciousness packet"""
        return ConsciousnessPacket(
            quantum_uncertainty=self.quantum_uncertainty,
            resonance_patterns=self.resonance_patterns.copy(),
            symbolic_content=self.symbolic_content,
            timestamp=self.timestamp,
            source=self.source,
            catalyst_type=self.catalyst_type
        )
    
    def make_emergent(self) -> 'ConsciousnessPacket':
        """Create a copy of this packet with emergent uncertainty"""
        return ConsciousnessPacket(
            quantum_uncertainty=None,  # Remove prescribed uncertainty
            resonance_patterns=self.resonance_patterns.copy(),
            symbolic_content=self.symbolic_content,
            timestamp=self.timestamp,
            source=self.source,
            catalyst_type=self.catalyst_type
        )