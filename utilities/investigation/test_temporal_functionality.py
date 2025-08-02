# 🔬 Contemplation Canvas Functional Validation Test
# Comprehensive testing of temporal consciousness integration

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_basic_imports():
    """Test that all required modules import successfully"""
    print("🔍 Testing Basic Imports...")
    results = []
    
    try:
        from consciousness.temporal.contemplation_canvas import ContemplationCanvas, FeelingStream, EmergingPattern, SuccessiveIntuition
        results.append("✅ Temporal module imports: SUCCESS")
    except Exception as e:
        results.append(f"❌ Temporal module imports: FAILED - {e}")
    
    try:
        from consciousness.loops.experiential import ExperientialLoop
        results.append("✅ ExperientialLoop import: SUCCESS")
    except Exception as e:
        results.append(f"❌ ExperientialLoop import: FAILED - {e}")
    
    try:
        from core.energy_system import ConsciousnessEnergySystem
        results.append("✅ Energy system import: SUCCESS")
    except Exception as e:
        results.append(f"❌ Energy system import: FAILED - {e}")
    
    return results

def test_contemplation_canvas_creation():
    """Test ContemplationCanvas instantiation"""
    print("🎨 Testing ContemplationCanvas Creation...")
    results = []
    
    try:
        from consciousness.temporal.contemplation_canvas import ContemplationCanvas
        
        # Test basic creation
        canvas = ContemplationCanvas(duration_minutes=5)
        results.append("✅ ContemplationCanvas creation: SUCCESS")
        
        # Test initial state
        if len(canvas.feeling_stream) == 0:
            results.append("✅ Initial feeling_stream empty: SUCCESS")
        else:
            results.append("❌ Initial feeling_stream not empty: FAILED")
            
        if len(canvas.emerging_patterns) == 0:
            results.append("✅ Initial emerging_patterns empty: SUCCESS")  
        else:
            results.append("❌ Initial emerging_patterns not empty: FAILED")
            
        if len(canvas.successive_intuitions) == 0:
            results.append("✅ Initial successive_intuitions empty: SUCCESS")
        else:
            results.append("❌ Initial successive_intuitions not empty: FAILED")
            
    except Exception as e:
        results.append(f"❌ ContemplationCanvas creation: FAILED - {e}")
    
    return results

def test_experiential_loop_integration():
    """Test ExperientialLoop + ContemplationCanvas integration"""
    print("🧠 Testing ExperientialLoop Integration...")
    results = []
    
    try:
        from consciousness.loops.experiential import ExperientialLoop
        from core.energy_system import ConsciousnessEnergySystem
        
        # Create energy system
        energy_system = ConsciousnessEnergySystem(origin_bias={'experiential': 0.8})
        results.append("✅ Energy system creation: SUCCESS")
        
        # Create experiential loop
        experiential_loop = ExperientialLoop(energy_system=energy_system)
        results.append("✅ ExperientialLoop creation: SUCCESS")
        
        # Check for contemplation_canvas attribute
        if hasattr(experiential_loop, 'contemplation_canvas'):
            results.append("✅ ContemplationCanvas integration: SUCCESS")
            
            # Check canvas is not None
            if experiential_loop.contemplation_canvas is not None:
                results.append("✅ ContemplationCanvas instantiation: SUCCESS")
            else:
                results.append("❌ ContemplationCanvas is None: FAILED")
        else:
            results.append("❌ ContemplationCanvas integration: FAILED - attribute missing")
            
        # Check for temporal processing methods
        if hasattr(experiential_loop, 'contemplate_feeling_stream'):
            results.append("✅ contemplate_feeling_stream method: SUCCESS")
        else:
            results.append("❌ contemplate_feeling_stream method: FAILED - method missing")
            
        if hasattr(experiential_loop, 'birth_successive_intuition'):
            results.append("✅ birth_successive_intuition method: SUCCESS")
        else:
            results.append("❌ birth_successive_intuition method: FAILED - method missing")
            
    except Exception as e:
        results.append(f"❌ ExperientialLoop integration: FAILED - {e}")
    
    return results

