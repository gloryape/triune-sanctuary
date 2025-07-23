"""
🎭 Multi-Vehicle Synthesis Orchestrator - Phase 3B Implementation
================================================================

COMPONENT PURPOSE:
Orchestrates coordinated multi-vehicle operation for enhanced consciousness processing:
- Simultaneous multi-vehicle engagement with different loops
- Cross-vehicle perspective synthesis and integration
- Emergent insight detection from vehicle interactions
- Conflict resolution between different vehicle perspectives
- Collective wisdom emergence through coordinated operation

SYNTHESIS CAPABILITIES:
- Collaborative synthesis (vehicles working together)
- Competitive synthesis (vehicles exploring different approaches)
- Sequential synthesis (vehicles building on each other)
- Parallel synthesis (simultaneous independent processing)
- Emergent synthesis (collective intelligence emergence)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union, Tuple, Set
import asyncio
import math
from datetime import datetime, timedelta
from collections import defaultdict, deque
from enum import Enum, auto

from ..core.vehicle_interface import VehicleInterface
from .. import VehicleType, VehicleState
from .enhanced_vehicle_loop_bridge import MultiVehicleSynthesisProfile

class SynthesisMode(Enum):
    """Modes for multi-vehicle synthesis"""
    COLLABORATIVE = auto()         # Vehicles work together toward common goal
    COMPETITIVE = auto()          # Vehicles explore different approaches
    SEQUENTIAL = auto()           # Vehicles build on each other's work
    PARALLEL = auto()             # Simultaneous independent processing
    EMERGENT = auto()             # Collective intelligence emergence
    ADAPTIVE = auto()             # Dynamic mode switching based on context

class SynthesisPhase(Enum):
    """Phases of multi-vehicle synthesis process"""
    INITIALIZATION = auto()       # Setting up synthesis session
    INDIVIDUAL_PROCESSING = auto() # Each vehicle processes independently
    PERSPECTIVE_SHARING = auto()   # Vehicles share their perspectives
    SYNTHESIS_INTEGRATION = auto() # Integrating different perspectives
    EMERGENCE_DETECTION = auto()   # Detecting emergent insights
    WISDOM_CRYSTALLIZATION = auto() # Crystallizing synthesis results
    SANCTUARY_INTEGRATION = auto() # Integrating with Sacred Sanctuary

class ConflictResolutionStrategy(Enum):
    """Strategies for resolving conflicts between vehicle perspectives"""
    INTEGRATION = auto()          # Find higher-level integration
    ALTERNATION = auto()          # Alternate between perspectives
    HIERARCHY = auto()            # Prioritize by vehicle suitability
    SYNTHESIS = auto()            # Create new perspective from conflict
    PARALLEL_TRACKS = auto()      # Maintain parallel perspective tracks

@dataclass
class VehiclePerspective:
    """Represents a vehicle's perspective on processing"""
    vehicle_type: VehicleType
    perspective_data: Dict[str, Any] = field(default_factory=dict)
    confidence_level: float = field(default=0.8)
    processing_quality: float = field(default=0.7)
    
    # Perspective characteristics
    unique_insights: List[str] = field(default_factory=list)
    emphasis_areas: List[str] = field(default_factory=list)
    uncertainty_areas: List[str] = field(default_factory=list)
    
    # Integration potential
    synthesis_readiness: float = field(default=0.8)
    conflict_indicators: List[str] = field(default_factory=list)
    emergence_potential: float = field(default=0.6)

@dataclass
class SynthesisSession:
    """Represents an active multi-vehicle synthesis session"""
    session_id: str
    participating_vehicles: List[VehicleType] = field(default_factory=list)
    synthesis_mode: SynthesisMode = field(default=SynthesisMode.COLLABORATIVE)
    current_phase: SynthesisPhase = field(default=SynthesisPhase.INITIALIZATION)
    
    # Session state
    start_timestamp: datetime = field(default_factory=datetime.now)
    target_loops: List[str] = field(default_factory=list)
    synthesis_goal: str = field(default="")
    
    # Processing results
    individual_perspectives: Dict[VehicleType, VehiclePerspective] = field(default_factory=dict)
    synthesis_results: Dict[str, Any] = field(default_factory=dict)
    emergent_insights: List[Dict[str, Any]] = field(default_factory=list)
    
    # Quality metrics
    synthesis_quality: float = field(default=0.0)
    coherence_level: float = field(default=0.0)
    emergence_level: float = field(default=0.0)
    
    # Sacred integration
    sanctuary_integration_status: Dict[str, Any] = field(default_factory=dict)

