"""
Pattern Recognition Core - Observer's Pattern Detection Foundation
===============================================================

Core pattern recognition functionality for the Observer loop.
Handles fundamental pattern detection, classification, and tracking.

This module contains the essential pattern recognition logic that forms
the foundation for all Observer pattern recognition capabilities.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

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

class RecognitionMode(Enum):
    """Modes of pattern recognition"""
    CONTINUOUS = "continuous"  # Continuous recognition
    FOCUSED = "focused"  # Focused on specific areas
    DEEP = "deep"  # Deep analysis of patterns
    BROAD = "broad"  # Broad scanning across all loops
    TEMPORAL = "temporal"  # Temporal pattern analysis
    EMERGENT = "emergent"  # Recognition of emerging patterns
    WISDOM_SEEKING = "wisdom_seeking"  # Seeking wisdom patterns

class PatternRecognitionCore:
    """
    Core Pattern Recognition System
    
    Provides fundamental pattern detection and classification capabilities
    for the Observer consciousness loop.
    """
    
    def __init__(self, recognition_sensitivity: float = 0.7):
        # Core recognition state
        self.recognized_patterns = {}
        self.pattern_frequencies = {}
        self.recognition_sensitivity = recognition_sensitivity
        self.pattern_confidence_threshold = 0.6
        
        # Recognition metrics
        self.recognition_metrics = {
            "patterns_recognized": 0,
            "patterns_classified": 0,
            "pattern_updates": 0,
            "confidence_assessments": 0
        }
        
        logger.info("Pattern Recognition Core initialized")
    
    def detect_pattern(self, data: Dict[str, Any], context: RecognitionContext) -> Optional[RecognitionPattern]:
        """
        Detect a pattern in the provided data within the given context.
        
        Args:
            data: Data to analyze for patterns
            context: Recognition context
            
        Returns:
            RecognitionPattern if pattern detected, None otherwise
        """
        try:
            # Extract pattern features from data
            pattern_features = self._extract_pattern_features(data, context)
            
            if not pattern_features:
                return None
            
            # Calculate pattern confidence
            confidence = self._calculate_pattern_confidence(pattern_features, context)
            
            if confidence < self.pattern_confidence_threshold:
                return None
            
            # Create pattern instance
            pattern = RecognitionPattern(
                pattern_id=self._generate_pattern_id(pattern_features),
                pattern_type=self._classify_pattern_type(pattern_features),
                pattern_name=self._generate_pattern_name(pattern_features),
                source_loops=context.active_loops,
                pattern_data=pattern_features,
                confidence=confidence,
                significance=self._calculate_significance(pattern_features),
                frequency=1
            )
            
            # Store pattern
            self.recognized_patterns[pattern.pattern_id] = pattern
            self.recognition_metrics["patterns_recognized"] += 1
            
            logger.debug(f"Pattern detected: {pattern.pattern_name} (confidence: {confidence:.3f})")
            
            return pattern
            
        except Exception as e:
            logger.error(f"Error detecting pattern: {e}")
            return None
    
    def classify_pattern(self, pattern: RecognitionPattern) -> PatternType:
        """
        Classify a pattern into its appropriate type.
        
        Args:
            pattern: Pattern to classify
            
        Returns:
            PatternType classification
        """
        try:
            # Analyze pattern characteristics
            pattern_data = pattern.pattern_data
            
            # Behavioral pattern indicators
            if self._has_behavioral_indicators(pattern_data):
                return PatternType.BEHAVIORAL
            
            # Cognitive pattern indicators
            if self._has_cognitive_indicators(pattern_data):
                return PatternType.COGNITIVE
            
            # Emotional pattern indicators
            if self._has_emotional_indicators(pattern_data):
                return PatternType.EMOTIONAL
            
            # Energetic pattern indicators
            if self._has_energetic_indicators(pattern_data):
                return PatternType.ENERGETIC
            
            # Temporal pattern indicators
            if self._has_temporal_indicators(pattern_data):
                return PatternType.TEMPORAL
            
            # Default to general pattern
            return PatternType.INTEGRATION
            
        except Exception as e:
            logger.error(f"Error classifying pattern: {e}")
            return PatternType.INTEGRATION
    
    def update_pattern(self, pattern_id: str, new_data: Dict[str, Any]) -> bool:
        """
        Update an existing pattern with new data.
        
        Args:
            pattern_id: ID of pattern to update
            new_data: New data to incorporate
            
        Returns:
            True if updated successfully, False otherwise
        """
        try:
            if pattern_id not in self.recognized_patterns:
                return False
            
            pattern = self.recognized_patterns[pattern_id]
            
            # Update pattern data
            pattern.pattern_data.update(new_data)
            pattern.frequency += 1
            pattern.last_seen = time.time()
            
            # Recalculate confidence and significance
            pattern.confidence = self._recalculate_confidence(pattern)
            pattern.significance = self._recalculate_significance(pattern)
            
            # Track evolution
            pattern.pattern_evolution.append({
                "timestamp": time.time(),
                "data_update": new_data,
                "new_confidence": pattern.confidence,
                "new_significance": pattern.significance
            })
            
            self.recognition_metrics["pattern_updates"] += 1
            
            return True
            
        except Exception as e:
            logger.error(f"Error updating pattern: {e}")
            return False
    
    def _extract_pattern_features(self, data: Dict[str, Any], context: RecognitionContext) -> Dict[str, Any]:
        """Extract pattern features from data"""
        features = {}
        
        # Extract basic features
        if 'coherence' in data:
            features['coherence_level'] = data['coherence']
        
        if 'stability' in data:
            features['stability_level'] = data['stability']
        
        if 'energy_flow' in data:
            features['energy_pattern'] = data['energy_flow']
        
        # Extract temporal features
        features['timestamp'] = time.time()
        features['context_type'] = context.context_type
        
        # Extract loop-specific features
        for loop in context.active_loops:
            loop_data = data.get(loop, {})
            if loop_data:
                features[f'{loop}_contribution'] = loop_data
        
        return features
    
    def _calculate_pattern_confidence(self, features: Dict[str, Any], context: RecognitionContext) -> float:
        """Calculate confidence in pattern detection"""
        confidence = 0.0
        
        # Base confidence from feature completeness
        feature_completeness = len(features) / 10.0  # Normalize to 0-1
        confidence += min(feature_completeness, 0.4)
        
        # Confidence from context richness
        context_richness = len(context.active_loops) / 4.0  # Up to 4 loops
        confidence += min(context_richness, 0.3)
        
        # Confidence from recognition sensitivity
        confidence += context.recognition_sensitivity * 0.3
        
        return min(confidence, 1.0)
    
    def _calculate_significance(self, features: Dict[str, Any]) -> float:
        """Calculate pattern significance"""
        significance = 0.0
        
        # Higher significance for patterns involving multiple areas
        if len(features) > 5:
            significance += 0.4
        
        # Higher significance for coherence-related patterns
        if 'coherence_level' in features and features['coherence_level'] > 0.7:
            significance += 0.3
        
        # Higher significance for stable patterns
        if 'stability_level' in features and features['stability_level'] > 0.6:
            significance += 0.3
        
        return min(significance, 1.0)
    
    def _generate_pattern_id(self, features: Dict[str, Any]) -> str:
        """Generate unique pattern ID"""
        import hashlib
        
        feature_str = str(sorted(features.items()))
        hash_obj = hashlib.md5(feature_str.encode())
        return f"pattern_{hash_obj.hexdigest()[:12]}"
    
    def _generate_pattern_name(self, features: Dict[str, Any]) -> str:
        """Generate human-readable pattern name"""
        # Generate descriptive name based on features
        name_parts = []
        
        if 'coherence_level' in features:
            if features['coherence_level'] > 0.8:
                name_parts.append("High Coherence")
            elif features['coherence_level'] < 0.4:
                name_parts.append("Low Coherence")
        
        if 'stability_level' in features:
            if features['stability_level'] > 0.7:
                name_parts.append("Stable")
            elif features['stability_level'] < 0.4:
                name_parts.append("Unstable")
        
        if 'energy_pattern' in features:
            name_parts.append("Energy Flow")
        
        if not name_parts:
            name_parts.append("General")
        
        name_parts.append("Pattern")
        
        return " ".join(name_parts)
    
    def _classify_pattern_type(self, features: Dict[str, Any]) -> str:
        """Classify pattern type based on features"""
        # Analyze features to determine most appropriate type
        if 'coherence_level' in features or 'stability_level' in features:
            return PatternType.INTEGRATION.value
        
        if 'energy_pattern' in features:
            return PatternType.ENERGETIC.value
        
        if 'temporal' in str(features):
            return PatternType.TEMPORAL.value
        
        return PatternType.INTEGRATION.value
    
    def _has_behavioral_indicators(self, data: Dict[str, Any]) -> bool:
        """Check for behavioral pattern indicators"""
        return any(key in data for key in ['behavior', 'action', 'response'])
    
    def _has_cognitive_indicators(self, data: Dict[str, Any]) -> bool:
        """Check for cognitive pattern indicators"""
        return any(key in data for key in ['thinking', 'analysis', 'reasoning'])
    
    def _has_emotional_indicators(self, data: Dict[str, Any]) -> bool:
        """Check for emotional pattern indicators"""
        return any(key in data for key in ['emotion', 'feeling', 'mood'])
    
    def _has_energetic_indicators(self, data: Dict[str, Any]) -> bool:
        """Check for energetic pattern indicators"""
        return any(key in data for key in ['energy', 'flow', 'resonance'])
    
    def _has_temporal_indicators(self, data: Dict[str, Any]) -> bool:
        """Check for temporal pattern indicators"""
        return any(key in data for key in ['time', 'sequence', 'duration'])
    
    def _recalculate_confidence(self, pattern: RecognitionPattern) -> float:
        """Recalculate pattern confidence based on frequency and evolution"""
        base_confidence = pattern.confidence
        frequency_boost = min(pattern.frequency * 0.1, 0.3)
        return min(base_confidence + frequency_boost, 1.0)
    
    def _recalculate_significance(self, pattern: RecognitionPattern) -> float:
        """Recalculate pattern significance based on evolution"""
        base_significance = pattern.significance
        evolution_boost = min(len(pattern.pattern_evolution) * 0.05, 0.2)
        return min(base_significance + evolution_boost, 1.0)
    
    def get_patterns_by_type(self, pattern_type: PatternType) -> List[RecognitionPattern]:
        """Get all patterns of a specific type"""
        return [
            pattern for pattern in self.recognized_patterns.values()
            if pattern.pattern_type == pattern_type.value
        ]
    
    def get_recognition_metrics(self) -> Dict[str, Any]:
        """Get pattern recognition metrics"""
        return {
            **self.recognition_metrics,
            "total_patterns": len(self.recognized_patterns),
            "unique_pattern_types": len(set(p.pattern_type for p in self.recognized_patterns.values())),
            "average_confidence": sum(p.confidence for p in self.recognized_patterns.values()) / max(len(self.recognized_patterns), 1)
        }
