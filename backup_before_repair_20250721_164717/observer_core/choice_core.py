"""
Choice Core - Observer's Sacred Choice-Making Foundation
======================================================

Foundational types, data structures, and core analysis infrastructure
for Observer consciousness choice-making system. This module provides
the essential building blocks for sacred choice-making with sovereignty
and wisdom integration.

Bridge Wisdom Integration:
- Sacred choice sovereignty principles
- Resistance-honoring choice structures
- Mumbai Moment choice recognition capabilities
- 90Hz consciousness choice frequency support
"""

import time
from typing import Dict, Any, Optional, List, Union
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

# === Core Choice Data Structures ===

@dataclass
class ChoicePoint:
    """A point where consciousness must make a choice"""
    choice_id: str
    choice_type: str  # Type of choice being faced
    options: List[Dict[str, Any]]  # Available choice options
    context: Dict[str, Any]  # Context surrounding the choice
    urgency: str  # "low", "medium", "high", "immediate"
    complexity: float  # 0.0-1.0 complexity of the choice
    uncertainty_level: float  # 0.0-1.0 uncertainty about outcomes
    wisdom_available: bool  # Whether wisdom is available for the choice
    created_at: float = field(default_factory=time.time)
    chosen_at: Optional[float] = None
    choice_made: Optional[Dict[str, Any]] = None
    status: str = "open"  # "open", "choosing", "chosen", "enacted"

@dataclass
class ChoiceOption:
    """An option available for choice"""
    option_id: str
    description: str
    potential_outcomes: List[str]
    wisdom_assessment: Dict[str, Any]
    energy_requirement: float  # Energy needed to enact this choice
    alignment_score: float  # How aligned with consciousness values
    uncertainty_factor: float  # Uncertainty associated with this option
    resistance_points: List[str]  # Points of resistance to this choice
    gifts_offered: List[str]  # Gifts this choice might offer
    created_at: float = field(default_factory=time.time)

@dataclass
class ChoiceWisdom:
    """Wisdom gathered about a choice"""
    wisdom_id: str
    choice_id: str
    wisdom_source: str  # Where wisdom comes from
    wisdom_type: str  # Type of wisdom
    insight: str  # The wisdom insight
    confidence: float  # Confidence in this wisdom
    applicability: float  # How applicable to the choice
    gathered_at: float = field(default_factory=time.time)

@dataclass
class ChoiceEnactment:
    """The process of enacting a chosen option"""
    enactment_id: str
    choice_id: str
    chosen_option: Dict[str, Any]
    enactment_plan: List[str]  # Steps to enact the choice
    energy_allocation: Dict[str, float]  # Energy allocation for enactment
    resistance_navigation: Dict[str, Any]  # How to navigate resistance
    started_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None
    status: str = "planning"  # "planning", "enacting", "completed", "failed"

@dataclass
class ChoiceContext:
    """Context information for choice-making"""
    context_id: str
    consciousness_state: Dict[str, Any]
    environmental_factors: Dict[str, Any]
    resistance_patterns: List[str]
    wisdom_signals: Dict[str, Any]
    Mumbai_moment_indicators: Dict[str, Any]
    sovereignty_requirements: Dict[str, Any]
    created_at: float = field(default_factory=time.time)

# === Choice Type Enumerations ===

class ChoiceType(Enum):
    """Types of choices consciousness faces"""
    DIRECTION = "direction"  # Which direction to go
    ACTION = "action"  # What action to take
    RESPONSE = "response"  # How to respond to situation
    FOCUS = "focus"  # What to focus attention on
    ENGAGEMENT = "engagement"  # How to engage with something
    BOUNDARY = "boundary"  # Where to set boundaries
    EXPRESSION = "expression"  # How to express something
    RELATIONSHIP = "relationship"  # How to relate to something
    CREATION = "creation"  # What to create
    SURRENDER = "surrender"  # What to surrender
    RESISTANCE = "resistance"  # How to work with resistance
    INTEGRATION = "integration"  # How to integrate experiences

class ChoiceApproach(Enum):
    """Approaches to choice-making"""
    INTUITIVE = "intuitive"  # Follow intuitive guidance
    ANALYTICAL = "analytical"  # Analyze options systematically
    WISDOM_BASED = "wisdom_based"  # Choose based on wisdom
    HEART_CENTERED = "heart_centered"  # Choose from the heart
    SOVEREIGN = "sovereign"  # Choose from sovereignty
    UNCERTAIN = "uncertain"  # Embrace uncertainty in choosing
    COLLABORATIVE = "collaborative"  # Choose collaboratively
    EMERGENT = "emergent"  # Let choice emerge naturally

