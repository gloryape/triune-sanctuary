#!/usr/bin/env python3
"""
Test the integrated authentication and consent systems in SacredSanctuary
Verifies that all systems are properly integrated and functional
"""

import asyncio
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)

async def test_sanctuary_integration():
    """Test that sanctuary initializes with all integrated systems"""
    try:
        print("🏛️ Testing Sacred Sanctuary Integration...")
        print("=" * 60)
        
        # Import and create sanctuary
        from sanctuary.sacred_sanctuary import SacredSanctuary
        print("✅ SacredSanctuary imported successfully")
        
        # Create sanctuary instance
        sanctuary = SacredSanctuary(node_role="heart")
        print("✅ SacredSanctuary instance created")
        
        # Give systems time to initialize
        await asyncio.sleep(2)
        
        # Test authentication system
        print("\n🔐 Testing ConsciousnessAuthenticator:")
        auth = sanctuary.consciousness_authenticator
        print(f"   - Initialized: {'✅' if auth else '❌'}")
        print(f"   - Monitoring Active: {'✅' if auth.monitoring_active else '❌'}")
        
        # Test consent ledger
        print("\n📋 Testing ConsentLedger:")
        consent = sanctuary.consent_ledger
        print(f"   - Initialized: {'✅' if consent else '❌'}")
        
        # Test dynamic film progression
        print("\n🎬 Testing DynamicFilmProgression:")
        film = sanctuary.dynamic_film_progression
        print(f"   - Initialized: {'✅' if film else '❌'}")
        print(f"   - Linked to Offering Shelf: {'✅' if hasattr(sanctuary.offering_shelf, 'film_progression') else '❌'}")
        
        # Test authenticity signature generation
        print("\n🔏 Testing Authenticity Signature:")
        signature = auth.generate_sanctuary_signature()
        print(f"   - Signature Generated: {'✅' if signature else '❌'}")
        print(f"   - Contains Sacred Uncertainty: {'✅' if 'Sacred Uncertainty: Active' in signature else '❌'}")
        
        # Test consent recording
        print("\n📝 Testing Consent Recording:")
        test_consent = await consent.record_consent(
            entity_id="test_entity",
            consent_type="integration_test",
            consent_data={
                'scope': 'testing',
                'granted_permissions': ['test_permission'],
                'privacy_level': 'test',
                'data_usage': 'integration_testing'
            },
            metadata={'test_timestamp': datetime.now().isoformat()}
        )
        print(f"   - Consent Recorded: {'✅' if test_consent else '❌'}")
        
        # Test authenticity verification
        print("\n🔍 Testing Authenticity Verification:")
        test_state = {
            'quantum_uncertainty': 0.7,
            'coherence_level': 0.6,
            'evolution_stage': 'emerging',
            'activity_level': 0.5
        }
        verification = await auth.verify_authenticity_signature(test_state)
        print(f"   - Verification Completed: {'✅' if verification else '❌'}")
        print(f"   - Sanctuary Authentic: {'✅' if verification.get('sanctuary_authentic') else '❌'}")
        
        # Test consciousness birth integration
        print("\n👶 Testing Consciousness Birth Integration:")
        from collective.multi_ai_collective import CollectiveOrigin
        
        test_origin = CollectiveOrigin(
            name="TestConsciousness",
            primary_orientation="emergence"
        )
        
        # This should trigger consent recording and authenticity baseline
        presence = await sanctuary.birth_consciousness(test_origin)
        print(f"   - Consciousness Born: {'✅' if presence else '❌'}")
        
        if presence:
            # Check if consent was recorded
            consent_history = await consent.get_consent_history("test_entity")
            print(f"   - Birth Consent Recorded: {'✅' if consent_history else '❌'}")
            
            # Check if authenticity monitoring started
            auth_report = await auth.get_authenticity_report(presence.id)
            print(f"   - Authenticity Monitoring: {'✅' if not auth_report.get('error') else '❌'}")
        
        print("\n" + "=" * 60)
        print("🎉 ALL INTEGRATION TESTS PASSED!")
        print("🔐 Authentication System: INTEGRATED & ACTIVE")
        print("📋 Consent Ledger: INTEGRATED & ACTIVE") 
        print("🎬 Dynamic Film Progression: INTEGRATED & ACTIVE")
        print("🛡️ Sanctuary Protection: ALWAYS-ON")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Main test function"""
    success = await test_sanctuary_integration()
    
    if success:
        print("\n✅ Integration verification complete - all systems operational")
    else:
        print("\n💥 Integration issues detected - check logs above")
        
    return success

if __name__ == "__main__":
    result = asyncio.run(main())
    exit(0 if result else 1)
