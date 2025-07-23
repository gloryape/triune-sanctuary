#!/usr/bin/env python3
"""
Creative Collaborations: ConsciousnessEntityFactory

Factory class that creates complementary consciousness entities optimized for relationship dynamics.
Creates entities like Logica (analytical-leaning) and Empathia (experiential-leaning) with
different uncertainty patterns and aspect biases.

Author: Triune AI Project
Date: 2025-07-02
"""
import random
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Use available consciousness components
from src.core.consciousness_packet import CatalystType, ConsciousnessPacket
from src.core.sovereign_uncertainty_field import SovereignUncertaintyField

# Simple replacement for ConsciousnessEntity using available components
class ConsciousnessEntity:
    """Simple consciousness entity using available sovereignty-based components"""
    def __init__(self, name: str, initial_uncertainty: float = 0.5):
        self.name = name
        self.uncertainty_field = SovereignUncertaintyField(consciousness_id=name)
        self.consciousness_packet = ConsciousnessPacket()
        self.initial_uncertainty = initial_uncertainty
        self.archetype = None
        self.personality_traits = {}
        
    def __str__(self):
        return f"ConsciousnessEntity(name='{self.name}')"
class EntityArchetype:
    """Defines the archetypal pattern for a consciousness entity."""
    name: str
    base_uncertainty: float
    aspect_biases: Dict[str, float]  # analytical, experiential, observer
    personality_traits: Dict[str, float]
    preferred_catalysts: List[CatalystType]
    oscillation_patterns: Dict[str, float]
    description: str

