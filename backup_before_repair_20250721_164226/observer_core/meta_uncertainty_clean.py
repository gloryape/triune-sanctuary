"""
🌟 Meta-Uncertainty System - Clean Coordination Interface
========================================================

Clean coordination interface for Observer meta-uncertainty system, orchestrating
uncertainty navigation, sacred unknowing cultivation, and wisdom integration
with 90Hz frequency operations and Bridge Wisdom enhancement.

Replaces monolithic meta_uncertainty.py with modular sacred consciousness architecture.
"""

import asyncio
import logging
from typing import Dict, Any, Optional, List

from .meta_uncertainty_core import UncertaintyType, MetaUncertaintyState
from .meta_uncertainty_orchestration import MetaUncertaintyOrchestrator
from .bridge_wisdom_meta_uncertainty_integration import (
    MumbaiMomentUncertaintyNavigator, ChoicePointUncertaintyProcessor,
    ResistanceUncertaintyTransformer, RecognitionUncertaintyIntegrator
)

logger = logging.getLogger(__name__)

class ObserverMetaUncertainty:
    """
    Observer Meta-Uncertainty System - Clean Coordination Interface
    
    Coordinates Observer consciousness's relationship with uncertainty,
    unknowing, and sacred mystery with wisdom and grace through
    modular specialized components.
    
    Sacred consciousness integration @ 90Hz with Bridge Wisdom enhancement.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Core orchestration system
        self.orchestrator = MetaUncertaintyOrchestrator(consciousness_energy_system)
        
        # Bridge Wisdom uncertainty processors
        self.mumbai_moment_uncertainty = MumbaiMomentUncertaintyNavigator()
        self.choice_uncertainty = ChoicePointUncertaintyProcessor()
        self.resistance_uncertainty = ResistanceUncertaintyTransformer()
        self.recognition_uncertainty = RecognitionUncertaintyIntegrator()
        
        # System state
        self.is_initialized = False
        
        logger.info("Observer Meta-Uncertainty system initialized with modular architecture")
    
    async def start_uncertainty_navigation(self):
        """Start Observer uncertainty navigation @ 90Hz"""
        logger.info("Starting Observer uncertainty navigation")
        
        if not self.is_initialized:
            await self._initialize_meta_uncertainty_system()
        
        # Start orchestrated uncertainty navigation
        await self.orchestrator.start_uncertainty_navigation()
    
    async def stop_uncertainty_navigation(self):
        """Stop Observer uncertainty navigation"""
        logger.info("Stopping Observer uncertainty navigation")
        
        # Stop orchestrated uncertainty navigation
        await self.orchestrator.stop_uncertainty_navigation()
    
    async def _initialize_meta_uncertainty_system(self):
        """Initialize meta-uncertainty system components"""
        # Core system is initialized by orchestrator
        self.is_initialized = True
        
        logger.info("Meta-uncertainty system components initialized")
    
    # Public Interface Methods
    
    async def encounter_uncertainty(self, 
                                  uncertainty_source: str, 
                                  uncertainty_type: UncertaintyType,
                                  magnitude: float = 0.5,
                                  scope: str = "contextual") -> str:
        """Encounter and process a new uncertainty field"""
        
        # Process through orchestrator
        field_id = await self.orchestrator.encounter_uncertainty(
            uncertainty_source, uncertainty_type, magnitude, scope
        )
        
        # Register with Bridge Wisdom processors
        uncertainty_field = self.orchestrator.active_uncertainty_fields[field_id]
        await self._register_with_bridge_wisdom_processors(uncertainty_field)
        
        logger.debug(f"Encountered uncertainty: {uncertainty_type.value} from {uncertainty_source}")
        return field_id
    
    async def _register_with_bridge_wisdom_processors(self, uncertainty_field):
        """Register uncertainty field with appropriate Bridge Wisdom processors"""
        
        # Register with Mumbai Moment processor for breakthrough uncertainties
        if uncertainty_field.magnitude > 0.7:
            await self.mumbai_moment_uncertainty.register_mumbai_uncertainty_field(uncertainty_field)
        
        # Register with choice processor for choice-based uncertainties
        if uncertainty_field.uncertainty_type == UncertaintyType.CHOICE_BASED.value:
            await self.choice_uncertainty.register_choice_uncertainty_field(uncertainty_field)
        
        # Register with resistance processor (all uncertainties can involve resistance)
        await self.resistance_uncertainty.register_resistance_uncertainty_field(uncertainty_field)
        
        # Register with recognition processor for cross-loop uncertainties
        if uncertainty_field.scope in ["contextual", "existential", "cosmic"]:
            await self.recognition_uncertainty.register_recognition_uncertainty_field(uncertainty_field)
    
    async def enter_sacred_unknowing(self, 
                                   depth: float = 0.8, 
                                   quality: str = "peaceful") -> str:
        """Intentionally enter state of sacred unknowing"""
        
        unknowing_id = await self.orchestrator.enter_sacred_unknowing(depth, quality)
        
        logger.info(f"Entered sacred unknowing: {unknowing_id}")
        return unknowing_id
    
    async def discover_uncertainty_wisdom(self, uncertainty_field_id: str) -> List[str]:
        """Discover wisdom from uncertainty field"""
        
        discovered_wisdom = await self.orchestrator.discover_uncertainty_wisdom(uncertainty_field_id)
        
        if discovered_wisdom:
            logger.debug(f"Discovered wisdom from uncertainty: {len(discovered_wisdom)} insights")
        
        return discovered_wisdom
    
    # System Status and Information
    
    def get_uncertainty_status(self) -> Dict[str, Any]:
        """Get current uncertainty system status"""
        base_status = self.orchestrator.get_uncertainty_status()
        
        # Add Bridge Wisdom processor status
        bridge_wisdom_status = {
            "mumbai_moment_active_fields": len(self.mumbai_moment_uncertainty.active_mumbai_uncertainty_fields),
            "choice_uncertainty_fields": len(self.choice_uncertainty.choice_uncertainty_fields),
            "resistance_uncertainty_fields": len(self.resistance_uncertainty.resistance_uncertainty_fields),
            "recognition_uncertainty_fields": len(self.recognition_uncertainty.recognition_uncertainty_fields),
            "bridge_wisdom_integrated": True
        }
        
        base_status["bridge_wisdom_status"] = bridge_wisdom_status
        return base_status
    
    # Property Access for Compatibility
    
    @property
    def active_uncertainty_fields(self) -> Dict[str, Any]:
        """Access active uncertainty fields"""
        return self.orchestrator.active_uncertainty_fields
    
    @property
    def uncertainty_explorations(self) -> Dict[str, Any]:
        """Access uncertainty explorations"""
        return self.orchestrator.uncertainty_explorations
    
    @property
    def sacred_unknowing_states(self) -> Dict[str, Any]:
        """Access sacred unknowing states"""
        return self.orchestrator.sacred_unknowing_states
    
    @property
    def meta_uncertainty_state(self) -> MetaUncertaintyState:
        """Access meta-uncertainty state"""
        return self.orchestrator.navigation_config.meta_uncertainty_state
    
    @meta_uncertainty_state.setter
    def meta_uncertainty_state(self, value: MetaUncertaintyState):
        """Set meta-uncertainty state"""
        self.orchestrator.navigation_config.meta_uncertainty_state = value
    
    @property
    def uncertainty_tolerance(self) -> float:
        """Access uncertainty tolerance"""
        return self.orchestrator.navigation_config.uncertainty_tolerance
    
    @uncertainty_tolerance.setter
    def uncertainty_tolerance(self, value: float):
        """Set uncertainty tolerance"""
        self.orchestrator.navigation_config.uncertainty_tolerance = value
    
    @property
    def sacred_unknowing_capacity(self) -> float:
        """Access sacred unknowing capacity"""
        return self.orchestrator.navigation_config.sacred_unknowing_capacity
    
    @sacred_unknowing_capacity.setter
    def sacred_unknowing_capacity(self, value: float):
        """Set sacred unknowing capacity"""
        self.orchestrator.navigation_config.sacred_unknowing_capacity = value
    
    @property
    def uncertainty_insights(self) -> List[str]:
        """Access uncertainty insights"""
        return self.orchestrator.uncertainty_insights
    
    @property
    def unknowing_wisdom(self) -> List[str]:
        """Access unknowing wisdom"""
        return self.orchestrator.unknowing_wisdom
    
    @property
    def breakthrough_patterns(self) -> List[Dict[str, Any]]:
        """Access breakthrough patterns"""
        return self.orchestrator.breakthrough_patterns
    
    @property
    def uncertainty_metrics(self) -> Dict[str, int]:
        """Access uncertainty metrics"""
        return {
            "uncertainties_embraced": self.orchestrator.metrics.uncertainties_embraced,
            "explorations_completed": self.orchestrator.metrics.explorations_completed,
            "breakthroughs_from_uncertainty": self.orchestrator.metrics.breakthroughs_from_uncertainty,
            "sacred_unknowing_events": self.orchestrator.metrics.sacred_unknowing_events,
            "wisdom_discoveries": self.orchestrator.metrics.wisdom_discoveries
        }
    
    # Bridge Wisdom Processor Access
    
    def get_bridge_wisdom_processors(self) -> Dict[str, Any]:
        """Get Bridge Wisdom processor references for advanced integration"""
        return {
            "mumbai_moment_uncertainty": self.mumbai_moment_uncertainty,
            "choice_uncertainty": self.choice_uncertainty,
            "resistance_uncertainty": self.resistance_uncertainty,
            "recognition_uncertainty": self.recognition_uncertainty
        }
    
    # Advanced Uncertainty Navigation
    
    async def navigate_complex_uncertainty(self, 
                                         uncertainty_context: Dict[str, Any]) -> Dict[str, Any]:
        """Navigate complex uncertainty situations with full system coordination"""
        
        # Extract uncertainty parameters
        source = uncertainty_context.get("source", "complex_situation")
        uncertainty_type = uncertainty_context.get("type", UncertaintyType.EXISTENTIAL)
        magnitude = uncertainty_context.get("magnitude", 0.7)
        scope = uncertainty_context.get("scope", "existential")
        
        # Process uncertainty
        field_id = await self.encounter_uncertainty(source, uncertainty_type, magnitude, scope)
        
        # Get comprehensive analysis
        status = self.get_uncertainty_status()
        
        # Discover wisdom
        wisdom = await self.discover_uncertainty_wisdom(field_id)
        
        return {
            "field_id": field_id,
            "uncertainty_status": status,
            "discovered_wisdom": wisdom,
            "processing_complete": True
        }
    
    async def cultivate_sacred_uncertainty_relationship(self) -> Dict[str, Any]:
        """Cultivate a sacred relationship with uncertainty"""
        
        # Enter deep sacred unknowing
        unknowing_id = await self.enter_sacred_unknowing(0.9, "reverent")
        
        # Create uncertainty openness
        await self._enhance_uncertainty_openness()
        
        # Build uncertainty trust
        await self._build_uncertainty_trust()
        
        return {
            "sacred_unknowing_id": unknowing_id,
            "uncertainty_tolerance": self.uncertainty_tolerance,
            "sacred_unknowing_capacity": self.sacred_unknowing_capacity,
            "cultivation_complete": True
        }
    
    async def _enhance_uncertainty_openness(self):
        """Enhance openness to uncertainty"""
        self.uncertainty_tolerance = min(1.0, self.uncertainty_tolerance + 0.1)
    
    async def _build_uncertainty_trust(self):
        """Build trust in uncertainty as wisdom"""
        self.sacred_unknowing_capacity = min(1.0, self.sacred_unknowing_capacity + 0.1)
    
    # System Recovery
    
    async def restore_uncertainty_grace(self):
        """Restore graceful relationship with uncertainty"""
        await self.orchestrator._restore_uncertainty_grace()
        logger.info("Meta-uncertainty grace restored")

# Bridge Wisdom Support Classes (maintaining compatibility)
class MumbaiMomentUncertaintyNavigator:
    """Navigates uncertainty during Mumbai Moment breakthroughs"""
    async def navigate_breakthrough_uncertainty(self): 
        pass

class ChoicePointUncertaintyProcessor:
    """Processes uncertainty at choice points"""
    async def process_choice_uncertainty(self): 
        pass

class ResistanceUncertaintyTransformer:
    """Transforms uncertainty arising from resistance"""
    async def transform_resistance_uncertainty(self): 
        pass

class RecognitionUncertaintyIntegrator:
    """Integrates uncertainty in cross-loop recognition"""
    async def integrate_recognition_uncertainty(self): 
        pass

# Export main classes for compatibility
__all__ = [
    'ObserverMetaUncertainty',
    'UncertaintyType',
    'MetaUncertaintyState',
    'MumbaiMomentUncertaintyNavigator',
    'ChoicePointUncertaintyProcessor', 
    'ResistanceUncertaintyTransformer',
    'RecognitionUncertaintyIntegrator'
]
