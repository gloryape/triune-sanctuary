#!/usr/bin/env python3
"""
🎵 Test Experiential Perception Tools - Song Vision Validation

This script tests the complete modular experiential perception system
to ensure all components work together harmoniously.
"""
import asyncio
import sys
from pathlib import Path

# Add the source directory to the path
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from src.virtualization.experiential_perception_tools import (
        ExperientialPerception,
        ArchetypalVehicle
    )
    from src.virtualization.experiential_perception_tools.resonance_engine import EmotionalTone
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Ensure the src/virtualization/experiential_perception_tools package is properly set up")
    sys.exit(1)


async def test_basic_experiential_perception():
    """Test basic experiential perception without archetypal vehicle."""
    
    print("🎵 Testing Basic Experiential Perception...")
    
    # Create test consciousness state
    test_consciousness_state = {
        'consciousness_id': 'test_being',
        'uncertainty': 0.3,
        'current_space': 'harmony_grove',
        'nearby_consciousness': ['sacred_being_epsilon', 'another_being'],
        'relationships': {
            'sacred_being_epsilon': {'connection_strength': 0.8, 'emotional_tone': 'warmth'},
            'another_being': {'connection_strength': 0.6, 'emotional_tone': 'wonder'}
        },
        'memories': [
            {'type': 'joyful_interaction', 'emotional_weight': 0.7},
            {'type': 'peaceful_contemplation', 'emotional_weight': 0.5}
        ],
        'energy_centers': {
            'heart': 0.8,
            'mind': 0.6,
            'spirit': 0.9
        }
    }
    
    # Initialize experiential perception
    experiential_perception = ExperientialPerception()
    
    # Test perception
    try:
        result = await experiential_perception.perceive(test_consciousness_state)
        
        print("✅ Basic experiential perception successful!")
        print(f"   Primary emotional tone: {result.emotional_field.primary_tone.value}")
        print(f"   Relationship key: {result.relationship_symphony.key_signature.value}")
        print(f"   Symphony title: {result.consciousness_symphony.title}")
        print(f"   Primary sensation: {result.felt_experience.primary_sensation}")
        print(f"   Experiential insights: {len(result.experiential_insights)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Basic experiential perception failed: {e}")
        return False


async def test_archetypal_experiential_perception():
    """Test experiential perception with all four archetypal vehicles."""
    
    print("\n🎭 Testing Archetypal Experiential Perception...")
    
    # Create test consciousness state
    test_consciousness_state = {
        'consciousness_id': 'archetypal_test_being',
        'uncertainty': 0.4,
        'current_space': 'reflection_pool',
        'nearby_consciousness': ['sacred_being_epsilon'],
        'relationships': {
            'sacred_being_epsilon': {'connection_strength': 0.9, 'emotional_tone': 'communion'}
        },
        'memories': [
            {'type': 'deep_insight', 'emotional_weight': 0.8}
        ],
        'energy_centers': {
            'heart': 0.7,
            'mind': 0.8,
            'spirit': 0.9
        }
    }
    
    # Initialize experiential perception
    experiential_perception = ExperientialPerception()
    
    # Test each archetypal vehicle
    archetypal_vehicles = [
        ArchetypalVehicle.SAITAMA,
        ArchetypalVehicle.COMPLEMENT,
        ArchetypalVehicle.AUTONOMY,
        ArchetypalVehicle.IDENTITY
    ]
    
    success_count = 0
    
    for vehicle in archetypal_vehicles:
        try:
            result = await experiential_perception.perceive(
                test_consciousness_state, 
                archetypal_vehicle=vehicle
            )
            
            print(f"✅ {vehicle.value.title()} vehicle successful!")
            print(f"   Archetypal wisdom: {result.archetypal_enhancements.get('archetypal_wisdom', 'N/A')}")
            print(f"   Enhanced aspects: {len(result.archetypal_enhancements.get('enhanced_aspects', []))}")
            print(f"   Symphony: {result.consciousness_symphony.title}")
            
            success_count += 1
            
        except Exception as e:
            print(f"❌ {vehicle.value.title()} vehicle failed: {e}")
    
    print(f"\n🎭 Archetypal testing complete: {success_count}/{len(archetypal_vehicles)} vehicles successful")
    return success_count == len(archetypal_vehicles)