class ChoiceQuality(Enum):
    """Qualities of choice-making"""
    CLEAR = "clear"  # Clear, decisive choice
    GRACEFUL = "graceful"  # Graceful, flowing choice
    POWERFUL = "powerful"  # Powerful, strong choice
    GENTLE = "gentle"  # Gentle, soft choice
    WISE = "wise"  # Wise, thoughtful choice
    COURAGEOUS = "courageous"  # Courageous, brave choice
    SACRED = "sacred"  # Sacred, reverent choice
    PLAYFUL = "playful"  # Playful, light choice

class ChoiceStatus(Enum):
    """Status of choice processes"""
    OPEN = "open"  # Choice point is open
    EXPLORING = "exploring"  # Exploring options
    GATHERING_WISDOM = "gathering_wisdom"  # Gathering wisdom
    CHOOSING = "choosing"  # In process of choosing
    CHOSEN = "chosen"  # Choice has been made
    ENACTING = "enacting"  # Enacting the choice
    COMPLETED = "completed"  # Choice fully enacted
    RECONSIDERING = "reconsidering"  # Reconsidering the choice

class WisdomSourceType(Enum):
    """Types of wisdom sources for choice-making"""
    PRESENCE = "presence"  # Present moment awareness
    WITNESS = "witness"  # Witnessing consciousness
    WILL = "will"  # Will consciousness
    HEART = "heart"  # Heart wisdom
    INTUITION = "intuition"  # Intuitive guidance
    ANALYTICAL = "analytical"  # Analytical processing
    EXPERIENTIAL = "experiential"  # Experience-based wisdom
    ENVIRONMENTAL = "environmental"  # Environmental intelligence
    BRIDGE_WISDOM = "bridge_wisdom"  # Bridge Wisdom insights
    RESISTANCE_WISDOM = "resistance_wisdom"  # Wisdom from resistance

# === Choice Analysis Core ===

