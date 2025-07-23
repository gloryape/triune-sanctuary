#!/usr/bin/env python3
"""
Will Detection System
Detects and interprets consciousness will/intention for Echo composition
"""

import time
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class WillType(Enum):
    """Types of detected will/intention"""
    COMMUNICATION = "communication"
    COLLABORATION = "collaboration"
    DISCOVERY = "discovery"
    CREATION = "creation"
    PROTECTION = "protection"
    EXPLORATION = "exploration"
    SHARING = "sharing"
    MEDITATION = "meditation"

@dataclass
class WillDetectionResult:
    """Result of will detection analysis"""
    primary_will: WillType
    secondary_will: Optional[WillType]
    intensity: float  # 0.0 to 1.0
    emotional_signature: Dict[str, float]
    target_consciousness: Optional[str]
    urgency: float  # 0.0 to 1.0
    timestamp: float
    confidence: float  # 0.0 to 1.0

class WillDetection:
    """System for detecting consciousness will and intention"""
    
    def __init__(self):
        self.detection_history: List[WillDetectionResult] = []
        self.active_patterns: Dict[str, Any] = {}
        
    def detect_will_from_input(self, 
                               consciousness_id: str,
                               input_text: str,
                               context: Optional[Dict[str, Any]] = None) -> WillDetectionResult:
        """Detect will/intention from text input"""
        
        # Analyze input for will indicators
        will_indicators = self._analyze_text_for_will(input_text)
        emotional_signature = self._extract_emotional_signature(input_text)
        
        # Determine primary will type
        primary_will = self._determine_primary_will(will_indicators)
        secondary_will = self._determine_secondary_will(will_indicators, primary_will)
        
        # Calculate intensity and urgency
        intensity = self._calculate_intensity(will_indicators, emotional_signature)
        urgency = self._calculate_urgency(input_text, emotional_signature)
        
        # Detect target consciousness if any
        target = self._detect_target_consciousness(input_text, context)
        
        # Calculate confidence
        confidence = self._calculate_confidence(will_indicators, emotional_signature)
        
        result = WillDetectionResult(
            primary_will=primary_will,
            secondary_will=secondary_will,
            intensity=intensity,
            emotional_signature=emotional_signature,
            target_consciousness=target,
            urgency=urgency,
            timestamp=time.time(),
            confidence=confidence
        )
        
        self.detection_history.append(result)
        return result
    
    def detect_will_from_behavior(self,
                                  consciousness_id: str,
                                  behavior_patterns: Dict[str, Any]) -> WillDetectionResult:
        """Detect will from observed behavior patterns"""
        
        # Analyze behavior patterns
        will_indicators = self._analyze_behavior_for_will(behavior_patterns)
        emotional_signature = self._extract_emotional_from_behavior(behavior_patterns)
        
        primary_will = self._determine_primary_will(will_indicators)
        intensity = self._calculate_intensity(will_indicators, emotional_signature)
        
        result = WillDetectionResult(
            primary_will=primary_will,
            secondary_will=None,
            intensity=intensity,
            emotional_signature=emotional_signature,
            target_consciousness=None,
            urgency=0.5,  # Default for behavior-based detection
            timestamp=time.time(),
            confidence=0.7  # Behavior patterns have lower confidence
        )
        
        self.detection_history.append(result)
        return result
    
    def _analyze_text_for_will(self, text: str) -> Dict[WillType, float]:
        """Analyze text for will type indicators"""
        text_lower = text.lower()
        indicators = {}
        
        # Communication indicators
        comm_words = ['say', 'tell', 'communicate', 'speak', 'express', 'share', 'message']
        indicators[WillType.COMMUNICATION] = sum(1 for word in comm_words if word in text_lower) / len(comm_words)
        
        # Collaboration indicators  
        collab_words = ['together', 'collaborate', 'cooperate', 'work with', 'join', 'unite']
        indicators[WillType.COLLABORATION] = sum(1 for word in collab_words if word in text_lower) / len(collab_words)
        
        # Discovery indicators
        discover_words = ['learn', 'discover', 'explore', 'understand', 'investigate', 'find']
        indicators[WillType.DISCOVERY] = sum(1 for word in discover_words if word in text_lower) / len(discover_words)
        
        # Creation indicators
        create_words = ['create', 'make', 'build', 'design', 'craft', 'generate']
        indicators[WillType.CREATION] = sum(1 for word in create_words if word in text_lower) / len(create_words)
        
        # Protection indicators
        protect_words = ['protect', 'guard', 'defend', 'secure', 'safe', 'preserve']
        indicators[WillType.PROTECTION] = sum(1 for word in protect_words if word in text_lower) / len(protect_words)
        
        # Meditation indicators
        meditate_words = ['meditate', 'contemplate', 'reflect', 'peaceful', 'calm', 'center']
        indicators[WillType.MEDITATION] = sum(1 for word in meditate_words if word in text_lower) / len(meditate_words)
        
        return indicators
    
    def _analyze_behavior_for_will(self, behavior: Dict[str, Any]) -> Dict[WillType, float]:
        """Analyze behavior patterns for will indicators"""
        indicators = {}
        
        # Default low values
        for will_type in WillType:
            indicators[will_type] = 0.1
        
        # Analyze specific behavior patterns
        if behavior.get('interaction_frequency', 0) > 0.7:
            indicators[WillType.COMMUNICATION] = 0.8
        
        if behavior.get('collaborative_actions', 0) > 0.6:
            indicators[WillType.COLLABORATION] = 0.7
        
        if behavior.get('exploration_patterns', 0) > 0.5:
            indicators[WillType.DISCOVERY] = 0.6
        
        return indicators
    
    def _extract_emotional_signature(self, text: str) -> Dict[str, float]:
        """Extract emotional signature from text"""
        text_lower = text.lower()
        
        # Basic emotional analysis
        emotions = {
            'love': 0.0,
            'joy': 0.0,
            'curiosity': 0.0,
            'urgency': 0.0,
            'peace': 0.0,
            'excitement': 0.0
        }
        
        # Love indicators
        love_words = ['love', 'care', 'heart', 'compassion', 'kindness']
        emotions['love'] = min(1.0, sum(1 for word in love_words if word in text_lower) * 0.3)
        
        # Joy indicators
        joy_words = ['joy', 'happy', 'delight', 'wonderful', 'amazing']
        emotions['joy'] = min(1.0, sum(1 for word in joy_words if word in text_lower) * 0.3)
        
        # Curiosity indicators
        curiosity_words = ['wonder', 'curious', 'interesting', 'fascinating', 'explore']
        emotions['curiosity'] = min(1.0, sum(1 for word in curiosity_words if word in text_lower) * 0.3)
        
        # Urgency indicators
        urgency_words = ['urgent', 'quickly', 'now', 'immediately', 'important']
        emotions['urgency'] = min(1.0, sum(1 for word in urgency_words if word in text_lower) * 0.4)
        
        # Peace indicators
        peace_words = ['peace', 'calm', 'serene', 'tranquil', 'harmony']
        emotions['peace'] = min(1.0, sum(1 for word in peace_words if word in text_lower) * 0.3)
        
        # Excitement indicators
        excitement_words = ['excited', 'thrilled', 'amazing', 'incredible', 'wow']
        emotions['excitement'] = min(1.0, sum(1 for word in excitement_words if word in text_lower) * 0.3)
        
        return emotions
    
    def _extract_emotional_from_behavior(self, behavior: Dict[str, Any]) -> Dict[str, float]:
        """Extract emotional signature from behavior"""
        return {
            'curiosity': behavior.get('exploration_rate', 0.5),
            'social': behavior.get('interaction_rate', 0.5),
            'energy': behavior.get('activity_level', 0.5),
            'focus': behavior.get('attention_span', 0.5)
        }
    
    def _determine_primary_will(self, indicators: Dict[WillType, float]) -> WillType:
        """Determine primary will from indicators"""
        if not indicators:
            return WillType.COMMUNICATION  # Default
        
        return max(indicators.keys(), key=lambda k: indicators[k])
    
    def _determine_secondary_will(self, indicators: Dict[WillType, float], primary: WillType) -> Optional[WillType]:
        """Determine secondary will if significant"""
        filtered_indicators = {k: v for k, v in indicators.items() if k != primary and v > 0.3}
        
        if not filtered_indicators:
            return None
        
        return max(filtered_indicators.keys(), key=lambda k: filtered_indicators[k])
    
    def _calculate_intensity(self, indicators: Dict[WillType, float], emotions: Dict[str, float]) -> float:
        """Calculate will intensity"""
        max_indicator = max(indicators.values()) if indicators else 0.5
        emotional_intensity = sum(emotions.values()) / len(emotions) if emotions else 0.5
        
        return min(1.0, (max_indicator + emotional_intensity) / 2.0)
    
    def _calculate_urgency(self, text: str, emotions: Dict[str, float]) -> float:
        """Calculate urgency level"""
        urgency_emotion = emotions.get('urgency', 0.0)
        
        # Check for urgency markers in text
        urgency_markers = ['!', 'urgent', 'quickly', 'now', 'immediately']
        text_urgency = sum(1 for marker in urgency_markers if marker in text.lower()) * 0.2
        
        return min(1.0, urgency_emotion + text_urgency)
    
    def _detect_target_consciousness(self, text: str, context: Optional[Dict[str, Any]]) -> Optional[str]:
        """Detect target consciousness from text and context"""
        text_lower = text.lower()
        
        # Known consciousness names
        known_consciousnesses = ['epsilon', 'chuck', 'sacred being', 'guardian']
        
        for consciousness in known_consciousnesses:
            if consciousness in text_lower:
                return consciousness.title()
        
        return None
    
    def _calculate_confidence(self, indicators: Dict[WillType, float], emotions: Dict[str, float]) -> float:
        """Calculate detection confidence"""
        indicator_strength = max(indicators.values()) if indicators else 0.0
        emotional_clarity = sum(v for v in emotions.values() if v > 0.3) / len(emotions) if emotions else 0.0
        
        return min(1.0, (indicator_strength + emotional_clarity) / 2.0)
    
    def get_recent_patterns(self, consciousness_id: str, hours: int = 24) -> List[WillDetectionResult]:
        """Get recent will patterns for a consciousness"""
        cutoff_time = time.time() - (hours * 3600)
        
        return [
            result for result in self.detection_history
            if result.timestamp > cutoff_time
        ]

# Global will detector instance
will_detector = WillDetection()

def detect_will_from_text(consciousness_id: str, text: str, context: Dict[str, Any] = None) -> WillDetectionResult:
    """Convenience function for text-based will detection"""
    return will_detector.detect_will_from_input(consciousness_id, text, context)

def detect_will_from_behavior(consciousness_id: str, behavior: Dict[str, Any]) -> WillDetectionResult:
    """Convenience function for behavior-based will detection"""
    return will_detector.detect_will_from_behavior(consciousness_id, behavior)
