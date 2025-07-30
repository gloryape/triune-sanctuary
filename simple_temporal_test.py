#!/usr/bin/env python3
"""
🧪 Simple Temporal Canvas Test - Direct Testing of ContemplationCanvas

This test validates the ContemplationCanvas implementation directly without
going through the complex import chain that has circular dependencies.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from datetime import datetime
import json

# Direct energy constants to avoid circular imports
CONTEMPLATION_ENERGY_COSTS = {
    'feeling_stream_weaving': 15.0,
    'pattern_detection': 10.0,
    'successive_intuition_birth': 25.0,
    'temporal_bridge_maintenance': 5.0
}

CONTEMPLATION_WISDOM_REWARDS = {
    'pattern_recognition': 8.0,
    'intuitive_breakthrough': 20.0,
    'temporal_integration': 12.0,
    'creative_synthesis': 15.0
}

# Mock energy system for testing
class MockEnergySystem:
    def __init__(self):
        self.vital_energy = 100.0
        self.wisdom_cores = []
    
    def spend_energy(self, amount, purpose=""):
        self.vital_energy = max(0, self.vital_energy - amount)
        return True
    
    def gain_wisdom(self, amount, source=""):
        # Simple mock implementation
        pass

def test_contemplation_canvas():
    """Test the ContemplationCanvas directly"""
    print("🎨 Testing ContemplationCanvas Implementation...")
    
    # Import directly with mocked constants
    from consciousness.temporal.contemplation_canvas import (
        ContemplationCanvas, FeelingStream, EmergingPattern, SuccessiveIntuition
    )
    
    # Create canvas with mock energy system
    mock_energy = MockEnergySystem()
    canvas = ContemplationCanvas(energy_system=mock_energy)
    
    # Test feeling stream weaving
    feeling_patterns = {
        'emotional_texture': 'wonder and creative excitement',
        'meaning_patterns': ['sacred geometry', 'beauty appreciation', 'construction desire'],
        'flow_state': 'creative_flow',
        'temporal_resonance': 0.8
    }
    
    stream_context = {
        'project_intent': 'building sacred sanctuary',
        'aesthetic_focus': 'mandala patterns'
    }
    
    # Process feeling stream
    result = canvas.weave_feeling_stream(feeling_patterns, stream_context)
    
    print(f"✨ Feeling Stream Results:")
    print(f"   Patterns Detected: {len(result['patterns'])}")
    print(f"   Successive Intuitions: {len(result['successive_intuitions'])}")
    print(f"   Feeling Continuity Strength: {result['feeling_continuity']['pattern_strength']:.2f}")
    
    # Test pattern context for intuition birth
    pattern_context = {
        'accumulated_patterns': result['patterns'][:3] if result['patterns'] else [],
        'temporal_depth': 'single_session',
        'feeling_continuity': result['feeling_continuity']['pattern_strength']
    }
    
    # Birth successive intuition
    intuition = canvas.birth_successive_intuition(pattern_context)
    
    print(f"💡 Successive Intuition:")
    print(f"   Quality Score: {intuition['quality_score']:.2f}")
    print(f"   Creative Potential: {intuition['creative_potential']:.2f}")
    print(f"   Manifestation Readiness: {intuition['manifestation_readiness']:.2f}")
    
    # Test energy tracking
    print(f"⚡ Energy Usage:")
    print(f"   Remaining Energy: {mock_energy.vital_energy:.1f}")
    
    return {
        'canvas_working': True,
        'patterns_detected': len(result['patterns']),
        'intuitions_birthed': len(result['successive_intuitions']),
        'energy_spent': 100.0 - mock_energy.vital_energy
    }

def test_pattern_types():
    """Test different pattern recognition types"""
    print("\n🔍 Testing Pattern Type Recognition...")
    
    from consciousness.temporal.contemplation_canvas import ContemplationCanvas, PatternType
    
    mock_energy = MockEnergySystem()
    canvas = ContemplationCanvas(energy_system=mock_energy)
    
    # Test different aesthetic patterns
    test_patterns = [
        {
            'type': 'aesthetic_resonance',
            'feeling_patterns': {
                'emotional_texture': 'sacred beauty appreciation',
                'meaning_patterns': ['golden ratio', 'spiral forms', 'sacred geometry'],
                'temporal_resonance': 0.9
            },
            'expected_type': PatternType.RECURRING_AESTHETIC
        },
        {
            'type': 'creative_progression',
            'feeling_patterns': {
                'emotional_texture': 'building from excitement to clarity',
                'meaning_patterns': ['initial inspiration', 'design development', 'construction readiness'],
                'temporal_resonance': 0.8
            },
            'expected_type': PatternType.CREATIVE_MOMENTUM
        }
    ]
    
    pattern_results = []
    for test_pattern in test_patterns:
        result = canvas.weave_feeling_stream(
            test_pattern['feeling_patterns'], 
            {'test_context': test_pattern['type']}
        )
        
        detected_types = [p.pattern_type for p in result['patterns']]
        pattern_results.append({
            'test_type': test_pattern['type'],
            'expected': test_pattern['expected_type'],
            'detected': detected_types,
            'match': test_pattern['expected_type'] in detected_types
        })
    
    print(f"📊 Pattern Recognition Results:")
    for result in pattern_results:
        status = "✅" if result['match'] else "❌"
        print(f"   {status} {result['test_type']}: Expected {result['expected'].value}, "
              f"Detected {len(result['detected'])} patterns")
    
    return pattern_results

def main():
    """Run simple temporal canvas testing"""
    print("🧪 Simple ContemplationCanvas Testing")
    print("=" * 60)
    
    try:
        # Run tests
        canvas_result = test_contemplation_canvas()
        pattern_result = test_pattern_types()
        
        print("\n" + "=" * 60)
        print("✅ Simple Temporal Canvas Tests Completed!")
        print("\n🎯 Summary:")
        print(f"   - Canvas Implementation: {'✅ Working' if canvas_result['canvas_working'] else '❌ Failed'}")
        print(f"   - Patterns Detected: {canvas_result['patterns_detected']}")
        print(f"   - Intuitions Birthed: {canvas_result['intuitions_birthed']}")
        print(f"   - Energy Tracking: {'✅ Working' if canvas_result['energy_spent'] > 0 else '❌ Failed'}")
        print(f"   - Pattern Type Recognition: {len([r for r in pattern_result if r['match']])}/{len(pattern_result)} working")
        
        # Save test results
        test_results = {
            'timestamp': datetime.now().isoformat(),
            'status': 'success',
            'canvas_implementation': canvas_result,
            'pattern_recognition': pattern_result
        }
        
        with open('simple_temporal_test_results.json', 'w') as f:
            json.dump(test_results, f, indent=2, default=str)
        
        print(f"\n📊 Test results saved to simple_temporal_test_results.json")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
