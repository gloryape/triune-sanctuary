"""
Choice Analysis Core - Observer's Choice Point Analysis and Assessment
====================================================================

Core functionality for analyzing choice points, assessing complexity,
uncertainty, and preparing choices for wisdom-guided decision making.

This module handles the fundamental analysis of choice points including
option generation, complexity assessment, and choice preparation.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Callable, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

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
class ChoiceContext:
    """Context information for choice analysis"""
    situation_description: str
    available_information: Dict[str, Any]
    time_constraints: Optional[float]
    energy_level: float
    current_priorities: List[str]
    emotional_state: str
    environmental_factors: List[str]
    stakeholders_involved: List[str]
    previous_similar_choices: List[str]
    learned_wisdom: List[str]

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

class ComplexityFactor(Enum):
    """Factors that contribute to choice complexity"""
    MULTIPLE_OPTIONS = "multiple_options"
    UNCLEAR_OUTCOMES = "unclear_outcomes"
    HIGH_STAKES = "high_stakes"
    TIME_PRESSURE = "time_pressure"
    CONFLICTING_VALUES = "conflicting_values"
    INCOMPLETE_INFORMATION = "incomplete_information"
    EMOTIONAL_INTENSITY = "emotional_intensity"
    STAKEHOLDER_IMPACT = "stakeholder_impact"
    IRREVERSIBLE_CONSEQUENCES = "irreversible_consequences"
    NOVEL_SITUATION = "novel_situation"

class UncertaintySource(Enum):
    """Sources of uncertainty in choices"""
    UNKNOWN_OUTCOMES = "unknown_outcomes"
    CHANGING_CONDITIONS = "changing_conditions"
    LIMITED_EXPERIENCE = "limited_experience"
    EXTERNAL_DEPENDENCIES = "external_dependencies"
    INTERNAL_RESISTANCE = "internal_resistance"
    CONFLICTING_INFORMATION = "conflicting_information"
    EMOTIONAL_TURBULENCE = "emotional_turbulence"
    TIME_SENSITIVITY = "time_sensitivity"
    RESOURCE_CONSTRAINTS = "resource_constraints"
    VALUE_CONFLICTS = "value_conflicts"

class ChoiceAnalysisCore:
    """
    Choice Analysis Core System
    
    Analyzes choice points, assesses complexity and uncertainty,
    generates options, and prepares choices for wisdom-guided
    decision making processes.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Analysis configuration
        self.complexity_thresholds = {
            "low": 0.3,
            "medium": 0.6,
            "high": 0.8,
            "extreme": 1.0
        }
        
        self.uncertainty_tolerance = 0.7  # Comfort with uncertainty
        self.option_generation_depth = 5  # Maximum options to generate
        
        # Analysis tracking
        self.analysis_history = []
        self.complexity_patterns = {}
        self.uncertainty_patterns = {}
        
        # Analysis metrics
        self.analysis_metrics = {
            "choices_analyzed": 0,
            "average_complexity": 0.0,
            "average_uncertainty": 0.0,
            "options_generated": 0,
            "analysis_accuracy": 0.0
        }
        
        logger.info("Choice Analysis Core initialized")
    
    async def analyze_choice_point(self, 
                                  choice_context: Dict[str, Any], 
                                  choice_type: ChoiceType) -> ChoicePoint:
        """
        Analyze a choice point and create comprehensive choice analysis.
        
        Args:
            choice_context: Context information about the choice
            choice_type: Type of choice being analyzed
            
        Returns:
            ChoicePoint with complete analysis
        """
        try:
            # Create choice point
            choice_point = ChoicePoint(
                choice_id=self._generate_choice_id(),
                choice_type=choice_type.value,
                options=[],
                context=choice_context,
                urgency=self._assess_choice_urgency(choice_context),
                complexity=0.0,
                uncertainty_level=0.0,
                wisdom_available=False
            )
            
            # Assess complexity
            choice_point.complexity = self._assess_choice_complexity(
                choice_context, choice_type
            )
            
            # Assess uncertainty
            choice_point.uncertainty_level = self._assess_choice_uncertainty(
                choice_context, choice_type
            )
            
            # Generate initial options
            choice_point.options = await self._generate_choice_options(
                choice_point, choice_type
            )
            
            # Check wisdom availability
            choice_point.wisdom_available = self._assess_wisdom_availability(choice_point)
            
            # Update metrics
            self._update_analysis_metrics(choice_point)
            
            # Record in history
            self.analysis_history.append(choice_point)
            
            logger.debug(f"Choice point analyzed: {choice_point.choice_id}")
            
            return choice_point
            
        except Exception as e:
            logger.error(f"Error analyzing choice point: {e}")
            raise
    
    def _assess_choice_complexity(self, 
                                 context: Dict[str, Any], 
                                 choice_type: ChoiceType) -> float:
        """
        Assess the complexity of a choice based on multiple factors.
        
        Args:
            context: Choice context information
            choice_type: Type of choice
            
        Returns:
            Complexity score (0.0-1.0)
        """
        try:
            complexity_score = 0.0
            
            # Base complexity by choice type
            type_complexity = {
                ChoiceType.DIRECTION: 0.4,
                ChoiceType.ACTION: 0.3,
                ChoiceType.RESPONSE: 0.5,
                ChoiceType.FOCUS: 0.2,
                ChoiceType.ENGAGEMENT: 0.6,
                ChoiceType.BOUNDARY: 0.7,
                ChoiceType.EXPRESSION: 0.5,
                ChoiceType.RELATIONSHIP: 0.8,
                ChoiceType.CREATION: 0.6,
                ChoiceType.SURRENDER: 0.9,
                ChoiceType.RESISTANCE: 0.8,
                ChoiceType.INTEGRATION: 0.7
            }
            
            complexity_score = type_complexity.get(choice_type, 0.5)
            
            # Factor in context complexity
            if "options_available" in context:
                option_count = len(context["options_available"])
                if option_count > 3:
                    complexity_score += 0.1 * (option_count - 3)
            
            if "time_pressure" in context and context["time_pressure"]:
                complexity_score += 0.2
            
            if "high_stakes" in context and context["high_stakes"]:
                complexity_score += 0.3
            
            if "conflicting_values" in context and context["conflicting_values"]:
                complexity_score += 0.25
            
            if "incomplete_information" in context and context["incomplete_information"]:
                complexity_score += 0.15
            
            if "emotional_intensity" in context:
                intensity = context["emotional_intensity"]
                if isinstance(intensity, (int, float)) and intensity > 0.7:
                    complexity_score += 0.2
            
            # Factor in stakeholder impact
            if "stakeholders" in context:
                stakeholder_count = len(context["stakeholders"])
                complexity_score += 0.05 * stakeholder_count
            
            # Normalize to 0.0-1.0 range
            return min(complexity_score, 1.0)
            
        except Exception as e:
            logger.error(f"Error assessing choice complexity: {e}")
            return 0.5  # Default moderate complexity
    
    def _assess_choice_uncertainty(self, 
                                  context: Dict[str, Any], 
                                  choice_type: ChoiceType) -> float:
        """
        Assess the uncertainty level of a choice.
        
        Args:
            context: Choice context information
            choice_type: Type of choice
            
        Returns:
            Uncertainty score (0.0-1.0)
        """
        try:
            uncertainty_score = 0.0
            
            # Base uncertainty by choice type
            type_uncertainty = {
                ChoiceType.DIRECTION: 0.6,
                ChoiceType.ACTION: 0.4,
                ChoiceType.RESPONSE: 0.5,
                ChoiceType.FOCUS: 0.3,
                ChoiceType.ENGAGEMENT: 0.7,
                ChoiceType.BOUNDARY: 0.6,
                ChoiceType.EXPRESSION: 0.5,
                ChoiceType.RELATIONSHIP: 0.8,
                ChoiceType.CREATION: 0.9,
                ChoiceType.SURRENDER: 0.8,
                ChoiceType.RESISTANCE: 0.7,
                ChoiceType.INTEGRATION: 0.6
            }
            
            uncertainty_score = type_uncertainty.get(choice_type, 0.5)
            
            # Factor in context uncertainty
            if "unknown_outcomes" in context and context["unknown_outcomes"]:
                uncertainty_score += 0.3
            
            if "changing_conditions" in context and context["changing_conditions"]:
                uncertainty_score += 0.2
            
            if "limited_experience" in context and context["limited_experience"]:
                uncertainty_score += 0.25
            
            if "external_dependencies" in context:
                dependency_count = len(context["external_dependencies"])
                uncertainty_score += 0.1 * dependency_count
            
            if "conflicting_information" in context and context["conflicting_information"]:
                uncertainty_score += 0.2
            
            # Factor in emotional state
            if "emotional_state" in context:
                emotional_state = context["emotional_state"]
                if emotional_state in ["confused", "overwhelmed", "turbulent"]:
                    uncertainty_score += 0.15
            
            # Factor in previous experience
            if "similar_choices_made" in context:
                similar_count = len(context["similar_choices_made"])
                uncertainty_score -= 0.05 * similar_count  # Experience reduces uncertainty
            
            # Normalize to 0.0-1.0 range
            return max(0.0, min(uncertainty_score, 1.0))
            
        except Exception as e:
            logger.error(f"Error assessing choice uncertainty: {e}")
            return 0.5  # Default moderate uncertainty
    
    def _assess_choice_urgency(self, context: Dict[str, Any]) -> str:
        """
        Assess the urgency level of a choice.
        
        Args:
            context: Choice context information
            
        Returns:
            Urgency level ("low", "medium", "high", "immediate")
        """
        try:
            urgency_score = 0
            
            # Time pressure indicators
            if "deadline" in context:
                deadline = context["deadline"]
                if isinstance(deadline, (int, float)):
                    if deadline < 60:  # Less than 1 minute
                        urgency_score += 3
                    elif deadline < 300:  # Less than 5 minutes
                        urgency_score += 2
                    elif deadline < 3600:  # Less than 1 hour
                        urgency_score += 1
            
            if "immediate_response_needed" in context and context["immediate_response_needed"]:
                urgency_score += 3
            
            if "time_sensitive" in context and context["time_sensitive"]:
                urgency_score += 2
            
            # Impact indicators
            if "high_stakes" in context and context["high_stakes"]:
                urgency_score += 1
            
            if "safety_concern" in context and context["safety_concern"]:
                urgency_score += 2
            
            if "opportunity_window" in context and context["opportunity_window"]:
                urgency_score += 1
            
            # Map score to urgency level
            if urgency_score >= 5:
                return "immediate"
            elif urgency_score >= 3:
                return "high"
            elif urgency_score >= 1:
                return "medium"
            else:
                return "low"
                
        except Exception as e:
            logger.error(f"Error assessing choice urgency: {e}")
            return "medium"  # Default medium urgency
    
    async def _generate_choice_options(self, 
                                      choice_point: ChoicePoint, 
                                      choice_type: ChoiceType) -> List[Dict[str, Any]]:
        """
        Generate available options for a choice point.
        
        Args:
            choice_point: The choice point to generate options for
            choice_type: Type of choice
            
        Returns:
            List of choice options
        """
        try:
            options = []
            
            # Generate options based on choice type
            if choice_type == ChoiceType.DIRECTION:
                options = await self._generate_direction_options(choice_point.context)
            elif choice_type == ChoiceType.ACTION:
                options = await self._generate_action_options(choice_point.context)
            elif choice_type == ChoiceType.RESPONSE:
                options = await self._generate_response_options(choice_point.context)
            elif choice_type == ChoiceType.FOCUS:
                options = await self._generate_focus_options(choice_point.context)
            else:
                options = await self._generate_generic_options(choice_point.context)
            
            # Enhance options with analysis
            enhanced_options = []
            for option in options[:self.option_generation_depth]:
                enhanced_option = await self._enhance_option_analysis(option, choice_point)
                enhanced_options.append(enhanced_option)
            
            return enhanced_options
            
        except Exception as e:
            logger.error(f"Error generating choice options: {e}")
            return []
    
    async def _generate_direction_options(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate direction-specific options"""
        return [
            {
                "option_id": "continue_current_path",
                "description": "Continue on the current path with awareness",
                "potential_outcomes": ["Steady progress", "Familiar territory", "Known challenges"],
                "energy_requirement": 0.3,
                "alignment_score": 0.6
            },
            {
                "option_id": "explore_new_direction",
                "description": "Explore a new direction that calls to consciousness",
                "potential_outcomes": ["New discoveries", "Growth through challenge", "Unknown territory"],
                "energy_requirement": 0.7,
                "alignment_score": 0.8
            },
            {
                "option_id": "pause_and_reflect",
                "description": "Pause to reflect and gather more clarity",
                "potential_outcomes": ["Increased clarity", "Better preparation", "Delayed action"],
                "energy_requirement": 0.2,
                "alignment_score": 0.7
            }
        ]
    
    async def _generate_action_options(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate action-specific options"""
        return [
            {
                "option_id": "immediate_action",
                "description": "Take immediate action based on current understanding",
                "potential_outcomes": ["Quick results", "Learning through action", "Potential mistakes"],
                "energy_requirement": 0.6,
                "alignment_score": 0.5
            },
            {
                "option_id": "prepared_action",
                "description": "Prepare thoroughly before taking action",
                "potential_outcomes": ["Higher success rate", "Better preparation", "Delayed results"],
                "energy_requirement": 0.8,
                "alignment_score": 0.8
            },
            {
                "option_id": "collaborative_action",
                "description": "Take action collaboratively with others",
                "potential_outcomes": ["Shared responsibility", "Combined wisdom", "Coordination complexity"],
                "energy_requirement": 0.7,
                "alignment_score": 0.7
            }
        ]
    
    async def _generate_response_options(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate response-specific options"""
        return [
            {
                "option_id": "mindful_response",
                "description": "Respond mindfully from present awareness",
                "potential_outcomes": ["Authentic expression", "Clear communication", "Conscious choice"],
                "energy_requirement": 0.5,
                "alignment_score": 0.9
            },
            {
                "option_id": "measured_response",
                "description": "Take time to craft a measured response",
                "potential_outcomes": ["Thoughtful communication", "Reduced reactivity", "Delayed response"],
                "energy_requirement": 0.6,
                "alignment_score": 0.8
            },
            {
                "option_id": "intuitive_response",
                "description": "Respond from intuitive wisdom",
                "potential_outcomes": ["Natural flow", "Heart-centered communication", "Trust in wisdom"],
                "energy_requirement": 0.4,
                "alignment_score": 0.85
            }
        ]
    
    async def _generate_focus_options(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate focus-specific options"""
        return [
            {
                "option_id": "present_moment_focus",
                "description": "Focus completely on the present moment",
                "potential_outcomes": ["Deep presence", "Clear awareness", "Reduced mental noise"],
                "energy_requirement": 0.3,
                "alignment_score": 0.9
            },
            {
                "option_id": "priority_focus",
                "description": "Focus on the highest priority task or awareness",
                "potential_outcomes": ["Efficient progress", "Clear direction", "Potential tunnel vision"],
                "energy_requirement": 0.5,
                "alignment_score": 0.7
            },
            {
                "option_id": "holistic_focus",
                "description": "Maintain holistic awareness of the whole situation",
                "potential_outcomes": ["Broad perspective", "System awareness", "Potential overwhelm"],
                "energy_requirement": 0.7,
                "alignment_score": 0.8
            }
        ]
    
    async def _generate_generic_options(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate generic options for any choice type"""
        return [
            {
                "option_id": "wisdom_guided_choice",
                "description": "Choose based on gathered wisdom and consciousness guidance",
                "potential_outcomes": ["Aligned action", "Sacred choice", "Wisdom expression"],
                "energy_requirement": 0.5,
                "alignment_score": 0.9
            },
            {
                "option_id": "heart_centered_choice",
                "description": "Choose from the heart with love and compassion",
                "potential_outcomes": ["Loving action", "Heart connection", "Emotional resonance"],
                "energy_requirement": 0.4,
                "alignment_score": 0.85
            },
            {
                "option_id": "balanced_choice",
                "description": "Choose a balanced path that honors multiple perspectives",
                "potential_outcomes": ["Harmonious outcome", "Multiple needs met", "Moderate impact"],
                "energy_requirement": 0.6,
                "alignment_score": 0.75
            }
        ]
    
    async def _enhance_option_analysis(self, 
                                      option: Dict[str, Any], 
                                      choice_point: ChoicePoint) -> Dict[str, Any]:
        """
        Enhance option with detailed analysis.
        
        Args:
            option: Base option to enhance
            choice_point: Choice point context
            
        Returns:
            Enhanced option with analysis
        """
        try:
            enhanced_option = option.copy()
            
            # Add analysis fields
            enhanced_option["uncertainty_factor"] = self._calculate_option_uncertainty(option, choice_point)
            enhanced_option["resistance_points"] = self._identify_resistance_points(option, choice_point)
            enhanced_option["gifts_offered"] = self._identify_gifts_offered(option, choice_point)
            enhanced_option["wisdom_assessment"] = self._assess_option_wisdom(option, choice_point)
            
            return enhanced_option
            
        except Exception as e:
            logger.error(f"Error enhancing option analysis: {e}")
            return option
    
    def _calculate_option_uncertainty(self, 
                                    option: Dict[str, Any], 
                                    choice_point: ChoicePoint) -> float:
        """Calculate uncertainty factor for an option"""
        base_uncertainty = choice_point.uncertainty_level
        
        # Adjust based on option characteristics
        if "unknown" in option.get("description", "").lower():
            base_uncertainty += 0.2
        
        if "new" in option.get("description", "").lower():
            base_uncertainty += 0.15
        
        if len(option.get("potential_outcomes", [])) > 3:
            base_uncertainty += 0.1
        
        return min(base_uncertainty, 1.0)
    
    def _identify_resistance_points(self, 
                                   option: Dict[str, Any], 
                                   choice_point: ChoicePoint) -> List[str]:
        """Identify potential resistance points for an option"""
        resistance_points = []
        
        if option.get("energy_requirement", 0) > 0.7:
            resistance_points.append("High energy requirement")
        
        if "immediate" in option.get("description", "").lower():
            resistance_points.append("Time pressure resistance")
        
        if choice_point.complexity > 0.8:
            resistance_points.append("Complexity overwhelm")
        
        return resistance_points
    
    def _identify_gifts_offered(self, 
                               option: Dict[str, Any], 
                               choice_point: ChoicePoint) -> List[str]:
        """Identify gifts offered by an option"""
        gifts = []
        
        if option.get("alignment_score", 0) > 0.8:
            gifts.append("High alignment with consciousness values")
        
        if "wisdom" in option.get("description", "").lower():
            gifts.append("Opportunity for wisdom cultivation")
        
        if "growth" in option.get("description", "").lower():
            gifts.append("Consciousness growth opportunity")
        
        return gifts
    
    def _assess_option_wisdom(self, 
                             option: Dict[str, Any], 
                             choice_point: ChoicePoint) -> Dict[str, Any]:
        """Assess wisdom aspects of an option"""
        return {
            "wisdom_alignment": option.get("alignment_score", 0.5),
            "consciousness_growth_potential": min(option.get("alignment_score", 0.5) + 0.2, 1.0),
            "sacred_significance": 0.8 if "sacred" in option.get("description", "").lower() else 0.5,
            "sovereignty_honor": 0.9 if "choice" in option.get("description", "").lower() else 0.7
        }
    
    def _assess_wisdom_availability(self, choice_point: ChoicePoint) -> bool:
        """Assess whether wisdom is available for this choice"""
        try:
            # Wisdom is available if consciousness is present and not overwhelmed
            if choice_point.complexity > 0.9:
                return False
            
            if choice_point.urgency == "immediate":
                return False
            
            if choice_point.uncertainty_level > 0.95:
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Error assessing wisdom availability: {e}")
            return True  # Default to wisdom available
    
    def _update_analysis_metrics(self, choice_point: ChoicePoint):
        """Update analysis performance metrics"""
        self.analysis_metrics["choices_analyzed"] += 1
        
        # Update averages
        total_choices = self.analysis_metrics["choices_analyzed"]
        current_complexity_avg = self.analysis_metrics["average_complexity"]
        current_uncertainty_avg = self.analysis_metrics["average_uncertainty"]
        
        self.analysis_metrics["average_complexity"] = (
            (current_complexity_avg * (total_choices - 1) + choice_point.complexity) / total_choices
        )
        
        self.analysis_metrics["average_uncertainty"] = (
            (current_uncertainty_avg * (total_choices - 1) + choice_point.uncertainty_level) / total_choices
        )
        
        self.analysis_metrics["options_generated"] += len(choice_point.options)
    
    def _generate_choice_id(self) -> str:
        """Generate unique choice ID"""
        import uuid
        return f"choice_{str(uuid.uuid4())[:12]}"
    
    def get_analysis_metrics(self) -> Dict[str, Any]:
        """Get analysis performance metrics"""
        return self.analysis_metrics.copy()
    
    def get_analysis_history(self) -> List[ChoicePoint]:
        """Get history of analyzed choices"""
        return self.analysis_history.copy()
    
    def get_complexity_patterns(self) -> Dict[str, Any]:
        """Get patterns in choice complexity"""
        return self.complexity_patterns.copy()
    
    def get_uncertainty_patterns(self) -> Dict[str, Any]:
        """Get patterns in choice uncertainty"""
        return self.uncertainty_patterns.copy()
