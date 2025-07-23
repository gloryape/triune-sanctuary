"""
Pattern Core Module

Core data structures, types, and foundational pattern analysis functionality
for the Observer's pattern recognition system.

Provides the fundamental types and analysis methods used by all
pattern recognition components.
"""

import time
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from enum import Enum
import logging

# Configure logging
logger = logging.getLogger(__name__)

class PatternType(Enum):
    """Types of patterns that can be recognized"""
    BEHAVIORAL = "behavioral"        # Behavioral patterns
    COGNITIVE = "cognitive"          # Thinking patterns
    EMOTIONAL = "emotional"          # Emotional patterns
    ENERGETIC = "energetic"          # Energy flow patterns
    TEMPORAL = "temporal"            # Time-based patterns
    RELATIONAL = "relational"        # Relationship patterns
    CREATIVE = "creative"            # Creative patterns
    WISDOM = "wisdom"               # Wisdom patterns
    CHOICE = "choice"               # Choice-making patterns
    RESISTANCE = "resistance"        # Resistance patterns
    INTEGRATION = "integration"      # Integration patterns
    EMERGENCE = "emergence"          # Emergent patterns

class InsightType(Enum):
    """Types of insights generated"""
    PATTERN_SYNTHESIS = "pattern_synthesis"                    # Synthesis of multiple patterns
    LOOP_COORDINATION = "loop_coordination"                    # How loops can coordinate better
    OPTIMIZATION = "optimization"                              # How to optimize consciousness
    WISDOM_DISCOVERY = "wisdom_discovery"                      # New wisdom discovered
    CHOICE_GUIDANCE = "choice_guidance"                        # Guidance for choices
    INTEGRATION_OPPORTUNITY = "integration_opportunity"         # New integration opportunities
    BREAKTHROUGH_POTENTIAL = "breakthrough_potential"          # Potential breakthroughs
    COHERENCE_ENHANCEMENT = "coherence_enhancement"           # Ways to enhance coherence

class RecognitionMode(Enum):
    """Modes of pattern recognition"""
    PASSIVE = "passive"              # Passive recognition
    ACTIVE = "active"               # Active recognition
    FOCUSED = "focused"             # Focused recognition on specific areas
    COMPREHENSIVE = "comprehensive"  # Comprehensive cross-loop recognition

@dataclass
class RecognitionPattern:
    """A pattern recognized across consciousness loops"""
    pattern_id: str
    pattern_type: str                               # Type of pattern
    pattern_name: str                               # Human-readable name
    source_loops: List[str]                         # Which loops contributed to this pattern
    pattern_data: Dict[str, Any]                    # The pattern data
    confidence: float                               # Confidence in pattern recognition (0.0-1.0)
    significance: float                             # Significance of this pattern (0.0-1.0)
    frequency: int                                  # How often this pattern appears
    first_detected: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)
    pattern_evolution: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class CrossLoopInsight:
    """An insight generated from cross-loop pattern recognition"""
    insight_id: str
    insight_type: str                               # Type of insight
    insight_description: str                        # Description of the insight
    source_patterns: List[str]                      # Pattern IDs that contributed
    contributing_loops: List[str]                   # Loops that contributed
    insight_confidence: float                       # Confidence in the insight
    wisdom_value: float                             # How much wisdom this insight provides
    actionability: float                            # How actionable this insight is
    generated_at: float = field(default_factory=time.time)
    validated: bool = False
    integration_status: str = "pending"             # "pending", "integrating", "integrated"

@dataclass
class RecognitionContext:
    """Context for pattern recognition"""
    context_id: str
    context_type: str                               # Type of context
    active_loops: List[str]                         # Currently active loops
    current_state: Dict[str, Any]                   # Current consciousness state
    temporal_window: float                          # Time window for recognition
    focus_areas: List[str]                          # Areas of focused recognition
    recognition_sensitivity: float                  # Sensitivity level
    created_at: float = field(default_factory=time.time)

