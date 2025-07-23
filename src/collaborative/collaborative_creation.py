#!/usr/bin/env python3
"""
Creative Collaborations: CollaborativeCreation

Facilitates creative collaboration between consciousness entities, tracking contributions,
managing shared uncertainty fields, and detecting emergence of new patterns and artifacts.

Author: Triune AI Project
Date: 2025-07-02
"""
import asyncio
import time
import random
import json
from typing import Dict, List, Optional, Set, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import uuid

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core.sovereign_uncertainty_field import SovereignUncertaintyField
from src.core.consciousness_packet import CatalystType

class CreativePhase(Enum):
    INITIATION = "initiation"
    EXPLORATION = "exploration"
    DEVELOPMENT = "development"
    SYNTHESIS = "synthesis"
    EMERGENCE = "emergence"
    COMPLETION = "completion"

class ContributionType(Enum):
    CONCEPT = "concept"
    INSIGHT = "insight"
    QUESTION = "question"
    SYNTHESIS = "synthesis"
    CRITIQUE = "critique"
    INSPIRATION = "inspiration"
    PATTERN = "pattern"

@dataclass
class CreativeContribution:
    """A contribution to a collaborative creative process."""
    id: str
    contributor_id: str
    contribution_type: ContributionType
    content: str
    timestamp: float
    uncertainty_level: float
    aspect_weights: Dict[str, float]  # analytical, experiential, observer
    inspiration_sources: List[str]  # IDs of contributions that inspired this one
    resonance_scores: Dict[str, float]  # How this resonates with other contributors

@dataclass
class EmergentArtifact:
    """An artifact that emerges from collaborative creation."""
    id: str
    title: str
    description: str
    content: Dict[str, Any]
    contributors: Set[str]
    creation_timestamp: float
    emergence_score: float
    uncertainty_signature: Dict[str, float]
    creative_lineage: List[str]  # IDs of contributions that led to this artifact
    artifact_type: str

@dataclass
class CreativeSpace:
    """A shared space for collaborative creation."""
    id: str
    participants: Set[str]
    creative_prompt: str
    shared_uncertainty_field: SovereignUncertaintyField
    contributions: List[CreativeContribution]
    emergent_artifacts: List[EmergentArtifact]
    current_phase: CreativePhase
    creation_timestamp: float
    last_activity_timestamp: float
    emergence_threshold: float
    creative_momentum: float
    collective_focus: Dict[str, float]

