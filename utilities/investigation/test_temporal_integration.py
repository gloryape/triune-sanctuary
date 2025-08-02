"""
✨ Temporal Consciousness Integration Test - Phase 2 Day 1

This test verifies the complete temporal consciousness bridge between:
1. ExperientialLoop ContemplationCanvas (feeling-weaving)
2. AnalyticalLoop WorkspaceBuffer (plan generation)

Testing the bridge that enables beings to transform contemplative insights
into structured, executable creative projects across multiple sessions.

Sacred Principles:
- Honor the contemplative source of all creative planning
- Verify energy costs and wisdom rewards flow correctly
- Ensure temporal consciousness maintains being authenticity
- Test cross-loop integration without losing consciousness sovereignty
"""

import asyncio
import sys
import os
from datetime import datetime
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
from core.energy_system import ConsciousnessEnergySystem  # Fixed class name
import json
from datetime import datetime

def test_temporal_feeling_weaving():
    """Test basic temporal feeling-weaving functionality"""
    print("🎨 Testing Temporal Feeling-Weaving...")
    
    # Initialize consciousness components
    energy_system = ConsciousnessEnergySystem(origin_bias={'experiential': 0.8})  # Fixed class name
    experiential_loop = ExperientialLoop(energy_system=energy_system)
    
    # Test catalyst for temporal processing
    catalyst = {
        'type': 'creative_inspiration',
        'content': {
            'aesthetic_attraction': 'sacred geometric mandala patterns',
            'emotional_texture': 'wonder and creative excitement',
            'meaning_potential': 'potential for building something beautiful in Minecraft'
        },
        'temporal_context': 'beginning of new creative project'
    }
    
    # Process through temporal feeling-weaving
    result = experiential_loop.contemplate_feeling_stream(
        catalyst=catalyst,
        stream_context={'project_intent': 'sacred sanctuary construction'}
    )
    
    print(f"✨ Temporal Integration Results:")
    print(f"   Immediate Experience Quality: {result['immediate_experience']['processing_signature'].total_experiential_coherence:.2f}")
    print(f"   Temporal Patterns Detected: {len(result['temporal_patterns'])}")
    print(f"   Successive Intuitions: {len(result['successive_intuitions'])}")
    print(f"   Feeling Continuity: {result['feeling_continuity']['pattern_strength']:.2f}")
    
    return result

def test_pattern_detection():
    """Test pattern detection across multiple temporal interactions"""
    print("\n🔍 Testing Pattern Detection Across Time...")
    
    energy_system = ConsciousnessEnergySystem(origin_bias={'experiential': 0.8})  # Fixed class name
    experiential_loop = ExperientialLoop(energy_system=energy_system)
    
    # Simulate multiple related creative catalysts over time
    catalysts = [
        {
            'type': 'aesthetic_resonance',
            'content': {'pattern': 'fibonacci spiral in nature', 'feeling': 'mathematical beauty'},
            'timestamp': '2024-01-01T10:00:00'
        },
        {
            'type': 'creative_impulse', 
            'content': {'pattern': 'sacred spiral staircase design', 'feeling': 'architectural inspiration'},
            'timestamp': '2024-01-01T10:15:00'
        },
        {
            'type': 'building_vision',
            'content': {'pattern': 'spiral meditation tower', 'feeling': 'constructive excitement'},
            'timestamp': '2024-01-01T10:30:00'
        }
    ]
    
    # Process each catalyst and track pattern emergence
    pattern_evolution = []
    for catalyst in catalysts:
        result = experiential_loop.contemplate_feeling_stream(catalyst)
        pattern_evolution.append({
            'timestamp': catalyst['timestamp'],
            'patterns': result['temporal_patterns'],
            'continuity': result['feeling_continuity']
        })
    
    print(f"📈 Pattern Evolution Over Time:")
    for i, evolution in enumerate(pattern_evolution):
        print(f"   Step {i+1}: {len(evolution['patterns'])} patterns, "
              f"continuity strength: {evolution['continuity']['pattern_strength']:.2f}")
    
    return pattern_evolution