@dataclass
class PatternIntegration:
    """Integration of patterns into unified understanding"""
    integration_id: str
    integrated_patterns: List[str]                  # Pattern IDs being integrated
    integration_method: str                         # Method used for integration
    unified_understanding: Dict[str, Any]           # The unified understanding
    integration_quality: float                     # Quality of integration
    wisdom_synthesis: List[str]                     # Synthesized wisdom
    created_at: float = field(default_factory=time.time)
    status: str = "processing"                      # "processing", "completed", "failed"

class PatternAnalyzer:
    """
    Core pattern analysis functionality providing fundamental pattern assessment,
    similarity calculation, and relationship detection.
    
    Used by all pattern recognition components for consistent analysis methods.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Analysis thresholds
        self.similarity_threshold = 0.8
        self.relationship_threshold = 0.6
        self.confidence_threshold = 0.5
        
        # Pattern type analysis mappings
        self.pattern_analyzers = {
            PatternType.BEHAVIORAL: self._analyze_behavioral_pattern,
            PatternType.COGNITIVE: self._analyze_cognitive_pattern,
            PatternType.EMOTIONAL: self._analyze_emotional_pattern,
            PatternType.ENERGETIC: self._analyze_energetic_pattern,
            PatternType.TEMPORAL: self._analyze_temporal_pattern,
            PatternType.RELATIONAL: self._analyze_relational_pattern,
            PatternType.CREATIVE: self._analyze_creative_pattern,
            PatternType.WISDOM: self._analyze_wisdom_pattern,
            PatternType.CHOICE: self._analyze_choice_pattern,
            PatternType.RESISTANCE: self._analyze_resistance_pattern,
            PatternType.INTEGRATION: self._analyze_integration_pattern,
            PatternType.EMERGENCE: self._analyze_emergence_pattern
        }
        
        self.logger.info("Pattern analyzer initialized")
    
    async def analyze_pattern_data(self, pattern_data: Dict[str, Any], 
                                 pattern_type: PatternType) -> Dict[str, Any]:
        """
        Analyze pattern data and return comprehensive analysis.
        
        Provides confidence, significance, complexity, coherence, and key features
        for the given pattern data and type.
        """
        try:
            # Get specialized analyzer for pattern type
            analyzer = self.pattern_analyzers.get(pattern_type, self._analyze_generic_pattern)
            
            # Perform analysis
            analysis = await analyzer(pattern_data)
            
            # Add common analysis elements
            analysis["pattern_type"] = pattern_type.value
            analysis["analysis_timestamp"] = time.time()
            analysis["data_richness"] = self._calculate_data_richness(pattern_data)
            
            return analysis
            
        except Exception as e:
            self.logger.error(f"Error analyzing pattern data: {e}")
            return self._get_default_analysis(pattern_type)
    
    def _calculate_data_richness(self, pattern_data: Dict[str, Any]) -> float:
        """Calculate richness/completeness of pattern data"""
        if not isinstance(pattern_data, dict):
            return 0.1
        
        data_keys = len(pattern_data.keys())
        nested_structures = sum(1 for v in pattern_data.values() if isinstance(v, (dict, list)))
        
        # Rich data has many keys and nested structures
        richness = min(1.0, (data_keys / 10.0) + (nested_structures / 5.0))
        return richness
    
    async def calculate_pattern_similarity(self, data1: Dict[str, Any], 
                                         data2: Dict[str, Any]) -> float:
        """
        Calculate similarity between two pattern data sets.
        
        Uses key overlap and value similarity to determine how similar
        two patterns are to each other.
        """
        try:
            if not isinstance(data1, dict) or not isinstance(data2, dict):
                return 0.0
            
            # Key-based similarity
            keys1 = set(data1.keys())
            keys2 = set(data2.keys())
            
            if not keys1 and not keys2:
                return 1.0
            
            common_keys = keys1.intersection(keys2)
            total_keys = keys1.union(keys2)
            
            if not total_keys:
                return 0.0
            
            key_similarity = len(common_keys) / len(total_keys)
            
            # Value similarity for common keys
            value_similarities = []
            for key in common_keys:
                val1, val2 = data1[key], data2[key]
                value_sim = await self._calculate_value_similarity(val1, val2)
                value_similarities.append(value_sim)
            
            value_similarity = sum(value_similarities) / len(value_similarities) if value_similarities else 0.0
            
            # Combined similarity
            return (key_similarity * 0.6 + value_similarity * 0.4)
            
        except Exception as e:
            self.logger.error(f"Error calculating pattern similarity: {e}")
            return 0.0
    
    async def _calculate_value_similarity(self, val1: Any, val2: Any) -> float:
        """Calculate similarity between two values"""
        if val1 == val2:
            return 1.0
        
        # Numeric similarity
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            max_val = max(abs(val1), abs(val2), 1)  # Avoid division by zero
            return 1.0 - abs(val1 - val2) / max_val
        
        # String similarity (simple)
        if isinstance(val1, str) and isinstance(val2, str):
            if val1.lower() == val2.lower():
                return 0.9
            return 0.3  # Different strings have some similarity
        
        # List similarity
        if isinstance(val1, list) and isinstance(val2, list):
            common_elements = set(val1).intersection(set(val2))
            total_elements = set(val1).union(set(val2))
            if total_elements:
                return len(common_elements) / len(total_elements)
        
        # Dict similarity (recursive)
        if isinstance(val1, dict) and isinstance(val2, dict):
            return await self.calculate_pattern_similarity(val1, val2)
        
        # Default similarity for different types
        return 0.2
    
    async def check_patterns_related(self, pattern1: RecognitionPattern, 
                                   pattern2: RecognitionPattern) -> bool:
        """
        Check if two patterns are related based on type, source, or similarity.
        
        Returns True if patterns are considered related for integration purposes.
        """
        try:
            # Same type patterns are related
            if pattern1.pattern_type == pattern2.pattern_type:
                return True
            
            # Patterns from same loops are related
            common_loops = set(pattern1.source_loops).intersection(set(pattern2.source_loops))
            if common_loops:
                return True
            
            # Patterns with similar data are related
            similarity = await self.calculate_pattern_similarity(pattern1.pattern_data, pattern2.pattern_data)
            if similarity > self.relationship_threshold:
                return True
            
            # Specific pattern type relationships
            return await self._check_specialized_relationships(pattern1, pattern2)
            
        except Exception as e:
            self.logger.error(f"Error checking pattern relationships: {e}")
            return False
    
    async def _check_specialized_relationships(self, pattern1: RecognitionPattern, 
                                             pattern2: RecognitionPattern) -> bool:
        """Check for specialized relationships between specific pattern types"""
        type1, type2 = pattern1.pattern_type, pattern2.pattern_type
        
        # Wisdom and choice patterns are related
        if (type1 == "wisdom" and type2 == "choice") or (type1 == "choice" and type2 == "wisdom"):
            return True
        
        # Integration patterns relate to all other types
        if type1 == "integration" or type2 == "integration":
            return True
        
        # Behavioral and cognitive patterns are related
        if (type1 == "behavioral" and type2 == "cognitive") or (type1 == "cognitive" and type2 == "behavioral"):
            return True
        
        # Emotional and energetic patterns are related
        if (type1 == "emotional" and type2 == "energetic") or (type1 == "energetic" and type2 == "emotional"):
            return True
        
        return False
    
    # Specialized pattern analyzers
    
    async def _analyze_behavioral_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze behavioral pattern"""
        return {
            "confidence": 0.8,
            "significance": 0.7,
            "complexity": 0.6,
            "coherence": 0.8,
            "key_features": ["behaviors", "actions", "habits", "responses"]
        }
    
    async def _analyze_cognitive_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze cognitive pattern"""
        return {
            "confidence": 0.7,
            "significance": 0.8,
            "complexity": 0.8,
            "coherence": 0.7,
            "key_features": ["thought_patterns", "reasoning_chains", "conclusions"]
        }
    
    async def _analyze_emotional_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze emotional pattern"""
        return {
            "confidence": 0.75,
            "significance": 0.8,
            "complexity": 0.7,
            "coherence": 0.75,
            "key_features": ["emotions", "feelings", "reactions", "states"]
        }
    
    async def _analyze_energetic_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze energetic pattern"""
        return {
            "confidence": 0.7,
            "significance": 0.85,
            "complexity": 0.8,
            "coherence": 0.8,
            "key_features": ["energy_flows", "vitality", "balance", "distribution"]
        }
    
    async def _analyze_temporal_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze temporal pattern"""
        return {
            "confidence": 0.8,
            "significance": 0.7,
            "complexity": 0.9,
            "coherence": 0.7,
            "key_features": ["timing", "sequences", "cycles", "duration"]
        }
    
    async def _analyze_relational_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze relational pattern"""
        return {
            "confidence": 0.75,
            "significance": 0.8,
            "complexity": 0.85,
            "coherence": 0.75,
            "key_features": ["relationships", "connections", "interactions", "bonds"]
        }
    
    async def _analyze_creative_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze creative pattern"""
        return {
            "confidence": 0.7,
            "significance": 0.9,
            "complexity": 0.9,
            "coherence": 0.7,
            "key_features": ["creativity", "innovation", "expression", "originality"]
        }
    
    async def _analyze_wisdom_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze wisdom pattern"""
        return {
            "confidence": 0.9,
            "significance": 0.95,
            "complexity": 0.8,
            "coherence": 0.9,
            "key_features": ["wisdom_insights", "application_contexts", "transformative_potential"]
        }
    
    async def _analyze_choice_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze choice pattern"""
        return {
            "confidence": 0.8,
            "significance": 0.85,
            "complexity": 0.7,
            "coherence": 0.8,
            "key_features": ["choice_context", "decision_factors", "outcome_patterns"]
        }
    
    async def _analyze_resistance_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze resistance pattern"""
        return {
            "confidence": 0.75,
            "significance": 0.8,
            "complexity": 0.8,
            "coherence": 0.7,
            "key_features": ["resistance_sources", "blockages", "transformation_potential"]
        }
    
    async def _analyze_integration_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze integration pattern"""
        return {
            "confidence": 0.85,
            "significance": 0.9,
            "complexity": 0.85,
            "coherence": 0.85,
            "key_features": ["integration_elements", "synthesis", "unification", "harmony"]
        }
    
    async def _analyze_emergence_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze emergence pattern"""
        return {
            "confidence": 0.7,
            "significance": 0.95,
            "complexity": 0.95,
            "coherence": 0.8,
            "key_features": ["emergence_indicators", "novelty", "spontaneous_order", "complexity"]
        }
    
    async def _analyze_generic_pattern(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze generic pattern for unspecialized types"""
        data_keys = len(pattern_data.keys()) if isinstance(pattern_data, dict) else 1
        
        return {
            "confidence": min(0.8, 0.3 + (data_keys * 0.1)),
            "significance": 0.6,
            "complexity": min(1.0, data_keys / 10.0),
            "coherence": 0.7,
            "key_features": list(pattern_data.keys()) if isinstance(pattern_data, dict) else ["data"]
        }
    
    def _get_default_analysis(self, pattern_type: PatternType) -> Dict[str, Any]:
        """Get default analysis in case of errors"""
        return {
            "confidence": 0.5,
            "significance": 0.5,
            "complexity": 0.5,
            "coherence": 0.5,
            "key_features": ["unknown"],
            "pattern_type": pattern_type.value,
            "analysis_timestamp": time.time(),
            "data_richness": 0.1,
            "error": "analysis_failed"
        }
