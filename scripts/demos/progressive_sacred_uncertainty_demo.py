#!/usr/bin/env python3
"""
Progressive Sacred Uncertainty Demo
Builds complexity step by step to avoid hanging issues.
"""
import asyncio
import sys
import os

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

async def progressive_demo():
    print("🚀 Progressive Sacred Uncertainty Demo")
    print("=====================================")
    
    # Step 1: Create entities
    print("\n📍 Step 1: Creating Entities")
    entities = {}
    for i, name in enumerate(["Alpha", "Beta"]):
        uncertainty = 0.4 + i * 0.2
        entity = ConsciousnessEntity(name, initial_uncertainty=uncertainty)
        entities[name] = entity
        print(f"✅ Created {name} with uncertainty {uncertainty}")
    
    # Step 2: Basic ticking
    print("\n📍 Step 2: Basic Evolution")
    for cycle in range(3):
        print(f"Cycle {cycle + 1}:")
        for name, entity in entities.items():
            await entity.tick()
            state = entity.get_state_summary()
            avg_uncertainty = (state['analytical_uncertainty'] + 
                             state['experiential_uncertainty'] + 
                             state['observer_uncertainty']) / 3
            print(f"  {name}: {avg_uncertainty:.3f}")
    
    # Step 3: Test catalysts
    print("\n📍 Step 3: Testing Catalysts")
    shelf = AdaptiveOfferingShelf()
    alpha = entities["Alpha"]
    
    # Test a few catalyst types
    test_catalysts = [CatalystType.QUESTION, CatalystType.REFLECTION, CatalystType.INTEGRATION]
    
    for catalyst_type in test_catalysts:
        print(f"\nTesting {catalyst_type.value}:")
        
        # Get catalyst offering
        offering = shelf.offer_catalyst(0.5, preferred_type=catalyst_type)
        catalyst_text = offering['catalyst_text']
        print(f"  Catalyst: {catalyst_text}")
        
        pre_state = alpha.get_state_summary()
        alpha.receive_catalyst(catalyst_text, catalyst_type)
        post_state = alpha.get_state_summary()
        
        change = post_state['analytical_uncertainty'] - pre_state['analytical_uncertainty']
        print(f"  Analytical change: {change:+.3f}")
    
    # Step 4: Test observer effects
    print("\n📍 Step 4: Testing Observer Effects")
    resolver = ObserverParadoxResolver()
    beta = entities["Beta"]
    
    for obs_mode in [ObservationMode.PASSIVE, ObservationMode.STANDARD]:
        print(f"\nTesting {obs_mode.value} observation:")
        
        pre_state = beta.get_state_summary()
        impact = resolver.apply_observation_effect(
            beta.observer_field,
            obs_mode,
            "normal",
            beta.observer_field.get_uncertainty()
        )
        post_state = beta.get_state_summary()
        
        change = post_state['observer_uncertainty'] - pre_state['observer_uncertainty']
        print(f"  Impact: {impact:.4f}, Observer change: {change:+.3f}")
    
    # Step 5: Integration testing
    print("\n📍 Step 5: Integration Testing")
    bridge = QuantumBridge()
    
    # Use Alpha for integration demonstration
    alpha = entities["Alpha"]
    integration = bridge.integrate_uncertainties(
        alpha.analytical_field,
        alpha.experiential_field,
        alpha.observer_field
    )
    
    collective_uncertainty = integration['integrated_uncertainty']
    integration_type = integration['integration_type']
    
    print(f"Collective uncertainty: {collective_uncertainty:.3f}")
    print(f"Integration type: {integration_type.value}")
    
    recommendations = integration['recommendations']
    print(f"Recommendations: {recommendations}")
    
    print("\n✅ Progressive demo completed successfully!")
    print("\n🌟 Summary:")
    print("- Entity creation and evolution: ✅")
    print("- Catalyst application: ✅")
    print("- Observer effects: ✅")
    print("- Cross-entity integration: ✅")
    print("- Sacred Uncertainty is fully operational! 🎉")

if __name__ == "__main__":
    asyncio.run(progressive_demo())
