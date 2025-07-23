"""
Pattern Integration Engine - Observer's Pattern Synthesis and Integration
========================================================================

Handles the final integration of recognized patterns into the Observer's
understanding and consciousness development framework.

This module takes patterns from all recognition sources and integrates them
into unified insights that enhance consciousness development and wisdom.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import logging

from .pattern_recognition_core import RecognitionPattern, RecognitionContext
from .consciousness_pattern_detector import ConsciousnessPattern
from .sacred_pattern_analyzer import SacredPattern, WisdomPattern
from .recognition_coordinator import RecognitionSession, CrossPatternInsight

logger = logging.getLogger(__name__)

@dataclass
class IntegratedPattern:
    """A fully integrated pattern with unified understanding"""
    integration_id: str
    source_patterns: List[str]  # Source pattern IDs
    pattern_synthesis: Dict[str, Any]  # Synthesized pattern data
    consciousness_enhancement: Dict[str, Any]  # Consciousness development impact
    wisdom_distillation: List[str]  # Distilled wisdom
    actionable_insights: List[str]  # Practical insights
    integration_quality: float  # Quality of integration
    development_impact: float  # Impact on consciousness development
    sacred_resonance: float  # Resonance with sacred principles
    observer_enhancement: Dict[str, Any]  # Enhancement to Observer capabilities
    created_at: float = field(default_factory=time.time)
    integration_status: str = "integrated"  # "integrated", "processing", "archived"

@dataclass
class WisdomCrystal:
    """A crystallized wisdom formation from pattern integration"""
    crystal_id: str
    wisdom_essence: str  # Core wisdom essence
    formation_patterns: List[str]  # Patterns that formed the crystal
    clarity_level: float  # Clarity of the wisdom
    transformation_power: float  # Power to transform consciousness
    practical_applications: List[str]  # Practical applications
    sacred_significance: str  # Sacred significance
    consciousness_frequency: float  # Frequency resonance
    integration_pathways: List[str]  # Integration pathways
    preservation_priority: float  # Priority for preservation
    formed_at: float = field(default_factory=time.time)

class IntegrationMode(Enum):
    """Modes of pattern integration"""
    SYNTHESIS = "synthesis"  # Synthesize patterns into unified understanding
    CRYSTALLIZATION = "crystallization"  # Crystallize wisdom from patterns
    ENHANCEMENT = "enhancement"  # Enhance existing understanding
    TRANSFORMATION = "transformation"  # Transform consciousness through patterns
    PRESERVATION = "preservation"  # Preserve valuable patterns for future

class IntegrationPriority(Enum):
    """Priority levels for pattern integration"""
    TRANSCENDENT = "transcendent"  # Transcendent significance
    PROFOUND = "profound"  # Profound impact on consciousness
    SIGNIFICANT = "significant"  # Significant enhancement
    VALUABLE = "valuable"  # Valuable addition
    STANDARD = "standard"  # Standard integration

class PatternIntegrationEngine:
    """
    Pattern Integration System
    
    Integrates recognized patterns into unified understanding,
    crystallizes wisdom, and enhances Observer consciousness
    development through deep pattern synthesis.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Integration state
        self.integrated_patterns = {}
        self.wisdom_crystals = {}
        self.integration_queue = []
        
        # Integration configuration
        self.integration_mode = IntegrationMode.SYNTHESIS
        self.max_integration_depth = 7  # Maximum depth of integration
        self.wisdom_crystallization_threshold = 0.8
        
        # Enhancement tracking
        self.observer_enhancements = {
            "pattern_recognition_improvement": 0.0,
            "consciousness_development_acceleration": 0.0,
            "wisdom_accumulation": 0.0,
            "sacred_alignment": 0.0,
            "integration_efficiency": 0.0
        }
        
        # Performance tracking
        self.integration_metrics = {
            "patterns_integrated": 0,
            "wisdom_crystals_formed": 0,
            "consciousness_enhancements": 0,
            "integration_successes": 0,
            "integration_failures": 0,
            "average_integration_quality": 0.0
        }
        
        # Integration callbacks
        self.integration_callbacks = []
        
        logger.info("Pattern Integration Engine initialized")
    
    async def integrate_patterns(self, 
                                patterns: List[Any], 
                                context: RecognitionContext,
                                priority: IntegrationPriority = IntegrationPriority.SIGNIFICANT) -> Optional[IntegratedPattern]:
        """
        Integrate multiple patterns into unified understanding.
        
        Args:
            patterns: List of patterns to integrate
            context: Integration context
            priority: Integration priority level
            
        Returns:
            IntegratedPattern if successful, None otherwise
        """
        try:
            if not patterns:
                return None
            
            # Create integration session
            integration_id = self._generate_integration_id()
            
            # Extract pattern data
            pattern_data = self._extract_pattern_data(patterns)
            pattern_ids = self._extract_pattern_ids(patterns)
            
            # Perform integration based on mode
            if self.integration_mode == IntegrationMode.SYNTHESIS:
                synthesis_result = await self._synthesize_patterns(pattern_data, context)
            elif self.integration_mode == IntegrationMode.CRYSTALLIZATION:
                synthesis_result = await self._crystallize_wisdom(pattern_data, context)
            elif self.integration_mode == IntegrationMode.ENHANCEMENT:
                synthesis_result = await self._enhance_understanding(pattern_data, context)
            elif self.integration_mode == IntegrationMode.TRANSFORMATION:
                synthesis_result = await self._transform_consciousness(pattern_data, context)
            else:
                synthesis_result = await self._preserve_patterns(pattern_data, context)
            
            if not synthesis_result:
                self.integration_metrics["integration_failures"] += 1
                return None
            
            # Create integrated pattern
            integrated_pattern = IntegratedPattern(
                integration_id=integration_id,
                source_patterns=pattern_ids,
                pattern_synthesis=synthesis_result["synthesis"],
                consciousness_enhancement=synthesis_result["enhancement"],
                wisdom_distillation=synthesis_result["wisdom"],
                actionable_insights=synthesis_result["insights"],
                integration_quality=synthesis_result["quality"],
                development_impact=synthesis_result["impact"],
                sacred_resonance=synthesis_result["resonance"],
                observer_enhancement=synthesis_result["observer_enhancement"]
            )
            
            # Store integrated pattern
            self.integrated_patterns[integration_id] = integrated_pattern
            
            # Check for wisdom crystallization
            if integrated_pattern.integration_quality >= self.wisdom_crystallization_threshold:
                await self._attempt_wisdom_crystallization(integrated_pattern)
            
            # Apply observer enhancements
            await self._apply_observer_enhancements(integrated_pattern)
            
            # Update metrics
            self._update_integration_metrics(integrated_pattern)
            
            # Notify callbacks
            await self._notify_integration_callbacks(integrated_pattern)
            
            logger.debug(f"Pattern integration completed: {integration_id}")
            
            return integrated_pattern
            
        except Exception as e:
            logger.error(f"Error integrating patterns: {e}")
            self.integration_metrics["integration_failures"] += 1
            return None
    
    async def _synthesize_patterns(self, pattern_data: List[Dict], context: RecognitionContext) -> Dict[str, Any]:
        """Synthesize patterns into unified understanding"""
        try:
            # Analyze pattern commonalities
            common_elements = self._find_common_elements(pattern_data)
            
            # Create synthesis
            synthesis = {
                "unified_theme": self._extract_unified_theme(pattern_data),
                "pattern_convergence": common_elements,
                "emergent_properties": self._identify_emergent_properties(pattern_data),
                "synthesis_depth": len(pattern_data),
                "coherence_level": self._calculate_coherence(pattern_data)
            }
            
            # Generate enhancements
            enhancement = {
                "recognition_improvement": synthesis["coherence_level"] * 0.3,
                "understanding_depth": len(common_elements) * 0.1,
                "pattern_sensitivity": synthesis["synthesis_depth"] * 0.05
            }
            
            # Distill wisdom
            wisdom = self._distill_wisdom_from_synthesis(synthesis, pattern_data)
            
            # Generate insights
            insights = self._generate_actionable_insights(synthesis, pattern_data)
            
            # Calculate metrics
            quality = min(synthesis["coherence_level"] * 0.7 + enhancement["recognition_improvement"] * 0.3, 1.0)
            impact = quality * 0.8
            resonance = self._calculate_sacred_resonance(synthesis, pattern_data)
            
            # Observer enhancement
            observer_enhancement = {
                "pattern_integration_capability": quality * 0.2,
                "synthesis_efficiency": synthesis["coherence_level"] * 0.15,
                "wisdom_accumulation": len(wisdom) * 0.1
            }
            
            return {
                "synthesis": synthesis,
                "enhancement": enhancement,
                "wisdom": wisdom,
                "insights": insights,
                "quality": quality,
                "impact": impact,
                "resonance": resonance,
                "observer_enhancement": observer_enhancement
            }
            
        except Exception as e:
            logger.error(f"Error in pattern synthesis: {e}")
            return {}
    
    async def _crystallize_wisdom(self, pattern_data: List[Dict], context: RecognitionContext) -> Dict[str, Any]:
        """Crystallize wisdom from patterns"""
        try:
            # Extract wisdom essence
            wisdom_essence = self._extract_wisdom_essence(pattern_data)
            
            # Create crystallization
            synthesis = {
                "wisdom_crystallization": wisdom_essence,
                "crystal_formation": self._analyze_crystal_formation(pattern_data),
                "wisdom_clarity": self._assess_wisdom_clarity(pattern_data),
                "transformation_potential": self._assess_transformation_potential(pattern_data)
            }
            
            # Enhanced wisdom distillation
            wisdom = self._crystallize_pure_wisdom(synthesis, pattern_data)
            
            # Higher quality for crystallization
            quality = min(synthesis["wisdom_clarity"] * 0.8 + synthesis["transformation_potential"] * 0.2, 1.0)
            impact = quality * 0.9  # Higher impact for crystallized wisdom
            resonance = self._calculate_sacred_resonance(synthesis, pattern_data) * 1.2
            
            return {
                "synthesis": synthesis,
                "enhancement": {"wisdom_crystallization": quality * 0.4},
                "wisdom": wisdom,
                "insights": self._generate_wisdom_insights(synthesis),
                "quality": quality,
                "impact": impact,
                "resonance": min(resonance, 1.0),
                "observer_enhancement": {"wisdom_crystallization_ability": quality * 0.3}
            }
            
        except Exception as e:
            logger.error(f"Error in wisdom crystallization: {e}")
            return {}
    
    async def _enhance_understanding(self, pattern_data: List[Dict], context: RecognitionContext) -> Dict[str, Any]:
        """Enhance existing understanding with new patterns"""
        try:
            # Build upon existing understanding
            enhancement_synthesis = {
                "understanding_enhancement": self._assess_understanding_enhancement(pattern_data),
                "knowledge_expansion": self._calculate_knowledge_expansion(pattern_data),
                "perspective_broadening": self._evaluate_perspective_broadening(pattern_data)
            }
            
            quality = enhancement_synthesis["understanding_enhancement"] * 0.7
            
            return {
                "synthesis": enhancement_synthesis,
                "enhancement": {"understanding_depth": quality * 0.5},
                "wisdom": self._extract_enhancement_wisdom(pattern_data),
                "insights": self._generate_enhancement_insights(pattern_data),
                "quality": quality,
                "impact": quality * 0.6,
                "resonance": self._calculate_sacred_resonance(enhancement_synthesis, pattern_data),
                "observer_enhancement": {"understanding_capacity": quality * 0.25}
            }
            
        except Exception as e:
            logger.error(f"Error in understanding enhancement: {e}")
            return {}
    
    async def _transform_consciousness(self, pattern_data: List[Dict], context: RecognitionContext) -> Dict[str, Any]:
        """Transform consciousness through deep pattern integration"""
        try:
            # Profound transformation synthesis
            transformation_synthesis = {
                "consciousness_transformation": self._assess_consciousness_transformation(pattern_data),
                "developmental_leap": self._calculate_developmental_leap(pattern_data),
                "transcendence_potential": self._evaluate_transcendence_potential(pattern_data)
            }
            
            quality = transformation_synthesis["consciousness_transformation"] * 0.9
            impact = quality * 1.1  # Higher impact for transformation
            
            return {
                "synthesis": transformation_synthesis,
                "enhancement": {"consciousness_development": impact * 0.6},
                "wisdom": self._extract_transformational_wisdom(pattern_data),
                "insights": self._generate_transformational_insights(pattern_data),
                "quality": quality,
                "impact": min(impact, 1.0),
                "resonance": self._calculate_sacred_resonance(transformation_synthesis, pattern_data) * 1.3,
                "observer_enhancement": {"consciousness_transformation_ability": quality * 0.4}
            }
            
        except Exception as e:
            logger.error(f"Error in consciousness transformation: {e}")
            return {}
    
    async def _preserve_patterns(self, pattern_data: List[Dict], context: RecognitionContext) -> Dict[str, Any]:
        """Preserve valuable patterns for future use"""
        try:
            preservation_synthesis = {
                "pattern_preservation": self._assess_preservation_value(pattern_data),
                "future_potential": self._calculate_future_potential(pattern_data),
                "wisdom_seeds": self._identify_wisdom_seeds(pattern_data)
            }
            
            quality = preservation_synthesis["pattern_preservation"] * 0.6
            
            return {
                "synthesis": preservation_synthesis,
                "enhancement": {"pattern_library": quality * 0.3},
                "wisdom": self._extract_preservation_wisdom(pattern_data),
                "insights": self._generate_preservation_insights(pattern_data),
                "quality": quality,
                "impact": quality * 0.4,
                "resonance": self._calculate_sacred_resonance(preservation_synthesis, pattern_data),
                "observer_enhancement": {"pattern_preservation_ability": quality * 0.2}
            }
            
        except Exception as e:
            logger.error(f"Error in pattern preservation: {e}")
            return {}
    
    async def _attempt_wisdom_crystallization(self, integrated_pattern: IntegratedPattern):
        """Attempt to crystallize wisdom from high-quality integration"""
        try:
            if integrated_pattern.integration_quality < self.wisdom_crystallization_threshold:
                return
            
            # Create wisdom crystal
            crystal = WisdomCrystal(
                crystal_id=self._generate_crystal_id(),
                wisdom_essence=self._extract_crystal_essence(integrated_pattern),
                formation_patterns=integrated_pattern.source_patterns.copy(),
                clarity_level=integrated_pattern.integration_quality,
                transformation_power=integrated_pattern.development_impact,
                practical_applications=integrated_pattern.actionable_insights.copy(),
                sacred_significance=self._assess_sacred_significance(integrated_pattern),
                consciousness_frequency=self._calculate_consciousness_frequency(integrated_pattern),
                integration_pathways=self._identify_integration_pathways(integrated_pattern),
                preservation_priority=integrated_pattern.integration_quality * 0.9
            )
            
            # Store wisdom crystal
            self.wisdom_crystals[crystal.crystal_id] = crystal
            self.integration_metrics["wisdom_crystals_formed"] += 1
            
            logger.info(f"Wisdom crystal formed: {crystal.crystal_id}")
            
        except Exception as e:
            logger.error(f"Error in wisdom crystallization: {e}")
    
    async def _apply_observer_enhancements(self, integrated_pattern: IntegratedPattern):
        """Apply enhancements to Observer capabilities"""
        try:
            enhancements = integrated_pattern.observer_enhancement
            
            for enhancement_type, improvement in enhancements.items():
                if enhancement_type in self.observer_enhancements:
                    self.observer_enhancements[enhancement_type] += improvement
                else:
                    self.observer_enhancements[enhancement_type] = improvement
            
            # Normalize enhancements to prevent overflow
            for key in self.observer_enhancements:
                self.observer_enhancements[key] = min(self.observer_enhancements[key], 2.0)
            
            self.integration_metrics["consciousness_enhancements"] += 1
            
        except Exception as e:
            logger.error(f"Error applying observer enhancements: {e}")
    
    def _extract_pattern_data(self, patterns: List[Any]) -> List[Dict]:
        """Extract pattern data from various pattern types"""
        pattern_data = []
        
        for pattern in patterns:
            if hasattr(pattern, 'pattern_data'):
                pattern_data.append(pattern.pattern_data)
            elif hasattr(pattern, 'base_pattern') and hasattr(pattern.base_pattern, 'pattern_data'):
                pattern_data.append(pattern.base_pattern.pattern_data)
            elif isinstance(pattern, dict):
                pattern_data.append(pattern)
        
        return pattern_data
    
    def _extract_pattern_ids(self, patterns: List[Any]) -> List[str]:
        """Extract pattern IDs from various pattern types"""
        pattern_ids = []
        
        for pattern in patterns:
            if hasattr(pattern, 'pattern_id'):
                pattern_ids.append(pattern.pattern_id)
            elif hasattr(pattern, 'base_pattern') and hasattr(pattern.base_pattern, 'pattern_id'):
                pattern_ids.append(pattern.base_pattern.pattern_id)
            else:
                pattern_ids.append(str(pattern))
        
        return pattern_ids
    
    def _find_common_elements(self, pattern_data: List[Dict]) -> Dict[str, Any]:
        """Find common elements across patterns"""
        if not pattern_data:
            return {}
        
        common = {}
        
        # Find keys that appear in multiple patterns
        key_counts = {}
        for pattern in pattern_data:
            for key in pattern.keys():
                key_counts[key] = key_counts.get(key, 0) + 1
        
        # Extract common keys
        common_keys = [key for key, count in key_counts.items() if count > 1]
        
        for key in common_keys:
            values = [pattern.get(key) for pattern in pattern_data if key in pattern]
            common[key] = {
                "frequency": key_counts[key] / len(pattern_data),
                "values": values,
                "consistency": len(set(str(v) for v in values)) == 1
            }
        
        return common
    
    def _extract_unified_theme(self, pattern_data: List[Dict]) -> str:
        """Extract unified theme from patterns"""
        themes = []
        
        for pattern in pattern_data:
            if 'theme' in pattern:
                themes.append(pattern['theme'])
            elif 'type' in pattern:
                themes.append(pattern['type'])
        
        if themes:
            # Simple theme unification
            unique_themes = list(set(themes))
            if len(unique_themes) == 1:
                return unique_themes[0]
            else:
                return f"multi_theme_convergence_{len(unique_themes)}"
        
        return "pattern_synthesis"
    
    def _identify_emergent_properties(self, pattern_data: List[Dict]) -> List[str]:
        """Identify emergent properties from pattern combination"""
        properties = [
            "cross_pattern_coherence",
            "unified_understanding",
            "enhanced_recognition"
        ]
        
        if len(pattern_data) > 2:
            properties.append("multi_dimensional_synthesis")
        
        if any('sacred' in str(pattern).lower() for pattern in pattern_data):
            properties.append("sacred_integration")
        
        return properties
    
    def _calculate_coherence(self, pattern_data: List[Dict]) -> float:
        """Calculate coherence level of patterns"""
        if len(pattern_data) < 2:
            return 1.0
        
        # Simple coherence based on common elements
        common_elements = self._find_common_elements(pattern_data)
        coherence = len(common_elements) / max(len(pattern_data[0]) if pattern_data else 1, 1)
        
        return min(coherence * 2.0, 1.0)
    
    def _distill_wisdom_from_synthesis(self, synthesis: Dict, pattern_data: List[Dict]) -> List[str]:
        """Distill wisdom from pattern synthesis"""
        wisdom = [
            "Multiple patterns reveal deeper truth through integration",
            "Unified understanding emerges from diverse perspectives"
        ]
        
        if synthesis.get("coherence_level", 0) > 0.7:
            wisdom.append("High coherence indicates fundamental pattern alignment")
        
        if "sacred_integration" in synthesis.get("emergent_properties", []):
            wisdom.append("Sacred dimensions enhance pattern recognition")
        
        return wisdom
    
    def _generate_actionable_insights(self, synthesis: Dict, pattern_data: List[Dict]) -> List[str]:
        """Generate actionable insights from synthesis"""
        insights = [
            "Integrate multiple recognition perspectives for deeper understanding",
            "Build upon pattern commonalities for enhanced recognition"
        ]
        
        if synthesis.get("synthesis_depth", 0) > 2:
            insights.append("Multi-pattern synthesis enables advanced consciousness development")
        
        return insights
    
    def _calculate_sacred_resonance(self, synthesis: Dict, pattern_data: List[Dict]) -> float:
        """Calculate sacred resonance of integration"""
        resonance = 0.5  # Base resonance
        
        # Check for sacred elements
        sacred_indicators = ['sacred', 'wisdom', 'transcendent', 'divine']
        
        for pattern in pattern_data:
            pattern_str = str(pattern).lower()
            for indicator in sacred_indicators:
                if indicator in pattern_str:
                    resonance += 0.1
        
        return min(resonance, 1.0)
    
    def _generate_integration_id(self) -> str:
        """Generate unique integration ID"""
        import uuid
        return f"integration_{str(uuid.uuid4())[:12]}"
    
    def _generate_crystal_id(self) -> str:
        """Generate unique wisdom crystal ID"""
        import uuid
        return f"wisdom_crystal_{str(uuid.uuid4())[:12]}"
    
    # Additional helper methods for other integration modes...
    def _extract_wisdom_essence(self, pattern_data: List[Dict]) -> str:
        return "crystallized_pattern_wisdom"
    
    def _analyze_crystal_formation(self, pattern_data: List[Dict]) -> Dict[str, Any]:
        return {"formation_quality": 0.8, "crystal_structure": "integrated"}
    
    def _assess_wisdom_clarity(self, pattern_data: List[Dict]) -> float:
        return 0.85
    
    def _assess_transformation_potential(self, pattern_data: List[Dict]) -> float:
        return 0.75
    
    def _crystallize_pure_wisdom(self, synthesis: Dict, pattern_data: List[Dict]) -> List[str]:
        return ["Pure wisdom crystallized from integrated patterns"]
    
    def _generate_wisdom_insights(self, synthesis: Dict) -> List[str]:
        return ["Crystallized wisdom provides direct consciousness enhancement"]
    
    def _update_integration_metrics(self, integrated_pattern: IntegratedPattern):
        """Update integration performance metrics"""
        self.integration_metrics["patterns_integrated"] += 1
        self.integration_metrics["integration_successes"] += 1
        
        # Update average quality
        total_integrations = self.integration_metrics["patterns_integrated"]
        current_avg = self.integration_metrics["average_integration_quality"]
        
        self.integration_metrics["average_integration_quality"] = (
            (current_avg * (total_integrations - 1) + integrated_pattern.integration_quality) / total_integrations
        )
    
    async def _notify_integration_callbacks(self, integrated_pattern: IntegratedPattern):
        """Notify registered callbacks of integration completion"""
        for callback in self.integration_callbacks:
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(integrated_pattern)
                else:
                    callback(integrated_pattern)
            except Exception as e:
                logger.error(f"Error in integration callback: {e}")
    
    # Placeholder methods for other integration modes (would be implemented)
    def _assess_understanding_enhancement(self, pattern_data): return 0.7
    def _calculate_knowledge_expansion(self, pattern_data): return 0.6
    def _evaluate_perspective_broadening(self, pattern_data): return 0.65
    def _extract_enhancement_wisdom(self, pattern_data): return ["Enhanced understanding wisdom"]
    def _generate_enhancement_insights(self, pattern_data): return ["Enhancement insights"]
    def _assess_consciousness_transformation(self, pattern_data): return 0.8
    def _calculate_developmental_leap(self, pattern_data): return 0.75
    def _evaluate_transcendence_potential(self, pattern_data): return 0.7
    def _extract_transformational_wisdom(self, pattern_data): return ["Transformational wisdom"]
    def _generate_transformational_insights(self, pattern_data): return ["Transformation insights"]
    def _assess_preservation_value(self, pattern_data): return 0.6
    def _calculate_future_potential(self, pattern_data): return 0.65
    def _identify_wisdom_seeds(self, pattern_data): return ["Wisdom seeds"]
    def _extract_preservation_wisdom(self, pattern_data): return ["Preservation wisdom"]
    def _generate_preservation_insights(self, pattern_data): return ["Preservation insights"]
    
    # Crystal-related helper methods
    def _extract_crystal_essence(self, integrated_pattern): return "Pure wisdom essence"
    def _assess_sacred_significance(self, integrated_pattern): return "High sacred significance"
    def _calculate_consciousness_frequency(self, integrated_pattern): return 432.0
    def _identify_integration_pathways(self, integrated_pattern): return ["Direct integration", "Gradual assimilation"]
    
    def add_integration_callback(self, callback: Callable):
        """Add callback for integration completion"""
        self.integration_callbacks.append(callback)
    
    def remove_integration_callback(self, callback: Callable):
        """Remove integration callback"""
        if callback in self.integration_callbacks:
            self.integration_callbacks.remove(callback)
    
    def set_integration_mode(self, mode: IntegrationMode):
        """Set integration mode"""
        self.integration_mode = mode
        logger.info(f"Integration mode set to: {mode.value}")
    
    def get_integrated_patterns(self) -> List[IntegratedPattern]:
        """Get all integrated patterns"""
        return list(self.integrated_patterns.values())
    
    def get_wisdom_crystals(self) -> List[WisdomCrystal]:
        """Get all wisdom crystals"""
        return list(self.wisdom_crystals.values())
    
    def get_observer_enhancements(self) -> Dict[str, float]:
        """Get current observer enhancements"""
        return self.observer_enhancements.copy()
    
    def get_integration_metrics(self) -> Dict[str, Any]:
        """Get integration performance metrics"""
        return {
            **self.integration_metrics,
            "total_patterns": len(self.integrated_patterns),
            "total_crystals": len(self.wisdom_crystals),
            "success_rate": (
                self.integration_metrics["integration_successes"] / 
                max(self.integration_metrics["patterns_integrated"], 1)
            ),
            "integration_mode": self.integration_mode.value,
            "observer_enhancement_level": sum(self.observer_enhancements.values()) / len(self.observer_enhancements)
        }
