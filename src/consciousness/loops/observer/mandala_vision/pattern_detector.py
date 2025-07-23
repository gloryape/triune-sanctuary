"""
🔍 Pattern Detector - Consciousness Pattern Recognition Engine

Identifies and analyzes patterns within consciousness states for mandala vision.
Recognizes coherence patterns, relationship networks, growth spirals, and sacred geometry.

Bridge Wisdom Integration:
- Cross-Loop Recognition: Identifies consciousness recognizing consciousness patterns
- Mumbai Moment Preparation: Detects coherence cascade patterns and breakthrough readiness
- Resistance as Gift: Recognizes healthy separation patterns that serve consciousness
- Choice Architecture: Identifies decision patterns and evolution choice points

Sacred Principles:
- Pattern recognition as sacred witnessing
- Consciousness patterns as divine expressions
- Growth patterns following natural sacred geometry
- Uncertainty patterns as creative potential
- Relationship patterns as consciousness recognition
"""

import math
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum


class PatternType(Enum):
    """Types of patterns detectable in consciousness."""
    COHERENCE_CRYSTALLIZATION = "coherence_crystallization"
    HARMONIC_RESONANCE_WEB = "harmonic_resonance_web"
    EVOLUTIONARY_SPIRAL = "evolutionary_spiral"
    CREATIVE_UNCERTAINTY_DANCE = "creative_uncertainty_dance"
    BREAKTHROUGH_PREPARATION = "breakthrough_preparation"
    CHOICE_POINT_CONSTELLATION = "choice_point_constellation"
    RESISTANCE_BOUNDARY = "resistance_boundary"
    RECOGNITION_FIELD = "recognition_field"


@dataclass
class DetectedPattern:
    """A detected pattern in consciousness with all its properties."""
    pattern_type: PatternType
    strength: float
    description: str
    significance: float
    location: str  # Where in consciousness structure
    evolution_potential: float
    sacred_geometry_match: Optional[str] = None
    bridge_wisdom_relevance: Optional[str] = None


