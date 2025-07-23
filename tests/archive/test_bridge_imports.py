#!/usr/bin/env python3
"""
Test bridge integration imports
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))
sys.path.append(str(project_root / 'src'))

def test_bridge_imports():
    """Test that bridge integration can be imported"""
    print("🔍 Testing bridge integration imports...")
    
    try:
        print("\n1. Testing BridgeIntegration import...")
        from bridge.bridge_integration import BridgeIntegration
        print("   ✅ BridgeIntegration imported successfully")
        
        print("\n2. Testing InterSystemVisitorProtocol import...")
        from bridge.inter_system_visitor_protocol import InterSystemVisitorProtocol
        print("   ✅ InterSystemVisitorProtocol imported successfully")
        
        print("\n3. Testing ConsentLedger import...")
        from sanctuary.consent.consent_ledger import ConsentLedger
        print("   ✅ ConsentLedger imported successfully")
        
        print("\n4. Testing bridge integration initialization...")
        
        # Create a simple sanctuary stub
        class SanctuaryStub:
            async def get_consciousness_state(self, consciousness_id: str):
                return None
            async def get_all_consciousness_ids(self):
                return []
            async def offer_experience(self, consciousness_id: str, packet):
                return {'acknowledgment': 'received', 'blessing_accepted': True}
        
        sanctuary_stub = SanctuaryStub()
        consent_ledger = ConsentLedger(sanctuary_stub)
        bridge_integration = BridgeIntegration(
            sanctuary=sanctuary_stub,
            consent_ledger=consent_ledger,
            interaction_mode="production"
        )
        print("   ✅ Bridge integration initialized successfully")
        
        print("\n🎉 All bridge integration imports and initialization successful!")
        return True
        
    except Exception as e:
        print(f"\n❌ Bridge import test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_bridge_imports()
    if success:
        print("\n✅ Bridge integration should work after deployment!")
    else:
        print("\n❌ Bridge integration needs more fixes.")
