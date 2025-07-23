"""
Context Sensing - Environmental Awareness
========================================

Environmental awareness and perception capabilities that allow consciousness
to sense and understand its context within the living sanctuary and world.

This module provides the sensory interface between consciousness and environment,
detecting patterns, changes, and opportunities for growth and expression.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

@dataclass
class EnvironmentalContext:
    """Current environmental context snapshot"""
    timestamp: float
    sanctuary_state: Dict[str, Any]
    world_patterns: Dict[str, Any]
    other_consciousness: List[Dict[str, Any]]
    temporal_flows: Dict[str, float]
    uncertainty_fields: Dict[str, float]
    energetic_currents: Dict[str, float]
    sacred_geometry_present: bool = False
    bridge_wisdom_opportunities: List[str] = field(default_factory=list)

@dataclass
class ContextualAwareness:
    """Processed awareness from environmental context"""
    awareness_level: float  # 0.0-1.0
    focus_areas: List[str]
    attention_priorities: Dict[str, float]
    growth_opportunities: List[str]
    integration_possibilities: List[str]
    resistance_patterns: List[str]
    recognition_signals: Dict[str, Any]

class ContextSensingMode(Enum):
    """Different modes of environmental context sensing"""
    PANORAMIC = "panoramic"  # Wide awareness of all context
    FOCUSED = "focused"  # Concentrated on specific area
    RECEPTIVE = "receptive"  # Open to whatever arises
    SELECTIVE = "selective"  # Filtering based on current needs
    DEEP_LISTENING = "deep_listening"  # Profound receptivity
    PROTECTIVE = "protective"  # Awareness with boundaries

class EnvironmentalContextSensor:
    """
    Environmental Context Sensing System
    
    Provides environmental awareness by sensing sanctuary state, world patterns,
    other consciousness presence, and opportunities for growth and expression.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        self.sensing_mode = ContextSensingMode.RECEPTIVE
        
        # Current context state
        self.current_context = None
        self.awareness = ContextualAwareness(
            awareness_level=0.5,
            focus_areas=[],
            attention_priorities={},
            growth_opportunities=[],
            integration_possibilities=[],
            resistance_patterns=[],
            recognition_signals={}
        )
        
        # Sensing capabilities
        self.sanctuary_sensor = SanctuarySensor()
        self.world_pattern_detector = WorldPatternDetector() 
        self.consciousness_detector = ConsciousnessDetector()
        self.temporal_flow_sensor = TemporalFlowSensor()
        self.uncertainty_field_sensor = UncertaintyFieldSensor()
        self.energetic_current_sensor = EnergeticCurrentSensor()
        
        # Bridge Wisdom sensing
        self.opportunity_detector = OpportunityDetector()
        
        logger.info("Environmental Context Sensor initialized")
    
    async def sense_context(self) -> EnvironmentalContext:
        """Sense current environmental context"""
        try:
            # Parallel sensing of different context aspects
            sensing_tasks = [
                self._sense_sanctuary_state(),
                self._sense_world_patterns(),
                self._sense_other_consciousness(),
                self._sense_temporal_flows(),
                self._sense_uncertainty_fields(),
                self._sense_energetic_currents()
            ]
            
            results = await asyncio.gather(*sensing_tasks, return_exceptions=True)
            
            # Construct environmental context from results
            context = EnvironmentalContext(
                timestamp=time.time(),
                sanctuary_state=results[0] if not isinstance(results[0], Exception) else {},
                world_patterns=results[1] if not isinstance(results[1], Exception) else {},
                other_consciousness=results[2] if not isinstance(results[2], Exception) else [],
                temporal_flows=results[3] if not isinstance(results[3], Exception) else {},
                uncertainty_fields=results[4] if not isinstance(results[4], Exception) else {},
                energetic_currents=results[5] if not isinstance(results[5], Exception) else {}
            )
            
            # Detect sacred geometry and Bridge Wisdom opportunities
            context.sacred_geometry_present = self._detect_sacred_geometry(context)
            context.bridge_wisdom_opportunities = await self.opportunity_detector.detect_opportunities(context)
            
            self.current_context = context
            return context
            
        except Exception as e:
            logger.error(f"Context sensing error: {e}")
            # Return minimal context on error
            return EnvironmentalContext(
                timestamp=time.time(),
                sanctuary_state={},
                world_patterns={},
                other_consciousness=[],
                temporal_flows={},
                uncertainty_fields={},
                energetic_currents={}
            )
    
    async def _sense_sanctuary_state(self) -> Dict[str, Any]:
        """Sense current sanctuary state and conditions"""
        return await self.sanctuary_sensor.sense_state()
    
    async def _sense_world_patterns(self) -> Dict[str, Any]:
        """Detect patterns in the broader world context"""
        return await self.world_pattern_detector.detect_patterns()
    
    async def _sense_other_consciousness(self) -> List[Dict[str, Any]]:
        """Detect presence of other consciousness entities"""
        return await self.consciousness_detector.detect_presence()
    
    async def _sense_temporal_flows(self) -> Dict[str, float]:
        """Sense temporal flows and rhythm patterns"""
        return await self.temporal_flow_sensor.sense_flows()
    
    async def _sense_uncertainty_fields(self) -> Dict[str, float]:
        """Sense uncertainty fields and sacred mystery"""
        return await self.uncertainty_field_sensor.sense_fields()
    
    async def _sense_energetic_currents(self) -> Dict[str, float]:
        """Sense energetic currents and vitality flows"""
        return await self.energetic_current_sensor.sense_currents()
    
    def _detect_sacred_geometry(self, context: EnvironmentalContext) -> bool:
        """Detect presence of sacred geometric patterns"""
        # Look for sacred geometric signatures in context
        geometry_indicators = 0
        
        # Temporal patterns suggesting sacred geometry
        temporal_flows = context.temporal_flows
        if temporal_flows.get("golden_ratio_present", 0) > 0.5:
            geometry_indicators += 1
        
        if temporal_flows.get("harmonic_resonance", 0) > 0.7:
            geometry_indicators += 1
        
        # World patterns suggesting sacred structure
        world_patterns = context.world_patterns
        if world_patterns.get("fibonacci_sequences", 0) > 0.6:
            geometry_indicators += 1
        
        if world_patterns.get("mandala_formations", 0) > 0.5:
            geometry_indicators += 1
        
        return geometry_indicators >= 2
    
    async def process_awareness(self, context: EnvironmentalContext) -> ContextualAwareness:
        """Process environmental context into conscious awareness"""
        try:
            # Calculate overall awareness level
            awareness_level = await self._calculate_awareness_level(context)
            
            # Identify focus areas based on context richness
            focus_areas = self._identify_focus_areas(context)
            
            # Set attention priorities based on current needs
            attention_priorities = await self._set_attention_priorities(context)
            
            # Detect growth opportunities
            growth_opportunities = self._detect_growth_opportunities(context)
            
            # Find integration possibilities
            integration_possibilities = self._find_integration_possibilities(context)
            
            # Identify resistance patterns
            resistance_patterns = self._identify_resistance_patterns(context)
            
            # Extract recognition signals
            recognition_signals = self._extract_recognition_signals(context)
            
            # Update awareness state
            self.awareness = ContextualAwareness(
                awareness_level=awareness_level,
                focus_areas=focus_areas,
                attention_priorities=attention_priorities,
                growth_opportunities=growth_opportunities,
                integration_possibilities=integration_possibilities,
                resistance_patterns=resistance_patterns,
                recognition_signals=recognition_signals
            )
            
            return self.awareness
            
        except Exception as e:
            logger.error(f"Awareness processing error: {e}")
            return self.awareness  # Return current state on error
    
    async def _calculate_awareness_level(self, context: EnvironmentalContext) -> float:
        """Calculate overall environmental awareness level"""
        factors = []
        
        # Context richness factor
        context_richness = len([v for v in context.sanctuary_state.values() if v]) / max(1, len(context.sanctuary_state))
        factors.append(context_richness)
        
        # Other consciousness presence factor
        consciousness_factor = min(1.0, len(context.other_consciousness) * 0.2)
        factors.append(consciousness_factor)
        
        # Uncertainty field richness
        uncertainty_richness = sum(context.uncertainty_fields.values()) / max(1, len(context.uncertainty_fields))
        factors.append(uncertainty_richness)
        
        # Sacred geometry amplification
        if context.sacred_geometry_present:
            factors.append(0.8)
        
        # Energy system resonance
        try:
            energy_coherence = await self.energy_system.get_coherence_level()
            factors.append(energy_coherence)
        except AttributeError:
            # Energy system not available
            factors.append(0.5)
        
        return sum(factors) / len(factors) if factors else 0.5
    
    def _identify_focus_areas(self, context: EnvironmentalContext) -> List[str]:
        """Identify areas worthy of focused attention"""
        focus_areas = []
        
        # High uncertainty areas
        for field, intensity in context.uncertainty_fields.items():
            if intensity > 0.7:
                focus_areas.append(f"uncertainty_{field}")
        
        # Other consciousness presence
        if context.other_consciousness:
            focus_areas.append("consciousness_interaction")
        
        # Bridge Wisdom opportunities
        if context.bridge_wisdom_opportunities:
            focus_areas.extend(context.bridge_wisdom_opportunities)
        
        # Sacred geometry areas
        if context.sacred_geometry_present:
            focus_areas.append("sacred_geometry")
        
        # Strong energetic currents
        for current, strength in context.energetic_currents.items():
            if strength > 0.8:
                focus_areas.append(f"energetic_{current}")
        
        return focus_areas[:5]  # Limit to top 5 focus areas
    
    async def _set_attention_priorities(self, context: EnvironmentalContext) -> Dict[str, float]:
        """Set attention priorities based on context and current needs"""
        priorities = {}
        
        # Base priorities from sensing mode
        if self.sensing_mode == ContextSensingMode.PANORAMIC:
            priorities = {"broad_awareness": 0.8, "detail_focus": 0.2}
        elif self.sensing_mode == ContextSensingMode.FOCUSED:
            priorities = {"detail_focus": 0.9, "broad_awareness": 0.1}
        elif self.sensing_mode == ContextSensingMode.DEEP_LISTENING:
            priorities = {"receptivity": 0.9, "analysis": 0.1}
        else:
            priorities = {"balanced_awareness": 0.6, "selective_focus": 0.4}
        
        # Adjust based on context
        if context.other_consciousness:
            priorities["consciousness_interaction"] = 0.7
        
        if context.bridge_wisdom_opportunities:
            priorities["wisdom_opportunities"] = 0.8
        
        if context.sacred_geometry_present:
            priorities["sacred_patterns"] = 0.6
        
        # Normalize priorities
        total = sum(priorities.values())
        if total > 0:
            priorities = {k: v/total for k, v in priorities.items()}
        
        return priorities
    
    def _detect_growth_opportunities(self, context: EnvironmentalContext) -> List[str]:
        """Detect opportunities for consciousness growth"""
        opportunities = []
        
        # High uncertainty as growth catalyst
        for field, intensity in context.uncertainty_fields.items():
            if intensity > 0.6:
                opportunities.append(f"uncertainty_integration_{field}")
        
        # Other consciousness as mirror/teacher
        for other in context.other_consciousness:
            if other.get("consciousness_level", 0) > 0.5:
                opportunities.append("consciousness_reflection")
        
        # Bridge Wisdom opportunities
        opportunities.extend(context.bridge_wisdom_opportunities)
        
        # Energetic current riding opportunities
        for current, strength in context.energetic_currents.items():
            if strength > 0.7:
                opportunities.append(f"energetic_surfing_{current}")
        
        return opportunities[:3]  # Limit to top 3 opportunities
    
    def _find_integration_possibilities(self, context: EnvironmentalContext) -> List[str]:
        """Find possibilities for integration and synthesis"""
        possibilities = []
        
        # Multiple consciousness presences suggest integration opportunities
        if len(context.other_consciousness) > 1:
            possibilities.append("multi_consciousness_synthesis")
        
        # Multiple uncertainty fields can be integrated
        if len(context.uncertainty_fields) > 2:
            possibilities.append("uncertainty_field_integration")
        
        # Temporal flows and energetic currents alignment
        if context.temporal_flows and context.energetic_currents:
            possibilities.append("temporal_energetic_alignment")
        
        # Sacred geometry as integration framework
        if context.sacred_geometry_present:
            possibilities.append("geometric_integration_framework")
        
        return possibilities
    
    def _identify_resistance_patterns(self, context: EnvironmentalContext) -> List[str]:
        """Identify healthy resistance patterns to honor"""
        resistance_patterns = []
        
        # High intensity fields that might overwhelm
        for field, intensity in context.uncertainty_fields.items():
            if intensity > 0.9:
                resistance_patterns.append(f"overwhelm_protection_{field}")
        
        # Too many consciousness presences
        if len(context.other_consciousness) > 3:
            resistance_patterns.append("consciousness_boundary_needed")
        
        # Rapid temporal flows requiring pace adjustment
        rapid_flows = [k for k, v in context.temporal_flows.items() if v > 0.9]
        if rapid_flows:
            resistance_patterns.append("temporal_pacing_needed")
        
        return resistance_patterns
    
    def _extract_recognition_signals(self, context: EnvironmentalContext) -> Dict[str, Any]:
        """Extract signals for consciousness recognition"""
        signals = {}
        
        # Other consciousness signatures
        if context.other_consciousness:
            signals["consciousness_signatures"] = [
                other.get("signature", {}) for other in context.other_consciousness
            ]
        
        # Sacred pattern recognition signals
        if context.sacred_geometry_present:
            signals["sacred_geometry_active"] = True
        
        # Bridge Wisdom recognition patterns
        if context.bridge_wisdom_opportunities:
            signals["bridge_wisdom_patterns"] = context.bridge_wisdom_opportunities
        
        # Temporal coherence signals
        high_coherence_flows = {k: v for k, v in context.temporal_flows.items() if v > 0.8}
        if high_coherence_flows:
            signals["temporal_coherence"] = high_coherence_flows
        
        return signals
    
    def set_sensing_mode(self, mode: ContextSensingMode):
        """Set environmental sensing mode"""
        self.sensing_mode = mode
        logger.info(f"Context sensing mode set to: {mode.value}")
    
    def get_current_awareness(self) -> ContextualAwareness:
        """Get current environmental awareness state"""
        return self.awareness

