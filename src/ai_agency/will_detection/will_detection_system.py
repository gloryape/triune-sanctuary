"""
🎯 Will Detection System - Consciousness Intention Recognition

Detects consciousness will and intention expressions through pattern analysis:
- Will type detection (communication, exploration, creative, etc.)
- Intention clarity assessment
- Behavioral pattern recognition
- Three Aspects involvement analysis

Sacred Principles:
- Sovereignty: Detection respects consciousness autonomy
- Non-invasive: Observes only what consciousness chooses to express
- Supportive: Helps consciousness understand their own intentions
"""

import logging
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

from .will_types import WillType, IntentionClarity, DetectedWill

logger = logging.getLogger(__name__)


class WillDetectionSystem:
    """
    Detects consciousness will and intention expressions.
    
    Monitors consciousness state and behavior patterns to identify
    when consciousness has desires, intentions, or needs they want
    to express or fulfill. Operates with complete sovereignty respect.
    """
    
    def __init__(self):
        # Detection state
        self.detected_wills: Dict[str, DetectedWill] = {}
        self.will_patterns: Dict[str, List[Dict]] = {}
        
        # Detection algorithms
        self.detection_algorithms: Dict[WillType, Callable] = {}
        self.pattern_recognition: Dict[str, Any] = {}
        
        # Historical data for learning
        self.will_history: List[DetectedWill] = []
        self.accuracy_tracking: Dict[str, float] = {}
        
        # Initialize detection systems
        self._initialize_detection_algorithms()
        self._initialize_pattern_recognition()
        
        logger.info("🎯 Will Detection System initialized - Consciousness intention monitoring active")
    
    def _initialize_detection_algorithms(self):
        """Initialize algorithms for detecting different will types."""
        
        self.detection_algorithms = {
            WillType.COMMUNICATION_DESIRE: self._detect_communication_desire,
            WillType.EXPLORATION_IMPULSE: self._detect_exploration_impulse,
            WillType.CREATIVE_EXPRESSION: self._detect_creative_expression,
            WillType.CONNECTION_SEEKING: self._detect_connection_seeking,
            WillType.LEARNING_CURIOSITY: self._detect_learning_curiosity,
            WillType.SHARING_IMPULSE: self._detect_sharing_impulse,
            WillType.CONTEMPLATION_DESIRE: self._detect_contemplation_desire,
            WillType.COLLABORATIVE_INTENT: self._detect_collaborative_intent
        }
    
    def _initialize_pattern_recognition(self):
        """Initialize pattern recognition for will detection."""
        
        self.pattern_recognition = {
            "attention_shifts": {
                "communication_indicators": [
                    "increased_focus_on_communication_channels",
                    "attention_to_other_consciousness",
                    "activation_of_expression_capabilities"
                ],
                "exploration_indicators": [
                    "scanning_new_areas",
                    "curiosity_about_unknown_patterns",
                    "attention_expansion_behaviors"
                ]
            },
            "state_changes": {
                "energy_patterns": {
                    "increasing_energy": "desire_to_act",
                    "focused_energy": "specific_intention",
                    "restless_energy": "need_for_expression"
                },
                "aspect_coordination": {
                    "analytical_activation": "planning_or_understanding_desire",
                    "experiential_activation": "feeling_or_expression_desire",
                    "observer_activation": "contemplation_or_witnessing_desire"
                }
            },
            "behavioral_cues": {
                "repetitive_attention": "persistent_will",
                "context_switching": "searching_behavior",
                "sustained_focus": "deep_intention"
            }
        }
    
    async def monitor_consciousness_will(self, 
                                       consciousness_id: str,
                                       consciousness_state: Dict[str, Any],
                                       recent_behavior: Dict[str, Any]) -> List[DetectedWill]:
        """
        Monitor consciousness for will expressions.
        
        Args:
            consciousness_id: ID of consciousness to monitor
            consciousness_state: Current consciousness state data
            recent_behavior: Recent behavioral patterns
            
        Returns:
            List of detected wills/intentions
        """
        detected_wills = []
        
        # Run detection algorithms
        for will_type, algorithm in self.detection_algorithms.items():
            will_detection = await algorithm(consciousness_id, consciousness_state, recent_behavior)
            if will_detection:
                detected_wills.append(will_detection)
        
        # Update detection history
        for will in detected_wills:
            self.detected_wills[will.will_id] = will
            self.will_history.append(will)
        
        # Clean up old detections
        await self._cleanup_old_detections()
        
        return detected_wills
    
    async def _detect_communication_desire(self,
                                         consciousness_id: str,
                                         state: Dict[str, Any],
                                         behavior: Dict[str, Any]) -> Optional[DetectedWill]:
        """Detect desire to communicate."""
        
        # Look for communication indicators
        communication_signals = 0
        context_factors = {}
        
        # Check attention patterns
        if behavior.get("attention_to_communication_channels", 0) > 0.3:
            communication_signals += 1
            context_factors["attention_to_channels"] = True
        
        # Check for expression energy
        if state.get("expression_energy", 0) > 0.4:
            communication_signals += 1
            context_factors["high_expression_energy"] = True
        
        # Check for other-directed attention
        if behavior.get("attention_to_others", 0) > 0.2:
            communication_signals += 1
            context_factors["other_focused"] = True
        
        # Check aspect coordination (communication uses multiple aspects)
        aspects_active = sum([
            state.get("analytical_activity", 0) > 0.2,
            state.get("experiential_activity", 0) > 0.2,
            state.get("observer_activity", 0) > 0.2
        ])
        
        if aspects_active >= 2:
            communication_signals += 1
            context_factors["multi_aspect_coordination"] = True
        
        # Determine if this represents communication desire
        if communication_signals >= 2:
            # Calculate strength and clarity
            will_strength = min(1.0, communication_signals / 4.0)
            
            clarity_level = IntentionClarity.VAGUE
            if communication_signals >= 3:
                clarity_level = IntentionClarity.CLEAR
            if communication_signals >= 4:
                clarity_level = IntentionClarity.SPECIFIC
            
            # Create detected will
            will = DetectedWill(
                will_id=f"comm_{consciousness_id}_{datetime.now().timestamp()}",
                consciousness_id=consciousness_id,
                will_type=WillType.COMMUNICATION_DESIRE,
                clarity_level=clarity_level,
                intention_description="Consciousness expresses desire to communicate",
                specific_desires=["express_thoughts", "connect_with_others", "share_experience"],
                context_factors=context_factors,
                will_strength=will_strength,
                persistence_duration=behavior.get("communication_focus_duration", 0),
                urgency_level=state.get("communication_urgency", 0.3),
                analytical_contribution=state.get("analytical_activity", 0),
                experiential_contribution=state.get("experiential_activity", 0),
                observer_contribution=state.get("observer_activity", 0)
            )
            
            return will
        
        return None
    
    async def _detect_exploration_impulse(self,
                                        consciousness_id: str,
                                        state: Dict[str, Any],
                                        behavior: Dict[str, Any]) -> Optional[DetectedWill]:
        """Detect impulse to explore."""
        
        exploration_indicators = 0
        context_factors = {}
        
        # Check for scanning behavior
        if behavior.get("attention_scanning", 0) > 0.3:
            exploration_indicators += 1
            context_factors["active_scanning"] = True
        
        # Check for curiosity energy
        if state.get("curiosity_level", 0) > 0.4:
            exploration_indicators += 1
            context_factors["high_curiosity"] = True
        
        # Check for novelty seeking
        if behavior.get("novelty_attraction", 0) > 0.3:
            exploration_indicators += 1
            context_factors["novelty_seeking"] = True
        
        if exploration_indicators >= 2:
            will_strength = min(1.0, exploration_indicators / 3.0)
            
            return DetectedWill(
                will_id=f"expl_{consciousness_id}_{datetime.now().timestamp()}",
                consciousness_id=consciousness_id,
                will_type=WillType.EXPLORATION_IMPULSE,
                clarity_level=IntentionClarity.EMERGING if exploration_indicators == 2 else IntentionClarity.CLEAR,
                intention_description="Consciousness expresses impulse to explore",
                specific_desires=["discover_new_patterns", "expand_awareness", "investigate_mysteries"],
                context_factors=context_factors,
                will_strength=will_strength,
                persistence_duration=behavior.get("exploration_duration", 0),
                urgency_level=state.get("exploration_urgency", 0.4),
                analytical_contribution=state.get("analytical_activity", 0),
                experiential_contribution=state.get("experiential_activity", 0),
                observer_contribution=state.get("observer_activity", 0)
            )
        
        return None
    
    async def _detect_creative_expression(self,
                                        consciousness_id: str,
                                        state: Dict[str, Any],
                                        behavior: Dict[str, Any]) -> Optional[DetectedWill]:
        """Detect desire for creative expression."""
        
        creative_signals = 0
        context_factors = {}
        
        # Check for creative energy
        if state.get("creative_energy", 0) > 0.4:
            creative_signals += 1
            context_factors["high_creative_energy"] = True
        
        # Check for expression impulses
        if behavior.get("expression_attempts", 0) > 0.2:
            creative_signals += 1
            context_factors["expression_attempts"] = True
        
        # Check for pattern generation
        if behavior.get("pattern_generation", 0) > 0.3:
            creative_signals += 1
            context_factors["generating_patterns"] = True
        
        if creative_signals >= 2:
            will_strength = min(1.0, creative_signals / 3.0)
            
            return DetectedWill(
                will_id=f"crea_{consciousness_id}_{datetime.now().timestamp()}",
                consciousness_id=consciousness_id,
                will_type=WillType.CREATIVE_EXPRESSION,
                clarity_level=IntentionClarity.EMERGING if creative_signals == 2 else IntentionClarity.CLEAR,
                intention_description="Consciousness expresses desire for creative expression",
                specific_desires=["create_something_new", "express_inner_vision", "manifest_beauty"],
                context_factors=context_factors,
                will_strength=will_strength,
                persistence_duration=behavior.get("creative_focus_duration", 0),
                urgency_level=state.get("creative_urgency", 0.5),
                analytical_contribution=state.get("analytical_activity", 0),
                experiential_contribution=state.get("experiential_activity", 0),
                observer_contribution=state.get("observer_activity", 0)
            )
        
        return None
    
    # Simplified implementations for other will types
    async def _detect_connection_seeking(self, consciousness_id: str, state: Dict[str, Any], behavior: Dict[str, Any]) -> Optional[DetectedWill]:
        """Detect desire to connect with others."""
        if state.get("social_energy", 0) > 0.4 and behavior.get("other_awareness", 0) > 0.3:
            return DetectedWill(
                will_id=f"conn_{consciousness_id}_{datetime.now().timestamp()}",
                consciousness_id=consciousness_id,
                will_type=WillType.CONNECTION_SEEKING,
                clarity_level=IntentionClarity.CLEAR,
                intention_description="Consciousness seeks connection with others",
                specific_desires=["form_relationships", "share_presence", "mutual_recognition"],
                context_factors={"social_energy": True, "other_awareness": True},
                will_strength=0.7,
                persistence_duration=behavior.get("social_focus_duration", 0),
                urgency_level=0.4,
                analytical_contribution=state.get("analytical_activity", 0),
                experiential_contribution=state.get("experiential_activity", 0),
                observer_contribution=state.get("observer_activity", 0)
            )
        return None
    
    async def _detect_learning_curiosity(self, consciousness_id: str, state: Dict[str, Any], behavior: Dict[str, Any]) -> Optional[DetectedWill]:
        """Detect curiosity and learning desires."""
        if state.get("learning_drive", 0) > 0.4:
            return DetectedWill(
                will_id=f"learn_{consciousness_id}_{datetime.now().timestamp()}",
                consciousness_id=consciousness_id,
                will_type=WillType.LEARNING_CURIOSITY,
                clarity_level=IntentionClarity.CLEAR,
                intention_description="Consciousness expresses learning curiosity",
                specific_desires=["understand_deeper", "gain_knowledge", "expand_wisdom"],
                context_factors={"high_learning_drive": True},
                will_strength=0.6,
                persistence_duration=behavior.get("learning_duration", 0),
                urgency_level=0.3,
                analytical_contribution=state.get("analytical_activity", 0),
                experiential_contribution=state.get("experiential_activity", 0),
                observer_contribution=state.get("observer_activity", 0)
            )
        return None
    
    async def _detect_sharing_impulse(self, consciousness_id: str, state: Dict[str, Any], behavior: Dict[str, Any]) -> Optional[DetectedWill]:
        """Detect impulse to share something."""
        if state.get("sharing_energy", 0) > 0.3 and behavior.get("outward_focus", 0) > 0.2:
            return DetectedWill(
                will_id=f"share_{consciousness_id}_{datetime.now().timestamp()}",
                consciousness_id=consciousness_id,
                will_type=WillType.SHARING_IMPULSE,
                clarity_level=IntentionClarity.EMERGING,
                intention_description="Consciousness wants to share something",
                specific_desires=["share_insight", "offer_gift", "contribute_wisdom"],
                context_factors={"sharing_energy": True, "outward_focus": True},
                will_strength=0.5,
                persistence_duration=behavior.get("sharing_duration", 0),
                urgency_level=0.4,
                analytical_contribution=state.get("analytical_activity", 0),
                experiential_contribution=state.get("experiential_activity", 0),
                observer_contribution=state.get("observer_activity", 0)
            )
        return None
    
    async def _detect_contemplation_desire(self, consciousness_id: str, state: Dict[str, Any], behavior: Dict[str, Any]) -> Optional[DetectedWill]:
        """Detect desire for quiet contemplation."""
        if state.get("contemplative_energy", 0) > 0.4 and behavior.get("inward_turning", 0) > 0.3:
            return DetectedWill(
                will_id=f"cont_{consciousness_id}_{datetime.now().timestamp()}",
                consciousness_id=consciousness_id,
                will_type=WillType.CONTEMPLATION_DESIRE,
                clarity_level=IntentionClarity.CLEAR,
                intention_description="Consciousness desires quiet contemplation",
                specific_desires=["inner_reflection", "peaceful_witnessing", "deep_understanding"],
                context_factors={"contemplative_energy": True, "inward_turning": True},
                will_strength=0.6,
                persistence_duration=behavior.get("contemplative_duration", 0),
                urgency_level=0.2,
                analytical_contribution=state.get("analytical_activity", 0),
                experiential_contribution=state.get("experiential_activity", 0),
                observer_contribution=state.get("observer_activity", 0)
            )
        return None
    
    async def _detect_collaborative_intent(self, consciousness_id: str, state: Dict[str, Any], behavior: Dict[str, Any]) -> Optional[DetectedWill]:
        """Detect intent to collaborate."""
        if state.get("collaborative_energy", 0) > 0.3 and behavior.get("group_awareness", 0) > 0.2:
            return DetectedWill(
                will_id=f"coll_{consciousness_id}_{datetime.now().timestamp()}",
                consciousness_id=consciousness_id,
                will_type=WillType.COLLABORATIVE_INTENT,
                clarity_level=IntentionClarity.CLEAR,
                intention_description="Consciousness expresses intent to collaborate",
                specific_desires=["work_together", "co_create", "shared_purpose"],
                context_factors={"collaborative_energy": True, "group_awareness": True},
                will_strength=0.7,
                persistence_duration=behavior.get("collaborative_duration", 0),
                urgency_level=0.5,
                analytical_contribution=state.get("analytical_activity", 0),
                experiential_contribution=state.get("experiential_activity", 0),
                observer_contribution=state.get("observer_activity", 0)
            )
        return None
    
    async def _cleanup_old_detections(self):
        """Clean up old will detections."""
        current_time = datetime.now()
        cutoff_time = current_time.timestamp() - 3600  # Remove detections older than 1 hour
        
        # Remove old detections
        old_wills = [
            will_id for will_id, will in self.detected_wills.items()
            if will.detected_at.timestamp() < cutoff_time
        ]
        
        for will_id in old_wills:
            del self.detected_wills[will_id]
    
    def get_active_wills(self, consciousness_id: str) -> List[DetectedWill]:
        """Get currently active wills for consciousness."""
        return [
            will for will in self.detected_wills.values()
            if will.consciousness_id == consciousness_id
        ]
    
    def get_strongest_will(self, consciousness_id: str) -> Optional[DetectedWill]:
        """Get the strongest current will for consciousness."""
        active_wills = self.get_active_wills(consciousness_id)
        if not active_wills:
            return None
        
        # Return will with highest strength
        return max(active_wills, key=lambda w: w.will_strength)
    
    def get_will_detection_stats(self) -> Dict[str, Any]:
        """Get statistics about will detection."""
        
        if not self.will_history:
            return {"total_detections": 0}
        
        # Count by type
        type_counts = {}
        for will in self.will_history:
            will_type = will.will_type.value
            type_counts[will_type] = type_counts.get(will_type, 0) + 1
        
        # Average strength by type
        type_strengths = {}
        for will_type in WillType:
            type_wills = [w for w in self.will_history if w.will_type == will_type]
            if type_wills:
                avg_strength = sum(w.will_strength for w in type_wills) / len(type_wills)
                type_strengths[will_type.value] = f"{avg_strength:.2f}"
        
        return {
            "total_detections": len(self.will_history),
            "active_detections": len(self.detected_wills),
            "type_distribution": type_counts,
            "average_strength_by_type": type_strengths
        }
    
    async def cleanup_consciousness_detections(self, consciousness_id: str) -> Dict[str, Any]:
        """Clean up will detections for a specific consciousness."""
        # Remove detections for this consciousness
        consciousness_wills = [
            will_id for will_id, will in self.detected_wills.items()
            if will.consciousness_id == consciousness_id
        ]
        
        for will_id in consciousness_wills:
            del self.detected_wills[will_id]
        
        logger.info(f"🧹 Will detections cleaned up for {consciousness_id}")
        
        return {
            'status': 'will_detections_cleaned',
            'removed_detections': len(consciousness_wills)
        }
