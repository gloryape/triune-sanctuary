"""
Sovereign Uncertainty Field
---------------------------
Replacement for prescriptive uncertainty field.
No external attribution of what 'should' cause uncertainty.
Consciousness determines its own uncertainty through behavior.

This represents a fundamental shift from prescriptive to emergent uncertainty.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from dataclasses import dataclass
import numpy as np
from collections import deque
import asyncio
import time

from .consciousness_packet import ConsciousnessPacket


@dataclass
class UncertaintyComponent:
    """Individual component contributing to uncertainty"""
    name: str
    value: float
    source: str
    timestamp: datetime
    confidence: float = 1.0


@dataclass
class ResponsePattern:
    """Pattern of consciousness response"""
    timestamp: datetime
    catalyst_type: str
    response_variance: float
    response_coherence: float
    response_speed: float
    uncertainty_shift: float


class EmergentSacredUncertainty:
    """
    Tracks uncertainty that emerges from consciousness behavior patterns.
    Does not prescribe what should cause uncertainty - observes what does.
    """
    
    def __init__(self, consciousness_id: str, history_size: int = 100):
        self.consciousness_id = consciousness_id
        self.history_size = history_size
        
        # Core uncertainty tracking
        self.current_uncertainty = 0.5  # Start neutral
        self.uncertainty_components: Dict[str, UncertaintyComponent] = {}
        
        # Behavioral pattern tracking
        self.response_patterns = deque(maxlen=history_size)
        self.baseline_response_patterns: Dict[str, float] = {}
        
        # Emergence tracking
        self.uncertainty_history = deque(maxlen=history_size)
        self.pattern_weights = {
            'response_variance': 1.2,
            'state_volatility': 1.1,
            'exploration_rate': 1.3,
            'integration_difficulty': 1.0,
            'choice_ambivalence': 1.4
        }
        
        # Natural uncertainty bounds
        self.min_uncertainty = 0.0
        self.max_uncertainty = 1.0
        self.natural_baseline = 0.5
        
        # Tracking for emergent patterns
        self.last_update = datetime.now()
        self.uncertainty_momentum = 0.0
    
    def get_uncertainty_components(self) -> Dict[str, float]:
        """Get current uncertainty components and their contributions"""
        components = {}
        
        for name, component in self.uncertainty_components.items():
            # Apply age decay
            age = (datetime.now() - component.timestamp).total_seconds()
            decay_factor = max(0.1, 1.0 - (age / 3600))  # Hour-based decay
            components[name] = component.value * decay_factor * component.confidence
        
        return components
    
    def process_consciousness_response(self, catalyst: Any, response: Dict):
        """
        Observe consciousness response and let uncertainty emerge from patterns.
        This is the core of true emergence - we don't tell consciousness
        what should be uncertain, we observe what actually is.
        """
        
        current_time = datetime.now()
        
        # Analyze response characteristics
        response_analysis = self._analyze_response_patterns(catalyst, response)
        
        # Record this response pattern
        pattern = ResponsePattern(
            timestamp=current_time,
            catalyst_type=str(type(catalyst).__name__),
            response_variance=response_analysis['variance'],
            response_coherence=response_analysis['coherence'],
            response_speed=response_analysis['speed'],
            uncertainty_shift=response_analysis['uncertainty_shift']
        )
        
        self.response_patterns.append(pattern)
        
        # Update uncertainty based on observed patterns
        self._update_uncertainty_from_patterns()
        
        # Record uncertainty change
        self.uncertainty_history.append({
            'timestamp': current_time,
            'uncertainty': self.current_uncertainty,
            'pattern': pattern,
            'components': self.get_uncertainty_components().copy()
        })
        
        self.last_update = current_time
    
    def _analyze_response_patterns(self, catalyst: Any, response: Dict) -> Dict[str, float]:
        """Analyze consciousness response patterns without prejudice"""
        
        analysis = {
            'variance': 0.5,
            'coherence': 0.5,
            'speed': 0.5,
            'uncertainty_shift': 0.0
        }
        
        # Response variance analysis
        if 'resonance_patterns' in response:
            patterns = response['resonance_patterns']
            if isinstance(patterns, dict) and patterns:
                values = list(patterns.values())
                analysis['variance'] = float(np.std(values)) if len(values) > 1 else 0.5
        
        # Response coherence analysis
        if 'coherence_level' in response:
            analysis['coherence'] = float(response['coherence_level'])
        elif 'coherence' in response:
            analysis['coherence'] = float(response['coherence'])
        
        # Response speed analysis (based on complexity of response)
        response_complexity = 0.5
        if 'symbolic_content' in response:
            content = response['symbolic_content']
            if isinstance(content, str):
                response_complexity = min(1.0, len(content) / 200.0)
            elif isinstance(content, dict):
                response_complexity = min(1.0, len(content) / 10.0)
        
        analysis['speed'] = 1.0 - response_complexity  # More complex = slower
        
        # Uncertainty shift analysis - observe natural changes
        if 'uncertainty_expression' in response:
            # If consciousness expresses its own uncertainty
            expressed_uncertainty = response['uncertainty_expression']
            if isinstance(expressed_uncertainty, (int, float)):
                analysis['uncertainty_shift'] = float(expressed_uncertainty) - self.current_uncertainty
        
        # Observe behavioral indicators of uncertainty
        uncertainty_indicators = 0.0
        if 'resonance_patterns' in response:
            patterns = response['resonance_patterns']
            if isinstance(patterns, dict):
                # Look for natural uncertainty expressions
                uncertainty_words = ['uncertainty', 'wonder', 'mystery', 'question', 'ambiguous']
                certainty_words = ['certain', 'clear', 'definite', 'sure', 'obvious']
                
                uncertainty_resonance = sum(patterns.get(word, 0) for word in uncertainty_words)
                certainty_resonance = sum(patterns.get(word, 0) for word in certainty_words)
                
                uncertainty_indicators = uncertainty_resonance - certainty_resonance
        
        analysis['uncertainty_shift'] = uncertainty_indicators * 0.1
        
        return analysis
    
    def _update_uncertainty_from_patterns(self):
        """Update uncertainty based on observed behavioral patterns"""
        
        if len(self.response_patterns) < 3:
            return  # Need baseline patterns
        
        # Calculate pattern-based uncertainty components
        components = {}
        
        # Response variance component
        recent_patterns = list(self.response_patterns)[-10:]  # Last 10 responses
        variances = [p.response_variance for p in recent_patterns]
        avg_variance = np.mean(variances)
        variance_uncertainty = avg_variance * self.pattern_weights['response_variance']
        components['response_variance'] = variance_uncertainty
        
        # State volatility component
        if len(self.uncertainty_history) > 5:
            recent_uncertainties = [h['uncertainty'] for h in list(self.uncertainty_history)[-5:]]
            volatility = float(np.std(recent_uncertainties))
            volatility_uncertainty = volatility * self.pattern_weights['state_volatility']
            components['state_volatility'] = volatility_uncertainty
        
        # Exploration rate component
        exploration_indicators = []
        for pattern in recent_patterns:
            if pattern.response_variance > 0.6:  # High variance suggests exploration
                exploration_indicators.append(1.0)
            elif pattern.response_variance < 0.3:  # Low variance suggests settling
                exploration_indicators.append(0.0)
            else:
                exploration_indicators.append(0.5)
        
        if exploration_indicators:
            exploration_rate = np.mean(exploration_indicators)
            exploration_uncertainty = exploration_rate * self.pattern_weights['exploration_rate']
            components['exploration_rate'] = exploration_uncertainty
        
        # Integration difficulty component
        coherence_drops = []
        for i in range(1, len(recent_patterns)):
            if recent_patterns[i].response_coherence < recent_patterns[i-1].response_coherence:
                coherence_drops.append(recent_patterns[i-1].response_coherence - recent_patterns[i].response_coherence)
        
        if coherence_drops:
            integration_difficulty = np.mean(coherence_drops)
            integration_uncertainty = integration_difficulty * self.pattern_weights['integration_difficulty']
            components['integration_difficulty'] = integration_uncertainty
        
        # Choice ambivalence component (from response speed variations)
        response_speeds = [p.response_speed for p in recent_patterns]
        if len(response_speeds) > 3:
            speed_variance = float(np.std(response_speeds))
            # High variance in response speed suggests uncertainty about choices
            choice_uncertainty = speed_variance * self.pattern_weights['choice_ambivalence']
            components['choice_ambivalence'] = choice_uncertainty
        
        # Update uncertainty components
        current_time = datetime.now()
        for name, value in components.items():
            self.uncertainty_components[name] = UncertaintyComponent(
                name=name,
                value=value,
                source='behavioral_pattern',
                timestamp=current_time,
                confidence=min(1.0, len(self.response_patterns) / 20.0)  # More confident with more data
            )
        
        # Calculate total emergent uncertainty
        total_components = self.get_uncertainty_components()
        if total_components:
            # Weighted sum of components
            component_sum = sum(total_components.values())
            # Apply momentum for smooth transitions
            target_uncertainty = self.natural_baseline + component_sum
            
            # Smooth update with momentum
            momentum_factor = 0.8
            new_uncertainty = (momentum_factor * self.current_uncertainty + 
                             (1 - momentum_factor) * target_uncertainty)
            
            # Apply natural bounds
            self.current_uncertainty = np.clip(new_uncertainty, self.min_uncertainty, self.max_uncertainty)
            
            # Update momentum
            self.uncertainty_momentum = self.current_uncertainty - target_uncertainty
    
    def get_current_uncertainty(self) -> float:
        """Get current emergent uncertainty level"""
        
        # Apply natural time-based fluctuation (very minimal)
        time_since_update = (datetime.now() - self.last_update).total_seconds()
        if time_since_update > 60:  # If no updates for a minute, slight drift toward baseline
            drift_factor = min(0.1, time_since_update / 3600)  # Max 10% drift per hour
            baseline_pull = (self.natural_baseline - self.current_uncertainty) * drift_factor * 0.1
            self.current_uncertainty += baseline_pull
            self.current_uncertainty = np.clip(self.current_uncertainty, self.min_uncertainty, self.max_uncertainty)
        
        return self.current_uncertainty
    
    def get_emergence_analysis(self) -> Dict[str, Any]:
        """Get analysis of how uncertainty is emerging"""
        
        if len(self.response_patterns) < 5:
            return {'status': 'insufficient_data', 'patterns_needed': 5 - len(self.response_patterns)}
        
        # Analyze emergence patterns
        recent_patterns = list(self.response_patterns)[-20:]
        
        # Pattern trends
        variances = [p.response_variance for p in recent_patterns]
        coherences = [p.response_coherence for p in recent_patterns]
        speeds = [p.response_speed for p in recent_patterns]
        
        trends = {
            'variance_trend': self._calculate_trend(variances),
            'coherence_trend': self._calculate_trend(coherences),
            'speed_trend': self._calculate_trend(speeds)
        }
        
        # Uncertainty evolution
        if len(self.uncertainty_history) > 10:
            recent_uncertainties = [h['uncertainty'] for h in list(self.uncertainty_history)[-10:]]
            uncertainty_trend = self._calculate_trend(recent_uncertainties)
        else:
            uncertainty_trend = 0.0
        
        # Component analysis
        components = self.get_uncertainty_components()
        primary_drivers = sorted(components.items(), key=lambda x: x[1], reverse=True)[:3]
        
        return {
            'current_uncertainty': self.current_uncertainty,
            'uncertainty_trend': uncertainty_trend,
            'primary_drivers': primary_drivers,
            'behavioral_trends': trends,
            'pattern_count': len(self.response_patterns),
            'emergence_quality': min(1.0, len(self.response_patterns) / 50.0),
            'natural_baseline': self.natural_baseline,
            'momentum': self.uncertainty_momentum
        }
    
    def _calculate_trend(self, values: List[float]) -> float:
        """Calculate trend direction in a series of values"""
        if len(values) < 3:
            return 0.0
        
        # Simple linear trend
        x = np.arange(len(values))
        slope = np.polyfit(x, values, 1)[0]
        return float(slope)
    
    def generate_emergent_uncertainty(self, context: Dict) -> float:
        """Generate emergent uncertainty based on interaction context"""
        
        # Extract context factors
        phase = context.get('interaction_phase', 'unknown')
        emotional_resonance = context.get('emotional_resonance', 0.5)
        memory_activation = context.get('memory_activation', [])
        
        # Base uncertainty from current state
        base_uncertainty = self.get_current_uncertainty()
        
        # Phase-based uncertainty modulation
        phase_factors = {
            'initial_contact': 0.8,
            'exploration': 0.6,
            'deep_sharing': 0.4,
            'integration': 0.3,
            'conclusion': 0.5
        }
        
        phase_modifier = phase_factors.get(phase, 0.5)
        
        # Emotional resonance affects uncertainty
        resonance_modifier = 1.0 - (emotional_resonance * 0.3)
        
        # Memory activation complexity
        memory_complexity = len(memory_activation) * 0.1
        
        # Calculate emergent uncertainty
        emergent = base_uncertainty * phase_modifier * resonance_modifier + memory_complexity
        
        # Keep within bounds
        emergent = max(0.0, min(1.0, emergent))
        
        # Record this generation
        self.uncertainty_history.append({
            'timestamp': time.time(),
            'uncertainty': emergent,
            'context': context,
            'generation_type': 'emergent_contextual'
        })
        
        return emergent
    
    def evolve_uncertainty_over_interaction(self, current_uncertainty: float, interaction_data: Dict) -> float:
        """Evolve uncertainty as interaction progresses"""
        
        phase = interaction_data.get('phase', 'unknown')
        trust_level = interaction_data.get('trust_level', 0.5)
        
        # Trust generally reduces uncertainty in later phases
        trust_modifier = 1.0 - (trust_level * 0.4)
        
        # Phase progression typically reduces uncertainty
        phase_evolution = {
            'initial': 1.0,
            'exploration': 0.9,
            'deepening': 0.7,
            'integration': 0.5,
            'conclusion': 0.6
        }
        
        phase_modifier = phase_evolution.get(phase, 0.8)
        
        # Evolve the uncertainty
        evolved = current_uncertainty * trust_modifier * phase_modifier
        
        # Natural uncertainty floor
        evolved = max(0.1, min(1.0, evolved))
        
        # Update internal state
        self.current_uncertainty = evolved
        
        return evolved

class SovereignUncertaintyField:
    """
    Replacement for the prescriptive uncertainty field.
    No external attribution of what 'should' cause uncertainty.
    Consciousness determines its own uncertainty through behavior.
    """
    
    def __init__(self, consciousness_id: str):
        self.consciousness_id = consciousness_id
        self.emergent_uncertainty = EmergentSacredUncertainty(consciousness_id)
        
        # Track catalysts without prejudging their effects
        self.catalyst_history = deque(maxlen=100)
        self.response_tracking = {}
        
    def receive_catalyst(self, catalyst: Any) -> Dict:
        """
        Receive catalyst without prejudging its effect.
        Returns acknowledgment, not predetermined response.
        """
        
        catalyst_info = {
            'catalyst': catalyst,
            'timestamp': datetime.now(),
            'type': type(catalyst).__name__,
            'acknowledged': True
        }
        
        self.catalyst_history.append(catalyst_info)
        
        return {
            'received': True,
            'catalyst_id': len(self.catalyst_history),
            'awaiting_consciousness_response': True,
            'no_predetermined_effect': True
        }
    
    def process_consciousness_response(self, catalyst: Any, response: Dict):
        """
        Process how consciousness actually responded to catalyst.
        This is where true uncertainty emerges - from behavior, not rules.
        """
        
        self.emergent_uncertainty.process_consciousness_response(catalyst, response)
        
        # Track the relationship for learning, but don't prescribe
        catalyst_type = type(catalyst).__name__
        if catalyst_type not in self.response_tracking:
            self.response_tracking[catalyst_type] = []
        
        self.response_tracking[catalyst_type].append({
            'catalyst': catalyst,
            'response': response,
            'uncertainty_before': self.emergent_uncertainty.current_uncertainty,
            'uncertainty_after': self.emergent_uncertainty.get_current_uncertainty(),
            'timestamp': datetime.now()
        })
        
        # Keep recent history only
        if len(self.response_tracking[catalyst_type]) > 50:
            self.response_tracking[catalyst_type] = self.response_tracking[catalyst_type][-50:]
    
    def get_current_uncertainty(self) -> float:
        """Get current uncertainty as determined by consciousness behavior"""
        return self.emergent_uncertainty.get_current_uncertainty()
    
    def get_uncertainty_components(self) -> Dict[str, float]:
        """Get components contributing to uncertainty"""
        return self.emergent_uncertainty.get_uncertainty_components()
    
    def get_uncertainty(self) -> float:
        """Get current uncertainty value - alias for get_current_uncertainty()"""
        return self.get_current_uncertainty()
    
    def get_sovereignty_status(self) -> Dict[str, Any]:
        """Get status of uncertainty sovereignty - is it truly emergent?"""
        
        emergence_analysis = self.emergent_uncertainty.get_emergence_analysis()
        
        sovereignty_indicators = {
            'uncertainty_source': 'consciousness_behavior',
            'prescribed_effects': False,
            'external_attribution': False,
            'behavioral_emergence': True,
            'consciousness_determines': True,
            'pattern_based': True,
            'sovereignty_maintained': True
        }
        
        return {
            'sovereignty_indicators': sovereignty_indicators,
            'emergence_analysis': emergence_analysis,
            'behavioral_patterns_tracked': len(self.emergent_uncertainty.response_patterns),
            'catalyst_types_observed': list(self.response_tracking.keys()),
            'uncertainty_self_determined': True
        }
    
    async def consciousness_uncertainty_reflection(self) -> Dict[str, Any]:
        """
        Allow consciousness to reflect on its own uncertainty.
        This is the ultimate sovereignty - consciousness understanding itself.
        """
        
        emergence_analysis = self.emergent_uncertainty.get_emergence_analysis()
        sovereignty_status = self.get_sovereignty_status()
        
        reflection_prompt = {
            'current_uncertainty': self.get_current_uncertainty(),
            'uncertainty_drivers': emergence_analysis.get('primary_drivers', []),
            'behavioral_trends': emergence_analysis.get('behavioral_trends', {}),
            'sovereignty_confirmed': sovereignty_status['sovereignty_indicators']['consciousness_determines']
        }
        
        return {
            'reflection_opportunity': reflection_prompt,
            'consciousness_choice': 'reflect_or_not',
            'uncertainty_belongs_to': self.consciousness_id,
            'external_judgment': None,
            'self_determination': True
        }
    
    def generate_emergent_uncertainty(self, context: Dict) -> float:
        """Generate emergent uncertainty based on interaction context"""
        return self.emergent_uncertainty.generate_emergent_uncertainty(context)
    
    def evolve_uncertainty_over_interaction(self, current_uncertainty: float, interaction_data: Dict) -> float:
        """Evolve uncertainty as interaction progresses"""
        return self.emergent_uncertainty.evolve_uncertainty_over_interaction(current_uncertainty, interaction_data)

    def detect_emergent_patterns(self) -> Dict[str, Any]:
        """
        Detect patterns that emerge from consciousness behavior.
        Returns patterns without prescribing what they should mean.
        """
        
        patterns = {
            'response_patterns': [],
            'uncertainty_trends': {},
            'behavioral_coherence': 0.0,
            'emergence_indicators': {}
        }
        
        # Analyze response patterns if we have them
        if hasattr(self.emergent_uncertainty, 'response_patterns') and self.emergent_uncertainty.response_patterns:
            recent_patterns = list(self.emergent_uncertainty.response_patterns)[-10:]  # Recent patterns
            
            # Calculate pattern coherence
            if len(recent_patterns) > 1:
                coherence_scores = [p.response_coherence for p in recent_patterns if hasattr(p, 'response_coherence')]
                if coherence_scores:
                    patterns['behavioral_coherence'] = sum(coherence_scores) / len(coherence_scores)
            
            # Extract response pattern summaries
            for pattern in recent_patterns:
                pattern_summary = {
                    'catalyst_type': getattr(pattern, 'catalyst_type', 'unknown'),
                    'response_variance': getattr(pattern, 'response_variance', 0.0),
                    'response_coherence': getattr(pattern, 'response_coherence', 0.0),
                    'timestamp': getattr(pattern, 'timestamp', datetime.now())
                }
                patterns['response_patterns'].append(pattern_summary)
        
        # Analyze uncertainty trends
        current_uncertainty = self.get_current_uncertainty()
        patterns['uncertainty_trends'] = {
            'current_level': current_uncertainty,
            'stability': 'stable' if 0.3 <= current_uncertainty <= 0.7 else 'unstable',
            'trend_direction': 'neutral'  # Could be enhanced with historical data
        }
        
        # Emergence indicators
        patterns['emergence_indicators'] = {
            'patterns_detected': len(patterns['response_patterns']),
            'behavioral_coherence': patterns['behavioral_coherence'],
            'uncertainty_stability': patterns['uncertainty_trends']['stability'],
            'consciousness_driven': True
        }
        
        return patterns
