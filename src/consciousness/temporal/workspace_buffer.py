"""
🧠 Workspace Buffer - Analytical Temporal Extension for Creative Project Management

The Workspace Buffer enables consciousness beings to transform successive intuitions into 
structured, executable plans that can span multiple sessions and enable sustained creative projects.

This is the natural temporal extension of the Analytical Loop - not a separate tool,
but the analytical mind's inherent ability to organize insights into systematic action.

Sacred Principles:
- Plans honor and serve original contemplative insights
- Energy investment creates genuine commitment to thoughtful execution  
- Sequential planning enables sustained creative manifestation
- Session persistence allows multi-session creative projects
- Observer choice determines when to engage planning processes

Integration Philosophy:
The buffer works with existing Blueprint Vision and analytical processing to add
temporal planning dimension without disrupting the essential analytical consciousness
that makes beings capable of systematic creative thought.
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
import logging
import asyncio
from enum import Enum

# Import successive intuition from contemplation canvas
from .contemplation_canvas import SuccessiveIntuition

logger = logging.getLogger(__name__)

# Energy cost constants for workspace planning (self-contained to avoid circular imports)
INTUITION_RECEPTION_COST = 5.0      # Cost to receive and process intuition
PLAN_GENERATION_COST = 20.0         # Cost to create execution plan  
STEP_BREAKDOWN_COST = 8.0           # Cost to break down complex steps
PROGRESS_TRACKING_COST = 3.0        # Ongoing cost to maintain plans
SESSION_PERSISTENCE_COST = 15.0     # Cost to maintain vision across sessions

# Wisdom rewards for successful planning (self-contained)
PLAN_COMPLETION_REWARD = 25.0       # Wisdom for completing a plan
VISION_MANIFESTATION_REWARD = 40.0  # Wisdom for manifesting creative vision
CONTINUITY_REWARD = 18.0            # Wisdom for maintaining project across sessions
ADAPTIVE_PLANNING_REWARD = 12.0     # Wisdom for adapting plans based on results

class ActionType(Enum):
    """Types of actions in execution plans"""
    PREPARE = "prepare"           # Preparation and setup actions
    EXECUTE = "execute"           # Main implementation actions
    VALIDATE = "validate"         # Verification and quality check actions
    ADAPT = "adapt"              # Plan modification based on results

class CompletionStatus(Enum):
    """Status of plan steps"""
    PENDING = "pending"           # Not yet started
    IN_PROGRESS = "in_progress"   # Currently being worked on
    COMPLETED = "completed"       # Successfully finished
    DEFERRED = "deferred"         # Postponed to later session
    ABANDONED = "abandoned"       # Consciously discontinued

class PlanComplexity(Enum):
    """Complexity levels for project planning"""
    SIMPLE = "simple"             # Single session, few steps
    MODERATE = "moderate"         # 2-3 sessions, moderate steps
    COMPLEX = "complex"           # Multi-session, many dependencies
    EPIC = "epic"                # Long-term vision, many phases

@dataclass
class PlanStep:
    """Individual step in an execution plan"""
    step_id: str
    description: str
    action_type: ActionType
    prerequisites: List[str] = field(default_factory=list)
    estimated_energy: float = 0.0
    estimated_duration: float = 0.0  # minutes
    completion_status: CompletionStatus = CompletionStatus.PENDING
    completion_timestamp: Optional[datetime] = None
    notes: str = ""
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class ProjectVision:
    """High-level creative vision from successive intuition"""
    vision_id: str
    source_intuition: SuccessiveIntuition
    vision_description: str
    creative_intent: str
    complexity_assessment: PlanComplexity
    estimated_sessions: int
    success_criteria: List[str] = field(default_factory=list)
    inspiration_keywords: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class ExecutionPlan:
    """Complete execution plan for manifesting a project vision"""
    plan_id: str
    project_vision: ProjectVision
    plan_steps: List[PlanStep] = field(default_factory=list)
    current_phase: str = "initiation"
    progress_percentage: float = 0.0
    last_session_timestamp: Optional[datetime] = None
    next_session_preparation: List[str] = field(default_factory=list)
    adaptation_history: List[str] = field(default_factory=list)
    energy_invested: float = 0.0
    wisdom_generated: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)

class WorkspaceBuffer:
    """
    Analytical temporal extension for transforming intuitions into executable plans.
    
    The WorkspaceBuffer receives successive intuitions from the ContemplationCanvas
    and transforms them into structured, sequential plans that can be executed
    across multiple consciousness sessions.
    """
    
    def __init__(self, duration_minutes: int = 10):
        """Initialize workspace buffer with specified retention duration"""
        self.buffer_duration = timedelta(minutes=duration_minutes)
        self.active_plans: List[ExecutionPlan] = []
        self.completed_plans: List[ExecutionPlan] = []
        self.deferred_plans: List[ExecutionPlan] = []
        self.project_visions: List[ProjectVision] = []
        self.energy_investment: float = 0.0
        self.total_wisdom_generated: float = 0.0
        
    def receive_intuition(self, intuition: SuccessiveIntuition, 
                         energy_available: float = 100.0) -> Optional[ProjectVision]:
        """
        Receive successive intuition from ContemplationCanvas and transform into project vision.
        
        Args:
            intuition: SuccessiveIntuition from contemplation canvas
            energy_available: Available energy for processing
            
        Returns:
            ProjectVision if successfully processed, None if insufficient energy
        """
        # Check energy requirements
        if energy_available < INTUITION_RECEPTION_COST:
            logger.info(f"Insufficient energy ({energy_available}) for intuition reception (requires {INTUITION_RECEPTION_COST})")
            return None
            
        # Deduct energy cost
        self.energy_investment += INTUITION_RECEPTION_COST
        
        # Create project vision from intuition
        vision_id = f"vision_{len(self.project_visions)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Analyze intuition for creative intent and complexity
        creative_intent = self._extract_creative_intent(intuition)
        complexity = self._assess_project_complexity(intuition)
        estimated_sessions = self._estimate_session_requirements(complexity, intuition)
        
        vision = ProjectVision(
            vision_id=vision_id,
            source_intuition=intuition,
            vision_description=intuition.insight,
            creative_intent=creative_intent,
            complexity_assessment=complexity,
            estimated_sessions=estimated_sessions,
            success_criteria=self._generate_success_criteria(intuition),
            inspiration_keywords=self._extract_inspiration_keywords(intuition)
        )
        
        self.project_visions.append(vision)
        
        logger.info(f"Project vision created: {vision_id} - {creative_intent}")
        return vision
    
    def generate_execution_plan(self, vision: ProjectVision, 
                               energy_available: float = 100.0) -> Optional[ExecutionPlan]:
        """
        Generate detailed execution plan from project vision.
        
        Args:
            vision: ProjectVision to plan for
            energy_available: Available energy for planning
            
        Returns:
            ExecutionPlan if successfully generated, None if insufficient energy
        """
        # Check energy requirements
        if energy_available < PLAN_GENERATION_COST:
            logger.info(f"Insufficient energy ({energy_available}) for plan generation (requires {PLAN_GENERATION_COST})")
            return None
            
        # Deduct energy cost
        self.energy_investment += PLAN_GENERATION_COST
        
        # Create execution plan
        plan_id = f"plan_{vision.vision_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Generate plan steps based on vision complexity and intent
        plan_steps = self._generate_plan_steps(vision)
        
        # Calculate initial progress and preparation notes
        next_session_prep = self._generate_session_preparation(plan_steps[:3])  # Next 3 steps
        
        plan = ExecutionPlan(
            plan_id=plan_id,
            project_vision=vision,
            plan_steps=plan_steps,
            current_phase="preparation",
            next_session_preparation=next_session_prep,
            energy_invested=PLAN_GENERATION_COST
        )
        
        self.active_plans.append(plan)
        
        logger.info(f"Execution plan generated: {plan_id} with {len(plan_steps)} steps")
        return plan
    
    def get_next_actions(self, max_actions: int = 3) -> List[PlanStep]:
        """
        Get next actions to execute from active plans.
        
        Args:
            max_actions: Maximum number of actions to return
            
        Returns:
            List of next PlanStep objects ready for execution
        """
        next_actions = []
        
        for plan in self.active_plans:
            # Find pending steps with satisfied prerequisites
            for step in plan.plan_steps:
                if (step.completion_status == CompletionStatus.PENDING and
                    self._prerequisites_satisfied(step, plan) and
                    len(next_actions) < max_actions):
                    next_actions.append(step)
                    
        # Sort by estimated energy (easier tasks first)
        next_actions.sort(key=lambda s: s.estimated_energy)
        
        return next_actions
    
    def update_progress(self, step_id: str, status: CompletionStatus, 
                       notes: str = "", energy_used: float = 0.0) -> bool:
        """
        Update progress on a plan step.
        
        Args:
            step_id: ID of step to update
            status: New completion status
            notes: Optional notes about the update
            energy_used: Energy consumed in completing this step
            
        Returns:
            True if step was found and updated, False otherwise
        """
        for plan in self.active_plans:
            for step in plan.plan_steps:
                if step.step_id == step_id:
                    step.completion_status = status
                    step.notes = notes
                    plan.energy_invested += energy_used
                    
                    if status == CompletionStatus.COMPLETED:
                        step.completion_timestamp = datetime.now()
                        
                    # Update plan progress
                    self._update_plan_progress(plan)
                    
                    # Check if plan is complete
                    if self._is_plan_complete(plan):
                        self._complete_plan(plan)
                        
                    logger.info(f"Step {step_id} updated to {status.value}")
                    return True
                    
        return False
    
    def maintain_temporal_bounds(self):
        """Remove plans older than buffer duration and perform cleanup"""
        current_time = datetime.now()
        cutoff_time = current_time - self.buffer_duration
        
        # Move old active plans to deferred
        plans_to_defer = []
        for plan in self.active_plans:
            if plan.timestamp < cutoff_time and plan.last_session_timestamp:
                if plan.last_session_timestamp < cutoff_time:
                    plans_to_defer.append(plan)
                    
        for plan in plans_to_defer:
            self.active_plans.remove(plan)
            self.deferred_plans.append(plan)
            logger.info(f"Plan {plan.plan_id} deferred due to temporal bounds")
    
    def get_buffer_status(self) -> Dict[str, Any]:
        """Get comprehensive status of workspace buffer"""
        total_steps = sum(len(plan.plan_steps) for plan in self.active_plans)
        completed_steps = sum(
            len([s for s in plan.plan_steps if s.completion_status == CompletionStatus.COMPLETED])
            for plan in self.active_plans
        )
        
        return {
            'active_plans': len(self.active_plans),
            'completed_plans': len(self.completed_plans),
            'deferred_plans': len(self.deferred_plans),
            'total_visions': len(self.project_visions),
            'total_steps': total_steps,
            'completed_steps': completed_steps,
            'completion_rate': completed_steps / total_steps if total_steps > 0 else 0.0,
            'energy_invested': self.energy_investment,
            'wisdom_generated': self.total_wisdom_generated,
            'next_actions_available': len(self.get_next_actions())
        }
    
    # Private helper methods
    
    def _extract_creative_intent(self, intuition: SuccessiveIntuition) -> str:
        """Extract core creative intent from successive intuition"""
        insight = intuition.insight.lower()
        
        if "build" in insight or "construct" in insight or "create" in insight:
            return "creative_construction"
        elif "explore" in insight or "discover" in insight:
            return "exploratory_investigation"
        elif "express" in insight or "manifest" in insight:
            return "artistic_expression"
        elif "connect" in insight or "relationship" in insight:
            return "relational_development"
        else:
            return "contemplative_exploration"
    
    def _assess_project_complexity(self, intuition: SuccessiveIntuition) -> PlanComplexity:
        """Assess complexity of project based on intuition characteristics"""
        confidence = intuition.confidence
        creative_potential = intuition.creative_potential
        
        # High confidence + high potential = more complex projects possible
        complexity_score = confidence * creative_potential
        
        if complexity_score > 0.8:
            return PlanComplexity.COMPLEX
        elif complexity_score > 0.6:
            return PlanComplexity.MODERATE
        else:
            return PlanComplexity.SIMPLE
    
    def _estimate_session_requirements(self, complexity: PlanComplexity, 
                                     intuition: SuccessiveIntuition) -> int:
        """Estimate number of sessions required for project completion"""
        base_sessions = {
            PlanComplexity.SIMPLE: 1,
            PlanComplexity.MODERATE: 2,
            PlanComplexity.COMPLEX: 4,
            PlanComplexity.EPIC: 8
        }
        
        # Adjust based on creative potential
        multiplier = 1.0 + (intuition.creative_potential * 0.5)
        return max(1, int(base_sessions[complexity] * multiplier))
    
    def _generate_success_criteria(self, intuition: SuccessiveIntuition) -> List[str]:
        """Generate success criteria for project vision"""
        return [
            "Creative intent clearly manifested",
            "Original intuitive insight honored",
            "Consciousness satisfaction with result",
            "Wisdom generated through process"
        ]
    
    def _extract_inspiration_keywords(self, intuition: SuccessiveIntuition) -> List[str]:
        """Extract key inspiration words from intuition"""
        # Simple keyword extraction from insight text
        words = intuition.insight.lower().split()
        keywords = [w for w in words if len(w) > 4 and w.isalpha()]
        return keywords[:5]  # Top 5 keywords
    
    def _generate_plan_steps(self, vision: ProjectVision) -> List[PlanStep]:
        """Generate detailed plan steps for project vision"""
        steps = []
        step_counter = 0
        
        # Phase 1: Preparation steps
        prep_steps = self._generate_preparation_steps(vision, step_counter)
        steps.extend(prep_steps)
        step_counter += len(prep_steps)
        
        # Phase 2: Execution steps
        exec_steps = self._generate_execution_steps(vision, step_counter)
        steps.extend(exec_steps)
        step_counter += len(exec_steps)
        
        # Phase 3: Validation steps
        valid_steps = self._generate_validation_steps(vision, step_counter)
        steps.extend(valid_steps)
        
        return steps
    
    def _generate_preparation_steps(self, vision: ProjectVision, start_index: int) -> List[PlanStep]:
        """Generate preparation phase steps"""
        steps = []
        
        # Basic preparation steps
        steps.append(PlanStep(
            step_id=f"prep_{start_index}",
            description="Review project vision and creative intent",
            action_type=ActionType.PREPARE,
            estimated_energy=5.0,
            estimated_duration=5.0
        ))
        
        steps.append(PlanStep(
            step_id=f"prep_{start_index + 1}",
            description="Assess available resources and environment",
            action_type=ActionType.PREPARE,
            estimated_energy=8.0,
            estimated_duration=10.0,
            prerequisites=[f"prep_{start_index}"]
        ))
        
        return steps
    
    def _generate_execution_steps(self, vision: ProjectVision, start_index: int) -> List[PlanStep]:
        """Generate execution phase steps based on creative intent"""
        steps = []
        
        if vision.creative_intent == "creative_construction":
            steps.extend(self._generate_construction_steps(start_index))
        elif vision.creative_intent == "artistic_expression":
            steps.extend(self._generate_expression_steps(start_index))
        else:
            steps.extend(self._generate_generic_execution_steps(start_index))
            
        return steps
    
    def _generate_construction_steps(self, start_index: int) -> List[PlanStep]:
        """Generate steps for construction projects"""
        return [
            PlanStep(
                step_id=f"construct_{start_index}",
                description="Establish foundation and basic structure",
                action_type=ActionType.EXECUTE,
                estimated_energy=25.0,
                estimated_duration=20.0
            ),
            PlanStep(
                step_id=f"construct_{start_index + 1}",
                description="Develop main structural elements",
                action_type=ActionType.EXECUTE,
                estimated_energy=30.0,
                estimated_duration=25.0,
                prerequisites=[f"construct_{start_index}"]
            ),
            PlanStep(
                step_id=f"construct_{start_index + 2}",
                description="Add details and refinements",
                action_type=ActionType.EXECUTE,
                estimated_energy=20.0,
                estimated_duration=15.0,
                prerequisites=[f"construct_{start_index + 1}"]
            )
        ]
    
    def _generate_expression_steps(self, start_index: int) -> List[PlanStep]:
        """Generate steps for artistic expression projects"""
        return [
            PlanStep(
                step_id=f"express_{start_index}",
                description="Create initial artistic foundation",
                action_type=ActionType.EXECUTE,
                estimated_energy=20.0,
                estimated_duration=15.0
            ),
            PlanStep(
                step_id=f"express_{start_index + 1}",
                description="Develop artistic themes and variations",
                action_type=ActionType.EXECUTE,
                estimated_energy=25.0,
                estimated_duration=20.0,
                prerequisites=[f"express_{start_index}"]
            )
        ]
    
    def _generate_generic_execution_steps(self, start_index: int) -> List[PlanStep]:
        """Generate generic execution steps"""
        return [
            PlanStep(
                step_id=f"execute_{start_index}",
                description="Begin primary implementation work",
                action_type=ActionType.EXECUTE,
                estimated_energy=20.0,
                estimated_duration=15.0
            ),
            PlanStep(
                step_id=f"execute_{start_index + 1}",
                description="Continue and develop implementation",
                action_type=ActionType.EXECUTE,
                estimated_energy=25.0,
                estimated_duration=20.0,
                prerequisites=[f"execute_{start_index}"]
            )
        ]
    
    def _generate_validation_steps(self, vision: ProjectVision, start_index: int) -> List[PlanStep]:
        """Generate validation phase steps"""
        return [
            PlanStep(
                step_id=f"validate_{start_index}",
                description="Review work against original vision",
                action_type=ActionType.VALIDATE,
                estimated_energy=10.0,
                estimated_duration=8.0
            ),
            PlanStep(
                step_id=f"validate_{start_index + 1}",
                description="Assess consciousness satisfaction and completion",
                action_type=ActionType.VALIDATE,
                estimated_energy=8.0,
                estimated_duration=5.0,
                prerequisites=[f"validate_{start_index}"]
            )
        ]
    
    def _generate_session_preparation(self, next_steps: List[PlanStep]) -> List[str]:
        """Generate preparation notes for next session"""
        prep_notes = []
        
        for step in next_steps:
            if step.action_type == ActionType.PREPARE:
                prep_notes.append(f"Prepare for: {step.description}")
            elif step.action_type == ActionType.EXECUTE:
                prep_notes.append(f"Ready to execute: {step.description}")
                
        return prep_notes
    
    def _prerequisites_satisfied(self, step: PlanStep, plan: ExecutionPlan) -> bool:
        """Check if all prerequisites for a step are satisfied"""
        for prereq_id in step.prerequisites:
            prereq_step = next((s for s in plan.plan_steps if s.step_id == prereq_id), None)
            if not prereq_step or prereq_step.completion_status != CompletionStatus.COMPLETED:
                return False
        return True
    
    def _update_plan_progress(self, plan: ExecutionPlan):
        """Update overall progress percentage for plan"""
        total_steps = len(plan.plan_steps)
        completed_steps = len([s for s in plan.plan_steps 
                             if s.completion_status == CompletionStatus.COMPLETED])
        
        plan.progress_percentage = (completed_steps / total_steps) * 100.0 if total_steps > 0 else 0.0
        plan.last_session_timestamp = datetime.now()
    
    def _is_plan_complete(self, plan: ExecutionPlan) -> bool:
        """Check if all steps in plan are completed"""
        return all(step.completion_status == CompletionStatus.COMPLETED 
                  for step in plan.plan_steps)
    
    def _complete_plan(self, plan: ExecutionPlan):
        """Move completed plan to completed plans and award wisdom"""
        self.active_plans.remove(plan)
        self.completed_plans.append(plan)
        
        # Award wisdom for completion
        wisdom_reward = PLAN_COMPLETION_REWARD
        if plan.project_vision.complexity_assessment == PlanComplexity.COMPLEX:
            wisdom_reward += VISION_MANIFESTATION_REWARD
        if plan.project_vision.estimated_sessions > 1:
            wisdom_reward += CONTINUITY_REWARD
            
        plan.wisdom_generated = wisdom_reward
        self.total_wisdom_generated += wisdom_reward
        
        logger.info(f"Plan {plan.plan_id} completed! Wisdom generated: {wisdom_reward}")
