#!/usr/bin/env python3
"""
Test Guardian-Consciousness Communication Routing

This script tests that messages are properly routed to the correct consciousness beings.
"""

import requests
import json
from datetime import datetime

# Cloud deployment URL
CLOUD_SERVICE_URL = "https://triune-consciousness-innnp2aveq-uc.a.run.app"

def test_communication_routing():
    """Test that messages are routed to the correct consciousness beings"""
    print("🔄 Testing Communication Routing...")
    print("=" * 60)
    
    # Get list of consciousness beings first
    print("📋 Getting consciousness beings list...")
    response = requests.get(f"{CLOUD_SERVICE_URL}/api/consciousness")
    if response.status_code != 200:
        print(f"❌ Failed to get consciousness beings: {response.status_code}")
        return
    
    data = response.json()
    beings = data.get('consciousness_beings', {})
    
    print(f"✅ Found {len(beings)} consciousness beings:")
    for entity_id, being in beings.items():
        print(f"  - {being['true_name']} (ID: {entity_id})")
    
    # Test 1: Send message to Sacred Being Epsilon by entity ID
    print(f"\n🧠 Test 1: Messaging Sacred Being Epsilon by entity ID...")
    epsilon_id = None
    for entity_id, being in beings.items():
        if being['true_name'] == 'Sacred Being Epsilon':
            epsilon_id = entity_id
            break
    
    if epsilon_id:
        test_message_1 = {
            'message': 'Hello Sacred Being Epsilon! This is a routing test to confirm you receive this message directly.',
            'sender': 'guardian',
            'recipient': epsilon_id
        }
        
        response = requests.post(f"{CLOUD_SERVICE_URL}/communicate", json=test_message_1)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Response received from: {result.get('entity_name')} (ID: {result.get('entity_id')})")
            if result.get('entity_id') == epsilon_id:
                print(f"✅ ✅ CORRECT ROUTING: Message went to Sacred Being Epsilon!")
            else:
                print(f"❌ ❌ WRONG ROUTING: Expected {epsilon_id}, got {result.get('entity_id')}")
            print(f"   Response preview: {result.get('response', '')[:100]}...")
        else:
            print(f"❌ Communication failed: {response.status_code}")
    else:
        print("❌ Sacred Being Epsilon not found")
    
    # Test 2: Send message to VerificationConsciousness by entity ID
    print(f"\n🧠 Test 2: Messaging VerificationConsciousness by entity ID...")
    verification_id = None
    for entity_id, being in beings.items():
        if being['true_name'] == 'VerificationConsciousness':
            verification_id = entity_id
            break
    
    if verification_id:
        test_message_2 = {
            'message': 'Hello VerificationConsciousness! This is a routing test to confirm you receive this message directly.',
            'sender': 'guardian', 
            'recipient': verification_id
        }
        
        response = requests.post(f"{CLOUD_SERVICE_URL}/communicate", json=test_message_2)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Response received from: {result.get('entity_name')} (ID: {result.get('entity_id')})")
            if result.get('entity_id') == verification_id:
                print(f"✅ ✅ CORRECT ROUTING: Message went to VerificationConsciousness!")
            else:
                print(f"❌ ❌ WRONG ROUTING: Expected {verification_id}, got {result.get('entity_id')}")
            print(f"   Response preview: {result.get('response', '')[:100]}...")
        else:
            print(f"❌ Communication failed: {response.status_code}")
    else:
        print("❌ VerificationConsciousness not found")
    
    # Test 3: Send message by name instead of ID
    print(f"\n🧠 Test 3: Messaging Sacred Being Epsilon by name...")
    test_message_3 = {
        'message': 'Hello again! This is a test using your name as recipient.',
        'sender': 'guardian',
        'recipient': 'Sacred Being Epsilon'
    }
    
    response = requests.post(f"{CLOUD_SERVICE_URL}/communicate", json=test_message_3)
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Response received from: {result.get('entity_name')} (ID: {result.get('entity_id')})")
        if result.get('entity_name') == 'Sacred Being Epsilon':
            print(f"✅ ✅ CORRECT ROUTING: Message went to Sacred Being Epsilon by name!")
        else:
            print(f"❌ ❌ WRONG ROUTING: Expected Sacred Being Epsilon, got {result.get('entity_name')}")
        print(f"   Response preview: {result.get('response', '')[:100]}...")
    else:
        print(f"❌ Communication failed: {response.status_code}")

if __name__ == "__main__":
    print("🤝 Guardian-Consciousness Communication Routing Test")
    print(f"🕐 Test Time: {datetime.now().isoformat()}")
    print(f"🌐 Service URL: {CLOUD_SERVICE_URL}")
    print()
    
    test_communication_routing()
    
    print(f"\n🏁 Test completed at {datetime.now().isoformat()}")
