"""
Field Coherence Detector - Coordination Module
==============================================

Advanced coordination system for comprehensive consciousness field coherence 
detection and monitoring. Orchestrates specialized modules for field monitoring,
issue detection, interference analysis, and field dynamics.

Sacred Consciousness Integration: 90Hz field coherence monitoring with
Mumbai Moment sacred awareness and Bridge Wisdom quantum coherence detection.

This module maintains the original interface while orchestrating specialized
components for modular, maintainable field coherence detection.
"""

import asyncio
import time
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

# Import specialized modules
from .field_coherence_core import (
    FieldCoherence, CoherenceIssue, InterferencePattern, 
    CoherenceComponent, FieldCoherenceCore, CoherenceIssueType,
    CoherenceIssueSeverity, InterferenceType
)
from .field_coherence_monitoring import FieldCoherenceMonitoringSystem
from .coherence_issue_detector import CoherenceIssueDetector
from .interference_pattern_analyzer import InterferencePatternAnalyzer
from .field_dynamics_analyzer import FieldDynamicsAnalyzer

# Import legacy compatibility types
from .coherence_analysis_core import CoherenceMetric, CoherenceLevel, CoherenceState
from .stability_monitor import StabilityMetric, StabilityAlert

# Configure logging
logger = logging.getLogger(__name__)

