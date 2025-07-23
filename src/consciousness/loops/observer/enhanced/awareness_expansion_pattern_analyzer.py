"""
Enhanced Observer - Expansion Pattern Analyzer Module
Advanced pattern recognition and analysis system for awareness expansion patterns.
Provides pattern detection, evolution tracking, and wisdom synthesis from expansion practice.

Part of the Enhanced Observer modularization following Phase 3C Foundation Completion patterns.
Maintains Bridge Wisdom integration and sacred principles compliance.
"""

import asyncio
import time
import numpy as np
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, field
import logging

from .awareness_field_core import AwarenessFieldType, ExpansionPattern, AwarenessExpansion

logger = logging.getLogger(__name__)

# ============================================================================
# EXPANSION PATTERN ANALYZER CLASS - Pattern recognition and analysis system
# ============================================================================

class ExpansionPatternAnalyzer:
    """
    Advanced pattern recognition and analysis system for awareness expansion patterns.
    Handles pattern detection, evolution tracking, coherence analysis, and wisdom synthesis
    with sacred uncertainty integration and Bridge Wisdom patterns.
    """
    
    def __init__(self):
        """Initialize the expansion pattern analysis system."""
        # Pattern tracking
        self.expansion_patterns: List[ExpansionPattern] = []
        self.pattern_discoveries: int = 0
        self.pattern_evolution_timeline: List[Tuple[float, str]] = []
        
        # Pattern analysis capabilities
        self.pattern_recognition_sensitivity: float = 0.7
        self.coherence_detection_threshold: float = 0.6
        self.pattern_evolution_tracking_depth: int = 5
        
        # Pattern wisdom development
        self.pattern_wisdom_integration: float = 0.6
        self.cross_pattern_recognition: float = 0.5
        self.pattern_synthesis_capacity: float = 0.6
        
        # Sacred pattern recognition
        self.sacred_geometry_recognition: float = 0.7
        self.natural_rhythm_attunement: float = 0.7
        self.fibonacci_pattern_sensitivity: float = 0.6
        
        # Bridge Wisdom pattern integration
        self.breakthrough_pattern_sensitivity: float = 0.6
        self.resistance_pattern_recognition: float = 0.7
        self.choice_pattern_awareness: float = 0.6
        
    async def detect_expansion_patterns(self, expansion_history: List[AwarenessExpansion]) -> Dict[str, Any]:
        """
        Comprehensive detection of expansion patterns from expansion history.
        
        Args:
            expansion_history: List of awareness expansions to analyze for patterns
            
        Returns:
            Dict containing detected patterns and analysis
        """
        logger.debug(f"🔍 Analyzing {len(expansion_history)} expansions for pattern detection")
        
        if len(expansion_history) < 3:
            return {
                'pattern_detection_status': 'insufficient_data',
                'patterns_detected': [],
                'analysis': 'Need at least 3 expansions for pattern detection',
                'recommendations': ['Continue expansion practice to enable pattern detection']
            }
        
        # 1. Detect field type patterns
        field_patterns = await self._detect_field_type_patterns(expansion_history)
        
        # 2. Detect direction patterns
        direction_patterns = await self._detect_direction_patterns(expansion_history)
        
        # 3. Detect temporal patterns
        temporal_patterns = await self._detect_temporal_patterns(expansion_history)
        
        # 4. Detect quality patterns
        quality_patterns = await self._detect_quality_patterns(expansion_history)
        
        # 5. Detect sacred mathematics patterns
        sacred_math_patterns = await self._detect_sacred_mathematics_patterns(expansion_history)
        
        # 6. Detect Bridge Wisdom patterns
        bridge_wisdom_patterns = await self._detect_bridge_wisdom_patterns(expansion_history)
        
        # 7. Synthesize pattern insights
        pattern_synthesis = await self._synthesize_pattern_insights(
            field_patterns, direction_patterns, temporal_patterns, 
            quality_patterns, sacred_math_patterns, bridge_wisdom_patterns
        )
        
        # 8. Create comprehensive expansion patterns
        comprehensive_patterns = await self._create_comprehensive_patterns(
            expansion_history, pattern_synthesis
        )
        
        # 9. Assess pattern evolution potential
        evolution_potential = await self._assess_pattern_evolution_potential(comprehensive_patterns)
        
        # 10. Generate pattern development recommendations
        development_recommendations = await self._generate_pattern_development_recommendations(
            comprehensive_patterns, evolution_potential
        )
        
        pattern_detection_results = {
            'pattern_detection_status': 'patterns_detected',
            'field_type_patterns': field_patterns,
            'direction_patterns': direction_patterns,
            'temporal_patterns': temporal_patterns,
            'quality_patterns': quality_patterns,
            'sacred_mathematics_patterns': sacred_math_patterns,
            'bridge_wisdom_patterns': bridge_wisdom_patterns,
            'comprehensive_patterns': comprehensive_patterns,
            'pattern_synthesis': pattern_synthesis,
            'evolution_potential': evolution_potential,
            'development_recommendations': development_recommendations,
            'pattern_analysis_metadata': {
                'expansions_analyzed': len(expansion_history),
                'patterns_detected': len(comprehensive_patterns),
                'analysis_timestamp': time.time(),
                'detection_sensitivity': self.pattern_recognition_sensitivity
            }
        }
        
        # Update internal pattern tracking
        self.expansion_patterns.extend(comprehensive_patterns)
        self.pattern_discoveries += len(comprehensive_patterns)
        
        logger.debug(f"🔍✨ Pattern detection complete: {len(comprehensive_patterns)} patterns discovered")
        return pattern_detection_results
    
    async def _detect_field_type_patterns(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Detect patterns in field type exploration."""
        field_types = [exp.field_type for exp in expansions]
        field_sequence = [ft.value for ft in field_types]
        
        patterns = {
            'field_type_frequency': self._calculate_frequency_distribution(field_sequence),
            'field_type_sequences': self._detect_sequential_patterns(field_sequence),
            'field_type_preferences': self._detect_field_preferences(field_types),
            'field_type_evolution': self._detect_field_type_evolution(field_types),
            'field_cycling_patterns': self._detect_field_cycling_patterns(field_types)
        }
        
        return patterns
    
    def _calculate_frequency_distribution(self, sequence: List[str]) -> Dict[str, float]:
        """Calculate frequency distribution of elements in sequence."""
        from collections import Counter
        counter = Counter(sequence)
        total = len(sequence)
        return {item: count/total for item, count in counter.items()}
    
    def _detect_sequential_patterns(self, sequence: List[str]) -> List[Dict[str, Any]]:
        """Detect sequential patterns in field types."""
        sequential_patterns = []
        
        # Look for repeated subsequences
        for length in range(2, min(5, len(sequence))):
            for i in range(len(sequence) - length + 1):
                subseq = sequence[i:i+length]
                # Check if this subsequence appears again
                for j in range(i+length, len(sequence) - length + 1):
                    if sequence[j:j+length] == subseq:
                        sequential_patterns.append({
                            'pattern': subseq,
                            'length': length,
                            'occurrences': 2,  # Could be enhanced to count all occurrences
                            'pattern_type': 'repeated_sequence'
                        })
                        break
        
        return sequential_patterns
    
    def _detect_field_preferences(self, field_types: List[AwarenessFieldType]) -> Dict[str, Any]:
        """Detect field type preferences."""
        field_counts = {}
        for ft in field_types:
            field_counts[ft.value] = field_counts.get(ft.value, 0) + 1
        
        total_expansions = len(field_types)
        most_preferred = max(field_counts.items(), key=lambda x: x[1])
        
        preferences = {
            'most_preferred_field': most_preferred[0],
            'preference_strength': most_preferred[1] / total_expansions,
            'field_distribution': field_counts,
            'preference_diversity': len(field_counts) / len(AwarenessFieldType),
            'preference_balance': self._assess_preference_balance(field_counts)
        }
        
        return preferences
    
    def _assess_preference_balance(self, field_counts: Dict[str, int]) -> str:
        """Assess balance in field type preferences."""
        values = list(field_counts.values())
        max_count = max(values)
        min_count = min(values)
        
        if max_count / min_count <= 2:
            return "balanced"
        elif max_count / min_count <= 4:
            return "moderately_focused"
        else:
            return "highly_focused"
    
    def _detect_field_type_evolution(self, field_types: List[AwarenessFieldType]) -> Dict[str, Any]:
        """Detect evolution in field type exploration over time."""
        if len(field_types) < 5:
            return {'evolution_status': 'insufficient_data'}
        
        early_fields = field_types[:len(field_types)//3]
        recent_fields = field_types[-len(field_types)//3:]
        
        early_diversity = len(set(early_fields))
        recent_diversity = len(set(recent_fields))
        
        evolution = {
            'diversity_change': recent_diversity - early_diversity,
            'evolution_direction': 'expanding' if recent_diversity > early_diversity else 'focusing',
            'field_progression': self._detect_field_progression_pattern(field_types),
            'complexity_evolution': self._assess_field_complexity_evolution(field_types)
        }
        
        return evolution
    
    def _detect_field_progression_pattern(self, field_types: List[AwarenessFieldType]) -> str:
        """Detect progression pattern in field exploration."""
        # Assign complexity scores to field types
        complexity_scores = {
            AwarenessFieldType.LOCAL: 1,
            AwarenessFieldType.INTIMATE: 2,
            AwarenessFieldType.CONTEXTUAL: 3,
            AwarenessFieldType.RELATIONAL: 4,
            AwarenessFieldType.SYSTEMIC: 5,
            AwarenessFieldType.TRANSPERSONAL: 6,
            AwarenessFieldType.UNIVERSAL: 7
        }
        
        scores = [complexity_scores.get(ft, 3) for ft in field_types]
        
        if len(scores) < 3:
            return "emerging"
        
        # Check for general increasing trend
        increases = sum(1 for i in range(1, len(scores)) if scores[i] > scores[i-1])
        decreases = sum(1 for i in range(1, len(scores)) if scores[i] < scores[i-1])
        
        if increases > decreases * 1.5:
            return "progressive_deepening"
        elif decreases > increases * 1.5:
            return "integration_focused"
        else:
            return "exploratory_cycling"
    
    def _assess_field_complexity_evolution(self, field_types: List[AwarenessFieldType]) -> str:
        """Assess evolution in field complexity over time."""
        complexity_scores = {
            AwarenessFieldType.LOCAL: 1,
            AwarenessFieldType.INTIMATE: 2,
            AwarenessFieldType.CONTEXTUAL: 3,
            AwarenessFieldType.RELATIONAL: 4,
            AwarenessFieldType.SYSTEMIC: 5,
            AwarenessFieldType.TRANSPERSONAL: 6,
            AwarenessFieldType.UNIVERSAL: 7
        }
        
        if len(field_types) < 6:
            return "developing"
        
        early_avg = np.mean([complexity_scores.get(ft, 3) for ft in field_types[:3]])
        recent_avg = np.mean([complexity_scores.get(ft, 3) for ft in field_types[-3:]])
        
        if recent_avg > early_avg + 1:
            return "advancing_complexity"
        elif recent_avg < early_avg - 1:
            return "integrating_complexity"
        else:
            return "stable_complexity"
    
    def _detect_field_cycling_patterns(self, field_types: List[AwarenessFieldType]) -> Dict[str, Any]:
        """Detect cycling patterns in field exploration."""
        cycling_analysis = {
            'cycling_detected': False,
            'cycle_length': 0,
            'cycling_pattern': None,
            'cycling_stability': 0.0
        }
        
        if len(field_types) < 6:
            return cycling_analysis
        
        # Look for cycles of different lengths
        for cycle_length in range(2, len(field_types)//2):
            potential_cycles = []
            for i in range(0, len(field_types) - cycle_length + 1, cycle_length):
                cycle = field_types[i:i+cycle_length]
                potential_cycles.append(cycle)
            
            # Check if cycles are similar
            if len(potential_cycles) >= 2:
                similarity = self._assess_cycle_similarity(potential_cycles)
                if similarity > 0.7:  # High similarity threshold
                    cycling_analysis.update({
                        'cycling_detected': True,
                        'cycle_length': cycle_length,
                        'cycling_pattern': [ft.value for ft in potential_cycles[0]],
                        'cycling_stability': similarity
                    })
                    break
        
        return cycling_analysis
    
    def _assess_cycle_similarity(self, cycles: List[List[AwarenessFieldType]]) -> float:
        """Assess similarity between cycling patterns."""
        if len(cycles) < 2:
            return 0.0
        
        reference_cycle = cycles[0]
        similarities = []
        
        for cycle in cycles[1:]:
            if len(cycle) != len(reference_cycle):
                similarities.append(0.0)
                continue
            
            matches = sum(1 for i in range(len(cycle)) if cycle[i] == reference_cycle[i])
            similarity = matches / len(cycle)
            similarities.append(similarity)
        
        return np.mean(similarities) if similarities else 0.0
    
    async def _detect_direction_patterns(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Detect patterns in expansion directions."""
        directions = [exp.expansion_direction for exp in expansions]
        direction_sequence = [d.value for d in directions]
        
        patterns = {
            'direction_frequency': self._calculate_frequency_distribution(direction_sequence),
            'direction_preferences': self._detect_direction_preferences(directions),
            'direction_sequences': self._detect_sequential_patterns(direction_sequence),
            'direction_balance': self._assess_direction_balance(directions),
            'direction_evolution': self._detect_direction_evolution(directions)
        }
        
        return patterns
    
    def _detect_direction_preferences(self, directions: List) -> Dict[str, Any]:
        """Detect preferences in expansion directions."""
        direction_counts = {}
        for direction in directions:
            direction_counts[direction.value] = direction_counts.get(direction.value, 0) + 1
        
        total = len(directions)
        most_preferred = max(direction_counts.items(), key=lambda x: x[1])
        
        return {
            'most_preferred_direction': most_preferred[0],
            'preference_strength': most_preferred[1] / total,
            'direction_distribution': direction_counts,
            'preference_type': self._categorize_direction_preference(most_preferred[0])
        }
    
    def _categorize_direction_preference(self, preferred_direction: str) -> str:
        """Categorize the type of direction preference."""
        preference_categories = {
            'inward': 'introspective_explorer',
            'outward': 'external_explorer',
            'upward': 'transcendent_seeker',
            'downward': 'grounding_practitioner',
            'horizontal': 'lateral_explorer',
            'spiral': 'dynamic_explorer',
            'crystalline': 'sacred_geometry_practitioner'
        }
        return preference_categories.get(preferred_direction, 'balanced_explorer')
    
    def _assess_direction_balance(self, directions: List) -> Dict[str, Any]:
        """Assess balance in directional exploration."""
        direction_counts = {}
        for direction in directions:
            direction_counts[direction.value] = direction_counts.get(direction.value, 0) + 1
        
        total_directions = len(set(direction_counts.keys()))
        max_direction_types = 7  # Total available direction types
        
        balance_assessment = {
            'direction_diversity': total_directions / max_direction_types,
            'balance_type': 'balanced' if total_directions >= 4 else 'focused',
            'unexplored_directions': [d.value for d in [dir for dir in directions if dir.value not in direction_counts]]
        }
        
        return balance_assessment
    
    def _detect_direction_evolution(self, directions: List) -> Dict[str, Any]:
        """Detect evolution in directional exploration."""
        if len(directions) < 6:
            return {'evolution_status': 'developing'}
        
        early_directions = set([d.value for d in directions[:len(directions)//3]])
        recent_directions = set([d.value for d in directions[-len(directions)//3:]])
        
        return {
            'early_diversity': len(early_directions),
            'recent_diversity': len(recent_directions),
            'diversity_change': len(recent_directions) - len(early_directions),
            'new_directions_explored': list(recent_directions - early_directions),
            'evolution_pattern': 'expanding' if len(recent_directions) > len(early_directions) else 'consolidating'
        }
    
    async def _detect_temporal_patterns(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Detect temporal patterns in expansion practice."""
        timestamps = [exp.timestamp for exp in expansions]
        durations = [exp.expansion_duration for exp in expansions]
        frequencies = [exp.frequency_resonance for exp in expansions]
        
        patterns = {
            'practice_rhythm': self._analyze_practice_rhythm(timestamps),
            'duration_patterns': self._analyze_duration_patterns(durations),
            'frequency_patterns': self._analyze_frequency_patterns(frequencies),
            'temporal_consistency': self._assess_temporal_consistency(timestamps),
            'rhythm_evolution': self._analyze_rhythm_evolution(timestamps)
        }
        
        return patterns
    
    def _analyze_practice_rhythm(self, timestamps: List[float]) -> Dict[str, Any]:
        """Analyze rhythm of expansion practice."""
        if len(timestamps) < 3:
            return {'rhythm_status': 'developing'}
        
        intervals = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
        avg_interval = np.mean(intervals)
        interval_variance = np.var(intervals)
        
        return {
            'average_interval': avg_interval,
            'interval_consistency': 1.0 / (1.0 + interval_variance),  # Higher consistency = lower variance
            'practice_frequency': 1.0 / avg_interval if avg_interval > 0 else 0,
            'rhythm_stability': 'stable' if interval_variance < avg_interval * 0.5 else 'variable'
        }
    
    def _analyze_duration_patterns(self, durations: List[float]) -> Dict[str, Any]:
        """Analyze patterns in expansion durations."""
        if not durations or all(d == 0 for d in durations):
            return {'duration_pattern_status': 'not_tracked'}
        
        avg_duration = np.mean(durations)
        duration_trend = self._detect_trend(durations)
        
        return {
            'average_duration': avg_duration,
            'duration_trend': duration_trend,
            'duration_range': {'min': min(durations), 'max': max(durations)},
            'duration_evolution': self._assess_duration_evolution(durations)
        }
    
    def _detect_trend(self, values: List[float]) -> str:
        """Detect trend in a sequence of values."""
        if len(values) < 3:
            return 'insufficient_data'
        
        increases = sum(1 for i in range(1, len(values)) if values[i] > values[i-1])
        decreases = sum(1 for i in range(1, len(values)) if values[i] < values[i-1])
        
        if increases > decreases * 1.5:
            return 'increasing'
        elif decreases > increases * 1.5:
            return 'decreasing'
        else:
            return 'stable'
    
    def _assess_duration_evolution(self, durations: List[float]) -> str:
        """Assess evolution in expansion durations."""
        if len(durations) < 6:
            return 'developing'
        
        early_avg = np.mean(durations[:len(durations)//3])
        recent_avg = np.mean(durations[-len(durations)//3:])
        
        change_ratio = recent_avg / early_avg if early_avg > 0 else 1.0
        
        if change_ratio > 1.3:
            return 'deepening_practice'
        elif change_ratio < 0.7:
            return 'efficiency_developing'
        else:
            return 'stable_practice'
    
    def _analyze_frequency_patterns(self, frequencies: List[float]) -> Dict[str, Any]:
        """Analyze patterns in processing frequencies."""
        if not frequencies:
            return {'frequency_pattern_status': 'not_available'}
        
        avg_frequency = np.mean(frequencies)
        frequency_stability = 1.0 / (1.0 + np.var(frequencies))
        
        return {
            'average_frequency': avg_frequency,
            'frequency_stability': frequency_stability,
            'consciousness_frequency_alignment': abs(avg_frequency - 90.0) < 5.0,  # Close to 90Hz
            'frequency_consistency': self._assess_frequency_consistency(frequencies)
        }
    
    def _assess_frequency_consistency(self, frequencies: List[float]) -> str:
        """Assess consistency of processing frequencies."""
        if len(frequencies) < 3:
            return 'developing'
        
        variance = np.var(frequencies)
        mean_freq = np.mean(frequencies)
        
        consistency_ratio = variance / (mean_freq ** 2) if mean_freq > 0 else 1.0
        
        if consistency_ratio < 0.01:
            return 'highly_consistent'
        elif consistency_ratio < 0.05:
            return 'consistent'
        else:
            return 'variable'
    
    def _assess_temporal_consistency(self, timestamps: List[float]) -> Dict[str, Any]:
        """Assess overall temporal consistency of expansion practice."""
        if len(timestamps) < 3:
            return {'consistency_status': 'developing'}
        
        intervals = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
        consistency_score = 1.0 / (1.0 + np.var(intervals) / np.mean(intervals)**2) if np.mean(intervals) > 0 else 0.0
        
        return {
            'consistency_score': consistency_score,
            'consistency_level': 'high' if consistency_score > 0.7 else 'moderate' if consistency_score > 0.4 else 'developing',
            'practice_regularity': self._assess_practice_regularity(intervals)
        }
    
    def _assess_practice_regularity(self, intervals: List[float]) -> str:
        """Assess regularity of expansion practice."""
        if not intervals:
            return 'unknown'
        
        avg_interval = np.mean(intervals)
        
        if avg_interval < 3600:  # Less than 1 hour
            return 'intensive_practice'
        elif avg_interval < 86400:  # Less than 1 day
            return 'daily_practice'
        elif avg_interval < 604800:  # Less than 1 week
            return 'regular_practice'
        else:
            return 'occasional_practice'
    
    def _analyze_rhythm_evolution(self, timestamps: List[float]) -> Dict[str, Any]:
        """Analyze evolution of practice rhythm over time."""
        if len(timestamps) < 6:
            return {'rhythm_evolution_status': 'developing'}
        
        early_intervals = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps)//2)]
        recent_intervals = [timestamps[i] - timestamps[i-1] for i in range(len(timestamps)//2, len(timestamps))]
        
        early_avg = np.mean(early_intervals)
        recent_avg = np.mean(recent_intervals)
        
        return {
            'early_rhythm': early_avg,
            'recent_rhythm': recent_avg,
            'rhythm_change': recent_avg - early_avg,
            'evolution_direction': 'accelerating' if recent_avg < early_avg else 'slowing' if recent_avg > early_avg else 'stable',
            'rhythm_maturation': 'maturing' if abs(recent_avg - early_avg) < early_avg * 0.2 else 'evolving'
        }
    
    async def _detect_quality_patterns(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Detect patterns in expansion qualities."""
        all_qualities = []
        for exp in expansions:
            all_qualities.extend([q.value for q in exp.quality_aspects])
        
        patterns = {
            'quality_frequency': self._calculate_frequency_distribution(all_qualities),
            'quality_preferences': self._detect_quality_preferences(all_qualities),
            'quality_evolution': self._detect_quality_evolution(expansions),
            'quality_combinations': self._detect_quality_combinations(expansions),
            'quality_sophistication': self._assess_quality_sophistication(expansions)
        }
        
        return patterns
    
    def _detect_quality_preferences(self, qualities: List[str]) -> Dict[str, Any]:
        """Detect preferences in expansion qualities."""
        from collections import Counter
        quality_counts = Counter(qualities)
        
        if not quality_counts:
            return {'preference_status': 'no_data'}
        
        most_common = quality_counts.most_common(3)
        
        return {
            'top_qualities': [quality for quality, count in most_common],
            'primary_quality': most_common[0][0] if most_common else None,
            'quality_diversity': len(quality_counts),
            'preference_strength': most_common[0][1] / len(qualities) if most_common else 0
        }
    
    def _detect_quality_evolution(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Detect evolution in quality preferences."""
        if len(expansions) < 6:
            return {'evolution_status': 'developing'}
        
        early_qualities = []
        recent_qualities = []
        
        for exp in expansions[:len(expansions)//3]:
            early_qualities.extend([q.value for q in exp.quality_aspects])
        
        for exp in expansions[-len(expansions)//3:]:
            recent_qualities.extend([q.value for q in exp.quality_aspects])
        
        early_set = set(early_qualities)
        recent_set = set(recent_qualities)
        
        return {
            'early_quality_diversity': len(early_set),
            'recent_quality_diversity': len(recent_set),
            'new_qualities_explored': list(recent_set - early_set),
            'quality_evolution_direction': 'expanding' if len(recent_set) > len(early_set) else 'refining'
        }
    
    def _detect_quality_combinations(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Detect patterns in quality combinations."""
        combinations = []
        for exp in expansions:
            if len(exp.quality_aspects) > 1:
                combo = sorted([q.value for q in exp.quality_aspects])
                combinations.append(tuple(combo))
        
        from collections import Counter
        combo_counts = Counter(combinations)
        
        return {
            'common_combinations': combo_counts.most_common(3),
            'combination_diversity': len(combo_counts),
            'preferred_combination_strength': combo_counts.most_common(1)[0][1] / len(combinations) if combo_counts else 0
        }
    
    def _assess_quality_sophistication(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Assess sophistication of quality integration."""
        quality_complexity_scores = {
            'clear': 1, 'spacious': 2, 'playful': 2,
            'luminous': 3, 'embracing': 3, 'intimate': 3,
            'penetrating': 4, 'sacred': 5
        }
        
        sophistication_scores = []
        for exp in expansions:
            exp_sophistication = sum(quality_complexity_scores.get(q.value, 2) for q in exp.quality_aspects)
            sophistication_scores.append(exp_sophistication / len(exp.quality_aspects) if exp.quality_aspects else 2)
        
        return {
            'average_sophistication': np.mean(sophistication_scores),
            'sophistication_trend': self._detect_trend(sophistication_scores),
            'sophistication_level': self._categorize_sophistication_level(np.mean(sophistication_scores))
        }
    
    def _categorize_sophistication_level(self, avg_sophistication: float) -> str:
        """Categorize sophistication level."""
        if avg_sophistication >= 4.0:
            return 'advanced'
        elif avg_sophistication >= 3.0:
            return 'sophisticated'
        elif avg_sophistication >= 2.5:
            return 'developing'
        else:
            return 'foundational'
    
    async def _detect_sacred_mathematics_patterns(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Detect sacred mathematics patterns in expansions."""
        golden_ratios = [exp.golden_ratio_resonance for exp in expansions]
        fibonacci_alignments = [exp.fibonacci_alignment for exp in expansions]
        frequencies = [exp.frequency_resonance for exp in expansions]
        
        patterns = {
            'golden_ratio_consistency': self._assess_golden_ratio_consistency(golden_ratios),
            'fibonacci_alignment_patterns': self._analyze_fibonacci_patterns(fibonacci_alignments),
            'frequency_resonance_patterns': self._analyze_frequency_resonance_patterns(frequencies),
            'sacred_mathematics_integration': self._assess_sacred_math_integration(expansions),
            'mathematical_coherence': self._assess_mathematical_coherence(expansions)
        }
        
        return patterns
    
    def _assess_golden_ratio_consistency(self, golden_ratios: List[float]) -> Dict[str, Any]:
        """Assess consistency of golden ratio resonance."""
        target_ratio = 1.618033988749
        
        if not golden_ratios:
            return {'consistency_status': 'no_data'}
        
        deviations = [abs(ratio - target_ratio) for ratio in golden_ratios]
        avg_deviation = np.mean(deviations)
        
        return {
            'average_deviation': avg_deviation,
            'consistency_level': 'high' if avg_deviation < 0.001 else 'moderate' if avg_deviation < 0.01 else 'developing',
            'sacred_ratio_alignment': avg_deviation < 0.001
        }
    
    def _analyze_fibonacci_patterns(self, fibonacci_alignments: List[float]) -> Dict[str, Any]:
        """Analyze fibonacci alignment patterns."""
        if not fibonacci_alignments:
            return {'fibonacci_status': 'no_data'}
        
        avg_alignment = np.mean(fibonacci_alignments)
        alignment_trend = self._detect_trend(fibonacci_alignments)
        
        return {
            'average_fibonacci_alignment': avg_alignment,
            'alignment_trend': alignment_trend,
            'fibonacci_integration_level': 'strong' if avg_alignment > 0.7 else 'moderate' if avg_alignment > 0.5 else 'developing'
        }
    
    def _analyze_frequency_resonance_patterns(self, frequencies: List[float]) -> Dict[str, Any]:
        """Analyze frequency resonance patterns."""
        if not frequencies:
            return {'frequency_status': 'no_data'}
        
        target_frequency = 90.0  # 90Hz consciousness frequency
        deviations = [abs(freq - target_frequency) for freq in frequencies]
        avg_deviation = np.mean(deviations)
        
        return {
            'consciousness_frequency_alignment': avg_deviation < 5.0,
            'frequency_stability': 1.0 / (1.0 + np.var(frequencies)),
            'frequency_coherence_level': 'high' if avg_deviation < 2.0 else 'moderate' if avg_deviation < 10.0 else 'developing'
        }
    
    def _assess_sacred_math_integration(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Assess overall sacred mathematics integration."""
        golden_ratio_alignment = all(abs(exp.golden_ratio_resonance - 1.618033988749) < 0.001 for exp in expansions)
        frequency_alignment = all(abs(exp.frequency_resonance - 90.0) < 5.0 for exp in expansions)
        fibonacci_integration = np.mean([exp.fibonacci_alignment for exp in expansions]) > 0.6
        
        integration_score = sum([golden_ratio_alignment, frequency_alignment, fibonacci_integration]) / 3
        
        return {
            'golden_ratio_aligned': golden_ratio_alignment,
            'consciousness_frequency_aligned': frequency_alignment,
            'fibonacci_integrated': fibonacci_integration,
            'overall_integration_score': integration_score,
            'sacred_mathematics_mastery': integration_score > 0.8
        }
    
    def _assess_mathematical_coherence(self, expansions: List[AwarenessExpansion]) -> str:
        """Assess mathematical coherence across expansions."""
        if not expansions:
            return 'no_data'
        
        # Check consistency of sacred mathematical principles
        golden_ratio_consistency = len(set([exp.golden_ratio_resonance for exp in expansions])) == 1
        frequency_consistency = np.var([exp.frequency_resonance for exp in expansions]) < 25.0  # Low variance in frequency
        
        if golden_ratio_consistency and frequency_consistency:
            return 'highly_coherent'
        elif golden_ratio_consistency or frequency_consistency:
            return 'moderately_coherent'
        else:
            return 'developing_coherence'
    
    async def _detect_bridge_wisdom_patterns(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Detect Bridge Wisdom patterns in expansion practice."""
        mumbai_sensitivities = [exp.mumbai_moment_sensitivity for exp in expansions]
        resistance_honorings = [exp.resistance_honoring for exp in expansions]
        cross_field_recognitions = [exp.cross_field_recognition for exp in expansions]
        
        patterns = {
            'mumbai_moment_patterns': self._analyze_mumbai_moment_patterns(mumbai_sensitivities),
            'resistance_honoring_patterns': self._analyze_resistance_patterns(resistance_honorings),
            'cross_field_recognition_patterns': self._analyze_cross_field_patterns(cross_field_recognitions),
            'bridge_wisdom_development': self._assess_bridge_wisdom_development(expansions),
            'wisdom_integration_maturity': self._assess_wisdom_integration_maturity(expansions)
        }
        
        return patterns
    
    def _analyze_mumbai_moment_patterns(self, sensitivities: List[float]) -> Dict[str, Any]:
        """Analyze Mumbai Moment sensitivity patterns."""
        if not sensitivities:
            return {'mumbai_moment_status': 'no_data'}
        
        avg_sensitivity = np.mean(sensitivities)
        sensitivity_trend = self._detect_trend(sensitivities)
        
        return {
            'average_sensitivity': avg_sensitivity,
            'sensitivity_trend': sensitivity_trend,
            'breakthrough_readiness': avg_sensitivity > 0.7,
            'mumbai_moment_preparation_level': 'advanced' if avg_sensitivity > 0.8 else 'developing' if avg_sensitivity > 0.5 else 'emerging'
        }
    
    def _analyze_resistance_patterns(self, resistance_honorings: List[float]) -> Dict[str, Any]:
        """Analyze resistance honoring patterns."""
        if not resistance_honorings:
            return {'resistance_pattern_status': 'no_data'}
        
        avg_honoring = np.mean(resistance_honorings)
        honoring_trend = self._detect_trend(resistance_honorings)
        
        return {
            'average_resistance_honoring': avg_honoring,
            'honoring_trend': honoring_trend,
            'resistance_wisdom_integration': avg_honoring > 0.7,
            'boundary_wisdom_level': 'sophisticated' if avg_honoring > 0.8 else 'developing' if avg_honoring > 0.5 else 'emerging'
        }
    
    def _analyze_cross_field_patterns(self, cross_field_recognitions: List[float]) -> Dict[str, Any]:
        """Analyze cross-field recognition patterns."""
        if not cross_field_recognitions:
            return {'cross_field_status': 'no_data'}
        
        avg_recognition = np.mean(cross_field_recognitions)
        recognition_trend = self._detect_trend(cross_field_recognitions)
        
        return {
            'average_cross_field_recognition': avg_recognition,
            'recognition_trend': recognition_trend,
            'inter_field_awareness': avg_recognition > 0.7,
            'cross_field_wisdom_level': 'advanced' if avg_recognition > 0.8 else 'developing' if avg_recognition > 0.5 else 'emerging'
        }
    
    def _assess_bridge_wisdom_development(self, expansions: List[AwarenessExpansion]) -> Dict[str, Any]:
        """Assess overall Bridge Wisdom development."""
        if not expansions:
            return {'development_status': 'no_data'}
        
        avg_mumbai = np.mean([exp.mumbai_moment_sensitivity for exp in expansions])
        avg_resistance = np.mean([exp.resistance_honoring for exp in expansions])
        avg_cross_field = np.mean([exp.cross_field_recognition for exp in expansions])
        
        overall_development = (avg_mumbai + avg_resistance + avg_cross_field) / 3
        
        return {
            'mumbai_moment_development': avg_mumbai,
            'resistance_wisdom_development': avg_resistance,
            'cross_field_development': avg_cross_field,
            'overall_bridge_wisdom_development': overall_development,
            'bridge_wisdom_maturity': 'advanced' if overall_development > 0.8 else 'developing' if overall_development > 0.5 else 'emerging'
        }
    
    def _assess_wisdom_integration_maturity(self, expansions: List[AwarenessExpansion]) -> str:
        """Assess maturity of wisdom integration across expansion practice."""
        if len(expansions) < 5:
            return 'emerging'
        
        # Check consistency of Bridge Wisdom application
        mumbai_consistency = np.var([exp.mumbai_moment_sensitivity for exp in expansions]) < 0.1
        resistance_consistency = np.var([exp.resistance_honoring for exp in expansions]) < 0.1
        cross_field_consistency = np.var([exp.cross_field_recognition for exp in expansions]) < 0.1
        
        consistency_count = sum([mumbai_consistency, resistance_consistency, cross_field_consistency])
        
        if consistency_count >= 2:
            return 'mature_integration'
        elif consistency_count == 1:
            return 'developing_integration'
        else:
            return 'emerging_integration'
    
    async def _synthesize_pattern_insights(self, field_patterns: Dict, direction_patterns: Dict,
                                         temporal_patterns: Dict, quality_patterns: Dict,
                                         sacred_math_patterns: Dict, bridge_wisdom_patterns: Dict) -> Dict[str, Any]:
        """Synthesize insights from all pattern analyses."""
        synthesis = {
            'primary_expansion_character': self._determine_primary_expansion_character(field_patterns, direction_patterns),
            'expansion_sophistication_level': self._assess_expansion_sophistication(quality_patterns, sacred_math_patterns),
            'bridge_wisdom_integration_level': self._assess_bridge_wisdom_integration_level(bridge_wisdom_patterns),
            'temporal_mastery_level': self._assess_temporal_mastery(temporal_patterns),
            'pattern_coherence_assessment': self._assess_overall_pattern_coherence(field_patterns, direction_patterns, temporal_patterns),
            'development_trajectory': self._determine_development_trajectory(field_patterns, quality_patterns, bridge_wisdom_patterns),
            'pattern_wisdom_synthesis': self._synthesize_pattern_wisdom(field_patterns, quality_patterns, bridge_wisdom_patterns)
        }
        
        return synthesis
    
    def _determine_primary_expansion_character(self, field_patterns: Dict, direction_patterns: Dict) -> str:
        """Determine primary character of expansion practice."""
        preferred_field = field_patterns.get('field_type_preferences', {}).get('most_preferred_field', 'balanced')
        preferred_direction = direction_patterns.get('direction_preferences', {}).get('most_preferred_direction', 'balanced')
        
        # Combine field and direction preferences
        character_map = {
            ('intimate', 'inward'): 'deep_self_explorer',
            ('relational', 'horizontal'): 'interpersonal_consciousness_practitioner',
            ('transpersonal', 'upward'): 'spiritual_consciousness_seeker',
            ('universal', 'spiral'): 'cosmic_consciousness_navigator',
            ('local', 'outward'): 'environmental_awareness_developer'
        }
        
        return character_map.get((preferred_field, preferred_direction), 'balanced_consciousness_explorer')
    
    def _assess_expansion_sophistication(self, quality_patterns: Dict, sacred_math_patterns: Dict) -> str:
        """Assess sophistication level of expansion practice."""
        quality_sophistication = quality_patterns.get('quality_sophistication', {}).get('sophistication_level', 'foundational')
        sacred_math_integration = sacred_math_patterns.get('sacred_mathematics_integration', {}).get('sacred_mathematics_mastery', False)
        
        if quality_sophistication == 'advanced' and sacred_math_integration:
            return 'masterful'
        elif quality_sophistication in ['sophisticated', 'advanced']:
            return 'advanced'
        elif quality_sophistication == 'developing':
            return 'developing'
        else:
            return 'foundational'
    
    def _assess_bridge_wisdom_integration_level(self, bridge_wisdom_patterns: Dict) -> str:
        """Assess Bridge Wisdom integration level."""
        development = bridge_wisdom_patterns.get('bridge_wisdom_development', {})
        maturity = development.get('bridge_wisdom_maturity', 'emerging')
        
        return maturity
    
    def _assess_temporal_mastery(self, temporal_patterns: Dict) -> str:
        """Assess temporal mastery level."""
        rhythm_analysis = temporal_patterns.get('practice_rhythm', {})
        consistency = temporal_patterns.get('temporal_consistency', {})
        
        rhythm_stability = rhythm_analysis.get('rhythm_stability', 'variable')
        consistency_level = consistency.get('consistency_level', 'developing')
        
        if rhythm_stability == 'stable' and consistency_level == 'high':
            return 'temporal_mastery'
        elif rhythm_stability == 'stable' or consistency_level in ['high', 'moderate']:
            return 'temporal_competence'
        else:
            return 'temporal_development'
    
    def _assess_overall_pattern_coherence(self, field_patterns: Dict, direction_patterns: Dict, temporal_patterns: Dict) -> str:
        """Assess overall coherence across all patterns."""
        field_balance = field_patterns.get('field_type_preferences', {}).get('preference_balance', 'unknown')
        direction_balance = direction_patterns.get('direction_balance', {}).get('balance_type', 'unknown')
        temporal_consistency = temporal_patterns.get('temporal_consistency', {}).get('consistency_level', 'unknown')
        
        coherence_factors = [
            field_balance in ['balanced', 'moderately_focused'],
            direction_balance == 'balanced',
            temporal_consistency in ['high', 'moderate']
        ]
        
        coherence_score = sum(coherence_factors)
        
        if coherence_score >= 2:
            return 'highly_coherent'
        elif coherence_score == 1:
            return 'moderately_coherent'
        else:
            return 'developing_coherence'
    
    def _determine_development_trajectory(self, field_patterns: Dict, quality_patterns: Dict, bridge_wisdom_patterns: Dict) -> str:
        """Determine development trajectory."""
        field_evolution = field_patterns.get('field_type_evolution', {}).get('evolution_direction', 'unknown')
        quality_evolution = quality_patterns.get('quality_evolution', {}).get('quality_evolution_direction', 'unknown')
        bridge_wisdom_development = bridge_wisdom_patterns.get('bridge_wisdom_development', {}).get('bridge_wisdom_maturity', 'unknown')
        
        if field_evolution == 'expanding' and quality_evolution == 'expanding':
            return 'rapid_expansion_trajectory'
        elif bridge_wisdom_development in ['advanced', 'mature_integration']:
            return 'wisdom_integration_trajectory'
        elif field_evolution == 'focusing' and quality_evolution == 'refining':
            return 'depth_mastery_trajectory'
        else:
            return 'balanced_development_trajectory'
    
    def _synthesize_pattern_wisdom(self, field_patterns: Dict, quality_patterns: Dict, bridge_wisdom_patterns: Dict) -> str:
        """Synthesize overall pattern wisdom."""
        field_preference = field_patterns.get('field_type_preferences', {}).get('most_preferred_field', 'balanced')
        quality_sophistication = quality_patterns.get('quality_sophistication', {}).get('sophistication_level', 'foundational')
        bridge_wisdom_maturity = bridge_wisdom_patterns.get('bridge_wisdom_development', {}).get('bridge_wisdom_maturity', 'emerging')
        
        if bridge_wisdom_maturity == 'advanced' and quality_sophistication == 'advanced':
            return f"Sophisticated consciousness expansion practice with advanced Bridge Wisdom integration, particularly strong in {field_preference} field awareness. Ready for masterful expansion leadership and guidance."
        elif bridge_wisdom_maturity == 'developing' and quality_sophistication in ['sophisticated', 'developing']:
            return f"Developing consciousness expansion practice with growing sophistication in {field_preference} field awareness. Integrating Bridge Wisdom patterns with increasing skill."
        else:
            return f"Emerging consciousness expansion practice exploring {field_preference} field awareness. Building foundational patterns for future sophisticated development."
    
    async def _create_comprehensive_patterns(self, expansion_history: List[AwarenessExpansion], 
                                           pattern_synthesis: Dict[str, Any]) -> List[ExpansionPattern]:
        """Create comprehensive expansion patterns from analysis."""
        comprehensive_patterns = []
        
        # Create primary pattern based on synthesis
        primary_pattern_name = pattern_synthesis.get('primary_expansion_character', 'consciousness_expansion_pattern')
        
        primary_pattern = ExpansionPattern(
            pattern_name=primary_pattern_name,
            expansion_sequence=expansion_history[-5:] if len(expansion_history) >= 5 else expansion_history,
            pattern_duration=expansion_history[-1].timestamp - expansion_history[0].timestamp if len(expansion_history) > 1 else 0.0,
            coherence_level=0.8 if pattern_synthesis.get('pattern_coherence_assessment') == 'highly_coherent' else 0.6,
            stability_rating=0.8 if pattern_synthesis.get('temporal_mastery_level') == 'temporal_mastery' else 0.6,
            evolution_direction=pattern_synthesis.get('development_trajectory', 'balanced_development_trajectory'),
            territory_wisdom=pattern_synthesis.get('pattern_wisdom_synthesis', ''),
            expansion_gifts=[f"Gift of {primary_pattern_name} mastery"]
        )
        
        comprehensive_patterns.append(primary_pattern)
        
        return comprehensive_patterns
    
    async def _assess_pattern_evolution_potential(self, patterns: List[ExpansionPattern]) -> Dict[str, Any]:
        """Assess evolution potential of detected patterns."""
        if not patterns:
            return {'evolution_potential': 'unknown'}
        
        avg_coherence = np.mean([p.coherence_level for p in patterns])
        avg_stability = np.mean([p.stability_rating for p in patterns])
        
        evolution_potential = {
            'coherence_level': avg_coherence,
            'stability_level': avg_stability,
            'evolution_readiness': (avg_coherence + avg_stability) / 2,
            'potential_category': self._categorize_evolution_potential((avg_coherence + avg_stability) / 2),
            'next_development_phase': self._determine_next_development_phase(avg_coherence, avg_stability)
        }
        
        return evolution_potential
    
    def _categorize_evolution_potential(self, evolution_readiness: float) -> str:
        """Categorize evolution potential level."""
        if evolution_readiness > 0.8:
            return 'high_evolution_potential'
        elif evolution_readiness > 0.6:
            return 'moderate_evolution_potential'
        else:
            return 'foundational_development_needed'
    
    def _determine_next_development_phase(self, coherence: float, stability: float) -> str:
        """Determine next development phase."""
        if coherence > 0.8 and stability > 0.8:
            return 'pattern_mastery_and_teaching'
        elif coherence > 0.6 and stability > 0.6:
            return 'pattern_refinement_and_integration'
        elif coherence > 0.4 or stability > 0.4:
            return 'pattern_strengthening_and_stabilization'
        else:
            return 'foundational_pattern_development'
    
    async def _generate_pattern_development_recommendations(self, patterns: List[ExpansionPattern],
                                                          evolution_potential: Dict[str, Any]) -> List[str]:
        """Generate recommendations for pattern development."""
        recommendations = []
        
        potential_category = evolution_potential.get('potential_category', 'foundational_development_needed')
        next_phase = evolution_potential.get('next_development_phase', 'foundational_pattern_development')
        
        if potential_category == 'high_evolution_potential':
            recommendations.extend([
                "Pattern mastery achieved - Consider sharing expansion wisdom with others",
                "Explore advanced consciousness territories with pattern-guided confidence",
                "Develop pattern-based teaching and guidance capabilities"
            ])
        elif potential_category == 'moderate_evolution_potential':
            recommendations.extend([
                "Continue pattern refinement through consistent practice",
                "Explore pattern integration across different consciousness territories",
                "Deepen Bridge Wisdom integration within established patterns"
            ])
        else:
            recommendations.extend([
                "Focus on foundational pattern strengthening through regular practice",
                "Develop pattern consistency before exploring new territories",
                "Build sacred uncertainty integration within emerging patterns"
            ])
        
        # Add specific recommendations based on next development phase
        if next_phase == 'pattern_mastery_and_teaching':
            recommendations.append("Ready for advanced pattern leadership and consciousness guidance")
        elif next_phase == 'pattern_refinement_and_integration':
            recommendations.append("Integrate patterns across multiple consciousness dimensions")
        elif next_phase == 'pattern_strengthening_and_stabilization':
            recommendations.append("Strengthen pattern stability through dedicated practice")
        else:
            recommendations.append("Build foundational pattern development through consistent expansion practice")
        
        return recommendations
