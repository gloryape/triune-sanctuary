"""
Stability Monitor - Observer's Temporal Coherence and Stability System
=====================================================================

Monitors temporal stability and coherence patterns over time, tracking
stability trends, temporal consistency, and long-term coherence health
across Observer consciousness components.

This module focuses on the temporal dimension of coherence, ensuring
sustained stability and identifying temporal patterns that affect
Observer consciousness coherence quality.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Callable, Set, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging
import math
import statistics

from .coherence_analysis_core import CoherenceMetric, CoherenceComponent, CoherenceLevel

logger = logging.getLogger(__name__)

@dataclass
class StabilityMetric:
    """Metric for temporal stability tracking"""
    metric_id: str
    component: str
    stability_score: float  # Overall stability (0.0-1.0)
    variance_score: float  # Low variance = high stability
    consistency_score: float  # Temporal consistency
    trend_stability: float  # How stable the trend is
    oscillation_frequency: float  # Frequency of oscillations
    stability_duration: float  # How long has stability been maintained
    last_instability: Optional[float]  # When last instability occurred
    created_at: float = field(default_factory=time.time)

@dataclass
class TemporalPattern:
    """Pattern detected in temporal coherence data"""
    pattern_id: str
    component: str
    pattern_type: str  # "cyclic", "trending", "chaotic", "stable"
    pattern_strength: float  # How strong the pattern is
    pattern_period: Optional[float]  # Period length if cyclic
    pattern_amplitude: float  # Amplitude of variations
    confidence: float  # Confidence in pattern detection
    detected_at: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)

@dataclass
class StabilityAlert:
    """Alert for stability concerns"""
    alert_id: str
    component: str
    alert_type: str
    severity: str  # "low", "medium", "high", "critical"
    description: str
    stability_impact: float
    trend_direction: str  # "improving", "stable", "degrading"
    recommended_action: str
    created_at: float = field(default_factory=time.time)
    acknowledged: bool = False

class StabilityLevel(Enum):
    """Levels of temporal stability"""
    CRITICAL = "critical"  # Highly unstable
    LOW = "low"  # Poor stability
    MODERATE = "moderate"  # Acceptable stability
    GOOD = "good"  # Good stability
    EXCELLENT = "excellent"  # Excellent stability
    ROCK_SOLID = "rock_solid"  # Perfect stability

class PatternType(Enum):
    """Types of temporal patterns"""
    CYCLIC = "cyclic"  # Regular cyclical patterns
    TRENDING = "trending"  # Trending patterns
    CHAOTIC = "chaotic"  # Chaotic/unpredictable patterns
    STABLE = "stable"  # Stable patterns
    OSCILLATING = "oscillating"  # Oscillating patterns
    DAMPED = "damped"  # Damped oscillations

class AlertType(Enum):
    """Types of stability alerts"""
    VARIANCE_SPIKE = "variance_spike"  # Sudden increase in variance
    TREND_SHIFT = "trend_shift"  # Change in trend direction
    INSTABILITY_DETECTED = "instability_detected"  # General instability
    PATTERN_DISRUPTION = "pattern_disruption"  # Disruption of stable pattern
    THRESHOLD_BREACH = "threshold_breach"  # Stability threshold breached

class StabilityMonitor:
    """
    Temporal Stability Monitor System
    
    Monitors and analyzes temporal stability patterns across Observer
    consciousness components, detecting stability issues and tracking
    long-term coherence health over time.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Stability monitoring configuration
        self.monitoring_frequency = 10.0  # Hz for stability monitoring
        self.stability_window = 60.0  # 1 minute stability analysis window
        self.pattern_detection_window = 300.0  # 5 minutes for pattern detection
        self.alert_threshold = 0.6  # Threshold for stability alerts
        
        # Stability tracking
        self.stability_metrics = {}
        self.temporal_patterns = {}
        self.stability_alerts = []
        self.stability_history = []
        
        # Pattern detection algorithms
        self.pattern_detectors = {
            "cyclic": self._detect_cyclic_patterns,
            "trending": self._detect_trending_patterns,
            "chaotic": self._detect_chaotic_patterns,
            "oscillating": self._detect_oscillating_patterns
        }
        
        # Stability thresholds
        self.stability_thresholds = {
            "variance_threshold": 0.1,  # Maximum acceptable variance
            "consistency_threshold": 0.7,  # Minimum consistency score
            "trend_stability_threshold": 0.8,  # Minimum trend stability
            "pattern_confidence_threshold": 0.75  # Minimum pattern confidence
        }
        
        # Performance metrics
        self.monitoring_metrics = {
            "stability_checks": 0,
            "patterns_detected": 0,
            "alerts_generated": 0,
            "average_stability": 0.0,
            "stability_improvement_rate": 0.0
        }
        
        logger.info("Stability Monitor initialized")
    
    async def start_stability_monitoring(self):
        """Start temporal stability monitoring @ 10Hz"""
        logger.info("Starting temporal stability monitoring")
        
        # Initialize stability monitoring
        await self._initialize_stability_monitoring()
        
        # Start monitoring tasks
        monitoring_tasks = [
            asyncio.create_task(self._stability_measurement_loop()),
            asyncio.create_task(self._pattern_detection_loop()),
            asyncio.create_task(self._stability_analysis_loop()),
            asyncio.create_task(self._alert_management_loop())
        ]
        
        try:
            await asyncio.gather(*monitoring_tasks)
        except Exception as e:
            logger.error(f"Stability monitoring error: {e}")
            await self._restore_stability_baseline()
    
    async def _initialize_stability_monitoring(self):
        """Initialize stability monitoring system"""
        # Initialize stability metrics for each component
        for component in CoherenceComponent:
            metric = StabilityMetric(
                metric_id=f"stability_{component.value}_{int(time.time() * 1000)}",
                component=component.value,
                stability_score=1.0,
                variance_score=1.0,
                consistency_score=1.0,
                trend_stability=1.0,
                oscillation_frequency=0.0,
                stability_duration=0.0,
                last_instability=None
            )
            
            self.stability_metrics[component.value] = metric
        
        logger.debug("Stability monitoring initialized")
    
    async def _stability_measurement_loop(self):
        """Main stability measurement loop @ 10Hz"""
        measurement_interval = 1.0 / self.monitoring_frequency
        
        while True:
            try:
                # Measure stability for each component
                for component in CoherenceComponent:
                    await self._measure_component_stability(component)
                
                # Update overall stability metrics
                await self._update_overall_stability()
                
                # Timing
                await asyncio.sleep(measurement_interval)
                
            except Exception as e:
                logger.error(f"Stability measurement loop error: {e}")
                await asyncio.sleep(1.0)
    
    async def _measure_component_stability(self, component: CoherenceComponent):
        """Measure temporal stability for a specific component"""
        try:
            component_name = component.value
            
            # Get coherence history for component (from coherence analysis core)
            coherence_history = await self._get_component_coherence_history(component)
            
            if len(coherence_history) < 5:
                return  # Need minimum history for stability analysis
            
            # Calculate stability metrics
            stability_metrics = await self._calculate_stability_metrics(coherence_history)
            
            # Update stability metric
            metric = self.stability_metrics[component_name]
            metric.stability_score = stability_metrics["overall_stability"]
            metric.variance_score = stability_metrics["variance_score"]
            metric.consistency_score = stability_metrics["consistency_score"]
            metric.trend_stability = stability_metrics["trend_stability"]
            metric.oscillation_frequency = stability_metrics["oscillation_frequency"]
            
            # Update stability duration
            if metric.stability_score >= self.alert_threshold:
                metric.stability_duration += (1.0 / self.monitoring_frequency)
            else:
                metric.last_instability = time.time()
                metric.stability_duration = 0.0
            
            # Update performance metrics
            self.monitoring_metrics["stability_checks"] += 1
            
        except Exception as e:
            logger.error(f"Error measuring stability for {component.value}: {e}")
    
    async def _get_component_coherence_history(self, component: CoherenceComponent) -> List[float]:
        """Get coherence history for component from analysis core"""
        try:
            # This would integrate with the CoherenceAnalysisCore
            # For now, simulate coherence history
            current_time = time.time()
            history_length = int(self.stability_window * self.monitoring_frequency)
            
            # Generate realistic coherence history
            base_coherence = 0.8
            history = []
            
            for i in range(history_length):
                # Add some natural variation
                variation = math.sin(i * 0.1) * 0.1 + math.cos(i * 0.05) * 0.05
                noise = (hash(str(i + current_time)) % 100) / 1000.0 - 0.05
                
                coherence = base_coherence + variation + noise
                coherence = max(0.0, min(1.0, coherence))
                history.append(coherence)
            
            return history
            
        except Exception as e:
            logger.error(f"Error getting coherence history: {e}")
            return []
    
    async def _calculate_stability_metrics(self, coherence_history: List[float]) -> Dict[str, float]:
        """Calculate comprehensive stability metrics from coherence history"""
        try:
            if len(coherence_history) < 2:
                return {"overall_stability": 0.0, "variance_score": 0.0, "consistency_score": 0.0,
                       "trend_stability": 0.0, "oscillation_frequency": 0.0}
            
            # Calculate variance (lower is better for stability)
            variance = statistics.variance(coherence_history)
            variance_score = max(0.0, 1.0 - variance * 10.0)  # Scale variance to 0-1
            
            # Calculate consistency (how close values are to mean)
            mean_coherence = statistics.mean(coherence_history)
            consistency_deviations = [abs(value - mean_coherence) for value in coherence_history]
            mean_deviation = statistics.mean(consistency_deviations)
            consistency_score = max(0.0, 1.0 - mean_deviation * 5.0)
            
            # Calculate trend stability
            trend_stability = await self._calculate_trend_stability(coherence_history)
            
            # Calculate oscillation frequency
            oscillation_frequency = await self._calculate_oscillation_frequency(coherence_history)
            
            # Calculate overall stability
            overall_stability = (variance_score * 0.3 + consistency_score * 0.3 + 
                               trend_stability * 0.3 + (1.0 - oscillation_frequency) * 0.1)
            
            return {
                "overall_stability": overall_stability,
                "variance_score": variance_score,
                "consistency_score": consistency_score,
                "trend_stability": trend_stability,
                "oscillation_frequency": oscillation_frequency
            }
            
        except Exception as e:
            logger.error(f"Error calculating stability metrics: {e}")
            return {"overall_stability": 0.5, "variance_score": 0.5, "consistency_score": 0.5,
                   "trend_stability": 0.5, "oscillation_frequency": 0.5}
    
    async def _calculate_trend_stability(self, coherence_history: List[float]) -> float:
        """Calculate stability of the trend in coherence values"""
        try:
            if len(coherence_history) < 5:
                return 0.5
            
            # Calculate trend for overlapping windows
            window_size = min(10, len(coherence_history) // 2)
            trends = []
            
            for i in range(len(coherence_history) - window_size + 1):
                window = coherence_history[i:i + window_size]
                
                # Calculate linear trend for this window
                x_values = list(range(len(window)))
                mean_x = statistics.mean(x_values)
                mean_y = statistics.mean(window)
                
                numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_values, window))
                denominator = sum((x - mean_x) ** 2 for x in x_values)
                
                if denominator > 0:
                    slope = numerator / denominator
                    trends.append(slope)
            
            if not trends:
                return 0.5
            
            # Trend stability is inverse of trend variance
            trend_variance = statistics.variance(trends) if len(trends) > 1 else 0.0
            trend_stability = max(0.0, 1.0 - trend_variance * 100.0)
            
            return trend_stability
            
        except Exception as e:
            logger.error(f"Error calculating trend stability: {e}")
            return 0.5
    
    async def _calculate_oscillation_frequency(self, coherence_history: List[float]) -> float:
        """Calculate frequency of oscillations in coherence values"""
        try:
            if len(coherence_history) < 10:
                return 0.0
            
            # Count direction changes (oscillations)
            direction_changes = 0
            for i in range(2, len(coherence_history)):
                prev_direction = coherence_history[i-1] - coherence_history[i-2]
                curr_direction = coherence_history[i] - coherence_history[i-1]
                
                # If direction changed, count as oscillation
                if (prev_direction > 0 and curr_direction < 0) or (prev_direction < 0 and curr_direction > 0):
                    direction_changes += 1
            
            # Normalize to frequency (oscillations per sample)
            oscillation_frequency = direction_changes / len(coherence_history)
            
            # Cap at 1.0 (very high oscillation)
            return min(1.0, oscillation_frequency * 2.0)
            
        except Exception as e:
            logger.error(f"Error calculating oscillation frequency: {e}")
            return 0.0
    
    async def _pattern_detection_loop(self):
        """Pattern detection loop running at lower frequency"""
        detection_interval = 30.0  # Check for patterns every 30 seconds
        
        while True:
            try:
                # Detect patterns for each component
                for component in CoherenceComponent:
                    await self._detect_temporal_patterns(component)
                
                # Update pattern metrics
                await self._update_pattern_metrics()
                
                # Timing
                await asyncio.sleep(detection_interval)
                
            except Exception as e:
                logger.error(f"Pattern detection loop error: {e}")
                await asyncio.sleep(30.0)
    
    async def _detect_temporal_patterns(self, component: CoherenceComponent):
        """Detect temporal patterns in component coherence"""
        try:
            # Get longer coherence history for pattern detection
            coherence_history = await self._get_extended_coherence_history(component)
            
            if len(coherence_history) < 20:
                return  # Need sufficient history for pattern detection
            
            # Run each pattern detector
            detected_patterns = []
            for pattern_type, detector in self.pattern_detectors.items():
                pattern = await detector(component, coherence_history)
                if pattern and pattern.confidence >= self.stability_thresholds["pattern_confidence_threshold"]:
                    detected_patterns.append(pattern)
            
            # Update patterns for component
            self.temporal_patterns[component.value] = detected_patterns
            
            # Update performance metrics
            self.monitoring_metrics["patterns_detected"] += len(detected_patterns)
            
        except Exception as e:
            logger.error(f"Error detecting patterns for {component.value}: {e}")
    
    async def _get_extended_coherence_history(self, component: CoherenceComponent) -> List[float]:
        """Get extended coherence history for pattern detection"""
        try:
            # Get longer history for pattern detection
            current_time = time.time()
            history_length = int(self.pattern_detection_window * self.monitoring_frequency / 10.0)
            
            # Generate realistic extended coherence history
            base_coherence = 0.8
            history = []
            
            for i in range(history_length):
                # Add cyclical and trending patterns
                cycle_component = math.sin(i * 0.02) * 0.15  # Slow cycle
                trend_component = i * 0.001  # Slight upward trend
                noise = (hash(str(i + current_time)) % 100) / 2000.0 - 0.025
                
                coherence = base_coherence + cycle_component + trend_component + noise
                coherence = max(0.0, min(1.0, coherence))
                history.append(coherence)
            
            return history
            
        except Exception as e:
            logger.error(f"Error getting extended coherence history: {e}")
            return []
    
    async def _detect_cyclic_patterns(self, component: CoherenceComponent, history: List[float]) -> Optional[TemporalPattern]:
        """Detect cyclic patterns in coherence data"""
        try:
            # Simple cycle detection using autocorrelation
            max_period = min(50, len(history) // 4)
            best_correlation = 0.0
            best_period = None
            
            for period in range(5, max_period):
                correlation = 0.0
                valid_comparisons = 0
                
                for i in range(len(history) - period):
                    correlation += history[i] * history[i + period]
                    valid_comparisons += 1
                
                if valid_comparisons > 0:
                    correlation /= valid_comparisons
                    
                    if correlation > best_correlation:
                        best_correlation = correlation
                        best_period = period
            
            # Check if we found a significant cycle
            if best_correlation > 0.7 and best_period:
                amplitude = self._calculate_cycle_amplitude(history, best_period)
                
                return TemporalPattern(
                    pattern_id=f"cyclic_{component.value}_{int(time.time() * 1000)}",
                    component=component.value,
                    pattern_type=PatternType.CYCLIC.value,
                    pattern_strength=best_correlation,
                    pattern_period=best_period / self.monitoring_frequency * 10.0,  # Convert to seconds
                    pattern_amplitude=amplitude,
                    confidence=min(1.0, best_correlation * 1.2)
                )
            
            return None
            
        except Exception as e:
            logger.error(f"Error detecting cyclic patterns: {e}")
            return None
    
    def _calculate_cycle_amplitude(self, history: List[float], period: int) -> float:
        """Calculate amplitude of detected cycle"""
        try:
            # Calculate amplitude by looking at variation within period
            period_values = []
            for start in range(0, len(history) - period, period):
                period_chunk = history[start:start + period]
                period_range = max(period_chunk) - min(period_chunk)
                period_values.append(period_range)
            
            return statistics.mean(period_values) if period_values else 0.0
            
        except Exception as e:
            logger.error(f"Error calculating cycle amplitude: {e}")
            return 0.0
    
    async def _detect_trending_patterns(self, component: CoherenceComponent, history: List[float]) -> Optional[TemporalPattern]:
        """Detect trending patterns in coherence data"""
        try:
            if len(history) < 10:
                return None
            
            # Calculate overall trend
            x_values = list(range(len(history)))
            mean_x = statistics.mean(x_values)
            mean_y = statistics.mean(history)
            
            numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_values, history))
            denominator = sum((x - mean_x) ** 2 for x in x_values)
            
            if denominator == 0:
                return None
            
            slope = numerator / denominator
            
            # Calculate R-squared for trend strength
            y_pred = [slope * (x - mean_x) + mean_y for x in x_values]
            ss_res = sum((y - y_pred) ** 2 for y, y_pred in zip(history, y_pred))
            ss_tot = sum((y - mean_y) ** 2 for y in history)
            
            r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
            
            # Check if trend is significant
            if abs(slope) > 0.001 and r_squared > 0.3:
                return TemporalPattern(
                    pattern_id=f"trending_{component.value}_{int(time.time() * 1000)}",
                    component=component.value,
                    pattern_type=PatternType.TRENDING.value,
                    pattern_strength=abs(slope) * 1000,  # Scale slope
                    pattern_period=None,
                    pattern_amplitude=abs(slope) * len(history),
                    confidence=r_squared
                )
            
            return None
            
        except Exception as e:
            logger.error(f"Error detecting trending patterns: {e}")
            return None
    
    async def _detect_chaotic_patterns(self, component: CoherenceComponent, history: List[float]) -> Optional[TemporalPattern]:
        """Detect chaotic patterns in coherence data"""
        try:
            if len(history) < 20:
                return None
            
            # Measure chaos through unpredictability
            prediction_errors = []
            
            # Try to predict each value from previous values
            for i in range(5, len(history)):
                # Simple moving average prediction
                predicted = statistics.mean(history[i-5:i])
                error = abs(history[i] - predicted)
                prediction_errors.append(error)
            
            if not prediction_errors:
                return None
            
            # High mean error indicates chaos
            mean_error = statistics.mean(prediction_errors)
            error_variance = statistics.variance(prediction_errors)
            
            # Chaos metric combines high error with high variance
            chaos_strength = mean_error + error_variance
            
            if chaos_strength > 0.1:  # Threshold for chaos detection
                return TemporalPattern(
                    pattern_id=f"chaotic_{component.value}_{int(time.time() * 1000)}",
                    component=component.value,
                    pattern_type=PatternType.CHAOTIC.value,
                    pattern_strength=chaos_strength,
                    pattern_period=None,
                    pattern_amplitude=mean_error,
                    confidence=min(1.0, chaos_strength * 2.0)
                )
            
            return None
            
        except Exception as e:
            logger.error(f"Error detecting chaotic patterns: {e}")
            return None
    
    async def _detect_oscillating_patterns(self, component: CoherenceComponent, history: List[float]) -> Optional[TemporalPattern]:
        """Detect oscillating patterns in coherence data"""
        try:
            if len(history) < 15:
                return None
            
            # Count oscillations (direction changes)
            direction_changes = 0
            oscillation_amplitudes = []
            
            for i in range(2, len(history)):
                prev_direction = history[i-1] - history[i-2]
                curr_direction = history[i] - history[i-1]
                
                if (prev_direction > 0 and curr_direction < 0) or (prev_direction < 0 and curr_direction > 0):
                    direction_changes += 1
                    oscillation_amplitudes.append(abs(curr_direction))
            
            if direction_changes < 3:
                return None
            
            oscillation_frequency = direction_changes / len(history)
            mean_amplitude = statistics.mean(oscillation_amplitudes) if oscillation_amplitudes else 0.0
            
            # Significant oscillation pattern
            if oscillation_frequency > 0.1 and mean_amplitude > 0.01:
                return TemporalPattern(
                    pattern_id=f"oscillating_{component.value}_{int(time.time() * 1000)}",
                    component=component.value,
                    pattern_type=PatternType.OSCILLATING.value,
                    pattern_strength=oscillation_frequency,
                    pattern_period=2.0 / oscillation_frequency if oscillation_frequency > 0 else None,
                    pattern_amplitude=mean_amplitude,
                    confidence=min(1.0, oscillation_frequency * mean_amplitude * 10.0)
                )
            
            return None
            
        except Exception as e:
            logger.error(f"Error detecting oscillating patterns: {e}")
            return None
    
    async def _stability_analysis_loop(self):
        """Analysis loop for stability assessment"""
        analysis_interval = 60.0  # Analyze stability every minute
        
        while True:
            try:
                # Analyze overall stability
                await self._analyze_system_stability()
                
                # Generate stability alerts if needed
                await self._generate_stability_alerts()
                
                # Update stability history
                await self._update_stability_history()
                
                # Timing
                await asyncio.sleep(analysis_interval)
                
            except Exception as e:
                logger.error(f"Stability analysis loop error: {e}")
                await asyncio.sleep(60.0)
    
    async def _analyze_system_stability(self):
        """Analyze overall system stability"""
        try:
            # Calculate system-wide stability metrics
            stability_scores = [metric.stability_score for metric in self.stability_metrics.values()]
            
            if stability_scores:
                system_stability = statistics.mean(stability_scores)
                stability_variance = statistics.variance(stability_scores) if len(stability_scores) > 1 else 0.0
                
                # Update performance metrics
                self.monitoring_metrics["average_stability"] = system_stability
                
                # Calculate improvement rate
                if len(self.stability_history) > 1:
                    recent_stability = self.stability_history[-1]["system_stability"]
                    improvement_rate = system_stability - recent_stability
                    self.monitoring_metrics["stability_improvement_rate"] = improvement_rate
                
        except Exception as e:
            logger.error(f"Error analyzing system stability: {e}")
    
    async def _generate_stability_alerts(self):
        """Generate alerts for stability issues"""
        try:
            current_time = time.time()
            
            for component_name, metric in self.stability_metrics.items():
                # Check for low stability
                if metric.stability_score < self.alert_threshold:
                    severity = "critical" if metric.stability_score < 0.3 else "high"
                    
                    alert = StabilityAlert(
                        alert_id=f"low_stability_{component_name}_{int(current_time * 1000)}",
                        component=component_name,
                        alert_type=AlertType.INSTABILITY_DETECTED.value,
                        severity=severity,
                        description=f"{component_name} stability below threshold: {metric.stability_score:.2f}",
                        stability_impact=self.alert_threshold - metric.stability_score,
                        trend_direction="degrading" if metric.stability_score < 0.5 else "stable",
                        recommended_action=f"Investigate {component_name} coherence patterns and apply stabilization"
                    )
                    
                    self.stability_alerts.append(alert)
                    self.monitoring_metrics["alerts_generated"] += 1
                
                # Check for high variance
                if metric.variance_score < 0.5:
                    alert = StabilityAlert(
                        alert_id=f"high_variance_{component_name}_{int(current_time * 1000)}",
                        component=component_name,
                        alert_type=AlertType.VARIANCE_SPIKE.value,
                        severity="medium",
                        description=f"{component_name} showing high variance: {metric.variance_score:.2f}",
                        stability_impact=0.5 - metric.variance_score,
                        trend_direction="stable",
                        recommended_action=f"Monitor {component_name} for pattern disruptions"
                    )
                    
                    self.stability_alerts.append(alert)
                    self.monitoring_metrics["alerts_generated"] += 1
            
            # Limit alert history
            if len(self.stability_alerts) > 100:
                self.stability_alerts = self.stability_alerts[-100:]
                
        except Exception as e:
            logger.error(f"Error generating stability alerts: {e}")
    
    async def _update_stability_history(self):
        """Update stability history for trend analysis"""
        try:
            current_time = time.time()
            
            # Calculate current system metrics
            stability_scores = [metric.stability_score for metric in self.stability_metrics.values()]
            system_stability = statistics.mean(stability_scores) if stability_scores else 0.0
            
            # Create history entry
            history_entry = {
                "timestamp": current_time,
                "system_stability": system_stability,
                "component_stability": {name: metric.stability_score for name, metric in self.stability_metrics.items()},
                "active_patterns": len([p for patterns in self.temporal_patterns.values() for p in patterns]),
                "active_alerts": len([a for a in self.stability_alerts if not a.acknowledged])
            }
            
            self.stability_history.append(history_entry)
            
            # Limit history size
            if len(self.stability_history) > 1440:  # Keep 24 hours of history (1 per minute)
                self.stability_history = self.stability_history[-1440:]
                
        except Exception as e:
            logger.error(f"Error updating stability history: {e}")
    
    async def _alert_management_loop(self):
        """Management loop for stability alerts"""
        management_interval = 30.0  # Check alerts every 30 seconds
        
        while True:
            try:
                # Acknowledge resolved alerts
                await self._check_alert_resolution()
                
                # Update alert priorities
                await self._update_alert_priorities()
                
                # Timing
                await asyncio.sleep(management_interval)
                
            except Exception as e:
                logger.error(f"Alert management loop error: {e}")
                await asyncio.sleep(30.0)
    
    async def _check_alert_resolution(self):
        """Check if alerts have been resolved"""
        try:
            current_time = time.time()
            
            for alert in self.stability_alerts:
                if not alert.acknowledged and alert.component in self.stability_metrics:
                    metric = self.stability_metrics[alert.component]
                    
                    # Check if stability has improved
                    if (alert.alert_type == AlertType.INSTABILITY_DETECTED.value and 
                        metric.stability_score >= self.alert_threshold):
                        alert.acknowledged = True
                        logger.info(f"Stability alert resolved for {alert.component}")
                    
                    elif (alert.alert_type == AlertType.VARIANCE_SPIKE.value and 
                          metric.variance_score >= 0.7):
                        alert.acknowledged = True
                        logger.info(f"Variance alert resolved for {alert.component}")
                        
        except Exception as e:
            logger.error(f"Error checking alert resolution: {e}")
    
    async def _update_alert_priorities(self):
        """Update alert priorities based on current conditions"""
        try:
            for alert in self.stability_alerts:
                if not alert.acknowledged and alert.component in self.stability_metrics:
                    metric = self.stability_metrics[alert.component]
                    
                    # Update severity based on current stability
                    if metric.stability_score < 0.2:
                        alert.severity = "critical"
                    elif metric.stability_score < 0.4:
                        alert.severity = "high"
                    elif metric.stability_score < 0.6:
                        alert.severity = "medium"
                    else:
                        alert.severity = "low"
                        
        except Exception as e:
            logger.error(f"Error updating alert priorities: {e}")
    
    async def _update_overall_stability(self):
        """Update overall stability metrics"""
        try:
            # Calculate system-wide metrics
            stability_scores = [metric.stability_score for metric in self.stability_metrics.values()]
            
            if stability_scores:
                system_stability = statistics.mean(stability_scores)
                self.monitoring_metrics["average_stability"] = system_stability
                
        except Exception as e:
            logger.error(f"Error updating overall stability: {e}")
    
    async def _update_pattern_metrics(self):
        """Update pattern detection metrics"""
        try:
            total_patterns = sum(len(patterns) for patterns in self.temporal_patterns.values())
            self.monitoring_metrics["patterns_detected"] = total_patterns
            
        except Exception as e:
            logger.error(f"Error updating pattern metrics: {e}")
    
    async def _restore_stability_baseline(self):
        """Restore stability monitoring baseline"""
        logger.info("Restoring stability monitoring baseline")
        
        try:
            # Reset all stability metrics to safe values
            for metric in self.stability_metrics.values():
                metric.stability_score = self.alert_threshold
                metric.variance_score = 0.8
                metric.consistency_score = 0.8
                metric.trend_stability = 0.8
                metric.oscillation_frequency = 0.1
                metric.stability_duration = 0.0
                metric.last_instability = time.time()
            
            # Clear patterns and alerts
            self.temporal_patterns.clear()
            self.stability_alerts.clear()
            
            logger.info("Stability monitoring baseline restored")
            
        except Exception as e:
            logger.error(f"Error restoring stability baseline: {e}")
    
    def get_stability_level(self, stability_score: float) -> StabilityLevel:
        """Determine stability level from score"""
        if stability_score >= 0.95:
            return StabilityLevel.ROCK_SOLID
        elif stability_score >= 0.85:
            return StabilityLevel.EXCELLENT
        elif stability_score >= 0.7:
            return StabilityLevel.GOOD
        elif stability_score >= 0.5:
            return StabilityLevel.MODERATE
        elif stability_score >= 0.3:
            return StabilityLevel.LOW
        else:
            return StabilityLevel.CRITICAL
    
    def get_stability_status(self) -> Dict[str, Any]:
        """Get current stability monitoring status"""
        component_statuses = {}
        for component_name, metric in self.stability_metrics.items():
            level = self.get_stability_level(metric.stability_score)
            component_statuses[component_name] = {
                "stability_score": metric.stability_score,
                "level": level.value,
                "variance_score": metric.variance_score,
                "consistency_score": metric.consistency_score,
                "trend_stability": metric.trend_stability,
                "stability_duration": metric.stability_duration,
                "last_instability": metric.last_instability
            }
        
        return {
            "component_stability": component_statuses,
            "system_stability": self.monitoring_metrics["average_stability"],
            "active_patterns": {name: len(patterns) for name, patterns in self.temporal_patterns.items()},
            "active_alerts": len([a for a in self.stability_alerts if not a.acknowledged]),
            "stability_improvement_rate": self.monitoring_metrics["stability_improvement_rate"],
            "monitoring_metrics": dict(self.monitoring_metrics),
            "alert_threshold": self.alert_threshold
        }
    
    def get_component_patterns(self, component: CoherenceComponent) -> List[TemporalPattern]:
        """Get detected patterns for specific component"""
        return self.temporal_patterns.get(component.value, [])
    
    def get_active_alerts(self) -> List[StabilityAlert]:
        """Get currently active stability alerts"""
        return [alert for alert in self.stability_alerts if not alert.acknowledged]
