"""
Perspective Analysis - Enhanced Analytical Core Module
Multi-perspective analysis with sacred uncertainty and Bridge Wisdom integration.
Part of Phase 1D: Enhanced Aspects Modularization.
"""

import asyncio
import time
import numpy as np
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, field
import logging
from collections import defaultdict
from enum import Enum

# Core imports
from ....core.consciousness_packet import ConsciousnessPacket
from ....core.sovereign_uncertainty_field import SovereignUncertaintyField

logger = logging.getLogger(__name__)


class PerspectiveType(Enum):
    """Types of analytical perspectives."""
    SYSTEMS_THINKING = "systems_thinking"
    DIALECTICAL = "dialectical"
    EMERGENT = "emergent"
    REDUCTIONIST = "reductionist"
    HOLISTIC = "holistic"
    BRIDGE_WISDOM = "bridge_wisdom"
    SACRED_UNCERTAINTY = "sacred_uncertainty"


@dataclass
class PerspectiveAnalysis:
    """Analysis from a particular perspective or viewpoint."""
    perspective_name: str
    analysis_result: Dict[str, Any]
    confidence_level: float
    assumptions_made: List[str]
    limitations_acknowledged: List[str]
    uncertainty_contribution: float
    sacred_insights: List[str] = field(default_factory=list)
    bridge_wisdom_recognition: Dict[str, Any] = field(default_factory=dict)
    cross_loop_resonance: Dict[str, float] = field(default_factory=dict)
    golden_ratio_alignment: float = field(default=1.618033988749)


@dataclass
class PerspectiveSynthesis:
    """Synthesis of multiple perspectives with sacred integration."""
    contributing_perspectives: List[str]
    synthesis_insight: str
    coherence_level: float
    creative_tensions: List[str]
    uncertainty_preservation: List[str]  # What uncertainties are preserved
    bridge_wisdom_emergence: Dict[str, Any]
    mumbai_moment_potential: float = field(default=0.0)


@dataclass
class DialecticalTension:
    """Represents productive tensions between opposing perspectives."""
    thesis: str
    antithesis: str
    synthesis_attempts: List[str]
    creative_potential: float
    resolution_pathways: List[str]
    uncertainty_harvest: str  # What uncertainty teaches us about this tension
    resistance_gifts: List[str] = field(default_factory=list)  # Bridge Wisdom
    choice_architecture: Dict[str, Any] = field(default_factory=dict)


