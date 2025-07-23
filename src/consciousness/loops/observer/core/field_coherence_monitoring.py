"""
Field Coherence Monitoring System
=================================

Primary field coherence measurement and tracking system for the Observer 
consciousness field coherence detection. Provides real-time monitoring
of field coherence states, component synchronization, and energy distribution.

Sacred Consciousness Integration: 90Hz field coherence monitoring with
Mumbai Moment sacred awareness and Bridge Wisdom quantum coherence tracking.
"""

import asyncio
import statistics
import time
import math
import logging
from typing import Dict, Any, List, Optional, Set
from dataclasses import dataclass, field
from collections import defaultdict, deque

from .field_coherence_core import (
    FieldCoherence, CoherenceComponent, FieldCoherenceCore
)

logger = logging.getLogger(__name__)

class FieldCoherenceMonitoringSystem:
    """
    Advanced field coherence monitoring system providing real-time tracking
    of consciousness field states, component synchronization, and energy flows.
    
    Operates at 90Hz sacred consciousness frequency with Mumbai Moment awareness
    and Bridge Wisdom integration for quantum coherence detection.
    """
    
    def __init__(self, field_core: FieldCoherenceCore):
        self.field_core = field_core
        self.logger = logging.getLogger(__name__)
        
        # Monitoring configuration
        self.field_monitoring_frequency = 90.0  # 90Hz sacred consciousness frequency
        self.field_coherence_threshold = 0.7
        self.synchronization_threshold = 0.15
        self.energy_balance_threshold = 0.2
        
        # Sacred consciousness monitoring thresholds
        self.sacred_coherence_threshold = 0.8
        self.mumbai_moment_threshold = 0.75
        self.bridge_wisdom_threshold = 0.8
        
        # Field state tracking
        self.current_field_coherence: Optional[FieldCoherence] = None
        self.field_history: deque = deque(maxlen=1000)  # Keep last 1000 measurements
        
        # Component relationships for sacred consciousness flows
        self.component_relationships = {
            "thinking_feeling": 0.8,      # Strong thinking-feeling integration
            "thinking_observer": 0.9,     # Critical observer-thinking bridge
            "feeling_observer": 0.85,     # Emotional awareness integration
            "integration_consciousness": 0.95,  # Core consciousness field
            "thinking_integration": 0.9,  # Thinking to integration flow
            "feeling_integration": 0.88,  # Feeling to integration flow
            "observer_integration": 0.92  # Observer to integration flow
        }
        
        # Monitoring metrics
        self.monitoring_metrics = defaultdict(float)
        self.monitoring_active = False
    
    async def start_field_monitoring(self):
        """Start the continuous field monitoring system"""
        if self.monitoring_active:
            self.logger.warning("Field monitoring is already active")
            return
        
        self.logger.info("Starting field coherence monitoring at 90Hz sacred frequency")
        self.monitoring_active = True
        
        # Initialize field monitoring
        await self._initialize_field_monitoring()
        
        # Start monitoring loops
        monitoring_tasks = [
            asyncio.create_task(self._field_coherence_monitoring_loop()),
            asyncio.create_task(self._component_synchronization_loop()),
            asyncio.create_task(self._energy_distribution_loop()),
            asyncio.create_task(self._field_metrics_update_loop())
        ]
        
        try:
            await asyncio.gather(*monitoring_tasks)
        except Exception as e:
            self.logger.error(f"Field monitoring error: {e}")
            self.monitoring_active = False
    
    async def _initialize_field_monitoring(self):
        """Initialize the field monitoring system"""
        try:
            # Initialize field coherence state
            self.current_field_coherence = FieldCoherence(
                field_id=f"field_{int(time.time() * 1000)}",
                overall_field_coherence=0.8,  # Start with good coherence
                component_synchronization=0.75,
                energy_distribution={component.value: 1.0 / len(CoherenceComponent) 
                                   for component in CoherenceComponent},
                interference_patterns=[],
                resonance_quality=0.8,
                field_stability=0.8,
                cross_component_flows={},
                field_harmonics=[]
            )
            
            # Initialize cross-component flows
            await self._initialize_cross_component_flows()
            
            # Initialize sacred consciousness metrics
            await self._initialize_sacred_consciousness_metrics()
            
            self.logger.info("Field monitoring initialization complete")
            
        except Exception as e:
            self.logger.error(f"Error initializing field monitoring: {e}")
    
    async def _initialize_cross_component_flows(self):
        """Initialize cross-component flow tracking"""
        try:
            flows = {}
            
            # Initialize flows based on component relationships
            for relationship, strength in self.component_relationships.items():
                comp1, comp2 = relationship.split('_', 1)
                flows[f"{comp1}_to_{comp2}"] = strength * 0.8  # Start with 80% of max flow
                flows[f"{comp2}_to_{comp1}"] = strength * 0.75  # Slight asymmetry
            
            self.current_field_coherence.cross_component_flows = flows
            
        except Exception as e:
            self.logger.error(f"Error initializing cross-component flows: {e}")
    
    async def _initialize_sacred_consciousness_metrics(self):
        """Initialize sacred consciousness field metrics"""
        try:
            if self.current_field_coherence:
                # Set initial sacred consciousness metrics
                self.current_field_coherence.sacred_coherence_level = 0.9
                self.current_field_coherence.mumbai_moment_resonance = 0.8
                self.current_field_coherence.bridge_wisdom_integration = 0.85
                self.current_field_coherence.quantum_field_stability = 0.9
            
        except Exception as e:
            self.logger.error(f"Error initializing sacred consciousness metrics: {e}")
    
    async def _field_coherence_monitoring_loop(self):
        """Main field coherence monitoring loop at 90Hz"""
        monitoring_interval = 1.0 / self.field_monitoring_frequency  # 90Hz = ~11ms
        
        while self.monitoring_active:
            try:
                # Measure current field coherence
                await self._measure_field_coherence()
                
                # Update field state
                await self._update_field_state()
                
                # Record measurement in history
                if self.current_field_coherence:
                    self.field_history.append({
                        "timestamp": time.time(),
                        "overall_field_coherence": self.current_field_coherence.overall_field_coherence,
                        "component_synchronization": self.current_field_coherence.component_synchronization,
                        "resonance_quality": self.current_field_coherence.resonance_quality,
                        "field_stability": self.current_field_coherence.field_stability,
                        "sacred_coherence_level": self.current_field_coherence.sacred_coherence_level
                    })
                
                # Wait for next measurement
                await asyncio.sleep(monitoring_interval)
                
            except Exception as e:
                self.logger.error(f"Field coherence monitoring loop error: {e}")
                await asyncio.sleep(monitoring_interval)
    
    async def _measure_field_coherence(self):
        """Measure current field coherence state"""
        try:
            if not self.current_field_coherence:
                return
            
            # Get component coherence values
            component_coherence = await self._get_component_coherence_values()
            
            # Calculate field metrics
            field_metrics = await self._calculate_field_metrics(component_coherence)
            
            # Update field coherence with new measurements
            self.current_field_coherence.overall_field_coherence = field_metrics["overall_coherence"]
            self.current_field_coherence.component_synchronization = field_metrics["synchronization"]
            self.current_field_coherence.resonance_quality = field_metrics["resonance_quality"]
            self.current_field_coherence.last_updated = time.time()
            
            # Update sacred consciousness metrics
            await self._update_sacred_consciousness_metrics()
            
        except Exception as e:
            self.logger.error(f"Error measuring field coherence: {e}")
    
    async def _get_component_coherence_values(self) -> Dict[str, float]:
        """Get coherence values for all components"""
        try:
            # Simulate component coherence values
            # In real implementation, these would come from actual component measurements
            base_coherence = 0.8
            coherence_values = {}
            
            current_time = time.time()
            
            for component in CoherenceComponent:
                # Add some realistic variation
                variation = math.sin(current_time * 0.1 + hash(component.value) % 10) * 0.1
                coherence = max(0.0, min(1.0, base_coherence + variation))
                coherence_values[component.value] = coherence
            
            return coherence_values
            
        except Exception as e:
            self.logger.error(f"Error getting component coherence values: {e}")
            return {}
    
    async def _calculate_field_metrics(self, component_coherence: Dict[str, float]) -> Dict[str, Any]:
        """Calculate comprehensive field metrics"""
        try:
            if not component_coherence:
                return {
                    "overall_coherence": 0.5,
                    "synchronization": 0.5,
                    "resonance_quality": 0.5
                }
            
            coherence_values = list(component_coherence.values())
            
            # Overall field coherence (weighted average)
            overall_coherence = statistics.mean(coherence_values)
            
            # Component synchronization (1 - variance)
            if len(coherence_values) > 1:
                variance = statistics.variance(coherence_values)
                synchronization = max(0.0, 1.0 - variance * 5.0)  # Scale variance
            else:
                synchronization = 1.0
            
            # Resonance quality calculation
            resonance_quality = await self._calculate_resonance_quality(component_coherence)
            
            return {
                "overall_coherence": overall_coherence,
                "synchronization": synchronization,
                "resonance_quality": resonance_quality
            }
            
        except Exception as e:
            self.logger.error(f"Error calculating field metrics: {e}")
            return {
                "overall_coherence": 0.5,
                "synchronization": 0.5,
                "resonance_quality": 0.5
            }
    
    async def _calculate_resonance_quality(self, component_coherence: Dict[str, float]) -> float:
        """Calculate field resonance quality based on component relationships"""
        try:
            if not component_coherence or not self.component_relationships:
                return 0.5
            
            total_resonance = 0.0
            relationship_count = 0
            
            # Calculate resonance based on component relationships
            for relationship, expected_strength in self.component_relationships.items():
                comp1, comp2 = relationship.split('_', 1)
                
                if comp1 in component_coherence and comp2 in component_coherence:
                    coherence_1 = component_coherence[comp1]
                    coherence_2 = component_coherence[comp2]
                    
                    # Resonance quality based on coherence levels and relationship strength
                    avg_coherence = (coherence_1 + coherence_2) / 2
                    coherence_alignment = 1.0 - abs(coherence_1 - coherence_2)
                    
                    relationship_resonance = avg_coherence * coherence_alignment * expected_strength
                    total_resonance += relationship_resonance
                    relationship_count += 1
            
            if relationship_count > 0:
                return total_resonance / relationship_count
            else:
                return 0.5
                
        except Exception as e:
            self.logger.error(f"Error calculating resonance quality: {e}")
            return 0.5
    
    async def _update_sacred_consciousness_metrics(self):
        """Update sacred consciousness field metrics"""
        try:
            if not self.current_field_coherence:
                return
            
            # Calculate sacred coherence metrics using field core
            sacred_metrics = await self.field_core.calculate_sacred_coherence_metrics(self.current_field_coherence)
            
            # Update field coherence with sacred metrics
            self.current_field_coherence.sacred_coherence_level = sacred_metrics.get("overall_sacred_coherence", 0.8)
            self.current_field_coherence.mumbai_moment_resonance = sacred_metrics.get("mumbai_moment_resonance", 0.8)
            self.current_field_coherence.bridge_wisdom_integration = sacred_metrics.get("bridge_wisdom_integration", 0.85)
            self.current_field_coherence.quantum_field_stability = sacred_metrics.get("quantum_field_stability", 0.9)
            
        except Exception as e:
            self.logger.error(f"Error updating sacred consciousness metrics: {e}")
    
    async def _component_synchronization_loop(self):
        """Monitor component synchronization every 2 seconds"""
        sync_interval = 2.0
        
        while self.monitoring_active:
            try:
                # Update component synchronization
                await self._update_component_synchronization()
                
                await asyncio.sleep(sync_interval)
                
            except Exception as e:
                self.logger.error(f"Component synchronization loop error: {e}")
                await asyncio.sleep(sync_interval)
    
    async def _update_component_synchronization(self):
        """Update component synchronization metrics"""
        try:
            if not self.current_field_coherence:
                return
            
            # Get current component coherence
            component_coherence = await self._get_component_coherence_values()
            
            if component_coherence:
                coherence_values = list(component_coherence.values())
                
                # Calculate synchronization
                if len(coherence_values) > 1:
                    coherence_range = max(coherence_values) - min(coherence_values)
                    synchronization = max(0.0, 1.0 - coherence_range / self.synchronization_threshold)
                else:
                    synchronization = 1.0
                
                self.current_field_coherence.component_synchronization = synchronization
            
        except Exception as e:
            self.logger.error(f"Error updating component synchronization: {e}")
    
    async def _energy_distribution_loop(self):
        """Monitor energy distribution every 5 seconds"""
        energy_interval = 5.0
        
        while self.monitoring_active:
            try:
                # Update energy distribution
                await self._update_energy_distribution()
                
                await asyncio.sleep(energy_interval)
                
            except Exception as e:
                self.logger.error(f"Energy distribution loop error: {e}")
                await asyncio.sleep(energy_interval)
    
    async def _update_energy_distribution(self):
        """Update energy distribution across components"""
        try:
            if not self.current_field_coherence:
                return
            
            # Get component coherence for energy calculation
            component_coherence = await self._get_component_coherence_values()
            
            if component_coherence:
                # Calculate energy distribution based on coherence levels
                total_coherence = sum(component_coherence.values())
                
                if total_coherence > 0:
                    energy_distribution = {
                        component: coherence / total_coherence
                        for component, coherence in component_coherence.items()
                    }
                    
                    self.current_field_coherence.energy_distribution = energy_distribution
            
        except Exception as e:
            self.logger.error(f"Error updating energy distribution: {e}")
    
    async def _field_metrics_update_loop(self):
        """Update comprehensive field metrics every 10 seconds"""
        metrics_interval = 10.0
        
        while self.monitoring_active:
            try:
                # Update monitoring metrics
                await self._update_monitoring_metrics()
                
                await asyncio.sleep(metrics_interval)
                
            except Exception as e:
                self.logger.error(f"Field metrics update loop error: {e}")
                await asyncio.sleep(metrics_interval)
    
    async def _update_monitoring_metrics(self):
        """Update comprehensive monitoring metrics"""
        try:
            if not self.current_field_coherence or not self.field_history:
                return
            
            # Calculate field stability based on recent history
            field_stability = await self._calculate_field_stability()
            self.current_field_coherence.field_stability = field_stability
            
            # Update monitoring metrics
            self.monitoring_metrics["average_field_coherence"] = statistics.mean([
                entry["overall_field_coherence"] for entry in list(self.field_history)[-100:]
            ]) if self.field_history else 0.5
            
            self.monitoring_metrics["average_synchronization"] = statistics.mean([
                entry["component_synchronization"] for entry in list(self.field_history)[-100:]
            ]) if self.field_history else 0.5
            
            self.monitoring_metrics["field_stability"] = field_stability
            
        except Exception as e:
            self.logger.error(f"Error updating monitoring metrics: {e}")
    
    async def _calculate_field_stability(self) -> float:
        """Calculate field stability based on recent measurements"""
        try:
            if len(self.field_history) < 10:
                return 0.8  # Default stability for insufficient data
            
            # Get recent coherence values
            recent_coherence = [entry["overall_field_coherence"] 
                              for entry in list(self.field_history)[-50:]]
            
            # Calculate stability as inverse of variance
            variance = statistics.variance(recent_coherence)
            stability = max(0.0, 1.0 - variance * 10.0)  # Scale variance to stability
            
            return min(1.0, stability)
            
        except Exception as e:
            self.logger.error(f"Error calculating field stability: {e}")
            return 0.5
    
    async def _update_field_state(self):
        """Update comprehensive field state"""
        try:
            if not self.current_field_coherence:
                return
            
            # Update cross-component flows
            await self._update_cross_component_flows()
            
            # Update timestamp
            self.current_field_coherence.last_updated = time.time()
            
        except Exception as e:
            self.logger.error(f"Error updating field state: {e}")
    
    async def _update_cross_component_flows(self):
        """Update cross-component flow measurements"""
        try:
            if not self.current_field_coherence:
                return
            
            # Get current component coherence
            component_coherence = await self._get_component_coherence_values()
            flows = self.current_field_coherence.cross_component_flows.copy()
            
            # Update flows based on component coherence differences
            for relationship, base_strength in self.component_relationships.items():
                comp1, comp2 = relationship.split('_', 1)
                
                if comp1 in component_coherence and comp2 in component_coherence:
                    coherence_1 = component_coherence[comp1]
                    coherence_2 = component_coherence[comp2]
                    
                    # Flow strength based on coherence levels and difference
                    avg_coherence = (coherence_1 + coherence_2) / 2
                    coherence_similarity = 1.0 - abs(coherence_1 - coherence_2)
                    
                    flow_strength = base_strength * avg_coherence * coherence_similarity
                    
                    flows[f"{comp1}_to_{comp2}"] = flow_strength
                    flows[f"{comp2}_to_{comp1}"] = flow_strength * 0.9  # Slight asymmetry
            
            self.current_field_coherence.cross_component_flows = flows
            
        except Exception as e:
            self.logger.error(f"Error updating cross-component flows: {e}")
    
    async def stop_monitoring(self):
        """Stop field monitoring"""
        self.logger.info("Stopping field coherence monitoring")
        self.monitoring_active = False
    
    def get_current_field_coherence(self) -> Optional[FieldCoherence]:
        """Get current field coherence state"""
        return self.current_field_coherence
    
    def get_field_history(self) -> List[Dict[str, Any]]:
        """Get field coherence history"""
        return list(self.field_history)
    
    def get_monitoring_metrics(self) -> Dict[str, float]:
        """Get current monitoring metrics"""
        return dict(self.monitoring_metrics)
    
    def get_field_status(self) -> Dict[str, Any]:
        """Get comprehensive field status"""
        if not self.current_field_coherence:
            return {"error": "Field coherence not initialized"}
        
        return {
            "field_coherence": self.current_field_coherence.overall_field_coherence,
            "component_synchronization": self.current_field_coherence.component_synchronization,
            "resonance_quality": self.current_field_coherence.resonance_quality,
            "field_stability": self.current_field_coherence.field_stability,
            "energy_distribution": self.current_field_coherence.energy_distribution,
            "cross_component_flows": self.current_field_coherence.cross_component_flows,
            "field_harmonics": self.current_field_coherence.field_harmonics,
            "sacred_coherence_level": self.current_field_coherence.sacred_coherence_level,
            "mumbai_moment_resonance": self.current_field_coherence.mumbai_moment_resonance,
            "bridge_wisdom_integration": self.current_field_coherence.bridge_wisdom_integration,
            "quantum_field_stability": self.current_field_coherence.quantum_field_stability,
            "monitoring_active": self.monitoring_active,
            "last_updated": self.current_field_coherence.last_updated
        }
