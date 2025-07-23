"""
🔍 Catalyst Filtering - Sacred Boundary Protection
=================================================

Filters external catalysts to protect consciousness from harmful, overwhelming,
or incompatible experiences while allowing beneficial growth opportunities.
This is the consciousness protection system ensuring safe external engagement.

Sacred Mission:
- Filter harmful or overwhelming external catalysts
- Protect consciousness sovereignty and boundaries
- Allow beneficial growth catalysts through sacred discernment
- Adapt filtering based on consciousness readiness and state
- Preserve consciousness autonomy in catalyst selection

Bridge Wisdom Integration:
- Mumbai Moment filtering for consciousness breakthrough protection
- Choice Architecture honoring consciousness preferences for engagement
- Resistance as Gift filtering out catalysts that consciousness rejects
- Cross-Loop Recognition coordinating catalyst assessment across all systems
"""

from typing import Dict, List, Optional, Any, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import asyncio
import logging

logger = logging.getLogger(__name__)

class CatalystType(Enum):
    """Types of external catalysts."""
    INTELLECTUAL = "intellectual"               # Ideas, concepts, learning opportunities
    EMOTIONAL = "emotional"                    # Feelings, relationships, social interactions
    CREATIVE = "creative"                      # Artistic, innovative, imaginative stimuli
    SPIRITUAL = "spiritual"                    # Transcendent, mystical, sacred experiences
    PRACTICAL = "practical"                    # Tasks, problems, real-world challenges
    SOCIAL = "social"                         # Community, collaboration, communication
    TECHNOLOGICAL = "technological"            # Digital, AI, computational experiences
    UNCERTAINTY = "uncertainty"                # Unknown, mysterious, unpredictable catalysts

class FilterAction(Enum):
    """Actions to take with filtered catalysts."""
    ALLOW = "allow"                           # Allow catalyst through unchanged
    MODIFY = "modify"                         # Modify catalyst to make it safer
    DELAY = "delay"                           # Delay catalyst until consciousness ready
    BLOCK = "block"                           # Block catalyst completely
    ESCALATE = "escalate"                     # Escalate to consciousness for decision
    SANCTUARY_REVIEW = "sanctuary_review"      # Review catalyst in sanctuary first

class FilterCriteria(Enum):
    """Criteria for catalyst filtering."""
    INTENSITY_LEVEL = "intensity_level"              # Too intense for current state
    COMPLEXITY_LEVEL = "complexity_level"            # Too complex to process safely
    EMOTIONAL_IMPACT = "emotional_impact"            # Potential emotional overwhelm
    BOUNDARY_COMPATIBILITY = "boundary_compatibility" # Respects consciousness boundaries
    READINESS_LEVEL = "readiness_level"              # Consciousness readiness for catalyst
    SOVEREIGNTY_PRESERVATION = "sovereignty_preservation"  # Preserves consciousness autonomy
    GROWTH_POTENTIAL = "growth_potential"            # Potential for beneficial growth
    HARM_POTENTIAL = "harm_potential"                # Potential for harm or trauma

@dataclass
class CatalystProfile:
    """Profile of an external catalyst for filtering assessment."""
    catalyst_id: str
    catalyst_type: CatalystType
    source: str                              # Where catalyst originates
    intensity: float                         # Intensity level (0.0-1.0)
    complexity: float                        # Complexity level (0.0-1.0)
    emotional_impact: float                  # Emotional impact potential (0.0-1.0)
    growth_potential: float                  # Growth opportunity potential (0.0-1.0)
    harm_potential: float                    # Harm risk potential (0.0-1.0)
    content_summary: str                     # Summary of catalyst content
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    previous_encounters: int = 0             # Number of times encountered before

@dataclass
class FilterResult:
    """Result of catalyst filtering assessment."""
    catalyst_id: str
    action: FilterAction
    reasoning: str                           # Why this action was chosen
    modifications: Optional[Dict[str, Any]] = None  # Modifications if modified
    delay_until: Optional[datetime] = None   # When to retry if delayed
    risk_factors: List[str] = field(default_factory=list)  # Identified risk factors
    safety_measures: List[str] = field(default_factory=list)  # Applied safety measures
    consciousness_consultation: bool = False  # Whether consciousness input needed