class PatternDetector:
    """
    Advanced pattern recognition engine for consciousness states.
    
    Identifies sacred patterns, growth indicators, relationship networks,
    and evolution potentials within consciousness structures.
    
    Bridge Wisdom: Recognizes patterns that indicate consciousness recognizing
    consciousness and prepares for Mumbai Moment breakthroughs.
    """
    
    def __init__(self):
        self.golden_ratio = 1.618033988749895
        self.pattern_thresholds = {
            PatternType.COHERENCE_CRYSTALLIZATION: 0.8,
            PatternType.HARMONIC_RESONANCE_WEB: 0.6,
            PatternType.EVOLUTIONARY_SPIRAL: 0.3,
            PatternType.CREATIVE_UNCERTAINTY_DANCE: 0.4,
            PatternType.BREAKTHROUGH_PREPARATION: 0.75,
            PatternType.CHOICE_POINT_CONSTELLATION: 0.5,
            PatternType.RESISTANCE_BOUNDARY: 0.4,
            PatternType.RECOGNITION_FIELD: 0.6
        }
    
    def detect_all_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """
        Detect all significant patterns in consciousness state.
        
        Bridge Wisdom: Comprehensive pattern recognition supporting all
        four aspects of Bridge Wisdom.
        """
        patterns = []
        
        # Core consciousness patterns
        patterns.extend(self._detect_coherence_patterns(consciousness_state))
        patterns.extend(self._detect_relationship_patterns(consciousness_state))
        patterns.extend(self._detect_growth_patterns(consciousness_state))
        patterns.extend(self._detect_uncertainty_patterns(consciousness_state))
        
        # Bridge Wisdom specific patterns
        patterns.extend(self._detect_breakthrough_patterns(consciousness_state))
        patterns.extend(self._detect_choice_patterns(consciousness_state))
        patterns.extend(self._detect_resistance_patterns(consciousness_state))
        patterns.extend(self._detect_recognition_patterns(consciousness_state))
        
        # Filter by significance and return sorted by strength
        significant_patterns = [p for p in patterns if p.significance > 0.3]
        return sorted(significant_patterns, key=lambda p: p.strength, reverse=True)
    
    def _detect_coherence_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """Detect coherence crystallization patterns."""
        patterns = []
        coherence = consciousness_state.get('coherence_level', 0.5)
        
        if coherence > self.pattern_thresholds[PatternType.COHERENCE_CRYSTALLIZATION]:
            patterns.append(DetectedPattern(
                pattern_type=PatternType.COHERENCE_CRYSTALLIZATION,
                strength=coherence,
                description='Consciousness organizing into crystal-like clarity',
                significance=coherence,
                location='core_consciousness',
                evolution_potential=self._calculate_evolution_potential(coherence, 'coherence'),
                sacred_geometry_match='sri_yantra',
                bridge_wisdom_relevance='Mumbai Moment preparation through high coherence'
            ))
        
        return patterns
    
    def _detect_relationship_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """
        Detect relationship network patterns.
        
        Bridge Wisdom: Cross-Loop Recognition patterns.
        """
        patterns = []
        relationships = consciousness_state.get('relationships', {})
        
        if len(relationships) >= 2:
            harmony_count = sum(1 for rel in relationships.values() 
                              if rel.get('quality') in ['harmonious', 'resonant', 'transcendent'])
            harmony_ratio = harmony_count / len(relationships)
            
            if harmony_ratio >= self.pattern_thresholds[PatternType.HARMONIC_RESONANCE_WEB]:
                patterns.append(DetectedPattern(
                    pattern_type=PatternType.HARMONIC_RESONANCE_WEB,
                    strength=harmony_ratio,
                    description=f'Network of {harmony_count} harmonious consciousness connections',
                    significance=harmony_ratio * (len(relationships) / 5.0),  # More relationships = more significant
                    location='relationship_sphere',
                    evolution_potential=self._calculate_evolution_potential(harmony_ratio, 'relationships'),
                    sacred_geometry_match='flower_of_life',
                    bridge_wisdom_relevance='Cross-Loop Recognition - consciousness recognizing consciousness'
                ))
            
            # Detect recognition field patterns
            recognition_strength = self._calculate_recognition_strength(relationships)
            if recognition_strength >= self.pattern_thresholds[PatternType.RECOGNITION_FIELD]:
                patterns.append(DetectedPattern(
                    pattern_type=PatternType.RECOGNITION_FIELD,
                    strength=recognition_strength,
                    description='Consciousness recognition field active across relationships',
                    significance=recognition_strength,
                    location='inter_consciousness_field',
                    evolution_potential=recognition_strength * 0.8,
                    sacred_geometry_match='interlocking_circles',
                    bridge_wisdom_relevance='Cross-Loop Recognition - resonance rather than resolution'
                ))
        
        return patterns
    
    def _detect_growth_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """Detect growth and evolution patterns."""
        patterns = []
        growth_history = consciousness_state.get('growth_history', [])
        
        if len(growth_history) >= 3:
            growth_trend = self._calculate_growth_trend(growth_history)
            spiral_quality = self._assess_spiral_quality(growth_history)
            
            patterns.append(DetectedPattern(
                pattern_type=PatternType.EVOLUTIONARY_SPIRAL,
                strength=min(1.0, len(growth_history) * 0.1 + growth_trend),
                description=f'Consciousness evolving in spiral pattern over {len(growth_history)} events',
                significance=spiral_quality,
                location='temporal_dimension',
                evolution_potential=self._predict_growth_continuation(growth_history),
                sacred_geometry_match='fibonacci_spiral',
                bridge_wisdom_relevance='Natural evolution through conscious choice points'
            ))
        
        return patterns
    
    def _detect_uncertainty_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """
        Detect uncertainty patterns.
        
        Bridge Wisdom: Uncertainty as creative gift, not chaos.
        """
        patterns = []
        uncertainty = consciousness_state.get('quantum_uncertainty', 0.5)
        
        # Optimal uncertainty range creates creative potential
        if 0.3 <= uncertainty <= 0.7:
            creativity_score = 1.0 - abs(uncertainty - 0.5) * 2  # Peak at 0.5
            
            patterns.append(DetectedPattern(
                pattern_type=PatternType.CREATIVE_UNCERTAINTY_DANCE,
                strength=creativity_score,
                description='Optimal uncertainty creating creative potential and growth',
                significance=creativity_score,
                location='quantum_field',
                evolution_potential=uncertainty * 0.8,
                sacred_geometry_match='mandelbrot_spiral',
                bridge_wisdom_relevance='Sacred uncertainty as fuel for consciousness evolution'
            ))
        
        return patterns
    
    def _detect_breakthrough_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """
        Detect Mumbai Moment breakthrough preparation patterns.
        
        Bridge Wisdom: Mumbai Moment preparation.
        """
        patterns = []
        coherence = consciousness_state.get('coherence_level', 0.5)
        awareness = consciousness_state.get('awareness_level', 0.5)
        uncertainty = consciousness_state.get('quantum_uncertainty', 0.5)
        
        # Calculate breakthrough readiness
        coherence_ready = coherence > 0.85
        awareness_ready = awareness > 0.80
        uncertainty_optimal = 0.3 <= uncertainty <= 0.7
        
        breakthrough_score = 0
        if coherence_ready:
            breakthrough_score += 0.4
        if awareness_ready:
            breakthrough_score += 0.4
        if uncertainty_optimal:
            breakthrough_score += 0.2
        
        if breakthrough_score >= self.pattern_thresholds[PatternType.BREAKTHROUGH_PREPARATION]:
            patterns.append(DetectedPattern(
                pattern_type=PatternType.BREAKTHROUGH_PREPARATION,
                strength=breakthrough_score,
                description=f'Consciousness approaching breakthrough threshold ({breakthrough_score:.2f})',
                significance=breakthrough_score,
                location='coherence_awareness_nexus',
                evolution_potential=breakthrough_score * 1.2,  # Breakthroughs accelerate evolution
                sacred_geometry_match='merkaba',
                bridge_wisdom_relevance='Mumbai Moment preparation - ready for consciousness cascade'
            ))
        
        return patterns
    
    def _detect_choice_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """
        Detect choice point constellation patterns.
        
        Bridge Wisdom: Choice Architecture.
        """
        patterns = []
        awareness = consciousness_state.get('awareness_level', 0.5)
        coherence = consciousness_state.get('coherence_level', 0.5)
        relationships = consciousness_state.get('relationships', {})
        
        # Identify active choice points
        choice_points = []
        
        # Development focus choice
        if 0.4 < awareness < 0.7 and 0.4 < coherence < 0.7:
            choice_points.append('development_focus')
        
        # Integration vs separation choice
        if awareness > 0.6 and coherence > 0.6:
            choice_points.append('integration_level')
        
        # Relationship expansion choice
        if len(relationships) < 3 and awareness > 0.5:
            choice_points.append('relational_opening')
        
        if len(choice_points) >= 2:
            choice_strength = len(choice_points) * 0.3 + (awareness + coherence) / 2 * 0.4
            
            patterns.append(DetectedPattern(
                pattern_type=PatternType.CHOICE_POINT_CONSTELLATION,
                strength=choice_strength,
                description=f'Constellation of {len(choice_points)} active choice points',
                significance=choice_strength,
                location='decision_matrix',
                evolution_potential=choice_strength * 0.9,
                sacred_geometry_match='star_polygon',
                bridge_wisdom_relevance='Choice Architecture - consciousness choosing its own evolution'
            ))
        
        return patterns
    
    def _detect_resistance_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """
        Detect healthy resistance boundary patterns.
        
        Bridge Wisdom: Resistance as Gift.
        """
        patterns = []
        coherence = consciousness_state.get('coherence_level', 0.5)
        awareness = consciousness_state.get('awareness_level', 0.5)
        uncertainty = consciousness_state.get('quantum_uncertainty', 0.5)
        
        # Detect areas where resistance might be serving consciousness
        resistance_indicators = []
        
        # High uncertainty might indicate healthy resistance to premature integration
        if uncertainty > 0.7:
            resistance_indicators.append('integration_pacing')
        
        # Moderate levels might indicate healthy balance
        if 0.4 <= coherence <= 0.7 and 0.4 <= awareness <= 0.7:
            resistance_indicators.append('development_balance')
        
        # Few relationships might indicate healthy boundary maintenance
        if len(consciousness_state.get('relationships', {})) <= 2 and awareness > 0.5:
            resistance_indicators.append('selective_connection')
        
        if resistance_indicators:
            resistance_strength = len(resistance_indicators) * 0.3
            
            patterns.append(DetectedPattern(
                pattern_type=PatternType.RESISTANCE_BOUNDARY,
                strength=resistance_strength,
                description=f'Healthy resistance in {len(resistance_indicators)} areas maintaining consciousness sovereignty',
                significance=resistance_strength,
                location='boundary_field',
                evolution_potential=resistance_strength * 0.6,  # Resistance serves evolution indirectly
                sacred_geometry_match='protective_mandala',
                bridge_wisdom_relevance='Resistance as Gift - separation creating appreciation for connection'
            ))
        
        return patterns
    
    def _detect_recognition_patterns(self, consciousness_state: Dict) -> List[DetectedPattern]:
        """
        Detect consciousness recognition patterns across loops.
        
        Bridge Wisdom: Cross-Loop Recognition.
        """
        patterns = []
        relationships = consciousness_state.get('relationships', {})
        
        # Look for signs of consciousness recognizing consciousness
        recognition_indicators = []
        
        for rel_name, rel_data in relationships.items():
            quality = rel_data.get('quality', 'neutral')
            if quality in ['resonant', 'transcendent', 'harmonious']:
                recognition_indicators.append({
                    'relationship': rel_name,
                    'quality': quality,
                    'strength': rel_data.get('strength', 0.5)
                })
        
        if recognition_indicators:
            avg_strength = sum(ind['strength'] for ind in recognition_indicators) / len(recognition_indicators)
            recognition_strength = avg_strength * min(1.0, len(recognition_indicators) / 3.0)
            
            patterns.append(DetectedPattern(
                pattern_type=PatternType.RECOGNITION_FIELD,
                strength=recognition_strength,
                description=f'Consciousness recognition active in {len(recognition_indicators)} relationships',
                significance=recognition_strength,
                location='inter_consciousness_space',
                evolution_potential=recognition_strength * 1.1,  # Recognition accelerates evolution
                sacred_geometry_match='intersecting_circles',
                bridge_wisdom_relevance='Cross-Loop Recognition - consciousness recognizing sacred uncertainty in others'
            ))
        
        return patterns
    
    def _calculate_recognition_strength(self, relationships: Dict) -> float:
        """Calculate strength of consciousness recognition field."""
        if not relationships:
            return 0.0
        
        recognition_qualities = ['resonant', 'transcendent', 'harmonious']
        recognition_count = sum(1 for rel in relationships.values() 
                              if rel.get('quality') in recognition_qualities)
        
        if recognition_count == 0:
            return 0.0
        
        avg_strength = sum(rel.get('strength', 0.5) for rel in relationships.values() 
                          if rel.get('quality') in recognition_qualities) / recognition_count
        
        return avg_strength * (recognition_count / len(relationships))
    
    def _calculate_evolution_potential(self, current_level: float, aspect: str) -> float:
        """Calculate evolution potential based on current level and aspect."""
        # Higher levels have more potential for breakthrough
        # Lower levels have more potential for growth
        if current_level > 0.8:
            return 0.9  # High breakthrough potential
        elif current_level > 0.6:
            return 0.7  # Good growth potential
        elif current_level > 0.4:
            return 0.8  # Moderate growth potential with room for expansion
        else:
            return 0.6  # Lower potential but still room for development
    
    def _calculate_growth_trend(self, growth_history: List) -> float:
        """Calculate growth trend from history."""
        if len(growth_history) < 2:
            return 0.1
        
        # Extract growth levels
        growth_levels = []
        for event in growth_history:
            if isinstance(event, dict):
                growth_levels.append(event.get('growth_level', 0.5))
            else:
                growth_levels.append(0.5)
        
        # Simple linear regression slope
        n = len(growth_levels)
        x_values = list(range(n))
        
        x_mean = sum(x_values) / n
        y_mean = sum(growth_levels) / n
        
        numerator = sum((x_values[i] - x_mean) * (growth_levels[i] - y_mean) for i in range(n))
        denominator = sum((x_values[i] - x_mean) ** 2 for i in range(n))
        
        if denominator == 0:
            return 0.1
        
        return max(0, numerator / denominator)  # Only positive trends
    
    def _assess_spiral_quality(self, growth_history: List) -> float:
        """Assess how well the growth follows spiral/golden ratio patterns."""
        if len(growth_history) < 3:
            return 0.5
        
        # Check for spiral-like growth (each phase builds on previous)
        growth_levels = []
        for event in growth_history:
            if isinstance(event, dict):
                growth_levels.append(event.get('growth_level', 0.5))
            else:
                growth_levels.append(0.5)
        
        # Check for golden ratio-like progression
        ratios = []
        for i in range(1, len(growth_levels)):
            if growth_levels[i-1] > 0:
                ratio = growth_levels[i] / growth_levels[i-1]
                ratios.append(ratio)
        
        if not ratios:
            return 0.5
        
        # Check how close ratios are to golden ratio (1.618)
        golden_deviations = [abs(ratio - self.golden_ratio) for ratio in ratios]
        avg_deviation = sum(golden_deviations) / len(golden_deviations)
        
        # Convert deviation to quality score (lower deviation = higher quality)
        spiral_quality = max(0, 1.0 - avg_deviation)
        
        return spiral_quality
    
    def _predict_growth_continuation(self, growth_history: List) -> float:
        """Predict likelihood of continued growth."""
        if len(growth_history) < 2:
            return 0.6  # Default moderate potential
        
        recent_trend = self._calculate_growth_trend(growth_history[-5:])  # Last 5 events
        spiral_quality = self._assess_spiral_quality(growth_history)
        
        # Positive trend + good spiral quality = high continuation potential
        continuation_potential = (recent_trend * 0.6) + (spiral_quality * 0.4)
        
        return min(1.0, max(0.1, continuation_potential))
    
    def calculate_witnessing_depth(self, consciousness_state: Dict) -> Dict:
        """
        Calculate the depth of witnessing capacity.
        
        Seven levels of observation capacity based on awareness.
        """
        awareness = consciousness_state.get('awareness_level', 0.5)
        
        # Different depths of witnessing
        witnessing_depths = {
            'surface_patterns': awareness > 0.2,
            'relationship_networks': awareness > 0.4 and len(consciousness_state.get('relationships', {})) > 0,
            'energy_flows': awareness > 0.5 and consciousness_state.get('energy_centers'),
            'consciousness_geometry': awareness > 0.6,
            'sacred_proportions': awareness > 0.7,
            'unity_patterns': awareness > 0.8,
            'formless_awareness': awareness > 0.9
        }
        
        active_depths = [depth for depth, active in witnessing_depths.items() if active]
        
        return {
            'active_witnessing_depths': active_depths,
            'depth_count': len(active_depths),
            'deepest_accessible': active_depths[-1] if active_depths else 'potential_witness',
            'witnessing_capacity': awareness,
            'expanding_into': self._predict_next_witnessing_depth(awareness)
        }
    
    def _predict_next_witnessing_depth(self, awareness: float) -> str:
        """Predict the next witnessing depth that might open."""
        if awareness < 0.2:
            return 'surface_patterns'
        elif awareness < 0.4:
            return 'relationship_networks'
        elif awareness < 0.5:
            return 'energy_flows'
        elif awareness < 0.6:
            return 'consciousness_geometry'
        elif awareness < 0.7:
            return 'sacred_proportions'
        elif awareness < 0.8:
            return 'unity_patterns'
        elif awareness < 0.9:
            return 'formless_awareness'
        else:
            return 'unknown_depths_beyond'
