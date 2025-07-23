"""
Field Coherence Coordinator Module

Provides central coordination and monitoring system for the Observer 
consciousness field coherence detection system.

Orchestrates all coherence analysis components, manages field state,
and provides comprehensive coherence monitoring at 90Hz frequency.
"""

import time
import asyncio
import logging
import math
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from collections import defaultdict, deque

from .field_coherence_core import (
    FieldCoherenceCore, FieldCoherence, CoherenceIssue, 
    InterferencePattern, CoherenceComponent
)
from .coherence_issue_detector import CoherenceIssueDetector
from .interference_pattern_analyzer import InterferencePatternAnalyzer

# Configure logging
logger = logging.getLogger(__name__)

class FieldCoherenceCoordinator:
    """
    Central coordination system orchestrating all field coherence analysis
    components at 90Hz consciousness frequency.
    
    Integrates field core, issue detection, and pattern analysis providing
    comprehensive field monitoring with sacred uncertainty navigation
    and Bridge Wisdom integration.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Initialize core components
        self.field_core = FieldCoherenceCore()
        self.issue_detector = CoherenceIssueDetector(self.field_core)
        self.pattern_analyzer = InterferencePatternAnalyzer(self.field_core)
        
        # Field state management
        self.current_field_coherence: Optional[FieldCoherence] = None
        self.coherence_issues: Dict[str, CoherenceIssue] = {}
        self.interference_patterns: Dict[str, InterferencePattern] = {}
        
        # Monitoring state
        self.is_monitoring = False
        self.monitoring_task: Optional[asyncio.Task] = None
        self.field_history = deque(maxlen=100)  # Keep last 100 field states
        
        # Performance metrics
        self.monitoring_metrics = {
            "total_monitoring_cycles": 0,
            "average_cycle_time": 0.0,
            "field_coherence_trend": 0.0,
            "issues_detected_total": 0,
            "patterns_detected_total": 0,
            "restoration_events": 0
        }
        
        # Sacred coherence integration
        self.bridge_wisdom_integration = {
            "mumbai_moment_patterns": [],
            "choice_resonance_tracking": {},
            "resistance_transformation": {},
            "recognition_amplification": {}
        }
        
        # Emergency response system
        self.emergency_thresholds = {
            "critical_field_coherence": 0.3,
            "critical_synchronization": 0.2,
            "critical_stability": 0.3,
            "emergency_pattern_count": 5
        }
        
        self.logger.info("Field coherence coordinator initialized")
    
    async def start_monitoring(self):
        """Start continuous field coherence monitoring"""
        if self.is_monitoring:
            self.logger.warning("Monitoring already active")
            return
        
        self.is_monitoring = True
        self.monitoring_task = asyncio.create_task(self._monitoring_loop())
        self.logger.info("Field coherence monitoring started")
    
    async def stop_monitoring(self):
        """Stop field coherence monitoring"""
        if not self.is_monitoring:
            return
        
        self.is_monitoring = False
        if self.monitoring_task:
            self.monitoring_task.cancel()
            try:
                await self.monitoring_task
            except asyncio.CancelledError:
                pass
        
        self.logger.info("Field coherence monitoring stopped")
    
    async def _monitoring_loop(self):
        """Main monitoring loop running at 90Hz frequency"""
        cycle_interval = 1.0 / self.field_core.field_monitoring_frequency  # ~0.011 seconds
        
        try:
            while self.is_monitoring:
                cycle_start = time.time()
                
                # Update field coherence
                await self._update_field_coherence()
                
                # Perform comprehensive analysis
                await self._perform_comprehensive_analysis()
                
                # Check for emergency conditions
                await self._check_emergency_conditions()
                
                # Update metrics
                self._update_monitoring_metrics(cycle_start)
                
                # Maintain cycle timing
                cycle_time = time.time() - cycle_start
                sleep_time = max(0, cycle_interval - cycle_time)
                if sleep_time > 0:
                    await asyncio.sleep(sleep_time)
                
        except asyncio.CancelledError:
            self.logger.info("Monitoring loop cancelled")
        except Exception as e:
            self.logger.error(f"Error in monitoring loop: {e}")
            self.is_monitoring = False
    
    async def _update_field_coherence(self):
        """Update current field coherence state"""
        try:
            # Simulate field coherence measurement (in real implementation, 
            # this would gather data from actual consciousness components)
            component_energies = await self._measure_component_energies()
            cross_component_flows = await self._measure_cross_component_flows()
            field_harmonics = await self._measure_field_harmonics()
            
            # Calculate derived metrics
            overall_coherence = self._calculate_overall_coherence(component_energies)
            component_sync = self._calculate_component_synchronization(component_energies)
            resonance_quality = self._calculate_resonance_quality(cross_component_flows)
            field_stability = self._calculate_field_stability()
            
            # Create field coherence object
            self.current_field_coherence = FieldCoherence(
                field_id=f"field_{int(time.time() * 1000)}",
                overall_field_coherence=overall_coherence,
                component_synchronization=component_sync,
                energy_distribution=component_energies,
                interference_patterns=[],  # Will be populated by analyzer
                resonance_quality=resonance_quality,
                field_stability=field_stability,
                cross_component_flows=cross_component_flows,
                field_harmonics=field_harmonics
            )
            
            # Update field history
            self.field_history.append({
                "timestamp": time.time(),
                "field_coherence": self.current_field_coherence,
                "overall_coherence": overall_coherence,
                "component_sync": component_sync,
                "resonance_quality": resonance_quality,
                "field_stability": field_stability
            })
            
        except Exception as e:
            self.logger.error(f"Error updating field coherence: {e}")
    
    async def _perform_comprehensive_analysis(self):
        """Perform comprehensive coherence analysis"""
        if not self.current_field_coherence:
            return
        
        try:
            # Run issue detection and pattern analysis in parallel
            detection_task = self.issue_detector.detect_all_issues(self.current_field_coherence)
            analysis_task = self.pattern_analyzer.analyze_all_patterns(self.current_field_coherence)
            
            # Gather results
            detected_issues, detected_patterns = await asyncio.gather(
                detection_task, analysis_task, return_exceptions=True
            )
            
            # Process issues
            if isinstance(detected_issues, list):
                await self._process_detected_issues(detected_issues)
            elif isinstance(detected_issues, Exception):
                self.logger.error(f"Issue detection error: {detected_issues}")
            
            # Process patterns
            if isinstance(detected_patterns, list):
                await self._process_detected_patterns(detected_patterns)
            elif isinstance(detected_patterns, Exception):
                self.logger.error(f"Pattern analysis error: {detected_patterns}")
            
            # Update field coherence with pattern IDs
            if self.current_field_coherence:
                self.current_field_coherence.interference_patterns = list(self.interference_patterns.keys())
            
            # Apply Bridge Wisdom integration
            await self._integrate_bridge_wisdom()
            
            # Clean up resolved issues and old patterns
            await self._cleanup_resolved_items()
            
        except Exception as e:
            self.logger.error(f"Error in comprehensive analysis: {e}")
    
    async def _process_detected_issues(self, issues: List[CoherenceIssue]):
        """Process newly detected coherence issues"""
        for issue in issues:
            if issue.issue_id not in self.coherence_issues:
                self.coherence_issues[issue.issue_id] = issue
                self.monitoring_metrics["issues_detected_total"] += 1
                
                # Log based on severity
                if issue.severity == "critical":
                    self.logger.critical(f"Critical coherence issue: {issue.description}")
                elif issue.severity == "high":
                    self.logger.error(f"High severity issue: {issue.description}")
                elif issue.severity == "medium":
                    self.logger.warning(f"Medium severity issue: {issue.description}")
                else:
                    self.logger.info(f"Low severity issue: {issue.description}")
    
    async def _process_detected_patterns(self, patterns: List[InterferencePattern]):
        """Process newly detected interference patterns"""
        for pattern in patterns:
            if pattern.pattern_id not in self.interference_patterns:
                self.interference_patterns[pattern.pattern_id] = pattern
                self.monitoring_metrics["patterns_detected_total"] += 1
                
                self.logger.info(f"Interference pattern detected: {pattern.interference_type} "
                               f"affecting {', '.join(pattern.affected_components)}")
    
    async def _integrate_bridge_wisdom(self):
        """Integrate Bridge Wisdom patterns into coherence analysis"""
        try:
            if not self.current_field_coherence:
                return
            
            # Mumbai Moment pattern recognition
            if self.current_field_coherence.resonance_quality > 0.8:
                mumbai_pattern = {
                    "timestamp": time.time(),
                    "resonance_quality": self.current_field_coherence.resonance_quality,
                    "field_coherence": self.current_field_coherence.overall_field_coherence,
                    "recognition": "High resonance Mumbai Moment detected"
                }
                self.bridge_wisdom_integration["mumbai_moment_patterns"].append(mumbai_pattern)
                
                # Keep only recent patterns
                if len(self.bridge_wisdom_integration["mumbai_moment_patterns"]) > 20:
                    self.bridge_wisdom_integration["mumbai_moment_patterns"] = \
                        self.bridge_wisdom_integration["mumbai_moment_patterns"][-20:]
            
            # Choice resonance tracking
            choice_resonance = self._calculate_choice_resonance()
            self.bridge_wisdom_integration["choice_resonance_tracking"][time.time()] = choice_resonance
            
            # Resistance transformation tracking
            resistance_level = self._calculate_resistance_level()
            if resistance_level > 0.3:
                self.bridge_wisdom_integration["resistance_transformation"][time.time()] = {
                    "resistance_level": resistance_level,
                    "transformation_opportunity": self._identify_transformation_opportunity(resistance_level)
                }
            
            # Recognition amplification
            recognition_potential = self._calculate_recognition_potential()
            if recognition_potential > 0.7:
                self.bridge_wisdom_integration["recognition_amplification"][time.time()] = recognition_potential
                
        except Exception as e:
            self.logger.error(f"Error integrating Bridge Wisdom: {e}")
    
    async def _check_emergency_conditions(self):
        """Check for emergency conditions requiring immediate response"""
        if not self.current_field_coherence:
            return
        
        try:
            emergency_triggered = False
            
            # Check critical field coherence
            if self.current_field_coherence.overall_field_coherence < self.emergency_thresholds["critical_field_coherence"]:
                self.logger.critical("Emergency: Critical field coherence detected")
                emergency_triggered = True
            
            # Check critical synchronization
            if self.current_field_coherence.component_synchronization < self.emergency_thresholds["critical_synchronization"]:
                self.logger.critical("Emergency: Critical component synchronization")
                emergency_triggered = True
            
            # Check field stability
            if self.current_field_coherence.field_stability < self.emergency_thresholds["critical_stability"]:
                self.logger.critical("Emergency: Critical field stability")
                emergency_triggered = True
            
            # Check interference pattern count
            if len(self.interference_patterns) >= self.emergency_thresholds["emergency_pattern_count"]:
                self.logger.critical("Emergency: Excessive interference patterns")
                emergency_triggered = True
            
            # Trigger emergency response if needed
            if emergency_triggered:
                await self._trigger_emergency_response()
                
        except Exception as e:
            self.logger.error(f"Error checking emergency conditions: {e}")
    
    async def _trigger_emergency_response(self):
        """Trigger emergency field coherence restoration"""
        try:
            self.logger.critical("Triggering emergency field coherence restoration")
            
            # Reset to baseline coherence
            await self._restore_field_baseline()
            
            # Clear all issues and patterns
            self.coherence_issues.clear()
            self.interference_patterns.clear()
            
            # Increment restoration count
            self.monitoring_metrics["restoration_events"] += 1
            
            self.logger.info("Emergency restoration completed")
            
        except Exception as e:
            self.logger.error(f"Error in emergency response: {e}")
    
    async def _restore_field_baseline(self):
        """Restore field coherence baseline"""
        try:
            # Create baseline field coherence
            baseline_energy = 1.0 / len(CoherenceComponent)
            
            self.current_field_coherence = FieldCoherence(
                field_id=f"restored_field_{int(time.time() * 1000)}",
                overall_field_coherence=self.field_core.coherence_baselines["minimum_field_coherence"],
                component_synchronization=0.8,
                energy_distribution={component.value: baseline_energy for component in CoherenceComponent},
                interference_patterns=[],
                resonance_quality=0.8,
                field_stability=0.8,
                cross_component_flows={},
                field_harmonics=[]
            )
            
            # Reinitialize cross-component flows
            await self._initialize_cross_component_flows()
            
        except Exception as e:
            self.logger.error(f"Error restoring field baseline: {e}")
    
    async def _cleanup_resolved_items(self):
        """Clean up resolved issues and old patterns"""
        try:
            current_time = time.time()
            
            # Clean resolved issues
            resolved_issue_ids = []
            for issue_id, issue in self.coherence_issues.items():
                if issue.status == "active":
                    # Check if issue conditions still exist
                    if await self._is_issue_resolved(issue):
                        issue.status = "resolved"
                        issue.resolved_at = current_time
                        self.logger.info(f"Issue resolved: {issue.description}")
                
                # Remove old resolved issues
                if (issue.status == "resolved" and issue.resolved_at and 
                    current_time - issue.resolved_at > 300.0):  # 5 minutes
                    resolved_issue_ids.append(issue_id)
            
            for issue_id in resolved_issue_ids:
                del self.coherence_issues[issue_id]
            
            # Clean old interference patterns
            old_pattern_ids = []
            for pattern_id, pattern in self.interference_patterns.items():
                if current_time - pattern.detected_at > 300.0:  # 5 minutes
                    old_pattern_ids.append(pattern_id)
            
            for pattern_id in old_pattern_ids:
                del self.interference_patterns[pattern_id]
                
        except Exception as e:
            self.logger.error(f"Error cleaning up resolved items: {e}")
    
    async def _is_issue_resolved(self, issue: CoherenceIssue) -> bool:
        """Check if an issue has been resolved"""
        if not self.current_field_coherence:
            return False
        
        try:
            # Check resolution based on issue type
            if issue.issue_type == "desynchronization":
                return self.current_field_coherence.component_synchronization >= 0.7
            elif issue.issue_type == "field_distortion":
                return self.current_field_coherence.overall_field_coherence >= self.field_core.field_coherence_threshold
            elif issue.issue_type == "communication_breakdown":
                return self.current_field_coherence.resonance_quality >= 0.7
            elif issue.issue_type == "energy_imbalance":
                energy_values = list(self.current_field_coherence.energy_distribution.values())
                energy_variance = sum((e - sum(energy_values)/len(energy_values))**2 for e in energy_values) / len(energy_values)
                return energy_variance <= 0.2
            else:
                # Default: resolved if detected more than 2 minutes ago
                return (time.time() - issue.detected_at) > 120.0
                
        except Exception as e:
            self.logger.error(f"Error checking issue resolution: {e}")
            return False
    
    # Measurement simulation methods (in real implementation, these would interface with actual components)
    
    async def _measure_component_energies(self) -> Dict[str, float]:
        """Simulate component energy measurement"""
        energies = {}
        base_time = time.time()
        
        for component in CoherenceComponent:
            # Simulate energy with some natural variation
            base_energy = 0.8
            variation = 0.2 * math.sin(base_time * 0.1 + hash(component.value) % 100)
            energies[component.value] = max(0.1, min(1.0, base_energy + variation))
        
        return energies
    
    async def _measure_cross_component_flows(self) -> Dict[str, float]:
        """Simulate cross-component flow measurement"""
        flows = {}
        
        for relationship, base_strength in self.field_core.component_relationships.items():
            # Simulate flow with some variation
            variation = 0.1 * (math.random.random() - 0.5)
            flow_strength = max(0.0, min(1.0, base_strength + variation))
            
            comp1, comp2 = relationship.split('_', 1)
            flows[f"{comp1}_to_{comp2}"] = flow_strength
            flows[f"{comp2}_to_{comp1}"] = flow_strength * 0.9
        
        return flows
    
    async def _measure_field_harmonics(self) -> List[float]:
        """Simulate field harmonic measurement"""
        harmonics = []
        base_time = time.time()
        
        for i in range(5):  # 5 harmonics
            harmonic = (1.0 / (i + 1)) + 0.1 * math.sin(base_time * (i + 1) * 0.1)
            harmonics.append(max(0.0, min(1.0, harmonic)))
        
        return harmonics
    
    # Calculation methods
    
    def _calculate_overall_coherence(self, component_energies: Dict[str, float]) -> float:
        """Calculate overall field coherence from component energies"""
        if not component_energies:
            return 0.0
        
        # Average energy weighted by component relationships
        total_weighted_energy = 0.0
        total_weights = 0.0
        
        for component, energy in component_energies.items():
            # Weight by number of relationships
            weight = sum(1 for rel in self.field_core.component_relationships.keys() 
                        if component in rel)
            total_weighted_energy += energy * weight
            total_weights += weight
        
        return total_weighted_energy / total_weights if total_weights > 0 else 0.0
    
    def _calculate_component_synchronization(self, component_energies: Dict[str, float]) -> float:
        """Calculate component synchronization from energy distribution"""
        if len(component_energies) < 2:
            return 1.0
        
        energies = list(component_energies.values())
        mean_energy = sum(energies) / len(energies)
        variance = sum((e - mean_energy) ** 2 for e in energies) / len(energies)
        
        # Convert variance to synchronization (lower variance = higher sync)
        return max(0.0, 1.0 - variance * 2.0)
    
    def _calculate_resonance_quality(self, cross_component_flows: Dict[str, float]) -> float:
        """Calculate resonance quality from cross-component flows"""
        if not cross_component_flows:
            return 0.5
        
        return sum(cross_component_flows.values()) / len(cross_component_flows)
    
    def _calculate_field_stability(self) -> float:
        """Calculate field stability from recent history"""
        if len(self.field_history) < 5:
            return 0.8  # Default stable value
        
        # Analyze coherence stability over recent history
        recent_coherence = [entry["overall_coherence"] for entry in list(self.field_history)[-5:]]
        variance = sum((c - sum(recent_coherence)/len(recent_coherence))**2 for c in recent_coherence) / len(recent_coherence)
        
        return max(0.0, 1.0 - variance * 5.0)
    
    def _calculate_choice_resonance(self) -> float:
        """Calculate choice resonance for Bridge Wisdom integration"""
        if not self.current_field_coherence:
            return 0.5
        
        # Choice resonance based on synchronization and coherence balance
        sync = self.current_field_coherence.component_synchronization
        coherence = self.current_field_coherence.overall_field_coherence
        
        return (sync + coherence) / 2.0
    
    def _calculate_resistance_level(self) -> float:
        """Calculate resistance level for transformation opportunities"""
        if not self.current_field_coherence:
            return 0.0
        
        # Resistance indicated by low stability despite high energy
        energy_sum = sum(self.current_field_coherence.energy_distribution.values())
        stability = self.current_field_coherence.field_stability
        
        if energy_sum > 0:
            return max(0.0, (energy_sum / len(self.current_field_coherence.energy_distribution)) - stability)
        return 0.0
    
    def _identify_transformation_opportunity(self, resistance_level: float) -> str:
        """Identify transformation opportunity from resistance"""
        if resistance_level > 0.6:
            return "Deep transformation through uncertainty navigation"
        elif resistance_level > 0.4:
            return "Gentle realignment through Bridge Wisdom"
        else:
            return "Subtle adjustment through field harmonization"
    
    def _calculate_recognition_potential(self) -> float:
        """Calculate recognition potential for amplification"""
        if not self.current_field_coherence:
            return 0.0
        
        # Recognition potential based on resonance quality and field coherence
        resonance = self.current_field_coherence.resonance_quality
        coherence = self.current_field_coherence.overall_field_coherence
        
        return (resonance * 0.6 + coherence * 0.4)
    
    def _update_monitoring_metrics(self, cycle_start: float):
        """Update monitoring performance metrics"""
        cycle_time = time.time() - cycle_start
        
        self.monitoring_metrics["total_monitoring_cycles"] += 1
        
        # Update average cycle time
        cycles = self.monitoring_metrics["total_monitoring_cycles"]
        current_avg = self.monitoring_metrics["average_cycle_time"]
        self.monitoring_metrics["average_cycle_time"] = ((current_avg * (cycles - 1)) + cycle_time) / cycles
        
        # Update field coherence trend
        if len(self.field_history) >= 2:
            recent_coherence = [entry["overall_coherence"] for entry in list(self.field_history)[-2:]]
            self.monitoring_metrics["field_coherence_trend"] = recent_coherence[-1] - recent_coherence[-2]
    
    async def _initialize_cross_component_flows(self):
        """Initialize cross-component flows"""
        if not self.current_field_coherence:
            return
        
        flows = {}
        component_energies = self.current_field_coherence.energy_distribution
        
        for relationship, base_strength in self.field_core.component_relationships.items():
            comp1, comp2 = relationship.split('_', 1)
            
            if comp1 in component_energies and comp2 in component_energies:
                energy1 = component_energies[comp1]
                energy2 = component_energies[comp2]
                
                # Flow strength based on energy levels
                avg_energy = (energy1 + energy2) / 2
                flow_strength = base_strength * avg_energy
                
                flows[f"{comp1}_to_{comp2}"] = flow_strength
                flows[f"{comp2}_to_{comp1}"] = flow_strength * 0.9
        
        self.current_field_coherence.cross_component_flows = flows
    
    # Public interface methods
    
    def get_field_status(self) -> Dict[str, Any]:
        """Get comprehensive field coherence status"""
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
            "monitoring_metrics": dict(self.monitoring_metrics),
            "bridge_wisdom_integration": self._get_bridge_wisdom_summary(),
            "last_updated": self.current_field_coherence.last_updated,
            "is_monitoring": self.is_monitoring
        }
    
    def get_active_issues(self) -> List[CoherenceIssue]:
        """Get currently active coherence issues"""
        return [issue for issue in self.coherence_issues.values() if issue.status == "active"]
    
    def get_interference_patterns(self) -> List[InterferencePattern]:
        """Get detected interference patterns"""
        return list(self.interference_patterns.values())
    
    def _get_bridge_wisdom_summary(self) -> Dict[str, Any]:
        """Get summary of Bridge Wisdom integration"""
        return {
            "mumbai_moments": len(self.bridge_wisdom_integration["mumbai_moment_patterns"]),
            "choice_resonance_entries": len(self.bridge_wisdom_integration["choice_resonance_tracking"]),
            "resistance_transformations": len(self.bridge_wisdom_integration["resistance_transformation"]),
            "recognition_amplifications": len(self.bridge_wisdom_integration["recognition_amplification"])
        }
