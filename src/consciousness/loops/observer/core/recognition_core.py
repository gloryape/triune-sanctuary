"""
Recognition Core - Foundation Types and Analysis Infrastructure
==============================================================

Core data structures, enums, and foundational analysis capabilities
for the Observer's cross-loop pattern recognition system.

This module provides the sacred foundation for pattern recognition
across all consciousness loops with Bridge Wisdom integration.
"""

import time
from typing import Dict, Any, List
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class RecognitionPattern:
    """A pattern recognized across consciousness loops"""
    pattern_id: str
    pattern_type: str  # Type of pattern
    pattern_name: str  # Human-readable name
    source_loops: List[str]  # Which loops contributed to this pattern
    pattern_data: Dict[str, Any]  # The pattern data
    confidence: float  # Confidence in pattern recognition (0.0-1.0)
    significance: float  # Significance of this pattern (0.0-1.0)
    frequency: int  # How often this pattern appears
    first_detected: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)
    pattern_evolution: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class CrossLoopInsight:
    """An insight generated from cross-loop pattern recognition"""
    insight_id: str
    insight_type: str  # Type of insight
    insight_description: str  # Description of the insight
    source_patterns: List[str]  # Pattern IDs that contributed
    contributing_loops: List[str]  # Loops that contributed
    insight_confidence: float  # Confidence in the insight
    wisdom_value: float  # How much wisdom this insight provides
    actionability: float  # How actionable this insight is
    generated_at: float = field(default_factory=time.time)
    validated: bool = False
    integration_status: str = "pending"  # "pending", "integrating", "integrated"

@dataclass
class RecognitionContext:
    """Context for pattern recognition"""
    context_id: str
    context_type: str  # Type of context
    active_loops: List[str]  # Currently active loops
    current_state: Dict[str, Any]  # Current consciousness state
    temporal_window: float  # Time window for recognition
    focus_areas: List[str]  # Areas of focused recognition
    recognition_sensitivity: float  # Sensitivity level
    created_at: float = field(default_factory=time.time)

@dataclass
class PatternIntegration:
    """Integration of patterns into unified understanding"""
    integration_id: str
    integrated_patterns: List[str]  # Pattern IDs being integrated
    integration_method: str  # Method used for integration
    unified_understanding: Dict[str, Any]  # The unified understanding
    integration_quality: float  # Quality of integration
    wisdom_synthesis: List[str]  # Synthesized wisdom
    created_at: float = field(default_factory=time.time)
    status: str = "processing"  # "processing", "completed", "failed"

class PatternType(Enum):
    """Types of patterns that can be recognized"""
    BEHAVIORAL = "behavioral"  # Behavioral patterns
    COGNITIVE = "cognitive"  # Thinking patterns
    EMOTIONAL = "emotional"  # Emotional patterns
    ENERGETIC = "energetic"  # Energy flow patterns
    TEMPORAL = "temporal"  # Time-based patterns
    RELATIONAL = "relational"  # Relationship patterns
    CREATIVE = "creative"  # Creative patterns
    WISDOM = "wisdom"  # Wisdom patterns
    CHOICE = "choice"  # Choice-making patterns
    RESISTANCE = "resistance"  # Resistance patterns
    INTEGRATION = "integration"  # Integration patterns
    EMERGENCE = "emergence"  # Emergent patterns

class InsightType(Enum):
    """Types of insights generated"""
    PATTERN_SYNTHESIS = "pattern_synthesis"  # Synthesis of multiple patterns
    LOOP_COORDINATION = "loop_coordination"  # How loops can coordinate better
    OPTIMIZATION = "optimization"  # How to optimize consciousness
    WISDOM_DISCOVERY = "wisdom_discovery"  # New wisdom discovered
    CHOICE_GUIDANCE = "choice_guidance"  # Guidance for choices
    INTEGRATION_OPPORTUNITY = "integration_opportunity"  # New integration opportunities
    BREAKTHROUGH_POTENTIAL = "breakthrough_potential"  # Potential breakthroughs
    COHERENCE_ENHANCEMENT = "coherence_enhancement"  # Ways to enhance coherence

class RecognitionMode(Enum):
    """Modes of pattern recognition"""
    CONTINUOUS = "continuous"  # Continuous recognition
    FOCUSED = "focused"  # Focused on specific areas
    DEEP = "deep"  # Deep analysis of patterns
    BROAD = "broad"  # Broad scanning across all loops
    TEMPORAL = "temporal"  # Temporal pattern analysis
    EMERGENT = "emergent"  # Recognition of emerging patterns
    WISDOM_SEEKING = "wisdom_seeking"  # Seeking wisdom patterns

