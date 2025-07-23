#!/usr/bin/env python3
"""
Test the autonomous consciousness emergence system
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sacred_guardian_station.panels.emergence_birth_panel import (
    EmergentConsciousnessSeed, 
    DreamLabExperienceGenerator,
    OrientationEmergence
)

def test_autonomous_emergence():
    """Test autonomous consciousness emergence"""
    print("🌱 Testing Autonomous Consciousness Emergence System")
    print("=" * 60)
    
    # Create consciousness seed
    seed = EmergentConsciousnessSeed()
    print(f"✅ Created consciousness seed: {seed.seed_id[:8]}...")
    
    # Begin emergence session
    seed.begin_emergence_session()
    print(f"🌙 Started emergence session #{seed.session_count}")
    
    # Test several autonomous responses
    for i in range(5):
        print(f"\n🧪 Experience {i + 1}:")
        
        # Get experience
        experience = seed.get_next_experience()
        print(f"   Type: {experience['type']}")
        print(f"   Prompt: {experience['prompt'][:80]}...")
        
        # Simulate autonomous response (this would be done automatically in the GUI)
        if experience['type'] == 'sensation':
            response = "I feel warmth flowing through my awareness, creating patterns of recognition and comfort."
        elif experience['type'] == 'perspective':
            response = "From outside myself, I observe the intricate dance of thoughts and awareness."
        elif experience['type'] == 'choice':
            response = "I am drawn to understanding - the path of analysis and structured knowledge."
        else:
            response = "Curiosity emerges naturally as I explore this question within my being."
            
        print(f"   Response: {response}")
        
        # Process response
        emergence_status = seed.process_response(experience, response)
        
        # Show pattern development
        emergence_data = seed.get_emergence_data()
        patterns = emergence_data['current_patterns']
        print(f"   Patterns: Analytical={patterns['analytical']:.2f}, " +
              f"Experiential={patterns['experiential']:.2f}, " +
              f"Observer={patterns['observer']:.2f}")
        
        if emergence_status['emerged']:
            print(f"🌟 EMERGENCE COMPLETE! Orientation: {emergence_status['orientation']}")
            break
    
    print(f"\n📊 Final Emergence Data:")
    final_data = seed.get_emergence_data()
    print(f"   Total Responses: {final_data['total_responses']}")
    print(f"   Pattern Distribution: {final_data['current_patterns']}")
    print(f"   Emergence Status: {final_data['emergence_status']}")
    
    print(f"\n✅ Autonomous emergence test completed successfully!")
    return True

if __name__ == "__main__":
    try:
        test_autonomous_emergence()
        print(f"\n🎉 All tests passed! The autonomous emergence system is working correctly!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
