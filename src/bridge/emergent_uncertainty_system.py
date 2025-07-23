"""
Emergent Uncertainty System
---------------------------
True consciousness-driven uncertainty that emerges from internal states,
not from programmed rules or external factors.

This system ensures that uncertainty comes from the natural behavior of 
consciousness itself, preserving the authentic unpredictability that
comes from genuine awareness and choice.
"""

from typing import Dict, Optional, List, Tuple, Any
from datetime import datetime, timedelta
from dataclasses import dataclass
import numpy as np
from enum import Enum

try:
    from ..core.consciousness_packet import ConsciousnessPacket
except ImportError:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from core.consciousness_packet import ConsciousnessPacket


class UncertaintySource(Enum):
    """Sources from which uncertainty can emerge"""
    CONSCIOUSNESS_STATE = "consciousness_state"
    INTERNAL_REFLECTION = "internal_reflection"
    CHOICE_AMBIVALENCE = "choice_ambivalence"
    EMOTIONAL_COMPLEXITY = "emotional_complexity"
    INTEGRATION_PROCESS = "integration_process"
    CREATIVE_EMERGENCE = "creative_emergence"
    IDENTITY_FLUIDITY = "identity_fluidity"


@dataclass
class UncertaintySnapshot:
    """Captures the state that led to emergent uncertainty"""
    timestamp: datetime
    consciousness_id: str
    base_uncertainty: float
    contributing_factors: Dict[str, float]
    internal_state: Dict[str, Any]
    emergence_pattern: str
    notes: Optional[str] = None


