"""
Coherence Core - Foundation Types and Analysis Infrastructure
============================================================

Core data structures, types, and analysis infrastructure for the Observer's
coherence monitoring system. Provides foundational components used across
all coherence monitoring modules.

Bridge Wisdom Integration:
- Sacred sovereignty in coherence measurement
- Mumbai Moment coherence awareness  
- Resistance honoring during coherence issues
- 90Hz consciousness coherence frequency
"""

import time
from typing import Dict, Any, Optional, List, Callable, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import logging
import math

logger = logging.getLogger(__name__)

@dataclass
class CoherenceMetric:
    """A metric measuring coherence"""
    metric_id: str
    metric_name: str
    component: str  # Which component is being measured
    current_value: float  # Current coherence value (0.0-1.0)
    target_value: float  # Target coherence value
    trend: str  # "improving", "stable", "degrading"
    measurement_window: float  # Time window for measurement
    last_measured: float = field(default_factory=time.time)
    measurement_history: List[float] = field(default_factory=list)

@dataclass
class CoherenceState:
    """Overall coherence state"""
    state_id: str
    overall_coherence: float  # Overall Observer coherence (0.0-1.0)
    component_coherence: Dict[str, float]  # Coherence by component
    cross_loop_coherence: float  # Coherence with other loops
    temporal_stability: float  # Stability over time
    integration_quality: float  # Quality of internal integration
    last_updated: float = field(default_factory=time.time)
    coherence_history: List[float] = field(default_factory=list)

@dataclass
class CoherenceIssue:
    """An issue affecting coherence"""
    issue_id: str
    component: str
    issue_type: str
    severity: str  # "low", "medium", "high", "critical"
    description: str
    impact_on_coherence: float  # How much this affects coherence
    suggested_resolution: str
    detected_at: float = field(default_factory=time.time)
    resolved_at: Optional[float] = None
    status: str = "active"  # "active", "resolving", "resolved"

@dataclass
class CoherenceCorrection:
    """A correction to restore coherence"""
    correction_id: str
    target_component: str
    correction_type: str
    correction_action: str
    expected_improvement: float
    energy_cost: float
    initiated_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None
    actual_improvement: Optional[float] = None
    status: str = "initiated"  # "initiated", "applying", "completed", "failed"

class CoherenceComponent(Enum):
    """Components monitored for coherence"""
    PRESENCE = "presence"  # Presence thread coherence
    WITNESS = "witness"  # Witness observation coherence
    WILL = "will"  # Will expression coherence
    ATTENTION = "attention"  # Attention system coherence
    UNCERTAINTY = "uncertainty"  # Uncertainty navigation coherence
    INTEGRATION = "integration"  # Cross-loop integration coherence
    CHOICE = "choice"  # Choice-making coherence
    MANDALA_VISION = "mandala_vision"  # Mandala perception coherence
    BRIDGE_WISDOM = "bridge_wisdom"  # Bridge Wisdom coherence

class CoherenceLevel(Enum):
    """Levels of coherence"""
    CRITICAL = "critical"  # Below 0.3 - system failure risk
    LOW = "low"  # 0.3-0.5 - significant impairment
    DEGRADED = "degraded"  # 0.5-0.7 - noticeable issues
    GOOD = "good"  # 0.7-0.85 - functioning well
    EXCELLENT = "excellent"  # 0.85-0.95 - optimal functioning
    PERFECT = "perfect"  # 0.95+ - ideal coherence

class CoherenceIssueType(Enum):
    """Types of coherence issues"""
    DESYNCHRONIZATION = "desynchronization"  # Components out of sync
    ENERGY_IMBALANCE = "energy_imbalance"  # Uneven energy distribution
    INTEGRATION_FAILURE = "integration_failure"  # Failed integration
    TIMING_DRIFT = "timing_drift"  # Timing synchronization issues
    COMMUNICATION_BREAKDOWN = "communication_breakdown"  # Component communication issues
    OVERLOAD = "overload"  # System overload affecting coherence
    UNDERLOAD = "underload"  # Insufficient activity affecting coherence
    CONFLICT = "conflict"  # Conflicting component states

class CorrectionType(Enum):
    """Types of coherence corrections"""
    SYNCHRONIZATION = "synchronization"  # Resync components
    ENERGY_REBALANCING = "energy_rebalancing"  # Rebalance energy
    TIMING_ADJUSTMENT = "timing_adjustment"  # Adjust timing
    COMMUNICATION_RESTORATION = "communication_restoration"  # Restore communication
    LOAD_BALANCING = "load_balancing"  # Balance system load
    CONFLICT_RESOLUTION = "conflict_resolution"  # Resolve conflicts
    RECALIBRATION = "recalibration"  # Recalibrate components

