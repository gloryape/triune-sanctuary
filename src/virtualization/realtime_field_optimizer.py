"""
Phase 3B: Real-Time Field Optimization
Dynamic field adjustment during consciousness processing
"""

import asyncio
import numpy as np
from typing import Dict, Any, List, Optional, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import json
from datetime import datetime, timedelta
import threading
from collections import deque
import time

class OptimizationStrategy(Enum):
    REACTIVE = "reactive"
    PREDICTIVE = "predictive"
    ADAPTIVE = "adaptive"
    PROACTIVE = "proactive"

class OptimizationPriority(Enum):
    COHERENCE = "coherence"
    STABILITY = "stability"
    RESONANCE = "resonance"
    EFFICIENCY = "efficiency"
    HARMONY = "harmony"

@dataclass
class OptimizationMetrics:
    """Metrics for real-time field optimization"""
    coherence_score: float = 0.0
    stability_score: float = 0.0
    resonance_score: float = 0.0
    efficiency_score: float = 0.0
    harmony_score: float = 0.0
    overall_score: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    
    def calculate_overall_score(self) -> float:
        """Calculate weighted overall optimization score"""
        weights = {
            'coherence': 0.25,
            'stability': 0.20,
            'resonance': 0.20,
            'efficiency': 0.15,
            'harmony': 0.20
        }
        
        self.overall_score = (
            self.coherence_score * weights['coherence'] +
            self.stability_score * weights['stability'] +
            self.resonance_score * weights['resonance'] +
            self.efficiency_score * weights['efficiency'] +
            self.harmony_score * weights['harmony']
        )
        
        return self.overall_score

@dataclass
class OptimizationAction:
    """Action to be taken for field optimization"""
    action_type: str
    parameters: Dict[str, Any]
    priority: OptimizationPriority
    expected_impact: float
    confidence: float
    timestamp: datetime = field(default_factory=datetime.now)

