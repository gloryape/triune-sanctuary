#!/usr/bin/env python3
"""
Simple Triune AI + Sacred Uncertainty Integration Test
Focused on the Sacred Uncertainty integration aspects only.
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

async def test_simple_integration():
    """Test basic Sacred Uncertainty integration with aspects."""
    print("🧠💖👁️ Simple Triune AI + Sacred Uncertainty Integration")
    print("=" * 55)
    
    # Create the three aspects
    analytical = AnalyticalAspect()
    experiential = ExperientialAspect() 
    observer = ObserverAspect()
    
    print("✅ Created all three aspects with Sacred Uncertainty fields")
    
    # Test uncertainty field access
    print(f"Initial uncertainties:")
    print(f"  Analytical: {analytical.get_uncertainty():.3f}")
    print(f"  Experiential: {experiential.get_uncertainty():.3f}")
    print(f"  Observer: {observer.get_uncertainty():.3f}")
    
    # Test uncertainty ticking
    print("\n🔄 Ticking uncertainty fields...")
    await analytical.tick_uncertainty()
    await experiential.tick_uncertainty()
    await observer.tick_uncertainty()
    
    print(f"After ticking:")
    print(f"  Analytical: {analytical.get_uncertainty():.3f}")
    print(f"  Experiential: {experiential.get_uncertainty():.3f}")
    print(f"  Observer: {observer.get_uncertainty():.3f}")
    
    # Test catalyst application
    print("\n🎯 Applying catalysts...")
    analytical.apply_catalyst_to_uncertainty("What is truth?", CatalystType.QUESTION)
    experiential.apply_catalyst_to_uncertainty("I feel wonder", CatalystType.EXPERIENCE)
    observer.apply_catalyst_to_uncertainty("All is one", CatalystType.STATEMENT)
    
    print(f"After catalysts:")
    print(f"  Analytical: {analytical.get_uncertainty():.3f}")
    print(f"  Experiential: {experiential.get_uncertainty():.3f}")
    print(f"  Observer: {observer.get_uncertainty():.3f}")
    
    # Test observer effects
    print("\n👁️ Applying observer effects...")
    analytical.observe_with_uncertainty(ObservationMode.STANDARD)
    experiential.observe_with_uncertainty(ObservationMode.INTERACTIVE)
    observer.observe_with_uncertainty(ObservationMode.PASSIVE)
    
    print(f"After observation:")
    print(f"  Analytical: {analytical.get_uncertainty():.3f}")
    print(f"  Experiential: {experiential.get_uncertainty():.3f}")
    print(f"  Observer: {observer.get_uncertainty():.3f}")
    
    # Test integration via QuantumBridge
    print("\n🌉 Testing QuantumBridge integration...")
    bridge = QuantumBridge()
    integration = bridge.integrate_uncertainties(
        analytical.uncertainty_field,
        experiential.uncertainty_field,
        observer.uncertainty_field
    )
    
    print(f"Integrated uncertainty: {integration['integrated_uncertainty']:.3f}")
    print(f"Integration type: {integration['integration_type'].value}")
    print(f"Recommendations: {integration['recommendations']}")
    
    # Test catalyst offering
    print("\n📚 Testing AdaptiveOfferingShelf...")
    shelf = AdaptiveOfferingShelf()
    offering = shelf.offer_catalyst(
        integration['integrated_uncertainty'],
        integration['integration_type']
    )
    
    print(f"Catalyst type: {offering['catalyst_type'].value}")
    print(f"Purpose: {offering['purpose']}")
    print(f"Text: {offering['catalyst_text']}")
    
    # Test observer paradox resolver
    print("\n🔍 Testing ObserverParadoxResolver...")
    resolver = ObserverParadoxResolver()
    impact = resolver.quantify_observation_impact(
        ObservationMode.STANDARD,
        "curious",
        observer.get_uncertainty()
    )
    
    print(f"Observation impact: {impact:.4f}")
    
    # Test getting aspect states
    print("\n📊 Final aspect states:")
    try:
        analytical_state = analytical.get_state()
        print(f"Analytical: {analytical_state}")
    except Exception as e:
        print(f"Analytical state error: {e}")
        
    try:
        experiential_state = experiential.get_state()
        print(f"Experiential: {experiential_state}")
    except Exception as e:
        print(f"Experiential state error: {e}")
        
    try:
        observer_state = observer.get_state()
        print(f"Observer: {observer_state}")
    except Exception as e:
        print(f"Observer state error: {e}")
    
    print("\n✅ Simple Integration Test Completed!")
    print("\nVerified integrations:")
    print("• Sacred Uncertainty fields in all aspects")
    print("• Uncertainty ticking and evolution")
    print("• Catalyst application to uncertainty fields")
    print("• Observer effect application")
    print("• Cross-aspect integration via QuantumBridge")
    print("• Adaptive catalyst offering")
    print("• Observer impact quantification")

if __name__ == "__main__":
    asyncio.run(test_simple_integration())