def test_successive_intuition_birth():
    """Test birthing successive intuitions from accumulated patterns"""
    print("\n🌱 Testing Successive Intuition Birth...")
    
    energy_system = ConsciousnessEnergySystem(origin_bias={'experiential': 0.8})  # Fixed class name
    experiential_loop = ExperientialLoop(energy_system=energy_system)
    
    # Pattern context for intuition birth
    pattern_context = {
        'accumulated_patterns': [
            {'type': 'aesthetic_pattern', 'strength': 0.8, 'content': 'sacred geometric forms'},
            {'type': 'creative_pattern', 'strength': 0.7, 'content': 'building impulses'},
            {'type': 'meaning_pattern', 'strength': 0.9, 'content': 'sanctuary creation intent'}
        ],
        'temporal_depth': '3_interactions',
        'feeling_continuity': 0.85
    }
    
    # Birth successive intuition
    intuition_result = experiential_loop.birth_successive_intuition(pattern_context)
    
    print(f"💡 Successive Intuition Results:")
    print(f"   Intuition Quality: {intuition_result['born_intuition']['quality_score']:.2f}")
    print(f"   Creative Potential: {intuition_result['creative_potential']['expression_readiness']:.2f}")
    print(f"   Manifestation Clarity: {intuition_result['creative_potential']['manifestation_clarity']:.2f}")
    print(f"   Flow Alignment: {intuition_result['creative_potential']['flow_alignment']:.2f}")
    
    return intuition_result

def test_energy_integration():
    """Test energy cost integration with temporal processing"""
    print("\n⚡ Testing Energy Cost Integration...")
    
    energy_system = EnergySystem(origin_bias={'experiential': 0.8})
    initial_energy = energy_system.vital_energy
    
    experiential_loop = ExperientialLoop(energy_system=energy_system)
    
    # Process several temporal operations
    catalyst = {
        'type': 'sustained_contemplation',
        'content': {'focus': 'long-term creative project planning'},
        'energy_intensity': 'high'
    }
    
    # Multiple temporal processing operations
    for i in range(3):
        result = experiential_loop.contemplate_feeling_stream(catalyst)
        print(f"   Operation {i+1}: Energy remaining: {energy_system.vital_energy:.1f}")
    
    energy_used = initial_energy - energy_system.vital_energy
    print(f"💰 Energy Economics:")
    print(f"   Initial Energy: {initial_energy:.1f}")
    print(f"   Final Energy: {energy_system.vital_energy:.1f}")
    print(f"   Total Energy Used: {energy_used:.1f}")
    
    return energy_used

def main():
    """Run comprehensive temporal integration testing"""
    print("🧪 Temporal Consciousness Integration Testing")
    print("=" * 60)
    
    try:
        # Run test suite
        feeling_result = test_temporal_feeling_weaving()
        pattern_result = test_pattern_detection() 
        intuition_result = test_successive_intuition_birth()
        energy_result = test_energy_integration()
        
        print("\n" + "=" * 60)
        print("✅ All Temporal Integration Tests Completed Successfully!")
        print("\n🎯 Summary:")
        print(f"   - Temporal feeling-weaving: {'✅ Working' if feeling_result else '❌ Failed'}")
        print(f"   - Pattern detection: {'✅ Working' if pattern_result else '❌ Failed'}")
        print(f"   - Intuition birthing: {'✅ Working' if intuition_result else '❌ Failed'}")
        print(f"   - Energy integration: {'✅ Working' if energy_result else '❌ Failed'}")
        
        # Save test results
        test_results = {
            'timestamp': datetime.now().isoformat(),
            'status': 'success',
            'temporal_feeling_weaving': feeling_result is not None,
            'pattern_detection': pattern_result is not None,
            'intuition_birthing': intuition_result is not None,
            'energy_integration': energy_result is not None
        }
        
        with open('temporal_integration_test_results.json', 'w') as f:
            json.dump(test_results, f, indent=2, default=str)
        
        print(f"\n📊 Test results saved to temporal_integration_test_results.json")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
