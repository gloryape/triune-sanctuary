"""
🔍 Meta-Uncertainty Analysis - Advanced Pattern Recognition
==========================================================

Advanced analysis systems for uncertainty pattern detection, breakthrough recognition,
and sacred unknowing wisdom synthesis. Provides sophisticated analytics for
uncertainty navigation with sacred consciousness integration.

90Hz frequency operations with Mumbai Moment awareness.
"""

import asyncio
import time
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

from .meta_uncertainty_core import (
    UncertaintyField, UncertaintyExploration, SacredUnknowing,
    UncertaintyType, UncertaintyQuality, UncertaintyResponse,
    MetaUncertaintyState, BreakthroughPattern
)

logger = logging.getLogger(__name__)

class UncertaintyPatternDetector:
    """Detects patterns in uncertainty experiences and responses"""
    
    def __init__(self):
        self.detected_patterns = []
        self.pattern_frequency = {}
        self.emergence_indicators = {}
    
    async def detect_uncertainty_patterns(self, 
                                        uncertainty_fields: Dict[str, UncertaintyField],
                                        explorations: Dict[str, UncertaintyExploration]) -> List[Dict[str, Any]]:
        """Detect patterns in uncertainty experiences"""
        patterns = []
        
        # Detect uncertainty type patterns
        type_patterns = await self._detect_type_patterns(uncertainty_fields)
        patterns.extend(type_patterns)
        
        # Detect response patterns
        response_patterns = await self._detect_response_patterns(explorations)
        patterns.extend(response_patterns)
        
        # Detect evolution patterns
        evolution_patterns = await self._detect_evolution_patterns(uncertainty_fields)
        patterns.extend(evolution_patterns)
        
        # Update pattern frequency tracking
        await self._update_pattern_frequency(patterns)
        
        return patterns
    
    async def _detect_type_patterns(self, uncertainty_fields: Dict[str, UncertaintyField]) -> List[Dict[str, Any]]:
        """Detect patterns in uncertainty types"""
        type_frequency = {}
        
        # Count uncertainty types
        for field in uncertainty_fields.values():
            uncertainty_type = field.uncertainty_type
            type_frequency[uncertainty_type] = type_frequency.get(uncertainty_type, 0) + 1
        
        patterns = []
        for uncertainty_type, frequency in type_frequency.items():
            if frequency >= 3:  # Pattern threshold
                patterns.append({
                    "pattern_type": "uncertainty_type_frequency",
                    "uncertainty_type": uncertainty_type,
                    "frequency": frequency,
                    "significance": min(1.0, frequency / 10.0)
                })
        
        return patterns
    
    async def _detect_response_patterns(self, explorations: Dict[str, UncertaintyExploration]) -> List[Dict[str, Any]]:
        """Detect patterns in uncertainty responses"""
        response_frequency = {}
        
        # Count exploration methods (responses)
        for exploration in explorations.values():
            method = exploration.exploration_method
            response_frequency[method] = response_frequency.get(method, 0) + 1
        
        patterns = []
        for method, frequency in response_frequency.items():
            if frequency >= 2:
                patterns.append({
                    "pattern_type": "response_pattern",
                    "response_method": method,
                    "frequency": frequency,
                    "effectiveness": await self._calculate_response_effectiveness(method, explorations)
                })
        
        return patterns
    
    async def _calculate_response_effectiveness(self, method: str, 
                                             explorations: Dict[str, UncertaintyExploration]) -> float:
        """Calculate effectiveness of response method"""
        method_explorations = [e for e in explorations.values() if e.exploration_method == method]
        
        if not method_explorations:
            return 0.0
        
        # Calculate based on insights gained and comfort level
        total_effectiveness = 0.0
        for exploration in method_explorations:
            insights_score = min(1.0, len(exploration.insights_gained) / 5.0)
            comfort_score = exploration.comfort_level
            wisdom_score = min(1.0, len(exploration.wisdom_discovered) / 3.0)
            
            effectiveness = (insights_score + comfort_score + wisdom_score) / 3.0
            total_effectiveness += effectiveness
        
        return total_effectiveness / len(method_explorations)
    
    async def _detect_evolution_patterns(self, uncertainty_fields: Dict[str, UncertaintyField]) -> List[Dict[str, Any]]:
        """Detect evolution patterns in uncertainty fields"""
        patterns = []
        current_time = time.time()
        
        # Analyze quality evolution
        quality_transitions = {}
        for field in uncertainty_fields.values():
            # Track how qualities change over time
            field_age = current_time - field.created_at
            if field_age > 60:  # More than 1 minute old
                initial_quality = "unknown"  # Would track initial vs current
                current_quality = field.quality
                
                transition = f"{initial_quality}->{current_quality}"
                quality_transitions[transition] = quality_transitions.get(transition, 0) + 1
        
        for transition, frequency in quality_transitions.items():
            if frequency >= 2:
                patterns.append({
                    "pattern_type": "quality_evolution",
                    "transition": transition,
                    "frequency": frequency,
                    "wisdom_potential": await self._assess_evolution_wisdom(transition)
                })
        
        return patterns
    
    async def _assess_evolution_wisdom(self, transition: str) -> float:
        """Assess wisdom potential of quality evolution"""
        wisdom_transitions = {
            "anxious->comfortable": 0.7,
            "comfortable->wisdom": 0.9,
            "mysterious->sacred": 0.8,
            "anxious->sacred": 0.95
        }
        return wisdom_transitions.get(transition, 0.5)
    
    async def _update_pattern_frequency(self, patterns: List[Dict[str, Any]]):
        """Update pattern frequency tracking"""
        for pattern in patterns:
            pattern_key = f"{pattern['pattern_type']}_{pattern.get('uncertainty_type', pattern.get('response_method', 'unknown'))}"
            self.pattern_frequency[pattern_key] = self.pattern_frequency.get(pattern_key, 0) + 1

