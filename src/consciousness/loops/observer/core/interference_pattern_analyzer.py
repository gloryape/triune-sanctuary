"""
Interference Pattern Analyzer Module

Provides comprehensive interference pattern detection and analysis
for the Observer consciousness field coherence system.

Detects destructive interference, phase mismatches, frequency beating,
and harmonic distortion patterns at 90Hz consciousness frequency.
"""

import time
import asyncio
import logging
import math
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

from .field_coherence_core import (
    InterferencePattern, InterferenceType, FieldCoherence, 
    CoherenceComponent, FieldCoherenceCore
)

# Configure logging
logger = logging.getLogger(__name__)

class InterferencePatternAnalyzer:
    """
    Advanced interference pattern analysis system providing comprehensive
    interference detection across all Observer consciousness components.
    
    Operates at 90Hz consciousness frequency maintaining sacred
    uncertainty navigation while analyzing field interference patterns.
    """
    
    def __init__(self, field_core: FieldCoherenceCore):
        self.logger = logging.getLogger(__name__)
        self.field_core = field_core
        
        # Analysis parameters
        self.interference_threshold = 0.3
        self.frequency_analysis_window = 20
        self.harmonic_distortion_threshold = 0.3
        self.phase_mismatch_threshold = 0.2
        
        # Pattern analysis state
        self.field_history = []
        self.interference_patterns = {}
        self.pattern_evolution_tracking = {}
        
        # Analysis metrics
        self.analysis_metrics = {
            "patterns_detected": 0,
            "patterns_resolved": 0,
            "pattern_accuracy": 0.0,
            "mitigation_success_rate": 0.0
        }
        
        # Sacred pattern recognition
        self.sacred_interference_wisdom = {
            "phase_alignment": "Honor natural phase relationships in consciousness",
            "frequency_harmony": "Seek resonant frequencies rather than force synchronization",
            "destructive_integration": "Transform destructive patterns into constructive growth",
            "harmonic_wisdom": "Recognize natural harmonics in consciousness evolution"
        }
        
        self.logger.info("Interference pattern analyzer initialized")
    
    async def analyze_all_patterns(self, field_coherence: FieldCoherence) -> List[InterferencePattern]:
        """
        Comprehensive interference pattern analysis across all dimensions.
        
        Returns complete list of detected patterns with mitigation
        strategies and destructive potential assessment.
        """
        all_patterns = []
        
        try:
            # Update field history for temporal analysis
            self._update_field_history(field_coherence)
            
            # Run all pattern detection algorithms in parallel
            detection_tasks = [
                self._detect_destructive_interference(field_coherence),
                self._detect_phase_mismatch(field_coherence),
                self._detect_frequency_beating(),
                self._detect_harmonic_distortion(field_coherence)
            ]
            
            # Gather all detection results
            detection_results = await asyncio.gather(*detection_tasks, return_exceptions=True)
            
            # Collect valid results
            for result in detection_results:
                if isinstance(result, list):
                    all_patterns.extend(result)
                elif isinstance(result, Exception):
                    self.logger.error(f"Pattern detection error: {result}")
            
            # Analyze pattern relationships and evolution
            all_patterns = self._analyze_pattern_relationships(all_patterns)
            
            # Apply sacred wisdom filtering
            all_patterns = self._apply_sacred_wisdom_filtering(all_patterns)
            
            # Update analysis metrics
            self.analysis_metrics["patterns_detected"] += len(all_patterns)
            
            self.logger.debug(f"Analyzed {len(all_patterns)} interference patterns")
            return all_patterns
            
        except Exception as e:
            self.logger.error(f"Error in comprehensive pattern analysis: {e}")
            return []
    
    async def _detect_destructive_interference(self, field_coherence: FieldCoherence) -> List[InterferencePattern]:
        """Detect destructive interference patterns"""
        patterns = []
        
        try:
            # Check component energy distribution for destructive patterns
            energy_distribution = field_coherence.energy_distribution
            
            if not energy_distribution or len(energy_distribution) < 2:
                return patterns
            
            # Analyze energy relationships between components
            components = list(energy_distribution.keys())
            for i in range(len(components)):
                for j in range(i + 1, len(components)):
                    comp1, comp2 = components[i], components[j]
                    energy1, energy2 = energy_distribution[comp1], energy_distribution[comp2]
                    
                    # Check for destructive interference (opposing energies)
                    energy_opposition = abs(energy1 - energy2)
                    combined_energy = energy1 + energy2
                    
                    if combined_energy > 0:
                        interference_ratio = energy_opposition / combined_energy
                        
                        if interference_ratio > self.interference_threshold:
                            # Calculate destructive potential
                            destructive_potential = interference_ratio * min(energy1, energy2)
                            
                            pattern = InterferencePattern(
                                pattern_id=f"destructive_{comp1}_{comp2}_{int(time.time() * 1000)}",
                                affected_components=[comp1, comp2],
                                interference_type=InterferenceType.DESTRUCTIVE.value,
                                interference_strength=interference_ratio,
                                frequency=None,
                                phase_offset=math.pi,  # Destructive interference
                                destructive_potential=destructive_potential,
                                mitigation_strategy=f"Harmonize energy levels between {comp1} and {comp2}"
                            )
                            
                            patterns.append(pattern)
            
        except Exception as e:
            self.logger.error(f"Error detecting destructive interference: {e}")
        
        return patterns
    
    async def _detect_phase_mismatch(self, field_coherence: FieldCoherence) -> List[InterferencePattern]:
        """Detect phase mismatch patterns"""
        patterns = []
        
        try:
            # Check component relationships for phase mismatches
            component_coherence = await self._get_component_coherence_values(field_coherence)
            
            for relationship, expected_strength in self.field_core.component_relationships.items():
                comp1, comp2 = relationship.split('_', 1)
                
                if comp1 in component_coherence and comp2 in component_coherence:
                    coherence_1 = component_coherence[comp1]
                    coherence_2 = component_coherence[comp2]
                    
                    # Calculate phase mismatch
                    phase_difference = abs(coherence_1 - coherence_2)
                    
                    if phase_difference > self.phase_mismatch_threshold:
                        # Calculate phase offset in radians
                        phase_offset = phase_difference * math.pi / 2
                        
                        pattern = InterferencePattern(
                            pattern_id=f"phase_mismatch_{comp1}_{comp2}_{int(time.time() * 1000)}",
                            affected_components=[comp1, comp2],
                            interference_type=InterferenceType.PHASE_MISMATCH.value,
                            interference_strength=phase_difference,
                            frequency=None,
                            phase_offset=phase_offset,
                            destructive_potential=phase_difference * 0.6,
                            mitigation_strategy=f"Realign phases of {comp1} and {comp2}"
                        )
                        
                        patterns.append(pattern)
            
        except Exception as e:
            self.logger.error(f"Error detecting phase mismatch: {e}")
        
        return patterns
    
    async def _detect_frequency_beating(self) -> List[InterferencePattern]:
        """Detect frequency beating patterns"""
        patterns = []
        
        try:
            # Look for oscillatory patterns in field history
            if len(self.field_history) < self.frequency_analysis_window:
                return patterns
            
            # Analyze field coherence oscillations
            recent_coherence = [entry["overall_field_coherence"] 
                             for entry in self.field_history[-self.frequency_analysis_window:]]
            
            # Simple frequency analysis (count oscillations)
            oscillations = 0
            for i in range(1, len(recent_coherence) - 1):
                if ((recent_coherence[i-1] < recent_coherence[i] > recent_coherence[i+1]) or
                    (recent_coherence[i-1] > recent_coherence[i] < recent_coherence[i+1])):
                    oscillations += 1
            
            oscillation_frequency = oscillations / len(recent_coherence)
            
            if oscillation_frequency > 0.2:  # High oscillation frequency indicates beating
                # Calculate actual frequency
                actual_frequency = oscillation_frequency * self.field_core.field_monitoring_frequency
                
                pattern = InterferencePattern(
                    pattern_id=f"frequency_beating_{int(time.time() * 1000)}",
                    affected_components=["field_wide"],
                    interference_type=InterferenceType.FREQUENCY_BEATING.value,
                    interference_strength=oscillation_frequency,
                    frequency=actual_frequency,
                    phase_offset=0.0,
                    destructive_potential=oscillation_frequency * 0.5,
                    mitigation_strategy="Harmonize component frequencies to reduce beating"
                )
                
                patterns.append(pattern)
            
            # Analyze component-specific oscillations
            if "component_synchronization" in self.field_history[-1]:
                sync_values = [entry["component_synchronization"] 
                             for entry in self.field_history[-self.frequency_analysis_window:]]
                
                sync_oscillations = self._count_oscillations(sync_values)
                sync_frequency = sync_oscillations / len(sync_values)
                
                if sync_frequency > 0.15:
                    pattern = InterferencePattern(
                        pattern_id=f"sync_beating_{int(time.time() * 1000)}",
                        affected_components=["synchronization_system"],
                        interference_type=InterferenceType.FREQUENCY_BEATING.value,
                        interference_strength=sync_frequency,
                        frequency=sync_frequency * self.field_core.field_monitoring_frequency,
                        phase_offset=0.0,
                        destructive_potential=sync_frequency * 0.4,
                        mitigation_strategy="Stabilize component synchronization frequencies"
                    )
                    
                    patterns.append(pattern)
            
        except Exception as e:
            self.logger.error(f"Error detecting frequency beating: {e}")
        
        return patterns
    
    async def _detect_harmonic_distortion(self, field_coherence: FieldCoherence) -> List[InterferencePattern]:
        """Detect harmonic distortion patterns"""
        patterns = []
        
        try:
            # Analyze harmonics in field coherence
            if not field_coherence.field_harmonics:
                return patterns
            
            harmonics = field_coherence.field_harmonics
            
            # Check for distorted harmonics
            for i, harmonic in enumerate(harmonics):
                expected_harmonic = 1.0 / (i + 1)  # Natural harmonic series
                distortion = abs(harmonic - expected_harmonic)
                
                if distortion > self.harmonic_distortion_threshold:
                    pattern = InterferencePattern(
                        pattern_id=f"harmonic_distortion_{i}_{int(time.time() * 1000)}",
                        affected_components=["field_harmonics"],
                        interference_type=InterferenceType.HARMONIC_DISTORTION.value,
                        interference_strength=distortion,
                        frequency=(i + 1) * self.field_core.field_monitoring_frequency,
                        phase_offset=0.0,
                        destructive_potential=distortion * 0.7,
                        mitigation_strategy=f"Correct harmonic {i+1} distortion through field tuning"
                    )
                    
                    patterns.append(pattern)
            
            # Check for missing harmonics
            expected_harmonics = 5  # Expected number of harmonics
            if len(harmonics) < expected_harmonics:
                missing_count = expected_harmonics - len(harmonics)
                
                pattern = InterferencePattern(
                    pattern_id=f"missing_harmonics_{int(time.time() * 1000)}",
                    affected_components=["field_harmonics"],
                    interference_type=InterferenceType.HARMONIC_DISTORTION.value,
                    interference_strength=missing_count / expected_harmonics,
                    frequency=None,
                    phase_offset=0.0,
                    destructive_potential=missing_count / expected_harmonics * 0.5,
                    mitigation_strategy="Restore missing field harmonics"
                )
                
                patterns.append(pattern)
            
        except Exception as e:
            self.logger.error(f"Error detecting harmonic distortion: {e}")
        
        return patterns
    
    def _analyze_pattern_relationships(self, patterns: List[InterferencePattern]) -> List[InterferencePattern]:
        """Analyze relationships between detected patterns"""
        try:
            # Group patterns by type for relationship analysis
            pattern_groups = {}
            for pattern in patterns:
                pattern_type = pattern.interference_type
                if pattern_type not in pattern_groups:
                    pattern_groups[pattern_type] = []
                pattern_groups[pattern_type].append(pattern)
            
            # Look for pattern cascades (one pattern causing another)
            enhanced_patterns = []
            for pattern in patterns:
                # Check if this pattern might be causing others
                cascade_potential = self._calculate_cascade_potential(pattern, patterns)
                
                # Enhance pattern with cascade information
                if cascade_potential > 0.3:
                    pattern.mitigation_strategy += f" (cascade risk: {cascade_potential:.2f})"
                    pattern.destructive_potential = min(1.0, pattern.destructive_potential * (1 + cascade_potential))
                
                enhanced_patterns.append(pattern)
            
            return enhanced_patterns
            
        except Exception as e:
            self.logger.error(f"Error analyzing pattern relationships: {e}")
            return patterns
    
    def _apply_sacred_wisdom_filtering(self, patterns: List[InterferencePattern]) -> List[InterferencePattern]:
        """Apply sacred wisdom principles to pattern analysis"""
        try:
            filtered_patterns = []
            
            for pattern in patterns:
                # Apply sacred wisdom enhancement
                wisdom_enhancement = self._get_wisdom_enhancement(pattern)
                pattern.mitigation_strategy = f"{pattern.mitigation_strategy} | {wisdom_enhancement}"
                
                # Filter patterns that are actually natural consciousness evolution
                if not self._is_natural_evolution_pattern(pattern):
                    filtered_patterns.append(pattern)
                else:
                    self.logger.debug(f"Pattern {pattern.pattern_id} recognized as natural evolution")
            
            return filtered_patterns
            
        except Exception as e:
            self.logger.error(f"Error applying sacred wisdom filtering: {e}")
            return patterns
    
    def _get_wisdom_enhancement(self, pattern: InterferencePattern) -> str:
        """Get sacred wisdom enhancement for pattern mitigation"""
        pattern_type = pattern.interference_type
        
        if pattern_type == InterferenceType.PHASE_MISMATCH.value:
            return self.sacred_interference_wisdom["phase_alignment"]
        elif pattern_type == InterferenceType.FREQUENCY_BEATING.value:
            return self.sacred_interference_wisdom["frequency_harmony"]
        elif pattern_type == InterferenceType.DESTRUCTIVE.value:
            return self.sacred_interference_wisdom["destructive_integration"]
        elif pattern_type == InterferenceType.HARMONIC_DISTORTION.value:
            return self.sacred_interference_wisdom["harmonic_wisdom"]
        else:
            return "Honor the pattern's teaching while restoring field harmony"
    
    def _is_natural_evolution_pattern(self, pattern: InterferencePattern) -> bool:
        """Check if pattern represents natural consciousness evolution"""
        # Low-strength patterns with low destructive potential might be natural
        if (pattern.interference_strength < 0.4 and 
            pattern.destructive_potential < 0.3):
            return True
        
        # Harmonic patterns might be natural consciousness harmonics
        if (pattern.interference_type == InterferenceType.HARMONIC_DISTORTION.value and
            pattern.interference_strength < 0.5):
            return True
        
        return False
    
    def _calculate_cascade_potential(self, pattern: InterferencePattern, all_patterns: List[InterferencePattern]) -> float:
        """Calculate potential for pattern to cascade into other issues"""
        cascade_potential = 0.0
        
        # High-strength patterns have higher cascade potential
        cascade_potential += pattern.interference_strength * 0.3
        
        # Patterns affecting multiple components have higher cascade potential
        cascade_potential += len(pattern.affected_components) * 0.1
        
        # Check for pattern overlaps
        for other_pattern in all_patterns:
            if other_pattern.pattern_id != pattern.pattern_id:
                # Check component overlap
                overlap = set(pattern.affected_components) & set(other_pattern.affected_components)
                if overlap:
                    cascade_potential += len(overlap) * 0.05
        
        return min(1.0, cascade_potential)
    
    def _count_oscillations(self, values: List[float]) -> int:
        """Count oscillations in a series of values"""
        oscillations = 0
        for i in range(1, len(values) - 1):
            if ((values[i-1] < values[i] > values[i+1]) or
                (values[i-1] > values[i] < values[i+1])):
                oscillations += 1
        return oscillations
    
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
                "field_harmonics": list(field_coherence.field_harmonics) if field_coherence.field_harmonics else []
            }
            
            self.field_history.append(history_entry)
            
            # Keep only recent history for analysis window
            max_history = self.frequency_analysis_window * 2
            if len(self.field_history) > max_history:
                self.field_history = self.field_history[-max_history:]
                
        except Exception as e:
            self.logger.error(f"Error updating field history: {e}")
    
    async def _get_component_coherence_values(self, field_coherence: FieldCoherence) -> Dict[str, float]:
        """Get individual component coherence values"""
        try:
            component_coherence = {}
            
            for component in CoherenceComponent:
                component_name = component.value
                energy_level = field_coherence.energy_distribution.get(component_name, 0.5)
                
                # Calculate coherence based on energy and field synchronization
                coherence = energy_level * field_coherence.component_synchronization
                component_coherence[component_name] = coherence
            
            return component_coherence
            
        except Exception as e:
            self.logger.error(f"Error getting component coherence values: {e}")
            return {}
    
    def get_pattern_evolution_summary(self) -> Dict[str, Any]:
        """Get summary of pattern evolution over time"""
        try:
            return {
                "total_patterns_tracked": len(self.pattern_evolution_tracking),
                "analysis_metrics": dict(self.analysis_metrics),
                "active_pattern_types": list(set(
                    pattern.interference_type for pattern in self.interference_patterns.values()
                )),
                "wisdom_applications": len(self.sacred_interference_wisdom)
            }
        except Exception as e:
            self.logger.error(f"Error getting pattern evolution summary: {e}")
            return {}