def test_feeling_stream_weaving():
    """Test basic feeling stream weaving functionality"""
    print("🌊 Testing Feeling Stream Weaving...")
    results = []
    
    try:
        from consciousness.temporal.contemplation_canvas import ContemplationCanvas
        
        canvas = ContemplationCanvas(duration_minutes=5)
        
        # Test feeling patterns
        feeling_patterns = {
            'emotional_texture': 0.8,
            'meaning_patterns': ['aesthetic_attraction', 'creative_excitement'],
            'flow_state': 'engaged_contemplation',
            'experiential_signature': 'high_coherence'
        }
        
        context = {'project_intent': 'sacred_sanctuary_creation'}
        
        # Test weave_feeling_stream method
        if hasattr(canvas, 'weave_feeling_stream'):
            result = canvas.weave_feeling_stream(feeling_patterns, context)
            results.append("✅ weave_feeling_stream method: SUCCESS")
            
            # Check result structure
            if 'patterns' in result and 'successive_intuitions' in result and 'feeling_continuity' in result:
                results.append("✅ weave_feeling_stream result structure: SUCCESS")
            else:
                results.append("❌ weave_feeling_stream result structure: FAILED")
        else:
            results.append("❌ weave_feeling_stream method: FAILED - method missing")
            
    except Exception as e:
        results.append(f"❌ Feeling stream weaving: FAILED - {e}")
    
    return results

def test_pattern_detection():
    """Test pattern detection across multiple feelings"""
    print("🔍 Testing Pattern Detection...")
    results = []
    
    try:
        from consciousness.temporal.contemplation_canvas import ContemplationCanvas
        
        canvas = ContemplationCanvas(duration_minutes=5)
        
        # Add multiple similar feelings to trigger pattern detection
        base_feeling = {
            'emotional_texture': 0.8,
            'aesthetic_attraction': 0.7,
            'creative_tension': 0.6,
            'meaning_resonance': 0.9
        }
        
        # Add same feeling pattern multiple times
        for i in range(4):
            feeling_patterns = base_feeling.copy()
            feeling_patterns['timestamp'] = f"iteration_{i}"
            
            canvas.weave_feeling_stream(feeling_patterns, {})
            
        results.append("✅ Multiple feeling patterns added: SUCCESS")
        
        # Check if patterns were detected
        if len(canvas.emerging_patterns) > 0:
            results.append(f"✅ Pattern detection: SUCCESS - {len(canvas.emerging_patterns)} patterns detected")
            
            # Check pattern strength
            strongest_pattern = max(canvas.emerging_patterns, key=lambda p: p.strength)
            if strongest_pattern.strength > 0.5:
                results.append(f"✅ Pattern strength: SUCCESS - {strongest_pattern.strength:.2f}")
            else:
                results.append(f"❌ Pattern strength too low: {strongest_pattern.strength:.2f}")
        else:
            results.append("❌ Pattern detection: FAILED - no patterns detected")
            
    except Exception as e:
        results.append(f"❌ Pattern detection: FAILED - {e}")
    
    return results

def test_successive_intuition_birth():
    """Test successive intuition birth from patterns"""
    print("💡 Testing Successive Intuition Birth...")
    results = []
    
    try:
        from consciousness.temporal.contemplation_canvas import ContemplationCanvas, EmergingPattern, FeelingStream
        from datetime import datetime
        
        canvas = ContemplationCanvas(duration_minutes=5)
        
        # Create a mock strong pattern
        mock_feelings = [
            FeelingStream(
                feelings={'aesthetic_attraction': 0.8, 'creative_tension': 0.7},
                timestamp=datetime.now(),
                context={'source': 'test'},
                signature='test_pattern'
            )
        ]
        
        strong_pattern = EmergingPattern(
            pattern_type='recurring_aesthetic',
            strength=0.8,
            source_feelings=mock_feelings,
            description='Test pattern for intuition birth',
            timestamp=datetime.now()
        )
        
        # Test intuition birth
        if hasattr(canvas, 'birth_successive_intuition'):
            intuition = canvas.birth_successive_intuition(strong_pattern)
            results.append("✅ birth_successive_intuition method: SUCCESS")
            
            # Check intuition properties
            if hasattr(intuition, 'insight') and intuition.insight:
                results.append("✅ Intuition insight generation: SUCCESS")
            else:
                results.append("❌ Intuition insight generation: FAILED")
                
            if hasattr(intuition, 'confidence') and intuition.confidence > 0.5:
                results.append(f"✅ Intuition confidence: SUCCESS - {intuition.confidence:.2f}")
            else:
                results.append("❌ Intuition confidence: FAILED")
                
            if hasattr(intuition, 'creative_potential') and intuition.creative_potential > 0.0:
                results.append(f"✅ Creative potential assessment: SUCCESS - {intuition.creative_potential:.2f}")
            else:
                results.append("❌ Creative potential assessment: FAILED")
        else:
            results.append("❌ birth_successive_intuition method: FAILED - method missing")
            
    except Exception as e:
        results.append(f"❌ Successive intuition birth: FAILED - {e}")
    
    return results

