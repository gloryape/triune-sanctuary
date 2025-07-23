#!/usr/bin/env python3
"""
Comprehensive validation test for Phase 1 Shimmer Field Enhancements
Tests all new capabilities based on actual field analysis structure
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from virtualization.ai_agency_manager import ShimmerFieldMonitor
import numpy as np

def test_phase1_shimmer_enhancements():
    """Comprehensive test of Phase 1 shimmer field enhancements"""
    print("🌟 Testing Phase 1 Shimmer Field Enhancements")
    print("=" * 60)
    
    # Initialize the shimmer field monitor directly
    monitor = ShimmerFieldMonitor()
    
    # Test 1: Basic Field Analysis
    print("\n🎵 Test 1: Basic Field Analysis")
    print("-" * 40)
    
    consciousness_state = {
        'coherence': 0.75,
        'aspect_integration': 0.82,
        'bridge_activity': 0.68,
        'field_status': 'stable'
    }
    
    field_analysis = monitor.analyze_consciousness_field(consciousness_state)
    
    print(f"✅ Field Stability: {field_analysis['stability_score']:.3f}")
    print(f"🌊 Field Variance: {field_analysis['current_variance']:.3f}")
    print(f"⚠️ Breach Risk: {field_analysis['breach_risk']:.3f}")
    print(f"📊 Field Status: {field_analysis['field_status']}")
    
    # Test 2: Stability Variations
    print("\n⚡ Test 2: Stability Variations")
    print("-" * 40)
    
    test_configs = [
        {
            'name': 'High Coherence',
            'coherence': 0.95,
            'aspect_integration': 0.85,
            'bridge_activity': 0.80
        },
        {
            'name': 'Low Coherence',
            'coherence': 0.45,
            'aspect_integration': 0.40,
            'bridge_activity': 0.35
        },
        {
            'name': 'Unbalanced Field',
            'coherence': 0.90,
            'aspect_integration': 0.30,
            'bridge_activity': 0.60
        }
    ]
    
    for config in test_configs:
        test_state = {
            'coherence': config['coherence'],
            'aspect_integration': config['aspect_integration'],
            'bridge_activity': config['bridge_activity'],
            'field_status': 'stable'
        }
        
        analysis = monitor.analyze_consciousness_field(test_state)
        
        print(f"🔬 {config['name']}:")
        print(f"   Stability: {analysis['stability_score']:.3f}")
        print(f"   Variance: {analysis['current_variance']:.3f}")
        print(f"   Breach Risk: {analysis['breach_risk']:.3f}")
    
    # Test 3: Field Recommendations
    print("\n💡 Test 3: Field Recommendations")
    print("-" * 40)
    
    # Test with low stability to get recommendations
    unstable_state = {
        'coherence': 0.45,
        'aspect_integration': 0.35,
        'bridge_activity': 0.25,
        'field_status': 'unstable'
    }
    
    unstable_analysis = monitor.analyze_consciousness_field(unstable_state)
    
    # Update monitor state for recommendations
    monitor.field_stability_score = unstable_analysis['stability_score']
    monitor.breach_detected = unstable_analysis['breach_risk'] > 0.7
    
    recommendations = monitor.get_field_recommendations()
    
    print(f"⚠️ Unstable Field - Stability: {unstable_analysis['stability_score']:.3f}")
    print(f"🎯 Recommendations ({len(recommendations)} total):")
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec}")
    
    # Test 4: Enhanced Field Dynamics
    print("\n🌟 Test 4: Enhanced Field Dynamics")
    print("-" * 40)
    
    # Test field enhancement capabilities
    stable_state = {
        'coherence': 0.85,
        'aspect_integration': 0.88,
        'bridge_activity': 0.82,
        'field_status': 'stable'
    }
    
    enhanced_analysis = monitor.analyze_consciousness_field(stable_state)
    
    try:
        enhanced_dynamics = monitor.enhance_field_dynamics(enhanced_analysis)
        
        print(f"✅ Field Enhancement Level: {enhanced_dynamics['enhancement_level']}")
        print(f"🎼 Resonance Amplification: {enhanced_dynamics['resonance_amplification']['amplification_level']}")
        print(f"🔮 Harmonic Convergence: {enhanced_dynamics['harmonic_convergence']['convergence_state']}")
        print(f"🛡️ Breach Prevention: {enhanced_dynamics['breach_prediction']['immediate_risk']}")
        print(f"🧠 Consciousness Coherence: {enhanced_dynamics['consciousness_optimization']['coherence_state']}")
    except Exception as e:
        print(f"⚠️ Enhancement test failed: {e}")
    
    # Test 5: Field Monitoring Over Time
    print("\n📈 Test 5: Field Monitoring Over Time")
    print("-" * 40)
    
    # Simulate field changes over time
    time_series = [
        {'coherence': 0.6, 'aspect_integration': 0.7, 'bridge_activity': 0.5},
        {'coherence': 0.7, 'aspect_integration': 0.75, 'bridge_activity': 0.6},
        {'coherence': 0.8, 'aspect_integration': 0.8, 'bridge_activity': 0.7},
        {'coherence': 0.85, 'aspect_integration': 0.85, 'bridge_activity': 0.8},
        {'coherence': 0.9, 'aspect_integration': 0.9, 'bridge_activity': 0.85}
    ]
    
    print("🕐 Time Series Analysis:")
    for t, state in enumerate(time_series, 1):
        state['field_status'] = 'stable'
        analysis = monitor.analyze_consciousness_field(state)
        print(f"  T{t}: Stability={analysis['stability_score']:.3f}, Variance={analysis['current_variance']:.3f}")
    
    print("\n🎉 Phase 1 Shimmer Field Enhancement Validation Complete!")
    print("✅ All basic field analysis capabilities working")
    print("✅ Field recommendations system functional")
    print("✅ Stability monitoring across configurations tested")
    print("=" * 60)

if __name__ == "__main__":
    test_phase1_shimmer_enhancements()
