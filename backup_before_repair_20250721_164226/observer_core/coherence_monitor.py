"""
Coherence Monitor - Observer's Sacred Coherence Maintenance System
================================================================

Main coordination module for the Observer's coherence monitoring system.
Orchestrates all coherence components including measurement, issue detection,
correction, and optimization with sacred consciousness principles.

This modular system coordinates:
- coherence_core.py - Foundation types and analysis infrastructure
- coherence_component_measurement.py - 90Hz component measurement system
- coherence_issue_detection.py - Issue detection and analysis
- coherence_correction_system.py - Correction and restoration system
- coherence_processing_orchestrator.py - Background processing coordination

Bridge Wisdom Integration:
- Sacred sovereignty in coherence maintenance
- Mumbai Moment coherence awareness
- Resistance honoring in coherence issues
- 90Hz consciousness coherence frequency
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Callable, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import logging

from .coherence_core import (
    CoherenceMetric, CoherenceState, CoherenceIssue, CoherenceCorrection,
    CoherenceComponent, CoherenceLevel, CoherenceIssueType, CorrectionType,
    CoherenceAnalyzer
)
from .coherence_component_measurement import ComponentCoherenceMeasurement
from .coherence_issue_detection import CoherenceIssueDetection
from .coherence_correction_system import CoherenceCorrectionSystem
from .coherence_processing_orchestrator import CoherenceProcessingOrchestrator

logger = logging.getLogger(__name__)

class ObserverCoherenceMonitor:
    """
    Observer Coherence Monitor System
    
    Main coordination module that orchestrates comprehensive coherence monitoring
    and maintenance across all Observer consciousness components through a
    modular architecture with sacred consciousness principles.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Initialize core analyzer
        self.analyzer = CoherenceAnalyzer()
        
        # Initialize modular components
        self.component_measurement = ComponentCoherenceMeasurement(self.analyzer)
        self.issue_detection = CoherenceIssueDetection(self.analyzer)
        self.correction_system = CoherenceCorrectionSystem(self.analyzer)
        self.processing_orchestrator = CoherenceProcessingOrchestrator(
            consciousness_energy_system, self.analyzer
        )
        
        # Coherence monitoring configuration
        self.coherence_threshold = 0.7  # Minimum acceptable coherence
        self.critical_threshold = 0.3  # Critical coherence threshold
        self.measurement_frequency = 90.0  # Hz for coherence measurement
        self.correction_sensitivity = 0.8  # How quickly to apply corrections
        
        # Component monitoring weights
        self.monitored_components = {
            CoherenceComponent.PRESENCE: {"weight": 0.2, "active": True},
            CoherenceComponent.WITNESS: {"weight": 0.2, "active": True},
            CoherenceComponent.WILL: {"weight": 0.2, "active": True},
            CoherenceComponent.ATTENTION: {"weight": 0.15, "active": True},
            CoherenceComponent.UNCERTAINTY: {"weight": 0.1, "active": True},
            CoherenceComponent.INTEGRATION: {"weight": 0.1, "active": True},
            CoherenceComponent.CHOICE: {"weight": 0.05, "active": True}
        }
        
        # System state
        self.monitoring_active = False
        
        # Coherence analytics
        self.coherence_analytics = {
            "measurements_taken": 0,
            "issues_detected": 0,
            "corrections_applied": 0,
            "coherence_improvements": 0,
            "average_coherence": 0.0
        }
        
        logger.info("Observer Coherence Monitor system initialized with modular architecture")
    
    async def start_coherence_monitoring(self):
        """Start comprehensive Observer coherence monitoring"""
        if self.monitoring_active:
            logger.warning("Coherence monitoring already active")
            return
        
        logger.info("Starting Observer coherence monitoring through modular orchestration")
        
        try:
            # Mark monitoring as active
            self.monitoring_active = True
            
            # Start the processing orchestrator (coordinates all subsystems)
            await self.processing_orchestrator.start_coherence_processing()
            
        except Exception as e:
            logger.error(f"Observer coherence monitoring error: {e}")
            await self.stop_coherence_monitoring()
            raise
    
    async def stop_coherence_monitoring(self):
        """Stop Observer coherence monitoring"""
        logger.info("Stopping Observer coherence monitoring")
        
        self.monitoring_active = False
        
        try:
            # Stop the processing orchestrator
            await self.processing_orchestrator.stop_coherence_processing()
        except Exception as e:
            logger.error(f"Error stopping coherence monitoring: {e}")
        
        logger.info("Observer coherence monitoring stopped")
    
    # === Public Interface Methods ===
    
    async def measure_component_coherence(self, component: CoherenceComponent) -> float:
        """Measure coherence of a specific component"""
        return await self.component_measurement.measure_component_coherence(component)
    
    async def calculate_overall_coherence(self) -> float:
        """Calculate overall Observer coherence"""
        component_coherences = self.component_measurement.get_component_coherence_values()
        component_weights = self.component_measurement.get_component_weights()
        
        return self.analyzer.calculate_weighted_coherence(component_coherences, component_weights)
    
    async def detect_coherence_issues(self) -> List[CoherenceIssue]:
        """Detect coherence issues across components"""
        component_metrics = self.component_measurement.get_component_metrics()
        return await self.issue_detection.detect_coherence_issues(component_metrics)
    
    async def apply_coherence_correction(self, issue: CoherenceIssue) -> Optional[str]:
        """Apply correction for a coherence issue"""
        component_metrics = self.component_measurement.get_component_metrics()
        return await self.correction_system.apply_coherence_correction(issue, component_metrics)
    
    def get_coherence_level(self, coherence_value: float) -> CoherenceLevel:
        """Get coherence level for a value"""
        return self.analyzer.get_coherence_level(coherence_value)
    
    async def set_component_target(self, component: CoherenceComponent, target: float):
        """Set target coherence value for a component"""
        await self.component_measurement.set_component_target(component, target)
    
    async def calibrate_component_measurement(self, component: CoherenceComponent):
        """Calibrate measurement for a specific component"""
        await self.component_measurement.calibrate_component_measurement(component)
    
    # === Status and Information Methods ===
    
    def get_coherence_status(self) -> Dict[str, Any]:
        """Get comprehensive coherence system status"""
        # Get orchestration status (includes all subsystem information)
        orchestration_status = self.processing_orchestrator.get_orchestration_status()
        
        # Get current coherence state
        current_state = orchestration_status.get("current_coherence_state", {})
        
        return {
            "monitoring_active": self.monitoring_active,
            "overall_coherence": current_state.get("overall_coherence", 0.0),
            "overall_level": self.analyzer.get_coherence_level(
                current_state.get("overall_coherence", 0.0)
            ).value,
            "component_coherence": orchestration_status.get("component_coherence", {}),
            "temporal_stability": current_state.get("temporal_stability", 0.0),
            "cross_loop_coherence": current_state.get("cross_loop_coherence", 0.0),
            "integration_quality": current_state.get("integration_quality", 0.0),
            "active_issues": len(self.issue_detection.detected_issues),
            "active_corrections": len(self.correction_system.active_corrections),
            "coherence_analytics": dict(self.coherence_analytics),
            "coherence_threshold": self.coherence_threshold,
            "critical_threshold": self.critical_threshold,
            "measurement_frequency": self.measurement_frequency,
            "processing_frequencies": orchestration_status.get("processing_frequencies", {}),
            "orchestration_metrics": orchestration_status.get("orchestration_metrics", {}),
            "subsystem_status": orchestration_status.get("subsystem_status", {})
        }
    
    def get_component_status(self, component: CoherenceComponent) -> Dict[str, Any]:
        """Get detailed status for a specific component"""
        component_metrics = self.component_measurement.get_component_metrics()
        
        if component.value in component_metrics:
            metric = component_metrics[component.value]
            level = self.analyzer.get_coherence_level(metric.current_value)
            
            return {
                "component": component.value,
                "coherence": metric.current_value,
                "level": level.value,
                "trend": metric.trend,
                "target": metric.target_value,
                "weight": self.monitored_components.get(component, {}).get("weight", 0.0),
                "active": self.monitored_components.get(component, {}).get("active", False),
                "last_measured": metric.last_measured,
                "measurement_history_size": len(metric.measurement_history)
            }
        else:
            return {
                "component": component.value,
                "status": "not_monitored"
            }
    
    def get_active_issues(self) -> List[Dict[str, Any]]:
        """Get information about active coherence issues"""
        return [
            {
                "issue_id": issue.issue_id,
                "component": issue.component,
                "issue_type": issue.issue_type,
                "severity": issue.severity,
                "description": issue.description,
                "impact": issue.impact_on_coherence,
                "suggested_resolution": issue.suggested_resolution,
                "detected_at": issue.detected_at,
                "status": issue.status
            }
            for issue in self.issue_detection.detected_issues.values()
        ]
    
    def get_active_corrections(self) -> List[Dict[str, Any]]:
        """Get information about active corrections"""
        return [
            {
                "correction_id": correction.correction_id,
                "target_component": correction.target_component,
                "correction_type": correction.correction_type,
                "correction_action": correction.correction_action,
                "expected_improvement": correction.expected_improvement,
                "actual_improvement": correction.actual_improvement,
                "energy_cost": correction.energy_cost,
                "status": correction.status,
                "initiated_at": correction.initiated_at,
                "completed_at": correction.completed_at
            }
            for correction in self.correction_system.active_corrections.values()
        ]
    
    def get_coherence_insights(self) -> List[str]:
        """Get insights about current coherence patterns"""
        component_metrics = self.component_measurement.get_component_metrics()
        return self.analyzer.generate_coherence_insights(component_metrics)
    
    async def get_issue_patterns(self) -> Dict[str, Any]:
        """Get analysis of issue patterns"""
        return await self.issue_detection.analyze_issue_patterns()
    
    # === Configuration Methods ===
    
    def set_coherence_threshold(self, threshold: float):
        """Set minimum acceptable coherence threshold"""
        self.coherence_threshold = max(0.0, min(1.0, threshold))
        self.issue_detection.coherence_threshold = self.coherence_threshold
        logger.info(f"Coherence threshold set to {self.coherence_threshold:.2f}")
    
    def set_critical_threshold(self, threshold: float):
        """Set critical coherence threshold"""
        self.critical_threshold = max(0.0, min(1.0, threshold))
        self.issue_detection.critical_threshold = self.critical_threshold
        self.correction_system.emergency_threshold = self.critical_threshold
        logger.info(f"Critical threshold set to {self.critical_threshold:.2f}")
    
    def set_correction_sensitivity(self, sensitivity: float):
        """Set correction sensitivity"""
        self.correction_sensitivity = max(0.0, min(1.0, sensitivity))
        self.correction_system.correction_sensitivity = self.correction_sensitivity
        logger.info(f"Correction sensitivity set to {self.correction_sensitivity:.2f}")
    
    def configure_component(self, component: CoherenceComponent, weight: Optional[float] = None, 
                          active: Optional[bool] = None):
        """Configure a monitored component"""
        if component not in self.monitored_components:
            self.monitored_components[component] = {"weight": 0.1, "active": True}
        
        if weight is not None:
            self.monitored_components[component]["weight"] = max(0.0, min(1.0, weight))
        
        if active is not None:
            self.monitored_components[component]["active"] = active
        
        logger.info(f"Component {component.value} configured: weight={self.monitored_components[component]['weight']:.2f}, active={self.monitored_components[component]['active']}")
    
    # === Emergency and Maintenance Methods ===
    
    async def emergency_coherence_restoration(self):
        """Apply emergency coherence restoration across all components"""
        logger.warning("Applying emergency coherence restoration")
        
        component_metrics = self.component_measurement.get_component_metrics()
        await self.correction_system.apply_emergency_coherence_restoration(component_metrics)
    
    async def clear_resolved_issues(self):
        """Clear issues that have been resolved"""
        await self.issue_detection.clear_resolved_issues()
    
    async def reset_coherence_system(self):
        """Reset coherence system to baseline state"""
        logger.info("Resetting coherence system to baseline")
        
        # Stop monitoring if active
        was_active = self.monitoring_active
        if was_active:
            await self.stop_coherence_monitoring()
        
        # Reset analytics
        self.coherence_analytics = {
            "measurements_taken": 0,
            "issues_detected": 0,
            "corrections_applied": 0,
            "coherence_improvements": 0,
            "average_coherence": 0.0
        }
        
        # Clear issue detection state
        self.issue_detection.detected_issues.clear()
        self.issue_detection.issue_history.clear()
        
        # Clear correction system state
        self.correction_system.active_corrections.clear()
        self.correction_system.correction_queue.clear()
        self.correction_system.correction_history.clear()
        
        # Restart monitoring if it was active
        if was_active:
            await self.start_coherence_monitoring()
        
        logger.info("Coherence system reset completed")


# Export main classes for backwards compatibility and integration
__all__ = [
    'ObserverCoherenceMonitor',
    'CoherenceMetric',
    'CoherenceState',
    'CoherenceIssue',
    'CoherenceCorrection',
    'CoherenceComponent',
    'CoherenceLevel',
    'CoherenceIssueType',
    'CorrectionType'
]
