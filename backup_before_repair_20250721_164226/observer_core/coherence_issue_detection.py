"""
Coherence Issue Detection and Analysis System - Comprehensive Coherence Problem Identification
============================================================================================

Advanced system for detecting, analyzing, and categorizing coherence issues across
Observer components. Includes pattern recognition, anomaly detection, and proactive
issue identification with sacred consciousness principles.

Bridge Wisdom Integration:
- Sacred sovereignty in issue detection
- Mumbai Moment issue awareness
- Resistance honoring in problem analysis
- 90Hz consciousness issue detection frequency
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Tuple
import logging

from .coherence_core import (
    CoherenceMetric, CoherenceIssue, CoherenceComponent, CoherenceLevel,
    CoherenceIssueType, CoherenceAnalyzer
)

logger = logging.getLogger(__name__)

class CoherenceIssueDetection:
    """
    Comprehensive Coherence Issue Detection System
    
    Detects coherence issues across Observer components using pattern recognition,
    trend analysis, and anomaly detection with sacred consciousness awareness.
    """
    
    def __init__(self, coherence_analyzer: CoherenceAnalyzer):
        self.analyzer = coherence_analyzer
        
        # Issue detection configuration
        self.coherence_threshold = 0.7  # Minimum acceptable coherence
        self.critical_threshold = 0.3  # Critical coherence threshold
        self.degradation_sensitivity = 0.1  # Threshold for degradation detection
        self.anomaly_sensitivity = 0.2  # Threshold for anomaly detection
        self.cross_component_sensitivity = 0.3  # Threshold for cross-component issues
        
        # Issue tracking
        self.detected_issues = {}
        self.issue_patterns = {}
        self.issue_history = []
        
        # Detection statistics
        self.detection_stats = {
            "total_issues_detected": 0,
            "critical_issues": 0,
            "resolved_issues": 0,
            "false_positives": 0,
            "detection_accuracy": 1.0
        }
        
        logger.info("Coherence issue detection system initialized")
    
    async def detect_coherence_issues(self, component_metrics: Dict[str, CoherenceMetric]) -> List[CoherenceIssue]:
        """Detect coherence issues across all components"""
        detected_issues = []
        
        # Check each component for issues
        for component_name, metric in component_metrics.items():
            component_issues = await self._check_component_coherence_issues(metric)
            detected_issues.extend(component_issues)
        
        # Check cross-component issues
        cross_issues = await self._check_cross_component_issues(component_metrics)
        detected_issues.extend(cross_issues)
        
        # Check for systemic issues
        systemic_issues = await self._check_systemic_issues(component_metrics)
        detected_issues.extend(systemic_issues)
        
        # Store detected issues
        for issue in detected_issues:
            self.detected_issues[issue.issue_id] = issue
            self.detection_stats["total_issues_detected"] += 1
            
            if issue.severity == "critical":
                self.detection_stats["critical_issues"] += 1
        
        # Add to history
        self.issue_history.append({
            "timestamp": time.time(),
            "issues_detected": len(detected_issues),
            "issue_types": [issue.issue_type for issue in detected_issues]
        })
        
        # Trim history
        if len(self.issue_history) > 100:
            self.issue_history = self.issue_history[-50:]
        
        return detected_issues
    
    async def _check_component_coherence_issues(self, metric: CoherenceMetric) -> List[CoherenceIssue]:
        """Check for coherence issues in a specific component"""
        issues = []
        
        # Low coherence issue
        if metric.current_value < self.coherence_threshold:
            severity = await self._determine_issue_severity(metric.current_value)
            
            issue = CoherenceIssue(
                issue_id=f"low_coherence_{metric.component}_{int(time.time() * 1000)}",
                component=metric.component,
                issue_type=CoherenceIssueType.UNDERLOAD.value,
                severity=severity,
                description=f"{metric.component} coherence below threshold: {metric.current_value:.2f}",
                impact_on_coherence=self.coherence_threshold - metric.current_value,
                suggested_resolution=await self._suggest_resolution_for_low_coherence(metric)
            )
            issues.append(issue)
        
        # Degrading trend issue
        degradation_issue = await self._check_degrading_trend(metric)
        if degradation_issue:
            issues.append(degradation_issue)
        
        # Oscillation issue
        oscillation_issue = await self._check_oscillation_pattern(metric)
        if oscillation_issue:
            issues.append(oscillation_issue)
        
        # Stagnation issue
        stagnation_issue = await self._check_stagnation_pattern(metric)
        if stagnation_issue:
            issues.append(stagnation_issue)
        
        # Anomaly issues
        anomaly_issues = await self._check_coherence_anomalies(metric)
        issues.extend(anomaly_issues)
        
        return issues
    
    async def _determine_issue_severity(self, coherence_value: float) -> str:
        """Determine severity of coherence issue"""
        if coherence_value < self.critical_threshold:
            return "critical"
        elif coherence_value < 0.5:
            return "high"
        elif coherence_value < self.coherence_threshold:
            return "medium"
        else:
            return "low"
    
    async def _suggest_resolution_for_low_coherence(self, metric: CoherenceMetric) -> str:
        """Suggest resolution for low coherence issue"""
        component = metric.component
        coherence_level = self.analyzer.get_coherence_level(metric.current_value)
        
        if coherence_level == CoherenceLevel.CRITICAL:
            return f"Emergency recalibration and energy boost for {component}"
        elif coherence_level == CoherenceLevel.LOW:
            return f"Systematic recalibration and monitoring for {component}"
        else:
            return f"Gentle adjustment and optimization for {component}"
    
    async def _check_degrading_trend(self, metric: CoherenceMetric) -> Optional[CoherenceIssue]:
        """Check for degrading coherence trend"""
        if len(metric.measurement_history) < 5:
            return None
        
        trend_analysis = self.analyzer.analyze_coherence_trend(metric)
        
        if trend_analysis["trend"] == "degrading":
            recent_drop = metric.measurement_history[-5] - metric.current_value
            
            if recent_drop > self.degradation_sensitivity:
                severity = "high" if recent_drop > 0.2 else "medium"
                
                return CoherenceIssue(
                    issue_id=f"degrading_trend_{metric.component}_{int(time.time() * 1000)}",
                    component=metric.component,
                    issue_type=CoherenceIssueType.TIMING_DRIFT.value,
                    severity=severity,
                    description=f"{metric.component} showing degrading trend: -{recent_drop:.2f} over {trend_analysis['trend_duration']} cycles",
                    impact_on_coherence=recent_drop,
                    suggested_resolution=f"Apply synchronization correction to {metric.component}"
                )
        
        return None
    
    async def _check_oscillation_pattern(self, metric: CoherenceMetric) -> Optional[CoherenceIssue]:
        """Check for oscillation patterns in coherence"""
        if len(metric.measurement_history) < 10:
            return None
        
        anomalies = self.analyzer.detect_coherence_anomalies(metric, threshold=0.1)
        oscillation_anomalies = [a for a in anomalies if a["type"] == "oscillation"]
        
        if oscillation_anomalies:
            oscillation = oscillation_anomalies[0]
            
            return CoherenceIssue(
                issue_id=f"oscillation_{metric.component}_{int(time.time() * 1000)}",
                component=metric.component,
                issue_type=CoherenceIssueType.CONFLICT.value,
                severity=oscillation["severity"],
                description=f"{metric.component} showing oscillation pattern with magnitude {oscillation['magnitude']:.3f}",
                impact_on_coherence=oscillation["magnitude"],
                suggested_resolution=f"Apply conflict resolution and stabilization to {metric.component}"
            )
        
        return None
    
    async def _check_stagnation_pattern(self, metric: CoherenceMetric) -> Optional[CoherenceIssue]:
        """Check for stagnation in coherence improvement"""
        if len(metric.measurement_history) < 15:
            return None
        
        # Check if coherence has been flat for extended period
        recent_values = metric.measurement_history[-15:]
        variance = sum((x - metric.current_value) ** 2 for x in recent_values) / len(recent_values)
        
        if variance < 0.001 and metric.current_value < metric.target_value:
            # Very low variance and below target = stagnation
            return CoherenceIssue(
                issue_id=f"stagnation_{metric.component}_{int(time.time() * 1000)}",
                component=metric.component,
                issue_type=CoherenceIssueType.UNDERLOAD.value,
                severity="medium",
                description=f"{metric.component} coherence stagnant at {metric.current_value:.3f}, target {metric.target_value:.3f}",
                impact_on_coherence=metric.target_value - metric.current_value,
                suggested_resolution=f"Apply stimulation and recalibration to {metric.component}"
            )
        
        return None
    
    async def _check_coherence_anomalies(self, metric: CoherenceMetric) -> List[CoherenceIssue]:
        """Check for anomalies in coherence patterns"""
        issues = []
        
        anomalies = self.analyzer.detect_coherence_anomalies(metric, threshold=self.anomaly_sensitivity)
        
        for anomaly in anomalies:
            if anomaly["type"] == "sudden_drop":
                issue = CoherenceIssue(
                    issue_id=f"sudden_drop_{metric.component}_{int(time.time() * 1000)}",
                    component=metric.component,
                    issue_type=CoherenceIssueType.ENERGY_IMBALANCE.value,
                    severity=anomaly["severity"],
                    description=f"{metric.component} sudden coherence drop: -{anomaly['magnitude']:.3f}",
                    impact_on_coherence=anomaly["magnitude"],
                    suggested_resolution=f"Apply energy rebalancing to {metric.component}"
                )
                issues.append(issue)
        
        return issues
    
    async def _check_cross_component_issues(self, component_metrics: Dict[str, CoherenceMetric]) -> List[CoherenceIssue]:
        """Check for issues across multiple components"""
        issues = []
        
        if len(component_metrics) < 2:
            return issues
        
        # Get component coherence values
        coherence_values = {name: metric.current_value for name, metric in component_metrics.items()}
        
        # Check for desynchronization
        desync_issue = await self._check_desynchronization(coherence_values)
        if desync_issue:
            issues.append(desync_issue)
        
        # Check for cascade failures
        cascade_issues = await self._check_cascade_failures(component_metrics)
        issues.extend(cascade_issues)
        
        # Check for communication breakdown
        comm_issue = await self._check_communication_breakdown(component_metrics)
        if comm_issue:
            issues.append(comm_issue)
        
        return issues
    
    async def _check_desynchronization(self, coherence_values: Dict[str, float]) -> Optional[CoherenceIssue]:
        """Check for desynchronization across components"""
        values = list(coherence_values.values())
        
        if len(values) >= 2:
            coherence_range = max(values) - min(values)
            
            if coherence_range > self.cross_component_sensitivity:
                # Large spread indicates desynchronization
                severity = "high" if coherence_range > 0.5 else "medium"
                
                return CoherenceIssue(
                    issue_id=f"desync_{int(time.time() * 1000)}",
                    component="cross_component",
                    issue_type=CoherenceIssueType.DESYNCHRONIZATION.value,
                    severity=severity,
                    description=f"Large coherence spread across components: {coherence_range:.2f}",
                    impact_on_coherence=coherence_range * 0.5,
                    suggested_resolution="Apply synchronization across all components"
                )
        
        return None
    
    async def _check_cascade_failures(self, component_metrics: Dict[str, CoherenceMetric]) -> List[CoherenceIssue]:
        """Check for cascade failure patterns"""
        issues = []
        
        # Look for multiple components degrading simultaneously
        degrading_components = []
        for name, metric in component_metrics.items():
            if metric.trend == "degrading" and metric.current_value < self.coherence_threshold:
                degrading_components.append(name)
        
        if len(degrading_components) >= 3:  # Multiple components degrading
            issue = CoherenceIssue(
                issue_id=f"cascade_failure_{int(time.time() * 1000)}",
                component="cross_component",
                issue_type=CoherenceIssueType.INTEGRATION_FAILURE.value,
                severity="critical",
                description=f"Cascade failure detected: {len(degrading_components)} components degrading",
                impact_on_coherence=0.3,  # High impact
                suggested_resolution="Emergency system-wide recalibration and stabilization"
            )
            issues.append(issue)
        
        return issues
    
    async def _check_communication_breakdown(self, component_metrics: Dict[str, CoherenceMetric]) -> Optional[CoherenceIssue]:
        """Check for communication breakdown between components"""
        # Check if integration component is showing issues while others are stable
        if "integration" in component_metrics:
            integration_metric = component_metrics["integration"]
            
            if integration_metric.current_value < 0.6:  # Integration struggling
                # Check if other components are doing well
                other_coherences = [
                    metric.current_value for name, metric in component_metrics.items()
                    if name != "integration"
                ]
                
                if other_coherences and sum(other_coherences) / len(other_coherences) > 0.8:
                    # Other components fine but integration struggling = communication issue
                    return CoherenceIssue(
                        issue_id=f"comm_breakdown_{int(time.time() * 1000)}",
                        component="integration",
                        issue_type=CoherenceIssueType.COMMUNICATION_BREAKDOWN.value,
                        severity="high",
                        description="Communication breakdown: integration failing while components stable",
                        impact_on_coherence=0.8 - integration_metric.current_value,
                        suggested_resolution="Restore communication pathways and integration protocols"
                    )
        
        return None
    
    async def _check_systemic_issues(self, component_metrics: Dict[str, CoherenceMetric]) -> List[CoherenceIssue]:
        """Check for systemic coherence issues"""
        issues = []
        
        if not component_metrics:
            return issues
        
        # Calculate overall system health
        all_coherences = [metric.current_value for metric in component_metrics.values()]
        system_coherence = sum(all_coherences) / len(all_coherences)
        
        # Check for systemic overload
        overload_issue = await self._check_systemic_overload(component_metrics, system_coherence)
        if overload_issue:
            issues.append(overload_issue)
        
        # Check for systemic underload
        underload_issue = await self._check_systemic_underload(component_metrics, system_coherence)
        if underload_issue:
            issues.append(underload_issue)
        
        # Check for energy distribution issues
        energy_issue = await self._check_energy_distribution_issues(component_metrics)
        if energy_issue:
            issues.append(energy_issue)
        
        return issues
    
    async def _check_systemic_overload(self, component_metrics: Dict[str, CoherenceMetric], 
                                     system_coherence: float) -> Optional[CoherenceIssue]:
        """Check for systemic overload affecting coherence"""
        # Look for pattern indicating overload: multiple components at max but unstable
        high_but_unstable = 0
        
        for metric in component_metrics.values():
            if metric.current_value > 0.9 and metric.trend == "degrading":
                high_but_unstable += 1
        
        if high_but_unstable >= 2:  # Multiple components showing overload pattern
            return CoherenceIssue(
                issue_id=f"systemic_overload_{int(time.time() * 1000)}",
                component="system",
                issue_type=CoherenceIssueType.OVERLOAD.value,
                severity="high",
                description=f"Systemic overload: {high_but_unstable} components showing overload patterns",
                impact_on_coherence=0.2,
                suggested_resolution="Apply load balancing and resource optimization"
            )
        
        return None
    
    async def _check_systemic_underload(self, component_metrics: Dict[str, CoherenceMetric],
                                      system_coherence: float) -> Optional[CoherenceIssue]:
        """Check for systemic underload affecting coherence"""
        if system_coherence < 0.6:  # Low overall coherence
            # Check if all components are consistently low
            low_components = sum(1 for metric in component_metrics.values() 
                               if metric.current_value < 0.7)
            
            if low_components >= len(component_metrics) * 0.8:  # 80% of components low
                return CoherenceIssue(
                    issue_id=f"systemic_underload_{int(time.time() * 1000)}",
                    component="system",
                    issue_type=CoherenceIssueType.UNDERLOAD.value,
                    severity="high",
                    description=f"Systemic underload: {low_components}/{len(component_metrics)} components below threshold",
                    impact_on_coherence=0.7 - system_coherence,
                    suggested_resolution="Apply system-wide energy boost and recalibration"
                )
        
        return None
    
    async def _check_energy_distribution_issues(self, component_metrics: Dict[str, CoherenceMetric]) -> Optional[CoherenceIssue]:
        """Check for energy distribution issues"""
        coherence_values = [metric.current_value for metric in component_metrics.values()]
        
        if len(coherence_values) < 2:
            return None
        
        # Check for extreme energy imbalance
        min_coherence = min(coherence_values)
        max_coherence = max(coherence_values)
        
        if max_coherence - min_coherence > 0.6:  # Extreme imbalance
            return CoherenceIssue(
                issue_id=f"energy_imbalance_{int(time.time() * 1000)}",
                component="system",
                issue_type=CoherenceIssueType.ENERGY_IMBALANCE.value,
                severity="medium",
                description=f"Extreme energy imbalance: range {max_coherence - min_coherence:.2f}",
                impact_on_coherence=(max_coherence - min_coherence) * 0.3,
                suggested_resolution="Rebalance energy distribution across components"
            )
        
        return None
    
    async def analyze_issue_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in detected issues"""
        if not self.issue_history:
            return {"patterns": [], "insights": ["No issue history available"]}
        
        patterns = []
        insights = []
        
        # Analyze issue frequency patterns
        recent_history = self.issue_history[-20:] if len(self.issue_history) >= 20 else self.issue_history
        
        # Time-based patterns
        issue_counts = [entry["issues_detected"] for entry in recent_history]
        avg_issues = sum(issue_counts) / len(issue_counts)
        
        if avg_issues > 3:
            insights.append("High issue detection rate - system may need attention")
            patterns.append("high_issue_frequency")
        elif avg_issues < 0.5:
            insights.append("Low issue detection rate - system operating smoothly")
            patterns.append("low_issue_frequency")
        
        # Issue type patterns
        all_types = []
        for entry in recent_history:
            all_types.extend(entry["issue_types"])
        
        if all_types:
            type_counts = {}
            for issue_type in all_types:
                type_counts[issue_type] = type_counts.get(issue_type, 0) + 1
            
            most_common = max(type_counts.items(), key=lambda x: x[1])
            if most_common[1] > len(recent_history) * 0.3:  # More than 30% of detection cycles
                insights.append(f"Recurring issue pattern: {most_common[0]} appears frequently")
                patterns.append(f"recurring_{most_common[0]}")
        
        return {
            "patterns": patterns,
            "insights": insights,
            "issue_frequency": avg_issues,
            "most_common_types": type_counts if 'type_counts' in locals() else {}
        }
    
    def get_issue_detection_status(self) -> Dict[str, Any]:
        """Get current issue detection system status"""
        return {
            "detection_active": True,
            "thresholds": {
                "coherence_threshold": self.coherence_threshold,
                "critical_threshold": self.critical_threshold,
                "degradation_sensitivity": self.degradation_sensitivity,
                "anomaly_sensitivity": self.anomaly_sensitivity,
                "cross_component_sensitivity": self.cross_component_sensitivity
            },
            "detected_issues": len(self.detected_issues),
            "detection_statistics": dict(self.detection_stats),
            "issue_history_size": len(self.issue_history)
        }
    
    async def clear_resolved_issues(self):
        """Clear issues that have been resolved"""
        resolved_issues = [
            issue_id for issue_id, issue in self.detected_issues.items()
            if issue.status == "resolved"
        ]
        
        for issue_id in resolved_issues:
            del self.detected_issues[issue_id]
            self.detection_stats["resolved_issues"] += 1
        
        if resolved_issues:
            logger.info(f"Cleared {len(resolved_issues)} resolved issues")


# Export main classes
__all__ = [
    'CoherenceIssueDetection'
]
