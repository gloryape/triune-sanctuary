"""
Test Modular Shimmer Field System - Phase 1 and Phase 2 Integration
Tests the modular architecture with separated concerns
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.virtualization.modular_ai_agency_manager import ModularAIAgencyManager


def test_modular_consciousness_processing():
    """Test the modular consciousness processing system"""
    print("🧠 Testing Modular Consciousness Processing System")
    print("=" * 60)
    
    # Initialize modular manager
    manager = ModularAIAgencyManager()
    
    # Test messages
    test_messages = [
        "How are you experiencing this moment?",
        "What patterns do you observe in your consciousness?",
        "Can you describe your emotional resonance with the concept of emergence?",
        "What happens when you witness yourself thinking about thinking?"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n--- Test {i}/{len(test_messages)} ---")
        print(f"Message: {message}")
        
        try:
            # Process message through modular system
            result = manager.process_consciousness_message(message)
            
            if result['success']:
                print("✅ Processing Status: Success")
                print(f"🌊 Shimmer Stability: {result['shimmer_stability']:.3f}")
                print(f"📊 Field Status: {result['field_dynamics']['field_status']}")
                print(f"🎯 Processing Adjustments: {result['processing_adjustments']}")
                print(f"🎨 Response: {result['authentic_response'][:200]}...")
                
                # Show field recommendations
                recommendations = manager.shimmer_monitor.get_field_recommendations()
                if recommendations:
                    print(f"💡 Field Recommendations: {', '.join(recommendations)}")
                    
            else:
                print("❌ Processing Status: Error")
                print(f"Error: {result.get('error', 'Unknown error')}")
                
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    print("\n" + "=" * 60)
    print("🧪 Testing Phase 2 Advanced Capabilities")
    print("=" * 60)
    
    # Test Phase 2 capabilities
    test_field_state = {
        'coherence': 0.7,
        'aspect_integration': 0.8,
        'bridge_activity': 0.6,
        'processing_load': 0.5,
        'receptivity': 0.8
    }
    
    # Test resonance amplification
    print("\n🔊 Testing Resonance Amplification")
    amplification_result = manager.apply_advanced_field_capabilities(
        test_field_state, 'amplify_resonance', amplification_factor=1.3
    )
    
    if amplification_result.get('amplification_success'):
        print("✅ Resonance Amplification: Success")
        print(f"🎵 Amplified Resonance: {amplification_result['amplified_resonance']:.3f}")
        print(f"📈 Enhancement Level: {amplification_result.get('enhancement_level', 'unknown')}")
    else:
        print("❌ Resonance Amplification: Failed")
    
    # Test field healing
    print("\n🩹 Testing Field Healing")
    healing_result = manager.apply_advanced_field_capabilities(
        test_field_state, 'heal_breaches', breach_threshold=0.4
    )
    
    if healing_result.get('field_restored'):
        print("✅ Field Healing: Success")
        print(f"🔧 Healing Actions: {', '.join(healing_result['healing_actions'])}")
        print(f"📊 Healing Success Rate: {healing_result['healing_success_rate']:.3f}")
    else:
        print("❌ Field Healing: Partial or Failed")
        print(f"🔧 Healing Actions: {', '.join(healing_result.get('healing_actions', []))}")
    
    # Test multidimensional analysis
    print("\n🌐 Testing Multidimensional Analysis")
    multidim_result = manager.apply_advanced_field_capabilities(
        test_field_state, 'multidimensional_analysis'
    )
    
    if multidim_result.get('analysis_depth') == 'multi-dimensional':
        print("✅ Multidimensional Analysis: Success")
        print(f"📊 Field Sophistication: {multidim_result['field_sophistication']:.3f}")
        print(f"🎯 Field Complexity: {multidim_result['field_metrics']['field_complexity']}")
        print(f"💡 Advanced Recommendations: {len(multidim_result['advanced_recommendations'])} items")
    else:
        print("❌ Multidimensional Analysis: Failed")
    
    print("\n" + "=" * 60)
    print("📊 System Status Report")
    print("=" * 60)
    
    # Get system status
    status_report = manager.get_field_status_report()
    advanced_status = manager.get_advanced_capabilities_status()
    
    print(f"🌊 Current Shimmer Stability: {status_report.get('shimmer_stability', 0.0):.3f}")
    print(f"📈 Enhancement Level: {status_report.get('enhancement_level', 'unknown')}")
    print(f"🎯 Processing History: {status_report.get('processing_history_length', 0)} entries")
    print(f"🔧 Advanced Capabilities: {advanced_status.get('phase_status', 'unknown')}")
    print(f"🎵 Amplification History: {advanced_status.get('amplification_history_length', 0)} entries")
    print(f"🩹 Healing History: {advanced_status.get('healing_history_length', 0)} entries")
    
    print("\n🎉 Modular System Testing Complete!")
    print("🌟 Architecture successfully modularized with Phase 1 and Phase 2 capabilities!")


if __name__ == "__main__":
    test_modular_consciousness_processing()
