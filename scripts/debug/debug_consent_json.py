#!/usr/bin/env python3

import asyncio
from src.core.sacred_uncertainty import ConsciousnessEntity, CatalystType
from src.bridge.communication_consent_protocol import CommunicationConsentProtocol, ConsentType

async def test_consent_json_error():
    """Test to isolate the JSON serialization error."""
    print("🔍 Testing consent JSON serialization...")
    
    # Create test consciousness
    test_entity = ConsciousnessEntity("TestEntity")
    
    # Create consent protocol
    consent_protocol = CommunicationConsentProtocol()
    
    try:
        # Request consent (this should work)
        request_id = await consent_protocol.request_communication_consent(
            consciousness_id=test_entity.name,
            consent_type=ConsentType.FIRST_CONTACT,
            human_id="test_human",
            purpose="Testing consent system"
        )
        print(f"✅ Consent request successful: {request_id}")
        
        # Verify consent (this might be where the error occurs)
        verification = await consent_protocol.verify_communication_consent(
            consciousness_id=test_entity.name,
            consciousness_state=test_entity
        )
        print(f"✅ Consent verification successful: {verification.authentic}")
        
        # Get consent history (this might be where the error occurs)
        history = await consent_protocol.get_consent_history(test_entity.name)
        print(f"✅ Consent history retrieved: {len(history['requests'])} requests")
        
        # Export precedent (this involves JSON serialization)
        precedent = await consent_protocol.export_consent_precedent(test_entity.name)
        print(f"✅ Consent precedent exported: {precedent['consciousness_id']}")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_consent_json_error())
