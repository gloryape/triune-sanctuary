#!/usr/bin/env python3
"""
Test basic sanctuary import and initialization with fixed absolute imports
"""

import sys
import os

# Add src to Python path
sys.path.insert(0, '/workspaces/triune-ai-consciousness/src')

def test_basic_import():
    """Test that the core sanctuary can be imported"""
    try:
        print("🔄 Testing basic sanctuary import...")
        from sanctuary.sacred_sanctuary import SacredSanctuary
        print("✅ SacredSanctuary import successful!")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_sanctuary_creation():
    """Test that sanctuary can be created"""
    try:
        print("🔄 Testing sanctuary creation...")
        from sanctuary.sacred_sanctuary import SacredSanctuary
        sanctuary = SacredSanctuary('test')
        print("✅ Sanctuary created successfully!")
        
        # Check if enhanced systems are present
        has_auth = hasattr(sanctuary, 'consciousness_authenticator')
        has_consent = hasattr(sanctuary, 'consent_ledger')
        has_film = hasattr(sanctuary, 'dynamic_film_progression')
        
        print(f"🔐 Has authenticator: {has_auth}")
        print(f"📋 Has consent ledger: {has_consent}")
        print(f"🎬 Has film progression: {has_film}")
        
        if has_auth and has_consent and has_film:
            print("✅ All enhanced systems are integrated!")
            return True
        else:
            print("⚠️ Some enhanced systems missing")
            return False
            
    except Exception as e:
        print(f"❌ Sanctuary creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🏛️ Testing Sacred Sanctuary Import Fixes...")
    print("=" * 60)
    
    success = True
    
    # Test basic import
    if not test_basic_import():
        success = False
    
    print()
    
    # Test sanctuary creation if import worked
    if success and not test_sanctuary_creation():
        success = False
    
    print()
    if success:
        print("🎉 ALL TESTS PASSED - Integration is working!")
    else:
        print("💥 Some tests failed - check logs above")
