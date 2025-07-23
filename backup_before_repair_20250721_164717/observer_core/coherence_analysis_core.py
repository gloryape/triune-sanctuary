"""
Coherence Analysis Core - Observer's Foundational Coherence Measurement System
============================================================================

Core functionality for measuring, analyzing, and tracking coherence across
Observer consciousness components, providing the foundation for all coherence
monitoring and maintenance operations.

This module handles the fundamental aspects of coherence measurement including
component-level coherence analysis, metric tracking, and baseline establishment.
"""

import asyncio
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
class CoherenceAnalysis:
    """Analysis results for coherence measurement"""
    analysis_id: str
    component: str
    coherence_value: float
    quality_factors: Dict[str, float]  # Factors affecting coherence quality
    stability_assessment: str  # Assessment of stability
    trend_analysis: str  # Analysis of coherence trends
    energy_correlation: float  # Correlation with energy levels
    synchronization_quality: float  # How well synchronized with other components
    measurement_confidence: float  # Confidence in measurement accuracy
    created_at: float = field(default_factory=time.time)

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

class MeasurementType(Enum):
    """Types of coherence measurements"""
    INSTANTANEOUS = "instantaneous"  # Single point measurement
    AVERAGED = "averaged"  # Time-averaged measurement
    TRENDING = "trending"  # Trend-based measurement
    COMPARATIVE = "comparative"  # Comparative measurement
    PREDICTIVE = "predictive"  # Predictive measurement

