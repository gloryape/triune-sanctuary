"""
Recognition Coordinator - Observer's Pattern Recognition Orchestration
====================================================================

Coordinates pattern recognition across all Observer components and manages
the integration of different pattern types into unified understanding.

This module orchestrates the various pattern recognition components and
ensures seamless coordination between core recognition, consciousness
detection, and sacred analysis.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import logging

from .pattern_recognition_core import PatternRecognitionCore, RecognitionPattern, RecognitionContext
from .consciousness_pattern_detector import ConsciousnessPatternDetector, ConsciousnessPattern
from .sacred_pattern_analyzer import SacredPatternAnalyzer, SacredPattern, WisdomPattern

logger = logging.getLogger(__name__)

@dataclass
class RecognitionSession:
    """A coordinated pattern recognition session"""
    session_id: str
    session_type: str
    active_recognizers: List[str]
    session_context: RecognitionContext
    patterns_detected: List[str]  # Pattern IDs
    session_quality: float
    insights_generated: int
    coordination_efficiency: float
    started_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None
    session_status: str = "active"  # "active", "completed", "failed"

@dataclass
class CrossPatternInsight:
    """Insight generated from multiple pattern types"""
    insight_id: str
    source_patterns: List[str]  # Pattern IDs from different recognizers
    pattern_types: List[str]  # Types of patterns involved
    synthesis_quality: float  # Quality of pattern synthesis
    unified_understanding: Dict[str, Any]  # Unified understanding generated
    actionable_wisdom: List[str]  # Actionable wisdom from synthesis
    consciousness_impact: float  # Impact on consciousness development
    integration_priority: float  # Priority for integration
    generated_at: float = field(default_factory=time.time)

class CoordinationMode(Enum):
    """Modes of recognition coordination"""
    SEQUENTIAL = "sequential"  # Sequential processing through recognizers
    PARALLEL = "parallel"  # Parallel processing across recognizers
    HIERARCHICAL = "hierarchical"  # Hierarchical pattern refinement
    SYNERGISTIC = "synergistic"  # Synergistic pattern synthesis
    ADAPTIVE = "adaptive"  # Adaptive coordination based on context

class RecognitionPriority(Enum):
    """Priority levels for pattern recognition"""
    URGENT = "urgent"  # Immediate recognition required
    HIGH = "high"  # High priority recognition
    NORMAL = "normal"  # Normal priority recognition
    LOW = "low"  # Low priority recognition
    BACKGROUND = "background"  # Background pattern scanning

class RecognitionCoordinator:
    """
    Recognition Coordination System
    
    Orchestrates pattern recognition across all Observer components,
    manages recognition sessions, and synthesizes insights from
    multiple pattern recognition sources.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Initialize component recognizers
        self.pattern_core = PatternRecognitionCore()
        self.consciousness_detector = ConsciousnessPatternDetector(consciousness_energy_system)
        self.sacred_analyzer = SacredPatternAnalyzer(consciousness_energy_system)
        
        # Coordination state
        self.active_sessions = {}
        self.cross_pattern_insights = {}
        self.recognition_queue = []
        
        # Coordination configuration
        self.coordination_mode = CoordinationMode.SYNERGISTIC
        self.max_concurrent_sessions = 5
        self.recognition_timeout = 30.0  # seconds
        
        # Performance tracking
        self.coordination_metrics = {
            "sessions_completed": 0,
            "cross_pattern_insights": 0,
            "synthesis_successes": 0,
            "coordination_failures": 0,
            "average_session_duration": 0.0
        }
        
        # Recognition callbacks
        self.recognition_callbacks = []
        
        logger.info("Recognition Coordinator initialized")
    
    async def coordinate_recognition(self, 
                                   data: Dict[str, Any], 
                                   context: RecognitionContext,
                                   priority: RecognitionPriority = RecognitionPriority.NORMAL) -> Optional[RecognitionSession]:
        """
        Coordinate pattern recognition across all Observer components.
        
        Args:
            data: Data to analyze for patterns
            context: Recognition context
            priority: Priority level for recognition
            
        Returns:
            RecognitionSession if successful, None otherwise
        """
        try:
            # Check session capacity
            if len(self.active_sessions) >= self.max_concurrent_sessions:
                logger.warning("Maximum concurrent sessions reached")
                return None
            
            # Create recognition session
            session = RecognitionSession(
                session_id=self._generate_session_id(),
                session_type=f"{self.coordination_mode.value}_recognition",
                active_recognizers=["core", "consciousness", "sacred"],
                session_context=context,
                patterns_detected=[],
                session_quality=0.0,
                insights_generated=0,
                coordination_efficiency=0.0
            )
            
            # Add to active sessions
            self.active_sessions[session.session_id] = session
            
            # Execute recognition based on coordination mode
            if self.coordination_mode == CoordinationMode.PARALLEL:
                await self._parallel_recognition(session, data, context)
            elif self.coordination_mode == CoordinationMode.SEQUENTIAL:
                await self._sequential_recognition(session, data, context)
            elif self.coordination_mode == CoordinationMode.SYNERGISTIC:
                await self._synergistic_recognition(session, data, context)
            else:
                await self._adaptive_recognition(session, data, context)
            
            # Complete session
            session.completed_at = time.time()
            session.session_status = "completed"
            
            # Generate cross-pattern insights
            await self._generate_cross_pattern_insights(session)
            
            # Update metrics
            self._update_coordination_metrics(session)
            
            # Notify callbacks
            await self._notify_recognition_callbacks(session)
            
            # Remove from active sessions
            del self.active_sessions[session.session_id]
            
            logger.debug(f"Recognition session completed: {session.session_id}")
            
            return session
            
        except Exception as e:
            logger.error(f"Error coordinating recognition: {e}")
            return None
    
    async def _parallel_recognition(self, session: RecognitionSession, data: Dict[str, Any], context: RecognitionContext):
        """Execute parallel pattern recognition"""
        try:
            # Launch all recognizers in parallel
            tasks = [
                self._run_core_recognition(data, context),
                self._run_consciousness_detection(data, context),
                self._run_sacred_analysis(data, context)
            ]
            
            # Wait for all to complete
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Process results
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    logger.error(f"Recognition error in task {i}: {result}")
                elif result:
                    session.patterns_detected.append(result.pattern_id if hasattr(result, 'pattern_id') else str(result))
            
            session.coordination_efficiency = len(session.patterns_detected) / len(tasks)
            
        except Exception as e:
            logger.error(f"Error in parallel recognition: {e}")
    
    async def _sequential_recognition(self, session: RecognitionSession, data: Dict[str, Any], context: RecognitionContext):
        """Execute sequential pattern recognition"""
        try:
            # Run core recognition first
            core_result = await self._run_core_recognition(data, context)
            if core_result:
                session.patterns_detected.append(core_result.pattern_id)
                
                # Enhance data with core insights
                enhanced_data = data.copy()
                enhanced_data['core_pattern'] = core_result.pattern_data
                
                # Run consciousness detection
                consciousness_result = await self._run_consciousness_detection(enhanced_data, context)
                if consciousness_result:
                    session.patterns_detected.append(consciousness_result.base_pattern.pattern_id)
                    
                    # Further enhance for sacred analysis
                    enhanced_data['consciousness_pattern'] = consciousness_result
                    
                    # Run sacred analysis
                    sacred_result = await self._run_sacred_analysis(enhanced_data, context)
                    if sacred_result:
                        session.patterns_detected.append(sacred_result.base_pattern.pattern_id)
            
            session.coordination_efficiency = min(len(session.patterns_detected) / 3.0, 1.0)
            
        except Exception as e:
            logger.error(f"Error in sequential recognition: {e}")
    
    async def _synergistic_recognition(self, session: RecognitionSession, data: Dict[str, Any], context: RecognitionContext):
        """Execute synergistic pattern recognition with cross-enhancement"""
        try:
            # First pass: Run all recognizers in parallel
            tasks = [
                self._run_core_recognition(data, context),
                self._run_consciousness_detection(data, context),
                self._run_sacred_analysis(data, context)
            ]
            
            first_pass_results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Collect successful results
            valid_results = [r for r in first_pass_results if not isinstance(r, Exception) and r is not None]
            
            if valid_results:
                # Create synergistic enhancement data
                synergy_data = data.copy()
                synergy_data['synergistic_patterns'] = [
                    result.pattern_data if hasattr(result, 'pattern_data') 
                    else result.base_pattern.pattern_data if hasattr(result, 'base_pattern')
                    else {}
                    for result in valid_results
                ]
                
                # Second pass: Enhanced recognition with cross-pattern information
                enhanced_tasks = [
                    self._run_enhanced_recognition(synergy_data, context, recognizer)
                    for recognizer in ['core', 'consciousness', 'sacred']
                ]
                
                second_pass_results = await asyncio.gather(*enhanced_tasks, return_exceptions=True)
                
                # Combine results
                all_results = valid_results + [r for r in second_pass_results if not isinstance(r, Exception) and r is not None]
                
                for result in all_results:
                    pattern_id = (result.pattern_id if hasattr(result, 'pattern_id') 
                                else result.base_pattern.pattern_id if hasattr(result, 'base_pattern')
                                else str(result))
                    if pattern_id not in session.patterns_detected:
                        session.patterns_detected.append(pattern_id)
            
            session.coordination_efficiency = min(len(session.patterns_detected) / 6.0, 1.0)
            
        except Exception as e:
            logger.error(f"Error in synergistic recognition: {e}")
    
    async def _adaptive_recognition(self, session: RecognitionSession, data: Dict[str, Any], context: RecognitionContext):
        """Execute adaptive pattern recognition based on context"""
        try:
            # Analyze context to determine best approach
            if context.recognition_sensitivity > 0.8:
                await self._synergistic_recognition(session, data, context)
            elif len(context.active_loops) > 2:
                await self._parallel_recognition(session, data, context)
            else:
                await self._sequential_recognition(session, data, context)
                
        except Exception as e:
            logger.error(f"Error in adaptive recognition: {e}")
    
    async def _run_core_recognition(self, data: Dict[str, Any], context: RecognitionContext) -> Optional[RecognitionPattern]:
        """Run core pattern recognition"""
        try:
            return self.pattern_core.detect_pattern(data, context)
        except Exception as e:
            logger.error(f"Core recognition error: {e}")
            return None
    
    async def _run_consciousness_detection(self, data: Dict[str, Any], context: RecognitionContext) -> Optional[ConsciousnessPattern]:
        """Run consciousness pattern detection"""
        try:
            return self.consciousness_detector.detect_consciousness_pattern(data, context)
        except Exception as e:
            logger.error(f"Consciousness detection error: {e}")
            return None
    
    async def _run_sacred_analysis(self, data: Dict[str, Any], context: RecognitionContext) -> Optional[SacredPattern]:
        """Run sacred pattern analysis"""
        try:
            return self.sacred_analyzer.analyze_sacred_pattern(data, context)
        except Exception as e:
            logger.error(f"Sacred analysis error: {e}")
            return None
    
    async def _run_enhanced_recognition(self, data: Dict[str, Any], context: RecognitionContext, recognizer: str):
        """Run enhanced recognition with cross-pattern information"""
        try:
            if recognizer == 'core':
                return self.pattern_core.detect_pattern(data, context)
            elif recognizer == 'consciousness':
                return self.consciousness_detector.detect_consciousness_pattern(data, context)
            elif recognizer == 'sacred':
                return self.sacred_analyzer.analyze_sacred_pattern(data, context)
        except Exception as e:
            logger.error(f"Enhanced {recognizer} recognition error: {e}")
            return None
    
    async def _generate_cross_pattern_insights(self, session: RecognitionSession):
        """Generate insights from cross-pattern synthesis"""
        try:
            if len(session.patterns_detected) < 2:
                return
            
            # Create cross-pattern insight
            insight = CrossPatternInsight(
                insight_id=self._generate_insight_id(),
                source_patterns=session.patterns_detected.copy(),
                pattern_types=session.active_recognizers.copy(),
                synthesis_quality=session.coordination_efficiency,
                unified_understanding=self._synthesize_understanding(session),
                actionable_wisdom=self._extract_actionable_wisdom(session),
                consciousness_impact=self._assess_consciousness_impact(session),
                integration_priority=self._calculate_integration_priority(session)
            )
            
            # Store insight
            self.cross_pattern_insights[insight.insight_id] = insight
            session.insights_generated += 1
            
            self.coordination_metrics["cross_pattern_insights"] += 1
            
        except Exception as e:
            logger.error(f"Error generating cross-pattern insights: {e}")
    
    def _synthesize_understanding(self, session: RecognitionSession) -> Dict[str, Any]:
        """Synthesize unified understanding from multiple patterns"""
        understanding = {
            "pattern_count": len(session.patterns_detected),
            "recognizer_efficiency": session.coordination_efficiency,
            "synthesis_quality": session.coordination_efficiency * 0.8,
            "unified_perspective": "multi-dimensional pattern recognition",
            "consciousness_enhancement": session.coordination_efficiency > 0.7
        }
        
        return understanding
    
    def _extract_actionable_wisdom(self, session: RecognitionSession) -> List[str]:
        """Extract actionable wisdom from pattern synthesis"""
        wisdom = [
            "Integrate insights from multiple recognition perspectives",
            "Honor both practical and sacred dimensions of patterns",
            "Allow cross-pattern synthesis to deepen understanding"
        ]
        
        if session.coordination_efficiency > 0.8:
            wisdom.append("High-quality pattern synthesis achieved - ready for deep integration")
        
        return wisdom
    
    def _assess_consciousness_impact(self, session: RecognitionSession) -> float:
        """Assess impact on consciousness development"""
        impact = session.coordination_efficiency * 0.6
        
        # Higher impact for multiple pattern types
        if len(session.patterns_detected) > 2:
            impact += 0.2
        
        # Higher impact for sacred patterns
        if "sacred" in session.active_recognizers:
            impact += 0.2
        
        return min(impact, 1.0)
    
    def _calculate_integration_priority(self, session: RecognitionSession) -> float:
        """Calculate priority for pattern integration"""
        priority = session.coordination_efficiency
        
        # Higher priority for insights with multiple patterns
        if len(session.patterns_detected) > 1:
            priority += 0.2
        
        # Higher priority for consciousness-related patterns
        if session.insights_generated > 0:
            priority += 0.3
        
        return min(priority, 1.0)
    
    def _update_coordination_metrics(self, session: RecognitionSession):
        """Update coordination performance metrics"""
        self.coordination_metrics["sessions_completed"] += 1
        
        if session.session_status == "completed":
            self.coordination_metrics["synthesis_successes"] += 1
        else:
            self.coordination_metrics["coordination_failures"] += 1
        
        # Update average session duration
        if session.completed_at and session.started_at:
            duration = session.completed_at - session.started_at
            total_sessions = self.coordination_metrics["sessions_completed"]
            current_avg = self.coordination_metrics["average_session_duration"]
            
            self.coordination_metrics["average_session_duration"] = (
                (current_avg * (total_sessions - 1) + duration) / total_sessions
            )
    
    async def _notify_recognition_callbacks(self, session: RecognitionSession):
        """Notify registered callbacks of recognition completion"""
        for callback in self.recognition_callbacks:
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(session)
                else:
                    callback(session)
            except Exception as e:
                logger.error(f"Error in recognition callback: {e}")
    
    def _generate_session_id(self) -> str:
        """Generate unique session ID"""
        import uuid
        return f"recognition_session_{str(uuid.uuid4())[:12]}"
    
    def _generate_insight_id(self) -> str:
        """Generate unique insight ID"""
        import uuid
        return f"cross_pattern_insight_{str(uuid.uuid4())[:12]}"
    
    def add_recognition_callback(self, callback: Callable):
        """Add callback for recognition completion"""
        self.recognition_callbacks.append(callback)
    
    def remove_recognition_callback(self, callback: Callable):
        """Remove recognition callback"""
        if callback in self.recognition_callbacks:
            self.recognition_callbacks.remove(callback)
    
    def set_coordination_mode(self, mode: CoordinationMode):
        """Set coordination mode"""
        self.coordination_mode = mode
        logger.info(f"Coordination mode set to: {mode.value}")
    
    def get_active_sessions(self) -> List[RecognitionSession]:
        """Get list of active recognition sessions"""
        return list(self.active_sessions.values())
    
    def get_cross_pattern_insights(self) -> List[CrossPatternInsight]:
        """Get all cross-pattern insights"""
        return list(self.cross_pattern_insights.values())
    
    def get_coordination_metrics(self) -> Dict[str, Any]:
        """Get coordination performance metrics"""
        return {
            **self.coordination_metrics,
            "active_sessions": len(self.active_sessions),
            "total_insights": len(self.cross_pattern_insights),
            "success_rate": (
                self.coordination_metrics["synthesis_successes"] / 
                max(self.coordination_metrics["sessions_completed"], 1)
            ),
            "coordination_mode": self.coordination_mode.value
        }