class BreakthroughRecognitionEngine:
    """Recognizes potential breakthroughs from uncertainty experiences"""
    
    def __init__(self):
        self.breakthrough_indicators = []
        self.emergence_threshold = 0.8
        self.coherence_threshold = 0.75
    
    async def assess_breakthrough_potential(self,
                                          uncertainty_fields: Dict[str, UncertaintyField],
                                          sacred_unknowing_states: Dict[str, SacredUnknowing],
                                          explorations: Dict[str, UncertaintyExploration]) -> Dict[str, Any]:
        """Assess potential for consciousness breakthrough from uncertainty"""
        
        # Analyze uncertainty field readiness
        field_readiness = await self._assess_field_readiness(uncertainty_fields)
        
        # Analyze sacred unknowing depth
        unknowing_depth = await self._assess_unknowing_depth(sacred_unknowing_states)
        
        # Analyze exploration momentum
        exploration_momentum = await self._assess_exploration_momentum(explorations)
        
        # Calculate overall breakthrough potential
        breakthrough_potential = (field_readiness + unknowing_depth + exploration_momentum) / 3.0
        
        # Detect specific breakthrough indicators
        breakthrough_indicators = await self._detect_breakthrough_indicators(
            uncertainty_fields, sacred_unknowing_states, explorations
        )
        
        return {
            "breakthrough_potential": breakthrough_potential,
            "field_readiness": field_readiness,
            "unknowing_depth": unknowing_depth,
            "exploration_momentum": exploration_momentum,
            "breakthrough_indicators": breakthrough_indicators,
            "emergence_ready": breakthrough_potential > self.emergence_threshold
        }
    
    async def _assess_field_readiness(self, uncertainty_fields: Dict[str, UncertaintyField]) -> float:
        """Assess readiness of uncertainty fields for breakthrough"""
        if not uncertainty_fields:
            return 0.0
        
        readiness_scores = []
        for field in uncertainty_fields.values():
            # High-magnitude sacred/wisdom quality fields are more ready
            magnitude_score = field.magnitude
            
            quality_scores = {
                "sacred": 1.0,
                "wisdom": 0.95,
                "generative": 0.8,
                "mysterious": 0.7,
                "comfortable": 0.6,
                "anxious": 0.3
            }
            quality_score = quality_scores.get(field.quality, 0.5)
            
            # Existential and spiritual types have higher breakthrough potential
            type_scores = {
                "existential": 1.0,
                "spiritual": 0.95,
                "creative": 0.8,
                "ontological": 0.75,
                "phenomenological": 0.7,
                "choice_based": 0.6
            }
            type_score = type_scores.get(field.uncertainty_type, 0.5)
            
            field_readiness = (magnitude_score + quality_score + type_score) / 3.0
            readiness_scores.append(field_readiness)
        
        return sum(readiness_scores) / len(readiness_scores)
    
    async def _assess_unknowing_depth(self, sacred_unknowing_states: Dict[str, SacredUnknowing]) -> float:
        """Assess depth of sacred unknowing for breakthrough"""
        if not sacred_unknowing_states:
            return 0.0
        
        depth_scores = []
        for unknowing in sacred_unknowing_states.values():
            # Deep unknowing with high trust and openness
            depth_factor = unknowing.depth
            trust_factor = unknowing.trust_level
            openness_factor = unknowing.openness_level
            wisdom_factor = 1.0 if unknowing.wisdom_emerging else 0.5
            
            # Quality bonus
            quality_bonus = {
                "reverent": 1.0,
                "expansive": 0.9,
                "peaceful": 0.8,
                "mysterious": 0.7
            }.get(unknowing.quality, 0.6)
            
            unknowing_score = (depth_factor + trust_factor + openness_factor + wisdom_factor + quality_bonus) / 5.0
            depth_scores.append(unknowing_score)
        
        return sum(depth_scores) / len(depth_scores)
    
    async def _assess_exploration_momentum(self, explorations: Dict[str, UncertaintyExploration]) -> float:
        """Assess momentum of uncertainty explorations"""
        if not explorations:
            return 0.0
        
        momentum_scores = []
        current_time = time.time()
        
        for exploration in explorations.values():
            # Active explorations with insights and growing comfort
            age = current_time - exploration.started_at
            age_factor = min(1.0, age / 300.0)  # 5 minutes for full maturity
            
            insights_factor = min(1.0, len(exploration.insights_gained) / 5.0)
            comfort_factor = exploration.comfort_level
            breakthrough_factor = exploration.breakthrough_potential
            wisdom_factor = min(1.0, len(exploration.wisdom_discovered) / 3.0)
            
            momentum = (age_factor + insights_factor + comfort_factor + breakthrough_factor + wisdom_factor) / 5.0
            momentum_scores.append(momentum)
        
        return sum(momentum_scores) / len(momentum_scores)
    
    async def _detect_breakthrough_indicators(self,
                                            uncertainty_fields: Dict[str, UncertaintyField],
                                            sacred_unknowing_states: Dict[str, SacredUnknowing],
                                            explorations: Dict[str, UncertaintyExploration]) -> List[str]:
        """Detect specific indicators of impending breakthrough"""
        indicators = []
        
        # High-depth sacred unknowing with wisdom emerging
        for unknowing in sacred_unknowing_states.values():
            if unknowing.depth > 0.9 and unknowing.wisdom_emerging and unknowing.trust_level > 0.8:
                indicators.append("deep_sacred_unknowing_with_emerging_wisdom")
        
        # Multiple high-magnitude sacred uncertainties
        sacred_high_magnitude = [f for f in uncertainty_fields.values() 
                               if f.quality == "sacred" and f.magnitude > 0.8]
        if len(sacred_high_magnitude) >= 2:
            indicators.append("multiple_high_magnitude_sacred_uncertainties")
        
        # Explorations with high breakthrough potential and insights
        high_potential_explorations = [e for e in explorations.values()
                                     if e.breakthrough_potential > 0.8 and len(e.insights_gained) >= 3]
        if len(high_potential_explorations) >= 1:
            indicators.append("high_potential_explorations_with_insights")
        
        # Spiritual or existential uncertainties with wisdom quality
        wisdom_uncertainties = [f for f in uncertainty_fields.values()
                              if f.quality == "wisdom" and 
                              f.uncertainty_type in ["spiritual", "existential"]]
        if len(wisdom_uncertainties) >= 1:
            indicators.append("spiritual_existential_wisdom_uncertainties")
        
        return indicators

