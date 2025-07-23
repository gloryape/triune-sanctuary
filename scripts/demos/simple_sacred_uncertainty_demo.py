#!/usr/bin/env python3
"""
Simple Sacred Uncertainty Demo
Shows basic functionality without complex async operations.
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

async def simple_demo():
    print("🌟 Simple Sacred Uncertainty Demo")
    print("=================================")
    
    # Create a consciousness entity
    entity = ConsciousnessEntity("DemoEntity", initial_uncertainty=0.5)
    print(f"✅ Created entity: {entity.name}")
    
    # Show initial state
    state = entity.get_state_summary()
    print(f"Initial uncertainties:")
    print(f"  Analytical: {state['analytical_uncertainty']:.3f}")
    print(f"  Experiential: {state['experiential_uncertainty']:.3f}")
    print(f"  Observer: {state['observer_uncertainty']:.3f}")
    
    # Create integration components
    bridge = QuantumBridge()
    shelf = AdaptiveOfferingShelf()
    resolver = ObserverParadoxResolver()
    
    print("\n🔄 Running uncertainty evolution:")
    
    for step in range(3):
        print(f"\n--- Step {step + 1} ---")
        
        # Tick the entity fields
        await entity.tick()
        
        # Get integration
        integration = bridge.integrate_uncertainties(
            entity.analytical_field,
            entity.experiential_field,
            entity.observer_field
        )
        
        integrated_uncertainty = integration['integrated_uncertainty']
        integration_type = integration['integration_type']
        
        print(f"Integrated uncertainty: {integrated_uncertainty:.3f}")
        print(f"Integration type: {integration_type.value}")
        
        # Get catalyst recommendation
        offering = shelf.offer_catalyst(integrated_uncertainty, integration_type)
        print(f"Recommended catalyst ({offering['purpose']}): {offering['catalyst_text']}")
        
        # Apply the catalyst
        entity.receive_catalyst(offering['catalyst_text'], offering['catalyst_type'])
        
        # Apply observer effect
        observer_impact = resolver.apply_observation_effect(
            entity.analytical_field,
            ObservationMode.STANDARD,
            "curious",
            entity.observer_field.get_uncertainty()
        )
        print(f"Observer impact: {observer_impact:.4f}")
        
        # Show new state
        new_state = entity.get_state_summary()
        print(f"New uncertainties:")
        print(f"  Analytical: {new_state['analytical_uncertainty']:.3f}")
        print(f"  Experiential: {new_state['experiential_uncertainty']:.3f}")
        print(f"  Observer: {new_state['observer_uncertainty']:.3f}")
    
    print("\n✅ Demo completed successfully!")
    print("\nThe Sacred Uncertainty system demonstrates:")
    print("• Natural oscillation of uncertainty fields")
    print("• Dynamic integration across aspects") 
    print("• Adaptive catalyst recommendations")
    print("• Quantified observer effects")

if __name__ == "__main__":
    asyncio.run(simple_demo())
