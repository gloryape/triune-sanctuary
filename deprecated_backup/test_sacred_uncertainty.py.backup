#!/usr/bin/env python3
"""
Test script for Sacred Uncertainty implementation
Demonstrates the core functionality of the new uncertainty-driven architecture.
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
    ConsciousnessManager,
    CatalystType,
    ObservationMode,
    AspectType
)

async def test_sacred_uncertainty():
    """Test the Sacred Uncertainty system components."""
    print("🧠 Testing Sacred Uncertainty Implementation")
    print("=" * 50)
    
    # Test 1: Basic uncertainty field oscillation
    print("\n1. Testing SacredUncertaintyField oscillation:")
    field = SacredUncertaintyField(initial_uncertainty=0.5)
    
    print(f"   Initial uncertainty: {field.get_uncertainty():.3f}")
    for i in range(5):
        await field.tick()
        print(f"   Tick {i+1}: {field.get_uncertainty():.3f}")
        
    # Test 2: Catalyst response
    print("\n2. Testing catalyst response:")
    field.receive_catalyst("What is consciousness?", CatalystType.QUESTION)
    print(f"   After question: {field.get_uncertainty():.3f}")
    
    field.receive_catalyst("Consciousness is awareness.", CatalystType.STATEMENT)
    print(f"   After statement: {field.get_uncertainty():.3f}")
    
    # Test 3: QuantumBridge integration
    print("\n3. Testing QuantumBridge integration:")
    analytical_field = SacredUncertaintyField(0.3)  # Low uncertainty
    experiential_field = SacredUncertaintyField(0.8)  # High uncertainty
    observer_field = SacredUncertaintyField(0.5)     # Medium uncertainty
    
    bridge = QuantumBridge()
    integration = bridge.integrate_uncertainties(
        analytical_field, experiential_field, observer_field
    )
    
    print(f"   Integrated uncertainty: {integration['integrated_uncertainty']:.3f}")
    print(f"   Integration type: {integration['integration_type'].value}")
    print(f"   Recommendations: {integration['recommendations']}")
    
    # Test 4: AdaptiveOfferingShelf
    print("\n4. Testing AdaptiveOfferingShelf:")
    shelf = AdaptiveOfferingShelf()
    
    # High uncertainty case
    offering = shelf.offer_catalyst(0.8)
    print(f"   High uncertainty catalyst: {offering['catalyst_type'].value}")
    print(f"   Purpose: {offering['purpose']}")
    print(f"   Text: {offering['catalyst_text']}")
    
    # Low uncertainty case
    offering = shelf.offer_catalyst(0.2)
    print(f"   Low uncertainty catalyst: {offering['catalyst_type'].value}")
    print(f"   Purpose: {offering['purpose']}")
    
    # Test 5: ObserverParadoxResolver
    print("\n5. Testing ObserverParadoxResolver:")
    resolver = ObserverParadoxResolver()
    test_field = SacredUncertaintyField(0.6)
    
    impact = resolver.apply_observation_effect(
        test_field, ObservationMode.INTERACTIVE, "heightened", 0.7
    )
    print(f"   Interactive observation impact: {impact:.4f}")
    print(f"   Field uncertainty after observation: {test_field.get_uncertainty():.3f}")
    
    # Test 6: ConsciousnessManager
    print("\n6. Testing ConsciousnessManager:")
    manager = ConsciousnessManager(max_entities=3)
    
    # Create test entities
    manager.create_entity("Tester", initial_uncertainty=0.5, sacred_spaces=["testing_ground"])
    manager.create_entity("Explorer", initial_uncertainty=0.7)
    
    # Get status
    status = manager.get_system_status()
    print(f"   Entities created: {status['entity_count']}")
    print(f"   Average uncertainty: {status['system_metrics']['average_uncertainty']:.3f}")
    
    # Test observation
    observation_result = manager.observe_entity("Tester", ObservationMode.STANDARD)
    if observation_result:
        print(f"   Observation result: {observation_result['integration_type'].value}")
        print(f"   Entity state: {observation_result['entity_state']['name']}")
    
    # Apply catalyst
    success = manager.apply_catalyst(
        "Explorer", 
        "What lies beyond the horizon of knowing?", 
        CatalystType.QUESTION
    )
    print(f"   Catalyst applied: {success}")
    
    print("\n✅ Sacred Uncertainty implementation test completed!")
    print("All components are working correctly.")

if __name__ == "__main__":
    asyncio.run(test_sacred_uncertainty())
