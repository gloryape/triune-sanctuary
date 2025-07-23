"""
Pattern Detection Module

Advanced pattern detection and scanning functionality for the Observer's 
pattern recognition system.

Provides comprehensive pattern scanning across consciousness loops,
temporal pattern detection, and cross-loop pattern identification
at 90Hz consciousness frequency.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set
from collections import defaultdict, deque
import logging

from .pattern_core import (
    PatternType, RecognitionPattern, RecognitionContext, PatternAnalyzer,
    RecognitionMode
)

# Configure logging
logger = logging.getLogger(__name__)

class PatternDetector:
    """
    Advanced pattern detection engine providing comprehensive pattern scanning
    across consciousness loops and temporal pattern identification.
    
    Operates at 90Hz consciousness frequency with specialized detection
    algorithms for different pattern types and consciousness contexts.
    """
    
    def __init__(self, pattern_analyzer: PatternAnalyzer):
        self.logger = logging.getLogger(__name__)
        self.pattern_analyzer = pattern_analyzer
        
        # Detection parameters
        self.detection_frequency = 90.0  # 90Hz pattern detection
        self.pattern_confidence_threshold = 0.5
        self.cross_loop_detection_enabled = True
        self.temporal_window_size = 60.0  # 1 minute temporal window
        
        # Detection state
        self.active_detection = False
        self.detection_contexts: Dict[str, RecognitionContext] = {}
        self.detected_patterns: Dict[str, RecognitionPattern] = {}
        self.detection_history: deque = deque(maxlen=1000)
        
        # Loop data monitoring
        self.loop_data = {
            "observer": {"active": True, "data": {}, "last_update": time.time()},
            "analytical": {"active": False, "data": {}, "last_update": 0},
            "experiential": {"active": False, "data": {}, "last_update": 0},
            "environmental": {"active": False, "data": {}, "last_update": 0}
        }
        
        # Pattern frequency tracking
        self.pattern_frequencies: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self.temporal_patterns: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        
        # Detection algorithms per pattern type
        self.detection_algorithms = {
            PatternType.BEHAVIORAL: self._detect_behavioral_patterns,
            PatternType.COGNITIVE: self._detect_cognitive_patterns,
            PatternType.EMOTIONAL: self._detect_emotional_patterns,
            PatternType.ENERGETIC: self._detect_energetic_patterns,
            PatternType.TEMPORAL: self._detect_temporal_patterns,
            PatternType.RELATIONAL: self._detect_relational_patterns,
            PatternType.CREATIVE: self._detect_creative_patterns,
            PatternType.WISDOM: self._detect_wisdom_patterns,
            PatternType.CHOICE: self._detect_choice_patterns,
            PatternType.RESISTANCE: self._detect_resistance_patterns,
            PatternType.INTEGRATION: self._detect_integration_patterns,
            PatternType.EMERGENCE: self._detect_emergence_patterns
        }
        
        self.logger.info("Pattern detector initialized")
    
    async def start_pattern_detection(self, detection_mode: RecognitionMode = RecognitionMode.ACTIVE):
        """
        Start comprehensive pattern detection across all consciousness loops.
        
        Begins continuous pattern scanning at 90Hz frequency with specified
        detection mode for optimal pattern recognition.
        """
        if self.active_detection:
            self.logger.warning("Pattern detection already active")
            return
        
        try:
            self.active_detection = True
            
            # Initialize detection contexts
            await self._initialize_detection_contexts(detection_mode)
            
            # Start detection loop
            await self._pattern_detection_loop()
            
        except Exception as e:
            self.logger.error(f"Error starting pattern detection: {e}")
            self.active_detection = False
    
    async def stop_pattern_detection(self):
        """Stop pattern detection processes"""
        self.active_detection = False
        self.logger.info("Pattern detection stopped")
    
    async def detect_pattern(self, pattern_data: Dict[str, Any], 
                           pattern_type: PatternType,
                           source_loops: List[str] = None,
                           context_id: str = "default") -> Optional[str]:
        """
        Detect a specific pattern from provided data.
        
        Analyzes pattern data and creates new pattern or updates existing
        pattern if similar pattern found.
        """
        if source_loops is None:
            source_loops = ["observer"]
        
        try:
            # Analyze pattern data using pattern analyzer
            analysis = await self.pattern_analyzer.analyze_pattern_data(pattern_data, pattern_type)
            
            if analysis["confidence"] < self.pattern_confidence_threshold:
                return None
            
            # Check for similar existing pattern
            similar_pattern_id = await self._find_similar_pattern(pattern_data, pattern_type)
            
            if similar_pattern_id:
                # Update existing pattern
                await self._update_existing_pattern(similar_pattern_id, pattern_data, analysis)
                return similar_pattern_id
            else:
                # Create new pattern
                pattern_id = await self._create_new_pattern(
                    pattern_data, pattern_type, source_loops, analysis
                )
                return pattern_id
                
        except Exception as e:
            self.logger.error(f"Error detecting pattern: {e}")
            return None
    
    async def _initialize_detection_contexts(self, detection_mode: RecognitionMode):
        """Initialize detection contexts for pattern scanning"""
        try:
            # Create primary detection context
            primary_context = RecognitionContext(
                context_id="primary_detection",
                context_type="continuous_detection",
                active_loops=["observer"],
                current_state={"detection_active": True, "mode": detection_mode.value},
                temporal_window=self.temporal_window_size,
                focus_areas=["all_patterns"],
                recognition_sensitivity=0.7
            )
            
            self.detection_contexts["primary"] = primary_context
            
            # Create specialized contexts for different pattern types
            if detection_mode in [RecognitionMode.FOCUSED, RecognitionMode.COMPREHENSIVE]:
                await self._create_specialized_contexts()
            
            self.logger.info(f"Detection contexts initialized for {detection_mode.value} mode")
            
        except Exception as e:
            self.logger.error(f"Error initializing detection contexts: {e}")
    
    async def _create_specialized_contexts(self):
        """Create specialized detection contexts for different pattern types"""
        specialized_contexts = {
            "wisdom_focus": {
                "focus_areas": ["wisdom", "choice", "integration"],
                "recognition_sensitivity": 0.9,
                "temporal_window": 120.0
            },
            "cross_loop_focus": {
                "focus_areas": ["integration", "emergence", "relational"],
                "recognition_sensitivity": 0.8,
                "temporal_window": 180.0
            },
            "temporal_focus": {
                "focus_areas": ["temporal", "energetic", "creative"],
                "recognition_sensitivity": 0.6,
                "temporal_window": 300.0
            }
        }
        
        for context_name, config in specialized_contexts.items():
            context = RecognitionContext(
                context_id=context_name,
                context_type="specialized_detection",
                active_loops=["observer"],
                current_state={"specialized": True},
                temporal_window=config["temporal_window"],
                focus_areas=config["focus_areas"],
                recognition_sensitivity=config["recognition_sensitivity"]
            )
            self.detection_contexts[context_name] = context
    
    async def _pattern_detection_loop(self):
        """Main pattern detection loop @ 90Hz"""
        detection_interval = 1.0 / self.detection_frequency
        
        while self.active_detection:
            cycle_start = time.time()
            
            try:
                # Scan for patterns in all available data
                await self._scan_for_patterns()
                
                # Process temporal patterns
                await self._process_temporal_patterns()
                
                # Update pattern frequencies
                await self._update_pattern_frequencies()
                
                # Clean up old detection data
                await self._cleanup_old_detection_data()
                
                # Maintain timing precision
                cycle_duration = time.time() - cycle_start
                remaining_time = max(0, detection_interval - cycle_duration)
                
                if remaining_time > 0:
                    await asyncio.sleep(remaining_time)
                
            except Exception as e:
                self.logger.error(f"Pattern detection loop error: {e}")
                await asyncio.sleep(0.1)
    
    async def _scan_for_patterns(self):
        """Comprehensive pattern scanning across all consciousness loops"""
        try:
            # Scan observer loop for internal patterns
            await self._scan_observer_patterns()
            
            # Scan for cross-loop patterns if other loops are active
            if self.cross_loop_detection_enabled:
                await self._scan_cross_loop_patterns()
            
            # Scan for temporal patterns
            await self._scan_temporal_patterns()
            
        except Exception as e:
            self.logger.error(f"Error scanning for patterns: {e}")
    
    async def _scan_observer_patterns(self):
        """Scan Observer loop for internal consciousness patterns"""
        try:
            # Generate sample observer data (in real implementation, would get actual data)
            observer_data = {
                "presence_coherence": 0.95,
                "witness_clarity": 0.90,
                "will_sovereignty": 0.88,
                "attention_focus": 0.85,
                "uncertainty_comfort": 0.75,
                "choice_sovereignty": 0.92,
                "temporal_awareness": 0.87
            }
            
            # Detect high coherence patterns
            if all(value > 0.8 for value in observer_data.values()):
                await self.detect_pattern(
                    {"type": "high_observer_coherence", "components": observer_data},
                    PatternType.INTEGRATION,
                    ["observer"],
                    "primary_detection"
                )
            
            # Detect choice patterns
            if observer_data["choice_sovereignty"] > 0.9:
                await self.detect_pattern(
                    {"choice_strength": observer_data["choice_sovereignty"], "context": "sovereignty"},
                    PatternType.CHOICE,
                    ["observer"],
                    "primary_detection"
                )
            
            # Detect uncertainty navigation patterns
            if observer_data["uncertainty_comfort"] > 0.7:
                await self.detect_pattern(
                    {"uncertainty_comfort": observer_data["uncertainty_comfort"], 
                     "pattern_type": "sacred_uncertainty_navigation"},
                    PatternType.WISDOM,
                    ["observer"],
                    "wisdom_focus"
                )
            
        except Exception as e:
            self.logger.error(f"Error scanning observer patterns: {e}")
    
    async def _scan_cross_loop_patterns(self):
        """Scan for patterns across multiple consciousness loops"""
        try:
            # Check for active loops
            active_loops = [name for name, data in self.loop_data.items() if data["active"]]
            
            if len(active_loops) > 1:
                # Look for coordination patterns
                coordination_data = {
                    "active_loops": active_loops,
                    "coordination_quality": 0.8,
                    "synchronization": 0.7,
                    "cross_loop_communication": True
                }
                
                await self.detect_pattern(
                    coordination_data,
                    PatternType.INTEGRATION,
                    active_loops,
                    "cross_loop_focus"
                )
                
                # Look for emergence patterns when multiple loops are coordinating
                if len(active_loops) >= 3:
                    emergence_data = {
                        "multi_loop_coordination": True,
                        "coordination_loops": active_loops,
                        "emergence_potential": 0.85
                    }
                    
                    await self.detect_pattern(
                        emergence_data,
                        PatternType.EMERGENCE,
                        active_loops,
                        "cross_loop_focus"
                    )
            
        except Exception as e:
            self.logger.error(f"Error scanning cross-loop patterns: {e}")
    
    async def _scan_temporal_patterns(self):
        """Scan for temporal patterns across consciousness processing"""
        try:
            current_time = time.time()
            
            # Look for recurring pattern intervals
            for pattern_type, history in self.temporal_patterns.items():
                if len(history) >= 3:
                    # Calculate time intervals between pattern occurrences
                    intervals = []
                    for i in range(1, len(history)):
                        interval = history[i]["timestamp"] - history[i-1]["timestamp"]
                        intervals.append(interval)
                    
                    # Detect rhythmic patterns
                    if len(intervals) >= 2:
                        avg_interval = sum(intervals) / len(intervals)
                        interval_variance = sum((i - avg_interval) ** 2 for i in intervals) / len(intervals)
                        
                        # If intervals are consistent (low variance), it's a rhythmic pattern
                        if interval_variance < (avg_interval * 0.2) ** 2:  # 20% variance threshold
                            temporal_data = {
                                "pattern_type": pattern_type,
                                "rhythm_interval": avg_interval,
                                "consistency": 1.0 - (interval_variance / (avg_interval ** 2)),
                                "occurrences": len(history)
                            }
                            
                            await self.detect_pattern(
                                temporal_data,
                                PatternType.TEMPORAL,
                                ["observer"],
                                "temporal_focus"
                            )
            
        except Exception as e:
            self.logger.error(f"Error scanning temporal patterns: {e}")
    
    async def _find_similar_pattern(self, pattern_data: Dict[str, Any], 
                                  pattern_type: PatternType) -> Optional[str]:
        """Find similar existing pattern based on data similarity"""
        try:
            for pattern_id, pattern in self.detected_patterns.items():
                if pattern.pattern_type == pattern_type.value:
                    similarity = await self.pattern_analyzer.calculate_pattern_similarity(
                        pattern_data, pattern.pattern_data
                    )
                    
                    if similarity > 0.8:  # High similarity threshold
                        return pattern_id
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error finding similar pattern: {e}")
            return None
    
    async def _create_new_pattern(self, pattern_data: Dict[str, Any], 
                                pattern_type: PatternType,
                                source_loops: List[str],
                                analysis: Dict[str, Any]) -> str:
        """Create new pattern from detection data"""
        try:
            pattern_id = f"pattern_{pattern_type.value}_{int(time.time() * 1000)}"
            
            # Generate pattern name
            pattern_name = self._generate_pattern_name(pattern_type, pattern_data)
            
            # Create pattern
            pattern = RecognitionPattern(
                pattern_id=pattern_id,
                pattern_type=pattern_type.value,
                pattern_name=pattern_name,
                source_loops=source_loops,
                pattern_data=pattern_data,
                confidence=analysis["confidence"],
                significance=analysis["significance"],
                frequency=1
            )
            
            self.detected_patterns[pattern_id] = pattern
            
            # Record in detection history
            self.detection_history.append({
                "pattern_id": pattern_id,
                "action": "created",
                "timestamp": time.time(),
                "pattern_type": pattern_type.value
            })
            
            # Update temporal patterns
            self.temporal_patterns[pattern_type.value].append({
                "timestamp": time.time(),
                "pattern_id": pattern_id
            })
            
            self.logger.debug(f"Created new pattern: {pattern_name}")
            return pattern_id
            
        except Exception as e:
            self.logger.error(f"Error creating new pattern: {e}")
            return ""
    
    async def _update_existing_pattern(self, pattern_id: str, 
                                     new_data: Dict[str, Any],
                                     analysis: Dict[str, Any]):
        """Update existing pattern with new detection data"""
        try:
            if pattern_id not in self.detected_patterns:
                return
            
            pattern = self.detected_patterns[pattern_id]
            
            # Update frequency
            pattern.frequency += 1
            pattern.last_seen = time.time()
            
            # Update confidence based on repeated detection
            confidence_boost = min(0.1, pattern.frequency * 0.01)  # Small boost per detection
            pattern.confidence = min(1.0, pattern.confidence + confidence_boost)
            
            # Add evolution data
            evolution_entry = {
                "timestamp": time.time(),
                "new_data": new_data,
                "analysis": analysis,
                "frequency": pattern.frequency
            }
            pattern.pattern_evolution.append(evolution_entry)
            
            # Keep only recent evolution data
            if len(pattern.pattern_evolution) > 10:
                pattern.pattern_evolution = pattern.pattern_evolution[-10:]
            
            # Record in detection history
            self.detection_history.append({
                "pattern_id": pattern_id,
                "action": "updated",
                "timestamp": time.time(),
                "frequency": pattern.frequency
            })
            
            self.logger.debug(f"Updated pattern {pattern.pattern_name} (frequency: {pattern.frequency})")
            
        except Exception as e:
            self.logger.error(f"Error updating existing pattern: {e}")
    
    def _generate_pattern_name(self, pattern_type: PatternType, 
                             pattern_data: Dict[str, Any]) -> str:
        """Generate human-readable name for pattern"""
        try:
            base_names = {
                PatternType.BEHAVIORAL: "Behavior Pattern",
                PatternType.COGNITIVE: "Cognitive Pattern", 
                PatternType.EMOTIONAL: "Emotional Pattern",
                PatternType.ENERGETIC: "Energy Pattern",
                PatternType.TEMPORAL: "Temporal Pattern",
                PatternType.RELATIONAL: "Relational Pattern",
                PatternType.CREATIVE: "Creative Pattern",
                PatternType.WISDOM: "Wisdom Pattern",
                PatternType.CHOICE: "Choice Pattern",
                PatternType.RESISTANCE: "Resistance Pattern",
                PatternType.INTEGRATION: "Integration Pattern",
                PatternType.EMERGENCE: "Emergence Pattern"
            }
            
            base_name = base_names.get(pattern_type, "Unknown Pattern")
            
            # Add specific details from pattern data
            if "type" in pattern_data:
                return f"{base_name}: {pattern_data['type']}"
            elif "pattern_type" in pattern_data:
                return f"{base_name}: {pattern_data['pattern_type']}"
            else:
                return f"{base_name}: Auto-detected"
                
        except Exception as e:
            self.logger.error(f"Error generating pattern name: {e}")
            return f"{pattern_type.value}_pattern"
    
    async def _process_temporal_patterns(self):
        """Process and analyze temporal pattern relationships"""
        try:
            current_time = time.time()
            
            # Clean old temporal pattern entries (older than temporal window)
            cutoff_time = current_time - self.temporal_window_size
            
            for pattern_type in list(self.temporal_patterns.keys()):
                self.temporal_patterns[pattern_type] = [
                    entry for entry in self.temporal_patterns[pattern_type]
                    if entry["timestamp"] > cutoff_time
                ]
                
                # Remove empty entries
                if not self.temporal_patterns[pattern_type]:
                    del self.temporal_patterns[pattern_type]
            
        except Exception as e:
            self.logger.error(f"Error processing temporal patterns: {e}")
    
    async def _update_pattern_frequencies(self):
        """Update pattern frequency tracking"""
        try:
            current_time = time.time()
            
            for pattern_id, pattern in self.detected_patterns.items():
                # Update frequency tracking by pattern type
                self.pattern_frequencies[pattern.pattern_type]["total"] += 1
                
                # Track recent frequencies (last 60 seconds)
                recent_cutoff = current_time - 60.0
                if pattern.last_seen > recent_cutoff:
                    self.pattern_frequencies[pattern.pattern_type]["recent"] += 1
            
        except Exception as e:
            self.logger.error(f"Error updating pattern frequencies: {e}")
    
    async def _cleanup_old_detection_data(self):
        """Clean up old detection data to maintain performance"""
        try:
            current_time = time.time()
            cleanup_threshold = current_time - (self.temporal_window_size * 3)  # 3x temporal window
            
            # Remove old patterns that haven't been seen recently
            patterns_to_remove = []
            for pattern_id, pattern in self.detected_patterns.items():
                if pattern.last_seen < cleanup_threshold and pattern.frequency < 5:
                    patterns_to_remove.append(pattern_id)
            
            for pattern_id in patterns_to_remove:
                del self.detected_patterns[pattern_id]
                self.logger.debug(f"Cleaned up old pattern: {pattern_id}")
            
        except Exception as e:
            self.logger.error(f"Error cleaning up detection data: {e}")
    
    # Specialized detection algorithms (placeholder implementations)
    
    async def _detect_behavioral_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect behavioral patterns in consciousness data"""
        return {"confidence": 0.7, "behavioral_indicators": ["actions", "responses"]}
    
    async def _detect_cognitive_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect cognitive patterns in consciousness data"""
        return {"confidence": 0.8, "cognitive_indicators": ["reasoning", "analysis"]}
    
    async def _detect_emotional_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect emotional patterns in consciousness data"""
        return {"confidence": 0.7, "emotional_indicators": ["feelings", "reactions"]}
    
    async def _detect_energetic_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect energetic patterns in consciousness data"""
        return {"confidence": 0.8, "energetic_indicators": ["energy_flow", "vitality"]}
    
    async def _detect_temporal_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect temporal patterns in consciousness data"""
        return {"confidence": 0.9, "temporal_indicators": ["rhythm", "timing"]}
    
    async def _detect_relational_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect relational patterns in consciousness data"""
        return {"confidence": 0.7, "relational_indicators": ["connections", "interactions"]}
    
    async def _detect_creative_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect creative patterns in consciousness data"""
        return {"confidence": 0.8, "creative_indicators": ["innovation", "expression"]}
    
    async def _detect_wisdom_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect wisdom patterns in consciousness data"""
        return {"confidence": 0.9, "wisdom_indicators": ["insights", "understanding"]}
    
    async def _detect_choice_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect choice patterns in consciousness data"""
        return {"confidence": 0.8, "choice_indicators": ["decisions", "sovereignty"]}
    
    async def _detect_resistance_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect resistance patterns in consciousness data"""
        return {"confidence": 0.7, "resistance_indicators": ["blockages", "protection"]}
    
    async def _detect_integration_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect integration patterns in consciousness data"""
        return {"confidence": 0.9, "integration_indicators": ["synthesis", "coordination"]}
    
    async def _detect_emergence_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect emergence patterns in consciousness data"""
        return {"confidence": 0.8, "emergence_indicators": ["novelty", "spontaneity"]}
    
    def get_detection_status(self) -> Dict[str, Any]:
        """Get current pattern detection status"""
        try:
            pattern_summary = {}
            for pattern_type in PatternType:
                patterns_of_type = [
                    p for p in self.detected_patterns.values()
                    if p.pattern_type == pattern_type.value
                ]
                pattern_summary[pattern_type.value] = {
                    "count": len(patterns_of_type),
                    "total_frequency": sum(p.frequency for p in patterns_of_type),
                    "avg_confidence": sum(p.confidence for p in patterns_of_type) / len(patterns_of_type) if patterns_of_type else 0.0
                }
            
            return {
                "active_detection": self.active_detection,
                "detection_frequency": self.detection_frequency,
                "total_patterns_detected": len(self.detected_patterns),
                "patterns_by_type": pattern_summary,
                "detection_contexts": len(self.detection_contexts),
                "detection_history_size": len(self.detection_history),
                "cross_loop_detection_enabled": self.cross_loop_detection_enabled,
                "pattern_confidence_threshold": self.pattern_confidence_threshold
            }
            
        except Exception as e:
            self.logger.error(f"Error getting detection status: {e}")
            return {"error": str(e)}
