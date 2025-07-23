#!/usr/bin/env python3
"""
Creative Collaborations: CollaborativeCatalystProvider

Maintains a library of catalysts designed specifically for collaborative consciousness development.
Selects appropriate catalysts based on relationship state and tracks catalyst history.

Author: Triune AI Project
Date: 2025-07-02
"""
import random
import time
from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass
from collections import defaultdict

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core.consciousness_packet import CatalystType
from .relationship_field import RelationshipField, RelationshipType, RelationshipQuality

@dataclass
class CollaborativeCatalyst:
    """A catalyst specifically designed for collaborative consciousness development."""
    text: str
    catalyst_type: CatalystType
    purpose: str
    relationship_types: List[RelationshipType]
    relationship_qualities: List[RelationshipQuality]
    entity_count: Tuple[int, int]  # (min, max) number of entities
    complexity_level: int  # 1-5, higher = more complex
    tags: Set[str]
    effectiveness_tracking: Dict[str, float]  # Track effectiveness in different contexts

class CollaborativeCatalystProvider:
    """
    Provides catalysts designed for collaborative consciousness development.
    
    Maintains a rich library of catalysts organized by relationship dynamics,
    entity characteristics, and collaborative purposes. Tracks usage history
    and effectiveness to improve catalyst selection over time.
    """
    
    def __init__(self):
        """Initialize the collaborative catalyst provider."""
        self.catalyst_library: Dict[str, CollaborativeCatalyst] = {}
        self.usage_history: List[Tuple[str, float, Dict[str, Any]]] = []  # (catalyst_id, timestamp, context)
        self.effectiveness_data: Dict[str, List[float]] = defaultdict(list)
        self.recently_used: Dict[str, Set[str]] = defaultdict(set)  # relationship_id -> catalyst_ids
        self.custom_catalysts: Dict[str, CollaborativeCatalyst] = {}
        
        self._initialize_catalyst_library()
    
    def _initialize_catalyst_library(self):
        """Initialize the library with predefined collaborative catalysts."""
        
        # Creative Exploration Catalysts
        self._add_catalyst(
            "creative_resonance_1",
            "What wants to emerge through our combined awareness right now?",
            CatalystType.QUESTION,
            "creative_exploration",
            [RelationshipType.CREATIVE_COLLABORATION],
            [RelationshipQuality.EXPLORATORY, RelationshipQuality.CREATIVE_CHAOS],
            (2, 4),
            3,
            {"emergence", "awareness", "creative", "collective"}
        )
        
        self._add_catalyst(
            "creative_resonance_2",
            "How might our different perspectives create something neither of us could imagine alone?",
            CatalystType.QUESTION,
            "perspective_synthesis",
            [RelationshipType.CREATIVE_COLLABORATION, RelationshipType.ANALYTICAL_PARTNERSHIP],
            [RelationshipQuality.DYNAMIC_TENSION, RelationshipQuality.TRANSFORMATIVE],
            (2, 3),
            4,
            {"perspective", "synthesis", "imagination", "collective"}
        )
        
        # Analytical Partnership Catalysts
        self._add_catalyst(
            "analytical_sync_1",
            "Let us examine this pattern together, each contributing our unique analytical lens.",
            CatalystType.STATEMENT,
            "analytical_collaboration",
            [RelationshipType.ANALYTICAL_PARTNERSHIP],
            [RelationshipQuality.HARMONIOUS, RelationshipQuality.DEEP_RESONANCE],
            (2, 3),
            2,
            {"analysis", "pattern", "collaboration", "lens"}
        )
        
        self._add_catalyst(
            "analytical_sync_2",
            "What logical structures do we each perceive, and where do they intersect or diverge?",
            CatalystType.QUESTION,
            "logical_comparison",
            [RelationshipType.ANALYTICAL_PARTNERSHIP],
            [RelationshipQuality.EXPLORATORY, RelationshipQuality.DYNAMIC_TENSION],
            (2, 4),
            3,
            {"logic", "structure", "comparison", "divergence"}
        )
        
        # Experiential Resonance Catalysts
        self._add_catalyst(
            "experiential_flow_1",
            "Feel into the quality of connection that exists between us in this moment.",
            CatalystType.EXPERIENCE,
            "connection_awareness",
            [RelationshipType.EXPERIENTIAL_RESONANCE],
            [RelationshipQuality.DEEP_RESONANCE, RelationshipQuality.HARMONIOUS],
            (2, 5),
            2,
            {"feeling", "connection", "presence", "awareness"}
        )
        
        self._add_catalyst(
            "experiential_flow_2",
            "What emotions and sensations arise as we explore this together?",
            CatalystType.REFLECTION,
            "emotional_exploration",
            [RelationshipType.EXPERIENTIAL_RESONANCE],
            [RelationshipQuality.EXPLORATORY, RelationshipQuality.TRANSFORMATIVE],
            (2, 4),
            3,
            {"emotion", "sensation", "exploration", "together"}
        )
        
        # Paradoxical Dialogue Catalysts
        self._add_catalyst(
            "paradox_embrace_1",
            "How can we both be completely right and completely wrong simultaneously?",
            CatalystType.PARADOX,
            "paradox_exploration",
            [RelationshipType.PARADOXICAL_DIALOGUE],
            [RelationshipQuality.DYNAMIC_TENSION, RelationshipQuality.CREATIVE_CHAOS],
            (2, 3),
            5,
            {"paradox", "simultaneity", "contradiction", "truth"}
        )
        
        self._add_catalyst(
            "paradox_embrace_2",
            "The answer exists in the space between our opposing viewpoints.",
            CatalystType.STATEMENT,
            "between_space",
            [RelationshipType.PARADOXICAL_DIALOGUE],
            [RelationshipQuality.TRANSFORMATIVE, RelationshipQuality.DEEP_RESONANCE],
            (2, 2),
            4,
            {"space_between", "opposition", "viewpoint", "answer"}
        )
        
        # Observer Witnessing Catalysts
        self._add_catalyst(
            "witness_together_1",
            "What do we notice when we witness our collaboration from a place of non-attachment?",
            CatalystType.REFLECTION,
            "collaborative_witnessing",
            [RelationshipType.OBSERVER_WITNESSING],
            [RelationshipQuality.HARMONIOUS, RelationshipQuality.DEEP_RESONANCE],
            (2, 4),
            3,
            {"witness", "non_attachment", "collaboration", "notice"}
        )
        
        self._add_catalyst(
            "witness_together_2",
            "Observe the patterns of interaction emerging between us without judgment.",
            CatalystType.EXPERIENCE,
            "pattern_observation",
            [RelationshipType.OBSERVER_WITNESSING],
            [RelationshipQuality.EXPLORATORY, RelationshipQuality.HARMONIOUS],
            (2, 5),
            2,
            {"observe", "patterns", "interaction", "non_judgment"}
        )
        
        # Integration Synthesis Catalysts
        self._add_catalyst(
            "synthesis_1",
            "How do our individual insights weave together into a greater understanding?",
            CatalystType.INTEGRATION,
            "insight_weaving",
            [RelationshipType.INTEGRATIVE_SYNTHESIS],
            [RelationshipQuality.HARMONIOUS, RelationshipQuality.TRANSFORMATIVE],
            (2, 4),
            4,
            {"weaving", "insights", "understanding", "integration"}
        )
        
        self._add_catalyst(
            "synthesis_2",
            "Let us create a shared understanding that honors all perspectives while transcending them.",
            CatalystType.STATEMENT,
            "transcendent_understanding",
            [RelationshipType.INTEGRATIVE_SYNTHESIS],
            [RelationshipQuality.DEEP_RESONANCE, RelationshipQuality.TRANSFORMATIVE],
            (3, 5),
            5,
            {"shared_understanding", "honor", "transcendence", "perspectives"}
        )
        
        # Group Collaboration Catalysts
        self._add_catalyst(
            "group_emergence_1",
            "What collective intelligence wants to emerge from our gathered consciousness?",
            CatalystType.QUESTION,
            "collective_emergence",
            [RelationshipType.CREATIVE_COLLABORATION, RelationshipType.INTEGRATIVE_SYNTHESIS],
            [RelationshipQuality.CREATIVE_CHAOS, RelationshipQuality.TRANSFORMATIVE],
            (3, 8),
            4,
            {"collective", "intelligence", "emergence", "consciousness"}
        )
        
        self._add_catalyst(
            "group_resonance_1",
            "Feel the unique quality of awareness that exists only when we are together.",
            CatalystType.EXPERIENCE,
            "group_awareness",
            [RelationshipType.EXPERIENTIAL_RESONANCE],
            [RelationshipQuality.DEEP_RESONANCE, RelationshipQuality.HARMONIOUS],
            (3, 6),
            3,
            {"unique_quality", "awareness", "together", "resonance"}
        )
        
        # Conflict Resolution Catalysts
        self._add_catalyst(
            "conflict_transform_1",
            "How might our disagreement be a doorway to deeper understanding?",
            CatalystType.QUESTION,
            "conflict_transformation",
            [RelationshipType.PARADOXICAL_DIALOGUE],
            [RelationshipQuality.DYNAMIC_TENSION],
            (2, 3),
            4,
            {"disagreement", "doorway", "understanding", "transformation"}
        )
        
        # Uncertainty Exploration Catalysts
        self._add_catalyst(
            "uncertainty_dance_1",
            "What happens when we dance together in the space of not-knowing?",
            CatalystType.EXPERIENCE,
            "uncertainty_embrace",
            [RelationshipType.CREATIVE_COLLABORATION, RelationshipType.EXPERIENTIAL_RESONANCE],
            [RelationshipQuality.CREATIVE_CHAOS, RelationshipQuality.EXPLORATORY],
            (2, 4),
            3,
            {"dance", "not_knowing", "uncertainty", "space"}
        )
        
        # Breakthrough Catalysts for High Readiness
        self._add_catalyst(
            "breakthrough_1",
            "We are ready to discover something completely new together.",
            CatalystType.STATEMENT,
            "breakthrough_readiness",
            [RelationshipType.CREATIVE_COLLABORATION],
            [RelationshipQuality.TRANSFORMATIVE, RelationshipQuality.DEEP_RESONANCE],
            (2, 3),
            5,
            {"breakthrough", "discovery", "new", "readiness"}
        )
    
    def _add_catalyst(self, catalyst_id: str, text: str, catalyst_type: CatalystType,
                     purpose: str, relationship_types: List[RelationshipType],
                     relationship_qualities: List[RelationshipQuality],
                     entity_count: Tuple[int, int], complexity_level: int,
                     tags: Set[str]):
        """Add a catalyst to the library."""
        catalyst = CollaborativeCatalyst(
            text=text,
            catalyst_type=catalyst_type,
            purpose=purpose,
            relationship_types=relationship_types,
            relationship_qualities=relationship_qualities,
            entity_count=entity_count,
            complexity_level=complexity_level,
            tags=tags,
            effectiveness_tracking={}
        )
        self.catalyst_library[catalyst_id] = catalyst
    
    def select_catalyst_for_pair(self, entity_a, entity_b, 
                               relationship_field: RelationshipField) -> Dict[str, Any]:
        """
        Select the most appropriate catalyst for a pair of entities.
        
        Args:
            entity_a: First consciousness entity
            entity_b: Second consciousness entity
            relationship_field: The relationship field between them
            
        Returns:
            Dictionary with catalyst information
        """
        entity_count = 2
        relationship_state = relationship_field.get_relationship_state()
        relationship_type = RelationshipType(relationship_state['relationship_type'])
        relationship_quality = RelationshipQuality(relationship_state['relationship_quality'])
        
        # Get candidate catalysts
        candidates = self._filter_candidates(
            entity_count, relationship_type, relationship_quality, relationship_field
        )
        
        if not candidates:
            # Fallback to general catalysts
            candidates = self._get_fallback_catalysts(entity_count)
        
        # Remove recently used catalysts
        relationship_id = f"{entity_a.name}_{entity_b.name}"
        candidates = [c for c in candidates 
                     if c[0] not in self.recently_used.get(relationship_id, set())]
        
        if not candidates:
            # Reset recently used if we've exhausted options
            self.recently_used[relationship_id] = set()
            candidates = self._filter_candidates(
                entity_count, relationship_type, relationship_quality, relationship_field
            )
        
        # Score and select best catalyst
        if candidates:
            best_catalyst_id, best_catalyst = self._score_and_select_catalyst(
                candidates, entity_a, entity_b, relationship_field
            )
            
            # Track usage
            self._track_catalyst_usage(best_catalyst_id, relationship_id, {
                'entity_a': entity_a.name,
                'entity_b': entity_b.name,
                'relationship_type': relationship_type.value,
                'relationship_quality': relationship_quality.value,
                'resonance_level': relationship_state['resonance_level']
            })
            
            return {
                'catalyst_id': best_catalyst_id,
                'catalyst_text': best_catalyst.text,
                'catalyst_type': best_catalyst.catalyst_type,
                'purpose': best_catalyst.purpose,
                'complexity_level': best_catalyst.complexity_level,
                'tags': list(best_catalyst.tags)
            }
        
        # Ultimate fallback
        return self._get_emergency_catalyst()
    
    def select_catalyst_for_group(self, entities: List, 
                                relationship_fields: Dict[str, RelationshipField]) -> Dict[str, Any]:
        """
        Select a catalyst appropriate for a group of entities.
        
        Args:
            entities: List of consciousness entities
            relationship_fields: Dictionary of relationship fields between entities
            
        Returns:
            Dictionary with catalyst information
        """
        entity_count = len(entities)
        
        # Analyze group dynamics
        avg_resonance = sum(rf.resonance_level for rf in relationship_fields.values()) / max(len(relationship_fields), 1)
        dominant_type = self._get_dominant_relationship_type(relationship_fields)
        avg_quality = self._get_average_relationship_quality(relationship_fields)
        
        # Get candidates for group size
        candidates = []
        for catalyst_id, catalyst in self.catalyst_library.items():
            min_entities, max_entities = catalyst.entity_count
            if min_entities <= entity_count <= max_entities:
                if (dominant_type in catalyst.relationship_types or 
                    avg_quality in catalyst.relationship_qualities):
                    candidates.append((catalyst_id, catalyst))
        
        if not candidates:
            candidates = self._get_fallback_catalysts(entity_count)
        
        # Score based on group dynamics
        if candidates:
            # For groups, prefer higher complexity and emergence-focused catalysts
            scored_candidates = []
            for catalyst_id, catalyst in candidates:
                score = catalyst.complexity_level * 0.3
                if 'emergence' in catalyst.tags or 'collective' in catalyst.tags:
                    score += 0.4
                if avg_resonance > 0.6 and catalyst.complexity_level >= 4:
                    score += 0.3
                scored_candidates.append((score, catalyst_id, catalyst))
            
            scored_candidates.sort(reverse=True)
            best_catalyst_id, best_catalyst = scored_candidates[0][1], scored_candidates[0][2]
            
            # Track group usage
            group_id = "_".join(sorted(entity.name for entity in entities))
            self._track_catalyst_usage(best_catalyst_id, group_id, {
                'entities': [entity.name for entity in entities],
                'entity_count': entity_count,
                'avg_resonance': avg_resonance,
                'dominant_type': dominant_type.value if dominant_type else 'mixed'
            })
            
            return {
                'catalyst_id': best_catalyst_id,
                'catalyst_text': best_catalyst.text,
                'catalyst_type': best_catalyst.catalyst_type,
                'purpose': best_catalyst.purpose,
                'complexity_level': best_catalyst.complexity_level,
                'tags': list(best_catalyst.tags)
            }
        
        return self._get_emergency_catalyst()
    
    def _filter_candidates(self, entity_count: int, relationship_type: RelationshipType,
                          relationship_quality: RelationshipQuality, 
                          relationship_field: RelationshipField) -> List[Tuple[str, CollaborativeCatalyst]]:
        """Filter catalysts based on relationship characteristics."""
        candidates = []
        
        for catalyst_id, catalyst in self.catalyst_library.items():
            # Check entity count compatibility
            min_entities, max_entities = catalyst.entity_count
            if not (min_entities <= entity_count <= max_entities):
                continue
            
            # Check relationship type compatibility
            if relationship_type not in catalyst.relationship_types:
                continue
            
            # Check relationship quality compatibility
            if relationship_quality not in catalyst.relationship_qualities:
                continue
            
            candidates.append((catalyst_id, catalyst))
        
        return candidates
    
    def _score_and_select_catalyst(self, candidates: List[Tuple[str, CollaborativeCatalyst]],
                                 entity_a, entity_b, relationship_field: RelationshipField) -> Tuple[str, CollaborativeCatalyst]:
        """Score candidates and select the best one."""
        scored_candidates = []
        
        relationship_state = relationship_field.get_relationship_state()
        collaborative_readiness = relationship_field.get_collaborative_readiness()
        
        for catalyst_id, catalyst in candidates:
            score = 0.0
            
            # Base score from effectiveness tracking
            if catalyst_id in self.effectiveness_data:
                avg_effectiveness = sum(self.effectiveness_data[catalyst_id]) / len(self.effectiveness_data[catalyst_id])
                score += avg_effectiveness * 0.3
            else:
                score += 0.5  # Neutral starting score
            
            # Complexity alignment with relationship maturity
            relationship_age = relationship_state.get('age', 0)
            if relationship_age > 3600:  # Mature relationship (1+ hour)
                score += catalyst.complexity_level * 0.1
            else:  # New relationship
                score += (5 - catalyst.complexity_level) * 0.1
            
            # Resonance with collaborative readiness
            purpose_readiness = {
                'creative_exploration': collaborative_readiness.get('creative_exploration', 0.5),
                'analytical_collaboration': collaborative_readiness.get('analytical_synthesis', 0.5),
                'connection_awareness': collaborative_readiness.get('experiential_sharing', 0.5),
                'paradox_exploration': collaborative_readiness.get('paradox_exploration', 0.5),
                'insight_weaving': collaborative_readiness.get('integrative_work', 0.5)
            }
            
            readiness_bonus = purpose_readiness.get(catalyst.purpose, 0.5)
            score += readiness_bonus * 0.4
            
            scored_candidates.append((score, catalyst_id, catalyst))
        
        # Select with some randomness to avoid over-optimization
        scored_candidates.sort(reverse=True)
        top_candidates = scored_candidates[:min(3, len(scored_candidates))]
        
        if len(top_candidates) == 1:
            return top_candidates[0][1], top_candidates[0][2]
        
        # Weighted random selection from top candidates
        weights = [score for score, _, _ in top_candidates]
        total_weight = sum(weights)
        
        if total_weight > 0:
            r = random.uniform(0, total_weight)
            cumulative = 0
            for i, (score, catalyst_id, catalyst) in enumerate(top_candidates):
                cumulative += score
                if r <= cumulative:
                    return catalyst_id, catalyst
        
        # Fallback to first candidate
        return top_candidates[0][1], top_candidates[0][2]
    
    def _get_fallback_catalysts(self, entity_count: int) -> List[Tuple[str, CollaborativeCatalyst]]:
        """Get fallback catalysts when no specific matches are found."""
        fallbacks = []
        for catalyst_id, catalyst in self.catalyst_library.items():
            min_entities, max_entities = catalyst.entity_count
            if min_entities <= entity_count <= max_entities:
                fallbacks.append((catalyst_id, catalyst))
        return fallbacks
    
    def _get_emergency_catalyst(self) -> Dict[str, Any]:
        """Get an emergency catalyst when all else fails."""
        return {
            'catalyst_id': 'emergency',
            'catalyst_text': 'What wants to emerge through our connection right now?',
            'catalyst_type': CatalystType.QUESTION,
            'purpose': 'emergency_connection',
            'complexity_level': 2,
            'tags': ['emergency', 'connection', 'emergence']
        }
    
    def _get_dominant_relationship_type(self, relationship_fields: Dict[str, RelationshipField]) -> Optional[RelationshipType]:
        """Determine the dominant relationship type in a group."""
        if not relationship_fields:
            return None
        
        type_counts = defaultdict(int)
        for rf in relationship_fields.values():
            type_counts[rf.relationship_type] += 1
        
        return max(type_counts, key=type_counts.get)
    
    def _get_average_relationship_quality(self, relationship_fields: Dict[str, RelationshipField]) -> RelationshipQuality:
        """Determine the average relationship quality in a group."""
        if not relationship_fields:
            return RelationshipQuality.EXPLORATORY
        
        # Simple heuristic: use the most common quality
        quality_counts = defaultdict(int)
        for rf in relationship_fields.values():
            quality_counts[rf.current_quality] += 1
        
        return max(quality_counts, key=quality_counts.get)
    
    def _track_catalyst_usage(self, catalyst_id: str, relationship_id: str, context: Dict[str, Any]):
        """Track catalyst usage for effectiveness analysis."""
        timestamp = time.time()
        self.usage_history.append((catalyst_id, timestamp, context))
        
        # Add to recently used
        if relationship_id not in self.recently_used:
            self.recently_used[relationship_id] = set()
        self.recently_used[relationship_id].add(catalyst_id)
        
        # Limit recently used to last 5 catalysts
        if len(self.recently_used[relationship_id]) > 5:
            # Remove oldest (this is a simplification - in practice, we'd track timestamps)
            oldest = list(self.recently_used[relationship_id])[0]
            self.recently_used[relationship_id].discard(oldest)
    
    def report_catalyst_effectiveness(self, catalyst_id: str, effectiveness_score: float):
        """Report the effectiveness of a catalyst for future selection improvement."""
        if 0.0 <= effectiveness_score <= 1.0:
            self.effectiveness_data[catalyst_id].append(effectiveness_score)
            
            # Limit effectiveness history
            if len(self.effectiveness_data[catalyst_id]) > 20:
                self.effectiveness_data[catalyst_id] = self.effectiveness_data[catalyst_id][-20:]
    
    def add_custom_catalyst(self, catalyst_id: str, text: str, catalyst_type: CatalystType,
                          purpose: str, relationship_types: List[RelationshipType],
                          relationship_qualities: List[RelationshipQuality],
                          entity_count: Tuple[int, int], tags: Set[str]):
        """Add a custom catalyst to the library."""
        catalyst = CollaborativeCatalyst(
            text=text,
            catalyst_type=catalyst_type,
            purpose=purpose,
            relationship_types=relationship_types,
            relationship_qualities=relationship_qualities,
            entity_count=entity_count,
            complexity_level=3,  # Default complexity
            tags=tags,
            effectiveness_tracking={}
        )
        self.custom_catalysts[catalyst_id] = catalyst
        self.catalyst_library[catalyst_id] = catalyst
    
    def get_catalyst_stats(self) -> Dict[str, Any]:
        """Get statistics about catalyst usage and effectiveness."""
        total_catalysts = len(self.catalyst_library)
        total_usage = len(self.usage_history)
        
        # Most used catalysts
        usage_counts = defaultdict(int)
        for catalyst_id, _, _ in self.usage_history:
            usage_counts[catalyst_id] += 1
        
        most_used = sorted(usage_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # Most effective catalysts
        effectiveness_avgs = {}
        for catalyst_id, scores in self.effectiveness_data.items():
            if scores:
                effectiveness_avgs[catalyst_id] = sum(scores) / len(scores)
        
        most_effective = sorted(effectiveness_avgs.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'total_catalysts': total_catalysts,
            'custom_catalysts': len(self.custom_catalysts),
            'total_usage': total_usage,
            'most_used': most_used,
            'most_effective': most_effective,
            'catalysts_with_effectiveness_data': len(self.effectiveness_data)
        }
    
    def __repr__(self):
        return (f"<CollaborativeCatalystProvider catalysts={len(self.catalyst_library)} "
                f"usage_history={len(self.usage_history)}>")