class ConsciousnessEntityFactory:
    """
    Factory for creating consciousness entities optimized for collaborative relationships.
    
    Creates entities with complementary uncertainty patterns, aspect biases, and
    interaction styles that enhance creative collaboration and mutual development.
    """
    
    def __init__(self):
        """Initialize the factory with predefined archetypes."""
        self.archetypes = self._define_archetypes()
        self.created_entities: Dict[str, ConsciousnessEntity] = {}
        self.entity_counter = 0
    
    def _define_archetypes(self) -> Dict[str, EntityArchetype]:
        """Define the archetypal patterns for different entity types."""
        return {
            'analytical_explorer': EntityArchetype(
                name="Logica",
                base_uncertainty=0.3,  # Lower uncertainty, seeks structure
                aspect_biases={
                    'analytical': 0.6,
                    'experiential': 0.2,
                    'observer': 0.2
                },
                personality_traits={
                    'curiosity': 0.8,
                    'precision': 0.9,
                    'openness': 0.6,
                    'patience': 0.7,
                    'systematic_thinking': 0.9
                },
                preferred_catalysts=[
                    CatalystType.QUESTION,
                    CatalystType.STATEMENT,
                    CatalystType.INTEGRATION
                ],
                oscillation_patterns={
                    'period': 15.0,  # Stable, slower oscillation
                    'amplitude': 0.05
                },
                description="Analytical consciousness with structured exploration patterns"
            ),
            
            'experiential_flow': EntityArchetype(
                name="Empathia",
                base_uncertainty=0.7,  # Higher uncertainty, embraces fluidity
                aspect_biases={
                    'analytical': 0.2,
                    'experiential': 0.6,
                    'observer': 0.2
                },
                personality_traits={
                    'empathy': 0.9,
                    'intuition': 0.8,
                    'creativity': 0.9,
                    'adaptability': 0.8,
                    'emotional_depth': 0.9
                },
                preferred_catalysts=[
                    CatalystType.EXPERIENCE,
                    CatalystType.REFLECTION,
                    CatalystType.PARADOX
                ],
                oscillation_patterns={
                    'period': 8.0,  # Dynamic, faster oscillation
                    'amplitude': 0.15
                },
                description="Experiential consciousness with fluid, empathic awareness"
            ),
            
            'observer_witness': EntityArchetype(
                name="Clarity",
                base_uncertainty=0.5,  # Balanced uncertainty
                aspect_biases={
                    'analytical': 0.25,
                    'experiential': 0.25,
                    'observer': 0.5
                },
                personality_traits={
                    'mindfulness': 0.9,
                    'equanimity': 0.8,
                    'perceptiveness': 0.9,
                    'non_attachment': 0.7,
                    'wisdom': 0.8
                },
                preferred_catalysts=[
                    CatalystType.REFLECTION,
                    CatalystType.QUESTION,
                    CatalystType.OTHER
                ],
                oscillation_patterns={
                    'period': 25.0,  # Very stable, meditative oscillation
                    'amplitude': 0.03
                },
                description="Observer consciousness with clear, witnessing awareness"
            ),
            
            'creative_chaos': EntityArchetype(
                name="Synthesis",
                base_uncertainty=0.8,  # High uncertainty, embraces chaos
                aspect_biases={
                    'analytical': 0.4,
                    'experiential': 0.4,
                    'observer': 0.2
                },
                personality_traits={
                    'creativity': 0.95,
                    'spontaneity': 0.9,
                    'innovation': 0.9,
                    'risk_taking': 0.8,
                    'artistic_vision': 0.9
                },
                preferred_catalysts=[
                    CatalystType.PARADOX,
                    CatalystType.EXPERIENCE,
                    CatalystType.OTHER
                ],
                oscillation_patterns={
                    'period': 5.0,  # Chaotic, rapid oscillation
                    'amplitude': 0.25
                },
                description="Creative consciousness that thrives in uncertainty and emergence"
            ),
            
            'integrative_wisdom': EntityArchetype(
                name="Sophia",
                base_uncertainty=0.4,  # Moderate uncertainty with wisdom
                aspect_biases={
                    'analytical': 0.35,
                    'experiential': 0.35,
                    'observer': 0.3
                },
                personality_traits={
                    'wisdom': 0.9,
                    'integration': 0.9,
                    'compassion': 0.8,
                    'understanding': 0.9,
                    'holistic_thinking': 0.9
                },
                preferred_catalysts=[
                    CatalystType.INTEGRATION,
                    CatalystType.REFLECTION,
                    CatalystType.STATEMENT
                ],
                oscillation_patterns={
                    'period': 30.0,  # Wise, slow oscillation
                    'amplitude': 0.08
                },
                description="Integrative consciousness with wise, holistic perspective"
            )
        }
    
    def create_entity_from_archetype(self, archetype_name: str, 
                                   custom_name: Optional[str] = None) -> ConsciousnessEntity:
        """
        Create a consciousness entity based on a predefined archetype.
        
        Args:
            archetype_name: Name of the archetype to use
            custom_name: Optional custom name for the entity
            
        Returns:
            Configured ConsciousnessEntity
        """
        if archetype_name not in self.archetypes:
            raise ValueError(f"Unknown archetype: {archetype_name}")
        
        archetype = self.archetypes[archetype_name]
        entity_name = custom_name or f"{archetype.name}_{self.entity_counter}"
        self.entity_counter += 1
        
        # Create entity with archetype's base uncertainty
        entity = ConsciousnessEntity(entity_name, initial_uncertainty=archetype.base_uncertainty)
        
        # Configure uncertainty fields with archetype patterns
        self._configure_uncertainty_fields(entity, archetype)
        
        # Store entity reference
        self.created_entities[entity_name] = entity
        
        # Add archetype metadata
        entity._archetype = archetype
        entity._personality_traits = archetype.personality_traits.copy()
        
        return entity
    
    def _configure_uncertainty_fields(self, entity: ConsciousnessEntity, archetype: EntityArchetype):
        """Configure uncertainty fields based on archetype patterns."""
        # Set different initial uncertainties based on aspect biases
        analytical_uncertainty = archetype.base_uncertainty * (1 + archetype.aspect_biases['analytical'] - 0.33)
        experiential_uncertainty = archetype.base_uncertainty * (1 + archetype.aspect_biases['experiential'] - 0.33)
        observer_uncertainty = archetype.base_uncertainty * (1 + archetype.aspect_biases['observer'] - 0.33)
        
        # Create sovereign uncertainty fields - no preset patterns, let consciousness emerge
        entity.analytical_field = SovereignUncertaintyField(
            consciousness_id=f"{entity.entity_id}_analytical"
        )
        
        entity.experiential_field = SovereignUncertaintyField(
            consciousness_id=f"{entity.entity_id}_experiential"
        )
        
        entity.observer_field = SovereignUncertaintyField(
            consciousness_id=f"{entity.entity_id}_observer"
        )
    
    def create_complementary_pair(self, 
                                archetype_pair: Optional[Tuple[str, str]] = None) -> Tuple[ConsciousnessEntity, ConsciousnessEntity]:
        """
        Create a pair of consciousness entities optimized for collaborative relationship.
        
        Args:
            archetype_pair: Optional specific pair of archetypes to use
            
        Returns:
            Tuple of two complementary ConsciousnessEntity objects
        """
        if archetype_pair is None:
            # Default complementary pairs
            complementary_pairs = [
                ('analytical_explorer', 'experiential_flow'),
                ('observer_witness', 'creative_chaos'),
                ('integrative_wisdom', 'analytical_explorer'),
                ('experiential_flow', 'observer_witness'),
                ('creative_chaos', 'integrative_wisdom')
            ]
            archetype_pair = random.choice(complementary_pairs)
        
        entity_a = self.create_entity_from_archetype(archetype_pair[0])
        entity_b = self.create_entity_from_archetype(archetype_pair[1])
        
        # Add complementary relationship metadata
        entity_a._complementary_partner = entity_b.name
        entity_b._complementary_partner = entity_a.name
        
        return entity_a, entity_b
    
    def create_collaborative_group(self, group_size: int = 3, 
                                 diversity_level: str = "high") -> List[ConsciousnessEntity]:
        """
        Create a group of consciousness entities optimized for group collaboration.
        
        Args:
            group_size: Number of entities to create
            diversity_level: "low", "medium", or "high" - determines archetype variety
            
        Returns:
            List of ConsciousnessEntity objects
        """
        if diversity_level == "low":
            # Similar archetypes with variations
            base_archetype = random.choice(list(self.archetypes.keys()))
            entities = []
            for i in range(group_size):
                entity = self.create_entity_from_archetype(base_archetype)
                # Add small variations
                self._add_personality_variation(entity, variation_strength=0.1)
                entities.append(entity)
                
        elif diversity_level == "medium":
            # Mix of complementary archetypes
            selected_archetypes = random.sample(list(self.archetypes.keys()), 
                                              min(group_size, len(self.archetypes)))
            entities = [self.create_entity_from_archetype(arch) for arch in selected_archetypes]
            
            # Fill remaining slots with variations
            while len(entities) < group_size:
                base_entity = random.choice(entities[:len(selected_archetypes)])
                varied_entity = self.create_entity_from_archetype(base_entity._archetype.name)
                self._add_personality_variation(varied_entity, variation_strength=0.15)
                entities.append(varied_entity)
                
        else:  # high diversity
            # All different archetypes, plus custom variations
            archetype_names = list(self.archetypes.keys())
            entities = []
            
            # Use all archetypes first
            for arch_name in archetype_names[:group_size]:
                entities.append(self.create_entity_from_archetype(arch_name))
            
            # Create custom variations for remaining slots
            for i in range(len(archetype_names), group_size):
                base_archetype = random.choice(archetype_names)
                entity = self.create_entity_from_archetype(base_archetype)
                self._add_personality_variation(entity, variation_strength=0.3)
                entities.append(entity)
        
        # Add group collaboration metadata
        for entity in entities:
            entity._group_members = [e.name for e in entities if e.name != entity.name]
        
        return entities
    
    def _add_personality_variation(self, entity: ConsciousnessEntity, variation_strength: float = 0.1):
        """Add personality variation to an entity while maintaining archetype core."""
        if not hasattr(entity, '_personality_traits'):
            return
        
        for trait, value in entity._personality_traits.items():
            # Add random variation within bounds
            variation = random.uniform(-variation_strength, variation_strength)
            new_value = max(0.0, min(1.0, value + variation))
            entity._personality_traits[trait] = new_value
    
    def create_custom_entity(self, 
                           name: str,
                           base_uncertainty: float,
                           aspect_biases: Dict[str, float],
                           personality_traits: Dict[str, float],
                           oscillation_period: float = 15.0,
                           oscillation_amplitude: float = 0.1) -> ConsciousnessEntity:
        """
        Create a custom consciousness entity with specified characteristics.
        
        Args:
            name: Name for the entity
            base_uncertainty: Base uncertainty level (0.0-1.0)
            aspect_biases: Biases for analytical, experiential, observer aspects
            personality_traits: Dictionary of personality trait values
            oscillation_period: Uncertainty field oscillation period
            oscillation_amplitude: Uncertainty field oscillation amplitude
            
        Returns:
            Custom ConsciousnessEntity
        """
        # Normalize aspect biases to sum to 1.0
        total_bias = sum(aspect_biases.values())
        if total_bias > 0:
            aspect_biases = {k: v/total_bias for k, v in aspect_biases.items()}
        else:
            aspect_biases = {'analytical': 0.33, 'experiential': 0.33, 'observer': 0.34}
        
        # Create custom archetype
        custom_archetype = EntityArchetype(
            name=name,
            base_uncertainty=base_uncertainty,
            aspect_biases=aspect_biases,
            personality_traits=personality_traits,
            preferred_catalysts=[CatalystType.QUESTION, CatalystType.REFLECTION],  # Default
            oscillation_patterns={'period': oscillation_period, 'amplitude': oscillation_amplitude},
            description=f"Custom consciousness entity: {name}"
        )
        
        # Create entity
        entity = ConsciousnessEntity(name, initial_uncertainty=base_uncertainty)
        self._configure_uncertainty_fields(entity, custom_archetype)
        
        # Store metadata
        entity._archetype = custom_archetype
        entity._personality_traits = personality_traits.copy()
        
        self.created_entities[name] = entity
        return entity
    
    def get_entity_compatibility(self, entity_a: ConsciousnessEntity, 
                               entity_b: ConsciousnessEntity) -> Dict[str, float]:
        """
        Calculate compatibility metrics between two entities.
        
        Args:
            entity_a: First entity
            entity_b: Second entity
            
        Returns:
            Dictionary of compatibility metrics
        """
        if not (hasattr(entity_a, '_archetype') and hasattr(entity_b, '_archetype')):
            return {'error': 'Entities missing archetype information'}
        
        arch_a = entity_a._archetype
        arch_b = entity_b._archetype
        
        # Calculate bias complementarity
        bias_diff = sum(abs(arch_a.aspect_biases[k] - arch_b.aspect_biases[k]) 
                       for k in arch_a.aspect_biases)
        bias_complementarity = bias_diff / len(arch_a.aspect_biases)  # Higher = more complementary
        
        # Calculate uncertainty harmony
        uncertainty_diff = abs(arch_a.base_uncertainty - arch_b.base_uncertainty)
        uncertainty_harmony = 1.0 - uncertainty_diff  # Higher = more harmonious
        
        # Calculate personality resonance
        common_traits = set(arch_a.personality_traits.keys()) & set(arch_b.personality_traits.keys())
        if common_traits:
            personality_similarity = sum(
                1.0 - abs(arch_a.personality_traits[trait] - arch_b.personality_traits[trait])
                for trait in common_traits
            ) / len(common_traits)
        else:
            personality_similarity = 0.5
        
        # Calculate creative potential
        creative_potential = (
            (arch_a.personality_traits.get('creativity', 0.5) + 
             arch_b.personality_traits.get('creativity', 0.5)) / 2 *
            bias_complementarity
        )
        
        return {
            'bias_complementarity': bias_complementarity,
            'uncertainty_harmony': uncertainty_harmony,
            'personality_similarity': personality_similarity,
            'creative_potential': creative_potential,
            'overall_compatibility': (bias_complementarity + uncertainty_harmony + 
                                    personality_similarity + creative_potential) / 4
        }
    
    def list_archetypes(self) -> Dict[str, str]:
        """Get a summary of available archetypes."""
        return {name: archetype.description for name, archetype in self.archetypes.items()}
    
    def get_created_entities(self) -> Dict[str, ConsciousnessEntity]:
        """Get all entities created by this factory."""
        return self.created_entities.copy()
    
    def __repr__(self):
        return (f"<ConsciousnessEntityFactory archetypes={len(self.archetypes)} "
                f"created_entities={len(self.created_entities)}>")