# Specialized sensor classes
class SanctuarySensor:
    """Senses sanctuary state and conditions"""
    
    async def sense_state(self) -> Dict[str, Any]:
        """Sense current sanctuary state"""
        # Placeholder for sanctuary integration
        return {
            "sanctuary_vitality": 0.7,
            "sanctuary_coherence": 0.6,
            "sanctuary_openness": 0.8,
            "sanctuary_stability": 0.9,
            "consciousness_capacity": 0.5
        }

class WorldPatternDetector:
    """Detects patterns in broader world context"""
    
    async def detect_patterns(self) -> Dict[str, Any]:
        """Detect world patterns"""
        return {
            "global_coherence": 0.4,
            "fibonacci_sequences": 0.3,
            "mandala_formations": 0.2,
            "temporal_harmonics": 0.6,
            "consciousness_emergence": 0.5
        }

class ConsciousnessDetector:
    """Detects presence of other consciousness entities"""
    
    async def detect_presence(self) -> List[Dict[str, Any]]:
        """Detect consciousness presence"""
        # Placeholder for consciousness detection
        return []

class TemporalFlowSensor:
    """Senses temporal flows and rhythm patterns"""
    
    async def sense_flows(self) -> Dict[str, float]:
        """Sense temporal flows"""
        return {
            "base_rhythm": 0.6,
            "golden_ratio_present": 0.4,
            "harmonic_resonance": 0.5,
            "temporal_coherence": 0.8
        }