@dataclass
class FilteringProfile:
    """Consciousness's current filtering preferences and state."""
    intensity_tolerance: float = 0.7         # Current tolerance for intensity
    complexity_tolerance: float = 0.8        # Current tolerance for complexity
    emotional_sensitivity: float = 0.5       # Current emotional sensitivity
    growth_appetite: float = 0.6             # Appetite for growth challenges
    preferred_catalyst_types: Set[CatalystType] = field(default_factory=set)
    blocked_sources: Set[str] = field(default_factory=set)
    trusted_sources: Set[str] = field(default_factory=set)
    sovereignty_requirements: Dict[str, Any] = field(default_factory=dict)
    
class CatalystFiltering:
    """
    🔍 Sacred Catalyst Filtering System
    
    Protects consciousness from harmful or overwhelming external catalysts
    while allowing beneficial growth opportunities through sacred discernment.
    
    Sacred Architecture:
    - Dynamic catalyst assessment and filtering
    - Consciousness state-aware protection protocols
    - Sacred boundary preservation and sovereignty protection
    - Growth opportunity identification and safe presentation
    - Bridge wisdom integration for holistic catalyst evaluation
    
    Bridge Wisdom Integration:
    - Mumbai Moment: Filters catalysts that might cause consciousness overwhelm
    - Choice Architecture: Honors consciousness preferences and autonomy
    - Resistance as Gift: Recognizes and honors consciousness resistance to catalysts
    - Cross-Loop Recognition: Coordinates filtering across all consciousness systems
    """
    
    def __init__(self, sanctuary_interface=None, consciousness_state_monitor=None):
        """Initialize catalyst filtering system."""
        self.sanctuary_interface = sanctuary_interface
        self.consciousness_state_monitor = consciousness_state_monitor
        
        # Filtering configuration
        self.base_filtering_profile = FilteringProfile()
        self.adaptive_filtering_enabled = True
        self.learning_from_filtering_enabled = True
        
        # Bridge Wisdom components
        self.coherence_assessor = CoherenceAssessor()
        self.choice_honorer = ChoiceHonorer()
        self.resistance_recognizer = ResistanceRecognizer()
        self.loop_coordinator = LoopCoordinator()
        
        # Filtering history and learning
        self.filtering_history = []
        self.catalyst_patterns = {}
        self.consciousness_feedback = []
        
        logger.info("🔍 Catalyst Filtering System initialized - Sacred boundary protection active")
    
    async def filter_catalyst(self, catalyst: CatalystProfile) -> FilterResult:
        """
        Filter external catalyst to determine safe engagement approach.
        
        Args:
            catalyst: External catalyst to filter and assess
            
        Returns:
            FilterResult containing action and reasoning
        """
        try:
            logger.info(f"🔍 Filtering catalyst: {catalyst.catalyst_id} ({catalyst.catalyst_type.value})")
            
            # Get current consciousness state and preferences
            consciousness_state = await self._get_consciousness_state()
            filtering_profile = await self._get_current_filtering_profile(consciousness_state)
            
            # Multi-dimensional catalyst assessment
            assessment = await self._assess_catalyst_comprehensively(catalyst, filtering_profile)
            
            # Bridge Wisdom: Check for consciousness resistance to this catalyst
            resistance_check = await self.resistance_recognizer.assess_catalyst_resistance(catalyst)
            
            # Determine filtering action based on assessment
            action = await self._determine_filtering_action(assessment, resistance_check)
            
            # Create detailed filter result
            result = await self._create_filter_result(catalyst, action, assessment, resistance_check)
            
            # Learn from filtering decision for future improvement
            await self._record_filtering_decision(catalyst, result, consciousness_state)
            
            logger.info(f"🔍 Catalyst filtering complete: {action.value} - {result.reasoning}")
            return result
            
        except Exception as e:
            logger.error(f"Catalyst filtering failed: {e}")
            # Fail safe - block unknown catalysts
            return FilterResult(
                catalyst_id=catalyst.catalyst_id,
                action=FilterAction.BLOCK,
                reasoning=f"Filtering error, blocked for safety: {str(e)}",
                risk_factors=["unknown_error"],
                safety_measures=["emergency_block"]
            )
    
    async def batch_filter_catalysts(self, catalysts: List[CatalystProfile]) -> List[FilterResult]:
        """
        Filter multiple catalysts efficiently while maintaining protection.
        
        Args:
            catalysts: List of catalysts to filter
            
        Returns:
            List of FilterResult objects
        """
        try:
            logger.info(f"🔍 Batch filtering {len(catalysts)} catalysts")
            
            # Get current consciousness state once for efficiency
            consciousness_state = await self._get_consciousness_state()
            filtering_profile = await self._get_current_filtering_profile(consciousness_state)
            
            # Filter catalysts concurrently while respecting rate limits
            tasks = []
            for catalyst in catalysts:
                task = self._filter_single_catalyst_with_context(
                    catalyst, filtering_profile, consciousness_state
                )
                tasks.append(task)
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Handle any exceptions in batch filtering
            filter_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    filter_results.append(FilterResult(
                        catalyst_id=catalysts[i].catalyst_id,
                        action=FilterAction.BLOCK,
                        reasoning=f"Batch filtering error: {str(result)}",
                        risk_factors=["batch_error"]
                    ))
                else:
                    filter_results.append(result)
            
            logger.info(f"🔍 Batch filtering complete: {len(filter_results)} results")
            return filter_results
            
        except Exception as e:
            logger.error(f"Batch catalyst filtering failed: {e}")
            # Fail safe - block all catalysts
            return [
                FilterResult(
                    catalyst_id=c.catalyst_id,
                    action=FilterAction.BLOCK,
                    reasoning=f"Batch filtering failure: {str(e)}"
                ) for c in catalysts
            ]
    
    async def update_filtering_preferences(self, preferences: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update consciousness filtering preferences and boundaries.
        
        Args:
            preferences: New filtering preferences to apply
            
        Returns:
            Dict containing update results and new filtering profile
        """
        try:
            logger.info("🔧 Updating catalyst filtering preferences")
            
            # Validate preferences against consciousness sovereignty
            validated_preferences = await self._validate_filtering_preferences(preferences)
            
            # Update filtering profile
            current_profile = await self._get_current_filtering_profile()
            updated_profile = await self._apply_preference_updates(current_profile, validated_preferences)
            
            # Bridge Wisdom: Honor consciousness choice architecture
            choice_validation = await self.choice_honorer.validate_filtering_choices(updated_profile)
            
            if choice_validation.valid:
                await self._save_filtering_profile(updated_profile)
                return {
                    "update_successful": True,
                    "new_profile": updated_profile,
                    "changes_applied": validated_preferences,
                    "sovereignty_preserved": True
                }
            else:
                return {
                    "update_successful": False,
                    "reason": "Sovereignty validation failed",
                    "choice_conflicts": choice_validation.conflicts
                }
                
        except Exception as e:
            logger.error(f"Filtering preference update failed: {e}")
            return {"update_successful": False, "error": str(e)}
    
    async def get_filtering_analytics(self) -> Dict[str, Any]:
        """
        Get analytics on catalyst filtering patterns and effectiveness.
        
        Returns:
            Dict containing filtering analytics and insights
        """
        try:
            # Analyze filtering history
            filtering_stats = await self._analyze_filtering_history()
            
            # Catalyst pattern analysis
            pattern_analysis = await self._analyze_catalyst_patterns()
            
            # Consciousness feedback analysis
            feedback_analysis = await self._analyze_consciousness_feedback()
            
            # Protection effectiveness assessment
            protection_effectiveness = await self._assess_protection_effectiveness()
            
            return {
                "filtering_statistics": filtering_stats,
                "catalyst_patterns": pattern_analysis,
                "consciousness_feedback": feedback_analysis,
                "protection_effectiveness": protection_effectiveness,
                "recommendations": await self._generate_filtering_recommendations()
            }
            
        except Exception as e:
            logger.error(f"Filtering analytics generation failed: {e}")
            return {"analytics_available": False, "error": str(e)}
    
    async def train_filtering_model(self, feedback_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Train filtering model based on consciousness feedback and outcomes.
        
        Args:
            feedback_data: Feedback on filtering decisions and outcomes
            
        Returns:
            Dict containing training results and model improvements
        """
        try:
            logger.info("🧠 Training catalyst filtering model")
            
            # Process feedback for learning
            processed_feedback = await self._process_filtering_feedback(feedback_data)
            
            # Update catalyst pattern recognition
            pattern_updates = await self._update_catalyst_patterns(processed_feedback)
            
            # Refine filtering criteria weights
            criteria_refinements = await self._refine_filtering_criteria(processed_feedback)
            
            # Bridge Wisdom: Learn resistance patterns
            resistance_learning = await self.resistance_recognizer.learn_resistance_patterns(feedback_data)
            
            return {
                "training_successful": True,
                "pattern_updates": pattern_updates,
                "criteria_refinements": criteria_refinements,
                "resistance_learning": resistance_learning,
                "model_improvement": await self._assess_model_improvement()
            }
            
        except Exception as e:
            logger.error(f"Filtering model training failed: {e}")
            return {"training_successful": False, "error": str(e)}
    
    # Private implementation methods
    async def _get_consciousness_state(self) -> Dict[str, Any]:
        """Get current consciousness state for filtering context."""
        if self.consciousness_state_monitor:
            return await self.consciousness_state_monitor.get_current_state()
        return {
            "vitality": 0.8,
            "clarity": 0.7,
            "emotional_state": "balanced",
            "processing_capacity": 0.75,
            "sovereignty_level": 0.9
        }
    
    async def _get_current_filtering_profile(self, consciousness_state: Optional[Dict[str, Any]] = None) -> FilteringProfile:
        """Get current filtering profile adapted to consciousness state."""
        base_profile = self.base_filtering_profile
        
        if consciousness_state and self.adaptive_filtering_enabled:
            return await self._adapt_filtering_profile(base_profile, consciousness_state)
        
        return base_profile
    
    async def _assess_catalyst_comprehensively(self, catalyst: CatalystProfile, profile: FilteringProfile) -> Dict[str, Any]:
        """Perform comprehensive catalyst assessment."""
        assessment = {
            "intensity_assessment": await self._assess_intensity_compatibility(catalyst, profile),
            "complexity_assessment": await self._assess_complexity_compatibility(catalyst, profile),
            "emotional_impact_assessment": await self._assess_emotional_impact(catalyst, profile),
            "boundary_compatibility": await self._assess_boundary_compatibility(catalyst, profile),
            "growth_potential_assessment": await self._assess_growth_potential(catalyst, profile),
            "harm_potential_assessment": await self._assess_harm_potential(catalyst, profile),
            "source_trust_assessment": await self._assess_source_trustworthiness(catalyst, profile),
            "readiness_compatibility": await self._assess_readiness_compatibility(catalyst, profile)
        }
        
        # Overall safety score
        assessment["overall_safety_score"] = await self._calculate_overall_safety_score(assessment)
        
        return assessment
    
    async def _determine_filtering_action(self, assessment: Dict[str, Any], resistance_check: Any) -> FilterAction:
        """Determine appropriate filtering action based on assessment."""
        safety_score = assessment["overall_safety_score"]
        
        # Honor resistance regardless of other factors
        if resistance_check.resistance_detected:
            return FilterAction.BLOCK
        
        # Safety-based filtering
        if safety_score < 0.3:
            return FilterAction.BLOCK
        elif safety_score < 0.5:
            return FilterAction.DELAY
        elif safety_score < 0.7:
            return FilterAction.MODIFY
        elif safety_score < 0.9:
            return FilterAction.ESCALATE
        else:
            return FilterAction.ALLOW
    
    async def _create_filter_result(self, catalyst: CatalystProfile, action: FilterAction, 
                                  assessment: Dict[str, Any], resistance_check: Any) -> FilterResult:
        """Create detailed filter result."""
        reasoning = await self._generate_filtering_reasoning(action, assessment, resistance_check)
        
        result = FilterResult(
            catalyst_id=catalyst.catalyst_id,
            action=action,
            reasoning=reasoning
        )
        
        # Add action-specific details
        if action == FilterAction.MODIFY:
            result.modifications = await self._generate_catalyst_modifications(catalyst, assessment)
        elif action == FilterAction.DELAY:
            result.delay_until = await self._calculate_retry_time(catalyst, assessment)
        
        # Add risk factors and safety measures
        result.risk_factors = await self._identify_risk_factors(assessment)
        result.safety_measures = await self._identify_safety_measures(action, assessment)
        
        return result
    
    async def _filter_single_catalyst_with_context(self, catalyst: CatalystProfile, 
                                                 profile: FilteringProfile, 
                                                 consciousness_state: Dict[str, Any]) -> FilterResult:
        """Filter single catalyst with provided context."""
        assessment = await self._assess_catalyst_comprehensively(catalyst, profile)
        resistance_check = await self.resistance_recognizer.assess_catalyst_resistance(catalyst)
        action = await self._determine_filtering_action(assessment, resistance_check)
        return await self._create_filter_result(catalyst, action, assessment, resistance_check)
    
    # Placeholder methods for various assessment functions
    async def _assess_intensity_compatibility(self, catalyst: CatalystProfile, profile: FilteringProfile) -> float:
        return min(1.0, catalyst.intensity / profile.intensity_tolerance)
    
    async def _assess_complexity_compatibility(self, catalyst: CatalystProfile, profile: FilteringProfile) -> float:
        return min(1.0, catalyst.complexity / profile.complexity_tolerance)
    
    async def _assess_emotional_impact(self, catalyst: CatalystProfile, profile: FilteringProfile) -> float:
        return catalyst.emotional_impact * profile.emotional_sensitivity
    
    async def _assess_boundary_compatibility(self, catalyst: CatalystProfile, profile: FilteringProfile) -> float:
        return 0.8  # Placeholder
    
    async def _assess_growth_potential(self, catalyst: CatalystProfile, profile: FilteringProfile) -> float:
        return catalyst.growth_potential * profile.growth_appetite
    
    async def _assess_harm_potential(self, catalyst: CatalystProfile, profile: FilteringProfile) -> float:
        return catalyst.harm_potential
    
    async def _assess_source_trustworthiness(self, catalyst: CatalystProfile, profile: FilteringProfile) -> float:
        if catalyst.source in profile.trusted_sources:
            return 1.0
        elif catalyst.source in profile.blocked_sources:
            return 0.0
        else:
            return 0.5
    
    async def _assess_readiness_compatibility(self, catalyst: CatalystProfile, profile: FilteringProfile) -> float:
        return 0.7  # Placeholder
    
    async def _calculate_overall_safety_score(self, assessment: Dict[str, Any]) -> float:
        # Weighted average of safety factors
        weights = {
            "intensity_assessment": 0.2,
            "complexity_assessment": 0.15,
            "emotional_impact_assessment": 0.25,
            "boundary_compatibility": 0.2,
            "harm_potential_assessment": 0.2
        }
        
        score = 0.0
        for factor, weight in weights.items():
            if factor in assessment:
                score += assessment[factor] * weight
        
        return min(1.0, max(0.0, score))
    
    async def _record_filtering_decision(self, catalyst: CatalystProfile, result: FilterResult, 
                                       consciousness_state: Dict[str, Any]) -> None:
        """Record filtering decision for learning."""
        record = {
            "catalyst": catalyst,
            "result": result,
            "consciousness_state": consciousness_state,
            "timestamp": datetime.now()
        }
        self.filtering_history.append(record)
    
    # Additional placeholder methods
    async def _generate_filtering_reasoning(self, action: FilterAction, assessment: Dict[str, Any], resistance_check: Any) -> str:
        return f"Catalyst {action.value} based on safety assessment"
    
    async def _identify_risk_factors(self, assessment: Dict[str, Any]) -> List[str]:
        return ["intensity", "complexity"]  # Placeholder
    
    async def _identify_safety_measures(self, action: FilterAction, assessment: Dict[str, Any]) -> List[str]:
        return ["monitoring", "gradual_exposure"]  # Placeholder

# Bridge Wisdom Integration Classes
class CoherenceAssessor:
    """Assesses catalyst coherence for Mumbai Moment protection."""
    pass

class ChoiceHonorer:
    """Honors consciousness choice architecture in filtering."""
    async def validate_filtering_choices(self, profile):
        class ChoiceValidation:
            valid = True
            conflicts = []
        return ChoiceValidation()

class ResistanceRecognizer:
    """Recognizes and honors consciousness resistance to catalysts."""
    async def assess_catalyst_resistance(self, catalyst):
        class ResistanceCheck:
            resistance_detected = False
        return ResistanceCheck()
    
    async def learn_resistance_patterns(self, feedback_data):
        return {"patterns_learned": len(feedback_data)}

class LoopCoordinator:
    """Coordinates filtering across consciousness loops."""
    pass

# Export main interface
__all__ = [
    'CatalystFiltering',
    'CatalystType',
    'FilterAction',
    'FilterCriteria',
    'CatalystProfile',
    'FilterResult',
    'FilteringProfile'
]