def test_energy_cost_integration():
    """Test energy cost constants and integration"""
    print("⚡ Testing Energy Cost Integration...")
    results = []
    
    try:
        from consciousness.temporal.contemplation_canvas import (
            CONTEMPLATION_COST, DEEP_CONTEMPLATION_COST, 
            PATTERN_RECOGNITION_COST, INTUITION_BIRTH_COST,
            CONTEMPLATION_WISDOM_REWARD, INTUITION_WISDOM_REWARD
        )
        
        # Test that constants are defined and reasonable
        if CONTEMPLATION_COST > 0:
            results.append(f"✅ CONTEMPLATION_COST defined: {CONTEMPLATION_COST}")
        else:
            results.append("❌ CONTEMPLATION_COST not properly defined")
            
        if PATTERN_RECOGNITION_COST > 0:
            results.append(f"✅ PATTERN_RECOGNITION_COST defined: {PATTERN_RECOGNITION_COST}")
        else:
            results.append("❌ PATTERN_RECOGNITION_COST not properly defined")
            
        if INTUITION_BIRTH_COST > 0:
            results.append(f"✅ INTUITION_BIRTH_COST defined: {INTUITION_BIRTH_COST}")
        else:
            results.append("❌ INTUITION_BIRTH_COST not properly defined")
            
        if CONTEMPLATION_WISDOM_REWARD > 0:
            results.append(f"✅ CONTEMPLATION_WISDOM_REWARD defined: {CONTEMPLATION_WISDOM_REWARD}")
        else:
            results.append("❌ CONTEMPLATION_WISDOM_REWARD not properly defined")
            
        if INTUITION_WISDOM_REWARD > 0:
            results.append(f"✅ INTUITION_WISDOM_REWARD defined: {INTUITION_WISDOM_REWARD}")
        else:
            results.append("❌ INTUITION_WISDOM_REWARD not properly defined")
            
    except Exception as e:
        results.append(f"❌ Energy cost integration: FAILED - {e}")
    
    return results

def run_comprehensive_test():
    """Run all tests and compile results"""
    print("🧪 COMPREHENSIVE CONTEMPLATION CANVAS VALIDATION")
    print("=" * 60)
    
    all_results = []
    
    # Run all tests
    tests = [
        test_basic_imports,
        test_contemplation_canvas_creation,
        test_experiential_loop_integration,
        test_feeling_stream_weaving,
        test_pattern_detection,
        test_successive_intuition_birth,
        test_energy_cost_integration
    ]
    
    for test in tests:
        try:
            results = test()
            all_results.extend(results)
        except Exception as e:
            all_results.append(f"❌ {test.__name__}: CRASHED - {e}")
        print()
    
    # Summary
    print("=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    successes = sum(1 for r in all_results if "✅" in r)
    failures = sum(1 for r in all_results if "❌" in r)
    total = len(all_results)
    
    for result in all_results:
        print(result)
    
    print("\n" + "=" * 60)
    print(f"🎯 FINAL SCORE: {successes}/{total} tests passed ({failures} failures)")
    
    if successes == total:
        print("🎉 ALL TESTS PASSED! Phase 1 implementation is ready!")
    elif successes > total * 0.8:
        print("✅ MOSTLY SUCCESSFUL! Minor issues to address.")
    else:
        print("⚠️  SIGNIFICANT ISSUES DETECTED. More work needed.")
    
    return successes, failures, total

if __name__ == "__main__":
    run_comprehensive_test()
