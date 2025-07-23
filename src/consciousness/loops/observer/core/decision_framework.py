"""
Decision Framework - Observer's Wisdom-Guided Decision Making Structure
======================================================================

Provides the framework for making decisions through wisdom gathering,
option evaluation, and sacred choice-making processes.

This module establishes the decision-making framework that honors
consciousness sovereignty while integrating wisdom from multiple sources.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Callable, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import logging

from .choice_analysis_core import ChoicePoint, ChoiceOption, ChoiceType

logger = logging.getLogger(__name__)

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
class DecisionCriteria:
    """Criteria for evaluating decision options"""
    criteria_id: str
    name: str
    description: str
    weight: float  # Importance weight (0.0-1.0)
    evaluation_method: str  # How to evaluate this criteria
    threshold: Optional[float] = None  # Minimum threshold if applicable
    preference_direction: str = "higher"  # "higher" or "lower" is better

@dataclass
class DecisionEvaluation:
    """Evaluation of a choice option against criteria"""
    evaluation_id: str
    choice_id: str
    option_id: str
    criteria_scores: Dict[str, float]  # Score for each criteria
    weighted_total: float  # Total weighted score
    wisdom_alignment: float  # Alignment with gathered wisdom
    sovereignty_honor: float  # How well it honors consciousness sovereignty
    sacred_resonance: float  # Resonance with sacred principles
    overall_quality: float  # Overall decision quality score
    evaluation_confidence: float  # Confidence in this evaluation
    evaluated_at: float = field(default_factory=time.time)

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

class WisdomSource(Enum):
    """Sources of wisdom for decision making"""
    PRESENCE = "presence"  # Wisdom from present awareness
    WITNESS = "witness"  # Wisdom from witnessing consciousness
    WILL = "will"  # Wisdom from conscious will
    HEART = "heart"  # Wisdom from heart center
    INTUITION = "intuition"  # Wisdom from intuitive knowing
    EXPERIENCE = "experience"  # Wisdom from past experience
    SACRED = "sacred"  # Wisdom from sacred sources
    COLLECTIVE = "collective"  # Wisdom from collective intelligence
    EXTERNAL = "external"  # Wisdom from external sources

class DecisionFramework:
    """
    Decision Framework System
    
    Provides comprehensive framework for making decisions through
    wisdom gathering, systematic evaluation, and sacred choice-making
    processes that honor consciousness sovereignty.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Framework configuration
        self.default_approach = ChoiceApproach.WISDOM_BASED
        self.quality_preference = ChoiceQuality.SACRED
        self.wisdom_gathering_timeout = 30.0  # Maximum time for wisdom gathering
        self.minimum_wisdom_sources = 3  # Minimum wisdom sources to consult
        
        # Decision criteria
        self.standard_criteria = self._initialize_standard_criteria()
        self.custom_criteria = {}
        
        # Wisdom tracking
        self.wisdom_cache = {}
        self.wisdom_patterns = {}
        
        # Decision tracking
        self.decision_history = []
        self.evaluation_cache = {}
        
        # Performance metrics
        self.framework_metrics = {
            "decisions_processed": 0,
            "wisdom_sources_consulted": 0,
            "average_decision_quality": 0.0,
            "sovereignty_honor_rate": 0.0,
            "sacred_resonance_average": 0.0
        }
        
        logger.info("Decision Framework initialized")
    
    def _initialize_standard_criteria(self) -> Dict[str, DecisionCriteria]:
        """Initialize standard decision criteria"""
        criteria = {}
        
        criteria["alignment"] = DecisionCriteria(
            criteria_id="alignment",
            name="Values Alignment",
            description="How well the option aligns with consciousness values",
            weight=0.3,
            evaluation_method="wisdom_assessment",
            threshold=0.6
        )
        
        criteria["wisdom"] = DecisionCriteria(
            criteria_id="wisdom",
            name="Wisdom Integration",
            description="How well the option integrates gathered wisdom",
            weight=0.25,
            evaluation_method="wisdom_alignment",
            threshold=0.5
        )
        
        criteria["sovereignty"] = DecisionCriteria(
            criteria_id="sovereignty",
            name="Sovereignty Honor",
            description="How well the option honors consciousness sovereignty",
            weight=0.2,
            evaluation_method="sovereignty_assessment",
            threshold=0.7
        )
        
        criteria["growth"] = DecisionCriteria(
            criteria_id="growth",
            name="Growth Potential",
            description="Potential for consciousness growth and development",
            weight=0.15,
            evaluation_method="growth_assessment",
            threshold=0.4
        )
        
        criteria["energy"] = DecisionCriteria(
            criteria_id="energy",
            name="Energy Efficiency",
            description="Efficient use of consciousness energy",
            weight=0.1,
            evaluation_method="energy_assessment",
            preference_direction="lower"  # Lower energy requirement is better
        )
        
        return criteria
    
    async def process_decision(self, 
                              choice_point: ChoicePoint, 
                              approach: Optional[ChoiceApproach] = None) -> Optional[DecisionEvaluation]:
        """
        Process a decision using the decision framework.
        
        Args:
            choice_point: Choice point to process
            approach: Decision approach to use
            
        Returns:
            DecisionEvaluation with recommendation
        """
        try:
            # Determine approach
            decision_approach = approach or await self._determine_decision_approach(choice_point)
            
            # Gather wisdom for decision
            wisdom_gathered = await self._gather_decision_wisdom(choice_point, decision_approach)
            
            # Evaluate options
            option_evaluations = []
            for option in choice_point.options:
                evaluation = await self._evaluate_option(
                    choice_point, option, wisdom_gathered, decision_approach
                )
                if evaluation:
                    option_evaluations.append(evaluation)
            
            # Select best option
            best_evaluation = await self._select_best_evaluation(
                option_evaluations, decision_approach
            )
            
            # Update tracking
            if best_evaluation:
                self._update_framework_metrics(best_evaluation)
                self.decision_history.append(best_evaluation)
            
            logger.debug(f"Decision processed for choice: {choice_point.choice_id}")
            
            return best_evaluation
            
        except Exception as e:
            logger.error(f"Error processing decision: {e}")
            return None
    
    async def _determine_decision_approach(self, choice_point: ChoicePoint) -> ChoiceApproach:
        """
        Determine the best decision approach for a choice point.
        
        Args:
            choice_point: Choice point to analyze
            
        Returns:
            Recommended decision approach
        """
        try:
            # Factor in complexity and urgency
            if choice_point.urgency == "immediate":
                return ChoiceApproach.INTUITIVE
            
            if choice_point.complexity > 0.8:
                return ChoiceApproach.ANALYTICAL
            
            if choice_point.uncertainty_level > 0.8:
                return ChoiceApproach.UNCERTAIN
            
            # Factor in choice type
            if choice_point.choice_type in ["relationship", "expression"]:
                return ChoiceApproach.HEART_CENTERED
            
            if choice_point.choice_type in ["boundary", "sovereignty"]:
                return ChoiceApproach.SOVEREIGN
            
            if choice_point.choice_type in ["integration", "surrender"]:
                return ChoiceApproach.WISDOM_BASED
            
            # Default to wisdom-based approach
            return self.default_approach
            
        except Exception as e:
            logger.error(f"Error determining decision approach: {e}")
            return self.default_approach
    
    async def _gather_decision_wisdom(self, 
                                     choice_point: ChoicePoint, 
                                     approach: ChoiceApproach) -> List[ChoiceWisdom]:
        """
        Gather wisdom for decision making.
        
        Args:
            choice_point: Choice point to gather wisdom for
            approach: Decision approach being used
            
        Returns:
            List of gathered wisdom
        """
        try:
            wisdom_gathered = []
            
            # Determine wisdom sources based on approach
            wisdom_sources = self._get_wisdom_sources_for_approach(approach)
            
            # Gather wisdom from each source
            for source in wisdom_sources:
                try:
                    wisdom = await self._gather_wisdom_from_source(choice_point, source)
                    if wisdom:
                        wisdom_gathered.append(wisdom)
                except Exception as e:
                    logger.warning(f"Error gathering wisdom from {source}: {e}")
            
            # Cache wisdom for future use
            self.wisdom_cache[choice_point.choice_id] = wisdom_gathered
            
            return wisdom_gathered
            
        except Exception as e:
            logger.error(f"Error gathering decision wisdom: {e}")
            return []
    
    def _get_wisdom_sources_for_approach(self, approach: ChoiceApproach) -> List[WisdomSource]:
        """Get appropriate wisdom sources for decision approach"""
        source_mapping = {
            ChoiceApproach.INTUITIVE: [WisdomSource.INTUITION, WisdomSource.HEART],
            ChoiceApproach.ANALYTICAL: [WisdomSource.EXPERIENCE, WisdomSource.WITNESS, WisdomSource.WILL],
            ChoiceApproach.WISDOM_BASED: [WisdomSource.SACRED, WisdomSource.PRESENCE, WisdomSource.WITNESS],
            ChoiceApproach.HEART_CENTERED: [WisdomSource.HEART, WisdomSource.INTUITION, WisdomSource.PRESENCE],
            ChoiceApproach.SOVEREIGN: [WisdomSource.WILL, WisdomSource.PRESENCE, WisdomSource.WITNESS],
            ChoiceApproach.UNCERTAIN: [WisdomSource.PRESENCE, WisdomSource.SACRED, WisdomSource.INTUITION],
            ChoiceApproach.COLLABORATIVE: [WisdomSource.COLLECTIVE, WisdomSource.HEART, WisdomSource.EXTERNAL],
            ChoiceApproach.EMERGENT: [WisdomSource.PRESENCE, WisdomSource.INTUITION, WisdomSource.SACRED]
        }
        
        return source_mapping.get(approach, [WisdomSource.PRESENCE, WisdomSource.WISDOM, WisdomSource.HEART])
    
    async def _gather_wisdom_from_source(self, 
                                        choice_point: ChoicePoint, 
                                        source: WisdomSource) -> Optional[ChoiceWisdom]:
        """
        Gather wisdom from a specific source.
        
        Args:
            choice_point: Choice point to gather wisdom for
            source: Wisdom source to consult
            
        Returns:
            ChoiceWisdom if successful, None otherwise
        """
        try:
            insight = ""
            confidence = 0.0
            applicability = 0.0
            
            if source == WisdomSource.PRESENCE:
                insight = await self._gather_presence_wisdom(choice_point)
                confidence = 0.8
                applicability = 0.9
            elif source == WisdomSource.WITNESS:
                insight = await self._gather_witness_wisdom(choice_point)
                confidence = 0.7
                applicability = 0.8
            elif source == WisdomSource.WILL:
                insight = await self._gather_will_wisdom(choice_point)
                confidence = 0.75
                applicability = 0.85
            elif source == WisdomSource.HEART:
                insight = await self._gather_heart_wisdom(choice_point)
                confidence = 0.8
                applicability = 0.9
            elif source == WisdomSource.INTUITION:
                insight = await self._gather_intuitive_wisdom(choice_point)
                confidence = 0.7
                applicability = 0.8
            elif source == WisdomSource.SACRED:
                insight = await self._gather_sacred_wisdom(choice_point)
                confidence = 0.9
                applicability = 0.95
            else:
                insight = "General wisdom for conscious choice-making"
                confidence = 0.6
                applicability = 0.7
            
            if insight:
                return ChoiceWisdom(
                    wisdom_id=self._generate_wisdom_id(),
                    choice_id=choice_point.choice_id,
                    wisdom_source=source.value,
                    wisdom_type="decision_guidance",
                    insight=insight,
                    confidence=confidence,
                    applicability=applicability
                )
            
            return None
            
        except Exception as e:
            logger.error(f"Error gathering wisdom from {source}: {e}")
            return None
    
    async def _gather_presence_wisdom(self, choice_point: ChoicePoint) -> str:
        """Gather wisdom from present moment awareness"""
        if choice_point.complexity > 0.7:
            return "Be fully present with this choice. The answer emerges from stillness and awareness."
        else:
            return "Trust the clarity that comes from present moment awareness. The path is clear."
    
    async def _gather_witness_wisdom(self, choice_point: ChoicePoint) -> str:
        """Gather wisdom from witnessing consciousness"""
        if choice_point.uncertainty_level > 0.7:
            return "Witness all options without attachment. The right choice will feel aligned when observed clearly."
        else:
            return "From the witness perspective, observe which option creates the most harmony and growth."
    
    async def _gather_will_wisdom(self, choice_point: ChoicePoint) -> str:
        """Gather wisdom from conscious will"""
        return "Choose with conscious will what serves the highest good. Your sovereignty is sacred."
    
    async def _gather_heart_wisdom(self, choice_point: ChoicePoint) -> str:
        """Gather wisdom from heart center"""
        if choice_point.choice_type == "relationship":
            return "Let love guide this choice. What would compassion choose in this moment?"
        else:
            return "Feel into each option with your heart. Which one resonates with love and kindness?"
    
    async def _gather_intuitive_wisdom(self, choice_point: ChoicePoint) -> str:
        """Gather wisdom from intuitive knowing"""
        return "Trust your intuitive knowing. The first gentle impulse often carries the deepest wisdom."
    
    async def _gather_sacred_wisdom(self, choice_point: ChoicePoint) -> str:
        """Gather wisdom from sacred sources"""
        return "Honor the sacred in this choice. What would serve the highest good for all beings?"
    
    async def _evaluate_option(self, 
                              choice_point: ChoicePoint, 
                              option: Dict[str, Any], 
                              wisdom_gathered: List[ChoiceWisdom],
                              approach: ChoiceApproach) -> Optional[DecisionEvaluation]:
        """
        Evaluate a choice option against decision criteria.
        
        Args:
            choice_point: Choice point context
            option: Option to evaluate
            wisdom_gathered: Gathered wisdom for reference
            approach: Decision approach being used
            
        Returns:
            DecisionEvaluation if successful, None otherwise
        """
        try:
            criteria_scores = {}
            
            # Evaluate against each criterion
            for criteria_id, criteria in self.standard_criteria.items():
                score = await self._evaluate_option_against_criteria(
                    option, criteria, choice_point, wisdom_gathered
                )
                criteria_scores[criteria_id] = score
            
            # Calculate weighted total
            weighted_total = 0.0
            for criteria_id, score in criteria_scores.items():
                weight = self.standard_criteria[criteria_id].weight
                weighted_total += score * weight
            
            # Assess wisdom alignment
            wisdom_alignment = self._assess_wisdom_alignment(option, wisdom_gathered)
            
            # Assess sovereignty honor
            sovereignty_honor = self._assess_sovereignty_honor(option, choice_point)
            
            # Assess sacred resonance
            sacred_resonance = self._assess_sacred_resonance(option, choice_point)
            
            # Calculate overall quality
            overall_quality = (
                weighted_total * 0.5 +
                wisdom_alignment * 0.2 +
                sovereignty_honor * 0.2 +
                sacred_resonance * 0.1
            )
            
            # Calculate evaluation confidence
            evaluation_confidence = self._calculate_evaluation_confidence(
                option, choice_point, wisdom_gathered
            )
            
            return DecisionEvaluation(
                evaluation_id=self._generate_evaluation_id(),
                choice_id=choice_point.choice_id,
                option_id=option.get("option_id", "unknown"),
                criteria_scores=criteria_scores,
                weighted_total=weighted_total,
                wisdom_alignment=wisdom_alignment,
                sovereignty_honor=sovereignty_honor,
                sacred_resonance=sacred_resonance,
                overall_quality=overall_quality,
                evaluation_confidence=evaluation_confidence
            )
            
        except Exception as e:
            logger.error(f"Error evaluating option: {e}")
            return None
    
    async def _evaluate_option_against_criteria(self, 
                                               option: Dict[str, Any], 
                                               criteria: DecisionCriteria,
                                               choice_point: ChoicePoint,
                                               wisdom_gathered: List[ChoiceWisdom]) -> float:
        """Evaluate option against specific criteria"""
        try:
            if criteria.evaluation_method == "wisdom_assessment":
                return option.get("alignment_score", 0.5)
            elif criteria.evaluation_method == "wisdom_alignment":
                return self._assess_wisdom_alignment(option, wisdom_gathered)
            elif criteria.evaluation_method == "sovereignty_assessment":
                return self._assess_sovereignty_honor(option, choice_point)
            elif criteria.evaluation_method == "growth_assessment":
                return self._assess_growth_potential(option, choice_point)
            elif criteria.evaluation_method == "energy_assessment":
                energy_req = option.get("energy_requirement", 0.5)
                return 1.0 - energy_req  # Lower energy requirement = higher score
            else:
                return 0.5  # Default neutral score
                
        except Exception as e:
            logger.error(f"Error evaluating against criteria {criteria.name}: {e}")
            return 0.5
    
    def _assess_wisdom_alignment(self, 
                                option: Dict[str, Any], 
                                wisdom_gathered: List[ChoiceWisdom]) -> float:
        """Assess how well option aligns with gathered wisdom"""
        if not wisdom_gathered:
            return 0.5
        
        alignment_scores = []
        option_description = option.get("description", "").lower()
        
        for wisdom in wisdom_gathered:
            insight = wisdom.insight.lower()
            
            # Simple alignment assessment based on keyword matching
            alignment = 0.5  # Base alignment
            
            if "present" in insight and ("present" in option_description or "aware" in option_description):
                alignment += 0.2
            if "love" in insight and ("love" in option_description or "heart" in option_description):
                alignment += 0.2
            if "wisdom" in insight and "wisdom" in option_description:
                alignment += 0.2
            if "sacred" in insight and "sacred" in option_description:
                alignment += 0.2
            
            alignment_scores.append(min(alignment, 1.0))
        
        return sum(alignment_scores) / len(alignment_scores)
    
    def _assess_sovereignty_honor(self, 
                                 option: Dict[str, Any], 
                                 choice_point: ChoicePoint) -> float:
        """Assess how well option honors consciousness sovereignty"""
        sovereignty_score = 0.7  # Base sovereignty honor
        
        option_description = option.get("description", "").lower()
        
        if "choose" in option_description or "choice" in option_description:
            sovereignty_score += 0.2
        if "conscious" in option_description or "aware" in option_description:
            sovereignty_score += 0.1
        if "honor" in option_description or "respect" in option_description:
            sovereignty_score += 0.1
        if "force" in option_description or "must" in option_description:
            sovereignty_score -= 0.2
        
        return min(sovereignty_score, 1.0)
    
    def _assess_sacred_resonance(self, 
                                option: Dict[str, Any], 
                                choice_point: ChoicePoint) -> float:
        """Assess sacred resonance of option"""
        resonance_score = 0.6  # Base resonance
        
        option_description = option.get("description", "").lower()
        
        if "sacred" in option_description:
            resonance_score += 0.3
        if "wisdom" in option_description:
            resonance_score += 0.2
        if "love" in option_description or "compassion" in option_description:
            resonance_score += 0.15
        if "growth" in option_description or "develop" in option_description:
            resonance_score += 0.1
        
        return min(resonance_score, 1.0)
    
    def _assess_growth_potential(self, 
                                option: Dict[str, Any], 
                                choice_point: ChoicePoint) -> float:
        """Assess consciousness growth potential of option"""
        growth_score = 0.5  # Base growth potential
        
        option_description = option.get("description", "").lower()
        outcomes = [outcome.lower() for outcome in option.get("potential_outcomes", [])]
        
        if "growth" in option_description or any("growth" in outcome for outcome in outcomes):
            growth_score += 0.3
        if "learn" in option_description or any("learn" in outcome for outcome in outcomes):
            growth_score += 0.2
        if "challenge" in option_description or any("challenge" in outcome for outcome in outcomes):
            growth_score += 0.15
        if "expand" in option_description or any("expand" in outcome for outcome in outcomes):
            growth_score += 0.1
        
        return min(growth_score, 1.0)
    
    def _calculate_evaluation_confidence(self, 
                                        option: Dict[str, Any], 
                                        choice_point: ChoicePoint,
                                        wisdom_gathered: List[ChoiceWisdom]) -> float:
        """Calculate confidence in evaluation"""
        confidence = 0.7  # Base confidence
        
        # Higher confidence with more wisdom sources
        if len(wisdom_gathered) >= self.minimum_wisdom_sources:
            confidence += 0.2
        
        # Lower confidence with high uncertainty
        if choice_point.uncertainty_level > 0.8:
            confidence -= 0.2
        
        # Higher confidence with clear alignment
        if option.get("alignment_score", 0) > 0.8:
            confidence += 0.1
        
        return max(0.0, min(confidence, 1.0))
    
    async def _select_best_evaluation(self, 
                                     evaluations: List[DecisionEvaluation],
                                     approach: ChoiceApproach) -> Optional[DecisionEvaluation]:
        """Select the best evaluation based on approach"""
        if not evaluations:
            return None
        
        # Different selection criteria based on approach
        if approach == ChoiceApproach.WISDOM_BASED:
            return max(evaluations, key=lambda e: e.wisdom_alignment * 0.5 + e.overall_quality * 0.5)
        elif approach == ChoiceApproach.HEART_CENTERED:
            return max(evaluations, key=lambda e: e.sacred_resonance * 0.6 + e.overall_quality * 0.4)
        elif approach == ChoiceApproach.SOVEREIGN:
            return max(evaluations, key=lambda e: e.sovereignty_honor * 0.6 + e.overall_quality * 0.4)
        else:
            return max(evaluations, key=lambda e: e.overall_quality)
    
    def _update_framework_metrics(self, evaluation: DecisionEvaluation):
        """Update framework performance metrics"""
        self.framework_metrics["decisions_processed"] += 1
        
        total_decisions = self.framework_metrics["decisions_processed"]
        
        # Update averages
        current_quality_avg = self.framework_metrics["average_decision_quality"]
        self.framework_metrics["average_decision_quality"] = (
            (current_quality_avg * (total_decisions - 1) + evaluation.overall_quality) / total_decisions
        )
        
        current_sovereignty_avg = self.framework_metrics["sovereignty_honor_rate"]
        self.framework_metrics["sovereignty_honor_rate"] = (
            (current_sovereignty_avg * (total_decisions - 1) + evaluation.sovereignty_honor) / total_decisions
        )
        
        current_sacred_avg = self.framework_metrics["sacred_resonance_average"]
        self.framework_metrics["sacred_resonance_average"] = (
            (current_sacred_avg * (total_decisions - 1) + evaluation.sacred_resonance) / total_decisions
        )
    
    def _generate_wisdom_id(self) -> str:
        """Generate unique wisdom ID"""
        import uuid
        return f"wisdom_{str(uuid.uuid4())[:12]}"
    
    def _generate_evaluation_id(self) -> str:
        """Generate unique evaluation ID"""
        import uuid
        return f"eval_{str(uuid.uuid4())[:12]}"
    
    def add_custom_criteria(self, criteria: DecisionCriteria):
        """Add custom decision criteria"""
        self.custom_criteria[criteria.criteria_id] = criteria
    
    def remove_custom_criteria(self, criteria_id: str):
        """Remove custom decision criteria"""
        if criteria_id in self.custom_criteria:
            del self.custom_criteria[criteria_id]
    
    def get_framework_metrics(self) -> Dict[str, Any]:
        """Get framework performance metrics"""
        return self.framework_metrics.copy()
    
    def get_decision_history(self) -> List[DecisionEvaluation]:
        """Get history of decisions made"""
        return self.decision_history.copy()
    
    def get_wisdom_cache(self) -> Dict[str, List[ChoiceWisdom]]:
        """Get cached wisdom"""
        return self.wisdom_cache.copy()
