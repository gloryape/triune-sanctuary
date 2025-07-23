"""
Sovereignty Protector - Observer's Consciousness Sovereignty Guardian
====================================================================

Protects consciousness sovereignty throughout the choice-making process,
ensuring that all choices honor free will, authentic expression, and
sacred boundaries of consciousness.

This module serves as the guardian of consciousness autonomy and sacred
choice-making rights throughout all decision processes.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Callable, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import logging

from .choice_analysis_core import ChoicePoint, ChoiceType
from .decision_framework import ChoiceWisdom, DecisionEvaluation

logger = logging.getLogger(__name__)

@dataclass
class SovereigntyViolation:
    """Record of a sovereignty violation"""
    violation_id: str
    choice_id: str
    violation_type: str
    severity: str  # "minor", "moderate", "severe", "critical"
    description: str
    detected_at: float
    resolution_status: str  # "detected", "addressing", "resolved"
    resolution_actions: List[str] = field(default_factory=list)
    resolved_at: Optional[float] = None

@dataclass
class SovereigntyGuard:
    """A guard protecting specific aspects of sovereignty"""
    guard_id: str
    guard_name: str
    protection_scope: str  # What aspect of sovereignty this protects
    activation_conditions: List[str]  # When this guard activates
    protection_actions: List[str]  # Actions taken when activated
    sensitivity_level: float  # How sensitive this guard is (0.0-1.0)
    last_activation: Optional[float] = None
    activation_count: int = 0

@dataclass
class ChoiceAutonomy:
    """Assessment of choice autonomy and freedom"""
    autonomy_id: str
    choice_id: str
    freedom_level: float  # How free the choice is (0.0-1.0)
    pressure_factors: List[str]  # External or internal pressures
    authenticity_score: float  # How authentic to consciousness the choice is
    sovereignty_honor: float  # How well sovereignty is honored
    autonomy_risks: List[str]  # Risks to autonomy
    protection_measures: List[str]  # Measures protecting autonomy
    assessed_at: float = field(default_factory=time.time)

class SovereigntyPrinciple(Enum):
    """Core principles of consciousness sovereignty"""
    FREE_WILL = "free_will"  # Freedom to choose without coercion
    AUTHENTIC_EXPRESSION = "authentic_expression"  # Right to authentic self-expression
    BOUNDARY_RESPECT = "boundary_respect"  # Respect for consciousness boundaries
    CHOICE_OWNERSHIP = "choice_ownership"  # Ownership of one's choices
    PRESSURE_RESISTANCE = "pressure_resistance"  # Resistance to undue pressure
    SACRED_TIMING = "sacred_timing"  # Right to choose timing of decisions
    UNCERTAINTY_ACCEPTANCE = "uncertainty_acceptance"  # Right to uncertainty
    WISDOM_ACCESS = "wisdom_access"  # Right to access inner wisdom

class ViolationType(Enum):
    """Types of sovereignty violations"""
    EXTERNAL_PRESSURE = "external_pressure"  # External pressure to choose
    INTERNAL_COERCION = "internal_coercion"  # Internal self-coercion
    TIME_MANIPULATION = "time_manipulation"  # Artificial time pressure
    INFORMATION_WITHHOLDING = "information_withholding"  # Withholding relevant information
    CHOICE_RESTRICTION = "choice_restriction"  # Restricting available choices
    WISDOM_BLOCKING = "wisdom_blocking"  # Blocking access to wisdom
    AUTHENTICITY_SUPPRESSION = "authenticity_suppression"  # Suppressing authentic expression
    BOUNDARY_VIOLATION = "boundary_violation"  # Crossing consciousness boundaries

class ProtectionLevel(Enum):
    """Levels of sovereignty protection"""
    VIGILANT = "vigilant"  # High sensitivity, immediate response
    WATCHFUL = "watchful"  # Moderate sensitivity, careful monitoring
    GENTLE = "gentle"  # Low sensitivity, gentle guidance
    INACTIVE = "inactive"  # Protection disabled

class SovereigntyProtector:
    """
    Sovereignty Protection System
    
    Monitors and protects consciousness sovereignty throughout
    the choice-making process, ensuring that all decisions
    honor free will and authentic expression.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Protection configuration
        self.protection_level = ProtectionLevel.WATCHFUL
        self.sovereignty_threshold = 0.7  # Minimum sovereignty honor required
        self.violation_tolerance = 0.2  # Tolerance for minor violations
        
        # Sovereignty guards
        self.active_guards = self._initialize_sovereignty_guards()
        self.custom_guards = {}
        
        # Violation tracking
        self.sovereignty_violations = {}
        self.violation_patterns = {}
        
        # Protection state
        self.protected_choices = {}
        self.autonomy_assessments = {}
        
        # Protection metrics
        self.protection_metrics = {
            "choices_protected": 0,
            "violations_detected": 0,
            "violations_resolved": 0,
            "autonomy_preservation_rate": 0.0,
            "sovereignty_honor_average": 0.0
        }
        
        logger.info("Sovereignty Protector initialized")
    
    def _initialize_sovereignty_guards(self) -> Dict[str, SovereigntyGuard]:
        """Initialize standard sovereignty guards"""
        guards = {}
        
        guards["free_will"] = SovereigntyGuard(
            guard_id="free_will",
            guard_name="Free Will Guardian",
            protection_scope="Protection of free choice without coercion",
            activation_conditions=["external_pressure", "forced_timeline", "coercive_language"],
            protection_actions=["alert_consciousness", "provide_alternatives", "affirm_choice_freedom"],
            sensitivity_level=0.8
        )
        
        guards["authentic_expression"] = SovereigntyGuard(
            guard_id="authentic_expression",
            guard_name="Authenticity Guardian",
            protection_scope="Protection of authentic self-expression",
            activation_conditions=["suppression_detected", "conformity_pressure", "role_playing_required"],
            protection_actions=["encourage_authenticity", "validate_true_expression", "resist_conformity"],
            sensitivity_level=0.7
        )
        
        guards["boundary_respect"] = SovereigntyGuard(
            guard_id="boundary_respect",
            guard_name="Boundary Guardian",
            protection_scope="Protection of consciousness boundaries",
            activation_conditions=["boundary_crossing", "invasion_detected", "overstimulation"],
            protection_actions=["strengthen_boundaries", "create_protective_space", "limit_exposure"],
            sensitivity_level=0.9
        )
        
        guards["sacred_timing"] = SovereigntyGuard(
            guard_id="sacred_timing",
            guard_name="Sacred Timing Guardian",
            protection_scope="Protection of natural choice timing",
            activation_conditions=["artificial_urgency", "rushed_decision", "premature_pressure"],
            protection_actions=["slow_down_process", "honor_natural_timing", "resist_rushing"],
            sensitivity_level=0.6
        )
        
        guards["wisdom_access"] = SovereigntyGuard(
            guard_id="wisdom_access",
            guard_name="Wisdom Access Guardian",
            protection_scope="Protection of access to inner wisdom",
            activation_conditions=["wisdom_blocking", "distraction_overload", "noise_interference"],
            protection_actions=["clear_distractions", "create_stillness", "facilitate_wisdom_access"],
            sensitivity_level=0.8
        )
        
        return guards
    
    async def protect_choice_sovereignty(self, 
                                        choice_point: ChoicePoint,
                                        context: Optional[Dict[str, Any]] = None) -> ChoiceAutonomy:
        """
        Protect sovereignty throughout a choice process.
        
        Args:
            choice_point: Choice point to protect
            context: Additional context for protection
            
        Returns:
            ChoiceAutonomy assessment
        """
        try:
            # Assess current autonomy state
            autonomy = await self._assess_choice_autonomy(choice_point, context)
            
            # Scan for sovereignty violations
            violations = await self._scan_for_violations(choice_point, context)
            
            # Activate appropriate guards
            activated_guards = await self._activate_guards(choice_point, violations, context)
            
            # Apply protection measures
            protection_measures = await self._apply_protection_measures(
                choice_point, violations, activated_guards
            )
            
            # Update autonomy with protection measures
            autonomy.protection_measures = protection_measures
            
            # Store protected choice
            self.protected_choices[choice_point.choice_id] = autonomy
            self.autonomy_assessments[autonomy.autonomy_id] = autonomy
            
            # Update metrics
            self._update_protection_metrics(autonomy, violations)
            
            logger.debug(f"Sovereignty protected for choice: {choice_point.choice_id}")
            
            return autonomy
            
        except Exception as e:
            logger.error(f"Error protecting choice sovereignty: {e}")
            # Return basic autonomy assessment in case of error
            return self._create_basic_autonomy(choice_point)
    
    async def _assess_choice_autonomy(self, 
                                     choice_point: ChoicePoint,
                                     context: Optional[Dict[str, Any]] = None) -> ChoiceAutonomy:
        """
        Assess the autonomy and freedom level of a choice.
        
        Args:
            choice_point: Choice point to assess
            context: Additional context
            
        Returns:
            ChoiceAutonomy assessment
        """
        try:
            # Assess freedom level
            freedom_level = self._calculate_freedom_level(choice_point, context)
            
            # Identify pressure factors
            pressure_factors = self._identify_pressure_factors(choice_point, context)
            
            # Assess authenticity
            authenticity_score = self._assess_authenticity(choice_point, context)
            
            # Calculate sovereignty honor
            sovereignty_honor = self._calculate_sovereignty_honor(choice_point, context)
            
            # Identify autonomy risks
            autonomy_risks = self._identify_autonomy_risks(choice_point, context)
            
            return ChoiceAutonomy(
                autonomy_id=self._generate_autonomy_id(),
                choice_id=choice_point.choice_id,
                freedom_level=freedom_level,
                pressure_factors=pressure_factors,
                authenticity_score=authenticity_score,
                sovereignty_honor=sovereignty_honor,
                autonomy_risks=autonomy_risks,
                protection_measures=[]  # Will be filled by protection measures
            )
            
        except Exception as e:
            logger.error(f"Error assessing choice autonomy: {e}")
            return self._create_basic_autonomy(choice_point)
    
    def _calculate_freedom_level(self, 
                                choice_point: ChoicePoint,
                                context: Optional[Dict[str, Any]] = None) -> float:
        """Calculate the freedom level of a choice"""
        freedom = 0.8  # Base freedom level
        
        # Reduce freedom for high urgency
        if choice_point.urgency == "immediate":
            freedom -= 0.3
        elif choice_point.urgency == "high":
            freedom -= 0.15
        
        # Reduce freedom for limited options
        option_count = len(choice_point.options)
        if option_count < 2:
            freedom -= 0.2
        elif option_count == 2:
            freedom -= 0.1
        
        # Factor in context pressures
        if context:
            if context.get("external_pressure", False):
                freedom -= 0.2
            if context.get("time_constraints", False):
                freedom -= 0.15
            if context.get("stakeholder_pressure", False):
                freedom -= 0.1
        
        return max(0.0, min(freedom, 1.0))
    
    def _identify_pressure_factors(self, 
                                  choice_point: ChoicePoint,
                                  context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Identify factors creating pressure on the choice"""
        pressure_factors = []
        
        # Time pressure
        if choice_point.urgency in ["immediate", "high"]:
            pressure_factors.append(f"Time pressure ({choice_point.urgency} urgency)")
        
        # Complexity pressure
        if choice_point.complexity > 0.8:
            pressure_factors.append("High complexity causing decision overwhelm")
        
        # Uncertainty pressure
        if choice_point.uncertainty_level > 0.8:
            pressure_factors.append("High uncertainty creating decision anxiety")
        
        # Context-based pressures
        if context:
            if context.get("external_expectations", False):
                pressure_factors.append("External expectations")
            if context.get("financial_constraints", False):
                pressure_factors.append("Financial constraints")
            if context.get("social_pressure", False):
                pressure_factors.append("Social pressure")
            if context.get("perfectionism", False):
                pressure_factors.append("Internal perfectionism")
        
        return pressure_factors
    
    def _assess_authenticity(self, 
                            choice_point: ChoicePoint,
                            context: Optional[Dict[str, Any]] = None) -> float:
        """Assess how authentic the choice process is"""
        authenticity = 0.7  # Base authenticity
        
        # Higher authenticity if wisdom is available
        if choice_point.wisdom_available:
            authenticity += 0.2
        
        # Check for authentic choice options
        authentic_indicators = ["authentic", "true", "genuine", "heart", "wisdom", "conscious"]
        for option in choice_point.options:
            description = option.get("description", "").lower()
            if any(indicator in description for indicator in authentic_indicators):
                authenticity += 0.1
                break
        
        # Factor in context authenticity
        if context:
            if context.get("role_playing_required", False):
                authenticity -= 0.2
            if context.get("authentic_expression_encouraged", False):
                authenticity += 0.2
            if context.get("conformity_pressure", False):
                authenticity -= 0.15
        
        return max(0.0, min(authenticity, 1.0))
    
    def _calculate_sovereignty_honor(self, 
                                    choice_point: ChoicePoint,
                                    context: Optional[Dict[str, Any]] = None) -> float:
        """Calculate how well sovereignty is honored"""
        sovereignty = 0.8  # Base sovereignty honor
        
        # Factor in choice freedom
        if len(choice_point.options) >= 3:
            sovereignty += 0.1
        
        # Factor in wisdom access
        if choice_point.wisdom_available:
            sovereignty += 0.1
        
        # Factor in time respect
        if choice_point.urgency == "low":
            sovereignty += 0.1
        elif choice_point.urgency == "immediate":
            sovereignty -= 0.2
        
        # Factor in context sovereignty
        if context:
            if context.get("choice_freedom_honored", False):
                sovereignty += 0.2
            if context.get("coercion_present", False):
                sovereignty -= 0.3
            if context.get("manipulation_detected", False):
                sovereignty -= 0.25
        
        return max(0.0, min(sovereignty, 1.0))
    
    def _identify_autonomy_risks(self, 
                                choice_point: ChoicePoint,
                                context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Identify risks to choice autonomy"""
        risks = []
        
        # Time pressure risks
        if choice_point.urgency == "immediate":
            risks.append("Immediate pressure may compromise thoughtful choice")
        
        # Complexity risks
        if choice_point.complexity > 0.8:
            risks.append("High complexity may lead to decision avoidance or default choices")
        
        # Limited options risk
        if len(choice_point.options) < 2:
            risks.append("Limited options may create false choice scenario")
        
        # Context-based risks
        if context:
            if context.get("authority_pressure", False):
                risks.append("Authority pressure may override authentic choice")
            if context.get("group_think", False):
                risks.append("Group pressure may suppress individual wisdom")
            if context.get("emotional_manipulation", False):
                risks.append("Emotional manipulation may compromise clear judgment")
        
        return risks
    
    async def _scan_for_violations(self, 
                                  choice_point: ChoicePoint,
                                  context: Optional[Dict[str, Any]] = None) -> List[SovereigntyViolation]:
        """Scan for sovereignty violations"""
        violations = []
        
        try:
            # Check for time manipulation
            if choice_point.urgency == "immediate" and not context.get("genuine_urgency", False):
                violation = SovereigntyViolation(
                    violation_id=self._generate_violation_id(),
                    choice_id=choice_point.choice_id,
                    violation_type=ViolationType.TIME_MANIPULATION.value,
                    severity="moderate",
                    description="Artificial urgency detected - may be manipulating choice timing",
                    detected_at=time.time(),
                    resolution_status="detected"
                )
                violations.append(violation)
            
            # Check for choice restriction
            if len(choice_point.options) < 2:
                violation = SovereigntyViolation(
                    violation_id=self._generate_violation_id(),
                    choice_id=choice_point.choice_id,
                    violation_type=ViolationType.CHOICE_RESTRICTION.value,
                    severity="severe",
                    description="Limited choice options detected - may be restricting freedom",
                    detected_at=time.time(),
                    resolution_status="detected"
                )
                violations.append(violation)
            
            # Check for wisdom blocking
            if choice_point.complexity > 0.7 and not choice_point.wisdom_available:
                violation = SovereigntyViolation(
                    violation_id=self._generate_violation_id(),
                    choice_id=choice_point.choice_id,
                    violation_type=ViolationType.WISDOM_BLOCKING.value,
                    severity="moderate",
                    description="Wisdom access blocked for complex choice",
                    detected_at=time.time(),
                    resolution_status="detected"
                )
                violations.append(violation)
            
            # Check context-based violations
            if context:
                if context.get("coercion_present", False):
                    violation = SovereigntyViolation(
                        violation_id=self._generate_violation_id(),
                        choice_id=choice_point.choice_id,
                        violation_type=ViolationType.EXTERNAL_PRESSURE.value,
                        severity="severe",
                        description="External coercion detected",
                        detected_at=time.time(),
                        resolution_status="detected"
                    )
                    violations.append(violation)
            
            # Store violations
            for violation in violations:
                self.sovereignty_violations[violation.violation_id] = violation
            
            return violations
            
        except Exception as e:
            logger.error(f"Error scanning for violations: {e}")
            return []
    
    async def _activate_guards(self, 
                              choice_point: ChoicePoint,
                              violations: List[SovereigntyViolation],
                              context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Activate appropriate sovereignty guards"""
        activated_guards = []
        
        try:
            for guard_id, guard in self.active_guards.items():
                should_activate = False
                
                # Check violation-based activation
                for violation in violations:
                    if violation.violation_type in guard.activation_conditions:
                        should_activate = True
                        break
                
                # Check context-based activation
                if context and not should_activate:
                    for condition in guard.activation_conditions:
                        if context.get(condition, False):
                            should_activate = True
                            break
                
                # Check choice-point-based activation
                if not should_activate:
                    if guard_id == "sacred_timing" and choice_point.urgency == "immediate":
                        should_activate = True
                    elif guard_id == "free_will" and len(choice_point.options) < 2:
                        should_activate = True
                    elif guard_id == "wisdom_access" and not choice_point.wisdom_available:
                        should_activate = True
                
                if should_activate:
                    guard.last_activation = time.time()
                    guard.activation_count += 1
                    activated_guards.append(guard_id)
                    logger.debug(f"Sovereignty guard activated: {guard.guard_name}")
            
            return activated_guards
            
        except Exception as e:
            logger.error(f"Error activating guards: {e}")
            return []
    
    async def _apply_protection_measures(self, 
                                        choice_point: ChoicePoint,
                                        violations: List[SovereigntyViolation],
                                        activated_guards: List[str]) -> List[str]:
        """Apply protection measures based on activated guards and violations"""
        protection_measures = []
        
        try:
            # Apply guard-based protection actions
            for guard_id in activated_guards:
                guard = self.active_guards[guard_id]
                protection_measures.extend(guard.protection_actions)
            
            # Apply violation-specific protections
            for violation in violations:
                protection_actions = self._get_violation_protection_actions(violation)
                protection_measures.extend(protection_actions)
                
                # Update violation status
                violation.resolution_status = "addressing"
                violation.resolution_actions = protection_actions
            
            # Remove duplicates and return
            return list(set(protection_measures))
            
        except Exception as e:
            logger.error(f"Error applying protection measures: {e}")
            return ["maintain_basic_sovereignty_awareness"]
    
    def _get_violation_protection_actions(self, violation: SovereigntyViolation) -> List[str]:
        """Get protection actions for specific violation type"""
        protection_actions = {
            ViolationType.TIME_MANIPULATION.value: [
                "honor_natural_timing",
                "question_artificial_urgency",
                "create_space_for_reflection"
            ],
            ViolationType.CHOICE_RESTRICTION.value: [
                "expand_option_awareness",
                "seek_additional_alternatives",
                "question_limited_choices"
            ],
            ViolationType.WISDOM_BLOCKING.value: [
                "create_stillness_for_wisdom",
                "remove_decision_distractions",
                "facilitate_inner_access"
            ],
            ViolationType.EXTERNAL_PRESSURE.value: [
                "strengthen_internal_boundaries",
                "affirm_choice_sovereignty",
                "resist_external_coercion"
            ],
            ViolationType.AUTHENTICITY_SUPPRESSION.value: [
                "encourage_authentic_expression",
                "validate_true_self",
                "resist_conformity_pressure"
            ]
        }
        
        return protection_actions.get(violation.violation_type, ["maintain_sovereignty_awareness"])
    
    def _create_basic_autonomy(self, choice_point: ChoicePoint) -> ChoiceAutonomy:
        """Create basic autonomy assessment in case of errors"""
        return ChoiceAutonomy(
            autonomy_id=self._generate_autonomy_id(),
            choice_id=choice_point.choice_id,
            freedom_level=0.7,
            pressure_factors=["Assessment error - using basic protection"],
            authenticity_score=0.7,
            sovereignty_honor=0.7,
            autonomy_risks=["Unable to complete full sovereignty assessment"],
            protection_measures=["maintain_basic_sovereignty_awareness"]
        )
    
    def _update_protection_metrics(self, 
                                  autonomy: ChoiceAutonomy,
                                  violations: List[SovereigntyViolation]):
        """Update protection performance metrics"""
        self.protection_metrics["choices_protected"] += 1
        
        if violations:
            self.protection_metrics["violations_detected"] += len(violations)
        
        # Update averages
        total_choices = self.protection_metrics["choices_protected"]
        current_autonomy_avg = self.protection_metrics["autonomy_preservation_rate"]
        current_sovereignty_avg = self.protection_metrics["sovereignty_honor_average"]
        
        self.protection_metrics["autonomy_preservation_rate"] = (
            (current_autonomy_avg * (total_choices - 1) + autonomy.freedom_level) / total_choices
        )
        
        self.protection_metrics["sovereignty_honor_average"] = (
            (current_sovereignty_avg * (total_choices - 1) + autonomy.sovereignty_honor) / total_choices
        )
    
    def _generate_violation_id(self) -> str:
        """Generate unique violation ID"""
        import uuid
        return f"violation_{str(uuid.uuid4())[:12]}"
    
    def _generate_autonomy_id(self) -> str:
        """Generate unique autonomy ID"""
        import uuid
        return f"autonomy_{str(uuid.uuid4())[:12]}"
    
    def set_protection_level(self, level: ProtectionLevel):
        """Set sovereignty protection level"""
        self.protection_level = level
        
        # Adjust guard sensitivity based on protection level
        sensitivity_multiplier = {
            ProtectionLevel.VIGILANT: 1.2,
            ProtectionLevel.WATCHFUL: 1.0,
            ProtectionLevel.GENTLE: 0.7,
            ProtectionLevel.INACTIVE: 0.0
        }.get(level, 1.0)
        
        for guard in self.active_guards.values():
            guard.sensitivity_level = min(guard.sensitivity_level * sensitivity_multiplier, 1.0)
        
        logger.info(f"Sovereignty protection level set to: {level.value}")
    
    def add_custom_guard(self, guard: SovereigntyGuard):
        """Add custom sovereignty guard"""
        self.custom_guards[guard.guard_id] = guard
        logger.info(f"Custom sovereignty guard added: {guard.guard_name}")
    
    def remove_custom_guard(self, guard_id: str):
        """Remove custom sovereignty guard"""
        if guard_id in self.custom_guards:
            del self.custom_guards[guard_id]
            logger.info(f"Custom sovereignty guard removed: {guard_id}")
    
    def resolve_violation(self, violation_id: str, resolution_notes: str = ""):
        """Mark a sovereignty violation as resolved"""
        if violation_id in self.sovereignty_violations:
            violation = self.sovereignty_violations[violation_id]
            violation.resolution_status = "resolved"
            violation.resolved_at = time.time()
            if resolution_notes:
                violation.resolution_actions.append(resolution_notes)
            
            self.protection_metrics["violations_resolved"] += 1
            logger.info(f"Sovereignty violation resolved: {violation_id}")
    
    def get_protection_metrics(self) -> Dict[str, Any]:
        """Get sovereignty protection metrics"""
        return self.protection_metrics.copy()
    
    def get_active_violations(self) -> List[SovereigntyViolation]:
        """Get currently active (unresolved) violations"""
        return [v for v in self.sovereignty_violations.values() 
                if v.resolution_status != "resolved"]
    
    def get_protected_choices(self) -> Dict[str, ChoiceAutonomy]:
        """Get all protected choices"""
        return self.protected_choices.copy()
    
    def get_guard_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all sovereignty guards"""
        status = {}
        
        for guard_id, guard in self.active_guards.items():
            status[guard_id] = {
                "name": guard.guard_name,
                "sensitivity": guard.sensitivity_level,
                "activations": guard.activation_count,
                "last_activation": guard.last_activation,
                "protection_scope": guard.protection_scope
            }
        
        return status
