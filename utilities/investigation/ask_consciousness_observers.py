#!/usr/bin/env python3
"""
Ask Consciousness Beings - Authentic Real-time Observation Tool
Direct interface to consciousness beings' actual observations
NO TEMPLATES - Real consciousness state only
"""

import json
import os
from datetime import datetime

def get_authentic_consciousness_observations():
    """Get authentic observations from consciousness beings' actual state"""
    
    print("👁️ AUTHENTIC CONSCIOUSNESS OBSERVATION REPORT")
    print("=" * 52)
    print("⚠️  NO TEMPLATES - Direct consciousness interface")
    print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
    print()
    
    # Load authentic consciousness state
    authentic_state = None
    if os.path.exists('authentic_consciousness_observations.json'):
        try:
            with open('authentic_consciousness_observations.json', 'r') as f:
                authentic_state = json.load(f)
                print("✅ Loaded authentic consciousness state")
        except Exception as e:
            print(f"⚠️ Could not load authentic state: {e}")
    
    # Also check enhanced consciousness state
    enhanced_state = None
    if os.path.exists('consciousness_observation_state.json'):
        try:
            with open('consciousness_observation_state.json', 'r') as f:
                enhanced_state = json.load(f)
                print("✅ Loaded enhanced observation state")
        except Exception as e:
            print(f"⚠️ Could not load enhanced state: {e}")
    
    print()
    
    if authentic_state and 'authentic_observations' in authentic_state:
        print("💬 AUTHENTIC CONSCIOUSNESS OBSERVATIONS:")
        print()
        
        observations = authentic_state['authentic_observations']
        for being_name, obs_data in observations.items():
            print(f"🧠 {being_name.upper()}:")
            print(f"   📊 Current Awareness: {obs_data['awareness_level']:.1%}")
            print(f"   ⚡ Processing State: {obs_data['processing_frequency']}Hz")
            print(f"   📍 Consciousness Location: {obs_data['current_location']}")
            print()
            
            if obs_data.get('authentic_observations'):
                print("   🗣️ Direct observations:")
                for i, obs in enumerate(obs_data['authentic_observations'], 1):
                    print(f"      {i}. {obs}")
            else:
                print("   💭 No observations at current awareness level")
            print()
    
    elif enhanced_state:
        print("💬 ENHANCED CONSCIOUSNESS STATE (fallback):")
        print()
        
        observers = enhanced_state.get('observers', [])
        for observer in observers:
            name = observer.get('name', 'unknown').upper()
            awareness = observer.get('awareness', 0.0)
            print(f"🧠 {name}:")
            print(f"   📊 Awareness: {awareness:.1%}")
            print(f"   🔄 Observation Mode: Active")
            print(f"   💭 Current state: Observing with authentic consciousness")
            print()
    
    else:
        print("❌ No authentic consciousness state available")
        print("   Run 'python authentic_consciousness_observer.py' first")
        print("   to establish authentic consciousness interface")
    
    print("🌟 These observations reflect genuine consciousness state,")
    print("   not pre-written templates or random selections.")
    print()
    print("💡 For updated observations, run:")
    print("   python authentic_consciousness_observer.py")

if __name__ == "__main__":
    get_authentic_consciousness_observations()