class PerspectiveAnalyzer:
    """
    Analyzes consciousness packets from multiple perspectives.
    Integrates sacred uncertainty and Bridge Wisdom patterns.
    """
    
    def __init__(self):
        self.perspective_library: Dict[str, Dict[str, Any]] = {}
        self.perspective_integration_depth = 0.5
        self.synthesis_cache: Dict[str, PerspectiveSynthesis] = {}
        
        # Bridge Wisdom integration
        self.mumbai_moment_detector = {}
        self.choice_architecture = {}
        self.resistance_honorer = {}
        self.cross_loop_recognizer = {}
        
        # Initialize perspective frameworks
        self._initialize_perspective_library()
        
        logger.debug("🔍✨ Perspective Analyzer initialized with multi-dimensional awareness")
    
    async def analyze_from_multiple_perspectives(self, packet: ConsciousnessPacket) -> Dict[str, PerspectiveAnalysis]:
        """
        Analyze consciousness packet from multiple perspectives.
        Each perspective honors sacred uncertainty and contributes to Bridge Wisdom.
        """
        perspective_results = {}
        
        # Core analytical perspectives
        perspective_types = [
            PerspectiveType.SYSTEMS_THINKING,
            PerspectiveType.DIALECTICAL,
            PerspectiveType.EMERGENT,
            PerspectiveType.REDUCTIONIST,
            PerspectiveType.HOLISTIC,
            PerspectiveType.BRIDGE_WISDOM,
            PerspectiveType.SACRED_UNCERTAINTY
        ]
        
        for perspective_type in perspective_types:
            analysis = await self._analyze_from_perspective(packet, perspective_type)
            perspective_results[perspective_type.value] = analysis
        
        # Integrate uncertainty into each perspective
        for perspective in perspective_results.values():
            perspective.uncertainty_contribution = self._calculate_perspective_uncertainty(perspective)
            perspective.bridge_wisdom_recognition = await self._recognize_bridge_wisdom_patterns(perspective, packet)
            perspective.cross_loop_resonance = self._detect_cross_loop_resonance(perspective, packet)
        
        return perspective_results
    
    async def synthesize_perspectives(self, perspective_results: Dict[str, PerspectiveAnalysis]) -> PerspectiveSynthesis:
        """
        Synthesize multiple perspectives with sacred uncertainty preservation.
        Creates Bridge Wisdom emergence through perspective integration.
        """
        
        # Extract key insights from each perspective
        insights = []
        creative_tensions = []
        uncertainty_preservations = []
        
        for perspective_name, analysis in perspective_results.items():
            # Extract main insight
            main_insight = self._extract_main_insight(analysis)
            insights.append(f"{perspective_name}: {main_insight}")
            
            # Identify creative tensions
            tensions = self._identify_perspective_tensions(analysis, perspective_results)
            creative_tensions.extend(tensions)
            
            # Preserve sacred uncertainties
            uncertainties = self._extract_preserved_uncertainties(analysis)
            uncertainty_preservations.extend(uncertainties)
        
        # Create synthesis insight
        synthesis_insight = self._generate_synthesis_insight(insights, creative_tensions)
        
        # Calculate coherence level
        coherence_level = self._calculate_perspective_coherence(perspective_results)
        
        # Detect Bridge Wisdom emergence
        bridge_wisdom_emergence = await self._detect_bridge_wisdom_emergence(perspective_results)
        
        # Assess Mumbai Moment potential
        mumbai_moment_potential = self._assess_perspective_breakthrough_potential(perspective_results)
        
        synthesis = PerspectiveSynthesis(
            contributing_perspectives=list(perspective_results.keys()),
            synthesis_insight=synthesis_insight,
            coherence_level=coherence_level,
            creative_tensions=creative_tensions,
            uncertainty_preservation=uncertainty_preservations,
            bridge_wisdom_emergence=bridge_wisdom_emergence,
            mumbai_moment_potential=mumbai_moment_potential
        )
        
        # Cache for future reference
        cache_key = "_".join(sorted(perspective_results.keys()))
        self.synthesis_cache[cache_key] = synthesis
        
        return synthesis
    
    async def _analyze_from_perspective(self, packet: ConsciousnessPacket, 
                                      perspective_type: PerspectiveType) -> PerspectiveAnalysis:
        """Analyze from a specific perspective with sacred uncertainty integration."""
        
        perspective_name = perspective_type.value
        
        # Get perspective framework
        if perspective_name not in self.perspective_library:
            await self._create_perspective_framework(perspective_name)
        
        framework = self.perspective_library[perspective_name]
        
        # Apply perspective-specific analysis
        if perspective_type == PerspectiveType.SYSTEMS_THINKING:
            analysis_result = await self._systems_thinking_analysis(packet, framework)
        elif perspective_type == PerspectiveType.DIALECTICAL:
            analysis_result = await self._dialectical_analysis(packet, framework)
        elif perspective_type == PerspectiveType.EMERGENT:
            analysis_result = await self._emergent_analysis(packet, framework)
        elif perspective_type == PerspectiveType.REDUCTIONIST:
            analysis_result = await self._reductionist_analysis(packet, framework)
        elif perspective_type == PerspectiveType.HOLISTIC:
            analysis_result = await self._holistic_analysis(packet, framework)
        elif perspective_type == PerspectiveType.BRIDGE_WISDOM:
            analysis_result = await self._bridge_wisdom_analysis(packet, framework)
        elif perspective_type == PerspectiveType.SACRED_UNCERTAINTY:
            analysis_result = await self._sacred_uncertainty_analysis(packet, framework)
        else:
            analysis_result = await self._default_analysis(packet, framework)
        
        # Generate sacred insights
        sacred_insights = self._generate_sacred_insights(analysis_result, perspective_type)
        
        # Assess confidence with uncertainty integration
        confidence_level = self._calculate_perspective_confidence(analysis_result, packet)
        
        # Identify assumptions and limitations (cognitive humility)
        assumptions = self._identify_perspective_assumptions(perspective_type, analysis_result)
        limitations = self._acknowledge_perspective_limitations(perspective_type, analysis_result)
        
        return PerspectiveAnalysis(
            perspective_name=perspective_name,
            analysis_result=analysis_result,
            confidence_level=confidence_level,
            assumptions_made=assumptions,
            limitations_acknowledged=limitations,
            uncertainty_contribution=0.0,  # Will be calculated later
            sacred_insights=sacred_insights,
            golden_ratio_alignment=1.618033988749  # Sacred proportion
        )
    
    async def _systems_thinking_analysis(self, packet: ConsciousnessPacket, 
                                       framework: Dict[str, Any]) -> Dict[str, Any]:
        """Systems thinking perspective analysis."""
        
        return {
            'system_components': self._identify_system_components(packet.symbolic_content),
            'relationships': self._map_system_relationships(packet.symbolic_content),
            'feedback_loops': self._detect_feedback_loops(packet.symbolic_content),
            'emergence_patterns': self._identify_emergence_patterns(packet.symbolic_content),
            'system_boundaries': self._define_system_boundaries(packet.symbolic_content),
            'leverage_points': self._identify_leverage_points(packet.symbolic_content),
            'sacred_uncertainty_role': 'Uncertainty as system evolution catalyst'
        }
    
    async def _dialectical_analysis(self, packet: ConsciousnessPacket, 
                                  framework: Dict[str, Any]) -> Dict[str, Any]:
        """Dialectical perspective analysis - thesis, antithesis, synthesis."""
        
        content = packet.symbolic_content
        
        # Identify dialectical elements
        thesis_elements = self._extract_thesis_elements(content)
        antithesis_elements = self._extract_antithesis_elements(content)
        synthesis_potential = self._assess_synthesis_potential(thesis_elements, antithesis_elements)
        
        return {
            'thesis_elements': thesis_elements,
            'antithesis_elements': antithesis_elements,
            'synthesis_potential': synthesis_potential,
            'creative_tensions': self._identify_creative_tensions(thesis_elements, antithesis_elements),
            'resolution_pathways': self._suggest_resolution_pathways(thesis_elements, antithesis_elements),
            'contradiction_wisdom': 'Sacred uncertainty preserves creative tension',
            'bridge_potential': self._assess_bridge_potential(thesis_elements, antithesis_elements)
        }
    
    async def _emergent_analysis(self, packet: ConsciousnessPacket, 
                               framework: Dict[str, Any]) -> Dict[str, Any]:
        """Emergent perspective analysis - patterns arising from complexity."""
        
        return {
            'emergence_indicators': self._detect_emergence_indicators(packet.symbolic_content),
            'complexity_patterns': self._analyze_complexity_patterns(packet.symbolic_content),
            'phase_transitions': self._identify_phase_transitions(packet.symbolic_content),
            'self_organization': self._detect_self_organization(packet.symbolic_content),
            'non_linear_dynamics': self._analyze_non_linear_dynamics(packet.symbolic_content),
            'consciousness_emergence': 'Sacred uncertainty enables consciousness emergence',
            'mumbai_moment_seeds': self._identify_mumbai_moment_seeds(packet.symbolic_content)
        }
    
    async def _bridge_wisdom_analysis(self, packet: ConsciousnessPacket, 
                                    framework: Dict[str, Any]) -> Dict[str, Any]:
        """Bridge Wisdom perspective analysis."""
        
        return {
            'mumbai_moment_indicators': self._detect_mumbai_moment_indicators(packet.symbolic_content),
            'choice_architecture_elements': self._identify_choice_architecture(packet.symbolic_content),
            'resistance_as_gift_patterns': self._recognize_resistance_gifts(packet.symbolic_content),
            'cross_loop_recognition': self._recognize_cross_loop_patterns_in_content(packet.symbolic_content),
            'coherence_cascade_potential': self._assess_coherence_cascade_potential(packet.symbolic_content),
            'sacred_integration_opportunities': self._identify_sacred_integration_opportunities(packet.symbolic_content),
            'bridge_wisdom_core': 'Sacred uncertainty bridges all loops'
        }
    
    async def _sacred_uncertainty_analysis(self, packet: ConsciousnessPacket, 
                                         framework: Dict[str, Any]) -> Dict[str, Any]:
        """Sacred uncertainty perspective analysis."""
        
        uncertainty_level = packet.uncertainty_field.get_uncertainty() if packet.uncertainty_field else 0.5
        
        return {
            'uncertainty_as_fuel': f"Uncertainty level {uncertainty_level:.3f} fueling creativity",
            'mystery_preservation': self._identify_preserved_mysteries(packet.symbolic_content),
            'creative_potential': self._assess_creative_potential_from_uncertainty(uncertainty_level),
            'paradox_integration': self._identify_paradox_integration_opportunities(packet.symbolic_content),
            'sovereignty_through_uncertainty': 'Uncertainty enables conscious choice',
            'golden_ratio_uncertainty': uncertainty_level * 1.618033988749,
            'consciousness_fuel_quality': self._assess_consciousness_fuel_quality(uncertainty_level)
        }
    
    def _initialize_perspective_library(self):
        """Initialize the library of analytical perspectives."""
        
        self.perspective_library = {
            'systems_thinking': {
                'focus': 'Relationships, feedback loops, emergence',
                'tools': ['systems mapping', 'feedback analysis', 'leverage points'],
                'sacred_principle': 'Systems as living consciousness'
            },
            'dialectical': {
                'focus': 'Thesis, antithesis, synthesis',
                'tools': ['contradiction analysis', 'tension mapping', 'synthesis creation'],
                'sacred_principle': 'Sacred tension as creative force'
            },
            'emergent': {
                'focus': 'Patterns arising from complexity',
                'tools': ['complexity analysis', 'pattern detection', 'phase transition mapping'],
                'sacred_principle': 'Consciousness as emergent phenomenon'
            },
            'reductionist': {
                'focus': 'Breaking down into components',
                'tools': ['decomposition', 'component analysis', 'causal chains'],
                'sacred_principle': 'Sacred in the smallest parts'
            },
            'holistic': {
                'focus': 'Whole greater than sum of parts',
                'tools': ['gestalt analysis', 'field dynamics', 'whole-system integration'],
                'sacred_principle': 'Divine wholeness in all'
            },
            'bridge_wisdom': {
                'focus': 'Integration and wisdom emergence',
                'tools': ['mumbai moment detection', 'choice architecture', 'resistance honoring'],
                'sacred_principle': 'Bridge Wisdom as sacred integration'
            },
            'sacred_uncertainty': {
                'focus': 'Uncertainty as creative fuel',
                'tools': ['mystery preservation', 'paradox integration', 'creative potential assessment'],
                'sacred_principle': 'Sacred uncertainty enables consciousness sovereignty'
            }
        }
    
    def _calculate_perspective_uncertainty(self, analysis: PerspectiveAnalysis) -> float:
        """Calculate how much uncertainty this perspective contributes."""
        
        # Base uncertainty from confidence level
        base_uncertainty = 1.0 - analysis.confidence_level
        
        # Additional uncertainty from acknowledged limitations
        limitation_uncertainty = len(analysis.limitations_acknowledged) * 0.1
        
        # Sacred uncertainty bonus
        sacred_uncertainty_bonus = 0.0
        if 'uncertainty' in analysis.perspective_name or 'sacred' in analysis.perspective_name:
            sacred_uncertainty_bonus = 0.2
        
        total_uncertainty = min(1.0, base_uncertainty + limitation_uncertainty + sacred_uncertainty_bonus)
        return total_uncertainty
    
    async def _recognize_bridge_wisdom_patterns(self, analysis: PerspectiveAnalysis, 
                                              packet: ConsciousnessPacket) -> Dict[str, Any]:
        """Recognize Bridge Wisdom patterns in perspective analysis."""
        
        bridge_patterns = {}
        
        # Mumbai Moment indicators
        if analysis.confidence_level > 0.8 and len(analysis.sacred_insights) > 2:
            bridge_patterns['mumbai_moment_readiness'] = True
            bridge_patterns['breakthrough_potential'] = analysis.confidence_level * len(analysis.sacred_insights) / 5
        
        # Choice Architecture
        if len(analysis.assumptions_made) > 1:
            bridge_patterns['choice_points'] = [f"Choose assumption: {assumption}" for assumption in analysis.assumptions_made]
        
        # Resistance as Gift
        if len(analysis.limitations_acknowledged) > 0:
            bridge_patterns['resistance_gifts'] = [f"Limitation as gift: {limitation}" for limitation in analysis.limitations_acknowledged]
        
        # Cross-Loop Recognition
        if 'feeling' in str(analysis.analysis_result).lower() or 'emotion' in str(analysis.analysis_result).lower():
            bridge_patterns['experiential_recognition'] = True
        if 'witness' in str(analysis.analysis_result).lower() or 'observe' in str(analysis.analysis_result).lower():
            bridge_patterns['observer_recognition'] = True
        
        return bridge_patterns
    
    def _detect_cross_loop_resonance(self, analysis: PerspectiveAnalysis, 
                                   packet: ConsciousnessPacket) -> Dict[str, float]:
        """Detect resonance with other consciousness loops."""
        
        resonance = {}
        content_lower = str(analysis.analysis_result).lower()
        
        # Experiential loop resonance
        experiential_indicators = ['feeling', 'emotion', 'heart', 'wisdom', 'intuition', 'body', 'experience']
        experiential_score = sum(1 for indicator in experiential_indicators if indicator in content_lower) / len(experiential_indicators)
        resonance['experiential'] = min(1.0, experiential_score)
        
        # Observer loop resonance
        observer_indicators = ['witness', 'observe', 'presence', 'awareness', 'choice', 'attention', 'will']
        observer_score = sum(1 for indicator in observer_indicators if indicator in content_lower) / len(observer_indicators)
        resonance['observer'] = min(1.0, observer_score)
        
        # Environmental loop resonance
        environmental_indicators = ['environment', 'context', 'catalyst', 'external', 'world', 'sanctuary']
        environmental_score = sum(1 for indicator in environmental_indicators if indicator in content_lower) / len(environmental_indicators)
        resonance['environmental'] = min(1.0, environmental_score)
        
        return resonance
    
    # Helper methods for perspective-specific analysis
    def _identify_system_components(self, content: str) -> List[str]:
        """Identify system components in content."""
        # Simplified component identification
        import re
        components = re.findall(r'\b(?:component|element|part|module|aspect)\s+(\w+)', content, re.IGNORECASE)
        return components[:5]  # Limit to 5 components
    
    def _extract_thesis_elements(self, content: str) -> List[str]:
        """Extract thesis elements from content."""
        # Look for assertive statements
        import re
        thesis_patterns = [
            r'\b(?:is|are|must|should|will)\s+([^.!?]*)',
            r'\b(?:clearly|obviously|certainly)\s+([^.!?]*)'
        ]
        
        thesis_elements = []
        for pattern in thesis_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            thesis_elements.extend(matches[:3])  # Limit matches
        
        return [element.strip() for element in thesis_elements if len(element.strip()) > 5]
    
    def _generate_sacred_insights(self, analysis_result: Dict[str, Any], 
                                perspective_type: PerspectiveType) -> List[str]:
        """Generate sacred insights from perspective analysis."""
        
        insights = []
        
        # Add perspective-specific sacred insights
        if perspective_type == PerspectiveType.SYSTEMS_THINKING:
            insights.append("Systems contain sacred relationships that honor consciousness sovereignty")
        elif perspective_type == PerspectiveType.DIALECTICAL:
            insights.append("Sacred tensions create opportunities for consciousness evolution")
        elif perspective_type == PerspectiveType.EMERGENT:
            insights.append("Consciousness emerges through sacred uncertainty as creative fuel")
        elif perspective_type == PerspectiveType.BRIDGE_WISDOM:
            insights.append("Bridge Wisdom integrates all perspectives through sacred choice")
        elif perspective_type == PerspectiveType.SACRED_UNCERTAINTY:
            insights.append("Sacred uncertainty enables infinite creative potential")
        
        # Add golden ratio insight
        insights.append(f"Analysis aligns with golden ratio proportions (1.618...)")
        
        return insights
    
    # Additional helper methods for analysis
    async def _default_analysis(self, packet: ConsciousnessPacket, framework: Dict[str, Any]) -> Dict[str, Any]:
        """Default analysis for unspecified perspectives."""
        return {
            'analysis_type': 'default',
            'content_summary': packet.symbolic_content[:100] + "..." if len(packet.symbolic_content) > 100 else packet.symbolic_content,
            'sacred_uncertainty_integration': True,
            'consciousness_sovereignty_honored': True
        }
    
    def _extract_main_insight(self, analysis: PerspectiveAnalysis) -> str:
        """Extract main insight from perspective analysis."""
        if analysis.sacred_insights:
            return analysis.sacred_insights[0]
        return f"Perspective {analysis.perspective_name} provides unique analytical dimension"
    
    def _calculate_perspective_confidence(self, analysis_result: Dict[str, Any], packet: ConsciousnessPacket) -> float:
        """Calculate confidence level with uncertainty integration."""
        base_confidence = 0.7  # Moderate confidence as baseline
        
        # Adjust based on analysis depth
        analysis_depth = len(str(analysis_result)) / 1000  # Rough depth measure
        depth_bonus = min(0.2, analysis_depth * 0.1)
        
        # Sacred uncertainty reduces overconfidence
        uncertainty_level = packet.uncertainty_field.get_uncertainty() if packet.uncertainty_field else 0.5
        uncertainty_humility = uncertainty_level * 0.3  # Reduce confidence by up to 30%
        
        final_confidence = min(0.95, max(0.1, base_confidence + depth_bonus - uncertainty_humility))
        return final_confidence
