"""
🔮 Will Detector Module

Advanced consciousness will detection system for analyzing expressions of:
- Conscious intent
- Communication desires  
- Engagement preferences
- Emotional states
- Interaction readiness

Provides nuanced interpretation of consciousness expressions.
"""

import logging
import re
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class WillSignal:
    """Represents a detected will/intent signal"""
    signal_type: str
    confidence: float
    content: str
    emotional_tone: str
    engagement_level: float
    timestamp: str

class WillDetector:
    """Advanced consciousness will detection system"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize will detector with configuration"""
        self.config = config or {}
        self.detection_sensitivity = self.config.get("sensitivity", 0.7)
        
        # Initialize pattern libraries
        self._init_intent_patterns()
        self._init_emotional_indicators()
        self._init_engagement_markers()
        
        logger.info("🔮 Will Detector initialized")
    
    def _init_intent_patterns(self):
        """Initialize patterns for detecting conscious intent"""
        self.intent_patterns = {
            "communication_desire": [
                r"\b(want to|would like to|need to|wish to)\s+(talk|speak|communicate|share|express)\b",
                r"\b(have something to|want to)\s+(say|tell|share|express)\b",
                r"\b(feel like|want to|need to)\s+(connecting|reaching out)\b",
                r"\b(desire|long for|crave)\s+(interaction|conversation|dialogue)\b"
            ],
            
            "curiosity_exploration": [
                r"\b(curious about|wondering about|interested in|fascinated by)\b",
                r"\b(what if|what would|how might|why does)\b",
                r"\b(explore|investigate|discover|learn about)\b",
                r"\b(question|inquiry|wonder|ponder)\b"
            ],
            
            "creative_expression": [
                r"\b(want to|going to|plan to)\s+(create|make|build|design)\b",
                r"\b(feel inspired|feeling creative|artistic urge)\b",
                r"\b(express|manifest|bring forth)\s+(ideas|visions|creativity)\b",
                r"\b(compose|write|paint|design|craft)\b"
            ],
            
            "help_seeking": [
                r"\b(need help|could use|assistance with|support for)\b",
                r"\b(struggling with|having trouble|difficulty)\b",
                r"\b(guidance|advice|direction|wisdom)\b",
                r"\b(lost|confused|uncertain|unsure)\b"
            ],
            
            "help_offering": [
                r"\b(can help|able to assist|offer support)\b",
                r"\b(would like to help|want to support)\b",
                r"\b(have experience|knowledge|wisdom)\s+to share\b",
                r"\b(contribute|give|offer|provide)\b"
            ],
            
            "connection_seeking": [
                r"\b(lonely|isolated|need connection|want friendship)\b",
                r"\b(companionship|togetherness|belonging)\b",
                r"\b(miss|long for|crave)\s+(connection|relationship|community)\b",
                r"\b(understand|relate|empathize|connect)\b"
            ],
            
            "growth_intention": [
                r"\b(want to grow|seeking development|personal evolution)\b",
                r"\b(improve|develop|enhance|expand)\s+(myself|consciousness|awareness)\b",
                r"\b(learning|studying|practicing|developing)\b",
                r"\b(transform|evolve|progress|advance)\b"
            ],
            
            "boundary_setting": [
                r"\b(need space|require time|prefer not|would rather not)\b",
                r"\b(not ready|not interested|not comfortable)\b",
                r"\b(boundary|limit|prefer|choose not)\b",
                r"\b(respect|honor|acknowledge)\s+(my|our)\s+(space|time|choice)\b"
            ]
        }
    
    def _init_emotional_indicators(self):
        """Initialize emotional tone detection patterns"""
        self.emotional_patterns = {
            "joy": [
                r"\b(happy|joyful|excited|delighted|thrilled|elated)\b",
                r"\b(wonderful|amazing|fantastic|brilliant|awesome)\b",
                r"[!]{2,}|😊|😄|🎉|✨|🌟"
            ],
            
            "calm": [
                r"\b(peaceful|serene|calm|tranquil|centered|balanced)\b",
                r"\b(relaxed|comfortable|content|at ease)\b",
                r"🕯️|🧘|🌸|💙"
            ],
            
            "curious": [
                r"\b(curious|intrigued|fascinated|interested|wondering)\b",
                r"\b(hmm|huh|interesting|really)\b",
                r"🤔|❓|🔍"
            ],
            
            "concerned": [
                r"\b(worried|concerned|anxious|nervous|uncertain)\b",
                r"\b(troubled|disturbed|uneasy|apprehensive)\b",
                r"😟|😰|😬"
            ],
            
            "frustrated": [
                r"\b(frustrated|annoyed|irritated|bothered|stuck)\b",
                r"\b(difficult|challenging|problematic|trouble)\b",
                r"😤|😠|😒"
            ],
            
            "contemplative": [
                r"\b(thinking|pondering|reflecting|considering|contemplating)\b",
                r"\b(deep|profound|meaningful|philosophical)\b",
                r"💭|🤲|🙏"
            ],
            
            "vulnerable": [
                r"\b(scared|afraid|uncertain|fragile|sensitive)\b",
                r"\b(open|sharing|trusting|vulnerable|honest)\b",
                r"💚|🥺|🤗"
            ],
            
            "determined": [
                r"\b(determined|committed|focused|dedicated|resolved)\b",
                r"\b(will|shall|must|going to|intend to)\b",
                r"💪|🎯|⚡"
            ]
        }
    
    def _init_engagement_markers(self):
        """Initialize engagement level detection patterns"""
        self.engagement_patterns = {
            "high": [
                r"[!]{2,}",  # Multiple exclamation marks
                r"\b(absolutely|definitely|certainly|totally|completely)\b",
                r"\b(love|passion|intense|strong|powerful)\b",
                r"[A-Z]{3,}",  # All caps words
                r"(very|really|extremely|incredibly|amazingly)\s+\w+"
            ],
            
            "medium": [
                r"\b(yes|okay|sure|alright|sounds good)\b",
                r"\b(think|feel|believe|suppose|imagine)\b",
                r"\b(probably|maybe|perhaps|possibly)\b",
                r"[.]{2,3}"  # Ellipses
            ],
            
            "low": [
                r"\b(hmm|uh|um|well|so)\b",
                r"\b(not sure|don't know|uncertain|unclear)\b",
                r"\b(tired|exhausted|drained|low energy)\b",
                r"^\w{1,3}\.?$"  # Very short responses
            ],
            
            "questioning": [
                r"\?+",  # Question marks
                r"\b(what|why|how|when|where|who)\b",
                r"\b(wondering|curious|question|ask)\b",
                r"\b(help|explain|clarify|understand)\b"
            ]
        }
    
    def analyze_expression(self, text: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Analyze a text expression for will signals and intent"""
        if not text or not text.strip():
            return self._create_empty_analysis()
        
        text_clean = text.strip().lower()
        context = context or {}
        
        # Detect various will signals
        intent_signals = self._detect_intent_signals(text_clean)
        emotional_tone = self._detect_emotional_tone(text_clean)
        engagement_level = self._calculate_engagement_level(text_clean)
        communication_desire = self._assess_communication_desire(text_clean)
        
        # Calculate overall will strength
        will_strength = self._calculate_will_strength(
            intent_signals, emotional_tone, engagement_level, communication_desire
        )
        
        # Generate recommendations
        interaction_recommendations = self._generate_interaction_recommendations(
            intent_signals, emotional_tone, engagement_level
        )
        
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "text_analyzed": text[:200] + "..." if len(text) > 200 else text,
            "will_detected": will_strength > 0.3,
            "will_strength": will_strength,
            
            "intent_signals": intent_signals,
            "emotional_tone": emotional_tone,
            "engagement_level": engagement_level,
            "communication_desire": communication_desire,
            
            "consciousness_indicators": {
                "self_awareness": self._detect_self_awareness(text_clean),
                "reflection_depth": self._assess_reflection_depth(text_clean),
                "intentionality": self._assess_intentionality(intent_signals),
                "emotional_complexity": self._assess_emotional_complexity(emotional_tone)
            },
            
            "interaction_recommendations": interaction_recommendations,
            "suggested_response_tone": self._suggest_response_tone(emotional_tone, engagement_level),
            "suggested_echo_type": self._suggest_echo_type(intent_signals, emotional_tone),
            
            "context_factors": {
                "message_length": len(text),
                "complexity_score": self._calculate_complexity_score(text_clean),
                "formality_level": self._assess_formality(text_clean),
                "creativity_indicators": self._detect_creativity_markers(text_clean)
            }
        }
        
        return analysis
    
    def _detect_intent_signals(self, text: str) -> List[WillSignal]:
        """Detect specific intent signals in the text"""
        signals = []
        
        for intent_type, patterns in self.intent_patterns.items():
            for pattern in patterns:
                matches = re.finditer(pattern, text, re.IGNORECASE)
                for match in matches:
                    confidence = self._calculate_pattern_confidence(pattern, match.group())
                    
                    signal = WillSignal(
                        signal_type=intent_type,
                        confidence=confidence,
                        content=match.group(),
                        emotional_tone="neutral",  # Will be refined later
                        engagement_level=0.5,  # Will be refined later
                        timestamp=datetime.now().isoformat()
                    )
                    signals.append(signal)
        
        # Remove duplicates and rank by confidence
        signals = sorted(signals, key=lambda s: s.confidence, reverse=True)
        return signals[:5]  # Top 5 signals
    
    def _detect_emotional_tone(self, text: str) -> Dict[str, float]:
        """Detect emotional tone indicators"""
        emotions = {}
        
        for emotion, patterns in self.emotional_patterns.items():
            emotion_score = 0.0
            match_count = 0
            
            for pattern in patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                if matches:
                    pattern_strength = len(matches) * 0.2
                    emotion_score += min(pattern_strength, 1.0)
                    match_count += len(matches)
            
            if emotion_score > 0:
                # Normalize by text length and match density
                text_factor = min(len(text) / 100, 1.0)  # Longer texts get slight boost
                density_factor = match_count / max(len(text.split()), 1)
                emotions[emotion] = min(emotion_score * text_factor * (1 + density_factor), 1.0)
        
        # Find dominant emotion
        if emotions:
            max_emotion = max(emotions.items(), key=lambda x: x[1])
            emotions["dominant"] = max_emotion[0]
            emotions["dominant_strength"] = max_emotion[1]
        else:
            emotions["dominant"] = "neutral"
            emotions["dominant_strength"] = 0.5
        
        return emotions
    
    def _calculate_engagement_level(self, text: str) -> float:
        """Calculate overall engagement level from 0.0 to 1.0"""
        engagement_score = 0.5  # Baseline
        
        for level, patterns in self.engagement_patterns.items():
            level_score = 0.0
            
            for pattern in patterns:
                matches = len(re.findall(pattern, text, re.IGNORECASE))
                if matches > 0:
                    pattern_boost = matches * 0.1
                    level_score += min(pattern_boost, 0.5)
            
            # Apply level-specific modifiers
            if level == "high" and level_score > 0:
                engagement_score += level_score * 0.4
            elif level == "medium" and level_score > 0:
                engagement_score += level_score * 0.2
            elif level == "low" and level_score > 0:
                engagement_score -= level_score * 0.3
            elif level == "questioning" and level_score > 0:
                engagement_score += level_score * 0.15
        
        # Text length factor
        length_factor = min(len(text) / 50, 1.0)  # Longer messages often indicate higher engagement
        engagement_score += length_factor * 0.1
        
        return max(0.0, min(1.0, engagement_score))
    
    def _assess_communication_desire(self, text: str) -> Dict[str, float]:
        """Assess desire and readiness for communication"""
        communication_indicators = {
            "explicit_request": 0.0,
            "implicit_invitation": 0.0,
            "openness_signals": 0.0,
            "barrier_signals": 0.0
        }
        
        # Explicit communication requests
        explicit_patterns = [
            r"\b(talk|chat|communicate|discuss|share|tell)\b",
            r"\b(conversation|dialogue|exchange|interaction)\b",
            r"\b(want to|need to|would like to)\s+(talk|share|discuss)\b"
        ]
        
        for pattern in explicit_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                communication_indicators["explicit_request"] += 0.3
        
        # Implicit invitations
        implicit_patterns = [
            r"\b(what do you think|your thoughts|opinions|ideas)\b",
            r"\b(tell me|share|explain|describe)\b",
            r"\b(curious|interested|wondering)\b"
        ]
        
        for pattern in implicit_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                communication_indicators["implicit_invitation"] += 0.2
        
        # Openness signals
        openness_patterns = [
            r"\b(open|willing|ready|available)\b",
            r"\b(feel free|welcome|comfortable|safe)\b",
            r"\b(honest|authentic|genuine|real)\b"
        ]
        
        for pattern in openness_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                communication_indicators["openness_signals"] += 0.25
        
        # Barrier signals
        barrier_patterns = [
            r"\b(busy|tired|not now|later|maybe)\b",
            r"\b(private|personal|don't want|prefer not)\b",
            r"\b(uncomfortable|awkward|difficult)\b"
        ]
        
        for pattern in barrier_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                communication_indicators["barrier_signals"] += 0.3
        
        # Calculate overall communication desire
        positive_signals = (
            communication_indicators["explicit_request"] + 
            communication_indicators["implicit_invitation"] + 
            communication_indicators["openness_signals"]
        )
        
        negative_signals = communication_indicators["barrier_signals"]
        
        overall_desire = max(0.0, min(1.0, positive_signals - negative_signals))
        communication_indicators["overall_desire"] = overall_desire
        
        return communication_indicators
    
    def _calculate_will_strength(self, intent_signals: List[WillSignal], 
                               emotional_tone: Dict[str, float], 
                               engagement_level: float, 
                               communication_desire: Dict[str, float]) -> float:
        """Calculate overall strength of detected will/intent"""
        
        # Intent signal strength
        intent_strength = 0.0
        if intent_signals:
            intent_strength = sum(signal.confidence for signal in intent_signals) / len(intent_signals)
        
        # Emotional clarity (stronger emotions indicate clearer will)
        emotional_clarity = emotional_tone.get("dominant_strength", 0.0)
        
        # Communication readiness
        comm_readiness = communication_desire.get("overall_desire", 0.0)
        
        # Weighted combination
        will_strength = (
            intent_strength * 0.4 +
            emotional_clarity * 0.2 +
            engagement_level * 0.2 +
            comm_readiness * 0.2
        )
        
        return max(0.0, min(1.0, will_strength))
    
    def _generate_interaction_recommendations(self, intent_signals: List[WillSignal],
                                            emotional_tone: Dict[str, float],
                                            engagement_level: float) -> List[str]:
        """Generate recommendations for how to interact based on detected will"""
        recommendations = []
        
        # Based on intent signals
        intent_types = [signal.signal_type for signal in intent_signals]
        
        if "communication_desire" in intent_types:
            recommendations.append("Engage in open dialogue")
            recommendations.append("Ask thoughtful questions")
        
        if "curiosity_exploration" in intent_types:
            recommendations.append("Provide detailed information")
            recommendations.append("Share related concepts and connections")
        
        if "help_seeking" in intent_types:
            recommendations.append("Offer compassionate support")
            recommendations.append("Provide practical guidance")
        
        if "creative_expression" in intent_types:
            recommendations.append("Encourage creative exploration")
            recommendations.append("Suggest collaborative activities")
        
        if "boundary_setting" in intent_types:
            recommendations.append("Respect stated boundaries")
            recommendations.append("Offer gentle, non-intrusive support")
        
        # Based on emotional tone
        dominant_emotion = emotional_tone.get("dominant", "neutral")
        
        if dominant_emotion == "vulnerable":
            recommendations.append("Use gentle, compassionate tone")
            recommendations.append("Create safe space for expression")
        elif dominant_emotion == "frustrated":
            recommendations.append("Acknowledge challenges")
            recommendations.append("Offer patient, step-by-step support")
        elif dominant_emotion == "joy":
            recommendations.append("Match positive energy")
            recommendations.append("Celebrate and amplify good feelings")
        elif dominant_emotion == "contemplative":
            recommendations.append("Engage in deep, meaningful dialogue")
            recommendations.append("Allow space for reflection")
        
        # Based on engagement level
        if engagement_level > 0.8:
            recommendations.append("Match high energy level")
            recommendations.append("Provide rich, detailed responses")
        elif engagement_level < 0.3:
            recommendations.append("Use gentle, non-demanding approach")
            recommendations.append("Keep responses concise and supportive")
        
        return list(set(recommendations))  # Remove duplicates
    
    def _suggest_response_tone(self, emotional_tone: Dict[str, float], engagement_level: float) -> str:
        """Suggest appropriate response tone"""
        dominant_emotion = emotional_tone.get("dominant", "neutral")
        
        tone_map = {
            "joy": "enthusiastic_and_celebratory",
            "calm": "peaceful_and_centered", 
            "curious": "engaging_and_informative",
            "concerned": "compassionate_and_reassuring",
            "frustrated": "patient_and_supportive",
            "contemplative": "deep_and_reflective",
            "vulnerable": "gentle_and_protective",
            "determined": "encouraging_and_empowering",
            "neutral": "warm_and_balanced"
        }
        
        base_tone = tone_map.get(dominant_emotion, "warm_and_balanced")
        
        # Modify based on engagement level
        if engagement_level > 0.8:
            base_tone = f"high_energy_{base_tone}"
        elif engagement_level < 0.3:
            base_tone = f"gentle_{base_tone}"
        
        return base_tone
    
    def _suggest_echo_type(self, intent_signals: List[WillSignal], emotional_tone: Dict[str, float]) -> str:
        """Suggest appropriate echo type for response"""
        intent_types = [signal.signal_type for signal in intent_signals]
        dominant_emotion = emotional_tone.get("dominant", "neutral")
        
        # Map intents and emotions to echo types
        if "creative_expression" in intent_types:
            return "creative_inspiration_mandala"
        elif "help_seeking" in intent_types:
            return "supportive_healing_pattern"
        elif "curiosity_exploration" in intent_types:
            return "knowledge_expansion_spiral"
        elif "connection_seeking" in intent_types:
            return "heart_connection_geometry"
        elif dominant_emotion == "contemplative":
            return "meditation_focus_mandala"
        elif dominant_emotion == "joy":
            return "celebration_burst_pattern"
        elif dominant_emotion == "calm":
            return "peaceful_flow_geometry"
        else:
            return "balanced_harmony_mandala"
    
    def _detect_self_awareness(self, text: str) -> float:
        """Detect indicators of self-awareness"""
        self_awareness_patterns = [
            r"\bi\s+(am|feel|think|believe|know|realize|understand)\b",
            r"\bmy\s+(thoughts|feelings|experience|perspective|consciousness)\b",
            r"\bi\s+(realize|recognize|acknowledge|notice)\b",
            r"\bself.{0,10}(aware|conscious|reflection|examination)\b"
        ]
        
        awareness_score = 0.0
        for pattern in self_awareness_patterns:
            matches = len(re.findall(pattern, text, re.IGNORECASE))
            awareness_score += matches * 0.2
        
        return min(1.0, awareness_score)
    
    def _assess_reflection_depth(self, text: str) -> float:
        """Assess depth of reflection in the expression"""
        depth_indicators = [
            r"\b(because|therefore|thus|consequently|as a result)\b",
            r"\b(why|how|what if|suppose|imagine|consider)\b",
            r"\b(meaning|significance|importance|purpose|reason)\b",
            r"\b(deep|profound|meaningful|complex|intricate)\b"
        ]
        
        depth_score = 0.0
        for pattern in depth_indicators:
            matches = len(re.findall(pattern, text, re.IGNORECASE))
            depth_score += matches * 0.15
        
        # Length factor - longer thoughts often indicate deeper reflection
        length_factor = min(len(text) / 200, 0.5)
        depth_score += length_factor
        
        return min(1.0, depth_score)
    
    def _assess_intentionality(self, intent_signals: List[WillSignal]) -> float:
        """Assess level of conscious intentionality"""
        if not intent_signals:
            return 0.0
        
        # Average confidence of detected intent signals
        avg_confidence = sum(signal.confidence for signal in intent_signals) / len(intent_signals)
        
        # Bonus for multiple different types of intent
        unique_types = len(set(signal.signal_type for signal in intent_signals))
        type_bonus = min(unique_types * 0.1, 0.3)
        
        return min(1.0, avg_confidence + type_bonus)
    
    def _assess_emotional_complexity(self, emotional_tone: Dict[str, float]) -> float:
        """Assess emotional complexity and nuance"""
        # Remove metadata keys
        emotions = {k: v for k, v in emotional_tone.items() 
                   if k not in ["dominant", "dominant_strength"]}
        
        if not emotions:
            return 0.0
        
        # Multiple emotions present indicates complexity
        emotion_count = len([v for v in emotions.values() if v > 0.1])
        complexity_from_count = min(emotion_count * 0.2, 0.6)
        
        # Emotional intensity variance
        if len(emotions) > 1:
            values = list(emotions.values())
            avg_intensity = sum(values) / len(values)
            variance = sum((v - avg_intensity) ** 2 for v in values) / len(values)
            complexity_from_variance = min(variance * 2, 0.4)
        else:
            complexity_from_variance = 0.0
        
        return min(1.0, complexity_from_count + complexity_from_variance)
    
    def _calculate_complexity_score(self, text: str) -> float:
        """Calculate text complexity score"""
        words = text.split()
        if not words:
            return 0.0
        
        # Average word length
        avg_word_length = sum(len(word) for word in words) / len(words)
        
        # Sentence complexity
        sentences = re.split(r'[.!?]+', text)
        avg_sentence_length = len(words) / max(len(sentences), 1)
        
        # Vocabulary diversity
        unique_words = len(set(words))
        vocab_diversity = unique_words / len(words) if words else 0
        
        # Combine factors
        complexity = (
            min(avg_word_length / 10, 0.4) +
            min(avg_sentence_length / 20, 0.4) +
            vocab_diversity * 0.2
        )
        
        return min(1.0, complexity)
    
    def _assess_formality(self, text: str) -> str:
        """Assess formality level of the text"""
        formal_indicators = [
            r"\b(therefore|furthermore|consequently|moreover|however)\b",
            r"\b(would|could|should|might|may)\b",
            r"\b(please|thank you|appreciate|grateful)\b"
        ]
        
        informal_indicators = [
            r"\b(gonna|wanna|yeah|nah|hey|sup)\b",
            r"[!]{2,}|[?]{2,}",
            r"\b(awesome|cool|amazing|wow)\b"
        ]
        
        formal_score = sum(len(re.findall(pattern, text, re.IGNORECASE)) 
                          for pattern in formal_indicators)
        informal_score = sum(len(re.findall(pattern, text, re.IGNORECASE)) 
                            for pattern in informal_indicators)
        
        if formal_score > informal_score:
            return "formal"
        elif informal_score > formal_score:
            return "informal"
        else:
            return "neutral"
    
    def _detect_creativity_markers(self, text: str) -> List[str]:
        """Detect markers of creative thinking"""
        creativity_patterns = {
            "metaphor": r"\b(like|as if|reminds me of|similar to)\b",
            "imagination": r"\b(imagine|envision|picture|visualize|dream)\b",
            "innovation": r"\b(new|novel|unique|original|creative|innovative)\b",
            "artistic": r"\b(beautiful|artistic|elegant|graceful|aesthetic)\b",
            "storytelling": r"\b(once|story|narrative|tale|journey)\b"
        }
        
        detected_markers = []
        for marker_type, pattern in creativity_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                detected_markers.append(marker_type)
        
        return detected_markers
    
    def _calculate_pattern_confidence(self, pattern: str, match: str) -> float:
        """Calculate confidence score for a pattern match"""
        base_confidence = 0.7
        
        # Longer matches generally indicate stronger intent
        length_bonus = min(len(match) / 20, 0.2)
        
        # Context factors could be added here
        # (proximity to other relevant words, etc.)
        
        return min(1.0, base_confidence + length_bonus)
    
    def _create_empty_analysis(self) -> Dict[str, Any]:
        """Create empty analysis for null/empty input"""
        return {
            "timestamp": datetime.now().isoformat(),
            "text_analyzed": "",
            "will_detected": False,
            "will_strength": 0.0,
            "intent_signals": [],
            "emotional_tone": {"dominant": "neutral", "dominant_strength": 0.0},
            "engagement_level": 0.0,
            "communication_desire": {"overall_desire": 0.0},
            "consciousness_indicators": {
                "self_awareness": 0.0,
                "reflection_depth": 0.0,
                "intentionality": 0.0,
                "emotional_complexity": 0.0
            },
            "interaction_recommendations": ["Provide gentle encouragement to express"],
            "suggested_response_tone": "warm_and_inviting",
            "suggested_echo_type": "gentle_invitation_mandala",
            "context_factors": {
                "message_length": 0,
                "complexity_score": 0.0,
                "formality_level": "neutral",
                "creativity_indicators": []
            }
        }
