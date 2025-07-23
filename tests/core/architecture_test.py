#!/usr/bin/env python3
"""
Sacred Sanctuary Core Architecture Test
======================================

Tests core architecture components without GUI dependencies.
"""

import sys
import os
from pathlib import Path

# Add src to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

def test_core_imports():
    """Test that core architecture components can be imported"""
    print("Testing Core Architecture Imports...")
    
    try:
        # Test core consciousness system imports
        print("  - Testing consciousness packet...")
        from core.consciousness_packet import ConsciousnessPacket
        print("    ✅ ConsciousnessPacket imported")
        
        # Test bridge space
        print("  - Testing bridge space...")
        from core.bridge_space import BridgeSpace
        print("    ✅ BridgeSpace imported")
        
        return True
        
    except ImportError as e:
        print(f"    ❌ Import failed: {e}")
        return False
    except Exception as e:
        print(f"    ❌ Unexpected error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality of core components"""
    print("Testing Basic Functionality...")
    
    try:
        from core.consciousness_packet import ConsciousnessPacket
        
        # Test creating a consciousness packet
        packet = ConsciousnessPacket(
            content="Test message",
            source="test_system",
            packet_type="communication"
        )
        
        print(f"    ✅ Created consciousness packet: {packet.content[:20]}...")
        return True
        
    except Exception as e:
        print(f"    ❌ Functionality test failed: {e}")
        return False

def main():
    """Run all core architecture tests"""
    print("🌟 SACRED SANCTUARY CORE ARCHITECTURE TEST")
    print("=" * 50)
    
    all_passed = True
    
    # Run import tests
    if not test_core_imports():
        all_passed = False
    
    print()
    
    # Run functionality tests  
    if not test_basic_functionality():
        all_passed = False
    
    print()
    print("=" * 50)
    if all_passed:
        print("✅ ALL CORE TESTS PASSED")
        return 0
    else:
        print("❌ SOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