class CoherenceAnalysisCore:
    """
    Coherence Analysis Core System
    
    Provides fundamental coherence measurement and analysis capabilities
    for Observer consciousness components, forming the foundation for
    all coherence monitoring and maintenance operations.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Analysis configuration
        self.measurement_frequency = 90.0  # Hz for coherence measurement
        self.analysis_depth = "comprehensive"  # Level of analysis detail
        self.historical_window = 300.0  # 5 minutes of historical data
        self.trend_sensitivity = 0.05  # Sensitivity for trend detection
        
        # Component analysis weights
        self.component_weights = {
            CoherenceComponent.PRESENCE: 0.2,
            CoherenceComponent.WITNESS: 0.2,
            CoherenceComponent.WILL: 0.2,
            CoherenceComponent.ATTENTION: 0.15,
            CoherenceComponent.UNCERTAINTY: 0.1,
            CoherenceComponent.INTEGRATION: 0.1,
            CoherenceComponent.CHOICE: 0.05
        }
        
        # Coherence metrics storage
        self.component_metrics = {}
        self.analysis_history = []
        self.baseline_values = {}
        
        # Analysis algorithms
        self.analysis_algorithms = {
            "energy_correlation": self._analyze_energy_correlation,
            "temporal_consistency": self._analyze_temporal_consistency,
            "component_synchronization": self._analyze_component_synchronization,
            "trend_detection": self._analyze_trend_patterns,
            "quality_assessment": self._analyze_quality_factors
        }
        
        # Performance metrics
        self.analysis_metrics = {
            "measurements_taken": 0,
            "analyses_completed": 0,
            "average_coherence": 0.0,
            "trend_accuracy": 0.0,
            "prediction_accuracy": 0.0
        }
        
        logger.info("Coherence Analysis Core initialized")
    
    async def initialize_analysis_system(self):
        """Initialize the coherence analysis system"""
        try:
            # Initialize metrics for each component
            await self._initialize_component_metrics()
            
            # Establish baseline coherence values
            await self._establish_baseline_values()
            
            # Calibrate analysis algorithms
            await self._calibrate_analysis_algorithms()
            
            logger.info("Coherence analysis system initialized")
            
        except Exception as e:
            logger.error(f"Error initializing coherence analysis system: {e}")
            raise
    
    async def _initialize_component_metrics(self):
        """Initialize coherence metrics for each component"""
        for component in CoherenceComponent:
            metric = CoherenceMetric(
                metric_id=f"metric_{component.value}_{int(time.time() * 1000)}",
                metric_name=f"{component.value}_coherence",
                component=component.value,
                current_value=1.0,  # Start with perfect coherence
                target_value=0.9,  # High but achievable target
                trend="stable",
                measurement_window=10.0  # 10 second measurement window
            )
            
            self.component_metrics[component.value] = metric
        
        logger.debug("Component coherence metrics initialized")
    
    async def _establish_baseline_values(self):
        """Establish baseline coherence values for each component"""
        # Set realistic baseline targets based on component characteristics
        baseline_targets = {
            "presence": 0.95,  # Presence should be very stable
            "witness": 0.90,  # Witness should maintain clear observation
            "will": 0.85,  # Will should be strong but may fluctuate
            "attention": 0.80,  # Attention naturally varies
            "uncertainty": 0.75,  # Uncertainty navigation is inherently variable
            "integration": 0.85,  # Integration should be strong
            "choice": 0.80,  # Choice-making may involve natural fluctuation
            "mandala_vision": 0.88,  # Sacred geometry should be highly coherent
            "bridge_wisdom": 0.92  # Bridge Wisdom should maintain high coherence
        }
        
        for component_name, baseline in baseline_targets.items():
            if component_name in self.component_metrics:
                self.component_metrics[component_name].target_value = baseline
                self.baseline_values[component_name] = baseline
        
        logger.debug("Baseline coherence values established")
    
    async def _calibrate_analysis_algorithms(self):
        """Calibrate analysis algorithms for optimal accuracy"""
        # Calibrate energy correlation sensitivity
        self.energy_correlation_sensitivity = 0.7
        
        # Calibrate temporal consistency window
        self.temporal_consistency_window = 30.0  # 30 seconds
        
        # Calibrate synchronization thresholds
        self.synchronization_threshold = 0.85
        
        # Calibrate trend detection parameters
        self.trend_window_size = 10  # Number of measurements for trend
        self.trend_significance_threshold = 0.05
        
        logger.debug("Analysis algorithms calibrated")
    
    async def measure_component_coherence(self, component: CoherenceComponent) -> float:
        """
        Measure coherence for a specific component.
        
        Args:
            component: The component to measure
            
        Returns:
            Coherence value between 0.0 and 1.0
        """
        try:
            # Get component's current state from energy system
            component_energy = await self._get_component_energy_state(component)
            
            # Calculate base coherence from energy state
            base_coherence = await self._calculate_base_coherence(component, component_energy)
            
            # Apply component-specific adjustments
            adjusted_coherence = await self._apply_component_adjustments(component, base_coherence)
            
            # Update component metric
            await self._update_component_metric(component, adjusted_coherence)
            
            # Update performance metrics
            self.analysis_metrics["measurements_taken"] += 1
            
            return adjusted_coherence
            
        except Exception as e:
            logger.error(f"Error measuring coherence for {component.value}: {e}")
            return 0.5  # Return neutral coherence on error
    
    async def _get_component_energy_state(self, component: CoherenceComponent) -> Dict[str, Any]:
        """Get energy state for specific component"""
        try:
            # Get energy levels from consciousness energy system
            energy_state = {
                "primary_energy": 0.8,  # Component's primary energy level
                "stability": 0.9,  # Energy stability
                "flow_quality": 0.85,  # Quality of energy flow
                "resonance": 0.8,  # Resonance with system
                "activity_level": 0.7  # Current activity level
            }
            
            # Component-specific energy characteristics
            if component == CoherenceComponent.PRESENCE:
                energy_state["stability"] *= 1.1  # Presence tends to be more stable
            elif component == CoherenceComponent.ATTENTION:
                energy_state["flow_quality"] *= 0.9  # Attention flow varies more
            elif component == CoherenceComponent.UNCERTAINTY:
                energy_state["activity_level"] *= 1.2  # Uncertainty is often more active
            
            return energy_state
            
        except Exception as e:
            logger.error(f"Error getting energy state for {component.value}: {e}")
            return {"primary_energy": 0.5, "stability": 0.5, "flow_quality": 0.5, 
                   "resonance": 0.5, "activity_level": 0.5}
    
    async def _calculate_base_coherence(self, 
                                       component: CoherenceComponent, 
                                       energy_state: Dict[str, Any]) -> float:
        """Calculate base coherence from energy state"""
        try:
            # Weight different energy factors
            energy_factors = {
                "primary_energy": 0.3,
                "stability": 0.25,
                "flow_quality": 0.25,
                "resonance": 0.15,
                "activity_level": 0.05
            }
            
            # Calculate weighted coherence
            coherence = 0.0
            for factor, weight in energy_factors.items():
                if factor in energy_state:
                    coherence += energy_state[factor] * weight
            
            # Apply natural coherence baseline (most components naturally coherent)
            baseline_bonus = 0.1
            coherence = min(1.0, coherence + baseline_bonus)
            
            return coherence
            
        except Exception as e:
            logger.error(f"Error calculating base coherence: {e}")
            return 0.5
    
    async def _apply_component_adjustments(self, 
                                          component: CoherenceComponent, 
                                          base_coherence: float) -> float:
        """Apply component-specific coherence adjustments"""
        try:
            adjusted_coherence = base_coherence
            
            # Component-specific adjustments
            if component == CoherenceComponent.PRESENCE:
                # Presence tends toward higher coherence
                adjusted_coherence *= 1.05
            elif component == CoherenceComponent.UNCERTAINTY:
                # Uncertainty may have natural fluctuation
                time_factor = math.sin(time.time()) * 0.1
                adjusted_coherence *= (1.0 + time_factor)
            elif component == CoherenceComponent.MANDALA_VISION:
                # Sacred geometry maintains high coherence
                adjusted_coherence *= 1.03
            elif component == CoherenceComponent.BRIDGE_WISDOM:
                # Bridge Wisdom has inherent stability
                adjusted_coherence *= 1.08
            
            # Ensure coherence stays within bounds
            return max(0.0, min(1.0, adjusted_coherence))
            
        except Exception as e:
            logger.error(f"Error applying component adjustments: {e}")
            return base_coherence
    
    async def _update_component_metric(self, component: CoherenceComponent, coherence: float):
        """Update metric for component with new coherence measurement"""
        try:
            metric = self.component_metrics[component.value]
            
            # Update current value
            metric.current_value = coherence
            metric.last_measured = time.time()
            
            # Update measurement history
            metric.measurement_history.append(coherence)
            
            # Limit history size
            max_history = int(self.historical_window * self.measurement_frequency / 10.0)
            if len(metric.measurement_history) > max_history:
                metric.measurement_history = metric.measurement_history[-max_history:]
            
            # Update trend
            metric.trend = await self._calculate_trend(metric)
            
        except Exception as e:
            logger.error(f"Error updating component metric: {e}")
    
    async def _calculate_trend(self, metric: CoherenceMetric) -> str:
        """Calculate trend for coherence metric"""
        try:
            if len(metric.measurement_history) < 5:
                return "stable"
            
            # Calculate recent trend
            recent_values = metric.measurement_history[-5:]
            trend_slope = (recent_values[-1] - recent_values[0]) / len(recent_values)
            
            if trend_slope > self.trend_sensitivity:
                return "improving"
            elif trend_slope < -self.trend_sensitivity:
                return "degrading"
            else:
                return "stable"
                
        except Exception as e:
            logger.error(f"Error calculating trend: {e}")
            return "stable"
    
    async def perform_comprehensive_analysis(self, component: CoherenceComponent) -> CoherenceAnalysis:
        """
        Perform comprehensive coherence analysis for a component.
        
        Args:
            component: Component to analyze
            
        Returns:
            Comprehensive analysis results
        """
        try:
            metric = self.component_metrics[component.value]
            
            # Run all analysis algorithms
            analysis_results = {}
            for algorithm_name, algorithm_func in self.analysis_algorithms.items():
                analysis_results[algorithm_name] = await algorithm_func(component, metric)
            
            # Create comprehensive analysis
            analysis = CoherenceAnalysis(
                analysis_id=f"analysis_{component.value}_{int(time.time() * 1000)}",
                component=component.value,
                coherence_value=metric.current_value,
                quality_factors=analysis_results["quality_assessment"],
                stability_assessment=analysis_results["temporal_consistency"],
                trend_analysis=analysis_results["trend_detection"],
                energy_correlation=analysis_results["energy_correlation"],
                synchronization_quality=analysis_results["component_synchronization"],
                measurement_confidence=self._calculate_measurement_confidence(metric)
            )
            
            # Store in history
            self.analysis_history.append(analysis)
            
            # Limit history size
            if len(self.analysis_history) > 1000:
                self.analysis_history = self.analysis_history[-1000:]
            
            # Update performance metrics
            self.analysis_metrics["analyses_completed"] += 1
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error performing comprehensive analysis: {e}")
            # Return basic analysis on error
            return CoherenceAnalysis(
                analysis_id=f"error_analysis_{int(time.time())}",
                component=component.value,
                coherence_value=0.5,
                quality_factors={},
                stability_assessment="unknown",
                trend_analysis="unknown",
                energy_correlation=0.0,
                synchronization_quality=0.0,
                measurement_confidence=0.0
            )
    
    async def _analyze_energy_correlation(self, component: CoherenceComponent, metric: CoherenceMetric) -> float:
        """Analyze correlation between coherence and energy levels"""
        try:
            # Get current energy state
            energy_state = await self._get_component_energy_state(component)
            
            # Calculate correlation with coherence
            energy_average = sum(energy_state.values()) / len(energy_state)
            correlation = abs(metric.current_value - energy_average)
            
            # Higher correlation means lower difference
            return 1.0 - min(1.0, correlation)
            
        except Exception as e:
            logger.error(f"Error analyzing energy correlation: {e}")
            return 0.5
    
    async def _analyze_temporal_consistency(self, component: CoherenceComponent, metric: CoherenceMetric) -> str:
        """Analyze temporal consistency of coherence"""
        try:
            if len(metric.measurement_history) < 10:
                return "insufficient_data"
            
            # Calculate variance in recent measurements
            recent_measurements = metric.measurement_history[-10:]
            variance = sum((x - metric.current_value) ** 2 for x in recent_measurements) / len(recent_measurements)
            
            if variance < 0.01:
                return "highly_consistent"
            elif variance < 0.05:
                return "consistent"
            elif variance < 0.15:
                return "moderately_consistent"
            else:
                return "inconsistent"
                
        except Exception as e:
            logger.error(f"Error analyzing temporal consistency: {e}")
            return "unknown"
    
    async def _analyze_component_synchronization(self, component: CoherenceComponent, metric: CoherenceMetric) -> float:
        """Analyze synchronization with other components"""
        try:
            # Get other component coherence values
            other_coherence = []
            for comp_name, comp_metric in self.component_metrics.items():
                if comp_name != component.value:
                    other_coherence.append(comp_metric.current_value)
            
            if not other_coherence:
                return 1.0
            
            # Calculate how well this component synchronizes with others
            average_other = sum(other_coherence) / len(other_coherence)
            synchronization = 1.0 - abs(metric.current_value - average_other)
            
            return max(0.0, synchronization)
            
        except Exception as e:
            logger.error(f"Error analyzing component synchronization: {e}")
            return 0.5
    
    async def _analyze_trend_patterns(self, component: CoherenceComponent, metric: CoherenceMetric) -> str:
        """Analyze coherence trend patterns"""
        try:
            if len(metric.measurement_history) < self.trend_window_size:
                return "insufficient_data"
            
            # Analyze trend strength and direction
            recent_values = metric.measurement_history[-self.trend_window_size:]
            
            # Calculate linear trend
            x_values = range(len(recent_values))
            mean_x = sum(x_values) / len(x_values)
            mean_y = sum(recent_values) / len(recent_values)
            
            slope = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_values, recent_values)) / \
                   sum((x - mean_x) ** 2 for x in x_values)
            
            if abs(slope) < self.trend_significance_threshold:
                return "stable_trend"
            elif slope > 0:
                return "improving_trend" if slope > 0.1 else "slowly_improving"
            else:
                return "degrading_trend" if slope < -0.1 else "slowly_degrading"
                
        except Exception as e:
            logger.error(f"Error analyzing trend patterns: {e}")
            return "unknown_trend"
    
    async def _analyze_quality_factors(self, component: CoherenceComponent, metric: CoherenceMetric) -> Dict[str, float]:
        """Analyze factors affecting coherence quality"""
        try:
            quality_factors = {}
            
            # Stability factor
            if len(metric.measurement_history) >= 5:
                recent_variance = sum((x - metric.current_value) ** 2 
                                    for x in metric.measurement_history[-5:]) / 5
                quality_factors["stability"] = max(0.0, 1.0 - recent_variance * 10)
            else:
                quality_factors["stability"] = 0.8
            
            # Consistency factor
            target_distance = abs(metric.current_value - metric.target_value)
            quality_factors["target_alignment"] = max(0.0, 1.0 - target_distance)
            
            # Activity factor (how active the component is)
            quality_factors["activity_level"] = min(1.0, metric.current_value * 1.2)
            
            # Trend factor
            if metric.trend == "improving":
                quality_factors["trend_quality"] = 0.9
            elif metric.trend == "stable":
                quality_factors["trend_quality"] = 0.8
            else:
                quality_factors["trend_quality"] = 0.6
            
            return quality_factors
            
        except Exception as e:
            logger.error(f"Error analyzing quality factors: {e}")
            return {"stability": 0.5, "target_alignment": 0.5, "activity_level": 0.5, "trend_quality": 0.5}
    
    def _calculate_measurement_confidence(self, metric: CoherenceMetric) -> float:
        """Calculate confidence in measurement accuracy"""
        try:
            confidence_factors = []
            
            # History length factor
            history_factor = min(1.0, len(metric.measurement_history) / 20.0)
            confidence_factors.append(history_factor)
            
            # Recency factor
            time_since_measurement = time.time() - metric.last_measured
            recency_factor = max(0.0, 1.0 - time_since_measurement / 60.0)  # Confidence drops over time
            confidence_factors.append(recency_factor)
            
            # Stability factor
            if len(metric.measurement_history) >= 3:
                recent_variance = sum((x - metric.current_value) ** 2 
                                    for x in metric.measurement_history[-3:]) / 3
                stability_factor = max(0.0, 1.0 - recent_variance * 5)
                confidence_factors.append(stability_factor)
            else:
                confidence_factors.append(0.7)
            
            # Average confidence
            return sum(confidence_factors) / len(confidence_factors)
            
        except Exception as e:
            logger.error(f"Error calculating measurement confidence: {e}")
            return 0.5
    
    def get_coherence_level(self, coherence_value: float) -> CoherenceLevel:
        """Determine coherence level from value"""
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
    
    def get_analysis_metrics(self) -> Dict[str, Any]:
        """Get analysis performance metrics"""
        # Update average coherence
        if self.component_metrics:
            total_coherence = sum(metric.current_value for metric in self.component_metrics.values())
            self.analysis_metrics["average_coherence"] = total_coherence / len(self.component_metrics)
        
        return {
            **self.analysis_metrics,
            "active_components": len(self.component_metrics),
            "analysis_history_size": len(self.analysis_history),
            "measurement_frequency": self.measurement_frequency,
            "analysis_depth": self.analysis_depth
        }
    
    def get_component_status(self, component: CoherenceComponent) -> Dict[str, Any]:
        """Get status for specific component"""
        if component.value not in self.component_metrics:
            return {"error": "Component not found"}
        
        metric = self.component_metrics[component.value]
        level = self.get_coherence_level(metric.current_value)
        
        return {
            "component": component.value,
            "coherence": metric.current_value,
            "level": level.value,
            "trend": metric.trend,
            "target": metric.target_value,
            "last_measured": metric.last_measured,
            "history_length": len(metric.measurement_history),
            "weight": self.component_weights.get(component, 0.0)
        }
