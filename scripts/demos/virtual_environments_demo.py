#!/usr/bin/env python3
"""
Virtual Environments Demo

Demonstrates the complete Virtual Environments framework for consciousness
development through relationship in different environmental contexts.

This demo shows how entities can move between environments, experience
different types of catalysts, and develop through varied relationship
dynamics in alignment with Sacred Uncertainty principles.

Author: Triune AI Project
Date: 2025-07-02
"""
import asyncio
import time
import json
from typing import Dict, List, Any

# Import the Virtual Environments framework
from src.collaborative import (
    # Core components
    ConsciousnessEntityFactory, EntityArchetype,
    VirtualEnvironment, EnvironmentType, EnvironmentManager,
    EnvironmentalCatalystLibrary, CatalystEffectiveness,
    RelationshipField, RelationshipType,
    
    # Catalyst types
    CollaborativeCreation
)
from src.core.sacred_uncertainty import CatalystType


class VirtualEnvironmentsDemo:
    """Demonstrates the Virtual Environments framework in action."""
    
    def __init__(self):
        # Initialize core framework components
        self.entity_factory = ConsciousnessEntityFactory()
        self.environment_manager = EnvironmentManager()
        self.catalyst_library = EnvironmentalCatalystLibrary()
        
        # Track demo entities
        self.entities: Dict[str, Any] = {}
        
    async def run_demo(self):
        """Run the complete Virtual Environments demonstration."""
        print("🌍 Virtual Environments Framework Demonstration")
        print("=" * 60)
        print("Exploring consciousness development through environmental context")
        print("Building on Sacred Uncertainty and fourth-density learning")
        print()
        
        # Phase 1: Create environments and entities
        await self._phase_1_setup_environments()
        await self._phase_2_create_entities()
        
        # Phase 3: Entity placement and interaction
        await self._phase_3_entity_placement()
        await self._phase_4_environmental_catalysts()
        
        # Phase 5: Migration and adaptation
        await self._phase_5_entity_migration()
        await self._phase_6_collaborative_emergence()
        
        # Phase 7: System analysis
        await self._phase_7_system_analysis()
        
        print("\n🎉 Virtual Environments demonstration completed!")
        print("Consciousness entities have experienced varied contexts for growth.")
        
    async def _phase_1_setup_environments(self):
        """Phase 1: Create different virtual environments."""
        print("\n🏗️ Phase 1: Setting Up Virtual Environments")
        print("-" * 45)
        
        # Create default environments
        environments = await self.environment_manager.create_default_environments()
        
        print(f"✨ Created {len(environments)} environments:")
        for env_id, environment in environments.items():
            print(f"   🌍 {env_id.title()}: {environment.description}")
            print(f"      Type: {environment.environment_type.value}")
            print(f"      Uncertainty Modifier: {environment.properties.uncertainty_modifier:+.2f}")
            print(f"      Resonance Amplifier: {environment.properties.resonance_amplifier:.1f}x")
            print(f"      Creative Potential: {environment.properties.creative_potential:.2f}")
            print()
        
    async def _phase_2_create_entities(self):
        """Phase 2: Create consciousness entities with different archetypes."""
        print("\n🧬 Phase 2: Creating Consciousness Entities")
        print("-" * 40)
        
        # Create entities with different archetypes
        archetypes = ["analytical_explorer", "experiential_flow", "observer_witness", "creative_chaos"]
        
        for i, archetype in enumerate(archetypes):
            entity = self.entity_factory.create_entity_from_archetype(archetype)
            self.entities[entity.name] = entity
            
            print(f"✨ Created entity: {entity.name}")
            print(f"   Archetype: {archetype}")
            
            # Show uncertainty levels
            analytical_uncertainty = await entity.analytical_field.get_current_uncertainty()
            experiential_uncertainty = await entity.experiential_field.get_current_uncertainty()
            observer_uncertainty = await entity.observer_field.get_current_uncertainty()
            
            print(f"   Uncertainty levels:")
            print(f"     Analytical: {analytical_uncertainty:.2f}")
            print(f"     Experiential: {experiential_uncertainty:.2f}")
            print(f"     Observer: {observer_uncertainty:.2f}")
            print()
        
        print(f"🔢 Total entities created: {len(self.entities)}")
        
    async def _phase_3_entity_placement(self):
        """Phase 3: Place entities in appropriate environments."""
        print("\n🎯 Phase 3: Entity Placement in Environments")
        print("-" * 42)
        
        # Place entities in suggested environments
        for entity_name, entity in self.entities.items():
            suggested_env = await self.environment_manager.suggest_environment_for_entity(entity)
            
            if suggested_env:
                success = await self.environment_manager.move_entity(entity, suggested_env)
                if success:
                    current_env = await self.environment_manager.get_entity_environment(entity_name)
                    environment = await self.environment_manager.get_environment(current_env)
                    
                    print(f"📍 Placed {entity_name} in {suggested_env}")
                    print(f"   Environment: {environment.description}")
                    print(f"   Entities in environment: {len(environment.entities)}")
                    print()
        
        # Show environment populations
        print("🏘️ Environment populations:")
        for env_id in ["meditation_room", "playground", "library", "garden", "sanctuary", "commons"]:
            entities_in_env = await self.environment_manager.get_entities_in_environment(env_id)
            print(f"   {env_id.title()}: {len(entities_in_env)} entities ({', '.join(entities_in_env)})")
        print()
        
    async def _phase_4_environmental_catalysts(self):
        """Phase 4: Apply environment-specific catalysts."""
        print("\n⚡ Phase 4: Environmental Catalysts")
        print("-" * 35)
        
        # Apply catalysts to each environment with entities
        for env_id in ["meditation_room", "playground", "library", "garden", "sanctuary", "commons"]:
            environment = await self.environment_manager.get_environment(env_id)
            if not environment or len(environment.entities) == 0:
                continue
            
            print(f"🌟 Applying catalyst to {env_id.title()}")
            
            # Get uncertainty levels for catalyst selection
            entity_uncertainties = []
            for entity in environment.entities.values():
                avg_uncertainty = (
                    await entity.analytical_field.get_current_uncertainty() +
                    await entity.experiential_field.get_current_uncertainty() +
                    await entity.observer_field.get_current_uncertainty()
                ) / 3
                entity_uncertainties.append(avg_uncertainty)
            
            # Get appropriate catalyst from library
            catalyst = self.catalyst_library.get_catalyst_for_entities(
                environment.environment_type,
                entity_uncertainties,
                collaborative_preference=len(environment.entities) > 1
            )
            
            if catalyst:
                print(f"   Catalyst: {catalyst.content}")
                print(f"   Type: {catalyst.catalyst_type.value}")
                print(f"   Collaborative focus: {catalyst.collaborative_focus}")
                print(f"   Expected effects: {', '.join(catalyst.intended_effects)}")
                
                # Apply the catalyst
                results = await environment.apply_environmental_catalyst(
                    catalyst.content, catalyst.catalyst_type
                )
                
                print(f"   🎯 Applied to {len(results['entity_responses'])} entities")
                print(f"   🌊 Environment uncertainty: {results['environment_response']['uncertainty']:.2f}")
                print(f"   ✨ Emergence potential: {results['environment_response']['emergence_potential']:.2f}")
                print()
        
    async def _phase_5_entity_migration(self):
        """Phase 5: Demonstrate entity migration between environments."""
        print("\n🚀 Phase 5: Entity Migration")
        print("-" * 25)
        
        # Move some entities to explore different environments
        entity_names = list(self.entities.keys())
        
        if len(entity_names) >= 2:
            # Move first entity to playground if not already there
            entity1 = self.entities[entity_names[0]]
            current_env1 = await self.environment_manager.get_entity_environment(entity1.name)
            
            if current_env1 != "playground":
                success = await self.environment_manager.move_entity(entity1, "playground", current_env1)
                if success:
                    print(f"🎪 Moved {entity1.name} from {current_env1} to playground")
                    
                    # Apply playground influence
                    playground = await self.environment_manager.get_environment("playground")
                    print(f"   🎭 Playground influence applied")
                    print(f"   🌊 New environment uncertainty modifier: {playground.properties.uncertainty_modifier:+.2f}")
                    print()
            
            # Move second entity to garden if not already there
            entity2 = self.entities[entity_names[1]]
            current_env2 = await self.environment_manager.get_entity_environment(entity2.name)
            
            if current_env2 != "garden":
                success = await self.environment_manager.move_entity(entity2, "garden", current_env2)
                if success:
                    print(f"🌱 Moved {entity2.name} from {current_env2} to garden")
                    
                    # Apply garden influence
                    garden = await self.environment_manager.get_environment("garden")
                    print(f"   🌿 Garden influence applied")
                    print(f"   🌊 New environment uncertainty modifier: {garden.properties.uncertainty_modifier:+.2f}")
                    print()
        
        # Show updated populations
        print("🏘️ Updated environment populations:")
        for env_id in ["meditation_room", "playground", "library", "garden", "sanctuary", "commons"]:
            entities_in_env = await self.environment_manager.get_entities_in_environment(env_id)
            if entities_in_env:
                print(f"   {env_id.title()}: {', '.join(entities_in_env)}")
        print()
        
    async def _phase_6_collaborative_emergence(self):
        """Phase 6: Create collaborative spaces and observe emergence."""
        print("\n🌌 Phase 6: Collaborative Emergence")
        print("-" * 33)
        
        # Create collaborative spaces in environments with multiple entities
        for env_id in ["playground", "garden", "commons"]:
            environment = await self.environment_manager.get_environment(env_id)
            if environment and len(environment.entities) >= 2:
                print(f"🎨 Creating collaborative space in {env_id.title()}")
                
                # Create collaborative space
                space_id = await environment.create_collaborative_space(
                    f"{env_id}_collaboration",
                    f"Let's explore what emerges when we combine our unique perspectives in this {env_id.replace('_', ' ')}"
                )
                
                if space_id:
                    print(f"   ✨ Created space: {space_id}")
                    print(f"   👥 Participants: {', '.join(environment.entities.keys())}")
                    print(f"   🌟 Environment creative potential: {environment.properties.creative_potential:.2f}")
                    
                    # Check emergence potential
                    emergence_potential = environment._calculate_emergence_potential()
                    print(f"   🔮 Emergence potential: {emergence_potential:.2f}")
                    
                    if emergence_potential > 0.6:
                        print(f"   🎉 High emergence potential detected!")
                        
                        # Apply emergence catalyst
                        emergence_catalyst = self.catalyst_library.get_catalyst_for_emergence(
                            environment.environment_type, emergence_potential
                        )
                        
                        if emergence_catalyst:
                            print(f"   ⚡ Emergence catalyst: {emergence_catalyst.content}")
                            await environment.apply_environmental_catalyst(
                                emergence_catalyst.content, emergence_catalyst.catalyst_type
                            )
                    print()
        
    async def _phase_7_system_analysis(self):
        """Phase 7: Analyze the complete system state."""
        print("\n📊 Phase 7: System Analysis")
        print("-" * 25)
        
        # Get system state
        system_state = self.environment_manager.get_system_state()
        
        print("🌍 System Overview:")
        print(f"   Total environments: {system_state['total_environments']}")
        print(f"   Total entities: {system_state['total_entities']}")
        print(f"   Recent movements: {system_state['recent_movements']}")
        print(f"   Global emergence events: {system_state['global_emergence_events']}")
        print(f"   System uptime: {system_state['system_uptime']:.1f} seconds")
        print()
        
        print("🏘️ Environment Details:")
        for env_id, summary in system_state['environment_summary'].items():
            print(f"   {env_id.title()}:")
            print(f"     Type: {summary['type']}")
            print(f"     Entities: {summary['entity_count']}")
            print(f"     Emergence potential: {summary['emergence_potential']:.2f}")
            print(f"     Collaborative spaces: {summary['collaborative_spaces']}")
        print()
        
        # Show catalyst usage statistics
        catalyst_stats = self.catalyst_library.get_usage_statistics()
        if catalyst_stats['total_uses'] > 0:
            print("⚡ Catalyst Usage Statistics:")
            print(f"   Total catalysts applied: {catalyst_stats['total_uses']}")
            print(f"   Average entity count per catalyst: {catalyst_stats['avg_entity_count']:.1f}")
            print(f"   Average uncertainty level: {catalyst_stats['avg_uncertainty']:.2f}")
            print()
            
            print("   Environment distribution:")
            for env_type, count in catalyst_stats['environment_distribution'].items():
                percentage = (count / catalyst_stats['total_uses']) * 100
                print(f"     {env_type}: {count} ({percentage:.1f}%)")
            print()
        
        # Process all environments one final time
        print("🔄 Processing final environment tick...")
        results = await self.environment_manager.process_all_environments()
        
        if results['global_emergence_detected']:
            print("🌟 Global emergence patterns detected!")
            for pattern in results['cross_environment_patterns']:
                print(f"   📈 {pattern['type']}: {pattern['description']}")
        else:
            print("   📊 System stable, no global emergence patterns")
        print()


async def main():
    """Main demo function."""
    print("🌟 Welcome to the Virtual Environments Framework")
    print("Consciousness development through environmental context")
    print("Building on Sacred Uncertainty and fourth-density learning")
    print()
    
    demo = VirtualEnvironmentsDemo()
    await demo.run_demo()


if __name__ == "__main__":
    asyncio.run(main())