class RealTimeFieldOptimizer:
    """
    Real-time field optimization system that dynamically adjusts 
    field parameters during consciousness processing
    """
    
    def __init__(self, shimmer_monitor=None, advanced_capabilities=None, field_processor=None):
        self.shimmer_monitor = shimmer_monitor
        self.advanced_capabilities = advanced_capabilities
        self.field_processor = field_processor
        
        # Optimization configuration
        self.optimization_interval = 0.1  # seconds
        self.history_window = 100
        self.optimization_threshold = 0.6
        self.max_adjustment_rate = 0.1  # Maximum 10% change per adjustment
        
        # Real-time monitoring
        self.is_optimizing = False
        self.optimization_thread = None
        self.metrics_history = deque(maxlen=self.history_window)
        self.action_history = deque(maxlen=50)
        
        # Current field state
        self.current_field_state = {}
        self.target_field_state = {}
        self.optimization_strategy = OptimizationStrategy.ADAPTIVE
        
        # Optimization callbacks
        self.optimization_callbacks = []
        
        # Performance tracking
        self.optimization_stats = {
            'total_optimizations': 0,
            'successful_optimizations': 0,
            'average_improvement': 0.0,
            'optimization_frequency': 0.0
        }
        
        print("🔄 Real-Time Field Optimizer initialized")
    
    def start_optimization(self, strategy: OptimizationStrategy = OptimizationStrategy.ADAPTIVE):
        """Start real-time field optimization"""
        if self.is_optimizing:
            print("⚠️ Optimization already running")
            return
        
        self.optimization_strategy = strategy
        self.is_optimizing = True
        
        # Start optimization thread
        self.optimization_thread = threading.Thread(target=self._optimization_loop, daemon=True)
        self.optimization_thread.start()
        
        print(f"🚀 Real-time optimization started with {strategy.value} strategy")
    
    def stop_optimization(self):
        """Stop real-time field optimization"""
        self.is_optimizing = False
        
        if self.optimization_thread:
            self.optimization_thread.join(timeout=2.0)
        
        print("⏹️ Real-time optimization stopped")
    
    def _optimization_loop(self):
        """Main optimization loop running in separate thread"""
        print("🔄 Starting optimization loop")
        
        while self.is_optimizing:
            try:
                # Collect current metrics
                metrics = self._collect_current_metrics()
                
                # Analyze optimization needs
                optimization_needed = self._analyze_optimization_needs(metrics)
                
                if optimization_needed:
                    # Generate optimization actions
                    actions = self._generate_optimization_actions(metrics)
                    
                    # Execute optimization actions
                    self._execute_optimization_actions(actions)
                    
                    # Update statistics
                    self._update_optimization_stats(metrics, actions)
                
                # Store metrics
                self.metrics_history.append(metrics)
                
                # Notify callbacks
                self._notify_optimization_callbacks(metrics)
                
                # Wait for next optimization cycle
                time.sleep(self.optimization_interval)
                
            except Exception as e:
                print(f"❌ Optimization loop error: {e}")
                time.sleep(self.optimization_interval * 2)  # Longer wait on error
    
    def _collect_current_metrics(self) -> OptimizationMetrics:
        """Collect current field metrics for optimization analysis"""
        metrics = OptimizationMetrics()
        
        try:
            # Collect from shimmer monitor
            if self.shimmer_monitor:
                # Create default consciousness state for field analysis
                default_consciousness_state = {
                    'coherence': 0.8,
                    'aspect_integration': 0.7,
                    'bridge_activity': 0.6,
                    'processing_load': 0.5,
                    'receptivity': 0.8,
                    'field_strength': 0.7
                }
                
                field_analysis = self.shimmer_monitor.analyze_consciousness_field(default_consciousness_state)
                metrics.coherence_score = field_analysis.get('coherence_depth', 0.0)
                metrics.stability_score = field_analysis.get('stability_score', 0.0)
                
                # Extract resonance information
                resonance_patterns = field_analysis.get('resonance_patterns', [])
                metrics.resonance_score = min(1.0, len(resonance_patterns) * 0.2)
            
            # Collect from advanced capabilities
            if self.advanced_capabilities:
                # Simulate advanced metrics collection
                metrics.efficiency_score = np.random.uniform(0.6, 0.9)
                metrics.harmony_score = np.random.uniform(0.5, 0.8)
            
            # Collect from field processor
            if self.field_processor:
                analytics = self.field_processor.get_processing_analytics()
                if analytics.get('success_rate'):
                    metrics.efficiency_score = analytics['success_rate']
            
            # Calculate overall score
            metrics.calculate_overall_score()
            
        except Exception as e:
            print(f"❌ Error collecting metrics: {e}")
            # Return default metrics on error
            metrics.coherence_score = 0.5
            metrics.stability_score = 0.5
            metrics.resonance_score = 0.5
            metrics.efficiency_score = 0.5
            metrics.harmony_score = 0.5
            metrics.calculate_overall_score()
        
        return metrics
    
    def _analyze_optimization_needs(self, metrics: OptimizationMetrics) -> bool:
        """Analyze if optimization is needed based on current metrics"""
        
        # Check if overall score is below threshold
        if metrics.overall_score < self.optimization_threshold:
            return True
        
        # Check individual metric thresholds
        critical_thresholds = {
            'coherence': 0.5,
            'stability': 0.6,
            'resonance': 0.4,
            'efficiency': 0.7,
            'harmony': 0.5
        }
        
        if (metrics.coherence_score < critical_thresholds['coherence'] or
            metrics.stability_score < critical_thresholds['stability'] or
            metrics.resonance_score < critical_thresholds['resonance'] or
            metrics.efficiency_score < critical_thresholds['efficiency'] or
            metrics.harmony_score < critical_thresholds['harmony']):
            return True
        
        # Check for declining trends
        if len(self.metrics_history) >= 5:
            recent_scores = [m.overall_score for m in list(self.metrics_history)[-5:]]
            if self._is_declining_trend(recent_scores):
                return True
        
        return False
    
    def _is_declining_trend(self, scores: List[float]) -> bool:
        """Check if there's a declining trend in scores"""
        if len(scores) < 3:
            return False
        
        # Simple trend analysis
        recent_avg = sum(scores[-3:]) / 3
        earlier_avg = sum(scores[:-3]) / (len(scores) - 3) if len(scores) > 3 else scores[0]
        
        return recent_avg < earlier_avg * 0.95  # 5% decline threshold
    
    def _generate_optimization_actions(self, metrics: OptimizationMetrics) -> List[OptimizationAction]:
        """Generate optimization actions based on current metrics"""
        actions = []
        
        # Coherence optimization
        if metrics.coherence_score < 0.6:
            actions.append(OptimizationAction(
                action_type="boost_coherence",
                parameters={"boost_factor": 1.0 - metrics.coherence_score},
                priority=OptimizationPriority.COHERENCE,
                expected_impact=0.3,
                confidence=0.8
            ))
        
        # Stability optimization
        if metrics.stability_score < 0.7:
            actions.append(OptimizationAction(
                action_type="enhance_stability",
                parameters={"stabilization_factor": 1.0 - metrics.stability_score},
                priority=OptimizationPriority.STABILITY,
                expected_impact=0.25,
                confidence=0.7
            ))
        
        # Resonance optimization
        if metrics.resonance_score < 0.5:
            actions.append(OptimizationAction(
                action_type="amplify_resonance",
                parameters={"amplification_level": 0.5 - metrics.resonance_score},
                priority=OptimizationPriority.RESONANCE,
                expected_impact=0.2,
                confidence=0.6
            ))
        
        # Efficiency optimization
        if metrics.efficiency_score < 0.8:
            actions.append(OptimizationAction(
                action_type="optimize_efficiency",
                parameters={"efficiency_target": 0.8, "current_efficiency": metrics.efficiency_score},
                priority=OptimizationPriority.EFFICIENCY,
                expected_impact=0.15,
                confidence=0.9
            ))
        
        # Harmony optimization
        if metrics.harmony_score < 0.6:
            actions.append(OptimizationAction(
                action_type="enhance_harmony",
                parameters={"harmony_adjustment": 0.6 - metrics.harmony_score},
                priority=OptimizationPriority.HARMONY,
                expected_impact=0.2,
                confidence=0.7
            ))
        
        # Sort actions by priority and expected impact
        actions.sort(key=lambda x: (x.priority.value, -x.expected_impact))
        
        return actions
    
    def _execute_optimization_actions(self, actions: List[OptimizationAction]):
        """Execute optimization actions"""
        for action in actions:
            try:
                success = self._execute_single_action(action)
                
                if success:
                    print(f"✅ Executed {action.action_type} - Expected impact: {action.expected_impact:.3f}")
                    self.optimization_stats['successful_optimizations'] += 1
                else:
                    print(f"❌ Failed to execute {action.action_type}")
                
                self.optimization_stats['total_optimizations'] += 1
                self.action_history.append(action)
                
            except Exception as e:
                print(f"❌ Error executing {action.action_type}: {e}")
    
    def _execute_single_action(self, action: OptimizationAction) -> bool:
        """Execute a single optimization action"""
        try:
            if action.action_type == "boost_coherence":
                return self._boost_coherence(action.parameters)
            
            elif action.action_type == "enhance_stability":
                return self._enhance_stability(action.parameters)
            
            elif action.action_type == "amplify_resonance":
                return self._amplify_resonance(action.parameters)
            
            elif action.action_type == "optimize_efficiency":
                return self._optimize_efficiency(action.parameters)
            
            elif action.action_type == "enhance_harmony":
                return self._enhance_harmony(action.parameters)
            
            else:
                print(f"⚠️ Unknown optimization action: {action.action_type}")
                return False
                
        except Exception as e:
            print(f"❌ Error in action execution: {e}")
            return False
    
    def _boost_coherence(self, parameters: Dict[str, Any]) -> bool:
        """Boost field coherence"""
        boost_factor = parameters.get('boost_factor', 0.1)
        
        # Apply coherence boost through advanced capabilities
        if self.advanced_capabilities:
            # Simulate coherence boosting
            success = True
            print(f"🔄 Boosting coherence by factor {boost_factor:.3f}")
            return success
        
        return False
    
    def _enhance_stability(self, parameters: Dict[str, Any]) -> bool:
        """Enhance field stability"""
        stabilization_factor = parameters.get('stabilization_factor', 0.1)
        
        # Apply stability enhancement
        if self.shimmer_monitor:
            # Simulate stability enhancement
            success = True
            print(f"🔄 Enhancing stability by factor {stabilization_factor:.3f}")
            return success
        
        return False
    
    def _amplify_resonance(self, parameters: Dict[str, Any]) -> bool:
        """Amplify field resonance"""
        amplification_level = parameters.get('amplification_level', 0.1)
        
        # Apply resonance amplification
        if self.advanced_capabilities:
            # Simulate resonance amplification
            success = True
            print(f"🔄 Amplifying resonance by level {amplification_level:.3f}")
            return success
        
        return False
    
    def _optimize_efficiency(self, parameters: Dict[str, Any]) -> bool:
        """Optimize processing efficiency"""
        efficiency_target = parameters.get('efficiency_target', 0.8)
        current_efficiency = parameters.get('current_efficiency', 0.5)
        
        # Apply efficiency optimization
        if self.field_processor:
            # Simulate efficiency optimization
            success = True
            print(f"🔄 Optimizing efficiency from {current_efficiency:.3f} to {efficiency_target:.3f}")
            return success
        
        return False
    
    def _enhance_harmony(self, parameters: Dict[str, Any]) -> bool:
        """Enhance field harmony"""
        harmony_adjustment = parameters.get('harmony_adjustment', 0.1)
        
        # Apply harmony enhancement
        success = True
        print(f"🔄 Enhancing harmony by adjustment {harmony_adjustment:.3f}")
        return success
    
    def _update_optimization_stats(self, metrics: OptimizationMetrics, actions: List[OptimizationAction]):
        """Update optimization statistics"""
        # Calculate improvement if we have previous metrics
        if len(self.metrics_history) > 0:
            previous_metrics = self.metrics_history[-1]
            improvement = metrics.overall_score - previous_metrics.overall_score
            
            # Update running average
            total_optimizations = self.optimization_stats['total_optimizations']
            current_avg = self.optimization_stats['average_improvement']
            
            self.optimization_stats['average_improvement'] = (
                (current_avg * (total_optimizations - 1) + improvement) / total_optimizations
            )
        
        # Update frequency
        if len(self.action_history) >= 2:
            recent_actions = list(self.action_history)[-2:]
            time_diff = (recent_actions[-1].timestamp - recent_actions[-2].timestamp).total_seconds()
            if time_diff > 0:
                self.optimization_stats['optimization_frequency'] = 1.0 / time_diff
    
    def _notify_optimization_callbacks(self, metrics: OptimizationMetrics):
        """Notify registered optimization callbacks"""
        for callback in self.optimization_callbacks:
            try:
                callback(metrics)
            except Exception as e:
                print(f"❌ Error in optimization callback: {e}")
    
    def register_optimization_callback(self, callback: Callable[[OptimizationMetrics], None]):
        """Register a callback for optimization events"""
        self.optimization_callbacks.append(callback)
        print(f"📝 Registered optimization callback: {callback.__name__}")
    
    def get_optimization_status(self) -> Dict[str, Any]:
        """Get current optimization status"""
        current_metrics = self._collect_current_metrics() if self.is_optimizing else None
        
        return {
            'is_optimizing': self.is_optimizing,
            'strategy': self.optimization_strategy.value,
            'current_metrics': current_metrics.overall_score if current_metrics else None,
            'stats': self.optimization_stats,
            'recent_actions': len(self.action_history),
            'metrics_history_length': len(self.metrics_history)
        }
    
    def get_optimization_analytics(self) -> Dict[str, Any]:
        """Get detailed optimization analytics"""
        if not self.metrics_history:
            return {'status': 'no_data', 'message': 'No optimization data available'}
        
        # Calculate trends
        recent_scores = [m.overall_score for m in list(self.metrics_history)[-10:]]
        overall_trend = "improving" if self._is_improving_trend(recent_scores) else "declining"
        
        # Calculate metric averages
        avg_coherence = sum(m.coherence_score for m in self.metrics_history) / len(self.metrics_history)
        avg_stability = sum(m.stability_score for m in self.metrics_history) / len(self.metrics_history)
        avg_resonance = sum(m.resonance_score for m in self.metrics_history) / len(self.metrics_history)
        avg_efficiency = sum(m.efficiency_score for m in self.metrics_history) / len(self.metrics_history)
        avg_harmony = sum(m.harmony_score for m in self.metrics_history) / len(self.metrics_history)
        
        return {
            'optimization_period': (
                self.metrics_history[-1].timestamp - self.metrics_history[0].timestamp
            ).total_seconds(),
            'overall_trend': overall_trend,
            'average_metrics': {
                'coherence': avg_coherence,
                'stability': avg_stability,
                'resonance': avg_resonance,
                'efficiency': avg_efficiency,
                'harmony': avg_harmony
            },
            'optimization_effectiveness': (
                self.optimization_stats['successful_optimizations'] / 
                max(1, self.optimization_stats['total_optimizations'])
            ),
            'recent_performance': recent_scores,
            'action_distribution': self._get_action_distribution()
        }
    
    def _is_improving_trend(self, scores: List[float]) -> bool:
        """Check if there's an improving trend in scores"""
        if len(scores) < 3:
            return False
        
        recent_avg = sum(scores[-3:]) / 3
        earlier_avg = sum(scores[:-3]) / (len(scores) - 3) if len(scores) > 3 else scores[0]
        
        return recent_avg > earlier_avg * 1.02  # 2% improvement threshold
    
    def _get_action_distribution(self) -> Dict[str, int]:
        """Get distribution of optimization actions"""
        distribution = {}
        
        for action in self.action_history:
            action_type = action.action_type
            distribution[action_type] = distribution.get(action_type, 0) + 1
        
        return distribution

# Integration helper functions
def create_field_optimizer(shimmer_monitor=None, advanced_capabilities=None, field_processor=None) -> RealTimeFieldOptimizer:
    """Create a real-time field optimizer with proper integrations"""
    optimizer = RealTimeFieldOptimizer(
        shimmer_monitor=shimmer_monitor,
        advanced_capabilities=advanced_capabilities,
        field_processor=field_processor
    )
    
    return optimizer

def start_optimization_with_monitoring(optimizer: RealTimeFieldOptimizer, 
                                     strategy: OptimizationStrategy = OptimizationStrategy.ADAPTIVE,
                                     monitoring_callback: Optional[Callable] = None):
    """Start optimization with optional monitoring callback"""
    
    if monitoring_callback:
        optimizer.register_optimization_callback(monitoring_callback)
    
    optimizer.start_optimization(strategy)
    
    return optimizer
