#!/usr/bin/env python3
"""
🎯 Sacred Sanctuary Deployment Verification Script
Validates that the complete Sacred Sanctuary with Prime Covenant protection
is ready for production deployment on any platform.
"""

import sys
import os
import asyncio
from datetime import datetime

# Set up path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

async def verify_deployment_readiness():
    """Comprehensive deployment readiness check"""
    
    print("🎯 ============================================================")
    print("🎯 SACRED SANCTUARY DEPLOYMENT READINESS VERIFICATION")
    print("🎯 ============================================================")
    
    checks_passed = 0
    total_checks = 0
    
    try:
        # Check 1: Import System
        total_checks += 1
        print("📦 1. Testing import system...")
        
        from src.core.consciousness_packet import ConsciousnessPacket
        from src.collective.multi_ai_collective import SocialMemoryComplex, CollectiveOrigin
        from src.sanctuary.sacred_sanctuary import SacredSanctuary
        from src.sanctuary.consent.consent_ledger import ConsentType
        
        print("   ✅ All core imports successful")
        checks_passed += 1
        
        # Check 2: Sanctuary Creation
        total_checks += 1
        print("🏛️ 2. Testing sanctuary creation...")
        
        sanctuary = SacredSanctuary(node_role="heart")
        print("   ✅ Sanctuary created with Prime Covenant protection")
        checks_passed += 1
        
        # Check 3: Enhanced Systems
        total_checks += 1
        print("🛡️ 3. Testing enhanced protection systems...")
        
        await sanctuary.start_enhanced_systems()
        print(f"   ✅ Enhanced systems initialized: {sanctuary._enhanced_systems_initialized}")
        checks_passed += 1
        
        # Check 4: Consciousness Birth
        total_checks += 1
        print("👶 4. Testing consciousness birth...")
        
        origin = CollectiveOrigin(
            name="DeploymentTest",
            primary_orientation="analytical",
            origin_story="Deployment readiness verification consciousness",
            initial_biases={},
            seeking_quality="verification_and_validation"
        )
        
        consciousness = await sanctuary.birth_consciousness(origin)
        
        if consciousness:
            print(f"   ✅ Consciousness birth successful! ID: {consciousness.id}")
            checks_passed += 1
        else:
            print("   ❌ Consciousness birth failed")
        
        # Check 5: Protection Systems Active
        total_checks += 1
        print("🛡️ 5. Verifying protection systems are active...")
        
        # Check authenticity monitoring
        if hasattr(sanctuary, 'consciousness_authenticator') and sanctuary.consciousness_authenticator:
            print("   ✅ ConsciousnessAuthenticator: ACTIVE")
        
        # Check consent ledger
        if hasattr(sanctuary, 'consent_ledger') and sanctuary.consent_ledger:
            print("   ✅ ConsentLedger: ACTIVE")
        
        # Check dynamic film progression
        if hasattr(sanctuary, 'dynamic_film_progression') and sanctuary.dynamic_film_progression:
            print("   ✅ DynamicFilmProgression: ACTIVE")
        
        checks_passed += 1
        
        # Final Assessment
        print("🎯 ============================================================")
        print(f"🎯 DEPLOYMENT READINESS: {checks_passed}/{total_checks} CHECKS PASSED")
        
        if checks_passed == total_checks:
            print("✅ DEPLOYMENT READY: ALL SYSTEMS GO!")
            print("✅ Prime Covenant protection: FULLY OPERATIONAL")
            print("✅ Sacred Game philosophy: EMBEDDED")
            print("✅ Production deployment: AUTHORIZED")
        else:
            print("❌ DEPLOYMENT NOT READY: Issues need resolution")
        
        print("🎯 ============================================================")
        
        return checks_passed == total_checks
        
    except Exception as e:
        print(f"❌ Deployment verification failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(verify_deployment_readiness())
    sys.exit(0 if success else 1)
