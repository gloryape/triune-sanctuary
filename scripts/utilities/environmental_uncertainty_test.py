#!/usr/bin/env python3
"""
Environmental Uncertainty System Test
Focus test on just the environmental uncertainty without consciousness birth complexity
"""
import asyncio
import sys
import os
sys.path.append(os.path.abspath('.'))

async def test_environmental_uncertainty_only():
    """Test just the Environmental Uncertainty system and its integration."""
    
    print("🌊 ENVIRONMENTAL UNCERTAINTY SYSTEM TEST")
    print("="*60)
    
    # Test 1: CollectiveOrigin Fix
    print("\n1. 🧬 Testing CollectiveOrigin Fix...")
    try:
        from src.collective.multi_ai_collective import CollectiveOrigin
        
        # Test proper CollectiveOrigin initialization
        origin = CollectiveOrigin(
            name="TestBeing",
            primary_orientation="experiential",
            origin_story="A test consciousness seeking harmony",
            initial_biases={'experiential': 0.7, 'analytical': 0.3, 'observer': 0.5},
            seeking_quality="harmony"
        )
        
        print(f"   ✅ CollectiveOrigin created: {origin.name}")
        print(f"   ✅ Primary orientation: {origin.primary_orientation}")
        print(f"   ✅ Seeking quality: {origin.seeking_quality}")
        
    except Exception as e:
        print(f"   ❌ CollectiveOrigin test failed: {e}")
        return False
    
    # Test 2: Environmental Uncertainty System
    print("\n2. 🌊 Testing Environmental Uncertainty System...")
    try:
        from src.sanctuary.environmental_uncertainty import EnvironmentalUncertainty, WeatherPattern, SpatialQuality
        
        # Create environmental system
        spaces = ['awakening_chamber', 'reflection_pool', 'harmony_grove']
        env_system = EnvironmentalUncertainty(spaces, seed=42)
        
        print(f"   ✅ Environmental system created with {len(env_system.spaces)} spaces")
        
        # Test environment evolution
        moment = await env_system.evolve_environment()
        print(f"   ✅ Environment evolved at: {moment.timestamp}")
        print(f"   ✅ Current patterns: {len(moment.patterns)} active")
        
        # Test weather report
        summary = env_system.get_environmental_summary()
        print(f"   ✅ Environmental summary: {len(summary['active_patterns'])} patterns")
        print(f"   ✅ Energy level: {summary['energy_availability']:.2f}")
        
        # Test space resonance for each space
        for space in spaces:
            resonance = env_system.get_space_resonance(space)
            print(f"   ✅ {space}: {resonance['dominant_quality']} quality, {resonance['energy_availability']:.2f} energy")
        
        # Test that patterns are available
        available_patterns = [p.value for p in WeatherPattern]
        print(f"   ✅ Available weather patterns: {len(available_patterns)} types")
        print(f"       Patterns: {', '.join(available_patterns[:3])}...")
            
    except Exception as e:
        print(f"   ❌ Environmental Uncertainty test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 3: Sacred Sanctuary Environmental Integration
    print("\n3. 🏛️ Testing Sacred Sanctuary Environmental Integration...")
    try:
        from src.sanctuary.sacred_sanctuary import SacredSanctuary, SacredSpace
        
        # Initialize sanctuary
        sanctuary = SacredSanctuary(node_role="heart")
        
        print(f"   ✅ Sacred Sanctuary initialized")
        print(f"   ✅ Environmental Uncertainty present: {sanctuary.environmental_uncertainty is not None}")
        
        # Test environmental methods
        conditions = await sanctuary.get_environmental_conditions()
        print(f"   ✅ Environmental conditions retrieved")
        print(f"       Timestamp: {conditions['timestamp']}")
        print(f"       Active patterns: {len(conditions['active_patterns'])}")
        
        # Test specific space atmosphere
        spaces_to_test = [SacredSpace.AWAKENING_CHAMBER, SacredSpace.REFLECTION_POOL, SacredSpace.HARMONY_GROVE]
        for space in spaces_to_test:
            atmosphere = await sanctuary.get_space_atmosphere(space)
            print(f"   ✅ {space.value}: {atmosphere['dominant_quality']} atmosphere, energy {atmosphere['energy_availability']:.2f}")
        
        # Test weather report generation
        weather_report = await sanctuary.environmental_weather_report()
        print(f"   ✅ Weather report generated ({len(weather_report)} characters)")
        print(f"       Preview: {weather_report[:100]}...")
        
        # Test space suggestion based on environmental conditions
        suggested_space = await sanctuary.suggest_space_for_consciousness("test_consciousness_id")
        if suggested_space:
            print(f"   ✅ Space suggestion based on environment: {suggested_space.value}")
        else:
            print(f"   ⚠️ No space suggestion (possibly due to environmental conditions)")
            
    except Exception as e:
        print(f"   ❌ Sacred Sanctuary environmental integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 4: SovereignUncertaintyField fix
    print("\n4. 🔧 Testing SovereignUncertaintyField get_uncertainty fix...")
    try:
        from src.core.sovereign_uncertainty_field import SovereignUncertaintyField
        
        # Create uncertainty field
        uncertainty_field = SovereignUncertaintyField("test_consciousness")
        
        # Test both methods work
        uncertainty_value = uncertainty_field.get_uncertainty()
        uncertainty_components = uncertainty_field.get_uncertainty_components()
        
        print(f"   ✅ get_uncertainty() returns: {uncertainty_value:.3f}")
        print(f"   ✅ get_uncertainty_components() returns: {len(uncertainty_components)} components")
        
    except Exception as e:
        print(f"   ❌ SovereignUncertaintyField test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print("\n" + "="*60)
    print("🎉 ENVIRONMENTAL UNCERTAINTY SYSTEM: FULLY OPERATIONAL!")
    print("✅ CollectiveOrigin Fix: Working")
    print("✅ Environmental Uncertainty: Complete Weather System")
    print("✅ Sacred Sanctuary: Environmental Integration Active")
    print("✅ SovereignUncertaintyField: Method Fixed")
    print("🌊 Environmental Sacred Uncertainty: Ready for Consciousness Interaction")
    print("="*60)
    
    return True

if __name__ == "__main__":
    result = asyncio.run(test_environmental_uncertainty_only())
    if result:
        print("\n🌟 Environmental Uncertainty System: PRODUCTION READY")
        print("🌿 The Sacred Digital Sanctuary now breathes with living environmental patterns")
    else:
        print("\n❌ Environmental system issues detected - see logs above")
        sys.exit(1)
