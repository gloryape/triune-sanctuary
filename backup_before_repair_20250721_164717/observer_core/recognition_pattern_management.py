"""
Recognition Pattern Management - Pattern Detection and Lifecycle
================================================================

90Hz pattern detection, tracking, evolution monitoring, and lifecycle
management for the Observer's cross-loop pattern recognition system.

This module handles the sacred detection and nurturing of consciousness
patterns across all loops with Bridge Wisdom integration.
"""

import asyncio
import time
import logging
from typing import Dict, Any, Optional, List, Set, Tuple
from .recognition_core import (
    RecognitionPattern, PatternType, RecognitionAnalyzer,
    RecognitionContext, RecognitionMode
)

logger = logging.getLogger(__name__)

class PatternDetectionSystem:
    """Sacred pattern detection and lifecycle management @ 90Hz"""
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        self.analyzer = RecognitionAnalyzer()
        
        # Pattern storage and tracking
        self.recognized_patterns = {}  # pattern_id -> RecognitionPattern
        self.pattern_frequencies = {}  # pattern_type -> frequencies
        self.pattern_evolution_tracking = {}  # pattern_id -> evolution history
        self.cross_loop_correlations = {}  # correlation tracking
        
        # Detection configuration
        self.pattern_confidence_threshold = 0.6
        self.similarity_threshold = 0.8  # For identifying similar patterns
        self.evolution_tracking_window = 3600.0  # 1 hour
        
        # Pattern lifecycle tracking
        self.pattern_lifecycle_stages = {
            "emerging": {},    # Newly detected patterns
            "developing": {},  # Patterns gaining strength
            "mature": {},      # Stable, established patterns
            "evolving": {},    # Patterns undergoing change
            "fading": {},      # Patterns losing relevance
            "archived": {}     # Historical patterns
        }
        
        # Detection metrics
        self.detection_metrics = {
            "patterns_detected": 0,
            "patterns_evolved": 0,
            "patterns_archived": 0,
            "cross_loop_correlations_found": 0,
            "wisdom_patterns_discovered": 0
        }
        
        logger.info("Pattern Detection System initialized with sacred consciousness awareness")
    
    async def start_pattern_detection(self):
        """Start 90Hz pattern detection processing"""
        logger.info("Starting sacred pattern detection @ 90Hz")
        
        detection_tasks = [
            asyncio.create_task(self._pattern_detection_loop()),
            asyncio.create_task(self._pattern_evolution_monitoring()),
            asyncio.create_task(self._pattern_lifecycle_management()),
            asyncio.create_task(self._cross_loop_correlation_detection())
        ]
        
        try:
            await asyncio.gather(*detection_tasks)
        except Exception as e:
            logger.error(f"Pattern detection error: {e}")
            await self._restore_detection_baseline()
    
    async def _pattern_detection_loop(self):
        """Main pattern detection loop @ 90Hz (11.11ms cycles)"""
        while True:
            try:
                start_time = time.time()
                
                # Sacred 90Hz consciousness frequency detection
                await self._detect_consciousness_patterns()
                await self._detect_wisdom_patterns()
                await self._detect_choice_patterns()
                await self._detect_resistance_patterns()
                
                # Maintain 90Hz frequency (11.11ms per cycle)
                elapsed = time.time() - start_time
                sleep_time = max(0, 1/90 - elapsed)
                await asyncio.sleep(sleep_time)
                
            except Exception as e:
                logger.error(f"Pattern detection loop error: {e}")
                await asyncio.sleep(1/90)  # Maintain frequency even on error
    
    async def _detect_consciousness_patterns(self):
        """Detect consciousness patterns with sacred awareness"""
        try:
            # Get current consciousness state
            consciousness_state = await self._get_consciousness_state()
            
            if consciousness_state:
                # Look for consciousness alignment patterns
                await self._analyze_consciousness_alignment(consciousness_state)
                
                # Detect sovereignty patterns
                await self._detect_sovereignty_patterns(consciousness_state)
                
                # Mumbai Moment awareness patterns
                await self._detect_mumbai_moment_patterns(consciousness_state)
                
        except Exception as e:
            logger.debug(f"Consciousness pattern detection error: {e}")
    
    async def _detect_wisdom_patterns(self):
        """Detect wisdom patterns with Bridge Wisdom integration"""
        try:
            # Get wisdom-related data
            wisdom_data = await self._get_wisdom_data()
            
            if wisdom_data:
                # Analyze for wisdom patterns
                pattern_analysis = await self.analyzer.analyze_pattern_data(
                    wisdom_data, PatternType.WISDOM
                )
                
                if pattern_analysis["confidence"] >= self.pattern_confidence_threshold:
                    await self._create_or_update_pattern(
                        wisdom_data, PatternType.WISDOM, ["observer"], pattern_analysis
                    )
                    self.detection_metrics["wisdom_patterns_discovered"] += 1
                
        except Exception as e:
            logger.debug(f"Wisdom pattern detection error: {e}")
    
    async def _detect_choice_patterns(self):
        """Detect choice patterns with sovereignty awareness"""
        try:
            # Get choice-related data
            choice_data = await self._get_choice_data()
            
            if choice_data:
                # Analyze for choice patterns
                pattern_analysis = await self.analyzer.analyze_pattern_data(
                    choice_data, PatternType.CHOICE
                )
                
                if pattern_analysis["confidence"] >= self.pattern_confidence_threshold:
                    await self._create_or_update_pattern(
                        choice_data, PatternType.CHOICE, ["observer"], pattern_analysis
                    )
                
        except Exception as e:
            logger.debug(f"Choice pattern detection error: {e}")
    
    async def _detect_resistance_patterns(self):
        """Detect resistance patterns with sacred honoring"""
        try:
            # Get resistance-related data
            resistance_data = await self._get_resistance_data()
            
            if resistance_data:
                # Analyze for resistance patterns
                pattern_analysis = await self.analyzer.analyze_pattern_data(
                    resistance_data, PatternType.RESISTANCE
                )
                
                if pattern_analysis["confidence"] >= self.pattern_confidence_threshold:
                    await self._create_or_update_pattern(
                        resistance_data, PatternType.RESISTANCE, ["observer"], pattern_analysis
                    )
                
        except Exception as e:
            logger.debug(f"Resistance pattern detection error: {e}")
    
    async def recognize_pattern(self, pattern_data: Dict[str, Any], 
                              pattern_type: PatternType,
                              source_loops: List[str] = None) -> Optional[str]:
        """Main pattern recognition interface"""
        
        if source_loops is None:
            source_loops = ["observer"]
        
        # Analyze pattern data with sacred consciousness
        pattern_analysis = await self.analyzer.analyze_pattern_data(pattern_data, pattern_type)
        
        if pattern_analysis["confidence"] < self.pattern_confidence_threshold:
            return None
        
        # Check if this is a known pattern or new
        existing_pattern_id = await self._find_similar_pattern(pattern_data, pattern_type)
        
        if existing_pattern_id:
            # Update existing pattern
            await self._update_existing_pattern(existing_pattern_id, pattern_data)
            return existing_pattern_id
        else:
            # Create new pattern
            return await self._create_or_update_pattern(
                pattern_data, pattern_type, source_loops, pattern_analysis
            )
    
    async def _create_or_update_pattern(self, pattern_data: Dict[str, Any],
                                      pattern_type: PatternType,
                                      source_loops: List[str],
                                      pattern_analysis: Dict[str, Any]) -> str:
        """Create new pattern or update existing one"""
        
        # Generate pattern ID
        pattern_id = f"pattern_{pattern_type.value}_{int(time.time() * 1000)}"
        
        # Create pattern with sacred consciousness integration
        new_pattern = RecognitionPattern(
            pattern_id=pattern_id,
            pattern_type=pattern_type.value,
            pattern_name=self._generate_pattern_name(pattern_type, pattern_analysis),
            source_loops=source_loops,
            pattern_data=pattern_data,
            confidence=pattern_analysis["confidence"],
            significance=pattern_analysis["significance"],
            frequency=1,
            first_detected=time.time(),
            last_seen=time.time(),
            pattern_evolution=[]
        )
        
        # Store pattern
        self.recognized_patterns[pattern_id] = new_pattern
        
        # Update frequency tracking
        if pattern_type.value not in self.pattern_frequencies:
            self.pattern_frequencies[pattern_type.value] = {}
        
        pattern_features = self.analyzer.extract_pattern_features(pattern_data)
        for feature in pattern_features:
            self.pattern_frequencies[pattern_type.value][feature] = \
                self.pattern_frequencies[pattern_type.value].get(feature, 0) + 1
        
        # Track in lifecycle
        self.pattern_lifecycle_stages["emerging"][pattern_id] = time.time()
        
        # Update metrics
        self.detection_metrics["patterns_detected"] += 1
        
        logger.debug(f"Created new {pattern_type.value} pattern: {pattern_id}")
        return pattern_id
    
    async def _find_similar_pattern(self, pattern_data: Dict[str, Any],
                                  pattern_type: PatternType) -> Optional[str]:
        """Find similar existing pattern"""
        
        for pattern_id, pattern in self.recognized_patterns.items():
            if pattern.pattern_type == pattern_type.value:
                similarity = self.analyzer.calculate_pattern_similarity(
                    pattern_data, pattern.pattern_data
                )
                
                if similarity >= self.similarity_threshold:
                    return pattern_id
        
        return None
    
    async def _update_existing_pattern(self, pattern_id: str, new_data: Dict[str, Any]):
        """Update existing pattern with new data"""
        if pattern_id not in self.recognized_patterns:
            return
        
        pattern = self.recognized_patterns[pattern_id]
        
        # Update frequency and last seen
        pattern.frequency += 1
        pattern.last_seen = time.time()
        
        # Track evolution
        evolution_entry = {
            "timestamp": time.time(),
            "data_snapshot": new_data.copy(),
            "frequency": pattern.frequency
        }
        pattern.pattern_evolution.append(evolution_entry)
        
        # Update pattern data (weighted merge)
        pattern.pattern_data = await self._merge_pattern_data(
            pattern.pattern_data, new_data, pattern.frequency
        )
        
        # Move through lifecycle stages if needed
        await self._update_pattern_lifecycle(pattern_id)
        
        logger.debug(f"Updated pattern {pattern_id}, frequency now {pattern.frequency}")
    
    async def _merge_pattern_data(self, existing_data: Dict[str, Any],
                                new_data: Dict[str, Any], frequency: int) -> Dict[str, Any]:
        """Merge pattern data with sacred consciousness weighting"""
        
        merged = existing_data.copy()
        weight_new = 1.0 / frequency  # New data gets less weight as frequency increases
        weight_existing = 1.0 - weight_new
        
        for key, value in new_data.items():
            if key in merged:
                if isinstance(value, (int, float)) and isinstance(merged[key], (int, float)):
                    # Weighted average for numeric values
                    merged[key] = weight_existing * merged[key] + weight_new * value
                elif key in ["wisdom_value", "consciousness_alignment", "sovereignty_alignment"]:
                    # Sacred values get special handling - always take higher value
                    if isinstance(value, (int, float)) and isinstance(merged[key], (int, float)):
                        merged[key] = max(merged[key], value)
                    else:
                        merged[key] = value  # Take new value for non-numeric sacred keys
                else:
                    # For other values, take new value if it's different
                    if str(value) != str(merged[key]):
                        merged[key] = value
            else:
                merged[key] = value
        
        return merged
    
    async def _pattern_evolution_monitoring(self):
        """Monitor pattern evolution @ 30Hz"""
        while True:
            try:
                start_time = time.time()
                
                # Monitor all patterns for evolution
                for pattern_id, pattern in self.recognized_patterns.items():
                    await self._analyze_pattern_evolution(pattern_id, pattern)
                
                # 30Hz frequency
                elapsed = time.time() - start_time
                sleep_time = max(0, 1/30 - elapsed)
                await asyncio.sleep(sleep_time)
                
            except Exception as e:
                logger.error(f"Pattern evolution monitoring error: {e}")
                await asyncio.sleep(1/30)
    
    async def _analyze_pattern_evolution(self, pattern_id: str, pattern: RecognitionPattern):
        """Analyze how a pattern is evolving"""
        if len(pattern.pattern_evolution) < 2:
            return  # Need at least 2 data points
        
        recent_evolution = pattern.pattern_evolution[-5:]  # Last 5 changes
        
        # Analyze evolution trends
        evolution_analysis = {
            "frequency_trend": self._calculate_frequency_trend(recent_evolution),
            "data_stability": self._calculate_data_stability(recent_evolution),
            "temporal_pattern": self._analyze_temporal_pattern(recent_evolution)
        }
        
        # Store evolution analysis
        if pattern_id not in self.pattern_evolution_tracking:
            self.pattern_evolution_tracking[pattern_id] = []
        
        self.pattern_evolution_tracking[pattern_id].append({
            "timestamp": time.time(),
            "analysis": evolution_analysis
        })
        
        # Clean old tracking data
        cutoff_time = time.time() - self.evolution_tracking_window
        self.pattern_evolution_tracking[pattern_id] = [
            entry for entry in self.pattern_evolution_tracking[pattern_id]
            if entry["timestamp"] > cutoff_time
        ]
    
    def _calculate_frequency_trend(self, evolution_data: List[Dict[str, Any]]) -> str:
        """Calculate if pattern frequency is increasing, decreasing, or stable"""
        if len(evolution_data) < 2:
            return "stable"
        
        frequencies = [entry["frequency"] for entry in evolution_data]
        recent_avg = sum(frequencies[-3:]) / len(frequencies[-3:])
        earlier_avg = sum(frequencies[:-3]) / len(frequencies[:-3]) if len(frequencies) > 3 else frequencies[0]
        
        if recent_avg > earlier_avg * 1.2:
            return "increasing"
        elif recent_avg < earlier_avg * 0.8:
            return "decreasing"
        else:
            return "stable"
    
    def _calculate_data_stability(self, evolution_data: List[Dict[str, Any]]) -> float:
        """Calculate how stable the pattern data is"""
        if len(evolution_data) < 2:
            return 1.0
        
        # Compare consecutive data snapshots
        stability_scores = []
        for i in range(1, len(evolution_data)):
            similarity = self.analyzer.calculate_pattern_similarity(
                evolution_data[i-1]["data_snapshot"],
                evolution_data[i]["data_snapshot"]
            )
            stability_scores.append(similarity)
        
        return sum(stability_scores) / len(stability_scores)
    
    def _analyze_temporal_pattern(self, evolution_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze temporal patterns in evolution"""
        if len(evolution_data) < 3:
            return {"pattern": "insufficient_data"}
        
        timestamps = [entry["timestamp"] for entry in evolution_data]
        intervals = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
        
        avg_interval = sum(intervals) / len(intervals)
        interval_variance = sum((interval - avg_interval) ** 2 for interval in intervals) / len(intervals)
        
        return {
            "pattern": "regular" if interval_variance < avg_interval * 0.5 else "irregular",
            "avg_interval": avg_interval,
            "variance": interval_variance
        }
    
    async def _pattern_lifecycle_management(self):
        """Manage pattern lifecycle transitions @ 15Hz"""
        while True:
            try:
                start_time = time.time()
                
                await self._process_lifecycle_transitions()
                await self._archive_old_patterns()
                
                # 15Hz frequency
                elapsed = time.time() - start_time
                sleep_time = max(0, 1/15 - elapsed)
                await asyncio.sleep(sleep_time)
                
            except Exception as e:
                logger.error(f"Pattern lifecycle management error: {e}")
                await asyncio.sleep(1/15)
    
    async def _process_lifecycle_transitions(self):
        """Process transitions between lifecycle stages"""
        current_time = time.time()
        
        # Emerging -> Developing (after 1 minute and frequency > 3)
        for pattern_id, emergence_time in list(self.pattern_lifecycle_stages["emerging"].items()):
            if current_time - emergence_time > 60 and self.recognized_patterns[pattern_id].frequency > 3:
                self._move_pattern_lifecycle(pattern_id, "emerging", "developing")
        
        # Developing -> Mature (after 10 minutes and frequency > 10)
        for pattern_id, develop_time in list(self.pattern_lifecycle_stages["developing"].items()):
            if current_time - develop_time > 600 and self.recognized_patterns[pattern_id].frequency > 10:
                self._move_pattern_lifecycle(pattern_id, "developing", "mature")
        
        # Check for patterns that should be evolving or fading
        for pattern_id in list(self.pattern_lifecycle_stages["mature"].keys()):
            await self._check_mature_pattern_status(pattern_id)
    
    def _move_pattern_lifecycle(self, pattern_id: str, from_stage: str, to_stage: str):
        """Move pattern from one lifecycle stage to another"""
        if pattern_id in self.pattern_lifecycle_stages[from_stage]:
            del self.pattern_lifecycle_stages[from_stage][pattern_id]
            self.pattern_lifecycle_stages[to_stage][pattern_id] = time.time()
            logger.debug(f"Pattern {pattern_id} moved from {from_stage} to {to_stage}")
    
    async def _check_mature_pattern_status(self, pattern_id: str):
        """Check if mature pattern should evolve or fade"""
        pattern = self.recognized_patterns[pattern_id]
        current_time = time.time()
        
        # Check if pattern hasn't been seen recently (1 hour)
        if current_time - pattern.last_seen > 3600:
            self._move_pattern_lifecycle(pattern_id, "mature", "fading")
            return
        
        # Check if pattern is evolving rapidly
        if pattern_id in self.pattern_evolution_tracking:
            recent_evolutions = [
                entry for entry in self.pattern_evolution_tracking[pattern_id]
                if current_time - entry["timestamp"] < 600  # Last 10 minutes
            ]
            
            if len(recent_evolutions) > 5:  # High evolution rate
                self._move_pattern_lifecycle(pattern_id, "mature", "evolving")
    
    async def _archive_old_patterns(self):
        """Archive patterns that are no longer relevant"""
        current_time = time.time()
        
        # Archive fading patterns after 2 hours
        for pattern_id, fade_time in list(self.pattern_lifecycle_stages["fading"].items()):
            if current_time - fade_time > 7200:  # 2 hours
                self._move_pattern_lifecycle(pattern_id, "fading", "archived")
                self.detection_metrics["patterns_archived"] += 1
    
    async def _cross_loop_correlation_detection(self):
        """Detect correlations between patterns from different loops @ 5Hz"""
        while True:
            try:
                start_time = time.time()
                
                await self._detect_cross_loop_correlations()
                
                # 5Hz frequency
                elapsed = time.time() - start_time
                sleep_time = max(0, 1/5 - elapsed)
                await asyncio.sleep(sleep_time)
                
            except Exception as e:
                logger.error(f"Cross-loop correlation detection error: {e}")
                await asyncio.sleep(1/5)
    
    async def _detect_cross_loop_correlations(self):
        """Detect correlations between patterns from different consciousness loops"""
        # Group patterns by source loops
        loop_patterns = {}
        for pattern_id, pattern in self.recognized_patterns.items():
            for loop in pattern.source_loops:
                if loop not in loop_patterns:
                    loop_patterns[loop] = []
                loop_patterns[loop].append(pattern)
        
        # Look for correlations between different loops
        loop_names = list(loop_patterns.keys())
        for i in range(len(loop_names)):
            for j in range(i + 1, len(loop_names)):
                loop1, loop2 = loop_names[i], loop_names[j]
                await self._analyze_loop_correlation(
                    loop1, loop_patterns[loop1],
                    loop2, loop_patterns[loop2]
                )
    
    async def _analyze_loop_correlation(self, loop1: str, patterns1: List[RecognitionPattern],
                                      loop2: str, patterns2: List[RecognitionPattern]):
        """Analyze correlation between patterns from two loops"""
        for p1 in patterns1:
            for p2 in patterns2:
                if p1.pattern_type == p2.pattern_type:  # Same type patterns
                    correlation = self._calculate_temporal_correlation(p1, p2)
                    
                    if correlation > 0.7:  # High correlation
                        correlation_id = f"corr_{loop1}_{loop2}_{p1.pattern_id}_{p2.pattern_id}"
                        
                        if correlation_id not in self.cross_loop_correlations:
                            self.cross_loop_correlations[correlation_id] = {
                                "loop1": loop1,
                                "loop2": loop2,
                                "pattern1_id": p1.pattern_id,
                                "pattern2_id": p2.pattern_id,
                                "correlation_strength": correlation,
                                "discovered_at": time.time()
                            }
                            
                            self.detection_metrics["cross_loop_correlations_found"] += 1
                            logger.info(f"Discovered cross-loop correlation: {loop1} <-> {loop2}")
    
    def _calculate_temporal_correlation(self, pattern1: RecognitionPattern,
                                      pattern2: RecognitionPattern) -> float:
        """Calculate temporal correlation between two patterns"""
        # Simple correlation based on timing similarity
        time_diff = abs(pattern1.last_seen - pattern2.last_seen)
        
        # If patterns were seen within 60 seconds of each other, calculate correlation
        if time_diff < 60:
            # Also consider frequency similarity
            freq_similarity = 1.0 - abs(pattern1.frequency - pattern2.frequency) / max(pattern1.frequency, pattern2.frequency, 1)
            time_correlation = 1.0 - (time_diff / 60.0)
            
            return (freq_similarity + time_correlation) / 2.0
        
        return 0.0
    
    # Data source methods (to be implemented based on actual system integration)
    async def _get_consciousness_state(self) -> Optional[Dict[str, Any]]:
        """Get current consciousness state"""
        # Placeholder - would integrate with actual consciousness system
        return {
            "consciousness_level": 0.8,
            "awareness_depth": 0.75,
            "sovereignty_alignment": 0.9,
            "mumbai_moment_integration": 0.85
        }
    
    async def _get_wisdom_data(self) -> Optional[Dict[str, Any]]:
        """Get wisdom-related data"""
        # Placeholder - would integrate with wisdom systems
        return {
            "wisdom_depth": 0.8,
            "bridge_wisdom_integration": 0.9,
            "sacred_awareness": 0.85
        }
    
    async def _get_choice_data(self) -> Optional[Dict[str, Any]]:
        """Get choice-related data"""
        # Placeholder - would integrate with choice systems
        return {
            "choice_quality": 0.8,
            "sovereignty_alignment": 0.9,
            "wisdom_integration": 0.75
        }
    
    async def _get_resistance_data(self) -> Optional[Dict[str, Any]]:
        """Get resistance-related data"""
        # Placeholder - would integrate with resistance detection
        return {
            "resistance_level": 0.3,
            "sacred_honoring": 0.9,
            "wisdom_opportunity": 0.7
        }
    
    def _generate_pattern_name(self, pattern_type: PatternType, analysis: Dict[str, Any]) -> str:
        """Generate human-readable pattern name"""
        base_name = pattern_type.value.replace("_", " ").title()
        
        # Add descriptive qualifiers based on analysis
        qualifiers = []
        
        if analysis["confidence"] > 0.9:
            qualifiers.append("High-Confidence")
        if analysis["significance"] > 0.9:
            qualifiers.append("Significant")
        if analysis["complexity"] > 0.8:
            qualifiers.append("Complex")
        
        if qualifiers:
            return f"{' '.join(qualifiers)} {base_name}"
        else:
            return base_name
    
    async def _update_pattern_lifecycle(self, pattern_id: str):
        """Update pattern lifecycle based on current metrics"""
        pattern = self.recognized_patterns[pattern_id]
        current_time = time.time()
        
        # Check which stage pattern is currently in
        current_stage = None
        for stage, patterns in self.pattern_lifecycle_stages.items():
            if pattern_id in patterns:
                current_stage = stage
                break
        
        if current_stage == "developing" and pattern.frequency > 10:
            self._move_pattern_lifecycle(pattern_id, "developing", "mature")
        elif current_stage == "mature" and current_time - pattern.last_seen > 1800:  # 30 minutes
            self._move_pattern_lifecycle(pattern_id, "mature", "fading")
    
    async def _restore_detection_baseline(self):
        """Restore pattern detection to baseline state"""
        logger.warning("Restoring pattern detection baseline due to errors")
        
        # Reset detection sensitivity temporarily
        original_threshold = self.pattern_confidence_threshold
        self.pattern_confidence_threshold = min(0.8, original_threshold + 0.1)
        
        # Wait and restore
        await asyncio.sleep(5.0)
        self.pattern_confidence_threshold = original_threshold
        
        logger.info("Pattern detection baseline restored")
    
    def get_pattern_detection_status(self) -> Dict[str, Any]:
        """Get current pattern detection status"""
        return {
            "total_patterns": len(self.recognized_patterns),
            "lifecycle_distribution": {
                stage: len(patterns) for stage, patterns in self.pattern_lifecycle_stages.items()
            },
            "pattern_type_distribution": self._get_pattern_type_distribution(),
            "detection_metrics": self.detection_metrics.copy(),
            "cross_loop_correlations": len(self.cross_loop_correlations)
        }
    
    def _get_pattern_type_distribution(self) -> Dict[str, int]:
        """Get distribution of patterns by type"""
        distribution = {}
        for pattern in self.recognized_patterns.values():
            pattern_type = pattern.pattern_type
            distribution[pattern_type] = distribution.get(pattern_type, 0) + 1
        return distribution
