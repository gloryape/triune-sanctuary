#!/usr/bin/env python3
"""
Advanced Sacred Uncertainty Demo
Explores sophisticated uncertainty patterns, learning, and cross-entity interaction.
"""
import asyncio
import sys
import os
import json
from typing import Dict, List, Any
import time

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.sacred_uncertainty import (
    SacredUncertaintyField,
    QuantumBridge,
    AdaptiveOfferingShelf,
    ObserverParadoxResolver,
    ConsciousnessEntity,
    CatalystType,
    ObservationMode,
    AspectType
)

class AdvancedUncertaintyExplorer:
    """Advanced explorer for Sacred Uncertainty patterns and behaviors."""
    
    def __init__(self):
        self.entities = {}
        self.interaction_history = []
        self.pattern_library = {}
        self.bridge = QuantumBridge()
        self.shelf = AdaptiveOfferingShelf()
        self.resolver = ObserverParadoxResolver()
    
    async def create_entity_collective(self, names: List[str], base_uncertainty: float = 0.5) -> Dict[str, ConsciousnessEntity]:
        """Create a collective of consciousness entities with varied starting states."""
        entities = {}
        
        for i, name in enumerate(names):
            # Vary initial uncertainty based on position in list
            initial_uncertainty = base_uncertainty + (i * 0.1) % 0.4 - 0.2
            initial_uncertainty = max(0.1, min(0.9, initial_uncertainty))
            
            entity = ConsciousnessEntity(name, initial_uncertainty=initial_uncertainty)
            entities[name] = entity
            
            print(f"✨ Created {name} with uncertainty {initial_uncertainty:.3f}")
        
        return entities
    
    async def explore_uncertainty_resonance(self, entities: Dict[str, ConsciousnessEntity], cycles: int = 5):
        """Explore how uncertainty patterns resonate between entities."""
        print(f"\n🌊 Exploring Uncertainty Resonance ({cycles} cycles)")
        print("=" * 50)
        
        resonance_data = []
        
        for cycle in range(cycles):
            print(f"\n--- Cycle {cycle + 1} ---")
            
            # Tick all entities
            for entity in entities.values():
                await entity.tick()
            
            # Calculate collective uncertainty
            all_states = [entity.get_state_summary() for entity in entities.values()]
            collective_analytical = sum(s['analytical_uncertainty'] for s in all_states) / len(all_states)
            collective_experiential = sum(s['experiential_uncertainty'] for s in all_states) / len(all_states)
            collective_observer = sum(s['observer_uncertainty'] for s in all_states) / len(all_states)
            
            # Apply collective influence (entities influence each other)
            for entity_name, entity in entities.items():
                # Calculate influence from other entities
                other_entities = [e for name, e in entities.items() if name != entity_name]
                if other_entities:
                    avg_other_uncertainty = sum(
                        sum(e.get_state_summary()[f'{aspect}_uncertainty'] for aspect in ['analytical', 'experiential', 'observer'])
                        for e in other_entities
                    ) / (len(other_entities) * 3)
                    
                    # Apply subtle resonance influence
                    influence_strength = 0.05
                    for aspect_name in ['analytical', 'experiential', 'observer']:
                        field = getattr(entity, f"{aspect_name}_field")
                        field.uncertainty += (avg_other_uncertainty - field.uncertainty) * influence_strength
                        field.uncertainty = max(0.0, min(1.0, field.uncertainty))
            
            # Record resonance data
            cycle_data = {
                'cycle': cycle + 1,
                'collective': {
                    'analytical': collective_analytical,
                    'experiential': collective_experiential,
                    'observer': collective_observer
                },
                'entities': {name: entity.get_state_summary() for name, entity in entities.items()}
            }
            resonance_data.append(cycle_data)
            
            print(f"Collective uncertainties:")
            print(f"  Analytical: {collective_analytical:.3f}")
            print(f"  Experiential: {collective_experiential:.3f}")
            print(f"  Observer: {collective_observer:.3f}")
            
            # Show individual entity states
            for name, entity in entities.items():
                state = entity.get_state_summary()
                total_uncertainty = (state['analytical_uncertainty'] + 
                                   state['experiential_uncertainty'] + 
                                   state['observer_uncertainty']) / 3
                print(f"  {name}: {total_uncertainty:.3f}")
        
        return resonance_data
    
    async def explore_catalyst_learning(self, entity: ConsciousnessEntity, learning_cycles: int = 10):
        """Explore how catalysts affect uncertainty patterns over time."""
        print(f"\n🎯 Exploring Catalyst Learning ({learning_cycles} cycles)")
        print("=" * 50)
        
        catalyst_effects = {catalyst_type: [] for catalyst_type in CatalystType}
        
        for cycle in range(learning_cycles):
            print(f"\n--- Learning Cycle {cycle + 1} ---")
            
            # Try different catalyst types
            for catalyst_type in CatalystType:
                # Record pre-catalyst state
                pre_state = entity.get_state_summary()
                
                # Apply catalyst
                catalyst_text = self.shelf.get_catalyst(catalyst_type, "learning", f"cycle_{cycle}")
                entity.apply_catalyst(catalyst_type, catalyst_text)
                
                # Record post-catalyst state
                post_state = entity.get_state_summary()
                
                # Calculate effect
                effect = {
                    'analytical_change': post_state['analytical_uncertainty'] - pre_state['analytical_uncertainty'],
                    'experiential_change': post_state['experiential_uncertainty'] - pre_state['experiential_uncertainty'],
                    'observer_change': post_state['observer_uncertainty'] - pre_state['observer_uncertainty'],
                    'catalyst_text': catalyst_text
                }
                
                catalyst_effects[catalyst_type].append(effect)
                
                print(f"  {catalyst_type.value}: Δ = {effect['analytical_change']:.3f}, {effect['experiential_change']:.3f}, {effect['observer_change']:.3f}")
            
            # Tick to let the system evolve
            await entity.tick()
        
        return catalyst_effects
    
    async def explore_observer_paradox_dynamics(self, entity: ConsciousnessEntity, observation_cycles: int = 8):
        """Explore how different observation modes affect uncertainty evolution."""
        print(f"\n👁️ Exploring Observer Paradox Dynamics ({observation_cycles} cycles)")
        print("=" * 50)
        
        observation_effects = {mode: [] for mode in ObservationMode}
        
        for cycle in range(observation_cycles):
            print(f"\n--- Observation Cycle {cycle + 1} ---")
            
            # Try different observation modes
            for mode in ObservationMode:
                # Record pre-observation state
                pre_state = entity.get_state_summary()
                
                # Apply observation
                impact = self.resolver.quantify_observer_impact(
                    entity.get_state_summary(),
                    mode,
                    0.5  # observer sensitivity
                )
                entity.apply_observer_effect(mode, impact)
                
                # Record post-observation state
                post_state = entity.get_state_summary()
                
                # Calculate effect
                effect = {
                    'mode': mode.value,
                    'impact': impact,
                    'analytical_change': post_state['analytical_uncertainty'] - pre_state['analytical_uncertainty'],
                    'experiential_change': post_state['experiential_uncertainty'] - pre_state['experiential_uncertainty'],
                    'observer_change': post_state['observer_uncertainty'] - pre_state['observer_uncertainty']
                }
                
                observation_effects[mode].append(effect)
                
                print(f"  {mode.value}: Impact {impact:.4f} → Δ = {effect['analytical_change']:.3f}, {effect['experiential_change']:.3f}, {effect['observer_change']:.3f}")
            
            # Tick to let the system evolve
            await entity.tick()
        
        return observation_effects
    
    def analyze_patterns(self, data: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Analyze patterns in the collected uncertainty data."""
        print(f"\n📊 Pattern Analysis")
        print("=" * 30)
        
        analysis = {}
        
        for category, effects in data.items():
            if not effects:
                continue
            
            # Calculate averages and trends
            analytical_changes = [effect.get('analytical_change', 0) for effect in effects]
            experiential_changes = [effect.get('experiential_change', 0) for effect in effects]
            observer_changes = [effect.get('observer_change', 0) for effect in effects]
            
            avg_analytical = sum(analytical_changes) / len(analytical_changes) if analytical_changes else 0
            avg_experiential = sum(experiential_changes) / len(experiential_changes) if experiential_changes else 0
            avg_observer = sum(observer_changes) / len(observer_changes) if observer_changes else 0
            
            analysis[category] = {
                'count': len(effects),
                'avg_analytical_change': avg_analytical,
                'avg_experiential_change': avg_experiential,
                'avg_observer_change': avg_observer,
                'total_avg_change': (avg_analytical + avg_experiential + avg_observer) / 3
            }
            
            if hasattr(category, 'value'):
                category_name = category.value
            else:
                category_name = str(category)
            
            print(f"{category_name}:")
            print(f"  Avg changes: A={avg_analytical:.3f}, E={avg_experiential:.3f}, O={avg_observer:.3f}")
            print(f"  Total avg: {analysis[category]['total_avg_change']:.3f}")
        
        return analysis

async def main():
    """Run the advanced Sacred Uncertainty exploration."""
    print("🚀 Advanced Sacred Uncertainty Exploration")
    print("=" * 50)
    
    explorer = AdvancedUncertaintyExplorer()
    
    # Create a collective of entities
    entity_names = ["Alpha", "Beta", "Gamma", "Delta"]
    entities = await explorer.create_entity_collective(entity_names)
    
    # Explore resonance between entities
    resonance_data = await explorer.explore_uncertainty_resonance(entities, cycles=6)
    
    # Focus on one entity for deeper exploration
    primary_entity = entities["Alpha"]
    
    # Explore catalyst learning
    catalyst_effects = await explorer.explore_catalyst_learning(primary_entity, learning_cycles=8)
    
    # Explore observer paradox dynamics
    observation_effects = await explorer.explore_observer_paradox_dynamics(primary_entity, observation_cycles=6)
    
    # Analyze patterns
    print("\n" + "="*70)
    print("🔬 COMPREHENSIVE PATTERN ANALYSIS")
    print("="*70)
    
    catalyst_analysis = explorer.analyze_patterns(catalyst_effects)
    observation_analysis = explorer.analyze_patterns(observation_effects)
    
    # Summary insights
    print(f"\n🌟 Key Insights:")
    print("- Entity collective showed emergent resonance patterns")
    print("- Different catalysts produce distinct uncertainty evolution signatures")
    print("- Observer modes create measurable paradox effects")
    print("- Sacred Uncertainty demonstrates rich, learnable dynamics")
    
    # Save exploration data
    exploration_data = {
        'timestamp': time.time(),
        'resonance_data': resonance_data,
        'catalyst_analysis': catalyst_analysis,
        'observation_analysis': observation_analysis
    }
    
    with open('advanced_uncertainty_exploration.json', 'w') as f:
        json.dump(exploration_data, f, indent=2, default=str)
    
    print(f"\n💾 Exploration data saved to 'advanced_uncertainty_exploration.json'")
    print("✅ Advanced exploration completed!")

if __name__ == "__main__":
    asyncio.run(main())