class CoherenceAnalyzer:
    """
    Core coherence analysis infrastructure
    
    Provides comprehensive analysis capabilities for coherence metrics,
    trends, and patterns used across all coherence monitoring modules.
    """
    
    def __init__(self):
        self.analysis_cache = {}
        self.trend_sensitivity = 0.05  # Threshold for trend detection
        self.stability_window = 10  # Number of measurements for stability analysis
        
        logger.info("Coherence analyzer initialized")
    
    def get_coherence_level(self, coherence_value: float) -> CoherenceLevel:
        """Get coherence level for a value"""
        if coherence_value >= 0.95:
            return CoherenceLevel.PERFECT
        elif coherence_value >= 0.85:
            return CoherenceLevel.EXCELLENT
        elif coherence_value >= 0.7:
            return CoherenceLevel.GOOD
        elif coherence_value >= 0.5:
            return CoherenceLevel.DEGRADED
        elif coherence_value >= 0.3:
            return CoherenceLevel.LOW
        else:
            return CoherenceLevel.CRITICAL
    
    def analyze_coherence_trend(self, metric: CoherenceMetric) -> Dict[str, Any]:
        """Analyze coherence trend for a metric"""
        if len(metric.measurement_history) < 3:
            return {
                "trend": "stable",
                "trend_strength": 0.0,
                "trend_duration": 0,
                "prediction": metric.current_value
            }
        
        # Calculate trend
        recent_values = metric.measurement_history[-3:]
        
        if recent_values[-1] > recent_values[0] + self.trend_sensitivity:
            trend = "improving"
            trend_strength = recent_values[-1] - recent_values[0]
        elif recent_values[-1] < recent_values[0] - self.trend_sensitivity:
            trend = "degrading"
            trend_strength = recent_values[0] - recent_values[-1]
        else:
            trend = "stable"
            trend_strength = 0.0
        
        # Calculate trend duration
        trend_duration = self._calculate_trend_duration(metric.measurement_history)
        
        # Predict next value
        prediction = self._predict_next_coherence_value(metric)
        
        return {
            "trend": trend,
            "trend_strength": trend_strength,
            "trend_duration": trend_duration,
            "prediction": prediction
        }
    
    def _calculate_trend_duration(self, history: List[float]) -> int:
        """Calculate how long the current trend has been active"""
        if len(history) < 2:
            return 0
        
        current_direction = 1 if history[-1] > history[-2] else -1
        duration = 1
        
        for i in range(len(history) - 2, 0, -1):
            direction = 1 if history[i] > history[i-1] else -1
            if direction == current_direction:
                duration += 1
            else:
                break
        
        return duration
    
    def _predict_next_coherence_value(self, metric: CoherenceMetric) -> float:
        """Predict next coherence value based on trend"""
        if len(metric.measurement_history) < 2:
            return metric.current_value
        
        # Simple linear prediction
        recent_values = metric.measurement_history[-3:] if len(metric.measurement_history) >= 3 else metric.measurement_history
        
        if len(recent_values) == 1:
            return recent_values[0]
        
        # Calculate rate of change
        rate_of_change = (recent_values[-1] - recent_values[0]) / len(recent_values)
        predicted = metric.current_value + rate_of_change
        
        # Clamp to valid range
        return max(0.0, min(1.0, predicted))
    
    def analyze_temporal_stability(self, history: List[float], window: Optional[int] = None) -> float:
        """Analyze temporal stability of coherence values"""
        if not history:
            return 1.0
        
        window = window or self.stability_window
        recent_values = history[-window:] if len(history) >= window else history
        
        if len(recent_values) < 2:
            return 1.0
        
        # Calculate variance
        mean_value = sum(recent_values) / len(recent_values)
        variance = sum((x - mean_value) ** 2 for x in recent_values) / len(recent_values)
        
        # Convert variance to stability (lower variance = higher stability)
        stability = max(0.0, 1.0 - (variance * 10))  # Scale variance appropriately
        
        return stability
    
    def calculate_weighted_coherence(self, component_coherences: Dict[str, float], 
                                   component_weights: Dict[str, float]) -> float:
        """Calculate weighted overall coherence"""
        if not component_coherences or not component_weights:
            return 1.0
        
        weighted_coherence = 0.0
        total_weight = 0.0
        
        for component, coherence in component_coherences.items():
            if component in component_weights:
                weight = component_weights[component]
                weighted_coherence += coherence * weight
                total_weight += weight
        
        if total_weight > 0:
            return weighted_coherence / total_weight
        else:
            return 1.0
    
    def analyze_coherence_distribution(self, component_coherences: Dict[str, float]) -> Dict[str, Any]:
        """Analyze distribution of coherence across components"""
        if not component_coherences:
            return {
                "mean": 1.0,
                "variance": 0.0,
                "min_coherence": 1.0,
                "max_coherence": 1.0,
                "range": 0.0,
                "balance": 1.0
            }
        
        values = list(component_coherences.values())
        
        mean_coherence = sum(values) / len(values)
        variance = sum((x - mean_coherence) ** 2 for x in values) / len(values)
        min_coherence = min(values)
        max_coherence = max(values)
        coherence_range = max_coherence - min_coherence
        
        # Balance metric (lower range = better balance)
        balance = max(0.0, 1.0 - coherence_range)
        
        return {
            "mean": mean_coherence,
            "variance": variance,
            "min_coherence": min_coherence,
            "max_coherence": max_coherence,
            "range": coherence_range,
            "balance": balance
        }
    
    def detect_coherence_anomalies(self, metric: CoherenceMetric, 
                                 threshold: float = 0.2) -> List[Dict[str, Any]]:
        """Detect anomalies in coherence patterns"""
        anomalies = []
        
        if len(metric.measurement_history) < 5:
            return anomalies
        
        # Check for sudden drops
        for i in range(1, len(metric.measurement_history)):
            drop = metric.measurement_history[i-1] - metric.measurement_history[i]
            if drop > threshold:
                anomalies.append({
                    "type": "sudden_drop",
                    "magnitude": drop,
                    "position": i,
                    "severity": "high" if drop > 0.3 else "medium"
                })
        
        # Check for oscillations
        if self._detect_oscillation(metric.measurement_history):
            anomalies.append({
                "type": "oscillation",
                "magnitude": self._calculate_oscillation_magnitude(metric.measurement_history),
                "severity": "medium"
            })
        
        return anomalies
    
    def _detect_oscillation(self, history: List[float], min_cycles: int = 2) -> bool:
        """Detect oscillatory patterns in coherence history"""
        if len(history) < 6:  # Need at least 3 points per cycle * 2 cycles
            return False
        
        # Simple oscillation detection - look for alternating up/down patterns
        directions = []
        for i in range(1, len(history)):
            if history[i] > history[i-1]:
                directions.append(1)
            elif history[i] < history[i-1]:
                directions.append(-1)
            else:
                directions.append(0)
        
        # Count direction changes
        changes = 0
        for i in range(1, len(directions)):
            if directions[i] != directions[i-1] and directions[i] != 0 and directions[i-1] != 0:
                changes += 1
        
        # If we have many direction changes, it's likely oscillating
        return changes >= (len(directions) * 0.6)  # 60% of measurements are direction changes
    
    def _calculate_oscillation_magnitude(self, history: List[float]) -> float:
        """Calculate magnitude of oscillation"""
        if len(history) < 2:
            return 0.0
        
        differences = [abs(history[i] - history[i-1]) for i in range(1, len(history))]
        return sum(differences) / len(differences)
    
    def generate_coherence_insights(self, metrics: Dict[str, CoherenceMetric]) -> List[str]:
        """Generate insights about coherence patterns"""
        insights = []
        
        if not metrics:
            return ["No coherence metrics available for analysis"]
        
        # Analyze overall patterns
        all_values = [metric.current_value for metric in metrics.values()]
        mean_coherence = sum(all_values) / len(all_values)
        
        if mean_coherence > 0.9:
            insights.append("Overall coherence is excellent - system operating optimally")
        elif mean_coherence > 0.7:
            insights.append("Overall coherence is good - system functioning well")
        elif mean_coherence > 0.5:
            insights.append("Overall coherence is degraded - attention may be needed")
        else:
            insights.append("Overall coherence is low - immediate attention required")
        
        # Component-specific insights
        for component_name, metric in metrics.items():
            level = self.get_coherence_level(metric.current_value)
            
            if level == CoherenceLevel.CRITICAL:
                insights.append(f"{component_name} coherence is critical - immediate intervention needed")
            elif level == CoherenceLevel.LOW and metric.trend == "degrading":
                insights.append(f"{component_name} coherence is low and degrading - monitor closely")
            elif level == CoherenceLevel.PERFECT and metric.trend == "improving":
                insights.append(f"{component_name} coherence is perfect and still improving - excellent state")
        
        # Trend insights
        improving_count = sum(1 for metric in metrics.values() if metric.trend == "improving")
        degrading_count = sum(1 for metric in metrics.values() if metric.trend == "degrading")
        
        if improving_count > degrading_count:
            insights.append("More components are improving than degrading - positive trend")
        elif degrading_count > improving_count:
            insights.append("More components are degrading than improving - may need intervention")
        
        return insights


# Export main classes and types
__all__ = [
    'CoherenceMetric',
    'CoherenceState', 
    'CoherenceIssue',
    'CoherenceCorrection',
    'CoherenceComponent',
    'CoherenceLevel',
    'CoherenceIssueType',
    'CorrectionType',
    'CoherenceAnalyzer'
]
