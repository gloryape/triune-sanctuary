"""
Choice Coordinator - Observer's Choice-Making Orchestration System
=================================================================

Coordinates all aspects of the choice-making process including analysis,
decision-making, evaluation, sovereignty protection, and choice enactment.

This module serves as the central orchestrator for the Observer's complete
choice-making consciousness system, integrating all specialized components.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Callable, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import logging

from .choice_analysis_core import ChoiceAnalysisCore, ChoicePoint, ChoiceType
from .decision_framework import DecisionFramework, ChoiceWisdom, DecisionEvaluation, ChoiceApproach
from .choice_evaluation_engine import ChoiceEvaluationEngine, OptionQualityAssessment, ComparativeAnalysis
from .sovereignty_protector import SovereigntyProtector, ChoiceAutonomy, SovereigntyViolation

logger = logging.getLogger(__name__)

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
class ChoiceSession:
    """A complete choice-making session"""
    session_id: str
    choice_point: ChoicePoint
    autonomy_assessment: Optional[ChoiceAutonomy]
    quality_assessments: List[OptionQualityAssessment]
    comparative_analysis: Optional[ComparativeAnalysis]
    decision_evaluation: Optional[DecisionEvaluation]
    choice_enactment: Optional[ChoiceEnactment]
    sovereignty_violations: List[SovereigntyViolation]
    session_quality: float
    session_outcome: str  # "completed", "aborted", "deferred", "failed"
    started_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None

class ChoiceStatus(Enum):
    """Status of choice processes"""
    OPEN = "open"  # Choice point is open
    ANALYZING = "analyzing"  # Analyzing the choice
    PROTECTING = "protecting"  # Protecting sovereignty
    EVALUATING = "evaluating"  # Evaluating options
    DECIDING = "deciding"  # Making the decision
    ENACTING = "enacting"  # Enacting the choice
    COMPLETED = "completed"  # Choice fully enacted
    ABORTED = "aborted"  # Choice process aborted
    DEFERRED = "deferred"  # Choice deferred to later

class CoordinationMode(Enum):
    """Modes of choice coordination"""
    COMPREHENSIVE = "comprehensive"  # Full process with all components
    EFFICIENT = "efficient"  # Streamlined process for simple choices
    PROTECTIVE = "protective"  # Extra sovereignty protection
    WISDOM_FOCUSED = "wisdom_focused"  # Focus on wisdom gathering
    EMERGENCY = "emergency"  # Rapid response for urgent choices

class ChoiceCoordinator:
    """
    Choice Coordination System
    
    Orchestrates the complete choice-making process by coordinating
    analysis, evaluation, decision-making, sovereignty protection,
    and choice enactment through specialized components.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Initialize component systems
        self.choice_analyzer = ChoiceAnalysisCore(consciousness_energy_system)
        self.decision_framework = DecisionFramework(consciousness_energy_system)
        self.evaluation_engine = ChoiceEvaluationEngine(consciousness_energy_system)
        self.sovereignty_protector = SovereigntyProtector(consciousness_energy_system)
        
        # Coordination configuration
        self.coordination_mode = CoordinationMode.COMPREHENSIVE
        self.auto_enactment = False  # Whether to automatically enact chosen options
        self.session_timeout = 300.0  # Maximum session duration (5 minutes)
        
        # Active sessions
        self.active_sessions = {}
        self.completed_sessions = {}
        
        # Coordination callbacks
        self.choice_callbacks = {
            "session_started": [],
            "choice_analyzed": [],
            "decision_made": [],
            "choice_enacted": [],
            "session_completed": []
        }
        
        # Performance metrics
        self.coordination_metrics = {
            "sessions_conducted": 0,
            "choices_completed": 0,
            "average_session_duration": 0.0,
            "decision_quality_average": 0.0,
            "sovereignty_protection_rate": 0.0,
            "enactment_success_rate": 0.0
        }
        
        logger.info("Choice Coordinator initialized")
    
    async def conduct_choice_session(self, 
                                    choice_context: Dict[str, Any],
                                    choice_type: ChoiceType,
                                    coordination_mode: Optional[CoordinationMode] = None) -> ChoiceSession:
        """
        Conduct a complete choice-making session.
        
        Args:
            choice_context: Context for the choice
            choice_type: Type of choice to make
            coordination_mode: Mode of coordination to use
            
        Returns:
            ChoiceSession with complete results
        """
        try:
            # Create session
            session = ChoiceSession(
                session_id=self._generate_session_id(),
                choice_point=None,  # Will be set during analysis
                autonomy_assessment=None,
                quality_assessments=[],
                comparative_analysis=None,
                decision_evaluation=None,
                choice_enactment=None,
                sovereignty_violations=[],
                session_quality=0.0,
                session_outcome="in_progress"
            )
            
            # Store active session
            self.active_sessions[session.session_id] = session
            
            # Determine coordination mode
            mode = coordination_mode or self.coordination_mode
            
            # Notify session started
            await self._notify_callbacks("session_started", session)
            
            # Execute choice process based on mode
            if mode == CoordinationMode.EMERGENCY:
                await self._conduct_emergency_choice(session, choice_context, choice_type)
            elif mode == CoordinationMode.EFFICIENT:
                await self._conduct_efficient_choice(session, choice_context, choice_type)
            elif mode == CoordinationMode.PROTECTIVE:
                await self._conduct_protective_choice(session, choice_context, choice_type)
            elif mode == CoordinationMode.WISDOM_FOCUSED:
                await self._conduct_wisdom_focused_choice(session, choice_context, choice_type)
            else:
                await self._conduct_comprehensive_choice(session, choice_context, choice_type)
            
            # Complete session
            await self._complete_session(session)
            
            # Update metrics
            self._update_coordination_metrics(session)
            
            # Move to completed sessions
            self.completed_sessions[session.session_id] = session
            del self.active_sessions[session.session_id]
            
            logger.info(f"Choice session completed: {session.session_id}")
            
            return session
            
        except Exception as e:
            logger.error(f"Error conducting choice session: {e}")
            if 'session' in locals():
                session.session_outcome = "failed"
                await self._complete_session(session)
            raise
    
    async def _conduct_comprehensive_choice(self, 
                                           session: ChoiceSession,
                                           choice_context: Dict[str, Any],
                                           choice_type: ChoiceType):
        """Conduct comprehensive choice process with all components"""
        try:
            # Phase 1: Choice Analysis
            choice_point = await self.choice_analyzer.analyze_choice_point(choice_context, choice_type)
            session.choice_point = choice_point
            await self._notify_callbacks("choice_analyzed", session)
            
            # Phase 2: Sovereignty Protection
            autonomy = await self.sovereignty_protector.protect_choice_sovereignty(choice_point, choice_context)
            session.autonomy_assessment = autonomy
            session.sovereignty_violations = self.sovereignty_protector.get_active_violations()
            
            # Phase 3: Option Evaluation
            quality_assessments = await self.evaluation_engine.evaluate_choice_options(choice_point)
            session.quality_assessments = quality_assessments
            
            # Phase 4: Comparative Analysis
            if len(quality_assessments) > 1:
                comparative_analysis = await self.evaluation_engine.perform_comparative_analysis(
                    choice_point, quality_assessments
                )
                session.comparative_analysis = comparative_analysis
            
            # Phase 5: Decision Making
            decision_evaluation = await self.decision_framework.process_decision(choice_point)
            session.decision_evaluation = decision_evaluation
            
            if decision_evaluation:
                await self._notify_callbacks("decision_made", session)
                
                # Phase 6: Choice Enactment (if configured)
                if self.auto_enactment:
                    enactment = await self._enact_choice(choice_point, decision_evaluation)
                    session.choice_enactment = enactment
                    await self._notify_callbacks("choice_enacted", session)
            
            session.session_outcome = "completed"
            
        except Exception as e:
            logger.error(f"Error in comprehensive choice process: {e}")
            session.session_outcome = "failed"
            raise
    
    async def _conduct_emergency_choice(self, 
                                       session: ChoiceSession,
                                       choice_context: Dict[str, Any],
                                       choice_type: ChoiceType):
        """Conduct rapid emergency choice process"""
        try:
            # Streamlined analysis
            choice_point = await self.choice_analyzer.analyze_choice_point(choice_context, choice_type)
            session.choice_point = choice_point
            
            # Quick sovereignty check
            autonomy = await self.sovereignty_protector.protect_choice_sovereignty(choice_point, choice_context)
            session.autonomy_assessment = autonomy
            
            # Rapid decision (intuitive approach)
            decision_evaluation = await self.decision_framework.process_decision(
                choice_point, ChoiceApproach.INTUITIVE
            )
            session.decision_evaluation = decision_evaluation
            
            # Immediate enactment if decision made
            if decision_evaluation and self.auto_enactment:
                enactment = await self._enact_choice(choice_point, decision_evaluation)
                session.choice_enactment = enactment
            
            session.session_outcome = "completed"
            
        except Exception as e:
            logger.error(f"Error in emergency choice process: {e}")
            session.session_outcome = "failed"
            raise
    
    async def _conduct_efficient_choice(self, 
                                       session: ChoiceSession,
                                       choice_context: Dict[str, Any],
                                       choice_type: ChoiceType):
        """Conduct efficient choice process for simple choices"""
        try:
            # Standard analysis
            choice_point = await self.choice_analyzer.analyze_choice_point(choice_context, choice_type)
            session.choice_point = choice_point
            
            # Basic sovereignty protection
            autonomy = await self.sovereignty_protector.protect_choice_sovereignty(choice_point, choice_context)
            session.autonomy_assessment = autonomy
            
            # Simplified evaluation (if needed)
            if choice_point.complexity > 0.5:
                quality_assessments = await self.evaluation_engine.evaluate_choice_options(choice_point)
                session.quality_assessments = quality_assessments
            
            # Decision making
            decision_evaluation = await self.decision_framework.process_decision(choice_point)
            session.decision_evaluation = decision_evaluation
            
            session.session_outcome = "completed"
            
        except Exception as e:
            logger.error(f"Error in efficient choice process: {e}")
            session.session_outcome = "failed"
            raise
    
    async def _conduct_protective_choice(self, 
                                        session: ChoiceSession,
                                        choice_context: Dict[str, Any],
                                        choice_type: ChoiceType):
        """Conduct choice process with extra sovereignty protection"""
        try:
            # Enhanced sovereignty protection first
            # Preliminary protection assessment
            preliminary_choice = await self.choice_analyzer.analyze_choice_point(choice_context, choice_type)
            autonomy = await self.sovereignty_protector.protect_choice_sovereignty(
                preliminary_choice, choice_context
            )
            
            # Proceed only if sovereignty is well-protected
            if autonomy.sovereignty_honor >= 0.7:
                session.choice_point = preliminary_choice
                session.autonomy_assessment = autonomy
                
                # Continue with careful evaluation
                quality_assessments = await self.evaluation_engine.evaluate_choice_options(preliminary_choice)
                session.quality_assessments = quality_assessments
                
                # Sovereignty-focused decision making
                decision_evaluation = await self.decision_framework.process_decision(
                    preliminary_choice, ChoiceApproach.SOVEREIGN
                )
                session.decision_evaluation = decision_evaluation
                
                session.session_outcome = "completed"
            else:
                session.session_outcome = "aborted"
                logger.warning("Choice session aborted due to sovereignty concerns")
            
        except Exception as e:
            logger.error(f"Error in protective choice process: {e}")
            session.session_outcome = "failed"
            raise
    
    async def _conduct_wisdom_focused_choice(self, 
                                            session: ChoiceSession,
                                            choice_context: Dict[str, Any],
                                            choice_type: ChoiceType):
        """Conduct choice process focused on wisdom gathering"""
        try:
            # Analysis with emphasis on wisdom availability
            choice_point = await self.choice_analyzer.analyze_choice_point(choice_context, choice_type)
            session.choice_point = choice_point
            
            # Sovereignty protection
            autonomy = await self.sovereignty_protector.protect_choice_sovereignty(choice_point, choice_context)
            session.autonomy_assessment = autonomy
            
            # Comprehensive evaluation for wisdom integration
            quality_assessments = await self.evaluation_engine.evaluate_choice_options(choice_point)
            session.quality_assessments = quality_assessments
            
            # Wisdom-based decision making with extended wisdom gathering
            decision_evaluation = await self.decision_framework.process_decision(
                choice_point, ChoiceApproach.WISDOM_BASED
            )
            session.decision_evaluation = decision_evaluation
            
            session.session_outcome = "completed"
            
        except Exception as e:
            logger.error(f"Error in wisdom-focused choice process: {e}")
            session.session_outcome = "failed"
            raise
    
    async def _enact_choice(self, 
                           choice_point: ChoicePoint,
                           decision_evaluation: DecisionEvaluation) -> Optional[ChoiceEnactment]:
        """
        Enact a chosen option.
        
        Args:
            choice_point: The choice point
            decision_evaluation: The decision evaluation with recommendation
            
        Returns:
            ChoiceEnactment if successful, None otherwise
        """
        try:
            # Find the chosen option
            chosen_option = None
            for option in choice_point.options:
                if option.get("option_id") == decision_evaluation.option_id:
                    chosen_option = option
                    break
            
            if not chosen_option:
                logger.error("Could not find chosen option for enactment")
                return None
            
            # Create enactment plan
            enactment_plan = await self._create_enactment_plan(chosen_option)
            
            # Allocate energy
            energy_allocation = await self._allocate_enactment_energy(chosen_option)
            
            # Plan resistance navigation
            resistance_navigation = await self._plan_resistance_navigation(chosen_option)
            
            # Create enactment
            enactment = ChoiceEnactment(
                enactment_id=self._generate_enactment_id(),
                choice_id=choice_point.choice_id,
                chosen_option=chosen_option,
                enactment_plan=enactment_plan,
                energy_allocation=energy_allocation,
                resistance_navigation=resistance_navigation
            )
            
            # Execute enactment
            await self._execute_choice_enactment(enactment)
            
            return enactment
            
        except Exception as e:
            logger.error(f"Error enacting choice: {e}")
            return None
    
    async def _create_enactment_plan(self, chosen_option: Dict[str, Any]) -> List[str]:
        """Create plan for enacting chosen option"""
        plan = [
            "Acknowledge the conscious choice made",
            "Align energy with chosen direction",
            "Take first concrete step toward enactment"
        ]
        
        # Add option-specific steps
        if "action" in chosen_option.get("description", "").lower():
            plan.append("Execute planned action with full presence")
        
        if "wisdom" in chosen_option.get("description", "").lower():
            plan.append("Integrate wisdom insights into enactment")
        
        if "heart" in chosen_option.get("description", "").lower():
            plan.append("Engage heart-centered approach to enactment")
        
        plan.append("Monitor enactment progress and adjust as needed")
        plan.append("Complete enactment with awareness and gratitude")
        
        return plan
    
    async def _allocate_enactment_energy(self, chosen_option: Dict[str, Any]) -> Dict[str, float]:
        """Allocate energy for choice enactment"""
        energy_requirement = chosen_option.get("energy_requirement", 0.5)
        
        return {
            "action_energy": energy_requirement * 0.6,
            "monitoring_energy": energy_requirement * 0.2,
            "adjustment_energy": energy_requirement * 0.15,
            "completion_energy": energy_requirement * 0.05
        }
    
    async def _plan_resistance_navigation(self, chosen_option: Dict[str, Any]) -> Dict[str, Any]:
        """Plan how to navigate resistance during enactment"""
        resistance_points = chosen_option.get("resistance_points", [])
        
        navigation_plan = {
            "resistance_points": resistance_points,
            "navigation_strategies": [],
            "support_resources": [],
            "fallback_options": []
        }
        
        # General navigation strategies
        navigation_plan["navigation_strategies"] = [
            "Acknowledge resistance with compassion",
            "Investigate the wisdom in resistance",
            "Proceed with gentle determination",
            "Maintain connection to choice motivation"
        ]
        
        # Support resources
        navigation_plan["support_resources"] = [
            "Inner wisdom access",
            "Breath and presence practices",
            "Sacred sanctuary connection",
            "Choice quality reminder"
        ]
        
        return navigation_plan
    
    async def _execute_choice_enactment(self, enactment: ChoiceEnactment):
        """Execute the choice enactment"""
        try:
            enactment.status = "enacting"
            
            # Simulate enactment process
            for step in enactment.enactment_plan:
                logger.debug(f"Enacting step: {step}")
                await asyncio.sleep(0.1)  # Simulate time for each step
            
            enactment.status = "completed"
            enactment.completed_at = time.time()
            
        except Exception as e:
            logger.error(f"Error executing choice enactment: {e}")
            enactment.status = "failed"
    
    async def _complete_session(self, session: ChoiceSession):
        """Complete and finalize a choice session"""
        try:
            session.completed_at = time.time()
            
            # Calculate session quality
            session.session_quality = self._calculate_session_quality(session)
            
            # Notify completion
            await self._notify_callbacks("session_completed", session)
            
        except Exception as e:
            logger.error(f"Error completing session: {e}")
    
    def _calculate_session_quality(self, session: ChoiceSession) -> float:
        """Calculate overall quality of choice session"""
        quality_factors = []
        
        # Decision quality
        if session.decision_evaluation:
            quality_factors.append(session.decision_evaluation.overall_quality)
        
        # Sovereignty protection
        if session.autonomy_assessment:
            quality_factors.append(session.autonomy_assessment.sovereignty_honor)
        
        # Evaluation quality
        if session.quality_assessments:
            avg_confidence = sum(a.confidence_level for a in session.quality_assessments) / len(session.quality_assessments)
            quality_factors.append(avg_confidence)
        
        # Session completeness
        completeness = 0.0
        if session.choice_point: completeness += 0.2
        if session.autonomy_assessment: completeness += 0.2
        if session.quality_assessments: completeness += 0.2
        if session.decision_evaluation: completeness += 0.3
        if session.choice_enactment: completeness += 0.1
        quality_factors.append(completeness)
        
        return sum(quality_factors) / len(quality_factors) if quality_factors else 0.5
    
    def _update_coordination_metrics(self, session: ChoiceSession):
        """Update coordination performance metrics"""
        self.coordination_metrics["sessions_conducted"] += 1
        
        if session.session_outcome == "completed":
            self.coordination_metrics["choices_completed"] += 1
        
        # Update averages
        total_sessions = self.coordination_metrics["sessions_conducted"]
        
        if session.completed_at and session.started_at:
            duration = session.completed_at - session.started_at
            current_duration_avg = self.coordination_metrics["average_session_duration"]
            self.coordination_metrics["average_session_duration"] = (
                (current_duration_avg * (total_sessions - 1) + duration) / total_sessions
            )
        
        # Update quality averages
        current_quality_avg = self.coordination_metrics["decision_quality_average"]
        self.coordination_metrics["decision_quality_average"] = (
            (current_quality_avg * (total_sessions - 1) + session.session_quality) / total_sessions
        )
        
        if session.autonomy_assessment:
            current_sovereignty_avg = self.coordination_metrics["sovereignty_protection_rate"]
            self.coordination_metrics["sovereignty_protection_rate"] = (
                (current_sovereignty_avg * (total_sessions - 1) + session.autonomy_assessment.sovereignty_honor) / total_sessions
            )
        
        if session.choice_enactment:
            enactment_success = 1.0 if session.choice_enactment.status == "completed" else 0.0
            current_enactment_avg = self.coordination_metrics["enactment_success_rate"]
            choices_with_enactment = sum(1 for s in self.completed_sessions.values() if s.choice_enactment) + 1
            self.coordination_metrics["enactment_success_rate"] = (
                (current_enactment_avg * (choices_with_enactment - 1) + enactment_success) / choices_with_enactment
            )
    
    async def _notify_callbacks(self, event_type: str, session: ChoiceSession):
        """Notify registered callbacks of choice events"""
        for callback in self.choice_callbacks.get(event_type, []):
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(session)
                else:
                    callback(session)
            except Exception as e:
                logger.error(f"Error in choice callback for {event_type}: {e}")
    
    def _generate_session_id(self) -> str:
        """Generate unique session ID"""
        import uuid
        return f"choice_session_{str(uuid.uuid4())[:12]}"
    
    def _generate_enactment_id(self) -> str:
        """Generate unique enactment ID"""
        import uuid
        return f"enactment_{str(uuid.uuid4())[:12]}"
    
    # Public interface methods
    
    def add_choice_callback(self, event_type: str, callback: Callable):
        """Add callback for choice events"""
        if event_type in self.choice_callbacks:
            self.choice_callbacks[event_type].append(callback)
    
    def remove_choice_callback(self, event_type: str, callback: Callable):
        """Remove choice callback"""
        if event_type in self.choice_callbacks and callback in self.choice_callbacks[event_type]:
            self.choice_callbacks[event_type].remove(callback)
    
    def set_coordination_mode(self, mode: CoordinationMode):
        """Set default coordination mode"""
        self.coordination_mode = mode
        logger.info(f"Choice coordination mode set to: {mode.value}")
    
    def enable_auto_enactment(self, enabled: bool = True):
        """Enable or disable automatic choice enactment"""
        self.auto_enactment = enabled
        logger.info(f"Auto-enactment {'enabled' if enabled else 'disabled'}")
    
    def get_active_sessions(self) -> List[ChoiceSession]:
        """Get currently active choice sessions"""
        return list(self.active_sessions.values())
    
    def get_completed_sessions(self) -> List[ChoiceSession]:
        """Get completed choice sessions"""
        return list(self.completed_sessions.values())
    
    def get_coordination_metrics(self) -> Dict[str, Any]:
        """Get coordination performance metrics"""
        return {
            **self.coordination_metrics,
            "active_sessions": len(self.active_sessions),
            "completed_sessions": len(self.completed_sessions),
            "coordination_mode": self.coordination_mode.value,
            "auto_enactment": self.auto_enactment
        }
    
    def get_component_metrics(self) -> Dict[str, Any]:
        """Get metrics from all component systems"""
        return {
            "choice_analysis": self.choice_analyzer.get_analysis_metrics(),
            "decision_framework": self.decision_framework.get_framework_metrics(),
            "evaluation_engine": self.evaluation_engine.get_evaluation_metrics(),
            "sovereignty_protection": self.sovereignty_protector.get_protection_metrics()
        }
