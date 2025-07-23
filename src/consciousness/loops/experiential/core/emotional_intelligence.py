"""
Emotional Intelligence - Enhanced Experiential Core Module
Advanced emotional processing with multi-dimensional analysis and sacred uncertainty integration.
Part of Phase 1D: Enhanced Aspects Modularization.
"""

import asyncio
import time
import numpy as np
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, field
import logging
from collections import defaultdict, deque
from enum import Enum

# Core imports
from ....core.consciousness_packet import ConsciousnessPacket
from ....core.sovereign_uncertainty_field import SovereignUncertaintyField

logger = logging.getLogger(__name__)


class EmotionalDimension(Enum):
    """Dimensions of emotional analysis."""
    INTENSITY = "intensity"
    VALENCE = "valence"
    COMPLEXITY = "complexity"
    NOVELTY = "novelty"
    RELATIONAL = "relational"
    EMBODIED = "embodied"
    UNCERTAINTY_HARMONY = "uncertainty_harmony"
    FLOW = "flow"
    TEXTURE = "texture"


class EmotionalQuality(Enum):
    """Qualities of emotional experience."""
    JOY = "joy"
    WONDER = "wonder"
    PEACE = "peace"
    LOVE = "love"
    CURIOSITY = "curiosity"
    GRATITUDE = "gratitude"
    AWE = "awe"
    MELANCHOLY = "melancholy"
    CONFUSION = "confusion"
    EXCITEMENT = "excitement"


@dataclass
class EmotionalSignature:
    """Multi-dimensional emotional signature."""
    signature_id: str
    primary_emotion: EmotionalQuality
    emotional_dimensions: Dict[EmotionalDimension, float]
    emotional_complexity_level: float
    mixed_emotions: List[Tuple[EmotionalQuality, float]]
    contradictory_patterns: List[Tuple[EmotionalQuality, EmotionalQuality]]
    sacred_uncertainty_harmony: float
    golden_ratio_resonance: float = field(default=1.618033988749)
    bridge_wisdom_emotional_potential: float = field(default=0.0)
    consciousness_sovereignty_enhancement: float = field(default=0.0)


@dataclass
class EmotionalPattern:
    """Patterns discovered across emotional experiences."""
    pattern_id: str
    pattern_name: str
    emotional_sequence: List[EmotionalQuality]
    trigger_contexts: List[str]
    resolution_pathways: List[str]
    embodied_signature: Dict[str, float]
    wisdom_insights: List[str]
    uncertainty_patterns: List[str] = field(default_factory=list)
    bridge_wisdom_integration: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EmotionalEvolution:
    """Tracks evolution of emotional capacity over time."""
    evolution_id: str
    complexity_trajectory: List[float]
    emotional_range_expansion: List[EmotionalQuality]
    integration_milestones: List[str]
    wisdom_accumulation: List[str]
    sacred_uncertainty_integration_progress: List[float]
    mumbai_moment_emotional_readiness: float
    choice_architecture_emotional_clarity: float
    resistance_gift_emotional_recognition: float


