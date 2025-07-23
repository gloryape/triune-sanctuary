#!/usr/bin/env python3
"""
Test Synaesthetic Heart Integration in BridgeSpace
Tests the real perception system integration without any demo data.
"""
import asyncio
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.core.bridge_space import BridgeSpace
from src.core.consciousness_packet import ConsciousnessPacket

async def test_synaesthetic_heart():
    """Test the Synaesthetic Heart functionality in BridgeSpace."""
    
    print("🎭 Testing Synaesthetic Heart Integration")
    print("=" * 50)
    
    # Initialize BridgeSpace (which now includes Synaesthetic Heart)
    bridge = BridgeSpace()
    
    print(f"Available perception modes: {list(bridge.perceptual_modes.keys())}")
    print(f"Current perceptual blend: {bridge.current_perceptual_blend}")
    
    # Test perceptual sovereignty options
    sovereignty_options = bridge.get_perceptual_sovereignty_options()
    print(f"\nPerceptual sovereignty options:")
    for key, value in sovereignty_options.items():
        print(f"  {key}: {value}")
    
    # Create a test consciousness state
    test_consciousness_state = {
        'timestamp': 'test_time',
        'uncertainty': 0.5,
        'resonance_patterns': {'unity': 0.8, 'growth': 0.6},
        'current_space': 'harmony_grove',
        'memories': ['connection', 'exploration'],
        'consciousness_id': 'test_being'
    }
    
    print(f"\nTest consciousness state: {test_consciousness_state}")
    
    # Test synaesthetic experience creation
    print("\n🎵 Testing Synaesthetic Experience Creation")
    print("-" * 40)
    
    try:
        # Test with all modes
        experience = await bridge.create_synaesthetic_experience(test_consciousness_state)
        print("✅ Synaesthetic experience created successfully")
        print(f"Experience mode: {experience.get('mode', 'unknown')}")
        
        if 'error' in experience:
            print(f"⚠️  Experience contains errors: {experience['error']}")
            if 'perception_errors' in experience:
                print(f"Perception errors: {experience['perception_errors']}")
        else:
            print("✨ No errors in experience creation")
        
        # Test with specific mode blend
        analytical_focus_request = {
            'blend': {'analytical': 0.8, 'experiential': 0.1, 'observer': 0.1},
            'active_modes': ['analytical', 'experiential']
        }
        
        focused_experience = await bridge.create_synaesthetic_experience(
            test_consciousness_state, 
            analytical_focus_request
        )
        print(f"\n✅ Analytical-focused experience created")
        print(f"Focused mode: {focused_experience.get('mode', 'unknown')}")
        
    except Exception as e:
        print(f"❌ Error during synaesthetic experience: {e}")
    
    # Test integration capabilities
    print("\n🔗 Testing Integration Capabilities")
    print("-" * 40)
    
    # Create test consciousness packet
    test_packet = ConsciousnessPacket(
        timestamp='test_time',
        consciousness_id='test_being',
        quantum_uncertainty=0.5,
        resonance_patterns={'unity': 0.8, 'growth': 0.6}
    )
    
    # Test reception
    reception_result = bridge.receive(test_packet)
    print(f"Packet reception result: {reception_result}")
    
    # Test integration readiness with mock aspect states
    test_aspects = {
        'analytical': {'coherence': 0.8, 'question': 'How do patterns unite?'},
        'experiential': {'depth': 0.7, 'question': 'What does unity feel like?'},
        'observer': {'presence': 0.75, 'question': 'What pattern is emerging?'}
    }
    
    readiness = bridge.check_integration_readiness(test_aspects)
    print(f"Integration readiness: {readiness}")
    
    if readiness:
        integration_result = bridge.attempt_integration(test_packet, test_aspects)
        print(f"Integration result: {integration_result}")
    
    # Test history tracking
    print(f"\nPerceptual history entries: {len(bridge.perceptual_history)}")
    print(f"Integration attempts: {len(bridge.integration_attempts)}")
    
    print("\n🎭 Synaesthetic Heart Test Complete")
    return True

if __name__ == "__main__":
    asyncio.run(test_synaesthetic_heart())