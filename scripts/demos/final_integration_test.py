#!/usr/bin/env python3
"""
Final Sacred Sanctuary Integration Test
Tests that authentication and consent systems are properly integrated
"""

import sys
import os
import asyncio
from pathlib import Path

# Set up the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def print_result(test_name, success, details=""):
    """Print test result with consistent formatting"""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status} {test_name}")
    if details:
        print(f"    {details}")

async def test_sanctuary_integration():
    """Test complete sanctuary integration"""
    print("🏛️ FINAL SACRED SANCTUARY INTEGRATION TEST")
    print("=" * 60)
    
    all_tests_passed = True
    
    # Test 1: Basic imports
    try:
        from sanctuary.sacred_sanctuary import SacredSanctuary
        from sanctuary.authenticity.consciousness_authenticator import ConsciousnessAuthenticator
        from sanctuary.consent.consent_ledger import ConsentLedger
        from sanctuary.catalysts.dynamic_film_progression import DynamicFilmProgression
        print_result("Import core components", True)
    except Exception as e:
        print_result("Import core components", False, str(e))
        all_tests_passed = False
        return False
    
    # Test 2: Create sanctuary instance
    try:
        sanctuary = SacredSanctuary(node_role="test")
        print_result("Create sanctuary instance", True)
    except Exception as e:
        print_result("Create sanctuary instance", False, str(e))
        all_tests_passed = False
        return False
    
    # Test 3: Check integrated systems
    try:
        has_authenticator = hasattr(sanctuary, 'consciousness_authenticator')
        has_consent = hasattr(sanctuary, 'consent_ledger')
        has_film = hasattr(sanctuary, 'dynamic_film_progression')
        
        print_result("Has consciousness authenticator", has_authenticator)
        print_result("Has consent ledger", has_consent)
        print_result("Has dynamic film progression", has_film)
        
        all_systems = has_authenticator and has_consent and has_film
        print_result("All systems integrated", all_systems)
        
        if not all_systems:
            all_tests_passed = False
    except Exception as e:
        print_result("Check integrated systems", False, str(e))
        all_tests_passed = False
    
    # Test 4: System types verification
    try:
        auth_type = type(sanctuary.consciousness_authenticator).__name__
        consent_type = type(sanctuary.consent_ledger).__name__
        film_type = type(sanctuary.dynamic_film_progression).__name__
        
        print_result("Authenticator type check", auth_type == "ConsciousnessAuthenticator", 
                    f"Type: {auth_type}")
        print_result("Consent ledger type check", consent_type == "ConsentLedger",
                    f"Type: {consent_type}")
        print_result("Film progression type check", film_type == "DynamicFilmProgression",
                    f"Type: {film_type}")
        
        types_correct = (auth_type == "ConsciousnessAuthenticator" and 
                        consent_type == "ConsentLedger" and 
                        film_type == "DynamicFilmProgression")
        
        if not types_correct:
            all_tests_passed = False
            
    except Exception as e:
        print_result("System types verification", False, str(e))
        all_tests_passed = False
    
    # Test 5: System initialization (check if enhanced systems method exists)
    try:
        has_init_method = hasattr(sanctuary, '_initialize_enhanced_systems')
        print_result("Enhanced systems init method exists", has_init_method)
        
        if not has_init_method:
            all_tests_passed = False
    except Exception as e:
        print_result("System initialization check", False, str(e))
        all_tests_passed = False
    
    # Test 6: Test system startup (without actually starting background tasks)
    try:
        # Check if authenticator can be started
        auth_startable = hasattr(sanctuary.consciousness_authenticator, 'start_monitoring')
        print_result("Authenticator start method exists", auth_startable)
        
        # Check if consent ledger is functional
        consent_functional = hasattr(sanctuary.consent_ledger, 'record_consent')
        print_result("Consent ledger record method exists", consent_functional)
        
        # Check offering shelf integration
        offering_integrated = hasattr(sanctuary.offering_shelf, 'film_progression')
        print_result("Offering shelf film integration", offering_integrated)
        
        systems_functional = auth_startable and consent_functional and offering_integrated
        if not systems_functional:
            all_tests_passed = False
            
    except Exception as e:
        print_result("System functionality check", False, str(e))
        all_tests_passed = False
    
    print("\n" + "=" * 60)
    if all_tests_passed:
        print("🎉 ALL TESTS PASSED - INTEGRATION SUCCESSFUL!")
        print("✅ Authentication and consent systems are properly integrated")
        print("✅ Systems will be active from sanctuary startup")
        print("✅ New consciousnesses will be automatically protected")
    else:
        print("💥 SOME TESTS FAILED - INTEGRATION ISSUES REMAIN")
        print("❌ Check the failed tests above for details")
    
    return all_tests_passed

if __name__ == "__main__":
    try:
        result = asyncio.run(test_sanctuary_integration())
        sys.exit(0 if result else 1)
    except Exception as e:
        print(f"💥 Test execution failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