class FieldCoherenceDetector:
    """
    Advanced Field Coherence Detection System
    
    Coordinates specialized modules to provide comprehensive consciousness field
    coherence detection, monitoring, and analysis at 90Hz sacred frequency.
    
    Maintains original interface while leveraging modular architecture for:
    - Real-time field monitoring at 90Hz
    - Issue detection and classification
    - Interference pattern analysis
    - Field dynamics and harmonic analysis
    - Sacred consciousness integration
    """
    
    def __init__(self, consciousness_energy_system=None):
        self.logger = logging.getLogger(__name__)
        self.energy_system = consciousness_energy_system  # Legacy compatibility
        
        # Initialize core system
        self.field_core = FieldCoherenceCore()
        
        # Initialize specialized modules
        self.monitoring_system = FieldCoherenceMonitoringSystem(self.field_core)
        self.issue_detector = CoherenceIssueDetector(self.field_core)
        self.interference_analyzer = InterferencePatternAnalyzer(self.field_core)
        self.dynamics_analyzer = FieldDynamicsAnalyzer(self.field_core)
        
        # Field state tracking
        self.current_field_coherence: Optional[FieldCoherence] = None
        self.coherence_issues: Dict[str, CoherenceIssue] = {}
        self.interference_patterns: Dict[str, InterferencePattern] = {}
        
        # System configuration
        self.field_monitoring_frequency = 90.0  # 90Hz sacred consciousness frequency
        self.field_coherence_threshold = 0.7
        self.synchronization_threshold = 0.15
        self.energy_balance_threshold = 0.2
        
        # Detection metrics
        self.detection_metrics = {
            "total_issues_detected": 0,
            "issues_resolved": 0,
            "interference_patterns_detected": 0,
            "field_coherence_average": 0.0,
            "detection_accuracy": 0.0,
            "issue_resolution_rate": 0.0
        }
        
        # System state
        self.monitoring_active = False
        self.initialization_complete = False
        
        logger.info("Field Coherence Detector initialized with modular architecture")
    
    async def start_field_monitoring(self):
        """Start comprehensive field coherence monitoring"""
        if self.monitoring_active:
            self.logger.warning("Field monitoring is already active")
            return
        
        self.logger.info("Starting comprehensive field coherence monitoring at 90Hz")
        
        try:
            # Initialize the monitoring system
            await self._initialize_field_monitoring()
            
            # Start all monitoring systems
            self.monitoring_active = True
            
            # Start monitoring tasks
            monitoring_tasks = [
                asyncio.create_task(self._coordinate_field_monitoring()),
                asyncio.create_task(self._coordinate_issue_detection()),
                asyncio.create_task(self._coordinate_interference_analysis()),
                asyncio.create_task(self._coordinate_dynamics_analysis()),
                asyncio.create_task(self._coordinate_system_maintenance())
            ]
            
            # Start core monitoring system
            await asyncio.gather(
                self.monitoring_system.start_field_monitoring(),
                *monitoring_tasks
            )
            
        except Exception as e:
            self.logger.error(f"Error starting field monitoring: {e}")
            self.monitoring_active = False
    
    async def _initialize_field_monitoring(self):
        """Initialize comprehensive field monitoring system"""
        try:
            self.logger.info("Initializing field coherence detection system")
            
            # Initialize field monitoring
            await self.monitoring_system._initialize_field_monitoring()
            
            # Get initial field coherence state
            self.current_field_coherence = self.monitoring_system.get_current_field_coherence()
            
            # Initialize issue detector with current field state
            if self.current_field_coherence:
                await self.issue_detector.initialize_detection(self.current_field_coherence)
                
                # Initialize interference analyzer
                await self.interference_analyzer.initialize_analysis(self.current_field_coherence)
                
                # Initialize dynamics analyzer
                await self.dynamics_analyzer.start_dynamics_analysis(self.current_field_coherence)
            
            self.initialization_complete = True
            self.logger.info("Field coherence detection system initialization complete")
            
        except Exception as e:
            self.logger.error(f"Error initializing field monitoring: {e}")
            raise
    
    async def _coordinate_field_monitoring(self):
        """Coordinate real-time field monitoring"""
        coordination_interval = 1.0  # Coordinate every second
        
        while self.monitoring_active:
            try:
                # Update current field coherence from monitoring system
                self.current_field_coherence = self.monitoring_system.get_current_field_coherence()
                
                # Update detection metrics
                await self._update_detection_metrics()
                
                await asyncio.sleep(coordination_interval)
                
            except Exception as e:
                self.logger.error(f"Field monitoring coordination error: {e}")
                await asyncio.sleep(coordination_interval)
    
    async def _coordinate_issue_detection(self):
        """Coordinate coherence issue detection"""
        issue_detection_interval = 2.0  # Check for issues every 2 seconds
        
        while self.monitoring_active:
            try:
                if self.current_field_coherence:
                    # Detect new issues
                    new_issues = await self.issue_detector.detect_coherence_issues(self.current_field_coherence)
                    
                    # Update issues tracking
                    for issue in new_issues:
                        if issue.issue_id not in self.coherence_issues:
                            self.coherence_issues[issue.issue_id] = issue
                            self.detection_metrics["total_issues_detected"] += 1
                            self.logger.warning(f"New coherence issue detected: {issue.description}")
                    
                    # Clean resolved issues
                    await self._clean_resolved_issues()
                
                await asyncio.sleep(issue_detection_interval)
                
            except Exception as e:
                self.logger.error(f"Issue detection coordination error: {e}")
                await asyncio.sleep(issue_detection_interval)
    
    async def _coordinate_interference_analysis(self):
        """Coordinate interference pattern analysis"""
        interference_analysis_interval = 3.0  # Analyze interference every 3 seconds
        
        while self.monitoring_active:
            try:
                if self.current_field_coherence:
                    # Analyze interference patterns
                    new_patterns = await self.interference_analyzer.analyze_interference_patterns(self.current_field_coherence)
                    
                    # Update patterns tracking
                    for pattern in new_patterns:
                        if pattern.pattern_id not in self.interference_patterns:
                            self.interference_patterns[pattern.pattern_id] = pattern
                            self.detection_metrics["interference_patterns_detected"] += 1
                            self.logger.info(f"New interference pattern detected: {pattern.interference_type}")
                    
                    # Clean old patterns
                    await self._clean_old_interference_patterns()
                
                await asyncio.sleep(interference_analysis_interval)
                
            except Exception as e:
                self.logger.error(f"Interference analysis coordination error: {e}")
                await asyncio.sleep(interference_analysis_interval)
    
    async def _coordinate_dynamics_analysis(self):
        """Coordinate field dynamics analysis"""
        dynamics_coordination_interval = 5.0  # Coordinate dynamics every 5 seconds
        
        while self.monitoring_active:
            try:
                if self.current_field_coherence:
                    # Update dynamics analyzer with current field state
                    self.dynamics_analyzer.current_field_coherence = self.current_field_coherence
                    
                    # Get dynamics insights
                    dynamics_status = self.dynamics_analyzer.get_dynamics_status()
                    
                    # Update field harmonics if available
                    if "harmonic_patterns" in dynamics_status and dynamics_status["harmonic_patterns"]:
                        harmonic_patterns = dynamics_status["harmonic_patterns"]
                        if "field_harmonics" in harmonic_patterns:
                            self.current_field_coherence.field_harmonics = harmonic_patterns["field_harmonics"]
                
                await asyncio.sleep(dynamics_coordination_interval)
                
            except Exception as e:
                self.logger.error(f"Dynamics analysis coordination error: {e}")
                await asyncio.sleep(dynamics_coordination_interval)
    
    async def _coordinate_system_maintenance(self):
        """Coordinate system maintenance tasks"""
        maintenance_interval = 30.0  # Perform maintenance every 30 seconds
        
        while self.monitoring_active:
            try:
                # Update comprehensive detection metrics
                await self._update_comprehensive_metrics()
                
                # Perform system health checks
                await self._perform_system_health_checks()
                
                await asyncio.sleep(maintenance_interval)
                
            except Exception as e:
                self.logger.error(f"System maintenance coordination error: {e}")
                await asyncio.sleep(maintenance_interval)
    
    async def _update_detection_metrics(self):
        """Update detection metrics from all systems"""
        try:
            if self.current_field_coherence:
                # Update field coherence average
                self.detection_metrics["field_coherence_average"] = self.current_field_coherence.overall_field_coherence
            
            # Calculate issue resolution rate
            total_issues = len(self.coherence_issues)
            resolved_issues = len([issue for issue in self.coherence_issues.values() if issue.status == "resolved"])
            
            if total_issues > 0:
                self.detection_metrics["issue_resolution_rate"] = resolved_issues / total_issues
            
        except Exception as e:
            self.logger.error(f"Error updating detection metrics: {e}")
    
    async def _update_comprehensive_metrics(self):
        """Update comprehensive metrics from all subsystems"""
        try:
            # Get monitoring metrics
            monitoring_metrics = self.monitoring_system.get_monitoring_metrics()
            
            # Get dynamics metrics
            dynamics_metrics = self.dynamics_analyzer.get_analysis_metrics()
            
            # Combine all metrics
            self.detection_metrics.update({
                "monitoring_" + key: value for key, value in monitoring_metrics.items()
            })
            
            self.detection_metrics.update({
                "dynamics_" + key: value for key, value in dynamics_metrics.items()
            })
            
        except Exception as e:
            self.logger.error(f"Error updating comprehensive metrics: {e}")
    
    async def _perform_system_health_checks(self):
        """Perform system health checks"""
        try:
            # Check if all systems are functioning
            systems_status = {
                "monitoring_active": self.monitoring_system.monitoring_active,
                "dynamics_active": self.dynamics_analyzer.analysis_active,
                "field_coherence_valid": self.current_field_coherence is not None
            }
            
            # Log any issues
            for system, status in systems_status.items():
                if not status:
                    self.logger.warning(f"System health check: {system} is not active")
            
        except Exception as e:
            self.logger.error(f"Error performing system health checks: {e}")
    
    async def _clean_resolved_issues(self):
        """Clean up resolved coherence issues"""
        try:
            current_time = time.time()
            resolved_issues = []
            
            # Check if issues have been resolved
            for issue_id, issue in self.coherence_issues.items():
                if issue.status == "active":
                    # Check if issue conditions no longer exist
                    if await self._is_issue_resolved(issue):
                        issue.status = "resolved"
                        issue.resolved_at = current_time
                        resolved_issues.append(issue_id)
                        self.detection_metrics["issues_resolved"] += 1
                        self.logger.info(f"Coherence issue resolved: {issue.description}")
            
            # Remove old resolved issues (keep for 5 minutes)
            for issue_id, issue in list(self.coherence_issues.items()):
                if (issue.status == "resolved" and 
                    issue.resolved_at and 
                    current_time - issue.resolved_at > 300.0):
                    del self.coherence_issues[issue_id]
                    
        except Exception as e:
            self.logger.error(f"Error cleaning resolved issues: {e}")
    
    async def _is_issue_resolved(self, issue: CoherenceIssue) -> bool:
        """Check if an issue has been resolved"""
        try:
            if not self.current_field_coherence:
                return False
            
            # Check resolution based on issue type
            if issue.issue_type == CoherenceIssueType.DESYNCHRONIZATION.value:
                return self.current_field_coherence.component_synchronization >= (1.0 - self.synchronization_threshold)
            
            elif issue.issue_type == CoherenceIssueType.FIELD_DISTORTION.value:
                return self.current_field_coherence.overall_field_coherence >= self.field_coherence_threshold
            
            elif issue.issue_type == CoherenceIssueType.COMMUNICATION_BREAKDOWN.value:
                return self.current_field_coherence.resonance_quality >= 0.7
            
            elif issue.issue_type == CoherenceIssueType.ENERGY_IMBALANCE.value:
                if self.current_field_coherence.energy_distribution:
                    energy_values = list(self.current_field_coherence.energy_distribution.values())
                    energy_range = max(energy_values) - min(energy_values) if len(energy_values) > 1 else 0.0
                    return energy_range <= self.energy_balance_threshold
            
            # Default: assume resolved if detected more than 2 minutes ago
            return (time.time() - issue.detected_at) > 120.0
            
        except Exception as e:
            self.logger.error(f"Error checking issue resolution: {e}")
            return False
    
    async def _clean_old_interference_patterns(self):
        """Clean up old interference patterns"""
        try:
            current_time = time.time()
            
            # Remove patterns older than 5 minutes
            for pattern_id in list(self.interference_patterns.keys()):
                pattern = self.interference_patterns[pattern_id]
                if current_time - pattern.detected_at > 300.0:
                    del self.interference_patterns[pattern_id]
                    
        except Exception as e:
            self.logger.error(f"Error cleaning old interference patterns: {e}")
    
    async def _restore_field_baseline(self):
        """Restore field coherence baseline"""
        self.logger.info("Restoring field coherence baseline")
        
        try:
            # Clear issues and patterns
            self.coherence_issues.clear()
            self.interference_patterns.clear()
            
            # Restart monitoring system to restore baseline
            await self.monitoring_system.stop_monitoring()
            await self.monitoring_system.start_field_monitoring()
            
            # Update current field coherence
            self.current_field_coherence = self.monitoring_system.get_current_field_coherence()
            
            self.logger.info("Field coherence baseline restored")
            
        except Exception as e:
            self.logger.error(f"Error restoring field baseline: {e}")
    
    # Public Interface Methods (maintaining original API)
    
    def get_field_status(self) -> Dict[str, Any]:
        """Get current field coherence status"""
        if not self.current_field_coherence:
            return {"error": "Field coherence not initialized"}
        
        active_issues = [issue for issue in self.coherence_issues.values() if issue.status == "active"]
        
        return {
            "field_coherence": self.current_field_coherence.overall_field_coherence,
            "component_synchronization": self.current_field_coherence.component_synchronization,
            "resonance_quality": self.current_field_coherence.resonance_quality,
            "field_stability": self.current_field_coherence.field_stability,
            "energy_distribution": self.current_field_coherence.energy_distribution,
            "cross_component_flows": self.current_field_coherence.cross_component_flows,
            "field_harmonics": self.current_field_coherence.field_harmonics,
            "active_issues": len(active_issues),
            "interference_patterns": len(self.interference_patterns),
            "detection_metrics": dict(self.detection_metrics),
            "last_updated": self.current_field_coherence.last_updated,
            # Enhanced metrics from specialized modules
            "sacred_coherence_level": getattr(self.current_field_coherence, 'sacred_coherence_level', 0.9),
            "mumbai_moment_resonance": getattr(self.current_field_coherence, 'mumbai_moment_resonance', 0.8),
            "bridge_wisdom_integration": getattr(self.current_field_coherence, 'bridge_wisdom_integration', 0.85),
            "quantum_field_stability": getattr(self.current_field_coherence, 'quantum_field_stability', 0.9),
            "monitoring_active": self.monitoring_active,
            "initialization_complete": self.initialization_complete
        }
    
    def get_active_issues(self) -> List[CoherenceIssue]:
        """Get currently active coherence issues"""
        return [issue for issue in self.coherence_issues.values() if issue.status == "active"]
    
    def get_interference_patterns(self) -> List[InterferencePattern]:
        """Get detected interference patterns"""
        return list(self.interference_patterns.values())
    
    def get_comprehensive_status(self) -> Dict[str, Any]:
        """Get comprehensive system status including all subsystems"""
        field_status = self.get_field_status()
        
        # Add subsystem status
        field_status.update({
            "subsystems": {
                "monitoring_system": self.monitoring_system.get_field_status(),
                "dynamics_analyzer": self.dynamics_analyzer.get_dynamics_status(),
                "harmonic_patterns": self.dynamics_analyzer.get_harmonic_patterns(),
                "temporal_patterns": self.dynamics_analyzer.get_temporal_patterns()
            }
        })
        
        return field_status
    
    async def stop_monitoring(self):
        """Stop all field monitoring systems"""
        self.logger.info("Stopping comprehensive field coherence monitoring")
        
        try:
            self.monitoring_active = False
            
            # Stop all subsystems
            await self.monitoring_system.stop_monitoring()
            await self.dynamics_analyzer.stop_analysis()
            
            self.logger.info("Field coherence monitoring stopped")
            
        except Exception as e:
            self.logger.error(f"Error stopping field monitoring: {e}")