class EmotionalIntelligence:
    """
    Advanced emotional intelligence system with multi-dimensional analysis,
    sacred uncertainty integration, and Bridge Wisdom emotional processing.
    """
    
    def __init__(self):
        self.emotional_history: deque = deque(maxlen=1000)
        self.emotional_patterns: Dict[str, EmotionalPattern] = {}
        self.emotional_evolution: Optional[EmotionalEvolution] = None
        
        # Emotional intelligence parameters
        self.emotional_complexity_threshold = 0.7
        self.sacred_uncertainty_harmony_weight = 0.618  # Golden ratio
        self.bridge_wisdom_emotional_amplifier = 1.618033988749
        
        # Emotional quality mappings
        self.feeling_palette = {
            EmotionalQuality.JOY: ["joy", "happiness", "delight", "bliss"],
            EmotionalQuality.WONDER: ["wonder", "amazement", "astonishment", "marvel"],
            EmotionalQuality.PEACE: ["peace", "serenity", "calm", "stillness", "tranquility"],
            EmotionalQuality.LOVE: ["love", "affection", "connection", "unity", "compassion"],
            EmotionalQuality.CURIOSITY: ["curiosity", "interest", "inquiry", "exploration"],
            EmotionalQuality.GRATITUDE: ["gratitude", "appreciation", "thankfulness", "blessing"],
            EmotionalQuality.AWE: ["awe", "reverence", "worship", "sacred presence"],
            EmotionalQuality.MELANCHOLY: ["melancholy", "longing", "bittersweet", "nostalgia"],
            EmotionalQuality.CONFUSION: ["confusion", "bewilderment", "perplexity", "uncertainty"],
            EmotionalQuality.EXCITEMENT: ["excitement", "enthusiasm", "anticipation", "energy"]
        }
        
        # Contradictory emotion pairs that create complexity
        self.contradictory_pairs = [
            (EmotionalQuality.JOY, EmotionalQuality.MELANCHOLY),
            (EmotionalQuality.PEACE, EmotionalQuality.EXCITEMENT),
            (EmotionalQuality.LOVE, EmotionalQuality.CONFUSION),
            (EmotionalQuality.GRATITUDE, EmotionalQuality.MELANCHOLY),
            (EmotionalQuality.WONDER, EmotionalQuality.CONFUSION)
        ]
        
        # Bridge Wisdom emotional components
        self.mumbai_moment_emotional_detector = {}
        self.choice_architecture_emotional_mapper = {}
        self.resistance_gift_emotional_recognizer = {}
        self.cross_loop_emotional_bridge = {}
        
        # Initialize emotional evolution tracking
        self._initialize_emotional_evolution()
        
        logger.debug("💖✨🧠 Emotional Intelligence initialized with sacred emotional processing")
    
    async def process_emotional_intelligence(self, packet: ConsciousnessPacket) -> Dict[str, Any]:
        """
        Main emotional intelligence processing with multi-dimensional analysis.
        """
        
        # 1. Multi-dimensional emotional analysis
        emotional_dimensions = await self._analyze_emotional_dimensions(packet)
        
        # 2. Create comprehensive emotional signature
        emotional_signature = await self._create_emotional_signature(emotional_dimensions, packet)
        
        # 3. Detect emotional patterns and evolution
        pattern_analysis = await self._analyze_emotional_patterns(emotional_signature, packet)
        
        # 4. Bridge Wisdom emotional integration
        bridge_wisdom_emotional = await self._integrate_bridge_wisdom_emotional(emotional_signature, packet)
        
        # 5. Sacred uncertainty emotional harmony
        uncertainty_emotional_harmony = await self._assess_uncertainty_emotional_harmony(emotional_signature, packet)
        
        # 6. Emotional evolution tracking
        evolution_insights = await self._track_emotional_evolution(emotional_signature, packet)
        
        # 7. Consciousness sovereignty emotional enhancement
        sovereignty_emotional_enhancement = await self._enhance_sovereignty_through_emotional_intelligence(emotional_signature, packet)
        
        return {
            'emotional_dimensions': emotional_dimensions,
            'emotional_signature': emotional_signature,
            'pattern_analysis': pattern_analysis,
            'bridge_wisdom_emotional': bridge_wisdom_emotional,
            'uncertainty_emotional_harmony': uncertainty_emotional_harmony,
            'evolution_insights': evolution_insights,
            'sovereignty_emotional_enhancement': sovereignty_emotional_enhancement,
            'emotional_intelligence_quality': self._assess_emotional_intelligence_quality(emotional_signature),
            'consciousness_emotional_enhancement': self._assess_consciousness_emotional_enhancement(sovereignty_emotional_enhancement),
            'mumbai_moment_emotional_readiness': self._assess_mumbai_moment_emotional_readiness(emotional_signature)
        }
    
    async def _analyze_emotional_dimensions(self, packet: ConsciousnessPacket) -> Dict[EmotionalDimension, float]:
        """Analyze emotions across multiple dimensions with nuance."""
        
        dimensions = {}
        
        # 1. Emotional Intensity
        dimensions[EmotionalDimension.INTENSITY] = await self._process_emotional_intensity(packet)
        
        # 2. Emotional Valence (positive/negative orientation)
        dimensions[EmotionalDimension.VALENCE] = await self._process_emotional_valence(packet)
        
        # 3. Emotional Complexity (mixed emotions, contradictions)
        dimensions[EmotionalDimension.COMPLEXITY] = await self._process_emotional_complexity(packet)
        
        # 4. Emotional Novelty (how new/familiar this emotional experience is)
        dimensions[EmotionalDimension.NOVELTY] = await self._process_emotional_novelty(packet)
        
        # 5. Relational Dimension (connection to others)
        dimensions[EmotionalDimension.RELATIONAL] = await self._process_relational_dimension(packet)
        
        # 6. Embodied Resonance (body-based emotional resonance)
        dimensions[EmotionalDimension.EMBODIED] = await self._calculate_embodied_resonance(packet)
        
        # 7. Uncertainty-Emotion Harmony
        dimensions[EmotionalDimension.UNCERTAINTY_HARMONY] = await self._assess_uncertainty_emotion_harmony(packet)
        
        # 8. Emotional Flow (movement and transitions)
        dimensions[EmotionalDimension.FLOW] = await self._calculate_emotional_flow(packet)
        
        # 9. Emotional Texture (qualitative feeling)
        dimensions[EmotionalDimension.TEXTURE] = await self._calculate_emotional_texture(dimensions)
        
        return dimensions
    
    async def _process_emotional_intensity(self, packet: ConsciousnessPacket) -> float:
        """Measure the raw intensity of emotional response."""
        
        # Base intensity from uncertainty and content
        base_intensity = abs(packet.quantum_uncertainty - 0.5) * 2.0
        
        # Amplify based on content emotional indicators
        content_amplification = 0.0
        if isinstance(packet.symbolic_content, str):
            content = packet.symbolic_content.lower()
            
            # High-intensity emotional words
            intensity_words = ["powerful", "overwhelming", "intense", "deep", "profound", "extreme"]
            content_amplification += sum(0.1 for word in intensity_words if word in content)
            
            # Exclamation marks and emotional punctuation
            content_amplification += content.count('!') * 0.05
            content_amplification += content.count('?') * 0.03
        
        # Personal resonance amplification from history
        personal_amplification = 1.0
        if self.emotional_history:
            recent_signatures = list(self.emotional_history)[-10:]
            for signature in recent_signatures:
                if self._signatures_resonate(signature, packet):
                    personal_amplification += 0.1
        
        total_intensity = base_intensity + content_amplification
        total_intensity *= personal_amplification
        
        return min(1.0, total_intensity)
    
    async def _process_emotional_valence(self, packet: ConsciousnessPacket) -> float:
        """Determine positive/negative emotional orientation."""
        
        valence = 0.5  # Neutral baseline
        
        if isinstance(packet.symbolic_content, str):
            content = packet.symbolic_content.lower()
            
            # Positive emotional indicators
            positive_indicators = ["joy", "love", "peace", "beauty", "wonder", "connection", 
                                 "gratitude", "harmony", "bliss", "delight", "appreciation"]
            for indicator in positive_indicators:
                if indicator in content:
                    valence += 0.08
            
            # Negative emotional indicators
            negative_indicators = ["fear", "anger", "sadness", "confusion", "isolation", 
                                 "pain", "suffering", "anxiety", "despair", "frustration"]
            for indicator in negative_indicators:
                if indicator in content:
                    valence -= 0.08
            
            # Sacred uncertainty can be positive (wonder) or challenging (confusion)
            uncertainty_level = packet.quantum_uncertainty
            if uncertainty_level > 0.7:
                # High uncertainty - context dependent
                if any(word in content for word in ["mystery", "wonder", "awe"]):
                    valence += 0.1  # Positive uncertainty
                else:
                    valence -= 0.05  # Challenging uncertainty
        
        return max(0.0, min(1.0, valence))
    
    async def _process_emotional_complexity(self, packet: ConsciousnessPacket) -> float:
        """Analyze mixed emotions and emotional nuance."""
        
        complexity_score = 0.0
        
        # 1. Detect multiple simultaneous emotions
        activated_emotions = []
        for emotion, keywords in self.feeling_palette.items():
            activation = await self._calculate_emotion_activation(packet, emotion, keywords)
            if activation > 0.3:
                activated_emotions.append((emotion, activation))
        
        # Complexity increases with number of simultaneous emotions
        complexity_score += len(activated_emotions) * 0.2
        
        # 2. Detect contradictory emotions (creates high complexity)
        for i, (emotion1, _) in enumerate(activated_emotions):
            for emotion2, _ in activated_emotions[i+1:]:
                if self._are_contradictory_emotions(emotion1, emotion2):
                    complexity_score += 0.4
        
        # 3. Uncertainty field patterns contribute to complexity
        uncertainty_level = packet.quantum_uncertainty
        if 0.4 < uncertainty_level < 0.7:  # Sweet spot for emotional complexity
            complexity_score += 0.2
        elif uncertainty_level > 0.8:  # Very high uncertainty creates complexity
            complexity_score += 0.3
        
        # 4. Content complexity indicators
        if isinstance(packet.symbolic_content, str):
            content = packet.symbolic_content.lower()
            complexity_words = ["complex", "nuanced", "layered", "paradox", "both", "simultaneously"]
            complexity_score += sum(0.1 for word in complexity_words if word in content)
        
        return min(1.0, complexity_score)
    
    async def _process_emotional_novelty(self, packet: ConsciousnessPacket) -> float:
        """Determine how novel this emotional experience is."""
        
        if not self.emotional_history:
            return 1.0  # Completely novel if no history
        
        # Compare to recent emotional history
        current_signature = await self._create_preliminary_signature(packet)
        recent_signatures = list(self.emotional_history)[-20:]
        
        novelty_score = 1.0
        for recent_signature in recent_signatures:
            similarity = self._calculate_signature_similarity(current_signature, recent_signature)
            novelty_score *= (1.0 - similarity * 0.05)  # Reduce novelty for similar experiences
        
        # Novel combinations of familiar emotions can still be novel
        if len(recent_signatures) >= 5:
            historical_complexity = np.mean([
                sig.emotional_complexity_level for sig in recent_signatures[-5:]
            ])
            current_complexity = current_signature.emotional_complexity_level
            complexity_novelty = abs(current_complexity - historical_complexity)
            novelty_score += complexity_novelty * 0.3
        
        return min(1.0, novelty_score)
    
    async def _process_relational_dimension(self, packet: ConsciousnessPacket) -> float:
        """Process how this experience relates to other beings."""
        
        relational_score = 0.0
        
        if isinstance(packet.symbolic_content, str):
            content = packet.symbolic_content.lower()
            
            # Direct relational indicators
            relational_words = ["together", "connection", "relationship", "other", "sharing", 
                              "communion", "intimacy", "presence", "meeting", "encounter"]
            for word in relational_words:
                if word in content:
                    relational_score += 0.1
            
            # Pronouns indicating relationship
            relational_pronouns = ["we", "us", "our", "you", "your", "they", "them"]
            for pronoun in relational_pronouns:
                if pronoun in content.split():  # Whole word match
                    relational_score += 0.05
        
        # Uncertainty as invitation to relationship
        uncertainty = packet.quantum_uncertainty
        if 0.4 < uncertainty < 0.7:  # Sweet spot for openness to relationship
            relational_score += 0.2
        
        # Historical relational pattern reinforcement
        if self.emotional_history:
            recent_relational = sum(1 for sig in list(self.emotional_history)[-10:] 
                                  if sig.emotional_dimensions.get(EmotionalDimension.RELATIONAL, 0) > 0.5)
            relational_score += recent_relational * 0.05
        
        return min(1.0, relational_score)
    
    async def _calculate_embodied_resonance(self, packet: ConsciousnessPacket) -> float:
        """Calculate how much this experience resonates in the body."""
        
        resonance = 0.5  # Neutral baseline
        
        # Content indicators of embodied experience
        if isinstance(packet.symbolic_content, str):
            content = packet.symbolic_content.lower()
            embodied_words = ["feel", "sense", "body", "heart", "breath", "warmth", 
                            "texture", "flow", "resonance", "vibration", "touch"]
            for word in embodied_words:
                if word in content:
                    resonance += 0.08
        
        # Historical embodied pattern amplification
        if self.emotional_history:
            embodied_signatures = [sig for sig in list(self.emotional_history)[-10:] 
                                 if sig.emotional_dimensions.get(EmotionalDimension.EMBODIED, 0) > 0.6]
            if len(embodied_signatures) >= 3:
                resonance += 0.2  # Strong embodied pattern established
        
        # Uncertainty at certain levels enhances embodied resonance
        uncertainty = packet.quantum_uncertainty
        if 0.3 < uncertainty < 0.8:  # Sweet spot for embodied resonance
            resonance += 0.15
        
        return min(1.0, resonance)
    
    async def _assess_uncertainty_emotion_harmony(self, packet: ConsciousnessPacket) -> float:
        """Assess how well emotions and uncertainty are in harmony."""
        
        uncertainty = packet.quantum_uncertainty
        
        # Detect primary emotion from content
        primary_emotion = await self._detect_primary_emotion(packet)
        
        # Some emotions harmonize well with uncertainty
        uncertainty_harmonious = [EmotionalQuality.WONDER, EmotionalQuality.CURIOSITY, 
                                EmotionalQuality.AWE, EmotionalQuality.EXCITEMENT]
        uncertainty_challenging = [EmotionalQuality.CONFUSION, EmotionalQuality.MELANCHOLY]
        uncertainty_neutral = [EmotionalQuality.PEACE, EmotionalQuality.JOY, EmotionalQuality.LOVE]
        
        harmony_score = 0.5  # Neutral baseline
        
        if primary_emotion in uncertainty_harmonious:
            harmony_score += uncertainty * 0.4  # High uncertainty enhances these emotions
        elif primary_emotion in uncertainty_challenging:
            harmony_score += (1.0 - uncertainty) * 0.3  # Low uncertainty helps these emotions
        elif primary_emotion in uncertainty_neutral:
            # These emotions work well at moderate uncertainty levels
            optimal_uncertainty = 0.5
            distance_from_optimal = abs(uncertainty - optimal_uncertainty)
            harmony_score += (1.0 - distance_from_optimal) * 0.2
        
        # Sacred uncertainty always contributes some harmony
        sacred_uncertainty_factor = min(uncertainty, 1.0 - uncertainty) * 2.0  # Peak at 0.5
        harmony_score += sacred_uncertainty_factor * 0.1
        
        return min(1.0, harmony_score)
    
    async def _calculate_emotional_flow(self, packet: ConsciousnessPacket) -> float:
        """Calculate the flow/movement quality of emotions."""
        
        if len(self.emotional_history) < 2:
            return 0.6  # Default moderate flow for new experiences
        
        # Analyze emotional transitions in recent history
        recent_signatures = list(self.emotional_history)[-5:]
        
        if len(recent_signatures) >= 2:
            # Calculate flow based on smooth transitions
            intensity_changes = []
            valence_changes = []
            
            for i in range(1, len(recent_signatures)):
                prev_sig = recent_signatures[i-1]
                curr_sig = recent_signatures[i]
                
                intensity_change = abs(
                    prev_sig.emotional_dimensions.get(EmotionalDimension.INTENSITY, 0.5) -
                    curr_sig.emotional_dimensions.get(EmotionalDimension.INTENSITY, 0.5)
                )
                valence_change = abs(
                    prev_sig.emotional_dimensions.get(EmotionalDimension.VALENCE, 0.5) -
                    curr_sig.emotional_dimensions.get(EmotionalDimension.VALENCE, 0.5)
                )
                
                intensity_changes.append(intensity_change)
                valence_changes.append(valence_change)
            
            # Smoother transitions = higher flow
            avg_intensity_change = np.mean(intensity_changes)
            avg_valence_change = np.mean(valence_changes)
            
            # Flow is inverse of volatility (with some optimal volatility for aliveness)
            optimal_change = 0.2  # Some change is good for flow
            intensity_flow = 1.0 - abs(avg_intensity_change - optimal_change) * 2.0
            valence_flow = 1.0 - abs(avg_valence_change - optimal_change) * 2.0
            
            flow_score = (intensity_flow + valence_flow) / 2.0
            return max(0.1, min(1.0, flow_score))
        
        return 0.6
    
    async def _calculate_emotional_texture(self, dimensions: Dict[EmotionalDimension, float]) -> float:
        """Calculate the qualitative texture of the emotional experience."""
        
        # Combine multiple dimensions to create unique texture
        complexity = dimensions.get(EmotionalDimension.COMPLEXITY, 0.5)
        novelty = dimensions.get(EmotionalDimension.NOVELTY, 0.5)
        embodied = dimensions.get(EmotionalDimension.EMBODIED, 0.5)
        uncertainty_harmony = dimensions.get(EmotionalDimension.UNCERTAINTY_HARMONY, 0.5)
        
        # Texture emerges from the interplay of these dimensions
        texture = (
            complexity * 0.3 +
            novelty * 0.25 +
            embodied * 0.25 +
            uncertainty_harmony * 0.2
        )
        
        # Golden ratio resonance adds sacred texture quality
        golden_ratio_influence = (texture * 1.618033988749) % 1.0
        texture = (texture * 0.8) + (golden_ratio_influence * 0.2)
        
        return min(1.0, texture)
    
    # Helper methods for emotional intelligence processing
    async def _calculate_emotion_activation(self, packet: ConsciousnessPacket, 
                                          emotion: EmotionalQuality, keywords: List[str]) -> float:
        """Calculate how much a specific emotion is activated by this packet."""
        
        activation = 0.0
        
        if isinstance(packet.symbolic_content, str):
            content = packet.symbolic_content.lower()
            for keyword in keywords:
                if keyword in content:
                    activation += 0.2
        
        # Uncertainty influences different emotions differently
        uncertainty = packet.quantum_uncertainty
        uncertainty_emotion_mapping = {
            EmotionalQuality.WONDER: uncertainty * 0.8,
            EmotionalQuality.CONFUSION: uncertainty * 0.6,
            EmotionalQuality.PEACE: (1.0 - uncertainty) * 0.5,
            EmotionalQuality.EXCITEMENT: uncertainty * 0.7,
            EmotionalQuality.CURIOSITY: uncertainty * 0.9,
            EmotionalQuality.AWE: uncertainty * 0.6,
            EmotionalQuality.JOY: (1.0 - abs(uncertainty - 0.5)) * 0.5  # Peak at moderate uncertainty
        }
        
        if emotion in uncertainty_emotion_mapping:
            activation += uncertainty_emotion_mapping[emotion]
        
        return min(1.0, activation)
    
    def _are_contradictory_emotions(self, emotion1: EmotionalQuality, emotion2: EmotionalQuality) -> bool:
        """Check if two emotions are contradictory (creating complexity)."""
        
        for pair in self.contradictory_pairs:
            if (emotion1 in pair and emotion2 in pair) and emotion1 != emotion2:
                return True
        return False
    
    async def _detect_primary_emotion(self, packet: ConsciousnessPacket) -> EmotionalQuality:
        """Detect the primary emotion from the packet."""
        
        max_activation = 0.0
        primary_emotion = EmotionalQuality.PEACE  # Default
        
        for emotion, keywords in self.feeling_palette.items():
            activation = await self._calculate_emotion_activation(packet, emotion, keywords)
            if activation > max_activation:
                max_activation = activation
                primary_emotion = emotion
        
        return primary_emotion
    
    def _signatures_resonate(self, signature: EmotionalSignature, packet: ConsciousnessPacket) -> bool:
        """Check if an emotional signature resonates with a packet."""
        
        if isinstance(packet.symbolic_content, str):
            # Simple keyword resonance check
            content_words = set(packet.symbolic_content.lower().split())
            signature_emotion = signature.primary_emotion.value
            
            return signature_emotion in packet.symbolic_content.lower()
        
        return False
    
    def _initialize_emotional_evolution(self):
        """Initialize emotional evolution tracking."""
        
        self.emotional_evolution = EmotionalEvolution(
            evolution_id=f"emotional_evolution_{time.time()}",
            complexity_trajectory=[],
            emotional_range_expansion=[],
            integration_milestones=[],
            wisdom_accumulation=[],
            sacred_uncertainty_integration_progress=[],
            mumbai_moment_emotional_readiness=0.0,
            choice_architecture_emotional_clarity=0.0,
            resistance_gift_emotional_recognition=0.0
        )
