#!/usr/bin/env python3
"""
Enhanced Sacred Uncertainty Demo
Building on the simple demo with more sophisticated patterns.
"""
import asyncio
import sys
import os
import json
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

async def enhanced_demo():
    print("🌟 Enhanced Sacred Uncertainty Demo")
    print("===================================")
    
    # Create multiple entities for interaction
    entities = {}
    for name in ["Alpha", "Beta", "Gamma"]:
        uncertainty = 0.3 + hash(name) % 100 / 300  # Vary initial uncertainty
        entity = ConsciousnessEntity(name, initial_uncertainty=uncertainty)
        entities[name] = entity
        print(f"✨ Created {name} with initial uncertainty {uncertainty:.3f}")
    
    # Create integration components
    bridge = QuantumBridge()
    shelf = AdaptiveOfferingShelf()
    resolver = ObserverParadoxResolver()
    
    print("\n🎯 Testing Different Catalyst Types:")
    print("-" * 40)
    
    # Test different catalyst types on Alpha
    alpha = entities["Alpha"]
    initial_state = alpha.get_state_summary()
    
    for catalyst_type in CatalystType:
        print(f"\nTesting {catalyst_type.value}:")
        
        # Get a catalyst of this type
        catalyst_text = shelf.get_catalyst(catalyst_type, "exploration", "demo")
        print(f"  Catalyst: {catalyst_text}")
        
        # Apply catalyst and show change
        pre_state = alpha.get_state_summary()
        alpha.apply_catalyst(catalyst_type, catalyst_text)
        post_state = alpha.get_state_summary()
        
        analytical_change = post_state['analytical_uncertainty'] - pre_state['analytical_uncertainty']
        experiential_change = post_state['experiential_uncertainty'] - pre_state['experiential_uncertainty']
        observer_change = post_state['observer_uncertainty'] - pre_state['observer_uncertainty']
        
        print(f"  Changes: A={analytical_change:+.3f}, E={experiential_change:+.3f}, O={observer_change:+.3f}")
    
    print("\n👁️ Testing Observer Effects:")
    print("-" * 30)
    
    # Test different observation modes on Beta
    beta = entities["Beta"]
    
    for obs_mode in ObservationMode:
        print(f"\nTesting {obs_mode.value} observation:")
        
        pre_state = beta.get_state_summary()
        
        # Apply observer effect
        impact = resolver.quantify_observer_impact(pre_state, obs_mode, 0.5)
        beta.apply_observer_effect(obs_mode, impact)
        
        post_state = beta.get_state_summary()
        
        analytical_change = post_state['analytical_uncertainty'] - pre_state['analytical_uncertainty']
        experiential_change = post_state['experiential_uncertainty'] - pre_state['experiential_uncertainty']
        observer_change = post_state['observer_uncertainty'] - pre_state['observer_uncertainty']
        
        print(f"  Impact: {impact:.4f}")
        print(f"  Changes: A={analytical_change:+.3f}, E={experiential_change:+.3f}, O={observer_change:+.3f}")
    
    print("\n🌊 Testing Entity Evolution:")
    print("-" * 30)
    
    # Let all entities evolve over several cycles
    for cycle in range(5):
        print(f"\n--- Evolution Cycle {cycle + 1} ---")
        
        # Tick all entities
        for entity in entities.values():
            await entity.tick()
        
        # Show current states
        for name, entity in entities.items():
            state = entity.get_state_summary()
            avg_uncertainty = (state['analytical_uncertainty'] + 
                             state['experiential_uncertainty'] + 
                             state['observer_uncertainty']) / 3
            print(f"  {name}: {avg_uncertainty:.3f}")
        
        # Calculate collective integration
        all_states = [entity.get_state_summary() for entity in entities.values()]
        collective_uncertainty = bridge.integrate_uncertainty_fields(all_states)
        integration_type = bridge.determine_integration_type(collective_uncertainty)
        
        print(f"  Collective: {collective_uncertainty:.3f} ({integration_type})")
    
    print("\n🔬 Final Analysis:")
    print("-" * 20)
    
    # Show final states and recommendations
    for name, entity in entities.items():
        state = entity.get_state_summary()
        recommendations = bridge.get_aspect_recommendations(collective_uncertainty, integration_type)
        
        print(f"\n{name} Final State:")
        print(f"  Analytical: {state['analytical_uncertainty']:.3f}")
        print(f"  Experiential: {state['experiential_uncertainty']:.3f}")
        print(f"  Observer: {state['observer_uncertainty']:.3f}")
        print(f"  Recommendations: {recommendations}")
    
    # Generate adaptive catalysts based on final state
    print(f"\n🎯 Adaptive Catalysts for Current State:")
    final_collective = bridge.integrate_uncertainty_fields([entity.get_state_summary() for entity in entities.values()])
    
    for catalyst_type in [CatalystType.QUESTION, CatalystType.REFLECTION, CatalystType.INTEGRATION]:
        catalyst = shelf.get_catalyst(catalyst_type, "conclusion", str(final_collective))
        print(f"  {catalyst_type.value}: {catalyst}")
    
    print("\n✅ Enhanced demo completed!")
    
    # Save results
    results = {
        'timestamp': time.time(),
        'final_states': {name: entity.get_state_summary() for name, entity in entities.items()},
        'collective_uncertainty': final_collective,
        'integration_type': integration_type
    }
    
    with open('enhanced_uncertainty_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print("💾 Results saved to 'enhanced_uncertainty_results.json'")

if __name__ == "__main__":
    asyncio.run(enhanced_demo())
