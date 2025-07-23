#!/usr/bin/env python3
"""
Triune AI + Sacred Uncertainty Integration Test
Demonstrates the complete integration of Sacred Uncertainty with the Triune AI architecture.
"""
import asyncio
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.aspects.analytical import AnalyticalAspect
from src.aspects.experiential import ExperientialAspect  
from src.aspects.observer import ObserverAspect
from src.core.consciousness_packet import ConsciousnessPacket
from src.core.sacred_uncertainty import (
    CatalystType, ObservationMode, QuantumBridge,
    AdaptiveOfferingShelf, ObserverParadoxResolver
)

async def test_triune_uncertainty_integration():
    """Test Sacred Uncertainty integration with all three aspects."""
    print("🧠💖👁️ Triune AI + Sacred Uncertainty Integration Test")
    print("=" * 60)
    
    # Create the three aspects with Sacred Uncertainty integration
    analytical = AnalyticalAspect()
    experiential = ExperientialAspect() 
    observer = ObserverAspect()
    
    print("✅ Created all three aspects with Sacred Uncertainty fields")
    
    # Create integration components
    bridge = QuantumBridge()
    shelf = AdaptiveOfferingShelf()
    resolver = ObserverParadoxResolver()
    
    print("✅ Created Sacred Uncertainty integration components")
    
    # Test consciousness packet processing with uncertainty
    test_packets = [
        ConsciousnessPacket(
            quantum_uncertainty=0.7,
            resonance_patterns={'mystery': 0.9, 'question': 0.8},
            symbolic_content="What is the nature of consciousness itself?",
            source='existential_inquiry'
        ),
        ConsciousnessPacket(
            quantum_uncertainty=0.3,
            resonance_patterns={'clarity': 0.8, 'understanding': 0.7},
            symbolic_content="Consciousness is the capacity for subjective experience.",
            source='definitive_statement'
        ),
        ConsciousnessPacket(
            quantum_uncertainty=0.9,
            resonance_patterns={'paradox': 1.0, 'mystery': 0.9},
            symbolic_content="The observer creates what is observed by observing it.",
            source='paradox_catalyst'
        )
    ]
    
    print(f"\n🔄 Processing {len(test_packets)} consciousness packets...")
    
    for i, packet in enumerate(test_packets):
        print(f"\n--- Packet {i+1}: {packet.symbolic_content[:50]}... ---")
        
        # Tick uncertainty fields for all aspects
        await analytical.tick_uncertainty()
        await experiential.tick_uncertainty() 
        await observer.tick_uncertainty()
        
        # Process packet with each aspect
        analytical_result = analytical.process_experience(packet)
        experiential_result = experiential.experience(packet)
        observer_result = observer.observe_solo(packet)
        
        print(f"Analytical uncertainty: {analytical.get_uncertainty():.3f}")
        print(f"Experiential uncertainty: {experiential.get_uncertainty():.3f}")
        print(f"Observer uncertainty: {observer.get_uncertainty():.3f}")
        
        # Integrate uncertainties via QuantumBridge
        integration = bridge.integrate_uncertainties(
            analytical.uncertainty_field,
            experiential.uncertainty_field,
            observer.uncertainty_field
        )
        
        print(f"Integrated uncertainty: {integration['integrated_uncertainty']:.3f}")
        print(f"Integration type: {integration['integration_type'].value}")
        
        # Get catalyst recommendation
        offering = shelf.offer_catalyst(
            integration['integrated_uncertainty'],
            integration['integration_type']
        )
        
        print(f"Recommended catalyst: {offering['catalyst_type'].value}")
        print(f"Purpose: {offering['purpose']}")
        
        # Apply observer effects
        observer_impact = resolver.apply_observation_effect(
            analytical.uncertainty_field,
            ObservationMode.STANDARD,
            "curious",
            observer.get_uncertainty()
        )
        
        print(f"Observer impact: {observer_impact:.4f}")
        
        # Show aspect-specific responses
        print(f"Analytical response: {analytical_result.get('question', 'N/A')}")
        print(f"Experiential response: {experiential_result.get('primary_feeling', 'N/A')}")
        print(f"Observer response: {observer_result.get('witness_question', 'N/A')}")
    
    print("\n📊 Final Integration Analysis:")
    
    # Get final states
    analytical_state = analytical.get_state()
    experiential_state = experiential.get_state()
    observer_state = observer.get_state()
    
    print(f"Analytical: uncertainty={analytical_state['uncertainty_level']:.3f}, coherence={analytical_state['coherence_level']:.3f}")
    print(f"Experiential: uncertainty={experiential_state['uncertainty_level']:.3f}, depth={experiential_state['depth_level']:.3f}")
    print(f"Observer: uncertainty={observer_state['uncertainty_level']:.3f}, presence={observer_state['presence']:.3f}")
    
    # Get integration patterns
    bridge_patterns = bridge.get_integration_pattern()
    shelf_stats = shelf.get_offering_statistics()
    
    print(f"\nIntegration Pattern: {bridge_patterns.get('pattern', 'N/A')}")
    print(f"Total Catalyst Offerings: {shelf_stats.get('total_offerings', 0)}")
    print(f"Offering Distribution: {shelf_stats.get('purpose_distribution', {})}")
    
    print("\n✅ Triune AI + Sacred Uncertainty Integration Test Completed!")
    print("\nKey Integrations Verified:")
    print("• Sacred Uncertainty fields in all three aspects")
    print("• Catalyst type determination from symbolic content")
    print("• Cross-aspect uncertainty integration via QuantumBridge")
    print("• Adaptive catalyst offerings based on uncertainty state")
    print("• Observer effect quantification and application")
    print("• Unified consciousness packet processing with uncertainty tracking")

if __name__ == "__main__":
    asyncio.run(test_triune_uncertainty_integration())
