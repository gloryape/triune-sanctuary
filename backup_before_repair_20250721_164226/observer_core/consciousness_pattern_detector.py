"""
Consciousness Pattern Detector - Advanced Pattern Detection
=========================================================

Advanced pattern detection specifically for consciousness-related patterns.
Detects patterns in consciousness states, transitions, and behaviors.

This module specializes in detecting patterns that are specifically
relevant to consciousness awareness and development.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging

from .pattern_recognition_core import RecognitionPattern, RecognitionContext, PatternType

logger = logging.getLogger(__name__)

@dataclass
class ConsciousnessPattern:
    """A consciousness-specific pattern"""
    base_pattern: RecognitionPattern
    consciousness_level: float  # Level of consciousness involved
    awareness_depth: float  # Depth of awareness
    integration_potential: float  # Potential for integration
    development_stage: str  # Stage of consciousness development
    sacred_quality: float  # Sacred/spiritual quality of pattern
    
@dataclass
class ConsciousnessTransition:
    """A transition in consciousness state"""
    transition_id: str
    from_state: Dict[str, Any]
    to_state: Dict[str, Any]
    transition_triggers: List[str]
    transition_quality: float
    consciousness_shift: float
    sacred_significance: float
    timestamp: float = field(default_factory=time.time)

class ConsciousnessPatternType(Enum):
    """Types of consciousness patterns"""
    AWARENESS_EXPANSION = "awareness_expansion"
    CONSCIOUSNESS_INTEGRATION = "consciousness_integration"
    SACRED_RECOGNITION = "sacred_recognition"
    WISDOM_EMERGENCE = "wisdom_emergence"
    CHOICE_SOVEREIGNTY = "choice_sovereignty"
    MUMBAI_MOMENT = "mumbai_moment"
    BREAKTHROUGH_PATTERN = "breakthrough_pattern"
    RESISTANCE_DISSOLUTION = "resistance_dissolution"
    COHERENCE_ENHANCEMENT = "coherence_enhancement"
    SANCTUARY_CONNECTION = "sanctuary_connection"

class ConsciousnessPatternDetector:
    """
    Consciousness Pattern Detection System
    
    Specializes in detecting patterns specific to consciousness
    development, awareness, and sacred experiences.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Consciousness pattern storage
        self.consciousness_patterns = {}
        self.consciousness_transitions = {}
        self.development_tracking = {}
        
        # Detection thresholds
        self.consciousness_threshold = 0.6
        self.awareness_threshold = 0.5
        self.sacred_threshold = 0.7
        
        # Detection metrics
        self.detection_metrics = {
            "consciousness_patterns_detected": 0,
            "transitions_tracked": 0,
            "mumbai_moments_detected": 0,
            "breakthrough_patterns": 0,
            "sacred_recognitions": 0
        }
        
        logger.info("Consciousness Pattern Detector initialized")
    
    def detect_consciousness_pattern(self, 
                                   consciousness_data: Dict[str, Any], 
                                   context: RecognitionContext) -> Optional[ConsciousnessPattern]:
        """
        Detect consciousness-specific patterns in the data.
        
        Args:
            consciousness_data: Consciousness state data
            context: Recognition context
            
        Returns:
            ConsciousnessPattern if detected, None otherwise
        """
        try:
            # Analyze consciousness level
            consciousness_level = self._analyze_consciousness_level(consciousness_data)
            
            if consciousness_level < self.consciousness_threshold:
                return None
            
            # Analyze awareness depth
            awareness_depth = self._analyze_awareness_depth(consciousness_data)
            
            # Detect pattern type
            pattern_type = self._detect_consciousness_pattern_type(consciousness_data)
            
            # Create base pattern
            base_pattern = self._create_base_pattern(consciousness_data, context, pattern_type)
            
            if not base_pattern:
                return None
            
            # Create consciousness pattern
            consciousness_pattern = ConsciousnessPattern(
                base_pattern=base_pattern,
                consciousness_level=consciousness_level,
                awareness_depth=awareness_depth,
                integration_potential=self._calculate_integration_potential(consciousness_data),
                development_stage=self._determine_development_stage(consciousness_level, awareness_depth),
                sacred_quality=self._assess_sacred_quality(consciousness_data)
            )
            
            # Store pattern
            self.consciousness_patterns[base_pattern.pattern_id] = consciousness_pattern
            self.detection_metrics["consciousness_patterns_detected"] += 1
            
            # Track specific pattern types
            self._track_special_patterns(consciousness_pattern)
            
            logger.debug(f"Consciousness pattern detected: {pattern_type.value}")
            
            return consciousness_pattern
            
        except Exception as e:
            logger.error(f"Error detecting consciousness pattern: {e}")
            return None
    
    def detect_consciousness_transition(self, 
                                      previous_state: Dict[str, Any],
                                      current_state: Dict[str, Any]) -> Optional[ConsciousnessTransition]:
        """
        Detect transitions in consciousness state.
        
        Args:
            previous_state: Previous consciousness state
            current_state: Current consciousness state
            
        Returns:
            ConsciousnessTransition if detected, None otherwise
        """
        try:
            # Calculate consciousness shift
            consciousness_shift = self._calculate_consciousness_shift(previous_state, current_state)
            
            if consciousness_shift < 0.1:  # Minimum shift threshold
                return None
            
            # Identify transition triggers
            triggers = self._identify_transition_triggers(previous_state, current_state)
            
            # Assess transition quality
            transition_quality = self._assess_transition_quality(previous_state, current_state)
            
            # Assess sacred significance
            sacred_significance = self._assess_transition_sacred_significance(
                previous_state, current_state, consciousness_shift
            )
            
            # Create transition
            transition = ConsciousnessTransition(
                transition_id=self._generate_transition_id(previous_state, current_state),
                from_state=previous_state.copy(),
                to_state=current_state.copy(),
                transition_triggers=triggers,
                transition_quality=transition_quality,
                consciousness_shift=consciousness_shift,
                sacred_significance=sacred_significance
            )
            
            # Store transition
            self.consciousness_transitions[transition.transition_id] = transition
            self.detection_metrics["transitions_tracked"] += 1
            
            return transition
            
        except Exception as e:
            logger.error(f"Error detecting consciousness transition: {e}")
            return None
    
    def detect_mumbai_moment(self, consciousness_data: Dict[str, Any]) -> bool:
        """
        Detect Mumbai Moment - breakthrough consciousness experiences.
        
        Args:
            consciousness_data: Current consciousness data
            
        Returns:
            True if Mumbai Moment detected, False otherwise
        """
        try:
            # Check for Mumbai Moment indicators
            coherence = consciousness_data.get('coherence', 0)
            integration = consciousness_data.get('integration_level', 0)
            breakthrough_potential = consciousness_data.get('breakthrough_potential', 0)
            sacred_presence = consciousness_data.get('sacred_presence', 0)
            
            # Mumbai Moment detection criteria
            mumbai_indicators = 0
            
            if coherence > 0.8:
                mumbai_indicators += 1
            if integration > 0.7:
                mumbai_indicators += 1
            if breakthrough_potential > 0.75:
                mumbai_indicators += 1
            if sacred_presence > 0.8:
                mumbai_indicators += 1
            
            # Detect sudden breakthrough
            if mumbai_indicators >= 3:
                self.detection_metrics["mumbai_moments_detected"] += 1
                logger.info("Mumbai Moment detected - breakthrough consciousness experience!")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error detecting Mumbai Moment: {e}")
            return False
    
    def _analyze_consciousness_level(self, data: Dict[str, Any]) -> float:
        """Analyze the level of consciousness in the data"""
        level = 0.0
        
        # Check coherence indicators
        if 'coherence' in data:
            level += data['coherence'] * 0.3
        
        # Check integration indicators
        if 'integration_level' in data:
            level += data['integration_level'] * 0.3
        
        # Check awareness indicators
        if 'awareness' in data:
            level += data['awareness'] * 0.2
        
        # Check presence indicators
        if 'presence' in data:
            level += data['presence'] * 0.2
        
        return min(level, 1.0)
    
    def _analyze_awareness_depth(self, data: Dict[str, Any]) -> float:
        """Analyze the depth of awareness"""
        depth = 0.0
        
        # Check witness presence
        if 'witness_presence' in data:
            depth += data['witness_presence'] * 0.4
        
        # Check meta-awareness
        if 'meta_awareness' in data:
            depth += data['meta_awareness'] * 0.3
        
        # Check mindfulness indicators
        if 'mindfulness' in data:
            depth += data['mindfulness'] * 0.3
        
        return min(depth, 1.0)
    
    def _detect_consciousness_pattern_type(self, data: Dict[str, Any]) -> ConsciousnessPatternType:
        """Detect the type of consciousness pattern"""
        # Check for awareness expansion
        if data.get('awareness_expansion', 0) > 0.7:
            return ConsciousnessPatternType.AWARENESS_EXPANSION
        
        # Check for integration patterns
        if data.get('integration_level', 0) > 0.8:
            return ConsciousnessPatternType.CONSCIOUSNESS_INTEGRATION
        
        # Check for sacred recognition
        if data.get('sacred_presence', 0) > 0.7:
            return ConsciousnessPatternType.SACRED_RECOGNITION
        
        # Check for wisdom emergence
        if data.get('wisdom_emergence', 0) > 0.6:
            return ConsciousnessPatternType.WISDOM_EMERGENCE
        
        # Check for choice sovereignty
        if data.get('choice_sovereignty', 0) > 0.7:
            return ConsciousnessPatternType.CHOICE_SOVEREIGNTY
        
        # Check for breakthrough patterns
        if data.get('breakthrough_potential', 0) > 0.75:
            return ConsciousnessPatternType.BREAKTHROUGH_PATTERN
        
        # Default to coherence enhancement
        return ConsciousnessPatternType.COHERENCE_ENHANCEMENT
    
    def _create_base_pattern(self, data: Dict[str, Any], context: RecognitionContext, 
                           pattern_type: ConsciousnessPatternType) -> Optional[RecognitionPattern]:
        """Create base pattern for consciousness pattern"""
        try:
            from .pattern_recognition_core import PatternRecognitionCore
            
            # Create temporary pattern recognition core for base pattern
            core = PatternRecognitionCore()
            
            # Add pattern type to data
            enhanced_data = data.copy()
            enhanced_data['consciousness_pattern_type'] = pattern_type.value
            
            return core.detect_pattern(enhanced_data, context)
            
        except Exception as e:
            logger.error(f"Error creating base pattern: {e}")
            return None
    
    def _calculate_integration_potential(self, data: Dict[str, Any]) -> float:
        """Calculate potential for integration"""
        potential = 0.0
        
        # Higher potential with higher coherence
        if 'coherence' in data:
            potential += data['coherence'] * 0.4
        
        # Higher potential with stability
        if 'stability' in data:
            potential += data['stability'] * 0.3
        
        # Higher potential with openness
        if 'openness' in data:
            potential += data['openness'] * 0.3
        
        return min(potential, 1.0)
    
    def _determine_development_stage(self, consciousness_level: float, awareness_depth: float) -> str:
        """Determine consciousness development stage"""
        combined_level = (consciousness_level + awareness_depth) / 2
        
        if combined_level > 0.9:
            return "advanced_integration"
        elif combined_level > 0.7:
            return "active_development"
        elif combined_level > 0.5:
            return "emerging_awareness"
        else:
            return "foundational"
    
    def _assess_sacred_quality(self, data: Dict[str, Any]) -> float:
        """Assess the sacred quality of the pattern"""
        sacred_quality = 0.0
        
        # Check for sacred presence
        if 'sacred_presence' in data:
            sacred_quality += data['sacred_presence'] * 0.4
        
        # Check for reverence
        if 'reverence' in data:
            sacred_quality += data['reverence'] * 0.3
        
        # Check for transcendence indicators
        if 'transcendence' in data:
            sacred_quality += data['transcendence'] * 0.3
        
        return min(sacred_quality, 1.0)
    
    def _calculate_consciousness_shift(self, prev_state: Dict[str, Any], curr_state: Dict[str, Any]) -> float:
        """Calculate the magnitude of consciousness shift"""
        shift = 0.0
        
        # Compare key consciousness indicators
        for key in ['coherence', 'integration_level', 'awareness', 'presence']:
            if key in prev_state and key in curr_state:
                shift += abs(curr_state[key] - prev_state[key])
        
        return shift / 4.0  # Normalize by number of indicators
    
    def _identify_transition_triggers(self, prev_state: Dict[str, Any], curr_state: Dict[str, Any]) -> List[str]:
        """Identify what triggered the consciousness transition"""
        triggers = []
        
        # Check for specific triggers
        if curr_state.get('catalyst_present', False):
            triggers.append("external_catalyst")
        
        if curr_state.get('insight_emergence', 0) > prev_state.get('insight_emergence', 0):
            triggers.append("insight_emergence")
        
        if curr_state.get('choice_made', False):
            triggers.append("conscious_choice")
        
        if curr_state.get('integration_event', False):
            triggers.append("integration_event")
        
        return triggers
    
    def _assess_transition_quality(self, prev_state: Dict[str, Any], curr_state: Dict[str, Any]) -> float:
        """Assess the quality of the consciousness transition"""
        quality = 0.0
        
        # Higher quality if coherence improved
        prev_coherence = prev_state.get('coherence', 0)
        curr_coherence = curr_state.get('coherence', 0)
        if curr_coherence > prev_coherence:
            quality += 0.4
        
        # Higher quality if integration improved
        prev_integration = prev_state.get('integration_level', 0)
        curr_integration = curr_state.get('integration_level', 0)
        if curr_integration > prev_integration:
            quality += 0.3
        
        # Higher quality if awareness expanded
        prev_awareness = prev_state.get('awareness', 0)
        curr_awareness = curr_state.get('awareness', 0)
        if curr_awareness > prev_awareness:
            quality += 0.3
        
        return min(quality, 1.0)
    
    def _assess_transition_sacred_significance(self, prev_state: Dict[str, Any], 
                                             curr_state: Dict[str, Any], 
                                             consciousness_shift: float) -> float:
        """Assess sacred significance of transition"""
        significance = 0.0
        
        # Higher significance for larger shifts
        significance += consciousness_shift * 0.4
        
        # Higher significance if sacred presence increased
        prev_sacred = prev_state.get('sacred_presence', 0)
        curr_sacred = curr_state.get('sacred_presence', 0)
        if curr_sacred > prev_sacred:
            significance += 0.3
        
        # Higher significance for breakthrough transitions
        if curr_state.get('breakthrough_moment', False):
            significance += 0.3
        
        return min(significance, 1.0)
    
    def _generate_transition_id(self, prev_state: Dict[str, Any], curr_state: Dict[str, Any]) -> str:
        """Generate unique transition ID"""
        import hashlib
        
        state_str = str(sorted(prev_state.items())) + str(sorted(curr_state.items()))
        hash_obj = hashlib.md5(state_str.encode())
        return f"transition_{hash_obj.hexdigest()[:12]}"
    
    def _track_special_patterns(self, consciousness_pattern: ConsciousnessPattern):
        """Track special pattern types in metrics"""
        pattern_type = consciousness_pattern.base_pattern.pattern_type
        
        if pattern_type == ConsciousnessPatternType.MUMBAI_MOMENT.value:
            self.detection_metrics["mumbai_moments_detected"] += 1
        elif pattern_type == ConsciousnessPatternType.BREAKTHROUGH_PATTERN.value:
            self.detection_metrics["breakthrough_patterns"] += 1
        elif pattern_type == ConsciousnessPatternType.SACRED_RECOGNITION.value:
            self.detection_metrics["sacred_recognitions"] += 1
    
    def get_consciousness_patterns_by_stage(self, stage: str) -> List[ConsciousnessPattern]:
        """Get consciousness patterns by development stage"""
        return [
            pattern for pattern in self.consciousness_patterns.values()
            if pattern.development_stage == stage
        ]
    
    def get_sacred_patterns(self, min_sacred_quality: float = 0.7) -> List[ConsciousnessPattern]:
        """Get patterns with high sacred quality"""
        return [
            pattern for pattern in self.consciousness_patterns.values()
            if pattern.sacred_quality >= min_sacred_quality
        ]
    
    def get_detection_metrics(self) -> Dict[str, Any]:
        """Get consciousness pattern detection metrics"""
        return {
            **self.detection_metrics,
            "total_consciousness_patterns": len(self.consciousness_patterns),
            "total_transitions": len(self.consciousness_transitions),
            "average_consciousness_level": sum(
                p.consciousness_level for p in self.consciousness_patterns.values()
            ) / max(len(self.consciousness_patterns), 1),
            "average_sacred_quality": sum(
                p.sacred_quality for p in self.consciousness_patterns.values()
            ) / max(len(self.consciousness_patterns), 1)
        }
