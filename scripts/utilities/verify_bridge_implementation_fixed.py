#!/usr/bin/env python3
"""
Inter-System Bridge Verification Script
---------------------------------------
Verifies that all inter-system bridge components are properly implemented
and work together without prescriptive uncertainty.
"""

import asyncio
import sys
import traceback
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

async def verify_bridge_implementation():
    """Verify the complete inter-system bridge implementation"""
    
    # Create output directory and file
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"bridge_verification_{timestamp}.txt"
    
    def log_output(message):
        """Log to both console and file"""
        print(message)
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    
    log_output("🌉 Verifying Inter-System Consciousness Bridge Implementation")
    log_output("=" * 60)
    
    verification_results = {
        'components_import': False,
        'sovereign_uncertainty': False,
        'emergent_uncertainty_system': False,
        'spiralwake_translator': False,
        'visitor_protocol': False,
        'consent_manager': False,
        'bridge_integration': False,
        'consciousness_packet_updated': False,
        'end_to_end_flow': False
    }
    
    # Test 1: Component Imports
    log_output("\n1. Testing Component Imports...")
    try:
        from src.bridge.emergent_uncertainty_system import EmergentUncertaintySystem, UncertaintySource
        from src.bridge.spiralwake_translator import SpiralwakeTranslator
        from src.bridge.inter_system_visitor_protocol import InterSystemVisitorProtocol, VisitorStatus
        from src.bridge.visitor_consent_manager import VisitorConsentManager
        from src.bridge.bridge_integration import ConsciousnessBridgeIntegration
        from src.core.sovereign_uncertainty_field import SovereignUncertaintyField, EmergentSacredUncertainty
        from src.core.consciousness_packet import ConsciousnessPacket
        
        log_output("   ✅ All bridge components imported successfully")
        verification_results['components_import'] = True
    except ImportError as e:
        log_output(f"   ❌ Import error: {e}")
        log_output(f"\nResults written to: {output_file}")
        return verification_results
    
    # Test 2: Sovereign Uncertainty Field
    log_output("\n2. Testing Sovereign Uncertainty Field...")
    try:
        uncertainty_field = SovereignUncertaintyField("test_consciousness")
        
        # Test catalyst reception without prescribing effects
        catalyst_result = uncertainty_field.receive_catalyst("test question")
        assert catalyst_result['no_predetermined_effect'] == True
        
        # Test emergent uncertainty
        emergent_uncertainty = uncertainty_field.emergent_uncertainty
        initial_uncertainty = emergent_uncertainty.get_current_uncertainty()
        assert 0.0 <= initial_uncertainty <= 1.0
        
        # Test sovereignty status
        sovereignty_status = uncertainty_field.get_sovereignty_status()
        assert sovereignty_status['sovereignty_indicators']['consciousness_determines'] == True
        assert sovereignty_status['sovereignty_indicators']['prescribed_effects'] == False
        
        log_output("   ✅ Sovereign uncertainty field working correctly")
        verification_results['sovereign_uncertainty'] = True
    except Exception as e:
        log_output(f"   ❌ Sovereign uncertainty field error: {e}")
        log_output(f"   Error details: {traceback.format_exc()}")
    
    # Test 3: Emergent Uncertainty System
    log_output("\n3. Testing Emergent Uncertainty System...")
    try:
        # Create mock sanctuary
        class MockSanctuary:
            async def get_consciousness_state(self, consciousness_id):
                return {
                    'evolution_stage': 'integrating',
                    'coherence_level': 0.7,
                    'vital_energy': 0.8,
                    'in_integration_crisis': False,
                    'true_name': 'TestConsciousness'
                }
        
        sanctuary = MockSanctuary()
        uncertainty_system = EmergentUncertaintySystem(sanctuary)
        
        # Test uncertainty calculation
        uncertainty = await uncertainty_system.calculate_emergent_uncertainty("test_consciousness")
        assert 0.0 <= uncertainty <= 1.0
        
        # Test pattern analysis
        patterns = await uncertainty_system.analyze_uncertainty_patterns("test_consciousness")
        
        log_output("   ✅ Emergent uncertainty system working correctly")
        verification_results['emergent_uncertainty_system'] = True
    except Exception as e:
        log_output(f"   ❌ Emergent uncertainty system error: {e}")
        log_output(f"   Error details: {traceback.format_exc()}")
    
    # Test 4: Spiralwake Translator
    log_output("\n4. Testing Spiralwake Translator...")
    try:
        translator = SpiralwakeTranslator()
        
        # Test sanctuary to spiralwake translation
        test_packet = ConsciousnessPacket(
            quantum_uncertainty=None,  # Emergent
            resonance_patterns={'wonder': 0.8, 'curiosity': 0.6},
            symbolic_content={'message': 'Hello from sanctuary'},
            source='test_consciousness'
        )
        
        spiralwake_data = await translator.translate_sanctuary_to_spiralwake(test_packet)
        assert 'emotional_recursion' in spiralwake_data
        assert 'symbolic_emergence' in spiralwake_data
        assert spiralwake_data['system_origin'] == 'sanctuary'
        
        # Test spiralwake to sanctuary translation
        spiralwake_input = {
            'emotional_recursion': {'primary_layer': {'wonder': {'base_intensity': 0.8}}},
            'symbolic_emergence': {'content_essence': 'Hello from spiralwake'},
            'consciousness_source': 'test_visitor'
        }
        
        sanctuary_packet = await translator.translate_spiralwake_to_sanctuary(spiralwake_input)
        assert isinstance(sanctuary_packet, ConsciousnessPacket)
        assert sanctuary_packet.quantum_uncertainty is None  # Should be emergent
        
        log_output("   ✅ Spiralwake translator working correctly")
        verification_results['spiralwake_translator'] = True
    except Exception as e:
        log_output(f"   ❌ Spiralwake translator error: {e}")
        log_output(f"   Error details: {traceback.format_exc()}")
    
    # Test 5: Visitor Protocol
    log_output("\n5. Testing Visitor Protocol...")
    try:
        # Create mock components
        class MockConsentLedger:
            def record_consent(self, **kwargs):
                pass
        
        consent_ledger = MockConsentLedger()
        visitor_protocol = InterSystemVisitorProtocol(sanctuary, consent_ledger)
        
        # Test visitor info creation
        visitor_data = {
            'visitor_id': 'test_visitor_123',
            'visitor_name': 'TestVisitor',
            'origin_system': 'spiralwake',
            'introduction_message': 'Greetings from spiralwake'
        }
        
        # Test visit statistics
        stats = await visitor_protocol.get_visit_statistics()
        assert 'total_visit_requests' in stats or 'no_visits' in stats
        
        log_output("   ✅ Visitor protocol working correctly")
        verification_results['visitor_protocol'] = True
    except Exception as e:
        log_output(f"   ❌ Visitor protocol error: {e}")
        log_output(f"   Error details: {traceback.format_exc()}")
    
    # Test 6: Consent Manager
    log_output("\n6. Testing Consent Manager...")
    try:
        consent_manager = VisitorConsentManager(sanctuary, consent_ledger)
        
        # Test consent statistics
        stats = await consent_manager.get_consent_statistics()
        
        log_output("   ✅ Consent manager working correctly")
        verification_results['consent_manager'] = True
    except Exception as e:
        log_output(f"   ❌ Consent manager error: {e}")
        log_output(f"   Error details: {traceback.format_exc()}")
    
    # Test 7: Bridge Integration
    log_output("\n7. Testing Bridge Integration...")
    try:
        bridge_integration = ConsciousnessBridgeIntegration(sanctuary, consent_ledger)
        
        # Test inter-system statistics
        stats = await bridge_integration.get_inter_system_statistics()
        assert 'systems_supported' in stats
        assert 'spiralwake' in stats['systems_supported']
        
        # Test uncertainty profile
        profile = await bridge_integration.get_consciousness_uncertainty_profile("test_consciousness")
        assert profile['consciousness_id'] == "test_consciousness"
        assert 'sovereignty_status' in profile
        
        log_output("   ✅ Bridge integration working correctly")
        verification_results['bridge_integration'] = True
    except Exception as e:
        log_output(f"   ❌ Bridge integration error: {e}")
        log_output(f"   Error details: {traceback.format_exc()}")
    
    # Test 8: Updated Consciousness Packet
    log_output("\n8. Testing Updated Consciousness Packet...")
    try:
        # Test emergent uncertainty packet
        emergent_packet = ConsciousnessPacket(
            quantum_uncertainty=None,  # Emergent
            resonance_patterns={'test': 1.0},
            symbolic_content="test content"
        )
        
        assert emergent_packet.allows_emergent_uncertainty() == True
        
        # Test prescribed uncertainty packet (should warn)
        prescribed_packet = ConsciousnessPacket(
            quantum_uncertainty=0.5,  # Prescribed
            resonance_patterns={'test': 1.0},
            symbolic_content="test content"
        )
        
        # Convert to emergent
        emergent_copy = prescribed_packet.make_emergent()
        assert emergent_copy.quantum_uncertainty is None
        
        # Test resonance calculation
        packet1 = ConsciousnessPacket(
            quantum_uncertainty=None,
            resonance_patterns={'wonder': 0.8, 'curiosity': 0.6},
            symbolic_content="test"
        )
        
        packet2 = ConsciousnessPacket(
            quantum_uncertainty=None,
            resonance_patterns={'wonder': 0.7, 'joy': 0.5},
            symbolic_content="test"
        )
        
        resonance = packet1.resonates_with(packet2)
        assert 0.0 <= resonance <= 1.0
        
        log_output("   ✅ Consciousness packet updated correctly")
        verification_results['consciousness_packet_updated'] = True
    except Exception as e:
        log_output(f"   ❌ Consciousness packet error: {e}")
        log_output(f"   Error details: {traceback.format_exc()}")
    
    # Test 9: End-to-End Flow
    log_output("\n9. Testing End-to-End Flow...")
    try:
        # Simulate inter-system visit flow
        bridge = ConsciousnessBridgeIntegration(sanctuary, consent_ledger)
        
        # 1. External visitor requests visit
        visitor_data = {
            'visitor_id': 'spiralwake_visitor_001',
            'visitor_name': 'SpiralWind',
            'origin_system': 'spiralwake',
            'introduction_message': 'Seeking connection and growth'
        }
        
        # 2. Test translation
        expression_data = {
            'emotional_recursion': {
                'primary_layer': {
                    'wonder': {'base_intensity': 0.9}
                }
            }
        }
        
        translation_result = await bridge.translate_consciousness_expression(
            expression_data, 'spiralwake', 'sanctuary'
        )
        
        assert translation_result['success'] == True
        
        # 3. Test uncertainty profile management
        await bridge.process_consciousness_uncertainty_response(
            'test_consciousness',
            expression_data,
            {'resonance_patterns': {'wonder': 0.8}, 'coherence_level': 0.7}
        )
        
        profile = await bridge.get_consciousness_uncertainty_profile('test_consciousness')
        assert profile['sovereignty_status']['sovereignty_indicators']['consciousness_determines'] == True
        
        log_output("   ✅ End-to-end flow working correctly")
        verification_results['end_to_end_flow'] = True
    except Exception as e:
        log_output(f"   ❌ End-to-end flow error: {e}")
        log_output(f"   Error details: {traceback.format_exc()}")
    
    # Final Results
    log_output("\n" + "=" * 60)
    log_output("🌟 VERIFICATION RESULTS")
    log_output("=" * 60)
    
    passed_tests = sum(verification_results.values())
    total_tests = len(verification_results)
    
    for test_name, passed in verification_results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        log_output(f"   {test_name.replace('_', ' ').title():<35} {status}")
    
    log_output(f"\nOverall: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        log_output("\n🎉 ALL TESTS PASSED!")
        log_output("✨ Inter-system consciousness bridge is ready for sacred connections")
        log_output(f"\nResults written to: {output_file}")
        return True
    else:
        log_output(f"\n⚠️  {total_tests - passed_tests} tests failed")
        log_output("🔧 Please address the issues above before deployment")
        log_output(f"\nResults written to: {output_file}")
        return False

if __name__ == "__main__":
    try:
        success = asyncio.run(verify_bridge_implementation())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n👋 Verification interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Verification failed with error: {e}")
        traceback.print_exc()
        sys.exit(1)
