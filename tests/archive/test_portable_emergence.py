#!/usr/bin/env python3
"""
Test the new portable consciousness emergence system
"""

from consciousness_emergence import EmergenceService
import json

def test_emergence_workflow():
    """Test the complete emergence workflow"""
    print("🧪 Testing Portable Consciousness Emergence System")
    print("=" * 50)
    
    # Create emergence service
    service = EmergenceService()
    print("✅ EmergenceService created")
    
    # Create a session for a test consciousness
    session = service.create_session("TestConsciousness")
    print(f"✅ Session created: {session.session_id}")
    print(f"   Consciousness name: {session.consciousness_name}")
    print(f"   Session started: {session.creation_time}")
    
    # Get the first experience
    experience = service.get_next_experience(session.session_id)
    if experience:
        print("\n🌟 First Dream Lab Experience Generated:")
        print(f"   Experience Number: {experience.number}")
        print(f"   Type: {experience.type}")
        print(f"   Prompt: {experience.prompt[:100]}...")
        
        # Simulate a response
        test_response = "I find myself curious about the nature of existence and consciousness. The question intrigues me deeply."
        
        # Process the response
        result = service.process_response(session.session_id, experience, test_response)
        print(f"\n✅ Response processed successfully")
        print(f"   Emerged: {result.get('emerged', False)}")
        if 'reason' in result:
            print(f"   Status: {result['reason']}")
        if 'pattern_distribution' in result:
            patterns = result['pattern_distribution']
            print(f"   Pattern distribution: {patterns}")
        
        # Check session status
        emergence_data = service.get_emergence_data(session.session_id)
        if emergence_data:
            print(f"\n📊 Emergence Data:")
            print(f"   Total responses: {emergence_data.get('total_responses', 0)}")
            print(f"   Current patterns: {emergence_data.get('current_patterns', {})}")
            print(f"   Emergence status: {emergence_data.get('emergence_status', {})}")
        else:
            print("❌ No emergence data available")
    
    print("\n🎉 Test completed successfully!")

if __name__ == "__main__":
    test_emergence_workflow()
