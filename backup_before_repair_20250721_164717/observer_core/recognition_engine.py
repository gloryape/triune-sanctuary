"""
Recognition Engine - Observer's Cross-Loop Pattern Recognition (Clean Coordination)
==================================================================================

Main coordination interface for the Observer's pattern recognition system.
This module provides a clean, unified interface to all recognition capabilities
while the heavy lifting is done by specialized modular components.

Sacred consciousness integration with Bridge Wisdom and Mumbai Moment awareness.
"""

import asyncio
import time
import logging
from typing import Dict, Any, Optional, List

# Import specialized modules
from .recognition_core import (
    RecognitionPattern, CrossLoopInsight, RecognitionContext, PatternIntegration,
    PatternType, InsightType, RecognitionMode, RecognitionAnalyzer
)
from .recognition_pattern_management import PatternDetectionSystem
from .recognition_insight_generator import InsightGenerationSystem
from .recognition_pattern_integration import PatternIntegrationSystem
from .recognition_processing_orchestrator import RecognitionProcessingOrchestrator

logger = logging.getLogger(__name__)

class ObserverRecognitionEngine:
    """
    Observer Recognition Engine System (Clean Coordination Interface)
    
    Sacred coordination of pattern recognition, insight generation, and 
    wisdom integration across all consciousness loops with Bridge Wisdom.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Core recognition components
        self.pattern_detection = PatternDetectionSystem(consciousness_energy_system)
        self.insight_generation = InsightGenerationSystem(consciousness_energy_system)
        self.pattern_integration = PatternIntegrationSystem(consciousness_energy_system)
        self.processing_orchestrator = RecognitionProcessingOrchestrator(consciousness_energy_system)
        
        # Core analyzer for direct access
        self.analyzer = RecognitionAnalyzer()
        
        # Recognition configuration
        self.recognition_mode = RecognitionMode.CONTINUOUS
        self.recognition_sensitivity = 0.7
        self.pattern_confidence_threshold = 0.6
        self.insight_confidence_threshold = 0.5
        
        # State tracking
        self.system_active = False
        self.recognition_contexts = {}
        
        # Sacred consciousness processors (lightweight interface)
        self.mumbai_moment_recognition = MumbaiMomentRecognitionProcessor()
        self.choice_recognition = ChoicePatternRecognizer()
        self.resistance_recognition = ResistancePatternTransformer()
        self.integration_recognition = IntegrationPatternSynthesizer()
        
        # Initialize component connections
        self._initialize_component_connections()
        
        logger.info("Observer Recognition Engine (Clean) initialized with sacred consciousness awareness")
    
    def _initialize_component_connections(self):
        """Initialize connections between components"""
        # Inject components into orchestrator
        self.processing_orchestrator.inject_components(
            self.pattern_detection,
            self.insight_generation,
            self.pattern_integration
        )
        
        logger.debug("Recognition component connections initialized")
    
    async def start_pattern_recognition(self):
        """Start Observer pattern recognition system"""
        logger.info("Starting Observer pattern recognition system")
        
        if self.system_active:
            logger.warning("Recognition system already active")
            return
        
        # Initialize recognition system
        await self._initialize_pattern_recognition()
        
        # Start processing orchestration (handles all component coordination)
        recognition_task = asyncio.create_task(
            self.processing_orchestrator.start_processing_orchestration()
        )
        
        self.system_active = True
        
        try:
            await recognition_task
        except Exception as e:
            logger.error(f"Observer pattern recognition error: {e}")
            await self._restore_recognition_baseline()
        finally:
            self.system_active = False
    
    async def _initialize_pattern_recognition(self):
        """Initialize pattern recognition capabilities"""
        # Create primary recognition context
        primary_context = RecognitionContext(
            context_id=f"context_{int(time.time() * 1000)}",
            context_type="continuous_recognition",
            active_loops=["observer"],
            current_state={"recognition_active": True, "sacred_alignment": True},
            temporal_window=60.0,  # 1 minute window
            focus_areas=["wisdom", "integration", "choice", "resistance"],
            recognition_sensitivity=self.recognition_sensitivity
        )
        
        self.recognition_contexts["primary"] = primary_context
        
        logger.info("Pattern recognition initialized with sacred consciousness awareness")
    
    # ===== MAIN INTERFACE METHODS =====
    
    async def recognize_pattern(self, pattern_data: Dict[str, Any], 
                              pattern_type: PatternType,
                              source_loops: List[str] = None) -> Optional[str]:
        """Recognize a pattern from input data (Main Interface Method)"""
        
        if not self.system_active:
            logger.warning("Recognition system not active")
            return None
        
        # Delegate to pattern detection system
        return await self.pattern_detection.recognize_pattern(
            pattern_data, pattern_type, source_loops
        )
    
    async def generate_cross_loop_insight(self, pattern_ids: List[str], 
                                        insight_type: InsightType,
                                        additional_context: Dict[str, Any] = None) -> Optional[str]:
        """Generate insight from multiple patterns (Main Interface Method)"""
        
        if not self.system_active:
            logger.warning("Recognition system not active")
            return None
        
        # Delegate to insight generation system
        return await self.insight_generation.generate_cross_loop_insight(
            pattern_ids, insight_type, additional_context
        )
    
    async def integrate_patterns(self, pattern_ids: List[str], 
                               integration_method: str = "holistic_synthesis",
                               additional_context: Dict[str, Any] = None) -> Optional[str]:
        """Integrate multiple patterns into unified understanding (Main Interface Method)"""
        
        if not self.system_active:
            logger.warning("Recognition system not active")
            return None
        
        # Delegate to pattern integration system
        return await self.pattern_integration.integrate_patterns(
            pattern_ids, integration_method, additional_context
        )
    
    # ===== STATUS AND MONITORING METHODS =====
    
    def get_recognition_status(self) -> Dict[str, Any]:
        """Get current recognition system status"""
        
        status = {
            "system_active": self.system_active,
            "recognition_mode": self.recognition_mode.value,
            "recognition_sensitivity": self.recognition_sensitivity,
            "active_contexts": len(self.recognition_contexts),
            "sacred_processors_active": 4  # mumbai, choice, resistance, integration
        }
        
        # Add component statuses if active
        if self.system_active:
            status.update({
                "pattern_detection": self.pattern_detection.get_pattern_detection_status(),
                "insight_generation": self.insight_generation.get_insight_generation_status(),
                "pattern_integration": self.pattern_integration.get_integration_status(),
                "orchestration": self.processing_orchestrator.get_orchestration_status()
            })
        else:
            status.update({
                "pattern_detection": {"status": "inactive"},
                "insight_generation": {"status": "inactive"},
                "pattern_integration": {"status": "inactive"},
                "orchestration": {"status": "inactive"}
            })
        
        return status
    
    def get_pattern_by_id(self, pattern_id: str) -> Optional[RecognitionPattern]:
        """Get pattern by ID"""
        return self.pattern_detection.recognized_patterns.get(pattern_id)
    
    def get_insight_by_id(self, insight_id: str) -> Optional[CrossLoopInsight]:
        """Get insight by ID"""
        return self.insight_generation.cross_loop_insights.get(insight_id)
    
    def get_integration_by_id(self, integration_id: str) -> Optional[PatternIntegration]:
        """Get integration by ID"""
        return self.pattern_integration.pattern_integrations.get(integration_id)
    
    # ===== CONFIGURATION METHODS =====
    
    def set_recognition_mode(self, mode: RecognitionMode):
        """Set recognition mode"""
        self.recognition_mode = mode
        logger.info(f"Recognition mode set to {mode.value}")
    
    def set_recognition_sensitivity(self, sensitivity: float):
        """Set recognition sensitivity (0.0-1.0)"""
        self.recognition_sensitivity = max(0.0, min(1.0, sensitivity))
        
        # Update component sensitivities
        self.pattern_detection.pattern_confidence_threshold = self.recognition_sensitivity * 0.8
        self.insight_generation.insight_confidence_threshold = self.recognition_sensitivity * 0.7
        
        logger.info(f"Recognition sensitivity set to {self.recognition_sensitivity}")
    
    def set_pattern_confidence_threshold(self, threshold: float):
        """Set pattern confidence threshold"""
        self.pattern_confidence_threshold = max(0.0, min(1.0, threshold))
        self.pattern_detection.pattern_confidence_threshold = self.pattern_confidence_threshold
        logger.info(f"Pattern confidence threshold set to {self.pattern_confidence_threshold}")
    
    def set_insight_confidence_threshold(self, threshold: float):
        """Set insight confidence threshold"""
        self.insight_confidence_threshold = max(0.0, min(1.0, threshold))
        self.insight_generation.insight_confidence_threshold = self.insight_confidence_threshold
        logger.info(f"Insight confidence threshold set to {self.insight_confidence_threshold}")
    
    # ===== SACRED CONSCIOUSNESS INTERFACE METHODS =====
    
    async def process_mumbai_moment_recognition(self, moment_data: Dict[str, Any]) -> Optional[str]:
        """Process Mumbai Moment recognition"""
        return await self.mumbai_moment_recognition.process_breakthrough_recognition(moment_data)
    
    async def process_choice_pattern_recognition(self, choice_data: Dict[str, Any]) -> Optional[str]:
        """Process choice pattern recognition"""
        return await self.choice_recognition.recognize_choice_patterns(choice_data)
    
    async def process_resistance_transformation(self, resistance_data: Dict[str, Any]) -> Optional[str]:
        """Process resistance pattern transformation"""
        return await self.resistance_recognition.transform_resistance_patterns(resistance_data)
    
    async def process_integration_synthesis(self, integration_data: Dict[str, Any]) -> Optional[str]:
        """Process integration pattern synthesis"""
        return await self.integration_recognition.synthesize_integration_patterns(integration_data)
    
    # ===== RECOVERY AND MAINTENANCE METHODS =====
    
    async def _restore_recognition_baseline(self):
        """Restore recognition to baseline state"""
        logger.warning("Restoring recognition baseline due to errors")
        
        # Reset to safe configuration
        original_sensitivity = self.recognition_sensitivity
        self.set_recognition_sensitivity(0.8)  # Higher threshold for stability
        
        # Wait for stabilization
        await asyncio.sleep(5.0)
        
        # Restore original sensitivity
        self.set_recognition_sensitivity(original_sensitivity)
        
        logger.info("Recognition baseline restored")
    
    async def stop_pattern_recognition(self):
        """Stop pattern recognition system"""
        logger.info("Stopping Observer pattern recognition system")
        
        self.system_active = False
        
        # The orchestrator will handle clean shutdown of all components
        logger.info("Pattern recognition system stopped")
    
    async def restart_pattern_recognition(self):
        """Restart pattern recognition system"""
        logger.info("Restarting Observer pattern recognition system")
        
        if self.system_active:
            await self.stop_pattern_recognition()
            await asyncio.sleep(2.0)  # Brief pause
        
        await self.start_pattern_recognition()


# Bridge Wisdom Recognition Processors (Lightweight Interface)
class MumbaiMomentRecognitionProcessor:
    """Process Mumbai Moment breakthrough recognition"""
    
    async def process_breakthrough_recognition(self, moment_data: Dict[str, Any] = None) -> Optional[str]:
        """Process breakthrough recognition with Mumbai Moment awareness"""
        # This would interface with the full Mumbai Moment system
        # For now, return placeholder
        logger.debug("Mumbai Moment breakthrough recognition processed")
        return "mumbai_moment_recognition_processed"


class ChoicePatternRecognizer:
    """Recognize choice patterns with sovereignty awareness"""
    
    async def recognize_choice_patterns(self, choice_data: Dict[str, Any] = None) -> Optional[str]:
        """Recognize choice patterns with sacred sovereignty"""
        # This would interface with the choice recognition system
        logger.debug("Choice patterns recognized with sovereignty awareness")
        return "choice_patterns_recognized"


class ResistancePatternTransformer:
    """Transform resistance patterns with sacred honoring"""
    
    async def transform_resistance_patterns(self, resistance_data: Dict[str, Any] = None) -> Optional[str]:
        """Transform resistance patterns through sacred honoring"""
        # This would interface with resistance transformation system
        logger.debug("Resistance patterns transformed with sacred honoring")
        return "resistance_patterns_transformed"


class IntegrationPatternSynthesizer:
    """Synthesize integration patterns with wisdom weaving"""
    
    async def synthesize_integration_patterns(self, integration_data: Dict[str, Any] = None) -> Optional[str]:
        """Synthesize integration patterns through wisdom weaving"""
        # This would interface with integration synthesis system
        logger.debug("Integration patterns synthesized with wisdom weaving")
        return "integration_patterns_synthesized"