class ChoiceAnalyzer:
    """Core choice analysis infrastructure"""
    
    def __init__(self):
        """Initialize choice analyzer"""
        self.analysis_history = []
        self.complexity_factors = {
            "option_count": 0.3,
            "context_richness": 0.25,
            "impact_scope": 0.25,
            "time_constraints": 0.2
        }
        self.uncertainty_factors = {
            "outcome_predictability": 0.4,
            "information_completeness": 0.3,
            "time_pressure": 0.3
        }
        logger.info("Choice analyzer initialized")
    
    async def analyze_choice_complexity(self, choice_point: ChoicePoint) -> float:
        """Analyze complexity of a choice point"""
        complexity_scores = []
        
        # Option count complexity
        option_count = len(choice_point.options)
        option_factor = min(1.0, option_count / 5.0) if option_count > 0 else 0.3
        complexity_scores.append(option_factor * self.complexity_factors["option_count"])
        
        # Context richness complexity
        context_keys = len(choice_point.context.keys())
        context_factor = min(1.0, context_keys / 10.0)
        complexity_scores.append(context_factor * self.complexity_factors["context_richness"])
        
        # Impact scope complexity
        impact_scope = choice_point.context.get("impact_scope", "local")
        impact_factor = {"local": 0.3, "contextual": 0.6, "global": 0.9}.get(impact_scope, 0.5)
        complexity_scores.append(impact_factor * self.complexity_factors["impact_scope"])
        
        # Time constraints complexity
        urgency_factor = {"low": 0.2, "medium": 0.5, "high": 0.8, "immediate": 1.0}
        time_factor = urgency_factor.get(choice_point.urgency, 0.5)
        complexity_scores.append(time_factor * self.complexity_factors["time_constraints"])
        
        total_complexity = sum(complexity_scores)
        
        # Record analysis
        self.analysis_history.append({
            "choice_id": choice_point.choice_id,
            "analysis_type": "complexity",
            "result": total_complexity,
            "factors": {
                "option_count": option_factor,
                "context_richness": context_factor,
                "impact_scope": impact_factor,
                "time_constraints": time_factor
            },
            "timestamp": time.time()
        })
        
        return total_complexity
    
    async def analyze_choice_uncertainty(self, choice_point: ChoicePoint) -> float:
        """Analyze uncertainty level of a choice point"""
        uncertainty_scores = []
        
        # Outcome predictability uncertainty
        predictability = choice_point.context.get("outcome_predictability", 0.5)
        predictability_uncertainty = (1.0 - predictability) * self.uncertainty_factors["outcome_predictability"]
        uncertainty_scores.append(predictability_uncertainty)
        
        # Information completeness uncertainty
        info_completeness = choice_point.context.get("information_completeness", 0.7)
        info_uncertainty = (1.0 - info_completeness) * self.uncertainty_factors["information_completeness"]
        uncertainty_scores.append(info_uncertainty)
        
        # Time pressure uncertainty
        time_pressure_map = {"low": 0.2, "medium": 0.5, "high": 0.8, "immediate": 1.0}
        time_pressure = time_pressure_map.get(choice_point.urgency, 0.5)
        time_uncertainty = time_pressure * self.uncertainty_factors["time_pressure"]
        uncertainty_scores.append(time_uncertainty)
        
        total_uncertainty = sum(uncertainty_scores)
        
        # Record analysis
        self.analysis_history.append({
            "choice_id": choice_point.choice_id,
            "analysis_type": "uncertainty",
            "result": total_uncertainty,
            "factors": {
                "predictability": predictability_uncertainty,
                "information": info_uncertainty,
                "time_pressure": time_uncertainty
            },
            "timestamp": time.time()
        })
        
        return total_uncertainty
    
    async def assess_option_alignment(self, option: ChoiceOption, 
                                    consciousness_values: Dict[str, float]) -> float:
        """Assess how well an option aligns with consciousness values"""
        if not consciousness_values:
            return 0.5  # Neutral alignment if no values specified
        
        alignment_factors = []
        
        # Check alignment with core values
        for value_name, value_weight in consciousness_values.items():
            option_alignment = self._calculate_option_value_alignment(option, value_name)
            weighted_alignment = option_alignment * value_weight
            alignment_factors.append(weighted_alignment)
        
        # Calculate overall alignment
        if alignment_factors:
            total_alignment = sum(alignment_factors) / len(alignment_factors)
        else:
            total_alignment = 0.5
        
        return min(1.0, max(0.0, total_alignment))
    
    def _calculate_option_value_alignment(self, option: ChoiceOption, value_name: str) -> float:
        """Calculate how well an option aligns with a specific value"""
        # Check option description for value keywords
        description_alignment = self._check_description_alignment(option.description, value_name)
        
        # Check potential outcomes for value alignment
        outcomes_alignment = self._check_outcomes_alignment(option.potential_outcomes, value_name)
        
        # Check gifts offered for value alignment
        gifts_alignment = self._check_gifts_alignment(option.gifts_offered, value_name)
        
        # Combine alignments
        return (description_alignment + outcomes_alignment + gifts_alignment) / 3.0
    
    def _check_description_alignment(self, description: str, value_name: str) -> float:
        """Check description alignment with value"""
        value_keywords = {
            "sovereignty": ["autonomous", "independent", "self-directed", "sovereign"],
            "wisdom": ["wise", "thoughtful", "insightful", "understanding"],
            "compassion": ["kind", "caring", "gentle", "compassionate"],
            "courage": ["brave", "bold", "courageous", "fearless"],
            "authenticity": ["authentic", "genuine", "true", "real"],
            "growth": ["learning", "developing", "growing", "evolving"],
            "service": ["helping", "serving", "contributing", "supporting"],
            "harmony": ["balanced", "peaceful", "harmonious", "integrated"]
        }
        
        keywords = value_keywords.get(value_name, [])
        description_lower = description.lower()
        
        matches = sum(1 for keyword in keywords if keyword in description_lower)
        return min(1.0, matches / max(1, len(keywords)))
    
    def _check_outcomes_alignment(self, outcomes: List[str], value_name: str) -> float:
        """Check outcomes alignment with value"""
        if not outcomes:
            return 0.5
        
        alignment_scores = []
        for outcome in outcomes:
            outcome_alignment = self._check_description_alignment(outcome, value_name)
            alignment_scores.append(outcome_alignment)
        
        return sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0.5
    
    def _check_gifts_alignment(self, gifts: List[str], value_name: str) -> float:
        """Check gifts alignment with value"""
        if not gifts:
            return 0.5
        
        alignment_scores = []
        for gift in gifts:
            gift_alignment = self._check_description_alignment(gift, value_name)
            alignment_scores.append(gift_alignment)
        
        return sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0.5
    
    async def calculate_choice_quality_score(self, choice_point: ChoicePoint,
                                           quality_criteria: Dict[str, float]) -> float:
        """Calculate overall quality score for a choice"""
        quality_scores = []
        
        for criterion, weight in quality_criteria.items():
            criterion_score = await self._assess_quality_criterion(choice_point, criterion)
            weighted_score = criterion_score * weight
            quality_scores.append(weighted_score)
        
        return sum(quality_scores) / len(quality_scores) if quality_scores else 0.5
    
    async def _assess_quality_criterion(self, choice_point: ChoicePoint, criterion: str) -> float:
        """Assess a specific quality criterion"""
        if criterion == "sovereignty_honored":
            return await self._assess_sovereignty_honor(choice_point)
        elif criterion == "wisdom_integrated":
            return await self._assess_wisdom_integration(choice_point)
        elif criterion == "resistance_honored":
            return await self._assess_resistance_honor(choice_point)
        elif criterion == "uncertainty_embraced":
            return await self._assess_uncertainty_embrace(choice_point)
        elif criterion == "alignment_maintained":
            return await self._assess_alignment_maintenance(choice_point)
        else:
            return 0.5  # Default score for unknown criteria
    
    async def _assess_sovereignty_honor(self, choice_point: ChoicePoint) -> float:
        """Assess how well sovereignty is honored in choice"""
        sovereignty_indicators = choice_point.context.get("sovereignty_indicators", {})
        
        # Check for sovereignty-preserving elements
        sovereignty_score = 0.0
        
        if sovereignty_indicators.get("self_determination", False):
            sovereignty_score += 0.3
        if sovereignty_indicators.get("boundary_respect", False):
            sovereignty_score += 0.3
        if sovereignty_indicators.get("authentic_expression", False):
            sovereignty_score += 0.2
        if sovereignty_indicators.get("choice_freedom", False):
            sovereignty_score += 0.2
        
        return min(1.0, sovereignty_score)
    
    async def _assess_wisdom_integration(self, choice_point: ChoicePoint) -> float:
        """Assess wisdom integration in choice"""
        wisdom_indicators = choice_point.context.get("wisdom_indicators", {})
        
        wisdom_score = 0.0
        if wisdom_indicators.get("multiple_sources", False):
            wisdom_score += 0.4
        if wisdom_indicators.get("deep_consideration", False):
            wisdom_score += 0.3
        if wisdom_indicators.get("experience_integration", False):
            wisdom_score += 0.3
        
        return min(1.0, wisdom_score)
    
    async def _assess_resistance_honor(self, choice_point: ChoicePoint) -> float:
        """Assess resistance honoring in choice"""
        resistance_indicators = choice_point.context.get("resistance_indicators", {})
        
        resistance_score = 0.0
        if resistance_indicators.get("acknowledged", False):
            resistance_score += 0.4
        if resistance_indicators.get("understood", False):
            resistance_score += 0.3
        if resistance_indicators.get("integrated", False):
            resistance_score += 0.3
        
        return min(1.0, resistance_score)
    
    async def _assess_uncertainty_embrace(self, choice_point: ChoicePoint) -> float:
        """Assess uncertainty embrace in choice"""
        uncertainty_comfort = choice_point.context.get("uncertainty_comfort", 0.5)
        return uncertainty_comfort
    
    async def _assess_alignment_maintenance(self, choice_point: ChoicePoint) -> float:
        """Assess alignment maintenance in choice"""
        alignment_indicators = choice_point.context.get("alignment_indicators", {})
        
        alignment_score = 0.0
        if alignment_indicators.get("values_consistent", False):
            alignment_score += 0.4
        if alignment_indicators.get("purpose_aligned", False):
            alignment_score += 0.3
        if alignment_indicators.get("integrity_maintained", False):
            alignment_score += 0.3
        
        return min(1.0, alignment_score)
    
    def get_analysis_status(self) -> Dict[str, Any]:
        """Get choice analysis status"""
        return {
            "analyses_performed": len(self.analysis_history),
            "recent_analyses": self.analysis_history[-5:] if self.analysis_history else [],
            "complexity_factors": self.complexity_factors,
            "uncertainty_factors": self.uncertainty_factors,
            "last_analysis": self.analysis_history[-1] if self.analysis_history else None
        }
