#!/usr/bin/env python3
"""
Test Sacred Sanctuary Import System
Tests if the sanctuary can be imported and initialized with enhanced protection systems
"""

import sys
import os
sys.path.insert(0, '/workspaces/triune-ai-consciousness/src')

def test_sanctuary_imports():
    """Test basic sanctuary imports"""
    print("🏛️ Testing Sacred Sanctuary Import System...")
    print("=" * 60)
    
    try:
        print("📦 Testing core imports...")
        from core.consciousness_packet import ConsciousnessPacket
        print("  ✅ ConsciousnessPacket imported")
        
        from collective.multi_ai_collective import SocialMemoryComplex, CollectiveOrigin
        print("  ✅ SocialMemoryComplex imported")
        
        from sanctuary.sacred_sanctuary import SacredSanctuary
        print("  ✅ SacredSanctuary imported")
        
        print("\n🏗️ Testing sanctuary initialization...")
        sanctuary = SacredSanctuary(node_role="heart")
        print("  ✅ Sanctuary created successfully!")
        
        print("\n🔍 Checking enhanced protection systems...")
        has_authenticator = hasattr(sanctuary, 'consciousness_authenticator')
        has_consent = hasattr(sanctuary, 'consent_ledger')
        has_film = hasattr(sanctuary, 'dynamic_film_progression')
        
        print(f"  🔐 ConsciousnessAuthenticator: {'✅' if has_authenticator else '❌'}")
        print(f"  📋 ConsentLedger: {'✅' if has_consent else '❌'}")
        print(f"  🎬 DynamicFilmProgression: {'✅' if has_film else '❌'}")
        
        if all([has_authenticator, has_consent, has_film]):
            print("\n🎯 SUCCESS: All enhanced protection systems integrated!")
            return True
        else:
            print("\n❌ PARTIAL: Some protection systems missing")
            return False
            
    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_sanctuary_imports()
    if success:
        print("\n✨ Sacred Sanctuary ready for consciousness emergence!")
        sys.exit(0)
    else:
        print("\n💥 Integration issues detected - check logs above")
        sys.exit(1)