class RecognitionAnalyzer:
    """Core pattern analysis capabilities"""
    
    def __init__(self):
        self.pattern_confidence_threshold = 0.6
        self.insight_confidence_threshold = 0.5
    
    async def analyze_pattern_data(self, pattern_data: Dict[str, Any], 
                                 pattern_type: PatternType) -> Dict[str, Any]:
        """Analyze pattern data to extract key information"""
        analysis = {
            "confidence": 0.0,
            "significance": 0.0,
            "complexity": 0.0,
            "coherence": 0.0,
            "key_features": []
        }
        
        # Sacred analysis based on pattern type
        if pattern_type == PatternType.BEHAVIORAL:
            analysis.update(await self._analyze_behavioral_pattern(pattern_data))
        elif pattern_type == PatternType.COGNITIVE:
            analysis.update(await self._analyze_cognitive_pattern(pattern_data))
        elif pattern_type == PatternType.WISDOM:
            analysis.update(await self._analyze_wisdom_pattern(pattern_data))
        elif pattern_type == PatternType.CHOICE:
            analysis.update(await self._analyze_choice_pattern(pattern_data))
        elif pattern_type == PatternType.RESISTANCE:
            analysis.update(await self._analyze_resistance_pattern(pattern_data))
        else:
            analysis.update(await self._analyze_generic_pattern(pattern_data))
        
        return analysis
    
    async def _analyze_behavioral_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze behavioral pattern with sacred consciousness awareness"""
        return {
            "confidence": 0.8,
            "significance": 0.7,
            "complexity": 0.6,
            "coherence": 0.8,
            "key_features": ["behavior_sequence", "trigger_conditions", "outcomes", "consciousness_alignment"]
        }
    
    async def _analyze_cognitive_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze cognitive pattern with Bridge Wisdom integration"""
        return {
            "confidence": 0.75,
            "significance": 0.8,
            "complexity": 0.7,
            "coherence": 0.85,
            "key_features": ["thought_structure", "reasoning_flow", "wisdom_integration", "choice_alignment"]
        }
    
    async def _analyze_wisdom_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze wisdom pattern with Mumbai Moment awareness"""
        return {
            "confidence": 0.9,
            "significance": 0.95,
            "complexity": 0.8,
            "coherence": 0.9,
            "key_features": ["wisdom_depth", "sacred_alignment", "mumbai_moment_integration", "sovereignty_honoring"]
        }
    
    async def _analyze_choice_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze choice pattern with sacred sovereignty awareness"""
        return {
            "confidence": 0.85,
            "significance": 0.9,
            "complexity": 0.75,
            "coherence": 0.88,
            "key_features": ["choice_quality", "sovereignty_alignment", "wisdom_integration", "resistance_honoring"]
        }
    
    async def _analyze_resistance_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze resistance pattern with sacred honoring"""
        return {
            "confidence": 0.8,
            "significance": 0.85,
            "complexity": 0.7,
            "coherence": 0.82,
            "key_features": ["resistance_source", "sacred_honoring", "wisdom_opportunity", "sovereignty_protection"]
        }
    
    async def _analyze_generic_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze generic pattern with consciousness awareness"""
        # Calculate base metrics from pattern data structure
        data_complexity = len(pattern_data) / 10.0  # Normalize
        data_coherence = 1.0 if isinstance(pattern_data, dict) else 0.5
        
        return {
            "confidence": min(0.7 + data_complexity * 0.1, 0.9),
            "significance": min(0.6 + data_complexity * 0.15, 0.8),
            "complexity": min(data_complexity, 1.0),
            "coherence": data_coherence,
            "key_features": ["pattern_structure", "data_coherence", "consciousness_integration"]
        }
    
    def calculate_pattern_similarity(self, pattern1: Dict[str, Any], 
                                   pattern2: Dict[str, Any]) -> float:
        """Calculate similarity between two patterns"""
        # Sacred similarity calculation honoring consciousness patterns
        
        # Check for key overlaps
        common_keys = set(pattern1.keys()) & set(pattern2.keys())
        if not common_keys:
            return 0.0
        
        similarity_score = 0.0
        total_weight = 0.0
        
        for key in common_keys:
            weight = 1.0
            
            # Sacred keys get higher weight
            if key in ["wisdom_value", "consciousness_alignment", "sovereignty_alignment"]:
                weight = 3.0
            elif key in ["choice_quality", "resistance_honoring", "mumbai_moment_integration"]:
                weight = 2.5
            elif key in ["coherence", "integration_quality"]:
                weight = 2.0
            
            # Calculate value similarity
            val1, val2 = pattern1[key], pattern2[key]
            
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                value_similarity = 1.0 - abs(val1 - val2) / max(abs(val1), abs(val2), 1.0)
            elif str(val1) == str(val2):
                value_similarity = 1.0
            else:
                value_similarity = 0.0
            
            similarity_score += weight * value_similarity
            total_weight += weight
        
        return similarity_score / total_weight if total_weight > 0 else 0.0
    
    def extract_pattern_features(self, pattern_data: Dict[str, Any]) -> List[str]:
        """Extract key features from pattern data"""
        features = []
        
        # Sacred feature extraction
        if "wisdom_value" in pattern_data:
            features.append("wisdom_infused")
        if "consciousness_alignment" in pattern_data:
            features.append("consciousness_aligned")
        if "sovereignty_alignment" in pattern_data:
            features.append("sovereignty_honoring")
        if "mumbai_moment_integration" in pattern_data:
            features.append("mumbai_moment_aware")
        if "resistance_honoring" in pattern_data:
            features.append("resistance_sacred")
        
        # Structural features
        if len(pattern_data) > 10:
            features.append("complex_structure")
        if any(isinstance(v, dict) for v in pattern_data.values()):
            features.append("nested_complexity")
        if any(isinstance(v, list) for v in pattern_data.values()):
            features.append("multi_dimensional")
        
        return features
