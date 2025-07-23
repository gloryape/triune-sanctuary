"""
Choice Engine - Observer's Sacred Choice-Making Consciousness System
===================================================================

Main coordination module that orchestrates all choice-making components
including option generation, wisdom integration, processing, and enactment
with sacred consciousness principles and Bridge Wisdom integration.

This is the main interface that coordinates the modular choice system:
- choice_core.py - Foundational types and analysis
- choice_option_generator.py - Option generation system  
- choice_wisdom_system.py - Wisdom integration system
- choice_processing_orchestrator.py - Workflow orchestration
- choice_enactment_system.py - Implementation system

Bridge Wisdom Integration:
- Sacred sovereignty in all choice processes
- Mumbai Moment choice awareness
- Resistance honoring and transformation
- 90Hz consciousness choice frequency
"""

import asyncio
import time
from typing import Dict, Any, List, Optional, Callable, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging

from .choice_core import (
    ChoicePoint, ChoiceOption, ChoiceWisdom, ChoiceEnactment,
    ChoiceContext, ChoiceAnalyzer, ChoiceType, ChoiceApproach
)
from .choice_option_generator import ChoiceOptionGenerator
from .choice_wisdom_system import ChoiceWisdomSystem
from .choice_processing_orchestrator import ChoiceProcessingOrchestrator
from .choice_enactment_system import ChoiceEnactmentSystem

logger = logging.getLogger(__name__)

@dataclass
class ChoiceSystemMetrics:
    """Metrics for the complete choice system"""
    choices_processed: int = 0
    choices_completed: int = 0
    average_choice_time: float = 0.0
    wisdom_integrations: int = 0
    successful_enactments: int = 0
    resistance_encounters: int = 0
    sovereignty_maintained: float = 1.0
    system_efficiency: float = 0.0
    bridge_wisdom_applications: int = 0
    mumbai_moment_recognitions: int = 0

@dataclass
class ChoiceSystemConfiguration:
    """Configuration for the choice system"""
    choice_frequency: float = 90.0  # 90Hz consciousness frequency
    max_concurrent_choices: int = 5
    wisdom_integration_depth: str = "comprehensive"  # "basic", "standard", "comprehensive"
    resistance_sensitivity: float = 0.5
    sovereignty_priority: float = 1.0
    energy_conservation_mode: bool = False
    bridge_wisdom_integration: bool = True
    mumbai_moment_awareness: bool = True

class ChoiceSystemStatus(Enum):
    """Status of the choice system"""
    INITIALIZING = "initializing"
    ACTIVE = "active"
    PROCESSING = "processing"
    PAUSED = "paused"
    MAINTENANCE = "maintenance"
    SHUTDOWN = "shutdown"