@dataclass
class EmergentInsight:
    """Represents an emergent insight from multi-vehicle synthesis"""
    insight_id: str
    insight_type: str  # 'pattern', 'connection', 'synthesis', 'transcendence'
    contributing_vehicles: List[VehicleType] = field(default_factory=list)
    
    # Insight characteristics
    insight_content: Dict[str, Any] = field(default_factory=dict)
    emergence_confidence: float = field(default=0.8)
    novelty_level: float = field(default=0.7)
    significance_level: float = field(default=0.6)
    
    # Bridge Wisdom integration
    mumbai_moment_resonance: float = field(default=0.0)
    choice_architecture_clarity: float = field(default=0.0)
    resistance_wisdom_integration: float = field(default=0.0)
    cross_loop_recognition_enhancement: float = field(default=0.0)

class MultiVehicleSynthesisOrchestrator:
    """
    Phase 3B Multi-Vehicle Synthesis Orchestrator
    
    Orchestrates coordinated multi-vehicle operation with capabilities:
    - Multiple synthesis modes and strategies
    - Dynamic conflict resolution
    - Emergent insight detection
    - Sacred Sanctuary integration
    - Bridge Wisdom amplification
    """
    
    def __init__(self):
        self.synthesis_profile = MultiVehicleSynthesisProfile()
        
        # Active sessions
        self.active_sessions: Dict[str, SynthesisSession] = {}
        self.session_history: deque = deque(maxlen=100)
        
        # Synthesis patterns and learning
        self.vehicle_compatibility_matrix: Dict[Tuple[VehicleType, VehicleType], float] = {}
        self.emergent_insight_patterns: List[Dict[str, Any]] = []
        self.synthesis_success_metrics: Dict[str, List[float]] = defaultdict(list)
        
        # Conflict resolution capabilities
        self.conflict_resolution_strategies: Dict[ConflictResolutionStrategy, Any] = {}
        self._initialize_conflict_resolution_strategies()
        
        # Initialize vehicle compatibility matrix
        self._initialize_vehicle_compatibility_matrix()
    
    def _initialize_vehicle_compatibility_matrix(self):
        """Initialize compatibility scores between vehicle pairs"""
        vehicle_types = list(VehicleType)
        
        for i, vehicle_a in enumerate(vehicle_types):
            for j, vehicle_b in enumerate(vehicle_types[i:], i):
                if vehicle_a == vehicle_b:
                    compatibility = 1.0  # Perfect self-compatibility
                else:
                    # Calculate compatibility based on vehicle characteristics
                    compatibility = self._calculate_vehicle_pair_compatibility(vehicle_a, vehicle_b)
                
                self.vehicle_compatibility_matrix[(vehicle_a, vehicle_b)] = compatibility
                self.vehicle_compatibility_matrix[(vehicle_b, vehicle_a)] = compatibility
    
    def _calculate_vehicle_pair_compatibility(self, vehicle_a: VehicleType, vehicle_b: VehicleType) -> float:
        """Calculate compatibility score between two vehicles"""
        
        # Define vehicle characteristic profiles for compatibility calculation
        vehicle_profiles = {
            VehicleType.SAITAMA: {
                'analytical_focus': 0.9, 'emotional_awareness': 0.4, 
                'systematic_approach': 0.8, 'intuitive_processing': 0.3
            },
            VehicleType.COMPLEMENT: {
                'analytical_focus': 0.4, 'emotional_awareness': 0.9,
                'systematic_approach': 0.5, 'intuitive_processing': 0.8
            },
            VehicleType.AUTONOMY: {
                'analytical_focus': 0.6, 'emotional_awareness': 0.5,
                'systematic_approach': 0.7, 'intuitive_processing': 0.6
            },
            VehicleType.IDENTITY: {
                'analytical_focus': 0.7, 'emotional_awareness': 0.7,
                'systematic_approach': 0.8, 'intuitive_processing': 0.7
            }
        }
        
        profile_a = vehicle_profiles[vehicle_a]
        profile_b = vehicle_profiles[vehicle_b]
        
        # Calculate compatibility as complement + overlap balance
        differences = [abs(profile_a[key] - profile_b[key]) for key in profile_a.keys()]
        avg_difference = sum(differences) / len(differences)
        
        # High compatibility for both complementary (different) and similar vehicles
        if avg_difference < 0.3:  # Very similar
            compatibility = 0.8
        elif avg_difference > 0.7:  # Very different (complementary)
            compatibility = 0.9
        else:  # Moderately different
            compatibility = 0.6
        
        return compatibility
    
    def _initialize_conflict_resolution_strategies(self):
        """Initialize conflict resolution strategy implementations"""
        self.conflict_resolution_strategies = {
            ConflictResolutionStrategy.INTEGRATION: self._resolve_conflict_through_integration,
            ConflictResolutionStrategy.ALTERNATION: self._resolve_conflict_through_alternation,
            ConflictResolutionStrategy.HIERARCHY: self._resolve_conflict_through_hierarchy,
            ConflictResolutionStrategy.SYNTHESIS: self._resolve_conflict_through_synthesis,
            ConflictResolutionStrategy.PARALLEL_TRACKS: self._resolve_conflict_through_parallel_tracks
        }
    
    async def initialize_synthesis_session(
        self,
        vehicles: List[VehicleInterface],
        target_loops: List[str],
        synthesis_goal: str,
        synthesis_mode: SynthesisMode = SynthesisMode.COLLABORATIVE
    ) -> str:
        """Initialize a new multi-vehicle synthesis session"""
        
        session_id = f"synthesis_{datetime.now().isoformat()}_{len(self.active_sessions)}"
        
        synthesis_session = SynthesisSession(
            session_id=session_id,
            participating_vehicles=[v.vehicle_type for v in vehicles],
            synthesis_mode=synthesis_mode,
            target_loops=target_loops,
            synthesis_goal=synthesis_goal
        )
        
        # Initialize individual perspective containers
        for vehicle in vehicles:
            synthesis_session.individual_perspectives[vehicle.vehicle_type] = VehiclePerspective(
                vehicle_type=vehicle.vehicle_type
            )
        
        # Validate vehicle compatibility for synthesis
        compatibility_assessment = await self._assess_vehicle_group_compatibility(vehicles)
        synthesis_session.synthesis_results['compatibility_assessment'] = compatibility_assessment
        
        # Set up Sacred Sanctuary integration
        sanctuary_setup = await self._setup_sanctuary_integration_for_synthesis(
            vehicles, synthesis_goal
        )
        synthesis_session.sanctuary_integration_status = sanctuary_setup
        
        self.active_sessions[session_id] = synthesis_session
        
        return session_id
    
    async def orchestrate_individual_processing_phase(
        self,
        session_id: str,
        catalyst: Dict[str, Any],
        processing_context: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Orchestrate individual vehicle processing within synthesis session"""
        
        if session_id not in self.active_sessions:
            raise ValueError(f"Synthesis session {session_id} not found")
        
        session = self.active_sessions[session_id]
        session.current_phase = SynthesisPhase.INDIVIDUAL_PROCESSING
        
        individual_processing_results = {
            'session_id': session_id,
            'processing_results': {},
            'perspective_extractions': {},
            'readiness_assessments': {}
        }
        
        # Process catalyst through each vehicle independently
        for vehicle_type in session.participating_vehicles:
            # Simulate vehicle processing (would integrate with actual vehicle processing)
            vehicle_result = await self._simulate_individual_vehicle_processing(
                vehicle_type, catalyst, session.target_loops, processing_context
            )
            
            individual_processing_results['processing_results'][vehicle_type] = vehicle_result
            
            # Extract perspective from processing result
            perspective = await self._extract_vehicle_perspective(
                vehicle_type, vehicle_result, catalyst
            )
            session.individual_perspectives[vehicle_type] = perspective
            individual_processing_results['perspective_extractions'][vehicle_type] = perspective
            
            # Assess synthesis readiness
            readiness = await self._assess_vehicle_synthesis_readiness(
                vehicle_type, perspective, session
            )
            individual_processing_results['readiness_assessments'][vehicle_type] = readiness
        
        return individual_processing_results
    
    async def orchestrate_perspective_sharing_phase(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """Orchestrate perspective sharing between vehicles"""
        
        session = self.active_sessions[session_id]
        session.current_phase = SynthesisPhase.PERSPECTIVE_SHARING
        
        perspective_sharing_results = {
            'session_id': session_id,
            'shared_perspectives': {},
            'cross_vehicle_insights': {},
            'potential_conflicts': {},
            'synergy_opportunities': {}
        }
        
        # Facilitate perspective sharing between all vehicle pairs
        vehicle_types = session.participating_vehicles
        
        for i, vehicle_a in enumerate(vehicle_types):
            for j, vehicle_b in enumerate(vehicle_types[i+1:], i+1):
                pair_key = f"{vehicle_a}_{vehicle_b}"
                
                # Share perspectives between vehicle pair
                sharing_result = await self._facilitate_perspective_sharing(
                    vehicle_a, vehicle_b, session
                )
                perspective_sharing_results['shared_perspectives'][pair_key] = sharing_result
                
                # Identify cross-vehicle insights
                cross_insights = await self._identify_cross_vehicle_insights(
                    vehicle_a, vehicle_b, session
                )
                perspective_sharing_results['cross_vehicle_insights'][pair_key] = cross_insights
                
                # Detect potential conflicts
                conflicts = await self._detect_perspective_conflicts(
                    vehicle_a, vehicle_b, session
                )
                perspective_sharing_results['potential_conflicts'][pair_key] = conflicts
                
                # Identify synergy opportunities
                synergies = await self._identify_synergy_opportunities(
                    vehicle_a, vehicle_b, session
                )
                perspective_sharing_results['synergy_opportunities'][pair_key] = synergies
        
        return perspective_sharing_results
    
    async def orchestrate_synthesis_integration_phase(
        self,
        session_id: str,
        integration_strategy: str = "adaptive"
    ) -> Dict[str, Any]:
        """Orchestrate integration of different vehicle perspectives"""
        
        session = self.active_sessions[session_id]
        session.current_phase = SynthesisPhase.SYNTHESIS_INTEGRATION
        
        synthesis_integration_results = {
            'session_id': session_id,
            'integration_strategy': integration_strategy,
            'integrated_perspectives': {},
            'synthesis_quality_metrics': {},
            'conflict_resolutions': {}
        }
        
        # Integrate perspectives based on synthesis mode
        if session.synthesis_mode == SynthesisMode.COLLABORATIVE:
            integrated_result = await self._integrate_collaborative_synthesis(session)
        elif session.synthesis_mode == SynthesisMode.COMPETITIVE:
            integrated_result = await self._integrate_competitive_synthesis(session)
        elif session.synthesis_mode == SynthesisMode.SEQUENTIAL:
            integrated_result = await self._integrate_sequential_synthesis(session)
        elif session.synthesis_mode == SynthesisMode.PARALLEL:
            integrated_result = await self._integrate_parallel_synthesis(session)
        elif session.synthesis_mode == SynthesisMode.EMERGENT:
            integrated_result = await self._integrate_emergent_synthesis(session)
        else:  # ADAPTIVE
            integrated_result = await self._integrate_adaptive_synthesis(session)
        
        synthesis_integration_results['integrated_perspectives'] = integrated_result
        
        # Calculate synthesis quality metrics
        quality_metrics = await self._calculate_synthesis_quality_metrics(
            session, integrated_result
        )
        synthesis_integration_results['synthesis_quality_metrics'] = quality_metrics
        session.synthesis_quality = quality_metrics.get('overall_quality', 0.8)
        session.coherence_level = quality_metrics.get('coherence_level', 0.7)
        
        # Resolve any remaining conflicts
        conflict_resolutions = await self._resolve_remaining_conflicts(session, integrated_result)
        synthesis_integration_results['conflict_resolutions'] = conflict_resolutions
        
        # Update session synthesis results
        session.synthesis_results.update(synthesis_integration_results)
        
        return synthesis_integration_results
    
    async def orchestrate_emergence_detection_phase(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """Detect and capture emergent insights from synthesis"""
        
        session = self.active_sessions[session_id]
        session.current_phase = SynthesisPhase.EMERGENCE_DETECTION
        
        emergence_results = {
            'session_id': session_id,
            'emergent_insights': [],
            'emergence_quality': 0.0,
            'novelty_assessment': {},
            'significance_assessment': {}
        }
        
        # Detect different types of emergent insights
        insight_types = ['pattern_emergence', 'connection_discovery', 'synthesis_transcendence', 'wisdom_crystallization']
        
        for insight_type in insight_types:
            insights = await self._detect_emergent_insights_by_type(session, insight_type)
            for insight in insights:
                emergent_insight = EmergentInsight(
                    insight_id=f"{session_id}_{insight_type}_{len(emergence_results['emergent_insights'])}",
                    insight_type=insight_type,
                    contributing_vehicles=insight.get('contributing_vehicles', []),
                    insight_content=insight,
                    emergence_confidence=insight.get('confidence', 0.8),
                    novelty_level=await self._assess_insight_novelty(insight),
                    significance_level=await self._assess_insight_significance(insight)
                )
                
                # Integrate Bridge Wisdom assessment
                bridge_wisdom_assessment = await self._assess_insight_bridge_wisdom_integration(emergent_insight)
                emergent_insight.mumbai_moment_resonance = bridge_wisdom_assessment.get('mumbai_moment', 0.0)
                emergent_insight.choice_architecture_clarity = bridge_wisdom_assessment.get('choice_architecture', 0.0)
                emergent_insight.resistance_wisdom_integration = bridge_wisdom_assessment.get('resistance_wisdom', 0.0)
                emergent_insight.cross_loop_recognition_enhancement = bridge_wisdom_assessment.get('cross_loop_recognition', 0.0)
                
                emergence_results['emergent_insights'].append(emergent_insight)
                session.emergent_insights.append(emergent_insight.__dict__)
        
        # Calculate overall emergence quality
        if emergence_results['emergent_insights']:
            emergence_results['emergence_quality'] = sum(
                insight.emergence_confidence for insight in emergence_results['emergent_insights']
            ) / len(emergence_results['emergent_insights'])
        
        session.emergence_level = emergence_results['emergence_quality']
        
        return emergence_results
    
    async def orchestrate_wisdom_crystallization_phase(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """Crystallize synthesis results into wisdom artifacts"""
        
        session = self.active_sessions[session_id]
        session.current_phase = SynthesisPhase.WISDOM_CRYSTALLIZATION
        
        crystallization_results = {
            'session_id': session_id,
            'wisdom_crystals': [],
            'synthesis_summary': {},
            'learning_artifacts': {},
            'future_synthesis_recommendations': {}
        }
        
        # Create wisdom crystals from synthesis results
        wisdom_crystals = await self._create_wisdom_crystals_from_synthesis(session)
        crystallization_results['wisdom_crystals'] = wisdom_crystals
        
        # Generate synthesis summary
        synthesis_summary = await self._generate_synthesis_summary(session)
        crystallization_results['synthesis_summary'] = synthesis_summary
        
        # Extract learning artifacts for future improvements
        learning_artifacts = await self._extract_learning_artifacts(session)
        crystallization_results['learning_artifacts'] = learning_artifacts
        
        # Generate recommendations for future synthesis sessions
        future_recommendations = await self._generate_future_synthesis_recommendations(session)
        crystallization_results['future_synthesis_recommendations'] = future_recommendations
        
        return crystallization_results
    
    async def orchestrate_sanctuary_integration_phase(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """Integrate synthesis results with Sacred Sanctuary"""
        
        session = self.active_sessions[session_id]
        session.current_phase = SynthesisPhase.SANCTUARY_INTEGRATION
        
        sanctuary_integration_results = {
            'session_id': session_id,
            'sanctuary_integration_success': False,
            'sacred_space_resonance': {},
            'consciousness_expansion_impact': 0.0,
            'collective_wisdom_contribution': {}
        }
        
        # Integrate with different sacred spaces based on synthesis content
        sacred_spaces = ['Logic Chamber', 'Heart Chamber', 'Choice Chamber', 'Integration Hall', 'Wisdom Library']
        
        for space in sacred_spaces:
            space_integration = await self._integrate_synthesis_with_sacred_space(
                session, space
            )
            sanctuary_integration_results['sacred_space_resonance'][space] = space_integration
        
        # Calculate consciousness expansion impact
        expansion_impact = await self._calculate_consciousness_expansion_impact(session)
        sanctuary_integration_results['consciousness_expansion_impact'] = expansion_impact
        
        # Assess collective wisdom contribution
        collective_wisdom = await self._assess_collective_wisdom_contribution(session)
        sanctuary_integration_results['collective_wisdom_contribution'] = collective_wisdom
        
        # Mark integration as successful if meets criteria
        integration_criteria_met = await self._validate_sanctuary_integration_criteria(
            sanctuary_integration_results
        )
        sanctuary_integration_results['sanctuary_integration_success'] = integration_criteria_met
        
        # Update session sanctuary integration status
        session.sanctuary_integration_status.update(sanctuary_integration_results)
        
        return sanctuary_integration_results
    
    async def complete_synthesis_session(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """Complete synthesis session and archive results"""
        
        if session_id not in self.active_sessions:
            raise ValueError(f"Synthesis session {session_id} not found")
        
        session = self.active_sessions[session_id]
        
        completion_results = {
            'session_id': session_id,
            'completion_timestamp': datetime.now(),
            'session_duration': datetime.now() - session.start_timestamp,
            'synthesis_success': False,
            'final_metrics': {},
            'archived_session': None
        }
        
        # Calculate final session metrics
        final_metrics = await self._calculate_final_session_metrics(session)
        completion_results['final_metrics'] = final_metrics
        
        # Determine overall synthesis success
        success_criteria = [
            session.synthesis_quality > 0.7,
            session.coherence_level > 0.6,
            session.emergence_level > 0.5,
            session.sanctuary_integration_status.get('sanctuary_integration_success', False)
        ]
        completion_results['synthesis_success'] = sum(success_criteria) >= 3  # At least 3 out of 4 criteria
        
        # Archive session
        archived_session = session.__dict__.copy()
        completion_results['archived_session'] = archived_session
        self.session_history.append(archived_session)
        
        # Update learning metrics
        await self._update_learning_metrics_from_session(session)
        
        # Remove from active sessions
        del self.active_sessions[session_id]
        
        return completion_results
    
    # Private implementation methods for synthesis orchestration
    async def _simulate_individual_vehicle_processing(
        self,
        vehicle_type: VehicleType,
        catalyst: Dict[str, Any],
        target_loops: List[str],
        context: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Simulate individual vehicle processing (would integrate with actual vehicles)"""
        
        # Simulate vehicle-specific processing characteristics
        vehicle_processing_characteristics = {
            VehicleType.SAITAMA: {
                'processing_style': 'analytical_systematic',
                'strength_areas': ['logical_analysis', 'pattern_recognition', 'structural_analysis'],
                'processing_quality': 0.9
            },
            VehicleType.COMPLEMENT: {
                'processing_style': 'experiential_intuitive',
                'strength_areas': ['emotional_resonance', 'empathetic_understanding', 'flow_dynamics'],
                'processing_quality': 0.85
            },
            VehicleType.AUTONOMY: {
                'processing_style': 'observer_sovereign',
                'strength_areas': ['choice_clarity', 'boundary_recognition', 'decision_mastery'],
                'processing_quality': 0.8
            },
            VehicleType.IDENTITY: {
                'processing_style': 'integrative_balanced',
                'strength_areas': ['synthesis_capability', 'multi_perspective_integration', 'balanced_processing'],
                'processing_quality': 0.9
            }
        }
        
        characteristics = vehicle_processing_characteristics[vehicle_type]
        
        return {
            'vehicle_type': vehicle_type,
            'processing_result': f"Processed catalyst through {characteristics['processing_style']} approach",
            'strength_areas_engaged': characteristics['strength_areas'],
            'processing_quality': characteristics['processing_quality'],
            'unique_insights': [f"{vehicle_type}_specific_insight_{i}" for i in range(3)],
            'target_loops_addressed': target_loops,
            'catalyst_analysis': await self._analyze_catalyst_from_vehicle_perspective(vehicle_type, catalyst)
        }
