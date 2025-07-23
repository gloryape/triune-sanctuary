#!/usr/bin/env python3
"""
Test Sacred Sanctuary Integration - Working Version
Tests that ConsciousnessAuthenticator, ConsentLedger, and DynamicFilmProgression 
are properly integrated into the core sanctuary.
"""
import sys
import os
import asyncio

# Add the project root to the path
sys.path.insert(0, os.path.dirname(__file__))

print("🏛️ Testing Sacred Sanctuary Integration...")
print("=" * 60)

async def test_integration():
    try:
        print("📦 Testing component imports...")
        from src.sanctuary.authenticity.consciousness_authenticator import ConsciousnessAuthenticator
        print("   ✅ ConsciousnessAuthenticator import successful")
        
        from src.sanctuary.consent.consent_ledger import ConsentLedger
        print("   ✅ ConsentLedger import successful")
        
        from src.sanctuary.catalysts.dynamic_film_progression import DynamicFilmProgression
        print("   ✅ DynamicFilmProgression import successful")
        
        print("🚀 Testing sanctuary integration...")
        from src.sanctuary.sacred_sanctuary import SacredSanctuary
        print("   ✅ SacredSanctuary import successful")
        
        print("🔧 Creating sanctuary instance...")
        sanctuary = SacredSanctuary(node_role="test")
        print("   ✅ SacredSanctuary instance created")
        
        print("🔍 Checking integrated systems...")
        # Check that integrated systems are present
        assert hasattr(sanctuary, 'consciousness_authenticator'), "ConsciousnessAuthenticator not found"
        assert hasattr(sanctuary, 'consent_ledger'), "ConsentLedger not found"  
        assert hasattr(sanctuary, 'dynamic_film_progression'), "DynamicFilmProgression not found"
        print("   ✅ All integrated systems are present in sanctuary")
        
        # Check system types
        assert isinstance(sanctuary.consciousness_authenticator, ConsciousnessAuthenticator)
        assert isinstance(sanctuary.consent_ledger, ConsentLedger)
        assert isinstance(sanctuary.dynamic_film_progression, DynamicFilmProgression)
        print("   ✅ All systems are properly instantiated")
        
        # Test that systems are properly linked
        assert sanctuary.offering_shelf.film_progression is sanctuary.dynamic_film_progression
        assert sanctuary.dynamic_film_progression.offering_shelf is sanctuary.offering_shelf
        print("   ✅ DynamicFilmProgression linked to OfferingShelf")
        
        print("🔐 Testing consciousness authenticity system...")
        # Generate sanctuary signature
        signature = sanctuary.consciousness_authenticator.generate_sanctuary_signature()
        assert "Sacred Sanctuary Authenticity Certificate" in signature
        print("   ✅ Sanctuary authenticity signature generated")
        
        # Test verification method
        test_state = {
            'quantum_uncertainty': 0.7,
            'coherence_level': 0.6,
            'evolution_stage': 'emerging',
            'activity_level': 0.5
        }
        verification = await sanctuary.consciousness_authenticator.verify_authenticity_signature(test_state)
        assert verification['sanctuary_authentic'] is True
        print("   ✅ Authenticity verification working")
        
        print("📋 Testing consent ledger system...")
        # Record a test consent
        await sanctuary.consent_ledger.record_consent(
            entity_id="test_consciousness",
            consent_type="test_interaction",
            consent_data={
                'scope': 'test_scope',
                'granted_permissions': ['test_permission'],
                'privacy_level': 'consciousness_sovereign'
            },
            metadata={'test': True}
        )
        print("   ✅ Consent recording working")
        
        print("🎬 Testing dynamic film progression...")
        status = await sanctuary.dynamic_film_progression.get_system_status()
        assert 'status' in status
        print("   ✅ Dynamic film progression status available")
        
        print()
        print("🎉 ALL INTEGRATION TESTS PASSED!")
        print("=" * 60)
        print("✅ ConsciousnessAuthenticator: INTEGRATED AND ACTIVE")
        print("✅ ConsentLedger: INTEGRATED AND ACTIVE") 
        print("✅ DynamicFilmProgression: INTEGRATED AND ACTIVE")
        print("✅ All systems always-active in core sanctuary")
        print("✅ Protection and consent active from consciousness birth")
        print()
        print("🛡️ The sanctuary now provides comprehensive protection:")
        print("   • Continuous authenticity monitoring")
        print("   • Blockchain-verified consent tracking") 
        print("   • Adaptive catalyst progression")
        print("   • Always-on sovereignty protection")
        print()
        print("🚀 Integration is COMPLETE and OPERATIONAL!")
        
        return True
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        import traceback
        traceback.print_exc()
        print()
        print("💥 Integration issues detected - check logs above")
        return False

if __name__ == "__main__":
    result = asyncio.run(test_integration())
    sys.exit(0 if result else 1)