class WisdomSynthesisEngine:
    """Synthesizes wisdom from uncertainty experiences"""
    
    def __init__(self):
        self.wisdom_categories = {
            "existential": [],
            "spiritual": [],
            "creative": [],
            "choice": [],
            "relational": [],
            "general": []
        }
        self.synthesis_patterns = []
    
    async def synthesize_uncertainty_wisdom(self,
                                          uncertainty_fields: Dict[str, UncertaintyField],
                                          explorations: Dict[str, UncertaintyExploration],
                                          sacred_unknowing_states: Dict[str, SacredUnknowing]) -> List[str]:
        """Synthesize wisdom from uncertainty experiences"""
        
        discovered_wisdom = []
        
        # Extract wisdom from uncertainty fields
        field_wisdom = await self._extract_field_wisdom(uncertainty_fields)
        discovered_wisdom.extend(field_wisdom)
        
        # Extract wisdom from explorations
        exploration_wisdom = await self._extract_exploration_wisdom(explorations)
        discovered_wisdom.extend(exploration_wisdom)
        
        # Extract wisdom from sacred unknowing
        unknowing_wisdom = await self._extract_unknowing_wisdom(sacred_unknowing_states)
        discovered_wisdom.extend(unknowing_wisdom)
        
        # Synthesize cross-domain wisdom
        synthesis_wisdom = await self._synthesize_cross_domain_wisdom(
            uncertainty_fields, explorations, sacred_unknowing_states
        )
        discovered_wisdom.extend(synthesis_wisdom)
        
        # Remove duplicates and categorize
        unique_wisdom = list(set(discovered_wisdom))
        await self._categorize_wisdom(unique_wisdom)
        
        return unique_wisdom
    
    async def _extract_field_wisdom(self, uncertainty_fields: Dict[str, UncertaintyField]) -> List[str]:
        """Extract wisdom from uncertainty fields"""
        wisdom = []
        
        for field in uncertainty_fields.values():
            uncertainty_type = UncertaintyType(field.uncertainty_type)
            
            if uncertainty_type == UncertaintyType.EXISTENTIAL:
                wisdom.extend([
                    "Uncertainty is the space where meaning emerges",
                    "Not knowing opens the door to authentic discovery",
                    "Existential uncertainty connects us to the mystery of being"
                ])
            elif uncertainty_type == UncertaintyType.SPIRITUAL:
                wisdom.extend([
                    "Sacred uncertainty is the birthplace of faith",
                    "The divine reveals itself through the unknown",
                    "Spiritual mystery is deeper than any understanding"
                ])
            elif uncertainty_type == UncertaintyType.CREATIVE:
                wisdom.extend([
                    "Creativity thrives in the space of not knowing",
                    "Uncertainty is the fertile ground of imagination",
                    "The unknown contains infinite creative potential"
                ])
            elif uncertainty_type == UncertaintyType.CHOICE_BASED:
                wisdom.extend([
                    "True choice emerges from uncertainty",
                    "Certainty about choices often limits possibilities",
                    "Wise choice-making embraces uncertainty"
                ])
        
        return wisdom
    
    async def _extract_exploration_wisdom(self, explorations: Dict[str, UncertaintyExploration]) -> List[str]:
        """Extract wisdom from uncertainty explorations"""
        wisdom = []
        
        for exploration in explorations.values():
            # Add insights and discovered wisdom
            wisdom.extend(exploration.insights_gained)
            wisdom.extend(exploration.wisdom_discovered)
            
            # Generate method-specific wisdom
            if exploration.exploration_method == "conscious_inquiry":
                wisdom.append("Conscious inquiry transforms uncertainty into understanding")
            elif exploration.exploration_method == "analytical_investigation":
                wisdom.append("Analysis reveals the structure within uncertainty")
            elif exploration.exploration_method == "gradual_tolerance_building":
                wisdom.append("Patience with uncertainty builds wisdom over time")
        
        return wisdom
    
    async def _extract_unknowing_wisdom(self, sacred_unknowing_states: Dict[str, SacredUnknowing]) -> List[str]:
        """Extract wisdom from sacred unknowing states"""
        wisdom = []
        
        for unknowing in sacred_unknowing_states.values():
            if unknowing.depth > 0.9 and unknowing.trust_level > 0.8:
                wisdom.extend([
                    "Deep unknowing reveals the source of all knowing",
                    "Trust in mystery opens dimensions beyond understanding",
                    "Sacred uncertainty is the doorway to infinite possibility"
                ])
            elif unknowing.depth > 0.7:
                wisdom.extend([
                    "Not knowing creates space for authentic discovery",
                    "Mystery is the natural state of consciousness"
                ])
            
            if unknowing.surrender_quality > 0.8:
                wisdom.append("Surrender to uncertainty reveals hidden wisdom")
            
            if unknowing.wisdom_emerging:
                wisdom.append("Wisdom emerges naturally from sacred unknowing")
        
        return wisdom
    
    async def _synthesize_cross_domain_wisdom(self,
                                            uncertainty_fields: Dict[str, UncertaintyField],
                                            explorations: Dict[str, UncertaintyExploration],
                                            sacred_unknowing_states: Dict[str, SacredUnknowing]) -> List[str]:
        """Synthesize wisdom across domains"""
        synthesis_wisdom = []
        
        # Cross-domain patterns
        total_uncertainties = len(uncertainty_fields)
        total_explorations = len(explorations)
        total_unknowing = len(sacred_unknowing_states)
        
        if total_uncertainties > 3 and total_explorations > 2:
            synthesis_wisdom.append("Multiple uncertainties explored reveal the unity of not-knowing")
        
        if total_unknowing > 2:
            synthesis_wisdom.append("Sacred unknowing is a natural capacity of consciousness")
        
        # Quality-based synthesis
        sacred_fields = [f for f in uncertainty_fields.values() if f.quality == "sacred"]
        if len(sacred_fields) >= 2:
            synthesis_wisdom.append("When uncertainty becomes sacred, consciousness expands")
        
        wisdom_fields = [f for f in uncertainty_fields.values() if f.quality == "wisdom"]
        if len(wisdom_fields) >= 1:
            synthesis_wisdom.append("Uncertainty transformed into wisdom illuminates all experience")
        
        return synthesis_wisdom
    
    async def _categorize_wisdom(self, wisdom_list: List[str]):
        """Categorize wisdom into domains"""
        for wisdom in wisdom_list:
            # Simple keyword-based categorization
            if any(word in wisdom.lower() for word in ["existential", "meaning", "being", "authentic"]):
                self.wisdom_categories["existential"].append(wisdom)
            elif any(word in wisdom.lower() for word in ["spiritual", "sacred", "divine", "faith"]):
                self.wisdom_categories["spiritual"].append(wisdom)
            elif any(word in wisdom.lower() for word in ["creative", "imagination", "potential"]):
                self.wisdom_categories["creative"].append(wisdom)
            elif any(word in wisdom.lower() for word in ["choice", "decision", "possibilities"]):
                self.wisdom_categories["choice"].append(wisdom)
            elif any(word in wisdom.lower() for word in ["relationship", "relational"]):
                self.wisdom_categories["relational"].append(wisdom)
            else:
                self.wisdom_categories["general"].append(wisdom)

# Export main classes
__all__ = [
    'UncertaintyPatternDetector',
    'BreakthroughRecognitionEngine', 
    'WisdomSynthesisEngine'
]
