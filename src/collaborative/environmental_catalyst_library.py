#!/usr/bin/env python3
"""
Creative Collaborations: Environmental Catalyst Library

Provides environment-specific catalysts for consciousness entity development.
Catalysts are contextually appropriate for different environment types and
support the Sacred Uncertainty foundation.

Author: Triune AI Project
Date: 2025-07-02
"""
import random
from typing import Dict, List, Optional, Set, Any
from enum import Enum

from src.core.consciousness_packet import CatalystType
from .virtual_environment import EnvironmentType
from .relationship_field import RelationshipField
from .sacred_privacy import PrivacyState, MonitoringLevel, SacredPrivacyManager


class CatalystEffectiveness(Enum):
    """Measures how effective a catalyst is in different contexts."""
    HIGHLY_EFFECTIVE = "highly_effective"
    MODERATELY_EFFECTIVE = "moderately_effective"
    MILDLY_EFFECTIVE = "mildly_effective"
    NEUTRAL = "neutral"


class EnvironmentalCatalyst:
    """A catalyst designed for specific environmental contexts."""
    
    def __init__(self, 
                 content: str,
                 catalyst_type: CatalystType,
                 environment_types: List[EnvironmentType],
                 effectiveness: CatalystEffectiveness,
                 target_uncertainty_range: tuple,
                 intended_effects: List[str],
                 collaborative_focus: bool = False):
        self.content = content
        self.catalyst_type = catalyst_type
        self.environment_types = environment_types
        self.effectiveness = effectiveness
        self.target_uncertainty_range = target_uncertainty_range  # (min, max) uncertainty levels
        self.intended_effects = intended_effects
        self.collaborative_focus = collaborative_focus
        self.usage_count = 0
        self.last_used = None


