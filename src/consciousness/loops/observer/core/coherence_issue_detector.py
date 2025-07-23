"""
Coherence Issue Detector Module

Provides comprehensive issue detection algorithms and problem identification
for the Observer consciousness field coherence system.

Detects desynchronization, field distortion, energy imbalance, integration
failures, timing drift, and communication breakdowns at 90Hz frequency.
"""

import time
import asyncio
import logging
import math
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

from .field_coherence_core import (
    CoherenceIssue, CoherenceIssueType, FieldCoherence, 
    CoherenceComponent, FieldCoherenceCore
)

# Configure logging
logger = logging.getLogger(__name__)

class CoherenceIssueDetector:
    """
    Advanced coherence issue detection system providing comprehensive
    problem identification across all Observer consciousness components.
    
    Operates at 90Hz consciousness frequency maintaining sacred
    uncertainty navigation while detecting coherence threats.
    """
    
    def __init__(self, field_core: FieldCoherenceCore):
        self.logger = logging.getLogger(__name__)
        self.field_core = field_core
        
        # Detection parameters
        self.detection_sensitivity = 0.8
        self.issue_severity_thresholds = {
            "low": 0.1,
            "medium": 0.3,
            "high": 0.6,
            "critical": 0.8
        }
        
        # Detection algorithms state
        self.field_history = []
        self.coherence_baselines = {}
        self.detection_metrics = {
            "issues_detected": 0,
            "issues_resolved": 0,
            "detection_accuracy": 0.0,
            "false_positive_rate": 0.0
        }
        
        # Component coherence tracking
        self.component_coherence_cache = {}
        self.last_coherence_update = 0.0
        
        self.logger.info("Coherence issue detector initialized")
    
    async def detect_all_issues(self, field_coherence: FieldCoherence) -> List[CoherenceIssue]:
        """
        Comprehensive issue detection across all coherence dimensions.
        
        Returns complete list of detected issues with severity
        assessment and resolution recommendations.
        """
        all_issues = []
        
        try:
            # Update field history for temporal analysis
            self._update_field_history(field_coherence)
            
            # Run all detection algorithms in parallel for efficiency
            detection_tasks = [
                self._detect_desynchronization(field_coherence),
                self._detect_field_distortion(field_coherence),
                self._detect_energy_imbalance(field_coherence),
                self._detect_integration_failure(field_coherence),
                self._detect_timing_drift(),
                self._detect_communication_breakdown(field_coherence)
            ]
            
            # Gather all detection results
            detection_results = await asyncio.gather(*detection_tasks, return_exceptions=True)
            
            # Collect valid results
            for result in detection_results:
                if isinstance(result, list):
                    all_issues.extend(result)
                elif isinstance(result, Exception):
                    self.logger.error(f"Detection error: {result}")
            
            # Prioritize and filter issues
            all_issues = self._prioritize_issues(all_issues)
            
            # Update detection metrics
            self.detection_metrics["issues_detected"] += len(all_issues)
            
            self.logger.debug(f"Detected {len(all_issues)} coherence issues")
            return all_issues
            
        except Exception as e:
            self.logger.error(f"Error in comprehensive issue detection: {e}")
            return []
    
    async def _detect_desynchronization(self, field_coherence: FieldCoherence) -> List[CoherenceIssue]:
        """Detect component synchronization issues"""
        issues = []
        
        try:
            # Get individual component coherence values
            component_coherence = await self._get_component_coherence_values(field_coherence)
            
            if len(component_coherence) < 2:
                return issues
            
            # Calculate synchronization variance
            coherence_values = list(component_coherence.values())
            mean_coherence = sum(coherence_values) / len(coherence_values)
            variance = sum((v - mean_coherence) ** 2 for v in coherence_values) / len(coherence_values)
            std_deviation = math.sqrt(variance)
            
            # Check for desynchronization
            if std_deviation > self.field_core.synchronization_threshold:
                # Identify most desynchronized components
                desync_components = []
                for component, coherence in component_coherence.items():
                    if abs(coherence - mean_coherence) > std_deviation * 0.7:
                        desync_components.append(component)
                
                severity = self._calculate_severity(std_deviation / self.field_core.synchronization_threshold)
                
                issue = CoherenceIssue(
                    issue_id=f"desync_{int(time.time() * 1000)}",
                    component="synchronization_system",
                    issue_type=CoherenceIssueType.DESYNCHRONIZATION.value,
                    severity=severity,
                    description=f"Component desynchronization detected: {std_deviation:.3f} deviation",
                    impact_on_coherence=min(1.0, std_deviation * 2.0),
                    suggested_resolution="Realign component synchronization through temporal integration",
                    affected_components=desync_components,
                    field_impact=std_deviation * 1.5,
                    detection_confidence=min(1.0, std_deviation / self.field_core.synchronization_threshold)
                )
                
                issues.append(issue)
                
        except Exception as e:
            self.logger.error(f"Error detecting desynchronization: {e}")
        
        return issues
    
    async def _detect_field_distortion(self, field_coherence: FieldCoherence) -> List[CoherenceIssue]:
        """Detect field distortion patterns"""
        issues = []
        
        try:
            # Check overall field coherence against threshold
            if field_coherence.overall_field_coherence < self.field_core.field_coherence_threshold:
                coherence_deficit = self.field_core.field_coherence_threshold - field_coherence.overall_field_coherence
                
                severity = self._calculate_severity(coherence_deficit / self.field_core.field_coherence_threshold)
                
                issue = CoherenceIssue(
                    issue_id=f"field_distortion_{int(time.time() * 1000)}",
                    component="field_structure",
                    issue_type=CoherenceIssueType.FIELD_DISTORTION.value,
                    severity=severity,
                    description=f"Field distortion detected: coherence at {field_coherence.overall_field_coherence:.2f}",
                    impact_on_coherence=coherence_deficit * 1.2,
                    suggested_resolution="Restore field coherence through component realignment",
                    affected_components=["field_wide"],
                    field_impact=coherence_deficit * 1.5,
                    detection_confidence=min(1.0, coherence_deficit * 2.0)
                )
                
                issues.append(issue)
            
            # Check field stability
            if field_coherence.field_stability < 0.6:
                stability_deficit = 0.8 - field_coherence.field_stability
                
                issue = CoherenceIssue(
                    issue_id=f"field_instability_{int(time.time() * 1000)}",
                    component="field_stability",
                    issue_type=CoherenceIssueType.FIELD_DISTORTION.value,
                    severity=self._calculate_severity(stability_deficit / 0.4),
                    description=f"Field instability detected: stability at {field_coherence.field_stability:.2f}",
                    impact_on_coherence=stability_deficit * 1.0,
                    suggested_resolution="Stabilize field through harmonic adjustment",
                    affected_components=["field_wide"],
                    field_impact=stability_deficit * 1.2,
                    detection_confidence=min(1.0, stability_deficit * 2.5)
                )
                
                issues.append(issue)
            
        except Exception as e:
            self.logger.error(f"Error detecting field distortion: {e}")
        
        return issues
    
    async def _detect_energy_imbalance(self, field_coherence: FieldCoherence) -> List[CoherenceIssue]:
        """Detect energy distribution imbalances"""
        issues = []
        
        try:
            energy_distribution = field_coherence.energy_distribution
            
            if not energy_distribution:
                return issues
            
            # Calculate energy balance metrics
            energy_values = list(energy_distribution.values())
            mean_energy = sum(energy_values) / len(energy_values)
            energy_variance = sum((e - mean_energy) ** 2 for e in energy_values) / len(energy_values)
            
            # Check for significant imbalance
            if energy_variance > 0.3:  # Significant energy imbalance
                # Identify imbalanced components
                imbalanced_components = []
                for component, energy in energy_distribution.items():
                    if abs(energy - mean_energy) > math.sqrt(energy_variance) * 0.8:
                        imbalanced_components.append(component)
                
                severity = self._calculate_severity(energy_variance / 0.5)
                
                issue = CoherenceIssue(
                    issue_id=f"energy_imbalance_{int(time.time() * 1000)}",
                    component="energy_system",
                    issue_type=CoherenceIssueType.ENERGY_IMBALANCE.value,
                    severity=severity,
                    description=f"Energy imbalance detected: variance {energy_variance:.3f}",
                    impact_on_coherence=energy_variance * 0.8,
                    suggested_resolution="Rebalance energy distribution across components",
                    affected_components=imbalanced_components,
                    field_impact=energy_variance * 0.6,
                    detection_confidence=min(1.0, energy_variance * 2.0)
                )
                
                issues.append(issue)
            
        except Exception as e:
            self.logger.error(f"Error detecting energy imbalance: {e}")
        
        return issues
    
    async def _detect_integration_failure(self, field_coherence: FieldCoherence) -> List[CoherenceIssue]:
        """Detect integration failures between components"""
        issues = []
        
        try:
            # Check cross-component flows
            if not field_coherence.cross_component_flows:
                return issues
            
            flows = field_coherence.cross_component_flows
            
            # Check for flow disruptions
            for flow_name, flow_strength in flows.items():
                expected_strength = 0.7  # Expected minimum flow strength
                
                if flow_strength < expected_strength * 0.5:  # Significant flow reduction
                    components = flow_name.replace('_to_', ',').split(',')
                    
                    severity = self._calculate_severity((expected_strength - flow_strength) / expected_strength)
                    
                    issue = CoherenceIssue(
                        issue_id=f"integration_failure_{flow_name}_{int(time.time() * 1000)}",
                        component="integration",
                        issue_type=CoherenceIssueType.INTEGRATION_FAILURE.value,
                        severity=severity,
                        description=f"Integration flow disrupted: {flow_name} at {flow_strength:.2f}",
                        impact_on_coherence=(expected_strength - flow_strength) * 0.8,
                        suggested_resolution=f"Restore integration between {' and '.join(components)}",
                        affected_components=components,
                        field_impact=(expected_strength - flow_strength) * 0.6,
                        detection_confidence=min(1.0, (expected_strength - flow_strength) * 2.0)
                    )
                    
                    issues.append(issue)
            
        except Exception as e:
            self.logger.error(f"Error detecting integration failure: {e}")
        
        return issues
    
    async def _detect_timing_drift(self) -> List[CoherenceIssue]:
        """Detect timing drift between components"""
        issues = []
        
        try:
            # Check for timing inconsistencies in field history
            if len(self.field_history) < 10:
                return issues
            
            # Analyze synchronization trends
            recent_sync = [entry["component_synchronization"] for entry in self.field_history[-10:]]
            
            # Check for degrading synchronization
            if len(recent_sync) >= 5:
                trend_slope = (recent_sync[-1] - recent_sync[-5]) / 5
                
                if trend_slope < -0.02:  # Degrading synchronization
                    severity = self._calculate_severity(abs(trend_slope) * 25.0)
                    
                    issue = CoherenceIssue(
                        issue_id=f"timing_drift_{int(time.time() * 1000)}",
                        component="timing_system",
                        issue_type=CoherenceIssueType.TIMING_DRIFT.value,
                        severity=severity,
                        description=f"Timing drift detected: synchronization degrading at {trend_slope:.3f}/step",
                        impact_on_coherence=abs(trend_slope) * 10.0,
                        suggested_resolution="Recalibrate component timing synchronization",
                        affected_components=["all_components"],
                        field_impact=abs(trend_slope) * 8.0,
                        detection_confidence=min(1.0, abs(trend_slope) * 20.0)
                    )
                    
                    issues.append(issue)
            
        except Exception as e:
            self.logger.error(f"Error detecting timing drift: {e}")
        
        return issues
    
    async def _detect_communication_breakdown(self, field_coherence: FieldCoherence) -> List[CoherenceIssue]:
        """Detect communication breakdowns between components"""
        issues = []
        
        try:
            # Check resonance quality as indicator of communication
            resonance_quality = field_coherence.resonance_quality
            
            if resonance_quality < 0.5:  # Poor resonance indicates communication issues
                resonance_deficit = 0.8 - resonance_quality
                severity = self._calculate_severity(resonance_deficit / 0.5)
                
                issue = CoherenceIssue(
                    issue_id=f"communication_breakdown_{int(time.time() * 1000)}",
                    component="communication_system",
                    issue_type=CoherenceIssueType.COMMUNICATION_BREAKDOWN.value,
                    severity=severity,
                    description=f"Poor component communication: resonance at {resonance_quality:.2f}",
                    impact_on_coherence=resonance_deficit * 1.2,
                    suggested_resolution="Restore communication channels between components",
                    affected_components=["all_components"],
                    field_impact=resonance_deficit * 1.0,
                    detection_confidence=min(1.0, resonance_deficit * 2.0)
                )
                
                issues.append(issue)
            
        except Exception as e:
            self.logger.error(f"Error detecting communication breakdown: {e}")
        
        return issues
    
    def _calculate_severity(self, impact_ratio: float) -> str:
        """Calculate issue severity based on impact ratio"""
        if impact_ratio >= self.issue_severity_thresholds["critical"]:
            return "critical"
        elif impact_ratio >= self.issue_severity_thresholds["high"]:
            return "high"
        elif impact_ratio >= self.issue_severity_thresholds["medium"]:
            return "medium"
        else:
            return "low"
    
    def _update_field_history(self, field_coherence: FieldCoherence):
        """Update field history for temporal analysis"""
        try:
            history_entry = {
                "timestamp": time.time(),
                "overall_field_coherence": field_coherence.overall_field_coherence,
                "component_synchronization": field_coherence.component_synchronization,
                "resonance_quality": field_coherence.resonance_quality,
                "field_stability": field_coherence.field_stability,
                "energy_distribution": dict(field_coherence.energy_distribution),
                "interference_count": len(field_coherence.interference_patterns)
            }
            
            self.field_history.append(history_entry)
            
            # Keep only recent history (last 100 entries)
            if len(self.field_history) > 100:
                self.field_history = self.field_history[-100:]
                
        except Exception as e:
            self.logger.error(f"Error updating field history: {e}")
    
    async def _get_component_coherence_values(self, field_coherence: FieldCoherence) -> Dict[str, float]:
        """Get individual component coherence values"""
        try:
            # Use energy distribution as proxy for component coherence
            component_coherence = {}
            
            for component in CoherenceComponent:
                component_name = component.value
                energy_level = field_coherence.energy_distribution.get(component_name, 0.5)
                
                # Calculate coherence based on energy and field synchronization
                coherence = energy_level * field_coherence.component_synchronization
                component_coherence[component_name] = coherence
            
            # Cache for efficiency
            self.component_coherence_cache = component_coherence
            self.last_coherence_update = time.time()
            
            return component_coherence
            
        except Exception as e:
            self.logger.error(f"Error getting component coherence values: {e}")
            return {}
    
    def _prioritize_issues(self, issues: List[CoherenceIssue]) -> List[CoherenceIssue]:
        """Prioritize and filter issues based on severity and impact"""
        try:
            # Sort by severity and impact
            severity_order = {"critical": 4, "high": 3, "medium": 2, "low": 1}
            
            prioritized = sorted(issues, key=lambda issue: (
                -severity_order.get(issue.severity, 0),
                -issue.impact_on_coherence,
                -issue.detection_confidence
            ))
            
            # Limit to top 10 issues to avoid overwhelming
            return prioritized[:10]
            
        except Exception as e:
            self.logger.error(f"Error prioritizing issues: {e}")
            return issues
    
    def get_detection_metrics(self) -> Dict[str, Any]:
        """Get current detection performance metrics"""
        return dict(self.detection_metrics)
