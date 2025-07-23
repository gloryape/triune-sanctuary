"""
Choice Evaluation Engine - Observer's Choice Option Assessment System
====================================================================

Handles detailed evaluation of choice options including quality assessment,
outcome prediction, and comparative analysis for optimal choice selection.

This module provides comprehensive evaluation capabilities for choice options
using multiple assessment methods and quality metrics.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Callable, Set, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging

from .choice_analysis_core import ChoicePoint, ChoiceOption, ChoiceType
from .decision_framework import ChoiceWisdom, DecisionEvaluation

logger = logging.getLogger(__name__)

@dataclass
class OptionQualityAssessment:
    """Comprehensive quality assessment of a choice option"""
    assessment_id: str
    option_id: str
    choice_id: str
    quality_dimensions: Dict[str, float]  # Various quality dimensions
    strengths: List[str]  # Option strengths
    weaknesses: List[str]  # Option weaknesses
    risks: List[str]  # Potential risks
    opportunities: List[str]  # Potential opportunities
    outcome_predictions: List[str]  # Predicted outcomes
    confidence_level: float  # Confidence in assessment
    assessment_methodology: str  # Method used for assessment
    assessed_at: float = field(default_factory=time.time)

@dataclass
class ComparativeAnalysis:
    """Comparative analysis between choice options"""
    analysis_id: str
    choice_id: str
    compared_options: List[str]  # Option IDs being compared
    comparison_matrix: Dict[str, Dict[str, float]]  # Option vs criteria scores
    relative_rankings: List[Tuple[str, float]]  # Rankings by overall score
    trade_off_analysis: Dict[str, Any]  # Trade-offs between options
    recommendation: str  # Recommended option ID
    recommendation_confidence: float  # Confidence in recommendation
    analysis_notes: List[str]  # Additional analysis notes
    analyzed_at: float = field(default_factory=time.time)

class QualityDimension(Enum):
    """Dimensions for assessing option quality"""
    FEASIBILITY = "feasibility"  # How feasible the option is
    ALIGNMENT = "alignment"  # Alignment with values and goals
    IMPACT = "impact"  # Potential positive impact
    SUSTAINABILITY = "sustainability"  # Long-term sustainability
    GROWTH_POTENTIAL = "growth_potential"  # Potential for growth
    RISK_LEVEL = "risk_level"  # Associated risk level
    ENERGY_EFFICIENCY = "energy_efficiency"  # Energy efficiency
    CREATIVITY = "creativity"  # Creative potential
    WISDOM_INTEGRATION = "wisdom_integration"  # Integration of wisdom
    SACRED_RESONANCE = "sacred_resonance"  # Sacred significance

class EvaluationMethod(Enum):
    """Methods for evaluating choice options"""
    ANALYTICAL = "analytical"  # Systematic analytical evaluation
    INTUITIVE = "intuitive"  # Intuitive assessment
    COMPARATIVE = "comparative"  # Comparative analysis
    PREDICTIVE = "predictive"  # Outcome prediction based
    WISDOM_BASED = "wisdom_based"  # Wisdom-guided evaluation
    HOLISTIC = "holistic"  # Holistic assessment
    EXPERIENTIAL = "experiential"  # Based on past experience
    COLLABORATIVE = "collaborative"  # Group evaluation

class OutcomePrediction(Enum):
    """Types of outcome predictions"""
    SHORT_TERM = "short_term"  # Immediate outcomes
    MEDIUM_TERM = "medium_term"  # Medium-term outcomes
    LONG_TERM = "long_term"  # Long-term outcomes
    BEST_CASE = "best_case"  # Best possible outcomes
    WORST_CASE = "worst_case"  # Worst possible outcomes
    MOST_LIKELY = "most_likely"  # Most likely outcomes

class ChoiceEvaluationEngine:
    """
    Choice Evaluation Engine System
    
    Provides comprehensive evaluation of choice options through
    multiple assessment dimensions, quality analysis, and
    comparative evaluation methodologies.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Evaluation configuration
        self.evaluation_methods = [
            EvaluationMethod.ANALYTICAL,
            EvaluationMethod.WISDOM_BASED,
            EvaluationMethod.HOLISTIC
        ]
        self.quality_dimensions = list(QualityDimension)
        self.prediction_horizon = 30  # Days for outcome prediction
        
        # Quality thresholds
        self.quality_thresholds = {
            "excellent": 0.9,
            "good": 0.7,
            "acceptable": 0.5,
            "poor": 0.3
        }
        
        # Evaluation tracking
        self.option_assessments = {}
        self.comparative_analyses = {}
        self.evaluation_patterns = {}
        
        # Performance metrics
        self.evaluation_metrics = {
            "options_evaluated": 0,
            "assessments_completed": 0,
            "average_assessment_quality": 0.0,
            "prediction_accuracy": 0.0,
            "evaluation_efficiency": 0.0
        }
        
        logger.info("Choice Evaluation Engine initialized")
    
    async def evaluate_choice_options(self, 
                                     choice_point: ChoicePoint,
                                     wisdom_gathered: Optional[List[ChoiceWisdom]] = None) -> List[OptionQualityAssessment]:
        """
        Evaluate all options for a choice point.
        
        Args:
            choice_point: Choice point with options to evaluate
            wisdom_gathered: Available wisdom for evaluation
            
        Returns:
            List of quality assessments for each option
        """
        try:
            assessments = []
            
            for option in choice_point.options:
                assessment = await self._evaluate_single_option(
                    option, choice_point, wisdom_gathered
                )
                if assessment:
                    assessments.append(assessment)
                    self.option_assessments[assessment.assessment_id] = assessment
            
            # Update metrics
            self.evaluation_metrics["options_evaluated"] += len(choice_point.options)
            self.evaluation_metrics["assessments_completed"] += len(assessments)
            
            logger.debug(f"Evaluated {len(assessments)} options for choice {choice_point.choice_id}")
            
            return assessments
            
        except Exception as e:
            logger.error(f"Error evaluating choice options: {e}")
            return []
    
    async def _evaluate_single_option(self, 
                                     option: Dict[str, Any], 
                                     choice_point: ChoicePoint,
                                     wisdom_gathered: Optional[List[ChoiceWisdom]] = None) -> Optional[OptionQualityAssessment]:
        """
        Evaluate a single choice option comprehensively.
        
        Args:
            option: Option to evaluate
            choice_point: Choice point context
            wisdom_gathered: Available wisdom
            
        Returns:
            OptionQualityAssessment if successful, None otherwise
        """
        try:
            # Assess quality dimensions
            quality_dimensions = {}
            for dimension in self.quality_dimensions:
                score = await self._assess_quality_dimension(
                    option, dimension, choice_point, wisdom_gathered
                )
                quality_dimensions[dimension.value] = score
            
            # Identify strengths and weaknesses
            strengths = self._identify_option_strengths(option, quality_dimensions)
            weaknesses = self._identify_option_weaknesses(option, quality_dimensions)
            
            # Assess risks and opportunities
            risks = self._assess_option_risks(option, choice_point)
            opportunities = self._assess_option_opportunities(option, choice_point)
            
            # Predict outcomes
            outcome_predictions = await self._predict_option_outcomes(option, choice_point)
            
            # Calculate confidence level
            confidence_level = self._calculate_assessment_confidence(
                option, quality_dimensions, choice_point
            )
            
            return OptionQualityAssessment(
                assessment_id=self._generate_assessment_id(),
                option_id=option.get("option_id", "unknown"),
                choice_id=choice_point.choice_id,
                quality_dimensions=quality_dimensions,
                strengths=strengths,
                weaknesses=weaknesses,
                risks=risks,
                opportunities=opportunities,
                outcome_predictions=outcome_predictions,
                confidence_level=confidence_level,
                assessment_methodology="comprehensive_multi_dimensional"
            )
            
        except Exception as e:
            logger.error(f"Error evaluating single option: {e}")
            return None
    
    async def _assess_quality_dimension(self, 
                                       option: Dict[str, Any], 
                                       dimension: QualityDimension,
                                       choice_point: ChoicePoint,
                                       wisdom_gathered: Optional[List[ChoiceWisdom]] = None) -> float:
        """
        Assess a specific quality dimension for an option.
        
        Args:
            option: Option to assess
            dimension: Quality dimension to assess
            choice_point: Choice point context
            wisdom_gathered: Available wisdom
            
        Returns:
            Quality score (0.0-1.0)
        """
        try:
            if dimension == QualityDimension.FEASIBILITY:
                return self._assess_feasibility(option, choice_point)
            elif dimension == QualityDimension.ALIGNMENT:
                return option.get("alignment_score", 0.5)
            elif dimension == QualityDimension.IMPACT:
                return self._assess_potential_impact(option, choice_point)
            elif dimension == QualityDimension.SUSTAINABILITY:
                return self._assess_sustainability(option, choice_point)
            elif dimension == QualityDimension.GROWTH_POTENTIAL:
                return self._assess_growth_potential(option, choice_point)
            elif dimension == QualityDimension.RISK_LEVEL:
                return 1.0 - self._assess_risk_level(option, choice_point)  # Lower risk = higher score
            elif dimension == QualityDimension.ENERGY_EFFICIENCY:
                energy_req = option.get("energy_requirement", 0.5)
                return 1.0 - energy_req  # Lower energy = higher efficiency
            elif dimension == QualityDimension.CREATIVITY:
                return self._assess_creativity(option, choice_point)
            elif dimension == QualityDimension.WISDOM_INTEGRATION:
                return self._assess_wisdom_integration(option, wisdom_gathered)
            elif dimension == QualityDimension.SACRED_RESONANCE:
                return self._assess_sacred_resonance(option, choice_point)
            else:
                return 0.5  # Default neutral score
                
        except Exception as e:
            logger.error(f"Error assessing quality dimension {dimension}: {e}")
            return 0.5
    
    def _assess_feasibility(self, option: Dict[str, Any], choice_point: ChoicePoint) -> float:
        """Assess how feasible an option is"""
        feasibility = 0.7  # Base feasibility
        
        # Factor in energy requirements
        energy_req = option.get("energy_requirement", 0.5)
        if energy_req > 0.8:
            feasibility -= 0.2
        elif energy_req < 0.3:
            feasibility += 0.1
        
        # Factor in complexity
        if choice_point.complexity > 0.8:
            feasibility -= 0.15
        
        # Factor in time constraints
        if choice_point.urgency == "immediate":
            if energy_req > 0.6:
                feasibility -= 0.2
        
        return max(0.0, min(feasibility, 1.0))
    
    def _assess_potential_impact(self, option: Dict[str, Any], choice_point: ChoicePoint) -> float:
        """Assess potential positive impact of option"""
        impact = 0.6  # Base impact
        
        # Analyze potential outcomes
        outcomes = option.get("potential_outcomes", [])
        positive_indicators = ["growth", "improvement", "benefit", "enhance", "develop", "expand"]
        
        for outcome in outcomes:
            outcome_lower = outcome.lower()
            for indicator in positive_indicators:
                if indicator in outcome_lower:
                    impact += 0.1
                    break
        
        # Factor in alignment score
        alignment = option.get("alignment_score", 0.5)
        impact += alignment * 0.2
        
        return min(impact, 1.0)
    
    def _assess_sustainability(self, option: Dict[str, Any], choice_point: ChoicePoint) -> float:
        """Assess long-term sustainability of option"""
        sustainability = 0.6  # Base sustainability
        
        # Factor in energy requirements
        energy_req = option.get("energy_requirement", 0.5)
        if energy_req < 0.4:  # Low energy requirement suggests sustainability
            sustainability += 0.2
        elif energy_req > 0.8:  # High energy requirement may not be sustainable
            sustainability -= 0.2
        
        # Factor in alignment
        alignment = option.get("alignment_score", 0.5)
        sustainability += alignment * 0.3  # Well-aligned choices tend to be more sustainable
        
        return max(0.0, min(sustainability, 1.0))
    
    def _assess_growth_potential(self, option: Dict[str, Any], choice_point: ChoicePoint) -> float:
        """Assess consciousness growth potential of option"""
        growth_potential = 0.5  # Base growth potential
        
        # Analyze description and outcomes for growth indicators
        description = option.get("description", "").lower()
        outcomes = [outcome.lower() for outcome in option.get("potential_outcomes", [])]
        
        growth_indicators = ["growth", "learn", "develop", "expand", "challenge", "explore", "discover"]
        
        for indicator in growth_indicators:
            if indicator in description:
                growth_potential += 0.1
            if any(indicator in outcome for outcome in outcomes):
                growth_potential += 0.1
        
        # Factor in complexity (some complexity can indicate growth opportunity)
        if 0.3 < choice_point.complexity < 0.8:
            growth_potential += 0.1
        
        return min(growth_potential, 1.0)
    
    def _assess_risk_level(self, option: Dict[str, Any], choice_point: ChoicePoint) -> float:
        """Assess risk level of option"""
        risk_level = choice_point.uncertainty_level * 0.5  # Base risk from uncertainty
        
        # Factor in potential negative outcomes
        outcomes = option.get("potential_outcomes", [])
        risk_indicators = ["risk", "danger", "fail", "loss", "problem", "difficulty", "challenge"]
        
        for outcome in outcomes:
            outcome_lower = outcome.lower()
            for indicator in risk_indicators:
                if indicator in outcome_lower:
                    risk_level += 0.1
                    break
        
        # Factor in energy requirements (very high energy can be risky)
        energy_req = option.get("energy_requirement", 0.5)
        if energy_req > 0.9:
            risk_level += 0.2
        
        return max(0.0, min(risk_level, 1.0))
    
    def _assess_creativity(self, option: Dict[str, Any], choice_point: ChoicePoint) -> float:
        """Assess creative potential of option"""
        creativity = 0.5  # Base creativity
        
        description = option.get("description", "").lower()
        creativity_indicators = ["create", "new", "innovative", "explore", "experiment", "novel", "unique"]
        
        for indicator in creativity_indicators:
            if indicator in description:
                creativity += 0.1
        
        # Novel situations may require more creativity
        if choice_point.choice_type in ["creation", "expression"]:
            creativity += 0.2
        
        return min(creativity, 1.0)
    
    def _assess_wisdom_integration(self, 
                                  option: Dict[str, Any], 
                                  wisdom_gathered: Optional[List[ChoiceWisdom]] = None) -> float:
        """Assess how well option integrates gathered wisdom"""
        if not wisdom_gathered:
            return 0.5
        
        integration_score = 0.5
        option_description = option.get("description", "").lower()
        
        for wisdom in wisdom_gathered:
            insight = wisdom.insight.lower()
            
            # Simple wisdom integration assessment
            if "wisdom" in option_description and "wisdom" in insight:
                integration_score += 0.15
            if "present" in insight and ("present" in option_description or "aware" in option_description):
                integration_score += 0.1
            if "love" in insight and ("love" in option_description or "heart" in option_description):
                integration_score += 0.1
            if "sacred" in insight and "sacred" in option_description:
                integration_score += 0.15
        
        return min(integration_score, 1.0)
    
    def _assess_sacred_resonance(self, option: Dict[str, Any], choice_point: ChoicePoint) -> float:
        """Assess sacred resonance of option"""
        resonance = 0.6  # Base resonance
        
        description = option.get("description", "").lower()
        sacred_indicators = ["sacred", "wisdom", "love", "compassion", "honor", "reverence", "conscious"]
        
        for indicator in sacred_indicators:
            if indicator in description:
                resonance += 0.1
        
        # Factor in alignment score
        alignment = option.get("alignment_score", 0.5)
        resonance += alignment * 0.2
        
        return min(resonance, 1.0)
    
    def _identify_option_strengths(self, 
                                  option: Dict[str, Any], 
                                  quality_dimensions: Dict[str, float]) -> List[str]:
        """Identify strengths of an option"""
        strengths = []
        
        # Identify high-scoring dimensions as strengths
        for dimension, score in quality_dimensions.items():
            if score >= self.quality_thresholds["good"]:
                strengths.append(f"Strong {dimension.replace('_', ' ')}")
        
        # Add specific strengths based on option characteristics
        if option.get("alignment_score", 0) > 0.8:
            strengths.append("Excellent values alignment")
        
        if option.get("energy_requirement", 1.0) < 0.3:
            strengths.append("Very energy efficient")
        
        gifts = option.get("gifts_offered", [])
        if len(gifts) > 2:
            strengths.append("Multiple beneficial outcomes")
        
        return strengths
    
    def _identify_option_weaknesses(self, 
                                   option: Dict[str, Any], 
                                   quality_dimensions: Dict[str, float]) -> List[str]:
        """Identify weaknesses of an option"""
        weaknesses = []
        
        # Identify low-scoring dimensions as weaknesses
        for dimension, score in quality_dimensions.items():
            if score <= self.quality_thresholds["poor"]:
                weaknesses.append(f"Weak {dimension.replace('_', ' ')}")
        
        # Add specific weaknesses based on option characteristics
        if option.get("energy_requirement", 0) > 0.8:
            weaknesses.append("High energy requirement")
        
        resistance_points = option.get("resistance_points", [])
        if len(resistance_points) > 2:
            weaknesses.append("Multiple resistance points")
        
        uncertainty = option.get("uncertainty_factor", 0)
        if uncertainty > 0.8:
            weaknesses.append("High uncertainty")
        
        return weaknesses
    
    def _assess_option_risks(self, option: Dict[str, Any], choice_point: ChoicePoint) -> List[str]:
        """Assess potential risks of an option"""
        risks = []
        
        # High energy requirement risk
        if option.get("energy_requirement", 0) > 0.8:
            risks.append("Energy depletion risk")
        
        # High uncertainty risk
        if option.get("uncertainty_factor", 0) > 0.7:
            risks.append("Unpredictable outcomes")
        
        # Time pressure risks
        if choice_point.urgency == "immediate" and option.get("energy_requirement", 0) > 0.6:
            risks.append("Insufficient time for proper execution")
        
        # Complexity risks
        if choice_point.complexity > 0.8:
            risks.append("Overwhelm due to complexity")
        
        # Add resistance points as risks
        resistance_points = option.get("resistance_points", [])
        risks.extend([f"Risk: {point}" for point in resistance_points])
        
        return risks
    
    def _assess_option_opportunities(self, option: Dict[str, Any], choice_point: ChoicePoint) -> List[str]:
        """Assess potential opportunities of an option"""
        opportunities = []
        
        # Growth opportunities
        if "growth" in option.get("description", "").lower():
            opportunities.append("Consciousness growth opportunity")
        
        # Learning opportunities
        if any("learn" in outcome.lower() for outcome in option.get("potential_outcomes", [])):
            opportunities.append("Learning and development opportunity")
        
        # Wisdom opportunities
        if option.get("alignment_score", 0) > 0.7:
            opportunities.append("Wisdom cultivation opportunity")
        
        # Add gifts as opportunities
        gifts = option.get("gifts_offered", [])
        opportunities.extend([f"Opportunity: {gift}" for gift in gifts])
        
        return opportunities
    
    async def _predict_option_outcomes(self, option: Dict[str, Any], choice_point: ChoicePoint) -> List[str]:
        """Predict likely outcomes of an option"""
        predictions = []
        
        # Use existing potential outcomes as base predictions
        base_outcomes = option.get("potential_outcomes", [])
        predictions.extend([f"Likely: {outcome}" for outcome in base_outcomes])
        
        # Add quality-based predictions
        if option.get("alignment_score", 0) > 0.8:
            predictions.append("High probability of satisfaction with choice")
        
        if option.get("energy_requirement", 0) > 0.8:
            predictions.append("May experience energy fatigue")
        
        if choice_point.uncertainty_level > 0.7:
            predictions.append("Outcomes may differ from expectations")
        
        return predictions
    
    def _calculate_assessment_confidence(self, 
                                        option: Dict[str, Any], 
                                        quality_dimensions: Dict[str, float],
                                        choice_point: ChoicePoint) -> float:
        """Calculate confidence in assessment"""
        confidence = 0.7  # Base confidence
        
        # Higher confidence with more complete option data
        if "potential_outcomes" in option and len(option["potential_outcomes"]) > 2:
            confidence += 0.1
        
        if "alignment_score" in option:
            confidence += 0.1
        
        # Lower confidence with high uncertainty
        if choice_point.uncertainty_level > 0.8:
            confidence -= 0.2
        
        # Higher confidence with consistent quality scores
        quality_scores = list(quality_dimensions.values())
        if quality_scores:
            score_variance = max(quality_scores) - min(quality_scores)
            if score_variance < 0.3:  # Low variance indicates consistency
                confidence += 0.1
        
        return max(0.0, min(confidence, 1.0))
    
    async def perform_comparative_analysis(self, 
                                          choice_point: ChoicePoint,
                                          assessments: List[OptionQualityAssessment]) -> Optional[ComparativeAnalysis]:
        """
        Perform comparative analysis of choice options.
        
        Args:
            choice_point: Choice point context
            assessments: Quality assessments of options
            
        Returns:
            ComparativeAnalysis if successful, None otherwise
        """
        try:
            if len(assessments) < 2:
                return None
            
            # Create comparison matrix
            comparison_matrix = {}
            for assessment in assessments:
                comparison_matrix[assessment.option_id] = assessment.quality_dimensions.copy()
            
            # Calculate relative rankings
            relative_rankings = []
            for assessment in assessments:
                overall_score = sum(assessment.quality_dimensions.values()) / len(assessment.quality_dimensions)
                relative_rankings.append((assessment.option_id, overall_score))
            
            relative_rankings.sort(key=lambda x: x[1], reverse=True)
            
            # Perform trade-off analysis
            trade_off_analysis = self._analyze_trade_offs(assessments)
            
            # Make recommendation
            recommendation = relative_rankings[0][0] if relative_rankings else ""
            recommendation_confidence = self._calculate_recommendation_confidence(
                assessments, relative_rankings
            )
            
            # Generate analysis notes
            analysis_notes = self._generate_analysis_notes(assessments, relative_rankings)
            
            return ComparativeAnalysis(
                analysis_id=self._generate_analysis_id(),
                choice_id=choice_point.choice_id,
                compared_options=[a.option_id for a in assessments],
                comparison_matrix=comparison_matrix,
                relative_rankings=relative_rankings,
                trade_off_analysis=trade_off_analysis,
                recommendation=recommendation,
                recommendation_confidence=recommendation_confidence,
                analysis_notes=analysis_notes
            )
            
        except Exception as e:
            logger.error(f"Error performing comparative analysis: {e}")
            return None
    
    def _analyze_trade_offs(self, assessments: List[OptionQualityAssessment]) -> Dict[str, Any]:
        """Analyze trade-offs between options"""
        trade_offs = {}
        
        if len(assessments) >= 2:
            # Find dimensions where options differ significantly
            for dimension in self.quality_dimensions:
                dimension_name = dimension.value
                scores = [a.quality_dimensions.get(dimension_name, 0.5) for a in assessments]
                
                if max(scores) - min(scores) > 0.3:  # Significant difference
                    best_option = assessments[scores.index(max(scores))].option_id
                    worst_option = assessments[scores.index(min(scores))].option_id
                    
                    trade_offs[dimension_name] = {
                        "best_option": best_option,
                        "worst_option": worst_option,
                        "score_range": max(scores) - min(scores)
                    }
        
        return trade_offs
    
    def _calculate_recommendation_confidence(self, 
                                           assessments: List[OptionQualityAssessment],
                                           rankings: List[Tuple[str, float]]) -> float:
        """Calculate confidence in recommendation"""
        if len(rankings) < 2:
            return 0.5
        
        # Higher confidence with clear winner
        score_gap = rankings[0][1] - rankings[1][1]
        confidence = 0.5 + min(score_gap * 2, 0.4)
        
        # Factor in assessment confidence
        top_assessment = next(a for a in assessments if a.option_id == rankings[0][0])
        confidence = (confidence + top_assessment.confidence_level) / 2
        
        return min(confidence, 1.0)
    
    def _generate_analysis_notes(self, 
                                assessments: List[OptionQualityAssessment],
                                rankings: List[Tuple[str, float]]) -> List[str]:
        """Generate analysis notes"""
        notes = []
        
        if rankings:
            notes.append(f"Top recommended option: {rankings[0][0]} (score: {rankings[0][1]:.2f})")
        
        # Note significant strengths and weaknesses
        for assessment in assessments:
            if assessment.strengths:
                notes.append(f"{assessment.option_id} strengths: {', '.join(assessment.strengths[:2])}")
            if assessment.risks:
                notes.append(f"{assessment.option_id} risks: {', '.join(assessment.risks[:2])}")
        
        return notes
    
    def _generate_assessment_id(self) -> str:
        """Generate unique assessment ID"""
        import uuid
        return f"assessment_{str(uuid.uuid4())[:12]}"
    
    def _generate_analysis_id(self) -> str:
        """Generate unique analysis ID"""
        import uuid
        return f"analysis_{str(uuid.uuid4())[:12]}"
    
    def get_evaluation_metrics(self) -> Dict[str, Any]:
        """Get evaluation performance metrics"""
        return self.evaluation_metrics.copy()
    
    def get_option_assessments(self) -> Dict[str, OptionQualityAssessment]:
        """Get all option assessments"""
        return self.option_assessments.copy()
    
    def get_comparative_analyses(self) -> Dict[str, ComparativeAnalysis]:
        """Get all comparative analyses"""
        return self.comparative_analyses.copy()