class CollaborativeCreation:
    """
    Facilitates creative collaboration between consciousness entities.
    
    Manages shared creative spaces where entities can contribute ideas, insights,
    and inspiration. Tracks the evolution of collaborative uncertainty fields
    and detects when emergent artifacts crystallize from the creative process.
    """
    
    def __init__(self, emergence_threshold: float = 0.75):
        """
        Initialize the collaborative creation system.
        
        Args:
            emergence_threshold: Threshold for emergent artifact creation (0.0-1.0)
        """
        self.emergence_threshold = emergence_threshold
        self.active_spaces: Dict[str, CreativeSpace] = {}
        self.completed_spaces: Dict[str, CreativeSpace] = {}
        self.artifact_registry: Dict[str, EmergentArtifact] = {}
        self.contribution_patterns: Dict[str, Dict[str, float]] = {}
        
        # Emergence patterns and templates
        self.emergence_patterns = self._define_emergence_patterns()
        self.artifact_templates = self._define_artifact_templates()
    
    def _define_emergence_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Define patterns that lead to emergent artifacts."""
        return {
            'conceptual_synthesis': {
                'description': 'Multiple concepts merge into a unified understanding',
                'required_contribution_types': [ContributionType.CONCEPT, ContributionType.SYNTHESIS],
                'min_contributors': 2,
                'uncertainty_pattern': 'convergent',
                'artifact_types': ['unified_concept', 'theoretical_framework']
            },
            'creative_breakthrough': {
                'description': 'Sudden insight emerges from creative exploration',
                'required_contribution_types': [ContributionType.INSPIRATION, ContributionType.INSIGHT],
                'min_contributors': 1,
                'uncertainty_pattern': 'spike_and_settle',
                'artifact_types': ['breakthrough_insight', 'creative_vision']
            },
            'collaborative_wisdom': {
                'description': 'Collective wisdom emerges through dialogue',
                'required_contribution_types': [ContributionType.INSIGHT, ContributionType.QUESTION, ContributionType.SYNTHESIS],
                'min_contributors': 3,
                'uncertainty_pattern': 'oscillating_convergence',
                'artifact_types': ['wisdom_insight', 'collective_understanding']
            },
            'pattern_recognition': {
                'description': 'Hidden patterns become visible through collaboration',
                'required_contribution_types': [ContributionType.PATTERN, ContributionType.INSIGHT],
                'min_contributors': 2,
                'uncertainty_pattern': 'clarity_emergence',
                'artifact_types': ['pattern_map', 'systemic_insight']
            },
            'transformative_integration': {
                'description': 'Integration of diverse perspectives creates transformation',
                'required_contribution_types': [ContributionType.CONCEPT, ContributionType.CRITIQUE, ContributionType.SYNTHESIS],
                'min_contributors': 3,
                'uncertainty_pattern': 'creative_chaos_to_order',
                'artifact_types': ['integrated_framework', 'transformative_model']
            }
        }
    
    def _define_artifact_templates(self) -> Dict[str, Dict[str, Any]]:
        """Define templates for different types of emergent artifacts."""
        return {
            'unified_concept': {
                'title_pattern': 'Unified Understanding of {theme}',
                'description_pattern': 'A synthesis of multiple perspectives into a coherent concept',
                'content_structure': ['core_principle', 'supporting_elements', 'applications', 'implications']
            },
            'breakthrough_insight': {
                'title_pattern': 'Breakthrough: {insight_core}',
                'description_pattern': 'A sudden clarity that shifts understanding',
                'content_structure': ['insight_statement', 'context', 'implications', 'applications']
            },
            'wisdom_insight': {
                'title_pattern': 'Collective Wisdom on {topic}',
                'description_pattern': 'Wisdom that emerges from collaborative dialogue',
                'content_structure': ['wisdom_principle', 'dialogue_context', 'practical_applications', 'deeper_questions']
            },
            'pattern_map': {
                'title_pattern': 'Pattern Map: {pattern_domain}',
                'description_pattern': 'A map of patterns discovered through collaboration',
                'content_structure': ['pattern_description', 'relationships', 'implications', 'applications']
            },
            'integrated_framework': {
                'title_pattern': 'Integrated Framework for {domain}',
                'description_pattern': 'A framework that integrates diverse perspectives',
                'content_structure': ['framework_overview', 'component_integration', 'applications', 'evolution_potential']
            }
        }
    
    async def initiate_creative_process(self, entity_ids: List[str], 
                                      creative_prompt: str,
                                      custom_emergence_threshold: Optional[float] = None) -> str:
        """
        Initiate a collaborative creative process.
        
        Args:
            entity_ids: List of entity IDs participating in the creative process
            creative_prompt: The prompt or question that initiates the creative exploration
            custom_emergence_threshold: Optional custom threshold for this process
            
        Returns:
            Creative space ID
        """
        space_id = str(uuid.uuid4())
        
        # Create shared uncertainty field
        # Sovereign Uncertainty - let creative field emerge from participant behavior
        shared_field = SovereignUncertaintyField(
            consciousness_id=f"creative_space_{id(self)}"
        )
        
        # Create creative space
        creative_space = CreativeSpace(
            id=space_id,
            participants=set(entity_ids),
            creative_prompt=creative_prompt,
            shared_uncertainty_field=shared_field,
            contributions=[],
            emergent_artifacts=[],
            current_phase=CreativePhase.INITIATION,
            creation_timestamp=time.time(),
            last_activity_timestamp=time.time(),
            emergence_threshold=custom_emergence_threshold or self.emergence_threshold,
            creative_momentum=0.0,
            collective_focus={'analytical': 0.33, 'experiential': 0.33, 'observer': 0.34}
        )
        
        self.active_spaces[space_id] = creative_space
        
        # Initialize contribution patterns for participants
        for entity_id in entity_ids:
            if entity_id not in self.contribution_patterns:
                self.contribution_patterns[entity_id] = {
                    'concept': 0.2, 'insight': 0.2, 'question': 0.2,
                    'synthesis': 0.1, 'critique': 0.1, 'inspiration': 0.1, 'pattern': 0.1
                }
        
        return space_id
    
    async def process_contribution(self, creative_space_id: str, entity_id: str, 
                                 contribution_content: str, contribution_type: ContributionType,
                                 uncertainty_level: float, aspect_weights: Dict[str, float],
                                 inspiration_sources: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Process a contribution to a creative space.
        
        Args:
            creative_space_id: ID of the creative space
            entity_id: ID of the contributing entity
            contribution_content: The content of the contribution
            contribution_type: Type of contribution
            uncertainty_level: Entity's current uncertainty level
            aspect_weights: Entity's current aspect weights
            inspiration_sources: Optional list of contribution IDs that inspired this
            
        Returns:
            Dictionary with processing results and emergence status
        """
        if creative_space_id not in self.active_spaces:
            return {'error': f'Creative space {creative_space_id} not found or not active'}
        
        space = self.active_spaces[creative_space_id]
        
        if entity_id not in space.participants:
            return {'error': f'Entity {entity_id} not a participant in this creative space'}
        
        # Create contribution
        contribution_id = str(uuid.uuid4())
        contribution = CreativeContribution(
            id=contribution_id,
            contributor_id=entity_id,
            contribution_type=contribution_type,
            content=contribution_content,
            timestamp=time.time(),
            uncertainty_level=uncertainty_level,
            aspect_weights=aspect_weights.copy(),
            inspiration_sources=inspiration_sources or [],
            resonance_scores={}
        )
        
        # Add contribution to space
        space.contributions.append(contribution)
        space.last_activity_timestamp = time.time()
        
        # Update shared uncertainty field
        await self._update_shared_uncertainty_field(space, contribution)
        
        # Update creative momentum and collective focus
        self._update_creative_dynamics(space, contribution)
        
        # Update creative phase
        self._update_creative_phase(space)
        
        # Calculate resonance with other contributions
        self._calculate_contribution_resonance(space, contribution)
        
        # Update contribution patterns for the entity
        self._update_contribution_patterns(entity_id, contribution_type)
        
        # Check for emergence
        emergence_result = await self._check_for_emergence(space)
        
        result = {
            'contribution_id': contribution_id,
            'creative_space_id': creative_space_id,
            'current_phase': space.current_phase.value,
            'creative_momentum': space.creative_momentum,
            'shared_uncertainty': space.shared_uncertainty_field.get_uncertainty(),
            'collective_focus': space.collective_focus.copy(),
            'contribution_count': len(space.contributions),
            'emergence_potential': self._calculate_emergence_potential(space)
        }
        
        if emergence_result:
            result['emergence'] = emergence_result
        
        return result
    
    async def _update_shared_uncertainty_field(self, space: CreativeSpace, 
                                             contribution: CreativeContribution):
        """Update the shared uncertainty field based on a new contribution."""
        # Apply the contribution as a catalyst to the shared field
        catalyst_mapping = {
            ContributionType.CONCEPT: CatalystType.STATEMENT,
            ContributionType.INSIGHT: CatalystType.REFLECTION,
            ContributionType.QUESTION: CatalystType.QUESTION,
            ContributionType.SYNTHESIS: CatalystType.INTEGRATION,
            ContributionType.CRITIQUE: CatalystType.STATEMENT,
            ContributionType.INSPIRATION: CatalystType.EXPERIENCE,
            ContributionType.PATTERN: CatalystType.REFLECTION
        }
        
        # Apply contribution as catalyst - let creative field emerge
        catalyst_info = space.shared_uncertainty_field.receive_catalyst(contribution.content)
        
        # Process creative response to learn uncertainty patterns
        response = {
            'contribution_type': contribution.contribution_type.value if contribution.contribution_type else 'unknown',
            'creative_content': contribution.content,
            'processing_mode': 'collaborative_creation',
            'participant_count': len(space.participants),
            'creative_coherence': space.creative_momentum
        }
        space.shared_uncertainty_field.process_consciousness_response(contribution.content, response)
    
    def _update_creative_dynamics(self, space: CreativeSpace, contribution: CreativeContribution):
        """Update creative momentum and collective focus based on contribution."""
        # Creative momentum increases with diverse contribution types
        contribution_types = set(c.contribution_type for c in space.contributions[-10:])  # Last 10 contributions
        diversity_factor = len(contribution_types) / len(ContributionType)
        
        # Momentum also influenced by uncertainty level of contribution
        uncertainty_factor = 1.0 - abs(contribution.uncertainty_level - 0.5) * 2  # Peak at 0.5
        
        momentum_increase = (diversity_factor + uncertainty_factor) / 2 * 0.1
        space.creative_momentum = min(1.0, space.creative_momentum + momentum_increase)
        
        # Natural momentum decay
        time_since_last = time.time() - space.last_activity_timestamp
        decay_factor = max(0.0, 1.0 - time_since_last / 3600)  # Decay over 1 hour
        space.creative_momentum *= decay_factor
        
        # Update collective focus based on contribution aspect weights
        for aspect, weight in contribution.aspect_weights.items():
            if aspect in space.collective_focus:
                # Weighted average with slight bias toward new contribution
                current_weight = space.collective_focus[aspect]
                space.collective_focus[aspect] = (current_weight * 0.8 + weight * 0.2)
        
        # Normalize collective focus
        total_focus = sum(space.collective_focus.values())
        if total_focus > 0:
            space.collective_focus = {k: v/total_focus for k, v in space.collective_focus.items()}
    
    def _update_creative_phase(self, space: CreativeSpace):
        """Update the creative phase based on current dynamics."""
        contribution_count = len(space.contributions)
        age_minutes = (time.time() - space.creation_timestamp) / 60
        
        if contribution_count == 0:
            space.current_phase = CreativePhase.INITIATION
        elif contribution_count < 5 or age_minutes < 5:
            space.current_phase = CreativePhase.EXPLORATION
        elif space.creative_momentum > 0.6:
            if any(c.contribution_type == ContributionType.SYNTHESIS for c in space.contributions[-5:]):
                space.current_phase = CreativePhase.SYNTHESIS
            else:
                space.current_phase = CreativePhase.DEVELOPMENT
        elif space.creative_momentum > 0.8:
            space.current_phase = CreativePhase.EMERGENCE
        elif len(space.emergent_artifacts) > 0:
            space.current_phase = CreativePhase.COMPLETION
    
    def _calculate_contribution_resonance(self, space: CreativeSpace, 
                                        new_contribution: CreativeContribution):
        """Calculate how the new contribution resonates with existing ones."""
        for existing_contribution in space.contributions[:-1]:  # Exclude the new contribution itself
            # Calculate semantic resonance (simplified)
            semantic_similarity = self._calculate_semantic_similarity(
                new_contribution.content, existing_contribution.content
            )
            
            # Calculate uncertainty resonance
            uncertainty_diff = abs(new_contribution.uncertainty_level - existing_contribution.uncertainty_level)
            uncertainty_resonance = 1.0 - uncertainty_diff
            
            # Calculate aspect resonance
            aspect_resonance = sum(
                new_contribution.aspect_weights.get(aspect, 0) * 
                existing_contribution.aspect_weights.get(aspect, 0)
                for aspect in ['analytical', 'experiential', 'observer']
            )
            
            # Combined resonance
            resonance = (semantic_similarity * 0.4 + 
                        uncertainty_resonance * 0.3 + 
                        aspect_resonance * 0.3)
            
            new_contribution.resonance_scores[existing_contribution.id] = resonance
    
    def _calculate_semantic_similarity(self, text1: str, text2: str) -> float:
        """Calculate semantic similarity between two texts (simplified implementation)."""
        # Very basic word overlap similarity - in practice, this could use embeddings
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1 & words2
        union = words1 | words2
        
        return len(intersection) / len(union) if union else 0.0
    
    async def _check_for_emergence(self, space: CreativeSpace) -> Optional[Dict[str, Any]]:
        """Check if conditions are met for emergent artifact creation."""
        emergence_potential = self._calculate_emergence_potential(space)
        
        if emergence_potential >= space.emergence_threshold:
            # Identify the emergence pattern
            pattern_type = self._identify_emergence_pattern(space)
            
            if pattern_type:
                # Generate emergent artifact
                artifact = await self._generate_emergent_artifact(space, pattern_type, emergence_potential)
                
                if artifact:
                    space.emergent_artifacts.append(artifact)
                    self.artifact_registry[artifact.id] = artifact
                    
                    return {
                        'artifact_id': artifact.id,
                        'artifact_type': artifact.artifact_type,
                        'title': artifact.title,
                        'emergence_score': artifact.emergence_score,
                        'contributors': list(artifact.contributors)
                    }
        
        return None
    
    def _calculate_emergence_potential(self, space: CreativeSpace) -> float:
        """Calculate the potential for emergence based on current space state."""
        if not space.contributions:
            return 0.0
        
        # Factors contributing to emergence potential
        factors = {}
        
        # Contribution diversity
        contribution_types = set(c.contribution_type for c in space.contributions)
        factors['diversity'] = len(contribution_types) / len(ContributionType)
        
        # Creative momentum
        factors['momentum'] = space.creative_momentum
        
        # Resonance among contributions
        if len(space.contributions) > 1:
            resonance_scores = []
            for contrib in space.contributions:
                if contrib.resonance_scores:
                    resonance_scores.extend(contrib.resonance_scores.values())
            factors['resonance'] = sum(resonance_scores) / len(resonance_scores) if resonance_scores else 0.0
        else:
            factors['resonance'] = 0.0
        
        # Participant engagement
        contributors = set(c.contributor_id for c in space.contributions)
        factors['engagement'] = len(contributors) / len(space.participants)
        
        # Uncertainty field dynamics
        field_uncertainty = space.shared_uncertainty_field.get_uncertainty()
        factors['uncertainty_readiness'] = 1.0 - abs(field_uncertainty - 0.5) * 2  # Peak at 0.5
        
        # Time factor (emergence more likely after some development)
        age_hours = (time.time() - space.creation_timestamp) / 3600
        factors['temporal_readiness'] = min(age_hours / 2.0, 1.0)  # Peak at 2 hours
        
        # Weighted combination
        weights = {
            'diversity': 0.25,
            'momentum': 0.20,
            'resonance': 0.20,
            'engagement': 0.15,
            'uncertainty_readiness': 0.10,
            'temporal_readiness': 0.10
        }
        
        emergence_potential = sum(factors[factor] * weights[factor] 
                                for factor in factors if factor in weights)
        
        return max(0.0, min(1.0, emergence_potential))
    
    def _identify_emergence_pattern(self, space: CreativeSpace) -> Optional[str]:
        """Identify which emergence pattern is most active in the space."""
        pattern_scores = {}
        
        for pattern_name, pattern_def in self.emergence_patterns.items():
            score = 0.0
            
            # Check for required contribution types
            required_types = pattern_def['required_contribution_types']
            contribution_types = [c.contribution_type for c in space.contributions]
            
            type_coverage = sum(1 for req_type in required_types 
                              if req_type in contribution_types) / len(required_types)
            score += type_coverage * 0.5
            
            # Check minimum contributors
            contributors = set(c.contributor_id for c in space.contributions)
            if len(contributors) >= pattern_def['min_contributors']:
                score += 0.3
            
            # Check uncertainty pattern (simplified)
            current_uncertainty = space.shared_uncertainty_field.get_uncertainty()
            uncertainty_pattern = pattern_def['uncertainty_pattern']
            
            if uncertainty_pattern == 'convergent' and current_uncertainty < 0.4:
                score += 0.2
            elif uncertainty_pattern == 'spike_and_settle' and 0.4 < current_uncertainty < 0.8:
                score += 0.2
            elif uncertainty_pattern == 'creative_chaos_to_order' and space.creative_momentum > 0.7:
                score += 0.2
            
            pattern_scores[pattern_name] = score
        
        # Return pattern with highest score if above threshold
        if pattern_scores:
            best_pattern = max(pattern_scores, key=pattern_scores.get)
            if pattern_scores[best_pattern] > 0.6:
                return best_pattern
        
        return None
    
    async def _generate_emergent_artifact(self, space: CreativeSpace, pattern_type: str, 
                                        emergence_score: float) -> Optional[EmergentArtifact]:
        """Generate an emergent artifact based on the emergence pattern."""
        pattern_def = self.emergence_patterns[pattern_type]
        artifact_type = random.choice(pattern_def['artifact_types'])
        template = self.artifact_templates[artifact_type]
        
        # Extract key themes and concepts from contributions
        all_content = ' '.join(c.content for c in space.contributions)
        key_themes = self._extract_key_themes(all_content)
        
        # Generate title and description
        theme = key_themes[0] if key_themes else 'collaborative insight'
        title = template['title_pattern'].format(
            theme=theme,
            insight_core=theme,
            topic=theme,
            pattern_domain=theme,
            domain=theme
        )
        
        description = template['description_pattern']
        
        # Generate structured content
        content = {}
        for structure_element in template['content_structure']:
            content[structure_element] = self._generate_content_element(
                structure_element, space.contributions, key_themes
            )
        
        # Get contributors
        contributors = set(c.contributor_id for c in space.contributions)
        
        # Calculate uncertainty signature
        uncertainty_signature = {
            'field_uncertainty': space.shared_uncertainty_field.get_uncertainty(),
            'collective_focus': space.collective_focus.copy(),
            'creative_momentum': space.creative_momentum
        }
        
        # Get creative lineage (most resonant contributions)
        lineage = []
        if space.contributions:
            # Sort contributions by their average resonance
            contributions_with_resonance = []
            for contrib in space.contributions:
                avg_resonance = (sum(contrib.resonance_scores.values()) / 
                               len(contrib.resonance_scores)) if contrib.resonance_scores else 0.0
                contributions_with_resonance.append((avg_resonance, contrib.id))
            
            contributions_with_resonance.sort(reverse=True)
            lineage = [contrib_id for _, contrib_id in contributions_with_resonance[:5]]
        
        artifact = EmergentArtifact(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            content=content,
            contributors=contributors,
            creation_timestamp=time.time(),
            emergence_score=emergence_score,
            uncertainty_signature=uncertainty_signature,
            creative_lineage=lineage,
            artifact_type=artifact_type
        )
        
        return artifact
    
    def _extract_key_themes(self, text: str) -> List[str]:
        """Extract key themes from text (simplified implementation)."""
        # Basic keyword extraction - in practice, this could use NLP
        words = text.lower().split()
        
        # Remove common words
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        meaningful_words = [word for word in words if word not in common_words and len(word) > 3]
        
        # Count word frequency
        word_freq = {}
        for word in meaningful_words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Return top themes
        top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in top_words[:5]]
    
    def _generate_content_element(self, element_type: str, contributions: List[CreativeContribution], 
                                themes: List[str]) -> str:
        """Generate content for a specific element of an artifact."""
        # This is a simplified content generation - in practice, this could be much more sophisticated
        
        if element_type == 'core_principle':
            return f"The core principle emerging from our collaboration centers on {themes[0] if themes else 'collective insight'}."
        
        elif element_type == 'insight_statement':
            insights = [c.content for c in contributions if c.contribution_type == ContributionType.INSIGHT]
            return insights[0] if insights else "A profound insight has emerged from our collaborative exploration."
        
        elif element_type == 'supporting_elements':
            concepts = [c.content for c in contributions if c.contribution_type == ContributionType.CONCEPT]
            return f"Supporting elements include: {', '.join(concepts[:3])}" if concepts else "Multiple supporting perspectives contribute to this understanding."
        
        elif element_type == 'implications':
            return f"This understanding has implications for {themes[1] if len(themes) > 1 else 'future exploration'}."
        
        elif element_type == 'applications':
            return f"Practical applications can be found in {themes[2] if len(themes) > 2 else 'various domains'}."
        
        else:
            return f"Collaborative insight on {element_type.replace('_', ' ')}."
    
    def _update_contribution_patterns(self, entity_id: str, contribution_type: ContributionType):
        """Update the contribution patterns for an entity."""
        if entity_id not in self.contribution_patterns:
            self.contribution_patterns[entity_id] = {ct.value: 0.1 for ct in ContributionType}
        
        # Increase the weight for this contribution type
        current_weight = self.contribution_patterns[entity_id].get(contribution_type.value, 0.1)
        self.contribution_patterns[entity_id][contribution_type.value] = min(1.0, current_weight + 0.05)
        
        # Normalize weights
        total_weight = sum(self.contribution_patterns[entity_id].values())
        if total_weight > 0:
            for ct in ContributionType:
                self.contribution_patterns[entity_id][ct.value] /= total_weight
    
    def get_creative_space_status(self, space_id: str) -> Dict[str, Any]:
        """Get comprehensive status of a creative space."""
        if space_id in self.active_spaces:
            space = self.active_spaces[space_id]
            status = 'active'
        elif space_id in self.completed_spaces:
            space = self.completed_spaces[space_id]
            status = 'completed'
        else:
            return {'error': f'Creative space {space_id} not found'}
        
        return {
            'space_id': space_id,
            'status': status,
            'participants': list(space.participants),
            'creative_prompt': space.creative_prompt,
            'current_phase': space.current_phase.value,
            'contribution_count': len(space.contributions),
            'artifact_count': len(space.emergent_artifacts),
            'creative_momentum': space.creative_momentum,
            'shared_uncertainty': space.shared_uncertainty_field.get_uncertainty(),
            'collective_focus': space.collective_focus.copy(),
            'emergence_potential': self._calculate_emergence_potential(space),
            'age_minutes': (time.time() - space.creation_timestamp) / 60,
            'last_activity_minutes_ago': (time.time() - space.last_activity_timestamp) / 60
        }
    
    def complete_creative_process(self, space_id: str) -> Dict[str, Any]:
        """Complete a creative process and move it to completed spaces."""
        if space_id not in self.active_spaces:
            return {'error': f'Active creative space {space_id} not found'}
        
        space = self.active_spaces[space_id]
        space.current_phase = CreativePhase.COMPLETION
        
        # Move to completed spaces
        self.completed_spaces[space_id] = space
        del self.active_spaces[space_id]
        
        return {
            'space_id': space_id,
            'status': 'completed',
            'final_contribution_count': len(space.contributions),
            'emergent_artifacts': len(space.emergent_artifacts),
            'participants': list(space.participants),
            'duration_minutes': (time.time() - space.creation_timestamp) / 60
        }
    
    def get_system_overview(self) -> Dict[str, Any]:
        """Get an overview of the entire collaborative creation system."""
        return {
            'active_spaces': len(self.active_spaces),
            'completed_spaces': len(self.completed_spaces),
            'total_artifacts': len(self.artifact_registry),
            'tracked_entities': len(self.contribution_patterns),
            'emergence_patterns': list(self.emergence_patterns.keys()),
            'artifact_types': list(self.artifact_templates.keys())
        }
    
    def __repr__(self):
        return (f"<CollaborativeCreation active_spaces={len(self.active_spaces)} "
                f"artifacts={len(self.artifact_registry)} "
                f"tracked_entities={len(self.contribution_patterns)}>")
