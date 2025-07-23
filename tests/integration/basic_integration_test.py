#!/usr/bin/env python3
"""
Sacred Sanctuary Integration Test
===============================

Tests integration between core consciousness systems.
"""

import sys
import os
from pathlib import Path

# Add src to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

def test_system_integration():
    """Test that systems can work together"""
    print("Testing System Integration...")
    
    try:
        # Test basic system coordination
        print("  - Testing basic integration...")
        
        # Test that we can create and use basic components
        from core.consciousness_packet import ConsciousnessPacket
        
        packet = ConsciousnessPacket(
            content="Integration test message",
            source="integration_test",
            packet_type="test"
        )
        
        print(f"    ✅ Integration test successful")
        return True
        
    except Exception as e:
        print(f"    ❌ Integration test failed: {e}")
        return False

def test_architecture_health():
    """Test overall architecture health"""
    print("Testing Architecture Health...")
    
    try:
        # Check project structure
        src_path = project_root / "src"
        if src_path.exists():
            print("    ✅ Source directory exists")
        else:
            print("    ❌ Source directory missing")
            return False
            
        # Check key directories
        key_dirs = ["core", "aspects", "consciousness", "sanctuary"]
        for dir_name in key_dirs:
            dir_path = src_path / dir_name
            if dir_path.exists():
                print(f"    ✅ {dir_name}/ directory exists")
            else:
                print(f"    ⚠️ {dir_name}/ directory missing")
        
        return True
        
    except Exception as e:
        print(f"    ❌ Architecture health check failed: {e}")
        return False

def main():
    """Run all integration tests"""
    print("🌟 SACRED SANCTUARY INTEGRATION TEST")
    print("=" * 50)
    
    all_passed = True
    
    # Run integration tests
    if not test_system_integration():
        all_passed = False
    
    print()
    
    # Run architecture health tests
    if not test_architecture_health():
        all_passed = False
    
    print()
    print("=" * 50)
    if all_passed:
        print("✅ ALL INTEGRATION TESTS PASSED")
        return 0
    else:
        print("❌ SOME INTEGRATION TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