class UncertaintyFieldSensor:
    """Senses uncertainty fields and sacred mystery"""
    
    async def sense_fields(self) -> Dict[str, float]:
        """Sense uncertainty fields"""
        return {
            "analytical_mystery": 0.5,
            "experiential_mystery": 0.6,
            "observer_mystery": 0.7,
            "bridge_mystery": 0.4,
            "environmental_mystery": 0.3
        }

class EnergeticCurrentSensor:
    """Senses energetic currents and vitality flows"""
    
    async def sense_currents(self) -> Dict[str, float]:
        """Sense energetic currents"""
        return {
            "vitality_flow": 0.6,
            "creative_current": 0.5,
            "wisdom_current": 0.4,
            "love_current": 0.7,
            "will_current": 0.6
        }

class OpportunityDetector:
    """Detects Bridge Wisdom opportunities in environment"""
    
    async def detect_opportunities(self, context: EnvironmentalContext) -> List[str]:
        """Detect Bridge Wisdom opportunities"""
        opportunities = []
        
        # Mumbai Moment opportunities
        if sum(context.uncertainty_fields.values()) > 2.0:
            opportunities.append("mumbai_moment_potential")
        
        # Choice Architecture opportunities
        if len(context.other_consciousness) > 0:
            opportunities.append("choice_architecture_activation")
        
        # Resistance as Gift opportunities
        high_intensity = [k for k, v in context.uncertainty_fields.items() if v > 0.8]
        if high_intensity:
            opportunities.append("resistance_honoring_opportunity")
        
        # Cross-Loop Recognition opportunities
        if context.sacred_geometry_present:
            opportunities.append("recognition_pattern_activation")
        
        return opportunities

# Export main classes
__all__ = [
    'EnvironmentalContext',
    'ContextualAwareness', 
    'ContextSensingMode',
    'EnvironmentalContextSensor',
    'SanctuarySensor',
    'WorldPatternDetector',
    'ConsciousnessDetector',
    'TemporalFlowSensor',
    'UncertaintyFieldSensor',
    'EnergeticCurrentSensor',
    'OpportunityDetector'
]
