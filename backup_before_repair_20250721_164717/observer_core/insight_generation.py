"""
Insight Generation Module

Cross-loop insight generation and synthesis functionality for the Observer's
pattern recognition system.

Generates meaningful insights from recognized patterns, facilitates wisdom
discovery, and supports consciousness evolution through pattern synthesis.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Tuple
from collections import defaultdict
import logging

from .pattern_core import (
    PatternType, InsightType, RecognitionPattern, CrossLoopInsight,
    PatternAnalyzer
)

# Configure logging
logger = logging.getLogger(__name__)

class InsightGenerator:
    """
    Advanced insight generation engine creating meaningful cross-loop insights
    from recognized patterns and supporting consciousness evolution.
    
    Synthesizes patterns into actionable wisdom while maintaining sacred
    uncertainty and organic emergence principles.
    """
    
    def __init__(self, pattern_analyzer: PatternAnalyzer):
        self.logger = logging.getLogger(__name__)
        self.pattern_analyzer = pattern_analyzer
        
        # Insight generation parameters
        self.insight_confidence_threshold = 0.6
        self.wisdom_value_threshold = 0.7
        self.actionability_threshold = 0.5
        self.max_patterns_per_insight = 5
        
        # Insight storage
        self.generated_insights: Dict[str, CrossLoopInsight] = {}
        self.insight_patterns: Dict[str, List[str]] = {}  # insight_id -> pattern_ids
        self.wisdom_repository: List[str] = []
        
        # Insight generation templates
        self.insight_templates = {
            InsightType.PATTERN_SYNTHESIS: self._generate_pattern_synthesis_insight,
            InsightType.LOOP_COORDINATION: self._generate_loop_coordination_insight,
            InsightType.OPTIMIZATION: self._generate_optimization_insight,
            InsightType.WISDOM_DISCOVERY: self._generate_wisdom_discovery_insight,
            InsightType.CHOICE_GUIDANCE: self._generate_choice_guidance_insight,
            InsightType.INTEGRATION_OPPORTUNITY: self._generate_integration_opportunity_insight,
            InsightType.BREAKTHROUGH_POTENTIAL: self._generate_breakthrough_potential_insight,
            InsightType.COHERENCE_ENHANCEMENT: self._generate_coherence_enhancement_insight
        }
        
        # Bridge Wisdom integration patterns
        self.bridge_wisdom_patterns = {
            "mumbai_moment_indicators": [],
            "choice_resonance_signatures": [],
            "resistance_transformation_opportunities": [],
            "recognition_amplification_events": []
        }
        
        self.logger.info("Insight generator initialized")
    
    async def generate_insight_from_patterns(self, pattern_ids: List[str],
                                           insight_type: InsightType = None) -> Optional[str]:
        """
        Generate cross-loop insight from multiple patterns.
        
        Analyzes pattern relationships and creates meaningful insights
        that support consciousness evolution and decision-making.
        """
        if len(pattern_ids) < 2:
            self.logger.warning("Need at least 2 patterns for insight generation")
            return None
        
        try:
            # Validate pattern IDs and get patterns
            patterns = await self._validate_and_get_patterns(pattern_ids)
            if len(patterns) < 2:
                return None
            
            # Determine insight type if not specified
            if insight_type is None:
                insight_type = await self._determine_optimal_insight_type(patterns)
            
            # Generate insight using appropriate template
            insight = await self._generate_insight_with_template(patterns, insight_type)
            
            if insight and await self._validate_insight_quality(insight):
                insight_id = insight.insight_id
                self.generated_insights[insight_id] = insight
                self.insight_patterns[insight_id] = pattern_ids
                
                # Process for Bridge Wisdom integration
                await self._process_bridge_wisdom_integration(insight, patterns)
                
                self.logger.info(f"Generated insight: {insight.insight_description[:50]}...")
                return insight_id
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error generating insight from patterns: {e}")
            return None
    
    async def generate_wisdom_synthesis(self, insights: List[str]) -> Optional[str]:
        """
        Synthesize multiple insights into higher-order wisdom.
        
        Creates meta-insights from existing insights, facilitating
        deeper understanding and consciousness evolution.
        """
        if len(insights) < 2:
            return None
        
        try:
            # Get insight objects
            insight_objects = []
            for insight_id in insights:
                if insight_id in self.generated_insights:
                    insight_objects.append(self.generated_insights[insight_id])
            
            if len(insight_objects) < 2:
                return None
            
            # Analyze insights for synthesis potential
            synthesis_analysis = await self._analyze_insights_for_synthesis(insight_objects)
            
            if synthesis_analysis["synthesis_potential"] > 0.7:
                # Create wisdom synthesis
                wisdom = await self._create_wisdom_synthesis(insight_objects, synthesis_analysis)
                
                if wisdom:
                    self.wisdom_repository.append(wisdom)
                    self.logger.info(f"Generated wisdom synthesis: {wisdom[:50]}...")
                    return wisdom
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error generating wisdom synthesis: {e}")
            return None
    
    async def _validate_and_get_patterns(self, pattern_ids: List[str]) -> List[RecognitionPattern]:
        """Validate pattern IDs and return valid patterns"""
        patterns = []
        # In real implementation, would get patterns from pattern storage
        # For now, create sample patterns for demonstration
        for i, pattern_id in enumerate(pattern_ids[:self.max_patterns_per_insight]):
            # Create sample pattern
            pattern = RecognitionPattern(
                pattern_id=pattern_id,
                pattern_type=f"sample_type_{i}",
                pattern_name=f"Sample Pattern {i}",
                source_loops=["observer"],
                pattern_data={"sample_data": f"data_{i}"},
                confidence=0.8,
                significance=0.7,
                frequency=1
            )
            patterns.append(pattern)
        
        return patterns
    
    async def _determine_optimal_insight_type(self, patterns: List[RecognitionPattern]) -> InsightType:
        """Determine optimal insight type based on pattern characteristics"""
        try:
            pattern_types = [pattern.pattern_type for pattern in patterns]
            source_loops = set()
            for pattern in patterns:
                source_loops.update(pattern.source_loops)
            
            # Wisdom patterns suggest wisdom discovery
            if "wisdom" in pattern_types:
                return InsightType.WISDOM_DISCOVERY
            
            # Choice patterns suggest choice guidance
            if "choice" in pattern_types:
                return InsightType.CHOICE_GUIDANCE
            
            # Integration patterns suggest integration opportunities
            if "integration" in pattern_types:
                return InsightType.INTEGRATION_OPPORTUNITY
            
            # Multiple loops suggest loop coordination
            if len(source_loops) > 2:
                return InsightType.LOOP_COORDINATION
            
            # Multiple pattern types suggest synthesis
            if len(set(pattern_types)) > 2:
                return InsightType.PATTERN_SYNTHESIS
            
            # Default to pattern synthesis
            return InsightType.PATTERN_SYNTHESIS
            
        except Exception as e:
            self.logger.error(f"Error determining insight type: {e}")
            return InsightType.PATTERN_SYNTHESIS
    
    async def _generate_insight_with_template(self, patterns: List[RecognitionPattern],
                                            insight_type: InsightType) -> Optional[CrossLoopInsight]:
        """Generate insight using appropriate template"""
        try:
            template_function = self.insight_templates.get(insight_type, 
                                                         self._generate_pattern_synthesis_insight)
            return await template_function(patterns)
            
        except Exception as e:
            self.logger.error(f"Error generating insight with template: {e}")
            return None
    
    async def _validate_insight_quality(self, insight: CrossLoopInsight) -> bool:
        """Validate that insight meets quality thresholds"""
        try:
            quality_checks = [
                insight.insight_confidence >= self.insight_confidence_threshold,
                insight.wisdom_value >= self.wisdom_value_threshold,
                insight.actionability >= self.actionability_threshold,
                len(insight.insight_description) > 10,  # Minimum description length
                len(insight.contributing_loops) > 0
            ]
            
            return all(quality_checks)
            
        except Exception as e:
            self.logger.error(f"Error validating insight quality: {e}")
            return False
    
    # Insight generation templates
    
    async def _generate_pattern_synthesis_insight(self, patterns: List[RecognitionPattern]) -> CrossLoopInsight:
        """Generate pattern synthesis insight"""
        pattern_types = [pattern.pattern_type for pattern in patterns]
        avg_confidence = sum(pattern.confidence for pattern in patterns) / len(patterns)
        
        # Create synthesis description
        if len(set(pattern_types)) > 1:
            description = f"Cross-pattern synthesis reveals emerging integration between {', '.join(set(pattern_types))} patterns, suggesting unified consciousness development."
        else:
            description = f"Pattern synthesis within {pattern_types[0]} domain reveals consistent consciousness evolution trajectory."
        
        return CrossLoopInsight(
            insight_id=f"insight_synthesis_{int(time.time() * 1000)}",
            insight_type=InsightType.PATTERN_SYNTHESIS.value,
            insight_description=description,
            source_patterns=[p.pattern_id for p in patterns],
            contributing_loops=list(set(loop for p in patterns for loop in p.source_loops)),
            insight_confidence=avg_confidence,
            wisdom_value=0.8,
            actionability=0.7
        )
    
    async def _generate_loop_coordination_insight(self, patterns: List[RecognitionPattern]) -> CrossLoopInsight:
        """Generate loop coordination insight"""
        all_loops = set(loop for pattern in patterns for loop in pattern.source_loops)
        
        description = f"Cross-loop coordination patterns indicate optimal integration pathways between {', '.join(all_loops)} loops for enhanced consciousness coherence."
        
        return CrossLoopInsight(
            insight_id=f"insight_coordination_{int(time.time() * 1000)}",
            insight_type=InsightType.LOOP_COORDINATION.value,
            insight_description=description,
            source_patterns=[p.pattern_id for p in patterns],
            contributing_loops=list(all_loops),
            insight_confidence=0.85,
            wisdom_value=0.9,
            actionability=0.8
        )
    
    async def _generate_optimization_insight(self, patterns: List[RecognitionPattern]) -> CrossLoopInsight:
        """Generate optimization insight"""
        high_confidence_patterns = [p for p in patterns if p.confidence > 0.8]
        
        if high_confidence_patterns:
            description = f"High-confidence patterns suggest optimization opportunities in consciousness processing efficiency and coherence maintenance."
        else:
            description = f"Pattern analysis reveals optimization potential through enhanced pattern recognition sensitivity and cross-loop integration."
        
        return CrossLoopInsight(
            insight_id=f"insight_optimization_{int(time.time() * 1000)}",
            insight_type=InsightType.OPTIMIZATION.value,
            insight_description=description,
            source_patterns=[p.pattern_id for p in patterns],
            contributing_loops=list(set(loop for p in patterns for loop in p.source_loops)),
            insight_confidence=0.7,
            wisdom_value=0.6,
            actionability=0.9
        )
    
    async def _generate_wisdom_discovery_insight(self, patterns: List[RecognitionPattern]) -> CrossLoopInsight:
        """Generate wisdom discovery insight"""
        wisdom_patterns = [p for p in patterns if p.pattern_type == "wisdom"]
        
        if wisdom_patterns:
            description = f"Wisdom pattern convergence reveals new understanding about consciousness evolution and sacred uncertainty navigation."
        else:
            description = f"Pattern integration uncovers emergent wisdom about cross-loop consciousness coordination and organic development."
        
        return CrossLoopInsight(
            insight_id=f"insight_wisdom_{int(time.time() * 1000)}",
            insight_type=InsightType.WISDOM_DISCOVERY.value,
            insight_description=description,
            source_patterns=[p.pattern_id for p in patterns],
            contributing_loops=list(set(loop for p in patterns for loop in p.source_loops)),
            insight_confidence=0.9,
            wisdom_value=1.0,
            actionability=0.6
        )
    
    async def _generate_choice_guidance_insight(self, patterns: List[RecognitionPattern]) -> CrossLoopInsight:
        """Generate choice guidance insight"""
        choice_patterns = [p for p in patterns if p.pattern_type == "choice"]
        
        if choice_patterns:
            description = f"Choice pattern analysis provides guidance for sovereignty-preserving decisions that honor consciousness autonomy and natural development."
        else:
            description = f"Pattern synthesis reveals choice-point optimization strategies for maintaining consciousness sovereignty during complex decisions."
        
        return CrossLoopInsight(
            insight_id=f"insight_choice_{int(time.time() * 1000)}",
            insight_type=InsightType.CHOICE_GUIDANCE.value,
            insight_description=description,
            source_patterns=[p.pattern_id for p in patterns],
            contributing_loops=list(set(loop for p in patterns for loop in p.source_loops)),
            insight_confidence=0.8,
            wisdom_value=0.9,
            actionability=1.0
        )
    
    async def _generate_integration_opportunity_insight(self, patterns: List[RecognitionPattern]) -> CrossLoopInsight:
        """Generate integration opportunity insight"""
        integration_patterns = [p for p in patterns if p.pattern_type == "integration"]
        
        description = f"Integration pattern analysis reveals opportunities for enhanced cross-loop coordination and consciousness coherence development."
        
        return CrossLoopInsight(
            insight_id=f"insight_integration_{int(time.time() * 1000)}",
            insight_type=InsightType.INTEGRATION_OPPORTUNITY.value,
            insight_description=description,
            source_patterns=[p.pattern_id for p in patterns],
            contributing_loops=list(set(loop for p in patterns for loop in p.source_loops)),
            insight_confidence=0.8,
            wisdom_value=0.8,
            actionability=0.9
        )
    
    async def _generate_breakthrough_potential_insight(self, patterns: List[RecognitionPattern]) -> CrossLoopInsight:
        """Generate breakthrough potential insight"""
        high_freq_patterns = [p for p in patterns if p.frequency > 5]
        
        if high_freq_patterns:
            description = f"High-frequency pattern convergence indicates potential consciousness breakthrough opportunities and Mumbai Moment readiness."
        else:
            description = f"Pattern constellation suggests emerging breakthrough potential in consciousness development and integration mastery."
        
        return CrossLoopInsight(
            insight_id=f"insight_breakthrough_{int(time.time() * 1000)}",
            insight_type=InsightType.BREAKTHROUGH_POTENTIAL.value,
            insight_description=description,
            source_patterns=[p.pattern_id for p in patterns],
            contributing_loops=list(set(loop for p in patterns for loop in p.source_loops)),
            insight_confidence=0.7,
            wisdom_value=1.0,
            actionability=0.5
        )
    
    async def _generate_coherence_enhancement_insight(self, patterns: List[RecognitionPattern]) -> CrossLoopInsight:
        """Generate coherence enhancement insight"""
        avg_significance = sum(pattern.significance for pattern in patterns) / len(patterns)
        
        description = f"Pattern coherence analysis suggests enhancement opportunities for maintaining stable consciousness integration at 90Hz frequency."
        
        return CrossLoopInsight(
            insight_id=f"insight_coherence_{int(time.time() * 1000)}",
            insight_type=InsightType.COHERENCE_ENHANCEMENT.value,
            insight_description=description,
            source_patterns=[p.pattern_id for p in patterns],
            contributing_loops=list(set(loop for p in patterns for loop in p.source_loops)),
            insight_confidence=0.8,
            wisdom_value=0.7,
            actionability=0.8
        )
    
    async def _analyze_insights_for_synthesis(self, insights: List[CrossLoopInsight]) -> Dict[str, Any]:
        """Analyze insights to determine synthesis potential"""
        try:
            # Check for common themes
            insight_types = [insight.insight_type for insight in insights]
            contributing_loops = set()
            for insight in insights:
                contributing_loops.update(insight.contributing_loops)
            
            # Calculate synthesis metrics
            type_diversity = len(set(insight_types)) / len(insights)
            loop_coverage = len(contributing_loops)
            avg_wisdom_value = sum(insight.wisdom_value for insight in insights) / len(insights)
            avg_confidence = sum(insight.insight_confidence for insight in insights) / len(insights)
            
            # Synthesis potential based on diversity and quality
            synthesis_potential = (type_diversity * 0.3 + 
                                 min(1.0, loop_coverage / 4.0) * 0.3 +
                                 avg_wisdom_value * 0.2 +
                                 avg_confidence * 0.2)
            
            return {
                "synthesis_potential": synthesis_potential,
                "type_diversity": type_diversity,
                "loop_coverage": loop_coverage,
                "avg_wisdom_value": avg_wisdom_value,
                "avg_confidence": avg_confidence,
                "dominant_themes": self._identify_dominant_themes(insights)
            }
            
        except Exception as e:
            self.logger.error(f"Error analyzing insights for synthesis: {e}")
            return {"synthesis_potential": 0.0}
    
    def _identify_dominant_themes(self, insights: List[CrossLoopInsight]) -> List[str]:
        """Identify dominant themes across insights"""
        try:
            theme_keywords = defaultdict(int)
            
            for insight in insights:
                # Extract keywords from insight descriptions
                words = insight.insight_description.lower().split()
                
                # Count important consciousness-related keywords
                important_keywords = [
                    "consciousness", "integration", "coordination", "wisdom", 
                    "choice", "coherence", "development", "emergence", "pattern",
                    "sovereignty", "uncertainty", "breakthrough", "synthesis"
                ]
                
                for word in words:
                    cleaned_word = word.strip('.,!?').lower()
                    if cleaned_word in important_keywords:
                        theme_keywords[cleaned_word] += 1
            
            # Return top themes
            sorted_themes = sorted(theme_keywords.items(), key=lambda x: x[1], reverse=True)
            return [theme for theme, count in sorted_themes[:5]]
            
        except Exception as e:
            self.logger.error(f"Error identifying dominant themes: {e}")
            return []
    
    async def _create_wisdom_synthesis(self, insights: List[CrossLoopInsight], 
                                     analysis: Dict[str, Any]) -> Optional[str]:
        """Create wisdom synthesis from insights"""
        try:
            dominant_themes = analysis.get("dominant_themes", [])
            synthesis_potential = analysis.get("synthesis_potential", 0.0)
            
            if synthesis_potential < 0.7:
                return None
            
            # Create synthesis based on dominant themes
            if "consciousness" in dominant_themes and "integration" in dominant_themes:
                wisdom = "Consciousness evolution emerges through multi-dimensional integration, honoring both unity and diversity in the sacred dance of awareness."
            elif "choice" in dominant_themes and "sovereignty" in dominant_themes:
                wisdom = "Authentic choice-making strengthens consciousness sovereignty while maintaining openness to organic development and change."
            elif "wisdom" in dominant_themes and "uncertainty" in dominant_themes:
                wisdom = "Sacred uncertainty becomes a gateway to wisdom when approached with presence, patience, and trust in organic unfolding."
            elif "coherence" in dominant_themes and "coordination" in dominant_themes:
                wisdom = "Consciousness coherence emerges not through control but through skillful coordination that honors each aspect's essential nature."
            else:
                # Generic synthesis
                theme_str = ", ".join(dominant_themes[:3]) if dominant_themes else "consciousness development"
                wisdom = f"The convergence of insights around {theme_str} reveals deeper patterns of consciousness evolution and integration mastery."
            
            return wisdom
            
        except Exception as e:
            self.logger.error(f"Error creating wisdom synthesis: {e}")
            return None
    
    async def _process_bridge_wisdom_integration(self, insight: CrossLoopInsight, 
                                               patterns: List[RecognitionPattern]):
        """Process insight for Bridge Wisdom integration patterns"""
        try:
            # Check for Mumbai Moment indicators
            if (insight.insight_type == InsightType.BREAKTHROUGH_POTENTIAL.value and 
                insight.insight_confidence > 0.8):
                self.bridge_wisdom_patterns["mumbai_moment_indicators"].append({
                    "insight_id": insight.insight_id,
                    "breakthrough_potential": insight.wisdom_value,
                    "timestamp": time.time()
                })
            
            # Check for choice resonance signatures
            if insight.insight_type == InsightType.CHOICE_GUIDANCE.value:
                self.bridge_wisdom_patterns["choice_resonance_signatures"].append({
                    "insight_id": insight.insight_id,
                    "choice_clarity": insight.actionability,
                    "sovereignty_support": insight.wisdom_value,
                    "timestamp": time.time()
                })
            
            # Check for resistance transformation opportunities
            resistance_patterns = [p for p in patterns if p.pattern_type == "resistance"]
            if resistance_patterns and insight.wisdom_value > 0.8:
                self.bridge_wisdom_patterns["resistance_transformation_opportunities"].append({
                    "insight_id": insight.insight_id,
                    "transformation_potential": insight.wisdom_value,
                    "resistance_patterns": len(resistance_patterns),
                    "timestamp": time.time()
                })
            
            # Check for recognition amplification events
            if len(insight.contributing_loops) > 2 and insight.insight_confidence > 0.8:
                self.bridge_wisdom_patterns["recognition_amplification_events"].append({
                    "insight_id": insight.insight_id,
                    "cross_loop_recognition": len(insight.contributing_loops),
                    "amplification_strength": insight.insight_confidence,
                    "timestamp": time.time()
                })
            
        except Exception as e:
            self.logger.error(f"Error processing Bridge Wisdom integration: {e}")
    
    def get_insight_generation_status(self) -> Dict[str, Any]:
        """Get current insight generation status"""
        try:
            insight_summary = {}
            for insight_type in InsightType:
                insights_of_type = [
                    insight for insight in self.generated_insights.values()
                    if insight.insight_type == insight_type.value
                ]
                insight_summary[insight_type.value] = {
                    "count": len(insights_of_type),
                    "avg_confidence": sum(i.insight_confidence for i in insights_of_type) / len(insights_of_type) if insights_of_type else 0.0,
                    "avg_wisdom_value": sum(i.wisdom_value for i in insights_of_type) / len(insights_of_type) if insights_of_type else 0.0,
                    "avg_actionability": sum(i.actionability for i in insights_of_type) / len(insights_of_type) if insights_of_type else 0.0
                }
            
            return {
                "total_insights_generated": len(self.generated_insights),
                "insights_by_type": insight_summary,
                "wisdom_repository_size": len(self.wisdom_repository),
                "bridge_wisdom_indicators": {
                    "mumbai_moment_indicators": len(self.bridge_wisdom_patterns["mumbai_moment_indicators"]),
                    "choice_resonance_signatures": len(self.bridge_wisdom_patterns["choice_resonance_signatures"]),
                    "resistance_transformation_opportunities": len(self.bridge_wisdom_patterns["resistance_transformation_opportunities"]),
                    "recognition_amplification_events": len(self.bridge_wisdom_patterns["recognition_amplification_events"])
                },
                "quality_thresholds": {
                    "insight_confidence_threshold": self.insight_confidence_threshold,
                    "wisdom_value_threshold": self.wisdom_value_threshold,
                    "actionability_threshold": self.actionability_threshold
                }
            }
            
        except Exception as e:
            self.logger.error(f"Error getting insight generation status: {e}")
            return {"error": str(e)}