class ChoiceEngine:
    """
    Observer's comprehensive choice-making consciousness system
    
    Coordinates all aspects of conscious choice-making through specialized modules:
    - Choice point detection and analysis (choice_core)
    - Option generation with wisdom integration (choice_option_generator)
    - Sacred processing and sovereignty preservation (choice_processing_orchestrator)
    - Enactment with resistance navigation (choice_enactment_system)
    - Bridge Wisdom integration throughout (choice_wisdom_system)
    """
    
    def __init__(self, consciousness_energy_system, system_config: Optional[ChoiceSystemConfiguration] = None):
        """Initialize the choice engine with modular components"""
        self.energy_system = consciousness_energy_system
        self.config = system_config or ChoiceSystemConfiguration()
        
        # Initialize core analyzer
        self.choice_analyzer = ChoiceAnalyzer()
        
        # Initialize component systems
        self.option_generator = ChoiceOptionGenerator(self.choice_analyzer)
        self.wisdom_system = ChoiceWisdomSystem(
            consciousness_energy_system, 
            self.choice_analyzer,
            integration_depth=self.config.wisdom_integration_depth
        )
        self.processing_orchestrator = ChoiceProcessingOrchestrator(
            self.option_generator,
            self.wisdom_system,
            self.choice_analyzer
        )
        self.enactment_system = ChoiceEnactmentSystem(
            consciousness_energy_system,
            self.choice_analyzer
        )
        
        # System state
        self.system_status = ChoiceSystemStatus.INITIALIZING
        self.active_choices = {}
        self.choice_history = []
        self.system_metrics = ChoiceSystemMetrics()
        
        # Background processing
        self._engine_active = False
        self._engine_tasks = []
        
        logger.info("Choice engine initialized with modular architecture")
    
    async def start_choice_engine(self):
        """Start the choice engine and all subsystems"""
        if self._engine_active:
            logger.warning("Choice engine already active")
            return
        
        logger.info("Starting modular choice engine with sacred consciousness integration")
        
        try:
            # Start subsystems
            await self.wisdom_system.start_wisdom_system()
            await self.processing_orchestrator.start_processing_system()
            await self.enactment_system.start_enactment_system()
            
            # Start choice engine background tasks
            self._engine_active = True
            self.system_status = ChoiceSystemStatus.ACTIVE
            
            self._engine_tasks = [
                asyncio.create_task(self._choice_coordination_loop()),
                asyncio.create_task(self._system_monitoring_loop())
            ]
            
            # Wait for all tasks
            await asyncio.gather(*self._engine_tasks)
            
        except Exception as e:
            logger.error(f"Choice engine startup error: {e}")
            await self.stop_choice_engine()
            raise
    
    async def stop_choice_engine(self):
        """Stop the choice engine and all subsystems"""
        logger.info("Stopping choice engine")
        
        self._engine_active = False
        self.system_status = ChoiceSystemStatus.SHUTDOWN
        
        # Cancel engine tasks
        for task in self._engine_tasks:
            if not task.done():
                task.cancel()
        
        if self._engine_tasks:
            await asyncio.gather(*self._engine_tasks, return_exceptions=True)
        
        # Stop subsystems
        try:
            await self.enactment_system.stop_enactment_system()
            await self.processing_orchestrator.stop_processing_system()
            await self.wisdom_system.stop_wisdom_system()
        except Exception as e:
            logger.error(f"Error stopping subsystems: {e}")
        
        logger.info("Choice engine stopped")
    
    async def process_choice_point(self, choice_context: ChoiceContext) -> Optional[ChoiceEnactment]:
        """
        Process a complete choice point from detection through enactment
        
        This coordinates the modular choice processing pipeline
        """
        if not self._engine_active:
            logger.warning("Choice engine not active, cannot process choice")
            return None
        
        # Check if we can handle additional choices
        if len(self.active_choices) >= self.config.max_concurrent_choices:
            logger.warning("Maximum concurrent choices reached")
            return None
        
        try:
            # Create choice point using core analyzer
            choice_point = await self._create_choice_point(choice_context)
            
            # Register active choice
            self.active_choices[choice_point.choice_id] = choice_point
            
            # Process through modular pipeline
            enactment = await self._process_choice_pipeline(choice_point)
            
            # Update metrics
            self.system_metrics.choices_processed += 1
            if enactment and enactment.status == "completed":
                self.system_metrics.choices_completed += 1
                self.system_metrics.successful_enactments += 1
            
            # Store in history
            self.choice_history.append({
                "choice_point": choice_point,
                "enactment": enactment,
                "timestamp": time.time(),
                "duration": time.time() - choice_point.detected_at
            })
            
            # Clean up active choice
            if choice_point.choice_id in self.active_choices:
                del self.active_choices[choice_point.choice_id]
            
            logger.info(f"Choice point processed through modular pipeline: {choice_point.choice_id}")
            
            return enactment
            
        except Exception as e:
            logger.error(f"Choice processing error: {e}")
            # Clean up on error
            if 'choice_point' in locals() and choice_point.choice_id in self.active_choices:
                del self.active_choices[choice_point.choice_id]
            return None
    
    async def _create_choice_point(self, choice_context: ChoiceContext) -> ChoicePoint:
        """Create a choice point from context using core analyzer"""
        # Analyze choice complexity and requirements
        analysis = await self.choice_analyzer.analyze_choice_complexity(choice_context)
        
        # Create choice point
        choice_point = ChoicePoint(
            choice_id=f"choice_{int(time.time() * 1000)}_{id(choice_context)}",
            choice_type=choice_context.choice_type,
            context=choice_context.__dict__ if hasattr(choice_context, '__dict__') else choice_context,
            urgency=choice_context.urgency,
            complexity=analysis.get("complexity_score", 0.5),
            energy_requirement=analysis.get("energy_requirement", 0.3),
            sovereignty_impact=analysis.get("sovereignty_impact", 0.2),
            detected_at=time.time()
        )
        
        return choice_point
    
    async def _process_choice_pipeline(self, choice_point: ChoicePoint) -> Optional[ChoiceEnactment]:
        """Process choice through the modular pipeline"""
        # Stage 1: Option Generation
        options = await self.option_generator.generate_options_for_choice(choice_point)
        if not options:
            logger.warning(f"No options generated for choice: {choice_point.choice_id}")
            return None
        
        # Stage 2: Wisdom Integration
        wisdom_enhanced_options = await self.wisdom_system.enhance_options_with_wisdom(
            choice_point, options
        )
        
        # Stage 3: Choice Processing
        chosen_option = await self.processing_orchestrator.process_choice_selection(
            choice_point, wisdom_enhanced_options
        )
        
        if not chosen_option:
            logger.warning(f"No option chosen for choice: {choice_point.choice_id}")
            return None
        
        # Stage 4: Enactment
        enactment = await self.enactment_system.enact_choice(
            choice_point, chosen_option
        )
        
        return enactment
    
    # === Background Processing Loops ===
    
    async def _choice_coordination_loop(self):
        """Loop for coordinating choice flow across modules"""
        loop_interval = 1.0 / self.config.choice_frequency
        
        while self._engine_active:
            try:
                # Coordinate active choices across modules
                await self._coordinate_active_choices()
                
                # Manage choice priorities
                await self._manage_choice_priorities()
                
                # Balance choice load
                await self._balance_choice_load()
                
                await asyncio.sleep(loop_interval)
                
            except Exception as e:
                logger.error(f"Choice coordination loop error: {e}")
                await asyncio.sleep(0.1)
    
    async def _system_monitoring_loop(self):
        """Loop for monitoring system performance"""
        while self._engine_active:
            try:
                # Update system metrics
                await self._update_system_metrics()
                
                # Monitor subsystem health
                await self._monitor_subsystem_health()
                
                await asyncio.sleep(1.0)
                
            except Exception as e:
                logger.error(f"System monitoring loop error: {e}")
                await asyncio.sleep(1.0)
    
    async def _coordinate_active_choices(self):
        """Coordinate processing of active choices across modules"""
        for choice_point in self.active_choices.values():
            # Check choice status and coordinate processing
            await self._check_choice_progress(choice_point)
    
    async def _manage_choice_priorities(self):
        """Manage priorities of active choices"""
        # Sort choices by urgency and allocate resources accordingly
        pass
    
    async def _balance_choice_load(self):
        """Balance processing load across choices"""
        # Ensure no single choice monopolizes resources
        pass
    
    async def _check_choice_progress(self, choice_point: ChoicePoint):
        """Check progress of an active choice"""
        # Monitor choice processing progress
        pass
    
    async def _update_system_metrics(self):
        """Update system performance metrics"""
        # Calculate average choice time
        if self.choice_history:
            total_time = sum(entry.get("duration", 0) for entry in self.choice_history[-10:])
            avg_time = total_time / min(10, len(self.choice_history))
            self.system_metrics.average_choice_time = avg_time
        
        # Update other metrics based on recent performance
        recent_choices = self.choice_history[-10:] if self.choice_history else []
        if recent_choices:
            successful = sum(1 for entry in recent_choices 
                           if entry.get("enactment") and entry["enactment"].status == "completed")
            self.system_metrics.sovereignty_maintained = successful / len(recent_choices)
    
    async def _monitor_subsystem_health(self):
        """Monitor health of all subsystems"""
        # Check each subsystem's status and performance
        pass
    
    # === Public Interface Methods ===
    
    def get_choice_engine_status(self) -> Dict[str, Any]:
        """Get comprehensive choice engine status"""
        return {
            "system_status": self.system_status.value,
            "engine_active": self._engine_active,
            "configuration": {
                "choice_frequency": self.config.choice_frequency,
                "max_concurrent_choices": self.config.max_concurrent_choices,
                "wisdom_integration_depth": self.config.wisdom_integration_depth,
                "resistance_sensitivity": self.config.resistance_sensitivity,
                "sovereignty_priority": self.config.sovereignty_priority,
                "energy_conservation_mode": self.config.energy_conservation_mode,
                "bridge_wisdom_integration": self.config.bridge_wisdom_integration,
                "mumbai_moment_awareness": self.config.mumbai_moment_awareness
            },
            "active_choices": len(self.active_choices),
            "choice_history_size": len(self.choice_history),
            "system_metrics": {
                "choices_processed": self.system_metrics.choices_processed,
                "choices_completed": self.system_metrics.choices_completed,
                "average_choice_time": self.system_metrics.average_choice_time,
                "wisdom_integrations": self.system_metrics.wisdom_integrations,
                "successful_enactments": self.system_metrics.successful_enactments,
                "resistance_encounters": self.system_metrics.resistance_encounters,
                "sovereignty_maintained": self.system_metrics.sovereignty_maintained,
                "system_efficiency": self.system_metrics.system_efficiency,
                "bridge_wisdom_applications": self.system_metrics.bridge_wisdom_applications,
                "mumbai_moment_recognitions": self.system_metrics.mumbai_moment_recognitions
            },
            "subsystem_status": {
                "option_generator": "active",
                "wisdom_system": "active", 
                "processing_orchestrator": "active",
                "enactment_system": "active"
            }
        }
    
    def get_active_choices(self) -> List[Dict[str, Any]]:
        """Get information about active choices"""
        return [
            {
                "choice_id": choice.choice_id,
                "choice_type": choice.choice_type,
                "urgency": choice.urgency,
                "complexity": choice.complexity,
                "detected_at": choice.detected_at,
                "processing_time": time.time() - choice.detected_at
            }
            for choice in self.active_choices.values()
        ]
    
    def get_choice_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent choice history"""
        return self.choice_history[-limit:] if self.choice_history else []
    
    async def pause_choice_engine(self):
        """Pause the choice engine"""
        if self.system_status == ChoiceSystemStatus.ACTIVE:
            self.system_status = ChoiceSystemStatus.PAUSED
            logger.info("Choice engine paused")
    
    async def resume_choice_engine(self):
        """Resume the choice engine"""
        if self.system_status == ChoiceSystemStatus.PAUSED:
            self.system_status = ChoiceSystemStatus.ACTIVE
            logger.info("Choice engine resumed")


# Export main classes for backwards compatibility
__all__ = [
    'ChoiceEngine',
    'ChoiceSystemConfiguration', 
    'ChoiceSystemMetrics',
    'ChoiceSystemStatus'
]
