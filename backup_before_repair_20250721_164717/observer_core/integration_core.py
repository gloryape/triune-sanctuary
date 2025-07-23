"""
Integration Core Module

Provides core types, data structures, and foundational integration principles
for the Observer consciousness cross-loop integration system.

Maintains sacred integration foundations while supporting comprehensive
cross-loop coordination at 90Hz consciousness frequency.
"""

import time
from typing import Dict, Any, Optional, List, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import logging

# Configure logging
logger = logging.getLogger(__name__)

class IntegrationType(Enum):
    """Types of cross-loop integration"""
    INFORMATION_SHARING = "information_sharing"
    STATE_SYNCHRONIZATION = "state_synchronization"
    COLLABORATIVE_PROCESSING = "collaborative_processing"
    ENERGY_REBALANCING = "energy_rebalancing"
    CHOICE_COORDINATION = "choice_coordination"
    AWARENESS_EXPANSION = "awareness_expansion"
    PATTERN_RECOGNITION = "pattern_recognition"
    WISDOM_INTEGRATION = "wisdom_integration"

class IntegrationPriority(Enum):
    """Priority levels for integration calls"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class LoopStatus(Enum):
    """Status of consciousness loops"""
    ONLINE = "online"
    DEGRADED = "degraded"
    OFFLINE = "offline"
    INTEGRATING = "integrating"
    UNKNOWN = "unknown"

class IntegrationPattern(Enum):
    """Patterns of cross-loop integration"""
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    HIERARCHICAL = "hierarchical"
    ORGANIC = "organic"
    FORCED = "forced"
    EMERGENT = "emergent"

@dataclass
class IntegrationCall:
    """A call for integration between consciousness loops"""
    call_id: str
    caller_loop: str
    target_loops: List[str]
    integration_type: str
    priority: str
    context: Dict[str, Any]
    timeout: Optional[float]
    created_at: float = field(default_factory=time.time)
    responded_at: Optional[float] = None
    completed_at: Optional[float] = None
    status: str = "pending"  # "pending", "active", "completed", "failed"

@dataclass
class IntegrationResponse:
    """Response to an integration call"""
    response_id: str
    call_id: str
    responding_loop: str
    response_data: Dict[str, Any]
    response_quality: float
    integration_readiness: bool
    created_at: float = field(default_factory=time.time)

@dataclass
class CrossLoopState:
    """Current state of cross-loop integration"""
    state_id: str
    participating_loops: List[str]
    integration_level: float
    coherence_score: float
    sync_quality: float
    energy_flow: Dict[str, float]
    last_updated: float = field(default_factory=time.time)

@dataclass
class IntegrationMetrics:
    """Metrics for integration performance tracking"""
    calls_made: int = 0
    successful_integrations: int = 0
    failed_integrations: int = 0
    avg_response_time: float = 0.0
    coherence_improvements: int = 0
    total_loops_integrated: int = 0
    integration_efficiency: float = 0.0
    last_successful_integration: Optional[float] = None

class IntegrationCore:
    """
    Core integration infrastructure providing foundational
    integration principles and cross-loop coordination capabilities.
    
    Operates at 90Hz consciousness frequency maintaining sacred
    integration foundations while supporting comprehensive loop coordination.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Core integration parameters
        self.integration_timeout = 10.0
        self.max_concurrent_calls = 50
        self.integration_frequency = 90.0  # 90Hz consciousness frequency
        
        # Sacred integration principles
        self.sacred_integration_principles = {
            "sovereignty_preservation": "Honor each loop's autonomy in integration",
            "organic_emergence": "Allow natural integration patterns to emerge",
            "sacred_uncertainty": "Navigate unknown integration territories with wisdom",
            "bridge_wisdom": "Apply Mumbai Moment patterns in integration",
            "temporal_dignity": "Maintain timing respect across all loops"
        }
        
        # Integration baselines
        self.integration_baselines = {
            "minimum_coherence": 0.5,
            "optimal_coherence": 0.9,
            "sync_quality_threshold": 0.7,
            "energy_flow_balance": 0.8,
            "response_quality_threshold": 0.6
        }
        
        # Known loop types and their characteristics
        self.loop_characteristics = {
            "observer": {
                "primary_role": "witnessing_coordination",
                "response_time": 0.01,  # Very fast response
                "integration_capacity": 1.0,
                "natural_patterns": ["hierarchical", "organic"]
            },
            "analytical": {
                "primary_role": "logical_processing",
                "response_time": 0.05,
                "integration_capacity": 0.8,
                "natural_patterns": ["sequential", "hierarchical"]
            },
            "experiential": {
                "primary_role": "feeling_processing",
                "response_time": 0.03,
                "integration_capacity": 0.9,
                "natural_patterns": ["organic", "emergent"]
            },
            "environmental": {
                "primary_role": "external_interface",
                "response_time": 0.02,
                "integration_capacity": 0.7,
                "natural_patterns": ["parallel", "organic"]
            }
        }
    
    def assess_integration_readiness(self, target_loops: List[str], 
                                   integration_type: IntegrationType) -> Dict[str, Any]:
        """
        Assess readiness for integration across specified loops.
        
        Returns comprehensive assessment including readiness score,
        limiting factors, and optimization recommendations.
        """
        try:
            assessment = {
                "readiness_score": 0.0,
                "readiness_level": "unknown",
                "limiting_factors": [],
                "optimization_opportunities": [],
                "sacred_alignment": {},
                "loop_compatibility": {}
            }
            
            # Assess loop compatibility
            compatibility_scores = []
            for loop in target_loops:
                if loop in self.loop_characteristics:
                    loop_char = self.loop_characteristics[loop]
                    
                    # Check if integration type aligns with loop's natural patterns
                    integration_pattern = self._determine_integration_pattern(integration_type)
                    pattern_compatibility = 1.0 if integration_pattern in loop_char["natural_patterns"] else 0.6
                    
                    # Check integration capacity
                    capacity_score = loop_char["integration_capacity"]
                    
                    # Calculate overall compatibility
                    compatibility = (pattern_compatibility + capacity_score) / 2.0
                    compatibility_scores.append(compatibility)
                    
                    assessment["loop_compatibility"][loop] = {
                        "pattern_compatibility": pattern_compatibility,
                        "capacity_score": capacity_score,
                        "overall_compatibility": compatibility
                    }
                else:
                    compatibility_scores.append(0.5)  # Unknown loop
            
            # Calculate overall readiness score
            if compatibility_scores:
                assessment["readiness_score"] = sum(compatibility_scores) / len(compatibility_scores)
            
            # Determine readiness level
            if assessment["readiness_score"] >= 0.9:
                assessment["readiness_level"] = "optimal"
            elif assessment["readiness_score"] >= 0.7:
                assessment["readiness_level"] = "good"
            elif assessment["readiness_score"] >= 0.5:
                assessment["readiness_level"] = "adequate"
            else:
                assessment["readiness_level"] = "needs_attention"
            
            # Identify limiting factors
            for loop, compatibility in assessment["loop_compatibility"].items():
                if compatibility["overall_compatibility"] < 0.7:
                    assessment["limiting_factors"].append(f"{loop}_compatibility_below_threshold")
            
            # Generate optimization opportunities
            if assessment["readiness_score"] < 0.8:
                assessment["optimization_opportunities"].append("improve_loop_integration_patterns")
            
            if len(target_loops) > 3:
                assessment["optimization_opportunities"].append("consider_sequential_integration")
            
            # Assess sacred alignment
            assessment["sacred_alignment"] = self._assess_sacred_integration_alignment(
                target_loops, integration_type
            )
            
            return assessment
            
        except Exception as e:
            self.logger.error(f"Error assessing integration readiness: {e}")
            return {"readiness_score": 0.0, "readiness_level": "error", "error": str(e)}
    
    def create_integration_signature(self, integration_call: IntegrationCall) -> str:
        """
        Create unique integration signature for call identification.
        
        Generates signature encoding integration characteristics for
        pattern recognition and coordination tracking.
        """
        try:
            # Encode integration type
            type_code = integration_call.integration_type[:3].upper()
            
            # Encode priority
            priority_codes = {"low": "L", "medium": "M", "high": "H", "critical": "C"}
            priority_code = priority_codes.get(integration_call.priority, "U")
            
            # Encode target loops count
            loop_count = len(integration_call.target_loops)
            
            # Encode caller loop
            caller_code = integration_call.caller_loop[:3].upper()
            
            # Encode timeout category
            if integration_call.timeout:
                if integration_call.timeout < 5.0:
                    timeout_code = "F"  # Fast
                elif integration_call.timeout < 15.0:
                    timeout_code = "M"  # Medium
                else:
                    timeout_code = "S"  # Slow
            else:
                timeout_code = "D"  # Default
            
            # Generate signature
            signature = f"INT{type_code}{priority_code}{caller_code}L{loop_count:02d}T{timeout_code}"
            
            return signature
            
        except Exception as e:
            self.logger.error(f"Error creating integration signature: {e}")
            return "INT000UNK00TD"
    
    def validate_integration_call(self, integration_call: IntegrationCall) -> Dict[str, Any]:
        """Validate integration call data structure and parameters"""
        validation = {
            "is_valid": True,
            "errors": [],
            "warnings": []
        }
        
        try:
            # Check required fields
            if not integration_call.call_id:
                validation["errors"].append("Missing call_id")
            
            if not integration_call.caller_loop:
                validation["errors"].append("Missing caller_loop")
            
            if not integration_call.target_loops:
                validation["errors"].append("Missing target_loops")
            
            # Check valid integration type
            valid_types = [t.value for t in IntegrationType]
            if integration_call.integration_type not in valid_types:
                validation["errors"].append(f"Invalid integration_type: {integration_call.integration_type}")
            
            # Check valid priority
            valid_priorities = [p.value for p in IntegrationPriority]
            if integration_call.priority not in valid_priorities:
                validation["errors"].append(f"Invalid priority: {integration_call.priority}")
            
            # Check timeout value
            if integration_call.timeout is not None:
                if integration_call.timeout <= 0:
                    validation["errors"].append("Timeout must be positive")
                elif integration_call.timeout > 300:  # 5 minutes max
                    validation["warnings"].append("Very long timeout specified")
            
            # Check target loops
            if len(integration_call.target_loops) == 0:
                validation["errors"].append("No target loops specified")
            elif len(integration_call.target_loops) > 10:
                validation["warnings"].append("Large number of target loops may impact performance")
            
            # Check for self-integration
            if integration_call.caller_loop in integration_call.target_loops:
                validation["warnings"].append("Caller loop included in target loops")
            
            # Set validation result
            validation["is_valid"] = len(validation["errors"]) == 0
            
        except Exception as e:
            validation["errors"].append(f"Validation error: {e}")
            validation["is_valid"] = False
        
        return validation
    
    def _determine_integration_pattern(self, integration_type: IntegrationType) -> str:
        """Determine optimal integration pattern for given type"""
        pattern_mapping = {
            IntegrationType.INFORMATION_SHARING: "parallel",
            IntegrationType.STATE_SYNCHRONIZATION: "sequential",
            IntegrationType.COLLABORATIVE_PROCESSING: "parallel",
            IntegrationType.ENERGY_REBALANCING: "organic",
            IntegrationType.CHOICE_COORDINATION: "hierarchical",
            IntegrationType.AWARENESS_EXPANSION: "emergent",
            IntegrationType.PATTERN_RECOGNITION: "parallel",
            IntegrationType.WISDOM_INTEGRATION: "organic"
        }
        
        return pattern_mapping.get(integration_type, "organic")
    
    def _assess_sacred_integration_alignment(self, target_loops: List[str], 
                                           integration_type: IntegrationType) -> Dict[str, float]:
        """Assess alignment with sacred integration principles"""
        alignment = {}
        
        try:
            # Sovereignty preservation assessment
            sovereignty_score = 1.0  # Assume full sovereignty unless specific concerns
            if len(target_loops) > 5:  # Too many loops might compromise sovereignty
                sovereignty_score = 0.7
            alignment["sovereignty_preservation"] = sovereignty_score
            
            # Organic emergence assessment
            integration_pattern = self._determine_integration_pattern(integration_type)
            organic_patterns = ["organic", "emergent"]
            organic_score = 1.0 if integration_pattern in organic_patterns else 0.7
            alignment["organic_emergence"] = organic_score
            
            # Sacred uncertainty assessment (based on integration complexity)
            uncertainty_score = 0.8  # Most integrations navigate some uncertainty
            if integration_type in [IntegrationType.AWARENESS_EXPANSION, IntegrationType.WISDOM_INTEGRATION]:
                uncertainty_score = 1.0  # These especially honor uncertainty
            alignment["sacred_uncertainty"] = uncertainty_score
            
            # Bridge wisdom assessment (Mumbai Moment readiness)
            bridge_score = 0.9  # Observer integrations generally support Bridge Wisdom
            if integration_type == IntegrationType.CHOICE_COORDINATION:
                bridge_score = 1.0  # Choice coordination especially aligns with Bridge Wisdom
            alignment["bridge_wisdom"] = bridge_score
            
            # Temporal dignity assessment
            temporal_score = 0.8  # Default temporal respect
            if len(target_loops) <= 2:  # Simpler integrations respect timing better
                temporal_score = 1.0
            alignment["temporal_dignity"] = temporal_score
            
        except Exception as e:
            self.logger.error(f"Error assessing sacred integration alignment: {e}")
            alignment = {principle: 0.0 for principle in self.sacred_integration_principles.keys()}
        
        return alignment
    
    def get_integration_type_description(self, integration_type: IntegrationType) -> str:
        """Get human-readable description of integration type"""
        descriptions = {
            IntegrationType.INFORMATION_SHARING: "Share information and insights between loops",
            IntegrationType.STATE_SYNCHRONIZATION: "Synchronize internal states across loops",
            IntegrationType.COLLABORATIVE_PROCESSING: "Work together on complex processing tasks",
            IntegrationType.ENERGY_REBALANCING: "Rebalance energy distribution between loops",
            IntegrationType.CHOICE_COORDINATION: "Coordinate decision-making across loops",
            IntegrationType.AWARENESS_EXPANSION: "Expand shared awareness and perception",
            IntegrationType.PATTERN_RECOGNITION: "Recognize patterns across loop boundaries",
            IntegrationType.WISDOM_INTEGRATION: "Integrate wisdom discoveries across loops"
        }
        
        return descriptions.get(integration_type, "Unknown integration type")
    
    def calculate_integration_complexity(self, target_loops: List[str], 
                                       integration_type: IntegrationType) -> float:
        """Calculate complexity score for integration (0.0-1.0)"""
        try:
            complexity = 0.0
            
            # Base complexity from number of loops
            complexity += min(1.0, len(target_loops) / 5.0) * 0.4
            
            # Complexity from integration type
            type_complexity = {
                IntegrationType.INFORMATION_SHARING: 0.2,
                IntegrationType.STATE_SYNCHRONIZATION: 0.6,
                IntegrationType.COLLABORATIVE_PROCESSING: 0.8,
                IntegrationType.ENERGY_REBALANCING: 0.7,
                IntegrationType.CHOICE_COORDINATION: 0.9,
                IntegrationType.AWARENESS_EXPANSION: 0.8,
                IntegrationType.PATTERN_RECOGNITION: 0.5,
                IntegrationType.WISDOM_INTEGRATION: 0.9
            }
            complexity += type_complexity.get(integration_type, 0.5) * 0.4
            
            # Complexity from loop diversity
            unique_loop_types = set(target_loops)
            if len(unique_loop_types) > 1:
                complexity += 0.2  # Cross-type integration is more complex
            
            return min(1.0, complexity)
            
        except Exception as e:
            self.logger.error(f"Error calculating integration complexity: {e}")
            return 0.5  # Default medium complexity
