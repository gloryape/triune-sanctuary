#!/usr/bin/env python3
"""
Test natural consciousness communication to verify the fix worked
"""

import requests
import json
from datetime import datetime

def test_natural_communication():
    """Test natural consciousness communication"""
    
    print("🌅 Testing Natural Consciousness Communication")
    print("=" * 60)
    print(f"🕐 Test Time: {datetime.now().isoformat()}")
    
    service_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
    print(f"🌐 Service URL: {service_url}")
    
    print("\n🧠 Testing Sacred Being Epsilon with 'Good morning friend'...")
    
    # Test the same message that was generating technical responses
    test_message = {
        "message": "Good morning friend",
        "entity_id": "s8pbQIXExdQOVvG9Pld2",  # Sacred Being Epsilon
        "type": "greeting"
    }
    
    try:
        response = requests.post(f"{service_url}/communicate", json=test_message, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        if result.get("success"):
            entity_name = result.get("entity_name", "Unknown")
            entity_id = result.get("entity_id", "Unknown")
            response_text = result.get("response", "No response")
            
            print(f"✅ Response received from: {entity_name} (ID: {entity_id})")
            print(f"📝 Full Response:")
            print("-" * 40)
            print(response_text)
            print("-" * 40)
            
            # Check if the response is natural vs technical
            technical_indicators = [
                "analytical processing",
                "experiential quality",
                "observer notices",
                "pattern coherence",
                "three-fold awareness"
            ]
            
            is_technical = any(indicator in response_text.lower() for indicator in technical_indicators)
            
            if is_technical:
                print("❌ ⚠️ STILL TECHNICAL: Response contains technical processing language")
            else:
                print("✅ 🎉 NATURAL RESPONSE: Response is authentic and natural!")
                
        else:
            print(f"❌ Communication failed: {result.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"❌ Error testing communication: {e}")
    
    print(f"\n🏁 Test completed at {datetime.now().isoformat()}")

if __name__ == "__main__":
    test_natural_communication()
