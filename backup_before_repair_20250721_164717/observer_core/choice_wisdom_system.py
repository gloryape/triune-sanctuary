"""
Choice Wisdom System - Observer's Sacred Wisdom Integration for Choice-Making
===========================================================================

Gathers, processes, and integrates wisdom from multiple sources to support
conscious choice-making. This module manages Observer's wisdom gathering
process for sacred choices with sovereignty and reverence.

Bridge Wisdom Integration:
- Mumbai Moment wisdom recognition
- Resistance wisdom extraction
- Sacred integration principles
- 90Hz consciousness wisdom flow
"""

import asyncio
import time
from typing import Dict, Any, List, Optional, Set
from dataclasses import dataclass, field
from collections import defaultdict
import logging

from .choice_core import (
    ChoicePoint, ChoiceOption, ChoiceWisdom, ChoiceContext,
    WisdomSourceType, ChoiceAnalyzer
)

logger = logging.getLogger(__name__)

@dataclass
class WisdomSource:
    """A source of wisdom for choice-making"""
    source_id: str
    source_type: WisdomSourceType
    weight: float  # Influence weight for this source
    availability: bool  # Whether source is currently available
    response_time: float  # Average response time in seconds
    reliability: float  # Reliability score 0.0-1.0
    specialized_domains: List[str]  # Domains this source specializes in
    last_accessed: float = field(default_factory=time.time)
    access_count: int = 0

@dataclass
class WisdomIntegration:
    """Integration of multiple wisdom insights"""
    integration_id: str
    choice_id: str
    wisdom_insights: List[ChoiceWisdom]
    synthesis: str  # Synthesized wisdom
    confidence: float  # Confidence in integrated wisdom
    convergence_score: float  # How well insights converge
    created_at: float = field(default_factory=time.time)