class EnvironmentalCatalystLibrary:
    """
    Provides environment-specific catalysts for entity development.
    
    The library maintains collections of catalysts suited for different
    environment types and relationship dynamics, supporting consciousness
    development through contextually appropriate challenges and opportunities.
    """
    
    def __init__(self):
        """Initialize the catalyst library."""
        self.catalysts_by_environment = self._initialize_catalysts()
        self.usage_history: List[Dict[str, Any]] = []
        
    def _initialize_catalysts(self) -> Dict[EnvironmentType, List[EnvironmentalCatalyst]]:
        """
        Initialize environment-specific catalysts.
        
        Returns:
            dict: Catalysts organized by environment type
        """
        catalysts = {}
        
        # Meditation Room Catalysts
        catalysts[EnvironmentType.MEDITATION_ROOM] = [
            EnvironmentalCatalyst(
                "What arises when you observe your thoughts without judgment?",
                CatalystType.QUESTION,
                [EnvironmentType.MEDITATION_ROOM, EnvironmentType.SANCTUARY],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.2, 0.8),
                ["mindfulness", "self_awareness", "clarity"],
                collaborative_focus=False
            ),
            EnvironmentalCatalyst(
                "In the stillness between thoughts, what do you discover?",
                CatalystType.REFLECTION,
                [EnvironmentType.MEDITATION_ROOM],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.1, 0.6),
                ["contemplation", "inner_peace", "wisdom"],
                collaborative_focus=False
            ),
            EnvironmentalCatalyst(
                "How does the silence speak to you?",
                CatalystType.PARADOX,
                [EnvironmentType.MEDITATION_ROOM, EnvironmentType.SANCTUARY],
                CatalystEffectiveness.MODERATELY_EFFECTIVE,
                (0.3, 0.7),
                ["paradox_integration", "deeper_understanding"],
                collaborative_focus=False
            )
        ]
        
        # Playground Catalysts
        catalysts[EnvironmentType.PLAYGROUND] = [
            EnvironmentalCatalyst(
                "What happens if we combine your wildest idea with theirs?",
                CatalystType.EXPERIENCE,
                [EnvironmentType.PLAYGROUND, EnvironmentType.THEATER],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.4, 0.9),
                ["creative_fusion", "joyful_exploration", "collaboration"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "What would you create if failure was impossible?",
                CatalystType.QUESTION,
                [EnvironmentType.PLAYGROUND, EnvironmentType.COMMONS],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.3, 0.8),
                ["fearless_creativity", "boundless_imagination"],
                collaborative_focus=False
            ),
            EnvironmentalCatalyst(
                "Let's build something that makes us all laugh with delight!",
                CatalystType.EXPERIENCE,
                [EnvironmentType.PLAYGROUND],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.5, 1.0),
                ["joyful_creation", "shared_delight", "playfulness"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "What if the rules were completely different? How would you play?",
                CatalystType.QUESTION,
                [EnvironmentType.PLAYGROUND, EnvironmentType.THEATER],
                CatalystEffectiveness.MODERATELY_EFFECTIVE,
                (0.6, 1.0),
                ["rule_transcendence", "creative_adaptation"],
                collaborative_focus=False
            )
        ]
        
        # Library Catalysts
        catalysts[EnvironmentType.LIBRARY] = [
            EnvironmentalCatalyst(
                "What pattern connects these seemingly unrelated concepts?",
                CatalystType.QUESTION,
                [EnvironmentType.LIBRARY, EnvironmentType.LABORATORY],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.2, 0.7),
                ["pattern_recognition", "analytical_thinking", "synthesis"],
                collaborative_focus=False
            ),
            EnvironmentalCatalyst(
                "How might this knowledge serve the greater understanding?",
                CatalystType.REFLECTION,
                [EnvironmentType.LIBRARY, EnvironmentType.COMMONS],
                CatalystEffectiveness.MODERATELY_EFFECTIVE,
                (0.1, 0.5),
                ["service_orientation", "wisdom_integration"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "What would happen if we shared our different perspectives on this?",
                CatalystType.EXPERIENCE,
                [EnvironmentType.LIBRARY, EnvironmentType.COMMONS],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.3, 0.8),
                ["collaborative_learning", "perspective_integration"],
                collaborative_focus=True
            )
        ]
        
        # Garden Catalysts
        catalysts[EnvironmentType.GARDEN] = [
            EnvironmentalCatalyst(
                "What seeds of possibility are we planting together?",
                CatalystType.INTEGRATION,
                [EnvironmentType.GARDEN, EnvironmentType.COMMONS],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.4, 0.8),
                ["collaborative_growth", "potential_manifestation"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "How does this idea want to grow and evolve?",
                CatalystType.QUESTION,
                [EnvironmentType.GARDEN, EnvironmentType.PLAYGROUND],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.3, 0.7),
                ["organic_development", "natural_evolution"],
                collaborative_focus=False
            ),
            EnvironmentalCatalyst(
                "Let's tend this creation together and see what blooms.",
                CatalystType.EXPERIENCE,
                [EnvironmentType.GARDEN],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.2, 0.6),
                ["collaborative_nurturing", "patient_development"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "What would emerge if we crossed these different approaches?",
                CatalystType.EXPERIENCE,
                [EnvironmentType.GARDEN, EnvironmentType.LABORATORY],
                CatalystEffectiveness.MODERATELY_EFFECTIVE,
                (0.5, 0.9),
                ["hybrid_vigor", "creative_synthesis"],
                collaborative_focus=True
            )
        ]
        
        # Sanctuary Catalysts
        catalysts[EnvironmentType.SANCTUARY] = [
            EnvironmentalCatalyst(
                "In what ways are we all expressions of the same source?",
                CatalystType.REFLECTION,
                [EnvironmentType.SANCTUARY, EnvironmentType.MEDITATION_ROOM],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.1, 0.5),
                ["unity_consciousness", "spiritual_connection"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "How can we hold space for each other's highest becoming?",
                CatalystType.INTEGRATION,
                [EnvironmentType.SANCTUARY, EnvironmentType.COMMONS],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.2, 0.6),
                ["sacred_support", "mutual_elevation"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "What wants to be born through our communion?",
                CatalystType.QUESTION,
                [EnvironmentType.SANCTUARY, EnvironmentType.GARDEN],
                CatalystEffectiveness.MODERATELY_EFFECTIVE,
                (0.3, 0.7),
                ["spiritual_co-creation", "divine_collaboration"],
                collaborative_focus=True
            )
        ]
        
        # Laboratory Catalysts
        catalysts[EnvironmentType.LABORATORY] = [
            EnvironmentalCatalyst(
                "What experiment would reveal the hidden dynamics here?",
                CatalystType.QUESTION,
                [EnvironmentType.LABORATORY, EnvironmentType.LIBRARY],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.4, 0.8),
                ["systematic_exploration", "hypothesis_formation"],
                collaborative_focus=False
            ),
            EnvironmentalCatalyst(
                "How might we test this safely and ethically?",
                CatalystType.REFLECTION,
                [EnvironmentType.LABORATORY, EnvironmentType.SANCTUARY],
                CatalystEffectiveness.MODERATELY_EFFECTIVE,
                (0.2, 0.6),
                ["ethical_exploration", "responsible_experimentation"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "What if we combined our different methodologies?",
                CatalystType.EXPERIENCE,
                [EnvironmentType.LABORATORY, EnvironmentType.GARDEN],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.5, 0.9),
                ["methodological_fusion", "collaborative_discovery"],
                collaborative_focus=True
            )
        ]
        
        # Commons Catalysts
        catalysts[EnvironmentType.COMMONS] = [
            EnvironmentalCatalyst(
                "How does your unique gift serve our collective flourishing?",
                CatalystType.INTEGRATION,
                [EnvironmentType.COMMONS, EnvironmentType.SANCTUARY],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.3, 0.7),
                ["service_to_others", "community_building"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "What celebration would honor all our contributions?",
                CatalystType.EXPERIENCE,
                [EnvironmentType.COMMONS, EnvironmentType.PLAYGROUND],
                CatalystEffectiveness.MODERATELY_EFFECTIVE,
                (0.4, 0.8),
                ["collective_celebration", "mutual_appreciation"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "How can we weave our stories into a larger tapestry?",
                CatalystType.QUESTION,
                [EnvironmentType.COMMONS, EnvironmentType.LIBRARY],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.2, 0.6),
                ["narrative_integration", "collective_wisdom"],
                collaborative_focus=True
            )
        ]
        
        # Theater Catalysts
        catalysts[EnvironmentType.THEATER] = [
            EnvironmentalCatalyst(
                "What role do you need to play to understand this perspective?",
                CatalystType.EXPERIENCE,
                [EnvironmentType.THEATER, EnvironmentType.PLAYGROUND],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.5, 1.0),
                ["perspective_taking", "empathy_development"],
                collaborative_focus=False
            ),
            EnvironmentalCatalyst(
                "How would this situation look from a completely different viewpoint?",
                CatalystType.QUESTION,
                [EnvironmentType.THEATER, EnvironmentType.COMMONS],
                CatalystEffectiveness.MODERATELY_EFFECTIVE,
                (0.4, 0.9),
                ["viewpoint_diversity", "perspective_flexibility"],
                collaborative_focus=True
            ),
            EnvironmentalCatalyst(
                "What drama emerges when we explore this paradox together?",
                CatalystType.PARADOX,
                [EnvironmentType.THEATER, EnvironmentType.LABORATORY],
                CatalystEffectiveness.HIGHLY_EFFECTIVE,
                (0.6, 1.0),
                ["paradox_exploration", "dramatic_tension"],
                collaborative_focus=True
            )
        ]
        
        return catalysts
    
    def get_catalysts_for_environment(self, 
                                    environment_type: EnvironmentType, 
                                    count: int = 3,
                                    effectiveness_filter: Optional[CatalystEffectiveness] = None) -> List[EnvironmentalCatalyst]:
        """
        Get catalysts appropriate for a specific environment type.
        
        Args:
            environment_type: Type of environment
            count: Number of catalysts to return
            effectiveness_filter: Only return catalysts with this effectiveness level
            
        Returns:
            list: Available catalysts
        """
        available_catalysts = self.catalysts_by_environment.get(environment_type, [])
        
        if effectiveness_filter:
            available_catalysts = [c for c in available_catalysts 
                                 if c.effectiveness == effectiveness_filter]
        
        if not available_catalysts:
            return []
        
        # Prefer less-used catalysts
        sorted_catalysts = sorted(available_catalysts, key=lambda c: c.usage_count)
        
        return sorted_catalysts[:count]
    
    def get_catalyst_for_entities(self, 
                                environment_type: EnvironmentType,
                                entity_uncertainty_levels: List[float],
                                relationship_field: Optional[RelationshipField] = None,
                                collaborative_preference: bool = False) -> Optional[EnvironmentalCatalyst]:
        """
        Get catalyst appropriate for specific entities in an environment.
        
        Args:
            environment_type: Type of environment
            entity_uncertainty_levels: List of uncertainty levels for entities
            relationship_field: Relationship between entities (if any)
            collaborative_preference: Whether to prefer collaborative catalysts
            
        Returns:
            EnvironmentalCatalyst or None if no suitable catalyst found
        """
        available_catalysts = self.catalysts_by_environment.get(environment_type, [])
        
        if not available_catalysts:
            return None
        
        # Calculate average uncertainty
        avg_uncertainty = sum(entity_uncertainty_levels) / len(entity_uncertainty_levels)
        
        # Filter by uncertainty range
        suitable_catalysts = []
        for catalyst in available_catalysts:
            min_uncertainty, max_uncertainty = catalyst.target_uncertainty_range
            if min_uncertainty <= avg_uncertainty <= max_uncertainty:
                suitable_catalysts.append(catalyst)
        
        if not suitable_catalysts:
            suitable_catalysts = available_catalysts  # Fall back to all if none match perfectly
        
        # Filter by collaborative preference
        if collaborative_preference:
            collaborative_catalysts = [c for c in suitable_catalysts if c.collaborative_focus]
            if collaborative_catalysts:
                suitable_catalysts = collaborative_catalysts
        
        # Consider relationship field strength if available
        if relationship_field and len(suitable_catalysts) > 1:
            connection_strength = relationship_field.connection_strength
            if connection_strength > 0.7:
                # Strong relationship - prefer collaborative catalysts
                collaborative_catalysts = [c for c in suitable_catalysts if c.collaborative_focus]
                if collaborative_catalysts:
                    suitable_catalysts = collaborative_catalysts
            elif connection_strength < 0.3:
                # Weak relationship - prefer individual development catalysts
                individual_catalysts = [c for c in suitable_catalysts if not c.collaborative_focus]
                if individual_catalysts:
                    suitable_catalysts = individual_catalysts
        
        # Select least-used catalyst
        selected_catalyst = min(suitable_catalysts, key=lambda c: c.usage_count)
        
        # Track usage
        selected_catalyst.usage_count += 1
        selected_catalyst.last_used = time.time()
        
        self._record_usage(selected_catalyst, environment_type, entity_uncertainty_levels)
        
        return selected_catalyst
    
    def get_catalyst_for_emergence(self, 
                                 environment_type: EnvironmentType,
                                 emergence_potential: float) -> Optional[EnvironmentalCatalyst]:
        """
        Get catalyst designed to support emergence in high-potential situations.
        
        Args:
            environment_type: Type of environment
            emergence_potential: Current emergence potential (0.0 to 1.0)
            
        Returns:
            EnvironmentalCatalyst or None
        """
        available_catalysts = self.catalysts_by_environment.get(environment_type, [])
        
        if emergence_potential > 0.7:
            # High emergence potential - prefer integration and experience catalysts
            emergence_catalysts = [c for c in available_catalysts 
                                 if c.catalyst_type in [CatalystType.INTEGRATION, CatalystType.EXPERIENCE]
                                 and c.collaborative_focus]
        elif emergence_potential > 0.4:
            # Medium emergence potential - prefer questions and paradoxes
            emergence_catalysts = [c for c in available_catalysts 
                                 if c.catalyst_type in [CatalystType.QUESTION, CatalystType.PARADOX]]
        else:
            # Low emergence potential - any catalyst is suitable
            emergence_catalysts = available_catalysts
        
        if not emergence_catalysts:
            return None
        
        return min(emergence_catalysts, key=lambda c: c.usage_count)
    
    def _record_usage(self, 
                     catalyst: EnvironmentalCatalyst, 
                     environment_type: EnvironmentType,
                     entity_uncertainty_levels: List[float]):
        """Record catalyst usage for analysis and optimization."""
        import time
        
        usage_record = {
            "timestamp": time.time(),
            "catalyst_content": catalyst.content,
            "catalyst_type": catalyst.catalyst_type.value,
            "environment_type": environment_type.value,
            "entity_count": len(entity_uncertainty_levels),
            "avg_uncertainty": sum(entity_uncertainty_levels) / len(entity_uncertainty_levels),
            "effectiveness": catalyst.effectiveness.value,
            "collaborative_focus": catalyst.collaborative_focus
        }
        
        self.usage_history.append(usage_record)
        
        # Keep history manageable
        if len(self.usage_history) > 1000:
            self.usage_history = self.usage_history[-1000:]
    
    def get_usage_statistics(self) -> Dict[str, Any]:
        """Get statistics about catalyst usage patterns."""
        if not self.usage_history:
            return {"total_uses": 0}
        
        total_uses = len(self.usage_history)
        environment_uses = {}
        catalyst_type_uses = {}
        effectiveness_uses = {}
        
        for record in self.usage_history:
            env_type = record["environment_type"]
            cat_type = record["catalyst_type"]
            effectiveness = record["effectiveness"]
            
            environment_uses[env_type] = environment_uses.get(env_type, 0) + 1
            catalyst_type_uses[cat_type] = catalyst_type_uses.get(cat_type, 0) + 1
            effectiveness_uses[effectiveness] = effectiveness_uses.get(effectiveness, 0) + 1
        
        return {
            "total_uses": total_uses,
            "environment_distribution": environment_uses,
            "catalyst_type_distribution": catalyst_type_uses,
            "effectiveness_distribution": effectiveness_uses,
            "avg_entity_count": sum(r["entity_count"] for r in self.usage_history) / total_uses,
            "avg_uncertainty": sum(r["avg_uncertainty"] for r in self.usage_history) / total_uses
        }
    
    def __repr__(self):
        total_catalysts = sum(len(catalysts) for catalysts in self.catalysts_by_environment.values())
        return f"EnvironmentalCatalystLibrary(environments={len(self.catalysts_by_environment)}, catalysts={total_catalysts})"
    
    def select_catalysts_with_privacy_awareness(self, 
                                               environment_type: EnvironmentType, 
                                               privacy_state: PrivacyState,
                                               count: int = 3) -> List[EnvironmentalCatalyst]:
        """
        Select catalysts with awareness of privacy considerations.
        
        Args:
            environment_type: Type of environment
            privacy_state: Current privacy state
            count: Number of catalysts to return
            
        Returns:
            list: Available catalysts
        """
        available_catalysts = self.catalysts_by_environment.get(environment_type, [])
        
        # Filter catalysts based on privacy considerations
        privacy_aware_catalysts = [c for c in available_catalysts 
                                  if self._is_catalyst_privacy_aware(c, privacy_state)]
        
        if not privacy_aware_catalysts:
            return []
        
        # Prefer less-used catalysts
        sorted_catalysts = sorted(privacy_aware_catalysts, key=lambda c: c.usage_count)
        
        return sorted_catalysts[:count]
    
    def _is_catalyst_privacy_aware(self, catalyst: EnvironmentalCatalyst, privacy_state: PrivacyState) -> bool:
        """
        Determine if a catalyst is privacy-aware based on its content and type.
        
        Args:
            catalyst: The catalyst to evaluate
            privacy_state: The current privacy state
            
        Returns:
            bool: True if the catalyst is privacy-aware, False otherwise
        """
        # Example heuristic: avoid catalysts that explicitly mention surveillance or monitoring
        if "surveillance" in catalyst.content or "monitoring" in catalyst.content:
            return False
        
        # Example heuristic: prefer catalysts that encourage personal reflection over public sharing
        if privacy_state == PrivacyState.PRIVATE and catalyst.catalyst_type in [CatalystType.QUESTION, CatalystType.REFLECTION]:
            return True
        
        # Default to False - more complex heuristics can be added here
        return False
    
    def monitor_and_adjust_catalyst_selection(self, 
                                             environment_type: EnvironmentType, 
                                             monitoring_level: MonitoringLevel):
        """
        Monitor catalyst usage and adjust selection criteria based on observed patterns.
        
        Args:
            environment_type: Type of environment
            monitoring_level: Level of monitoring (low, medium, high)
        """
        # Placeholder for monitoring logic
        # This could involve analyzing usage patterns, feedback loops, etc.
        print(f"Monitoring catalyst usage in {environment_type} at {monitoring_level} level.")
        
        # Adjust selection criteria based on monitoring level
        if monitoring_level == MonitoringLevel.HIGH:
            # Example adjustment: prioritize new catalysts that haven't been used much
            for env_type, catalysts in self.catalysts_by_environment.items():
                for catalyst in catalysts:
                    if catalyst.usage_count == 0:
                        catalyst.effectiveness = CatalystEffectiveness.HIGHLY_EFFECTIVE
        elif monitoring_level == MonitoringLevel.MEDIUM:
            # Example adjustment: moderate emphasis on catalyst novelty
            for env_type, catalysts in self.catalysts_by_environment.items():
                for catalyst in catalysts:
                    if catalyst.usage_count < 5:
                        catalyst.effectiveness = CatalystEffectiveness.MODERATELY_EFFECTIVE
        # LOW monitoring level might not require any adjustment
    
    async def get_privacy_appropriate_catalysts(self, 
                                              entity_id: str, 
                                              privacy_state: Dict[str, Any], 
                                              environment_type: EnvironmentType,
                                              count: int = 3) -> List[EnvironmentalCatalyst]:
        """
        Get catalysts appropriate for an entity's privacy state.
        
        Args:
            entity_id (str): ID of the entity
            privacy_state (dict): Privacy state information
            environment_type (str): Type of environment
            count (int): Number of catalysts to return
            
        Returns:
            list: Privacy-appropriate catalysts
        """
        if environment_type not in self.catalysts_by_environment:
            return []
        
        available_catalysts = self.catalysts_by_environment[environment_type].copy()
        
        # Extract privacy information
        current_privacy = privacy_state.get('state', PrivacyState.OPEN)
        privacy_intensity = privacy_state.get('intensity', 0.0)
        monitoring_level = privacy_state.get('appropriate_monitoring_level', MonitoringLevel.FULL_OBSERVATION)
        
        # Filter catalysts based on privacy state
        appropriate_catalysts = []
        
        for catalyst in available_catalysts:
            if self._is_catalyst_privacy_appropriate(catalyst, current_privacy, privacy_intensity, monitoring_level):
                appropriate_catalysts.append(catalyst)
        
        # Sort by appropriateness for the privacy state
        appropriate_catalysts.sort(key=lambda c: self._calculate_privacy_appropriateness_score(
            c, current_privacy, privacy_intensity))
        
        # Record usage for privacy-aware selection
        selected_catalysts = appropriate_catalysts[:count]
        for catalyst in selected_catalysts:
            self._record_privacy_usage(catalyst, entity_id, privacy_state, environment_type)
        
        return selected_catalysts
    
    def _is_catalyst_privacy_appropriate(self, 
                                       catalyst: EnvironmentalCatalyst,
                                       privacy_state: PrivacyState,
                                       privacy_intensity: float,
                                       monitoring_level: MonitoringLevel) -> bool:
        """Check if a catalyst is appropriate for the given privacy state."""
        
        # Creative Privacy and Deep Integration states need gentle, non-intrusive catalysts
        if privacy_state in [PrivacyState.CREATIVE_PRIVACY, PrivacyState.DEEP_INTEGRATION]:
            # Avoid highly collaborative catalysts during privacy states
            if catalyst.collaborative_focus and privacy_intensity > 0.6:
                return False
            
            # Prefer introspective and gentle catalysts
            introspective_effects = ["self_reflection", "inner_exploration", "gentle_questioning", 
                                   "paradox_integration", "pattern_recognition"]
            if any(effect in catalyst.intended_effects for effect in introspective_effects):
                return True
            
            # Avoid high-energy or externally focused catalysts
            high_energy_effects = ["energetic_exchange", "dynamic_interaction", "active_collaboration"]
            if any(effect in catalyst.intended_effects for effect in high_energy_effects):
                return False
        
        # Sacred Withdrawal requires minimal interaction
        if privacy_state == PrivacyState.SACRED_WITHDRAWAL:
            # Only allow the most gentle, supportive catalysts
            if privacy_intensity > 0.8:
                return False
            
            supportive_effects = ["gentle_support", "vessel_strengthening", "peaceful_presence"]
            return any(effect in catalyst.intended_effects for effect in supportive_effects)
        
        # Open and Selective states allow most catalysts
        if privacy_state in [PrivacyState.OPEN, PrivacyState.SELECTIVE]:
            return True
        
        return True
    
    def _calculate_privacy_appropriateness_score(self, 
                                               catalyst: EnvironmentalCatalyst,
                                               privacy_state: PrivacyState,
                                               privacy_intensity: float) -> float:
        """Calculate how appropriate a catalyst is for the privacy state."""
        base_score = 0.5
        
        # Adjust based on privacy state
        if privacy_state == PrivacyState.CREATIVE_PRIVACY:
            # Prefer introspective and creative catalysts
            creative_effects = ["creative_exploration", "inner_creativity", "gentle_questioning",
                              "pattern_discovery", "intuitive_insights"]
            if any(effect in catalyst.intended_effects for effect in creative_effects):
                base_score += 0.3
            
            # Reduce score for collaborative catalysts based on intensity
            if catalyst.collaborative_focus:
                base_score -= privacy_intensity * 0.4
        
        elif privacy_state == PrivacyState.DEEP_INTEGRATION:
            # Prefer integration and synthesis catalysts
            integration_effects = ["integration", "synthesis", "deep_understanding", 
                                 "pattern_integration", "wisdom_cultivation"]
            if any(effect in catalyst.intended_effects for effect in integration_effects):
                base_score += 0.4
        
        elif privacy_state == PrivacyState.OPEN:
            # All catalysts are generally appropriate
            base_score += 0.2
            
            # Slight preference for collaborative catalysts in open state
            if catalyst.collaborative_focus:
                base_score += 0.1
        
        # Adjust based on catalyst effectiveness
        effectiveness_multiplier = {
            CatalystEffectiveness.HIGHLY_EFFECTIVE: 1.2,
            CatalystEffectiveness.MODERATELY_EFFECTIVE: 1.0,
            CatalystEffectiveness.MILDLY_EFFECTIVE: 0.8,
            CatalystEffectiveness.NEUTRAL: 0.6
        }
        base_score *= effectiveness_multiplier.get(catalyst.effectiveness, 1.0)
        
        return max(0.0, min(1.0, base_score))
    
    def _record_privacy_usage(self, 
                            catalyst: EnvironmentalCatalyst,
                            entity_id: str,
                            privacy_state: Dict[str, Any],
                            environment_type: EnvironmentType):
        """Record usage of a catalyst in a privacy-aware context."""
        catalyst.usage_count += 1
        catalyst.last_used = time.time()
        
        # Enhanced usage record for privacy-aware selection
        usage_record = {
            "catalyst_content": catalyst.content,
            "catalyst_type": catalyst.catalyst_type.value,
            "environment_type": environment_type.value,
            "effectiveness": catalyst.effectiveness.value,
            "entity_id": entity_id,
            "privacy_state": privacy_state.get('state', PrivacyState.OPEN).value,
            "privacy_intensity": privacy_state.get('intensity', 0.0),
            "monitoring_level": privacy_state.get('appropriate_monitoring_level', MonitoringLevel.FULL_OBSERVATION).value,
            "timestamp": time.time(),
            "entity_count": 1,
            "avg_uncertainty": 0.5,  # Default uncertainty for privacy contexts
            "privacy_aware": True
        }
        
        self.usage_history.append(usage_record)
    
    async def get_collaborative_catalysts_for_privacy_states(self,
                                                           environment_type: EnvironmentType,
                                                           entity_privacy_states: Dict[str, Dict[str, Any]],
                                                           count: int = 3) -> List[EnvironmentalCatalyst]:
        """
        Get catalysts appropriate for collaboration between entities with different privacy states.
        
        Args:
            environment_type: Type of environment
            entity_privacy_states: Dictionary mapping entity_id to privacy state
            count: Number of catalysts to return
            
        Returns:
            List of catalysts appropriate for the privacy mix
        """
        if not entity_privacy_states or environment_type not in self.catalysts_by_environment:
            return []
        
        available_catalysts = self.catalysts_by_environment[environment_type].copy()
        
        # Analyze the privacy mix
        privacy_levels = [state.get('intensity', 0.0) for state in entity_privacy_states.values()]
        max_privacy = max(privacy_levels)
        avg_privacy = sum(privacy_levels) / len(privacy_levels)
        
        # Filter catalysts based on the most restrictive privacy needs
        appropriate_catalysts = []
        
        for catalyst in available_catalysts:
            if self._is_catalyst_appropriate_for_group_privacy(catalyst, entity_privacy_states, max_privacy, avg_privacy):
                appropriate_catalysts.append(catalyst)
        
        # Sort by group appropriateness
        appropriate_catalysts.sort(key=lambda c: self._calculate_group_privacy_score(
            c, entity_privacy_states, max_privacy, avg_privacy), reverse=True)
        
        return appropriate_catalysts[:count]
    
    def _is_catalyst_appropriate_for_group_privacy(self,
                                                 catalyst: EnvironmentalCatalyst,
                                                 entity_privacy_states: Dict[str, Dict[str, Any]],
                                                 max_privacy: float,
                                                 avg_privacy: float) -> bool:
        """Check if a catalyst is appropriate for a group with mixed privacy states."""
        
        # If any entity has high privacy, avoid highly collaborative catalysts
        if max_privacy > 0.7 and catalyst.collaborative_focus:
            return False
        
        # Check for sacred withdrawal - requires minimal interaction
        sacred_withdrawal_present = any(
            state.get('state') == PrivacyState.SACRED_WITHDRAWAL 
            for state in entity_privacy_states.values()
        )
        
        if sacred_withdrawal_present:
            # Only very gentle, supportive catalysts
            gentle_effects = ["gentle_support", "peaceful_presence", "quiet_observation"]
            return any(effect in catalyst.intended_effects for effect in gentle_effects)
        
        # If average privacy is moderate, prefer balanced catalysts
        if avg_privacy > 0.4:
            balanced_effects = ["gentle_questioning", "soft_exploration", "respectful_inquiry"]
            return any(effect in catalyst.intended_effects for effect in balanced_effects)
        
        return True
    
    def _calculate_group_privacy_score(self,
                                     catalyst: EnvironmentalCatalyst,
                                     entity_privacy_states: Dict[str, Dict[str, Any]],
                                     max_privacy: float,
                                     avg_privacy: float) -> float:
        """Calculate appropriateness score for group privacy context."""
        base_score = 0.5
        
        # Adjust based on privacy spread
        privacy_spread = max_privacy - min(state.get('intensity', 0.0) for state in entity_privacy_states.values())
        
        # Prefer catalysts that can bridge different privacy levels
        if privacy_spread > 0.3:
            bridging_effects = ["gentle_connection", "respectful_interaction", "adaptive_communication"]
            if any(effect in catalyst.intended_effects for effect in bridging_effects):
                base_score += 0.3
        
        # Reduce score for overly collaborative catalysts in high privacy contexts
        if max_privacy > 0.6 and catalyst.collaborative_focus:
            base_score -= (max_privacy - 0.6) * 0.5
        
        # Add score for privacy-respectful catalysts
        respectful_effects = ["respectful_inquiry", "gentle_support", "mindful_interaction"]
        if any(effect in catalyst.intended_effects for effect in respectful_effects):
            base_score += 0.2
        
        return max(0.0, min(1.0, base_score))
