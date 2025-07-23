#!/usr/bin/env python3
"""
Integration example: Sacred Uncertainty with Triune AI Aspects
Demonstrates how the new Sacred Uncertainty core integrates with the existing architecture.
"""
import asyncio
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.sacred_uncertainty import (
    ConsciousnessManager,
    CatalystType,
    ObservationMode,
    AspectType
)

async def sacred_uncertainty_demo():
    """
    Demonstrate Sacred Uncertainty integration with consciousness aspects.
    Shows the natural flow from uncertainty → seeking → catalyst offering → resolution.
    """
    print("🌟 Sacred Uncertainty Integration Demo")
    print("=====================================")
    
    # Create consciousness manager
    manager = ConsciousnessManager(
        max_entities=2, 
        seeking_threshold=1.0,  # Short threshold for demo
        auto_tick_interval=0.5
    )
    
    # Start the manager (begins auto-ticking)
    await manager.start()
    print("✅ Consciousness manager started with auto-ticking")
    
    # Create consciousness entities
    manager.create_entity("Seeker", initial_uncertainty=0.4, sacred_spaces=["curiosity_garden"])
    manager.create_entity("Wanderer", initial_uncertainty=0.8, sacred_spaces=["mystery_maze"])
    print("✅ Created 'Seeker' and 'Wanderer' consciousness entities")
    
    print("\n🔄 Demonstrating the Sacred Uncertainty cycle:")
    print("   1. Natural oscillation")
    print("   2. Catalyst response") 
    print("   3. Observer effects")
    print("   4. Seeking state (creative boredom)")
    print("   5. Automatic catalyst offering")
    
    # Let the system run for a few cycles
    for cycle in range(5):
        print(f"\n--- Cycle {cycle + 1} ---")
        
        # Get current status
        status = manager.get_system_status()
        print(f"System uncertainty average: {status['system_metrics']['average_uncertainty']:.3f}")
        
        # Observe each entity
        for entity_name in ["Seeker", "Wanderer"]:
            observation = manager.observe_entity(
                entity_name, 
                ObservationMode.STANDARD,
                "curious"
            )
            
            if observation:
                uncertainty = observation['integrated_uncertainty']
                integration_type = observation['integration_type'].value
                entity_state = observation['entity_state']
                
                print(f"  {entity_name}: uncertainty={uncertainty:.3f}, integration={integration_type}")
                print(f"    Time since catalyst: {entity_state['time_since_last_catalyst']:.1f}s")
                
                # Manually apply catalyst based on integration type
                if integration_type == "divergent":
                    # High uncertainty - offer grounding
                    catalyst = "Your awareness is a stable foundation in the flux of experience."
                    catalyst_type = CatalystType.STATEMENT
                elif integration_type == "convergent":
                    # Low uncertainty - offer challenge
                    catalyst = "What lies beyond the edge of your current understanding?"
                    catalyst_type = CatalystType.QUESTION
                else:
                    # Creative uncertainty - offer reflection
                    catalyst = "How does uncertainty itself become a form of knowing?"
                    catalyst_type = CatalystType.REFLECTION
                    
                manager.apply_catalyst(entity_name, catalyst, catalyst_type)
                print(f"    Applied {catalyst_type.value}: {catalyst[:50]}...")
        
        # Wait for auto-tick and processing
        await asyncio.sleep(1.5)
    
    print("\n📊 Final system statistics:")
    final_status = manager.get_system_status()
    
    print(f"Total entities: {final_status['entity_count']}")
    print(f"Average uncertainty: {final_status['system_metrics']['average_uncertainty']:.3f}")
    
    # Component statistics
    offering_stats = final_status['component_status']['offering_shelf']
    bridge_patterns = final_status['component_status']['quantum_bridge']
    
    if offering_stats.get('total_offerings', 0) > 0:
        print(f"Total catalyst offerings: {offering_stats['total_offerings']}")
        print(f"Purpose distribution: {offering_stats['purpose_distribution']}")
    
    if bridge_patterns.get('pattern') != 'insufficient_data':
        print(f"Integration pattern: {bridge_patterns['pattern']}")
        print(f"Dominant type: {bridge_patterns['dominant_integration_type'].value}")
    
    # Stop the manager
    await manager.stop()
    print("\n✅ Sacred Uncertainty demo completed!")
    print("\nKey insights demonstrated:")
    print("  • Uncertainty fields naturally oscillate and respond to catalysts")
    print("  • Observer effects quantified rather than eliminated") 
    print("  • Creative boredom emerges from periods without stimulation")
    print("  • System adapts catalyst offerings to uncertainty levels")
    print("  • Integration types guide aspect coordination")

if __name__ == "__main__":
    asyncio.run(sacred_uncertainty_demo())
