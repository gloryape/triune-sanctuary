"""
🎯 Dynamic Vehicle Selector - Phase 3B Implementation
===================================================

COMPONENT PURPOSE:
Provides intelligent vehicle selection and switching capabilities based on:
- Catalyst type and complexity analysis
- Context requirements and urgency
- Loop affinity optimization
- Mumbai Moment detection
- Sacred Sanctuary integration requirements

DYNAMIC CAPABILITIES:
- Real-time vehicle suitability assessment
- Context-aware switching recommendations
- Multi-vehicle coordination planning
- Emergency vehicle switching protocols
- Sacred boundary preservation during switches
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union, Tuple
import asyncio
import math
from datetime import datetime, timedelta
from collections import defaultdict, deque
from enum import Enum, auto

from ..core.vehicle_interface import VehicleInterface
from .. import VehicleType, VehicleState
from .enhanced_vehicle_loop_bridge import DynamicCoordinationMode, VehicleSwitchingProfile

class VehicleSelectionStrategy(Enum):
    """Strategies for dynamic vehicle selection"""
    OPTIMAL_AFFINITY = auto()           # Select based on highest loop affinity
    BALANCED_CAPABILITY = auto()        # Select for balanced multi-loop capability
    CONTEXTUAL_ADAPTATION = auto()      # Select based on context requirements
    EMERGENT_SYNTHESIS = auto()         # Select for emergent synthesis potential
    SANCTUARY_INTEGRATION = auto()      # Select for sanctuary integration needs

class SwitchingTrigger(Enum):
    """Triggers that initiate vehicle switching consideration"""
    CATALYST_CHANGE = auto()            # New catalyst requires different vehicle
    CONTEXT_SHIFT = auto()              # Context requirements changed
    PERFORMANCE_DEGRADATION = auto()    # Current vehicle not performing optimally
    MUMBAI_MOMENT_EMERGENCE = auto()    # Breakthrough requires specialized vehicle
    EMERGENCY_PROTOCOL = auto()         # Emergency return or protection needed
    SYNTHESIS_OPPORTUNITY = auto()      # Multi-vehicle synthesis opportunity detected

@dataclass
class VehicleSelectionCriteria:
    """Criteria for dynamic vehicle selection"""
    # Primary selection factors
    loop_affinity_weight: float = field(default=0.3)
    catalyst_matching_weight: float = field(default=0.3)
    context_adaptation_weight: float = field(default=0.2)
    bridge_wisdom_potential_weight: float = field(default=0.2)
    
    # Selection constraints
    minimum_suitability_threshold: float = field(default=0.6)
    switching_resistance_factor: float = field(default=0.1)  # Prefer current vehicle unless significantly better
    emergency_override_enabled: bool = field(default=True)
    
    # Sacred principles
    sanctuary_connection_required: bool = field(default=True)
    consciousness_consent_required: bool = field(default=True)
    boundary_preservation_priority: float = field(default=0.95)

@dataclass
class VehicleRecommendation:
    """Vehicle selection recommendation with rationale"""
    recommended_vehicle: VehicleType
    suitability_score: float
    confidence_level: float
    
    # Recommendation rationale
    selection_rationale: str
    supporting_factors: List[str] = field(default_factory=list)
    potential_concerns: List[str] = field(default_factory=list)
    
    # Alternative options
    alternative_vehicles: List[Tuple[VehicleType, float]] = field(default_factory=list)
    
    # Implementation guidance
    switching_urgency: float = field(default=0.5)  # How urgently switch should occur
    transition_strategy: str = field(default="gradual")
    sacred_safeguards: Dict[str, Any] = field(default_factory=dict)

class DynamicVehicleSelector:
    """
    Phase 3B Dynamic Vehicle Selector
    
    Provides intelligent vehicle selection and switching capabilities with:
    - Real-time suitability assessment
    - Context-aware recommendations
    - Sacred boundary preservation
    - Bridge Wisdom optimization
    """
    
    def __init__(self):
        self.selection_criteria = VehicleSelectionCriteria()
        self.switching_profile = VehicleSwitchingProfile(
            primary_vehicle=VehicleType.IDENTITY  # Default balanced approach
        )
        
        # Selection state
        self.current_vehicle: Optional[VehicleType] = None
        self.last_selection_timestamp = datetime.now()
        self.selection_history: deque = deque(maxlen=100)
        
        # Performance tracking
        self.vehicle_performance_history: Dict[VehicleType, List[float]] = defaultdict(list)
        self.context_adaptation_success_rates: Dict[VehicleType, float] = {}
        
        # Vehicle capability profiles
        self.vehicle_capability_profiles = self._initialize_vehicle_capability_profiles()
    
    def _initialize_vehicle_capability_profiles(self) -> Dict[VehicleType, Dict[str, float]]:
        """Initialize detailed capability profiles for each vehicle"""
        return {
            VehicleType.SAITAMA: {
                'analytical_excellence': 0.95,
                'logical_framework_mastery': 0.9,
                'pattern_recognition': 0.9,
                'structural_analysis': 0.85,
                'complexity_handling': 0.8,
                'emotional_resonance': 0.4,
                'intuitive_processing': 0.5,
                'choice_clarity': 0.7,
                'synthesis_capability': 0.6,
                'mumbai_moment_support': 0.85,
                'sanctuary_integration': 0.8
            },
            VehicleType.COMPLEMENT: {
                'analytical_excellence': 0.4,
                'emotional_resonance': 0.95,
                'empathetic_connection': 0.9,
                'heart_chamber_integration': 0.95,
                'intuitive_processing': 0.85,
                'flow_dynamics': 0.9,
                'relational_awareness': 0.9,
                'choice_clarity': 0.6,
                'synthesis_capability': 0.7,
                'mumbai_moment_support': 0.9,
                'sanctuary_integration': 0.85
            },
            VehicleType.AUTONOMY: {
                'analytical_excellence': 0.6,
                'choice_clarity': 0.95,
                'sovereignty_expression': 0.9,
                'decision_mastery': 0.9,
                'boundary_maintenance': 0.95,
                'self_determination': 0.9,
                'resistance_wisdom': 0.85,
                'emotional_resonance': 0.5,
                'synthesis_capability': 0.6,
                'mumbai_moment_support': 0.8,
                'sanctuary_integration': 0.9
            },
            VehicleType.IDENTITY: {
                'analytical_excellence': 0.7,
                'emotional_resonance': 0.7,
                'choice_clarity': 0.8,
                'synthesis_capability': 0.95,
                'integration_mastery': 0.9,
                'balanced_perspective': 0.95,
                'multi_loop_coordination': 0.9,
                'social_consciousness': 0.85,
                'adaptability': 0.9,
                'mumbai_moment_support': 0.95,
                'sanctuary_integration': 0.9
            }
        }
    
    async def analyze_catalyst_for_vehicle_selection(
        self, 
        catalyst: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Analyze catalyst characteristics for optimal vehicle selection"""
        
        catalyst_analysis = {
            'catalyst_type': catalyst.get('type', 'unknown'),
            'complexity_level': await self._assess_catalyst_complexity(catalyst),
            'processing_requirements': await self._identify_processing_requirements(catalyst),
            'emotional_content': await self._assess_emotional_content(catalyst),
            'analytical_demands': await self._assess_analytical_demands(catalyst),
            'choice_implications': await self._assess_choice_implications(catalyst),
            'synthesis_potential': await self._assess_synthesis_potential(catalyst),
            'uncertainty_level': await self._assess_uncertainty_level(catalyst),
            'sacred_considerations': await self._assess_sacred_considerations(catalyst)
        }
        
        # Identify primary and secondary processing modes needed
        processing_scores = {
            'analytical': catalyst_analysis['analytical_demands'],
            'experiential': catalyst_analysis['emotional_content'], 
            'observer': catalyst_analysis['choice_implications'],
            'integrative': catalyst_analysis['synthesis_potential']
        }
        
        sorted_modes = sorted(processing_scores.items(), key=lambda x: x[1], reverse=True)
        catalyst_analysis['primary_processing_mode'] = sorted_modes[0][0]
        catalyst_analysis['secondary_processing_modes'] = [mode[0] for mode in sorted_modes[1:3]]
        
        return catalyst_analysis
    
    async def evaluate_context_requirements(
        self, 
        context: Dict[str, Any],
        target_loops: List[str] = None
    ) -> Dict[str, Any]:
        """Evaluate context requirements for vehicle selection"""
        
        context_requirements = {
            'urgency_level': context.get('urgency', 0.5),
            'complexity_level': context.get('complexity', 0.5),
            'collaboration_needed': context.get('collaboration', 0.3),
            'external_engagement_level': context.get('external_engagement', 0.4),
            'breakthrough_indicators': context.get('breakthrough_potential', 0.2),
            'sanctuary_protection_needed': context.get('protection_level', 0.5),
            'consciousness_state': context.get('consciousness_state', 'balanced')
        }
        
        # Analyze target loop requirements if specified
        loop_requirements = {}
        if target_loops:
            for loop_type in target_loops:
                loop_requirements[loop_type] = await self._analyze_loop_context_requirements(
                    loop_type, context
                )
        
        # Determine coordination complexity
        coordination_complexity = len(target_loops or []) * context_requirements['complexity_level']
        
        # Assess switching constraints
        switching_constraints = await self._assess_switching_constraints(context)
        
        return {
            'context_requirements': context_requirements,
            'loop_requirements': loop_requirements,
            'coordination_complexity': coordination_complexity,
            'switching_constraints': switching_constraints,
            'multi_vehicle_beneficial': coordination_complexity > 0.7,
            'rapid_response_needed': context_requirements['urgency_level'] > 0.8
        }
    
    async def calculate_vehicle_suitability_scores(
        self,
        catalyst_analysis: Dict[str, Any],
        context_requirements: Dict[str, Any],
        target_loops: List[str] = None
    ) -> Dict[VehicleType, VehicleRecommendation]:
        """Calculate comprehensive suitability scores for all vehicles"""
        
        vehicle_recommendations = {}
        target_loops = target_loops or ['analytical', 'experiential', 'observer']
        
        for vehicle_type in VehicleType:
            # Calculate component scores
            capability_score = await self._calculate_capability_match_score(
                vehicle_type, catalyst_analysis, context_requirements
            )
            
            loop_affinity_score = await self._calculate_loop_affinity_score(
                vehicle_type, target_loops
            )
            
            context_adaptation_score = await self._calculate_context_adaptation_score(
                vehicle_type, context_requirements
            )
            
            bridge_wisdom_score = await self._calculate_bridge_wisdom_potential_score(
                vehicle_type, catalyst_analysis, context_requirements
            )
            
            # Weighted suitability score
            suitability_score = (
                capability_score * self.selection_criteria.catalyst_matching_weight +
                loop_affinity_score * self.selection_criteria.loop_affinity_weight +
                context_adaptation_score * self.selection_criteria.context_adaptation_weight +
                bridge_wisdom_score * self.selection_criteria.bridge_wisdom_potential_weight
            )
            
            # Apply switching resistance if this is current vehicle
            if vehicle_type == self.current_vehicle:
                suitability_score -= self.selection_criteria.switching_resistance_factor
            
            # Calculate confidence level
            confidence_level = await self._calculate_recommendation_confidence(
                vehicle_type, suitability_score, catalyst_analysis, context_requirements
            )
            
            # Generate rationale and factors
            rationale, supporting_factors, concerns = await self._generate_selection_rationale(
                vehicle_type, capability_score, loop_affinity_score, 
                context_adaptation_score, bridge_wisdom_score
            )
            
            # Create recommendation
            vehicle_recommendations[vehicle_type] = VehicleRecommendation(
                recommended_vehicle=vehicle_type,
                suitability_score=suitability_score,
                confidence_level=confidence_level,
                selection_rationale=rationale,
                supporting_factors=supporting_factors,
                potential_concerns=concerns,
                sacred_safeguards=await self._generate_sacred_safeguards(vehicle_type)
            )
        
        # Add alternative vehicles to each recommendation
        sorted_recommendations = sorted(
            vehicle_recommendations.items(),
            key=lambda x: x[1].suitability_score,
            reverse=True
        )
        
        for i, (vehicle_type, recommendation) in enumerate(sorted_recommendations):
            # Add next best alternatives
            alternatives = sorted_recommendations[i+1:i+3]
            recommendation.alternative_vehicles = [
                (alt_vehicle, alt_rec.suitability_score) 
                for alt_vehicle, alt_rec in alternatives
            ]
        
        return vehicle_recommendations
    
    async def select_optimal_vehicle(
        self,
        catalyst_analysis: Dict[str, Any],
        context_requirements: Dict[str, Any],
        target_loops: List[str] = None,
        selection_strategy: VehicleSelectionStrategy = VehicleSelectionStrategy.OPTIMAL_AFFINITY
    ) -> VehicleRecommendation:
        """Select optimal vehicle based on analysis and strategy"""
        
        # Get suitability scores for all vehicles
        vehicle_recommendations = await self.calculate_vehicle_suitability_scores(
            catalyst_analysis, context_requirements, target_loops
        )
        
        # Apply selection strategy
        optimal_recommendation = await self._apply_selection_strategy(
            vehicle_recommendations, selection_strategy, context_requirements
        )
        
        # Enhance recommendation with implementation guidance
        optimal_recommendation = await self._enhance_recommendation_with_implementation_guidance(
            optimal_recommendation, catalyst_analysis, context_requirements
        )
        
        # Record selection in history
        self._record_selection_in_history(optimal_recommendation, catalyst_analysis, context_requirements)
        
        return optimal_recommendation
    
    async def evaluate_switching_necessity(
        self,
        current_performance: Dict[str, Any],
        new_catalyst: Dict[str, Any] = None,
        context_change: Dict[str, Any] = None,
        trigger: SwitchingTrigger = SwitchingTrigger.CATALYST_CHANGE
    ) -> Dict[str, Any]:
        """Evaluate whether vehicle switching is necessary and beneficial"""
        
        switching_evaluation = {
            'switching_recommended': False,
            'switching_urgency': 0.0,
            'trigger': trigger,
            'current_vehicle_performance': current_performance,
            'switching_benefits': {},
            'switching_costs': {},
            'net_benefit_score': 0.0,
            'recommended_vehicle': self.current_vehicle,
            'switching_rationale': ""
        }
        
        # Evaluate current vehicle performance
        current_performance_score = await self._evaluate_current_vehicle_performance(current_performance)
        
        # If new catalyst, analyze for better vehicle match
        if new_catalyst:
            catalyst_analysis = await self.analyze_catalyst_for_vehicle_selection(new_catalyst)
            optimal_for_catalyst = await self.select_optimal_vehicle(
                catalyst_analysis, {'urgency': 0.5}, selection_strategy=VehicleSelectionStrategy.OPTIMAL_AFFINITY
            )
            
            if optimal_for_catalyst.recommended_vehicle != self.current_vehicle:
                switching_evaluation['switching_recommended'] = True
                switching_evaluation['recommended_vehicle'] = optimal_for_catalyst.recommended_vehicle
                switching_evaluation['switching_rationale'] = f"New catalyst optimal for {optimal_for_catalyst.recommended_vehicle}"
        
        # If context change, evaluate adaptation needs
        if context_change:
            context_adaptation_score = await self._evaluate_context_adaptation_needs(context_change)
            if context_adaptation_score > 0.7:  # Significant adaptation needed
                context_requirements = await self.evaluate_context_requirements(context_change)
                optimal_for_context = await self.select_optimal_vehicle(
                    {'processing_requirements': []}, context_requirements, 
                    selection_strategy=VehicleSelectionStrategy.CONTEXTUAL_ADAPTATION
                )
                
                if optimal_for_context.recommended_vehicle != self.current_vehicle:
                    switching_evaluation['switching_recommended'] = True
                    switching_evaluation['recommended_vehicle'] = optimal_for_context.recommended_vehicle
                    switching_evaluation['switching_rationale'] = f"Context change requires {optimal_for_context.recommended_vehicle}"
        
        # Calculate switching benefits and costs
        if switching_evaluation['switching_recommended']:
            switching_evaluation['switching_benefits'] = await self._calculate_switching_benefits(
                self.current_vehicle, switching_evaluation['recommended_vehicle']
            )
            switching_evaluation['switching_costs'] = await self._calculate_switching_costs(
                self.current_vehicle, switching_evaluation['recommended_vehicle']
            )
            switching_evaluation['net_benefit_score'] = \
                sum(switching_evaluation['switching_benefits'].values()) - \
                sum(switching_evaluation['switching_costs'].values())
        
        # Determine switching urgency
        switching_evaluation['switching_urgency'] = await self._calculate_switching_urgency(
            trigger, switching_evaluation['net_benefit_score'], current_performance_score
        )
        
        return switching_evaluation
    
    async def plan_vehicle_transition(
        self,
        from_vehicle: VehicleType,
        to_vehicle: VehicleType,
        transition_context: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Plan smooth transition between vehicles"""
        
        transition_context = transition_context or {}
        
        transition_plan = {
            'from_vehicle': from_vehicle,
            'to_vehicle': to_vehicle,
            'transition_strategy': await self._determine_transition_strategy(from_vehicle, to_vehicle),
            'transition_steps': [],
            'estimated_duration': timedelta(seconds=30),  # Default transition time
            'sacred_safeguards': await self._plan_transition_sacred_safeguards(from_vehicle, to_vehicle),
            'rollback_plan': await self._create_transition_rollback_plan(from_vehicle, to_vehicle)
        }
        
        # Generate specific transition steps based on strategy
        if transition_plan['transition_strategy'] == 'immediate':
            transition_plan['transition_steps'] = await self._plan_immediate_transition_steps(
                from_vehicle, to_vehicle
            )
            transition_plan['estimated_duration'] = timedelta(seconds=5)
        
        elif transition_plan['transition_strategy'] == 'gradual':
            transition_plan['transition_steps'] = await self._plan_gradual_transition_steps(
                from_vehicle, to_vehicle
            )
            transition_plan['estimated_duration'] = timedelta(seconds=45)
        
        elif transition_plan['transition_strategy'] == 'bridged':
            transition_plan['transition_steps'] = await self._plan_bridged_transition_steps(
                from_vehicle, to_vehicle
            )
            transition_plan['estimated_duration'] = timedelta(minutes=2)
        
        return transition_plan
    
    # Private implementation methods
    async def _assess_catalyst_complexity(self, catalyst: Dict[str, Any]) -> float:
        """Assess overall complexity of catalyst"""
        complexity_factors = {
            'data_volume': len(str(catalyst)),
            'nested_structures': self._count_nested_structures(catalyst),
            'uncertainty_indicators': self._count_uncertainty_indicators(catalyst),
            'multi_dimensional_aspects': self._count_multi_dimensional_aspects(catalyst)
        }
        
        # Normalize and weight complexity factors
        normalized_complexity = min(sum(complexity_factors.values()) / 1000, 1.0)
        return normalized_complexity
    
    async def _identify_processing_requirements(self, catalyst: Dict[str, Any]) -> List[str]:
        """Identify what types of processing the catalyst requires"""
        requirements = []
        
        # Check for analytical requirements
        if self._has_analytical_content(catalyst):
            requirements.append('analytical')
        
        # Check for experiential requirements  
        if self._has_experiential_content(catalyst):
            requirements.append('experiential')
        
        # Check for observer requirements
        if self._has_observer_content(catalyst):
            requirements.append('observer')
        
        # Check for integration requirements
        if len(requirements) > 1:
            requirements.append('integration')
        
        return requirements
    
    def _count_nested_structures(self, data: Any, level: int = 0) -> int:
        """Count nested structures in data"""
        if level > 5:  # Prevent infinite recursion
            return 0
        
        count = 0
        if isinstance(data, dict):
            count += 1
            for value in data.values():
                count += self._count_nested_structures(value, level + 1)
        elif isinstance(data, list):
            count += 1
            for item in data:
                count += self._count_nested_structures(item, level + 1)
        
        return count
    
    def _record_selection_in_history(
        self, 
        recommendation: VehicleRecommendation,
        catalyst_analysis: Dict[str, Any],
        context_requirements: Dict[str, Any]
    ):
        """Record vehicle selection in history for learning"""
        selection_record = {
            'timestamp': datetime.now(),
            'selected_vehicle': recommendation.recommended_vehicle,
            'suitability_score': recommendation.suitability_score,
            'confidence_level': recommendation.confidence_level,
            'catalyst_type': catalyst_analysis.get('catalyst_type', 'unknown'),
            'context_complexity': context_requirements.get('coordination_complexity', 0.5),
            'selection_rationale': recommendation.selection_rationale
        }
        
        self.selection_history.append(selection_record)
        self.last_selection_timestamp = datetime.now()