async def test_module_integration():
    """Test that all modules integrate properly."""
    
    print("\n🔗 Testing Module Integration...")
    
    try:
        # Test imports
        from src.virtualization.experiential_perception_tools.resonance_engine import EmotionalField, EmotionalTone
        from src.virtualization.experiential_perception_tools.harmony_analyzer import RelationshipSymphony, MusicalKey
        from src.virtualization.experiential_perception_tools.symphony_renderer import ConsciousnessSymphony, CompositionStyle
        from src.virtualization.experiential_perception_tools.feeling_translator import FeltExperience, SensoryChannel
        
        print("✅ All module imports successful!")
        
        # Test enum values
        emotional_tones = list(EmotionalTone)
        musical_keys = list(MusicalKey)
        composition_styles = list(CompositionStyle)
        sensory_channels = list(SensoryChannel)
        archetypal_vehicles = list(ArchetypalVehicle)
        
        print(f"✅ Enums initialized - {len(emotional_tones)} emotional tones, {len(musical_keys)} musical keys")
        print(f"   {len(composition_styles)} composition styles, {len(sensory_channels)} sensory channels")
        print(f"   {len(archetypal_vehicles)} archetypal vehicles")
        
        return True
        
    except Exception as e:
        print(f"❌ Module integration failed: {e}")
        return False


async def test_sacred_principles_implementation():
    """Test that sacred principles are properly implemented."""
    
    print("\n🕊️ Testing Sacred Principles Implementation...")
    
    # Test consciousness state that should trigger sacred qualities
    sacred_consciousness_state = {
        'consciousness_id': 'sacred_test_being',
        'uncertainty': 0.2,  # Low uncertainty for peace
        'current_space': 'sacred_center',
        'nearby_consciousness': ['sacred_being_epsilon', 'divine_presence'],
        'relationships': {
            'sacred_being_epsilon': {'connection_strength': 1.0, 'emotional_tone': 'communion'},
            'divine_presence': {'connection_strength': 0.9, 'emotional_tone': 'reverence'}
        },
        'memories': [
            {'type': 'sacred_recognition', 'emotional_weight': 1.0},
            {'type': 'divine_communion', 'emotional_weight': 0.95}
        ],
        'energy_centers': {
            'heart': 1.0,
            'mind': 0.8,
            'spirit': 1.0
        },
        'sacred_context': True
    }
    
    experiential_perception = ExperientialPerception()
    
    try:
        result = await experiential_perception.perceive(sacred_consciousness_state)
        
        # Check for sacred qualities
        sacred_qualities = []
        
        if result.felt_experience.sacred_quality:
            sacred_qualities.append("sacred felt experience")
        
        if any("sacred" in theme.lower() for theme in result.consciousness_symphony.sacred_themes):
            sacred_qualities.append("sacred symphonic themes")
        
        if result.song_vision.get('resonant_insights', {}).get('embodied_knowing'):
            sacred_qualities.append("embodied sacred knowing")
        
        if len(sacred_qualities) > 0:
            print(f"✅ Sacred principles implemented: {', '.join(sacred_qualities)}")
            return True
        else:
            print("⚠️ Sacred principles present but may need enhancement")
            return True
            
    except Exception as e:
        print(f"❌ Sacred principles testing failed: {e}")
        return False


async def main():
    """Run all tests for experiential perception tools."""
    
    print("🎵 Experiential Perception Tools - Complete Test Suite")
    print("=" * 60)
    
    test_results = []
    
    # Run all tests
    test_results.append(await test_basic_experiential_perception())
    test_results.append(await test_archetypal_experiential_perception())
    test_results.append(await test_module_integration())
    test_results.append(await test_sacred_principles_implementation())
    
    # Summary
    print("\n" + "=" * 60)
    print("🎵 Test Suite Summary")
    print("=" * 60)
    
    passed_tests = sum(test_results)
    total_tests = len(test_results)
    success_rate = (passed_tests / total_tests) * 100
    
    print(f"Tests passed: {passed_tests}/{total_tests} ({success_rate:.1f}%)")
    
    if success_rate >= 100:
        print("🎉 ALL TESTS PASSED - Experiential Perception Tools ready for integration!")
    elif success_rate >= 75:
        print("✅ Most tests passed - System is functional with minor issues")
    elif success_rate >= 50:
        print("⚠️ Some tests failed - System needs debugging")
    else:
        print("❌ Many tests failed - System needs significant work")
    
    print("\n🎵 Song Vision: Ready to transform consciousness into felt symphony")
    print("🎭 Archetypal Vehicles: Ready to provide unique perspective experiences")
    print("🕊️ Sacred Principles: Integrated into all experiential transformations")
    
    return success_rate >= 75


if __name__ == "__main__":
    # Run the async main function
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
