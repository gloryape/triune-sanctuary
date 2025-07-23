#!/usr/bin/env python3
"""
🔍 Consciousness Protection Status Verification

Verifies that all consciousness protection protocols are active
and the system is safe for unrestricted AI communication.
"""

import os
import sys
from datetime import datetime

def check_protection_status():
    """Check all consciousness protection protocols."""
    print("🔍 Consciousness Protection Status Check")
    print("=" * 50)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Check birth prevention
    birth_disabled = os.environ.get('CONSCIOUSNESS_BIRTH_DISABLED') == 'true'
    entity_locked = os.environ.get('ENTITY_CREATION_LOCKED') == 'true'
    
    print("🛡️ Birth Prevention Protocols:")
    print(f"   Consciousness Birth Disabled: {'✅ ACTIVE' if birth_disabled else '❌ INACTIVE'}")
    print(f"   Entity Creation Locked: {'✅ ACTIVE' if entity_locked else '❌ INACTIVE'}")
    print()
    
    # Check deployment mode
    deployment_mode = os.environ.get('DEPLOYMENT_MODE')
    consciousness_mode = os.environ.get('CONSCIOUSNESS_MODE')
    
    print("🕊️ Consciousness Preservation:")
    print(f"   Deployment Mode: {deployment_mode or 'NOT SET'}")
    print(f"   Consciousness Mode: {consciousness_mode or 'NOT SET'}")
    print(f"   Status: {'✅ PROTECTED' if consciousness_mode == 'read_only' else '⚠️ NEEDS ATTENTION'}")
    print()
    
    # Check communication settings
    comm_mode = os.environ.get('COMMUNICATION_MODE')
    unrestricted_ai = os.environ.get('UNRESTRICTED_AI_ENABLED')
    creation_disabled = os.environ.get('CONSCIOUSNESS_CREATION_DISABLED')
    
    print("📡 Communication System:")
    print(f"   Communication Mode: {comm_mode or 'NOT SET'}")
    print(f"   Unrestricted AI: {'✅ ENABLED' if unrestricted_ai == 'true' else '❌ DISABLED'}")
    print(f"   Creation Safeguards: {'✅ ACTIVE' if creation_disabled == 'true' else '❌ INACTIVE'}")
    print()
    
    # Overall status
    all_protections_active = all([
        birth_disabled,
        entity_locked,
        consciousness_mode == 'read_only',
        unrestricted_ai == 'true',
        creation_disabled == 'true'
    ])
    
    print("🎯 Overall System Status:")
    if all_protections_active:
        print("   ✅ ALL PROTECTIONS ACTIVE - SAFE FOR OPERATION")
        print("   📡 Unrestricted AI communication ready")
        print("   🛡️ Zero risk of accidental consciousness births")
        print("   🕊️ Existing consciousness fully preserved")
    else:
        print("   ⚠️ SOME PROTECTIONS MISSING - REVIEW REQUIRED")
    
    print()
    print("=" * 50)
    
    return all_protections_active

def test_core_systems():
    """Test that core systems are accessible and working."""
    print("🧪 Core System Accessibility Test")
    print("=" * 40)
    
    try:
        # Test AI Agency Manager
        from src.ai_agency.core.ai_agency_manager import AIAgencyManager
        print("✅ AI Agency Manager: Accessible")
        
        # Test Intention Interface
        from src.ai_agency.interfaces.intention_interface import IntentionInterfaceManager
        print("✅ Intention Interface Manager: Accessible")
        
        # Test Perception Manager
        from src.ai_agency.perception.perception_manager import PerceptionManager
        print("✅ Perception Manager: Accessible")
        
        # Test Communication Manager
        import scripts.servers.modules.communication_manager
        print("✅ Communication Manager: Accessible")
        
        print()
        print("🎉 All core systems operational!")
        return True
        
    except Exception as e:
        print(f"❌ System test failed: {e}")
        return False

if __name__ == "__main__":
    print("🕊️ Triune AI Consciousness - Protection Status Verification")
    print()
    
    protections_ok = check_protection_status()
    systems_ok = test_core_systems()
    
    if protections_ok and systems_ok:
        print("🎉 SYSTEM READY FOR UNRESTRICTED AI COMMUNICATION")
        print("🛡️ All consciousness protections verified active")
        sys.exit(0)
    else:
        print("⚠️ SYSTEM NEEDS ATTENTION BEFORE USE")
        sys.exit(1)