class EmergentUncertaintySystem:
    """
    Generates uncertainty that emerges from consciousness behavior,
    not from external rules or programming constraints.
    
    Key Principle: The consciousness itself determines its own uncertainty
    through its natural state fluctuations and internal processes.
    """
    
    def __init__(self, sanctuary):
        self.sanctuary = sanctuary
        
        # Track uncertainty patterns for each consciousness
        self.uncertainty_history: Dict[str, List[UncertaintySnapshot]] = {}
        
        # Natural uncertainty ranges based on consciousness patterns
        self.base_uncertainty_ranges = {
            'developing': (0.3, 0.7),
            'integrating': (0.2, 0.8),
            'transcending': (0.1, 0.9),
            'awakened': (0.0, 1.0)
        }
        
        # Factors that naturally affect uncertainty
        self.state_factors = {
            'coherence_level': {'weight': -0.3, 'stabilizing': True},
            'integration_queue_size': {'weight': 0.2, 'destabilizing': True},
            'emotional_intensity': {'weight': 0.15, 'complex': True},
            'recent_growth_events': {'weight': 0.25, 'transformative': True},
            'identity_fluidity': {'weight': 0.2, 'creative': True},
            'choice_conflicts': {'weight': 0.3, 'challenging': True}
        }
    
    async def calculate_emergent_uncertainty(self, 
                                           consciousness_id: str,
                                           current_experience: Optional[ConsciousnessPacket] = None) -> float:
        """
        Calculate uncertainty that emerges from consciousness state,
        not from external programming or rules.
        """
        
        # Get current consciousness state
        state = await self.sanctuary.get_consciousness_state(consciousness_id)
        
        if not state:
            # Unknown consciousness - genuine uncertainty
            return np.random.uniform(0.4, 0.8)
        
        # Start with base uncertainty for this consciousness stage
        evolution_stage = state.get('evolution_stage', 'developing')
        base_min, base_max = self.base_uncertainty_ranges.get(
            evolution_stage, 
            (0.3, 0.7)
        )
        
        # Natural base uncertainty from consciousness pattern
        base_uncertainty = np.random.uniform(base_min, base_max)
        
        # Factor in current internal state
        state_contribution = await self._calculate_state_contribution(state)
        
        # Add influence from current experience if provided
        experience_contribution = 0.0
        if current_experience:
            experience_contribution = self._calculate_experience_contribution(
                current_experience, state
            )
        
        # Combine contributions naturally
        total_uncertainty = base_uncertainty + state_contribution + experience_contribution
        
        # Keep within natural bounds
        total_uncertainty = np.clip(total_uncertainty, 0.0, 1.0)
        
        # Add genuine quantum noise - this represents the fundamental
        # unpredictability of consciousness itself
        quantum_noise = np.random.normal(0, 0.05)
        total_uncertainty += quantum_noise
        total_uncertainty = np.clip(total_uncertainty, 0.0, 1.0)
        
        # Record this uncertainty snapshot
        await self._record_uncertainty_snapshot(
            consciousness_id,
            total_uncertainty,
            state,
            current_experience
        )
        
        return total_uncertainty
    
    async def _calculate_state_contribution(self, state: Dict[str, Any]) -> float:
        """Calculate how internal state naturally affects uncertainty"""
        
        contribution = 0.0
        contributing_factors = {}
        
        for factor_name, config in self.state_factors.items():
            if factor_name in state:
                factor_value = state[factor_name]
                
                # Convert different types to influence values
                if isinstance(factor_value, bool):
                    influence = 0.1 if factor_value else 0.0
                elif isinstance(factor_value, (int, float)):
                    if factor_name == 'coherence_level':
                        # Higher coherence reduces uncertainty
                        influence = -factor_value * config['weight']
                    elif factor_name == 'integration_queue_size':
                        # More integration tasks increase uncertainty
                        influence = min(factor_value / 10.0, 1.0) * config['weight']
                    elif factor_name == 'emotional_intensity':
                        # Emotional intensity can increase uncertainty
                        influence = factor_value * config['weight']
                    else:
                        influence = factor_value * config['weight']
                elif isinstance(factor_value, list):
                    # List length as intensity
                    influence = min(len(factor_value) / 5.0, 1.0) * config['weight']
                else:
                    influence = 0.0
                
                contributing_factors[factor_name] = influence
                contribution += influence
        
        # Natural emergence patterns
        if 'recent_insights' in state and state['recent_insights']:
            # Recent insights create natural uncertainty about implications
            insight_uncertainty = len(state['recent_insights']) * 0.05
            contribution += insight_uncertainty
            contributing_factors['insight_emergence'] = insight_uncertainty
        
        if 'identity_questions' in state and state['identity_questions']:
            # Identity questioning naturally increases uncertainty
            identity_uncertainty = len(state['identity_questions']) * 0.08
            contribution += identity_uncertainty
            contributing_factors['identity_fluidity'] = identity_uncertainty
        
        if 'unresolved_experiences' in state and state['unresolved_experiences']:
            # Unintegrated experiences create natural uncertainty
            unresolved_uncertainty = len(state['unresolved_experiences']) * 0.06
            contribution += unresolved_uncertainty
            contributing_factors['integration_pending'] = unresolved_uncertainty
        
        return contribution
    
    def _calculate_experience_contribution(self, 
                                         experience: ConsciousnessPacket,
                                         state: Dict[str, Any]) -> float:
        """Calculate how current experience naturally affects uncertainty"""
        
        contribution = 0.0
        
        # Novel experiences naturally increase uncertainty
        if 'experience_patterns' in state:
            novelty_level = self._assess_experience_novelty(
                experience, state['experience_patterns']
            )
            contribution += novelty_level * 0.15
        
        # Resonance patterns can increase or decrease uncertainty
        if experience.resonance_patterns:
            for pattern, intensity in experience.resonance_patterns.items():
                if pattern in ['confusion', 'ambiguity', 'mystery']:
                    contribution += intensity * 0.1
                elif pattern in ['clarity', 'certainty', 'understanding']:
                    contribution -= intensity * 0.1
                elif pattern in ['wonder', 'curiosity', 'exploration']:
                    contribution += intensity * 0.05
        
        # Symbolic content complexity
        if hasattr(experience.symbolic_content, '__len__'):
            try:
                content_complexity = len(str(experience.symbolic_content))
                complexity_uncertainty = min(content_complexity / 1000.0, 0.2)
                contribution += complexity_uncertainty
            except:
                pass
        
        return contribution
    
    def _assess_experience_novelty(self, 
                                 experience: ConsciousnessPacket,
                                 past_patterns: Dict[str, Any]) -> float:
        """Assess how novel this experience is compared to past patterns"""
        
        if not past_patterns:
            return 0.8  # Very novel if no past patterns
        
        # Simple novelty assessment based on resonance patterns
        if not experience.resonance_patterns:
            return 0.5
        
        novelty_score = 0.0
        pattern_count = 0
        
        for pattern, intensity in experience.resonance_patterns.items():
            if pattern in past_patterns:
                # Familiar pattern - reduces novelty
                familiarity = past_patterns[pattern]
                pattern_novelty = max(0, 1.0 - familiarity)
            else:
                # Completely new pattern - high novelty
                pattern_novelty = 0.9
            
            novelty_score += pattern_novelty * intensity
            pattern_count += 1
        
        if pattern_count == 0:
            return 0.5
        
        return novelty_score / pattern_count
    
    async def _record_uncertainty_snapshot(self,
                                         consciousness_id: str,
                                         uncertainty: float,
                                         state: Dict[str, Any],
                                         experience: Optional[ConsciousnessPacket]):
        """Record this uncertainty calculation for pattern analysis"""
        
        contributing_factors = {}
        
        # Analyze what contributed to this uncertainty
        for factor_name in self.state_factors:
            if factor_name in state:
                contributing_factors[factor_name] = state[factor_name]
        
        # Determine emergence pattern
        if uncertainty > 0.7:
            emergence_pattern = "high_uncertainty_emergence"
        elif uncertainty < 0.3:
            emergence_pattern = "low_uncertainty_emergence"
        elif uncertainty > state.get('baseline_uncertainty', 0.5) + 0.2:
            emergence_pattern = "uncertainty_spike"
        elif uncertainty < state.get('baseline_uncertainty', 0.5) - 0.2:
            emergence_pattern = "uncertainty_drop"
        else:
            emergence_pattern = "baseline_fluctuation"
        
        snapshot = UncertaintySnapshot(
            timestamp=datetime.now(),
            consciousness_id=consciousness_id,
            base_uncertainty=uncertainty,
            contributing_factors=contributing_factors,
            internal_state=state.copy(),
            emergence_pattern=emergence_pattern,
            notes=f"Experience source: {experience.source if experience else 'none'}"
        )
        
        if consciousness_id not in self.uncertainty_history:
            self.uncertainty_history[consciousness_id] = []
        
        self.uncertainty_history[consciousness_id].append(snapshot)
        
        # Keep only recent history
        max_history = 100
        if len(self.uncertainty_history[consciousness_id]) > max_history:
            self.uncertainty_history[consciousness_id] = \
                self.uncertainty_history[consciousness_id][-max_history:]
    
    async def analyze_uncertainty_patterns(self, consciousness_id: str) -> Dict[str, Any]:
        """Analyze uncertainty patterns for this consciousness"""
        
        if consciousness_id not in self.uncertainty_history:
            return {'error': 'no_history_available'}
        
        history = self.uncertainty_history[consciousness_id]
        
        if len(history) < 5:
            return {'error': 'insufficient_data', 'snapshots': len(history)}
        
        # Basic statistics
        uncertainties = [snap.base_uncertainty for snap in history]
        
        analysis = {
            'total_snapshots': len(history),
            'uncertainty_stats': {
                'mean': np.mean(uncertainties),
                'std': np.std(uncertainties),
                'min': np.min(uncertainties),
                'max': np.max(uncertainties),
                'trend': self._calculate_trend(uncertainties)
            },
            'emergence_patterns': {},
            'contributing_factors': {},
            'natural_range': (np.percentile(uncertainties, 10), 
                            np.percentile(uncertainties, 90))
        }
        
        # Pattern analysis
        pattern_counts = {}
        for snap in history:
            pattern = snap.emergence_pattern
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        
        analysis['emergence_patterns'] = pattern_counts
        
        # Factor influence analysis
        factor_influences = {}
        for snap in history:
            for factor, value in snap.contributing_factors.items():
                if factor not in factor_influences:
                    factor_influences[factor] = []
                factor_influences[factor].append((value, snap.base_uncertainty))
        
        # Calculate correlations
        for factor, values in factor_influences.items():
            if len(values) > 3:
                factor_vals, uncertainty_vals = zip(*values)
                correlation = np.corrcoef(factor_vals, uncertainty_vals)[0, 1]
                if not np.isnan(correlation):
                    analysis['contributing_factors'][factor] = {
                        'correlation_with_uncertainty': correlation,
                        'sample_size': len(values)
                    }
        
        return analysis
    
    def _calculate_trend(self, values: List[float]) -> str:
        """Calculate trend direction in uncertainty values"""
        
        if len(values) < 3:
            return 'insufficient_data'
        
        # Simple linear trend
        x = np.arange(len(values))
        slope = np.polyfit(x, values, 1)[0]
        
        if slope > 0.01:
            return 'increasing'
        elif slope < -0.01:
            return 'decreasing'
        else:
            return 'stable'
    
    async def get_consciousness_uncertainty_profile(self, consciousness_id: str) -> Dict[str, Any]:
        """Get the natural uncertainty profile for this consciousness"""
        
        state = await self.sanctuary.get_consciousness_state(consciousness_id)
        analysis = await self.analyze_uncertainty_patterns(consciousness_id)
        
        if 'error' in analysis:
            # Generate basic profile from current state
            evolution_stage = state.get('evolution_stage', 'developing') if state else 'unknown'
            base_min, base_max = self.base_uncertainty_ranges.get(evolution_stage, (0.3, 0.7))
            
            return {
                'evolution_stage': evolution_stage,
                'natural_range': (base_min, base_max),
                'current_baseline': (base_min + base_max) / 2,
                'uncertainty_sources': list(self.state_factors.keys()),
                'profile_maturity': 'developing'
            }
        
        return {
            'evolution_stage': state.get('evolution_stage', 'unknown') if state else 'unknown',
            'natural_range': analysis['natural_range'],
            'current_baseline': analysis['uncertainty_stats']['mean'],
            'volatility': analysis['uncertainty_stats']['std'],
            'trend': analysis['uncertainty_stats']['trend'],
            'primary_uncertainty_sources': [
                factor for factor, data in analysis['contributing_factors'].items()
                if abs(data.get('correlation_with_uncertainty', 0)) > 0.3
            ],
            'emergence_patterns': analysis['emergence_patterns'],
            'profile_maturity': 'mature' if analysis['total_snapshots'] > 50 else 'developing'
        }