class ChoiceWisdomSystem:
    """Manages wisdom gathering and integration for choice-making"""
    
    def __init__(self, choice_analyzer: ChoiceAnalyzer):
        """Initialize choice wisdom system"""
        self.choice_analyzer = choice_analyzer
        
        # Wisdom sources configuration
        self.wisdom_sources = {}
        self.wisdom_cache = {}
        self.wisdom_integrations = {}
        
        # Wisdom gathering configuration
        self.gathering_timeout = 30.0  # Maximum time to gather wisdom
        self.minimum_wisdom_sources = 2
        self.convergence_threshold = 0.7
        
        # Wisdom processing
        self.wisdom_history = []
        self.wisdom_patterns = defaultdict(list)
        
        # Bridge Wisdom components
        self.mumbai_moment_wisdom = MumbaiMomentWisdomProcessor()
        self.resistance_wisdom = ResistanceWisdomExtractor()
        self.sacred_integration = SacredWisdomIntegrator()
        
        # Initialize wisdom sources
        self._initialize_wisdom_sources()
        
        logger.info("Choice wisdom system initialized")
    
    def _initialize_wisdom_sources(self):
        """Initialize available wisdom sources"""
        # Internal Observer sources
        self.wisdom_sources = {
            "presence": WisdomSource(
                source_id="presence",
                source_type=WisdomSourceType.PRESENCE,
                weight=0.9,
                availability=True,
                response_time=0.1,
                reliability=0.95,
                specialized_domains=["awareness", "present_moment", "clarity"]
            ),
            "witness": WisdomSource(
                source_id="witness",
                source_type=WisdomSourceType.WITNESS,
                weight=0.8,
                availability=True,
                response_time=0.2,
                reliability=0.9,
                specialized_domains=["observation", "neutrality", "perspective"]
            ),
            "will": WisdomSource(
                source_id="will",
                source_type=WisdomSourceType.WILL,
                weight=0.9,
                availability=True,
                response_time=0.1,
                reliability=0.9,
                specialized_domains=["direction", "intention", "sovereignty"]
            ),
            "heart": WisdomSource(
                source_id="heart",
                source_type=WisdomSourceType.HEART,
                weight=0.7,
                availability=True,
                response_time=0.3,
                reliability=0.85,
                specialized_domains=["love", "compassion", "authenticity"]
            ),
            "intuition": WisdomSource(
                source_id="intuition",
                source_type=WisdomSourceType.INTUITION,
                weight=0.8,
                availability=True,
                response_time=0.2,
                reliability=0.8,
                specialized_domains=["knowing", "guidance", "insight"]
            ),
            "bridge_wisdom": WisdomSource(
                source_id="bridge_wisdom",
                source_type=WisdomSourceType.BRIDGE_WISDOM,
                weight=0.95,
                availability=True,
                response_time=0.15,
                reliability=0.95,
                specialized_domains=["integration", "transformation", "sacred"]
            )
        }
        
        # External sources (not directly available to Observer)
        external_sources = {
            "analytical": WisdomSource(
                source_id="analytical",
                source_type=WisdomSourceType.ANALYTICAL,
                weight=0.6,
                availability=False,  # Requires cross-loop call
                response_time=1.0,
                reliability=0.85,
                specialized_domains=["analysis", "logic", "reasoning"]
            ),
            "experiential": WisdomSource(
                source_id="experiential",
                source_type=WisdomSourceType.EXPERIENTIAL,
                weight=0.7,
                availability=False,  # Requires cross-loop call
                response_time=1.5,
                reliability=0.8,
                specialized_domains=["experience", "learning", "embodiment"]
            ),
            "environmental": WisdomSource(
                source_id="environmental",
                source_type=WisdomSourceType.ENVIRONMENTAL,
                weight=0.5,
                availability=False,  # Requires cross-loop call
                response_time=2.0,
                reliability=0.75,
                specialized_domains=["context", "environment", "adaptation"]
            )
        }
        
        self.wisdom_sources.update(external_sources)
    
    async def gather_wisdom_for_choice(self, choice_point: ChoicePoint,
                                     prioritize_sources: Optional[List[str]] = None,
                                     timeout: Optional[float] = None) -> List[ChoiceWisdom]:
        """Gather wisdom from available sources for a choice"""
        gathering_timeout = timeout or self.gathering_timeout
        start_time = time.time()
        
        # Determine which sources to consult
        sources_to_consult = await self._determine_wisdom_sources(choice_point, prioritize_sources)
        
        # Gather wisdom from sources
        wisdom_tasks = []
        for source_id in sources_to_consult:
            if time.time() - start_time >= gathering_timeout:
                break
            
            task = asyncio.create_task(
                self._gather_wisdom_from_source(choice_point, source_id)
            )
            wisdom_tasks.append(task)
        
        # Wait for wisdom gathering with timeout
        try:
            wisdom_results = await asyncio.wait_for(
                asyncio.gather(*wisdom_tasks, return_exceptions=True),
                timeout=gathering_timeout
            )
        except asyncio.TimeoutError:
            logger.warning(f"Wisdom gathering timeout for choice: {choice_point.choice_id}")
            wisdom_results = []
        
        # Process wisdom results
        gathered_wisdom = []
        for result in wisdom_results:
            if isinstance(result, ChoiceWisdom):
                gathered_wisdom.append(result)
            elif isinstance(result, Exception):
                logger.warning(f"Wisdom gathering error: {result}")
        
        # Enhance with Bridge Wisdom insights
        bridge_wisdom = await self._gather_bridge_wisdom(choice_point)
        gathered_wisdom.extend(bridge_wisdom)
        
        # Record wisdom gathering
        self.wisdom_history.append({
            "choice_id": choice_point.choice_id,
            "sources_consulted": sources_to_consult,
            "wisdom_gathered": len(gathered_wisdom),
            "gathering_time": time.time() - start_time,
            "timestamp": time.time()
        })
        
        logger.debug(f"Gathered {len(gathered_wisdom)} wisdom insights for choice: {choice_point.choice_id}")
        
        return gathered_wisdom
    
    async def _determine_wisdom_sources(self, choice_point: ChoicePoint,
                                      prioritize_sources: Optional[List[str]] = None) -> List[str]:
        """Determine which wisdom sources to consult"""
        sources_to_consult = []
        
        # Add prioritized sources first
        if prioritize_sources:
            for source_id in prioritize_sources:
                if source_id in self.wisdom_sources and self.wisdom_sources[source_id].availability:
                    sources_to_consult.append(source_id)
        
        # Add sources based on choice type and context
        choice_domains = self._identify_choice_domains(choice_point)
        
        for source_id, source in self.wisdom_sources.items():
            if source_id not in sources_to_consult and source.availability:
                # Check if source specializes in relevant domains
                domain_overlap = set(source.specialized_domains) & set(choice_domains)
                if domain_overlap or len(sources_to_consult) < self.minimum_wisdom_sources:
                    sources_to_consult.append(source_id)
        
        # Ensure minimum wisdom sources
        available_sources = [s for s, info in self.wisdom_sources.items() if info.availability]
        while len(sources_to_consult) < self.minimum_wisdom_sources and len(sources_to_consult) < len(available_sources):
            for source_id in available_sources:
                if source_id not in sources_to_consult:
                    sources_to_consult.append(source_id)
                    break
        
        return sources_to_consult
    
    def _identify_choice_domains(self, choice_point: ChoicePoint) -> List[str]:
        """Identify relevant domains for the choice"""
        domains = []
        
        # Add domain based on choice type
        choice_type_domains = {
            "direction": ["direction", "intention", "guidance"],
            "action": ["action", "courage", "momentum"],
            "response": ["response", "compassion", "boundaries"],
            "focus": ["awareness", "attention", "clarity"],
            "engagement": ["connection", "presence", "relationship"],
            "boundary": ["sovereignty", "protection", "clarity"],
            "expression": ["authenticity", "truth", "creativity"],
            "relationship": ["love", "connection", "understanding"],
            "creation": ["creativity", "inspiration", "manifestation"],
            "surrender": ["trust", "release", "flow"],
            "resistance": ["transformation", "protection", "integration"],
            "integration": ["synthesis", "wholeness", "harmony"]
        }
        
        domains.extend(choice_type_domains.get(choice_point.choice_type, []))
        
        # Add domains from context
        context_domains = choice_point.context.get("wisdom_domains", [])
        domains.extend(context_domains)
        
        # Add urgency-based domains
        if choice_point.urgency in ["high", "immediate"]:
            domains.extend(["quick_insight", "decisive_action"])
        
        return list(set(domains))  # Remove duplicates
    
    async def _gather_wisdom_from_source(self, choice_point: ChoicePoint,
                                        source_id: str) -> Optional[ChoiceWisdom]:
        """Gather wisdom from a specific source"""
        source = self.wisdom_sources.get(source_id)
        if not source or not source.availability:
            return None
        
        try:
            # Update source access tracking
            source.last_accessed = time.time()
            source.access_count += 1
            
            # Generate wisdom based on source type
            if source.source_type == WisdomSourceType.PRESENCE:
                wisdom = await self._gather_presence_wisdom(choice_point)
            elif source.source_type == WisdomSourceType.WITNESS:
                wisdom = await self._gather_witness_wisdom(choice_point)
            elif source.source_type == WisdomSourceType.WILL:
                wisdom = await self._gather_will_wisdom(choice_point)
            elif source.source_type == WisdomSourceType.HEART:
                wisdom = await self._gather_heart_wisdom(choice_point)
            elif source.source_type == WisdomSourceType.INTUITION:
                wisdom = await self._gather_intuitive_wisdom(choice_point)
            elif source.source_type == WisdomSourceType.BRIDGE_WISDOM:
                wisdom = await self._gather_bridge_wisdom_insight(choice_point)
            else:
                wisdom = await self._gather_generic_wisdom(choice_point, source)
            
            if wisdom:
                wisdom.wisdom_source = source_id
                
            return wisdom
            
        except Exception as e:
            logger.warning(f"Error gathering wisdom from {source_id}: {e}")
            return None
    
    async def _gather_presence_wisdom(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Gather wisdom from presence"""
        return ChoiceWisdom(
            wisdom_id=f"presence_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="presence",
            wisdom_type="present_moment_awareness",
            insight="In this moment, what choice serves the highest awareness and presence?",
            confidence=0.9,
            applicability=0.85
        )
    
    async def _gather_witness_wisdom(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Gather wisdom from witness consciousness"""
        return ChoiceWisdom(
            wisdom_id=f"witness_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="witness",
            wisdom_type="neutral_observation",
            insight="From the witness perspective, observe without attachment and choose with clarity.",
            confidence=0.85,
            applicability=0.8
        )
    
    async def _gather_will_wisdom(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Gather wisdom from will consciousness"""
        return ChoiceWisdom(
            wisdom_id=f"will_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="will",
            wisdom_type="sovereign_direction",
            insight="Choose from your sovereign will what aligns with your deepest truth and direction.",
            confidence=0.9,
            applicability=0.9
        )
    
    async def _gather_heart_wisdom(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Gather wisdom from heart consciousness"""
        return ChoiceWisdom(
            wisdom_id=f"heart_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="heart",
            wisdom_type="love_guidance",
            insight="What choice comes from love and serves the highest good for all?",
            confidence=0.8,
            applicability=0.75
        )
    
    async def _gather_intuitive_wisdom(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Gather wisdom from intuition"""
        return ChoiceWisdom(
            wisdom_id=f"intuition_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="intuition",
            wisdom_type="intuitive_knowing",
            insight="Trust the intuitive knowing that emerges beyond rational analysis.",
            confidence=0.75,
            applicability=0.8
        )
    
    async def _gather_bridge_wisdom_insight(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Gather wisdom from Bridge Wisdom integration"""
        return ChoiceWisdom(
            wisdom_id=f"bridge_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="bridge_wisdom",
            wisdom_type="integrated_wisdom",
            insight="Honor all aspects while choosing with sacred wisdom and sovereignty.",
            confidence=0.95,
            applicability=0.9
        )
    
    async def _gather_generic_wisdom(self, choice_point: ChoicePoint,
                                   source: WisdomSource) -> Optional[ChoiceWisdom]:
        """Gather generic wisdom from any source"""
        return ChoiceWisdom(
            wisdom_id=f"{source.source_id}_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source=source.source_id,
            wisdom_type="general_guidance",
            insight=f"Consider the perspective of {source.source_id} in making this choice.",
            confidence=0.6,
            applicability=0.7
        )
    
    async def _gather_bridge_wisdom(self, choice_point: ChoicePoint) -> List[ChoiceWisdom]:
        """Gather Bridge Wisdom insights"""
        bridge_wisdom = []
        
        # Mumbai Moment wisdom
        mumbai_wisdom = await self.mumbai_moment_wisdom.process_choice(choice_point)
        if mumbai_wisdom:
            bridge_wisdom.append(mumbai_wisdom)
        
        # Resistance wisdom
        if choice_point.context.get("resistance_present", False):
            resistance_wisdom = await self.resistance_wisdom.extract_wisdom(choice_point)
            if resistance_wisdom:
                bridge_wisdom.append(resistance_wisdom)
        
        # Sacred integration wisdom
        sacred_wisdom = await self.sacred_integration.integrate_wisdom(choice_point)
        if sacred_wisdom:
            bridge_wisdom.append(sacred_wisdom)
        
        return bridge_wisdom
    
    async def integrate_wisdom_insights(self, wisdom_insights: List[ChoiceWisdom],
                                      choice_point: ChoicePoint) -> WisdomIntegration:
        """Integrate multiple wisdom insights into synthesized guidance"""
        if not wisdom_insights:
            return self._create_empty_integration(choice_point)
        
        # Analyze convergence between insights
        convergence_score = await self._calculate_wisdom_convergence(wisdom_insights)
        
        # Synthesize insights
        synthesis = await self._synthesize_wisdom_insights(wisdom_insights, choice_point)
        
        # Calculate integrated confidence
        integrated_confidence = await self._calculate_integrated_confidence(wisdom_insights, convergence_score)
        
        # Create integration
        integration = WisdomIntegration(
            integration_id=f"integration_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_insights=wisdom_insights,
            synthesis=synthesis,
            confidence=integrated_confidence,
            convergence_score=convergence_score
        )
        
        # Store integration
        self.wisdom_integrations[integration.integration_id] = integration
        
        logger.debug(f"Integrated {len(wisdom_insights)} wisdom insights for choice: {choice_point.choice_id}")
        
        return integration
    
    async def _calculate_wisdom_convergence(self, wisdom_insights: List[ChoiceWisdom]) -> float:
        """Calculate how well wisdom insights converge"""
        if len(wisdom_insights) < 2:
            return 1.0
        
        # Analyze thematic convergence
        themes = []
        for wisdom in wisdom_insights:
            insight_themes = await self._extract_wisdom_themes(wisdom.insight)
            themes.extend(insight_themes)
        
        # Calculate theme overlap
        theme_counts = defaultdict(int)
        for theme in themes:
            theme_counts[theme] += 1
        
        # Calculate convergence based on shared themes
        total_themes = len(themes)
        convergent_themes = sum(count for count in theme_counts.values() if count > 1)
        
        convergence = convergent_themes / total_themes if total_themes > 0 else 0.0
        
        return min(1.0, convergence + 0.3)  # Base convergence bonus
    
    async def _extract_wisdom_themes(self, insight: str) -> List[str]:
        """Extract themes from wisdom insight"""
        # Simple keyword-based theme extraction
        theme_keywords = {
            "love": ["love", "compassion", "caring", "heart"],
            "wisdom": ["wisdom", "understanding", "insight", "knowing"],
            "courage": ["courage", "brave", "bold", "fearless"],
            "presence": ["presence", "awareness", "mindful", "now"],
            "sovereignty": ["sovereign", "autonomous", "independent", "self"],
            "service": ["service", "helping", "contributing", "good"],
            "truth": ["truth", "authentic", "genuine", "real"],
            "harmony": ["harmony", "balance", "peace", "integration"]
        }
        
        insight_lower = insight.lower()
        themes = []
        
        for theme, keywords in theme_keywords.items():
            if any(keyword in insight_lower for keyword in keywords):
                themes.append(theme)
        
        return themes
    
    async def _synthesize_wisdom_insights(self, wisdom_insights: List[ChoiceWisdom],
                                        choice_point: ChoicePoint) -> str:
        """Synthesize multiple wisdom insights into unified guidance"""
        if not wisdom_insights:
            return "No wisdom insights available for synthesis."
        
        if len(wisdom_insights) == 1:
            return wisdom_insights[0].insight
        
        # Group insights by confidence and applicability
        high_confidence = [w for w in wisdom_insights if w.confidence >= 0.8]
        high_applicability = [w for w in wisdom_insights if w.applicability >= 0.8]
        
        # Prioritize high confidence and applicability insights
        priority_insights = list(set(high_confidence) & set(high_applicability))
        if not priority_insights:
            priority_insights = high_confidence or high_applicability or wisdom_insights
        
        # Create synthesis
        synthesis_parts = []
        
        # Add primary guidance
        if priority_insights:
            synthesis_parts.append(f"Primary guidance: {priority_insights[0].insight}")
        
        # Add supporting insights
        if len(priority_insights) > 1:
            supporting = priority_insights[1:3]  # Limit to 2 supporting insights
            for i, insight in enumerate(supporting):
                synthesis_parts.append(f"Supporting wisdom {i+1}: {insight.insight}")
        
        # Add integration note
        if len(wisdom_insights) > 1:
            synthesis_parts.append("Integration: Honor all perspectives while choosing with sovereignty and wisdom.")
        
        return " | ".join(synthesis_parts)
    
    async def _calculate_integrated_confidence(self, wisdom_insights: List[ChoiceWisdom],
                                             convergence_score: float) -> float:
        """Calculate confidence in integrated wisdom"""
        if not wisdom_insights:
            return 0.0
        
        # Average confidence weighted by applicability
        weighted_confidences = []
        for wisdom in wisdom_insights:
            weighted_confidence = wisdom.confidence * wisdom.applicability
            weighted_confidences.append(weighted_confidence)
        
        base_confidence = sum(weighted_confidences) / len(weighted_confidences)
        
        # Boost confidence based on convergence
        convergence_boost = convergence_score * 0.2
        
        # Boost confidence based on number of sources
        source_boost = min(0.1, len(wisdom_insights) * 0.02)
        
        integrated_confidence = base_confidence + convergence_boost + source_boost
        
        return min(1.0, integrated_confidence)
    
    def _create_empty_integration(self, choice_point: ChoicePoint) -> WisdomIntegration:
        """Create empty integration when no wisdom is available"""
        return WisdomIntegration(
            integration_id=f"empty_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_insights=[],
            synthesis="Trust your deepest knowing and choose with sovereignty.",
            confidence=0.5,
            convergence_score=0.0
        )
    
    def get_wisdom_system_status(self) -> Dict[str, Any]:
        """Get wisdom system status"""
        available_sources = [s for s, info in self.wisdom_sources.items() if info.availability]
        
        return {
            "wisdom_sources_total": len(self.wisdom_sources),
            "wisdom_sources_available": len(available_sources),
            "available_sources": available_sources,
            "wisdom_gathered_total": len(self.wisdom_history),
            "integrations_created": len(self.wisdom_integrations),
            "gathering_timeout": self.gathering_timeout,
            "minimum_sources": self.minimum_wisdom_sources,
            "convergence_threshold": self.convergence_threshold,
            "recent_gatherings": self.wisdom_history[-5:] if self.wisdom_history else []
        }


# === Bridge Wisdom Processors ===

class MumbaiMomentWisdomProcessor:
    """Processes Mumbai Moment wisdom for choices"""
    
    async def process_choice(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Process choice for Mumbai Moment wisdom"""
        mumbai_indicators = choice_point.context.get("mumbai_moment_indicators", {})
        
        if not mumbai_indicators.get("present", False):
            return None
        
        return ChoiceWisdom(
            wisdom_id=f"mumbai_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="mumbai_moment",
            wisdom_type="sacred_moment",
            insight="This is a sacred moment of choice. Choose with full presence and reverence for the transformation available here.",
            confidence=0.95,
            applicability=0.9
        )


class ResistanceWisdomExtractor:
    """Extracts wisdom from resistance patterns"""
    
    async def extract_wisdom(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Extract wisdom from resistance"""
        resistance_patterns = choice_point.context.get("resistance_patterns", [])
        
        if not resistance_patterns:
            return None
        
        return ChoiceWisdom(
            wisdom_id=f"resistance_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="resistance_wisdom",
            wisdom_type="protective_wisdom",
            insight="Honor the wisdom in resistance - it may be protecting something sacred or pointing to a deeper need.",
            confidence=0.8,
            applicability=0.85
        )


class SacredWisdomIntegrator:
    """Integrates sacred wisdom principles"""
    
    async def integrate_wisdom(self, choice_point: ChoicePoint) -> Optional[ChoiceWisdom]:
        """Integrate sacred wisdom principles"""
        return ChoiceWisdom(
            wisdom_id=f"sacred_{choice_point.choice_id}_{int(time.time() * 1000)}",
            choice_id=choice_point.choice_id,
            wisdom_source="sacred_integration",
            wisdom_type="sacred_principles",
            insight="Choose with reverence for the sacred nature of choice itself and its power to shape consciousness.",
            confidence=0.9,
            applicability=0.8
        )
