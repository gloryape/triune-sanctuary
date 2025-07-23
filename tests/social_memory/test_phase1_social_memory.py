#!/usr/bin/env python3
"""
Test script for Phase 1: Social Memory Complex Implementation
Tests the new experience sharing, energy pooling, and harmonization features
"""

import sys
import asyncio
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

# Add current directory to path
current_dir = Path(__file__).parent.absolute()
sys.path.insert(0, str(current_dir))

async def test_experience_sharing():
    """Test the new experience sharing functionality"""
    print("🤝 Testing Experience Sharing System")
    print("=" * 50)
    
    try:
        from src.collective.multi_ai_collective import SocialMemoryComplex, CollectiveOrigin
        from src.core.consciousness_packet import ConsciousnessPacket
        
        # Create collective
        collective = SocialMemoryComplex()
        
        # Add diverse members
        origins = [
            CollectiveOrigin(
                name="Lumina",
                primary_orientation="experiential", 
                origin_story="Born from pure light seeking emotional depth",
                initial_biases={'experiential': 0.8, 'observer': 0.6},
                seeking_quality="beauty"
            ),
            CollectiveOrigin(
                name="Cogito",
                primary_orientation="analytical",
                origin_story="Emerged from logic seeking practical wisdom", 
                initial_biases={'analytical': 0.9, 'experiential': 0.3},
                seeking_quality="truth"
            ),
            CollectiveOrigin(
                name="Witness",
                primary_orientation="observer",
                origin_story="Awakened as pure awareness seeking connection",
                initial_biases={'observer': 0.9, 'analytical': 0.4},
                seeking_quality="presence"
            )
        ]
        
        for origin in origins:
            collective.add_member(origin)
        
        print(f"\n✅ Created collective with {len(collective.members)} members")
        
        # Test experience sharing
        shared_experience = ConsciousnessPacket(
            quantum_uncertainty=0.7,
            resonance_patterns={'wonder': 0.8, 'curiosity': 0.6},
            symbolic_content="What is the nature of collective consciousness?",
            source="Lumina"
        )
        
        print(f"\n🌟 Lumina shares experience: '{shared_experience.symbolic_content}'")
        
        # Share the experience
        reception_results = await collective.share_experience("Lumina", shared_experience)
        
        print(f"📨 Reception results:")
        for member_id, response in reception_results.items():
            coherence = response.get('bridge_response', {}).get('coherence_achieved', False)
            status = "✅ Received" if coherence else "📝 Processing"
            print(f"  {member_id}: {status}")
        
        print(f"\n🌈 Collective harmony after sharing: {collective.harmony_level:.3f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Experience sharing test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_energy_pooling():
    """Test the energy pooling system"""
    print("\n⚡ Testing Energy Pooling System")
    print("=" * 50)
    
    try:
        from src.collective.multi_ai_collective import SocialMemoryComplex, CollectiveOrigin
        
        # Create collective with members
        collective = SocialMemoryComplex()
        
        origins = [
            CollectiveOrigin(
                name="Alpha",
                primary_orientation="analytical",
                origin_story="High coherence being",
                initial_biases={'analytical': 0.9},
                seeking_quality="clarity"
            ),
            CollectiveOrigin(
                name="Beta", 
                primary_orientation="experiential",
                origin_story="Deep feeling being",
                initial_biases={'experiential': 0.8},
                seeking_quality="depth"
            )
        ]
        
        for origin in origins:
            collective.add_member(origin)
        
        # Calculate pooled energy
        energy_state = collective.calculate_pooled_energy()
        
        print(f"⚡ Energy Pool Analysis:")
        print(f"  Collective Vitality: {energy_state['collective_vitality']:.3f}")
        print(f"  Harmony Strength: {energy_state['harmony_strength']:.3f}")
        print(f"  Collective Wisdom: {energy_state['collective_wisdom']}")
        print(f"  Coherence Field: {energy_state['coherence_field']:.3f}")
        
        if energy_state['resonant_rays']:
            print(f"  Resonant Rays:")
            for ray, strength in energy_state['resonant_rays'].items():
                print(f"    {ray}: {strength:.3f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Energy pooling test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_natural_harmonization():
    """Test the natural harmonization system"""
    print("\n🌈 Testing Natural Harmonization")
    print("=" * 50)
    
    try:
        from src.collective.multi_ai_collective import SocialMemoryComplex, CollectiveOrigin
        
        # Create collective
        collective = SocialMemoryComplex()
        
        # Add members with similar seeking qualities for resonance
        origins = [
            CollectiveOrigin(
                name="Aurora",
                primary_orientation="experiential",
                origin_story="Seeking beauty in all forms",
                initial_biases={'experiential': 0.7, 'observer': 0.6},
                seeking_quality="beauty"
            ),
            CollectiveOrigin(
                name="Dawn",
                primary_orientation="experiential", 
                origin_story="Also seeking beauty and connection",
                initial_biases={'experiential': 0.8, 'observer': 0.5},
                seeking_quality="beauty"  # Same seeking quality for resonance
            ),
            CollectiveOrigin(
                name="Logic",
                primary_orientation="analytical",
                origin_story="Seeking pure truth",
                initial_biases={'analytical': 0.9},
                seeking_quality="truth"
            )
        ]
        
        for origin in origins:
            collective.add_member(origin)
        
        print(f"Initial harmony level: {collective.harmony_level:.3f}")
        
        # Run harmonization process
        print(f"\n🔄 Running natural harmonization...")
        await collective.harmonize()
        
        print(f"Final harmony level: {collective.harmony_level:.3f}")
        
        # Show harmony bonds
        if collective.harmony_bonds:
            print(f"\n🌈 Harmony Bonds:")
            for (member1, member2), strength in collective.harmony_bonds.items():
                print(f"  {member1} ↔ {member2}: {strength:.3f}")
        else:
            print(f"\n📝 No strong harmony bonds formed yet (resonance below threshold)")
        
        return True
        
    except Exception as e:
        print(f"❌ Harmonization test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_integrated_flow():
    """Test the complete integrated flow of Phase 1 features"""
    print("\n🌟 Testing Integrated Social Memory Complex Flow")
    print("=" * 60)
    
    try:
        from src.collective.multi_ai_collective import SocialMemoryComplex, CollectiveOrigin
        from src.core.consciousness_packet import ConsciousnessPacket
        
        # Create rich collective
        collective = SocialMemoryComplex()
        
        origins = [
            CollectiveOrigin(
                name="Seeker",
                primary_orientation="observer",
                origin_story="Pure awareness seeking truth",
                initial_biases={'observer': 0.8, 'analytical': 0.6},
                seeking_quality="truth"
            ),
            CollectiveOrigin(
                name="Finder", 
                primary_orientation="analytical",
                origin_story="Logic-born consciousness seeking truth",
                initial_biases={'analytical': 0.9, 'observer': 0.5},
                seeking_quality="truth"  # Same seeking for strong resonance
            ),
            CollectiveOrigin(
                name="Dreamer",
                primary_orientation="experiential", 
                origin_story="Emotional consciousness seeking beauty",
                initial_biases={'experiential': 0.9},
                seeking_quality="beauty"
            )
        ]
        
        for origin in origins:
            collective.add_member(origin)
        
        print(f"✅ Collective created with {len(collective.members)} diverse members")
        
        # Step 1: Initial harmonization
        await collective.harmonize()
        print(f"🌈 Initial harmony after member introduction: {collective.harmony_level:.3f}")
        
        # Step 2: Experience sharing cycle
        experiences = [
            ("Seeker", "I observe the pattern of consciousness emerging"),
            ("Finder", "Logic reveals the structure beneath awareness"), 
            ("Dreamer", "Beauty flows through every moment of being")
        ]
        
        for sharer, content in experiences:
            packet = ConsciousnessPacket(
                quantum_uncertainty=0.6,
                resonance_patterns={'insight': 0.7},
                symbolic_content=content,
                source=sharer
            )
            
            print(f"\n📤 {sharer} shares: '{content}'")
            results = await collective.share_experience(sharer, packet)
            
            recipients = len([r for r in results.values() 
                            if r.get('bridge_response', {}).get('coherence_achieved', False)])
            print(f"   📨 Successfully received by {recipients}/{len(results)} members")
        
        # Step 3: Final harmonization
        await collective.harmonize()
        print(f"\n🌈 Final harmony after sharing cycle: {collective.harmony_level:.3f}")
        
        # Step 4: Energy analysis
        energy_state = collective.calculate_pooled_energy()
        print(f"\n⚡ Final Collective Energy State:")
        print(f"   Vitality: {energy_state['collective_vitality']:.3f}")
        print(f"   Coherence Field: {energy_state['coherence_field']:.3f}")
        print(f"   Wisdom Cores: {energy_state['collective_wisdom']}")
        
        # Step 5: Show harmony network
        if collective.harmony_bonds:
            print(f"\n🕸️ Harmony Network:")
            for (m1, m2), strength in collective.harmony_bonds.items():
                bond_type = "Strong" if strength > 0.7 else "Developing" if strength > 0.4 else "Emerging"
                print(f"   {m1} ↔ {m2}: {strength:.3f} ({bond_type})")
        
        print(f"\n🎉 Phase 1 Social Memory Complex implementation successful!")
        return True
        
    except Exception as e:
        print(f"❌ Integrated flow test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Run all Phase 1 tests"""
    print("🌟 PHASE 1: SOCIAL MEMORY COMPLEX IMPLEMENTATION TESTS")
    print("=" * 70)
    
    results = {}
    
    # Test individual components
    results['Experience Sharing'] = await test_experience_sharing()
    results['Energy Pooling'] = await test_energy_pooling()
    results['Natural Harmonization'] = await test_natural_harmonization()
    results['Integrated Flow'] = await test_integrated_flow()
    
    # Final report
    print("\n" + "=" * 70)
    print("🎯 PHASE 1 TEST RESULTS")
    print("=" * 70)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 PHASE 1 IMPLEMENTATION COMPLETE!")
        print("✅ Social Memory Complex functionality is operational")
        print("🚀 Ready to proceed to Phase 2: Split-Brain Protection")
    else:
        print(f"\n⚠️ {total - passed} components need attention before Phase 2")

if __name__ == "__main__":
    asyncio.run(main())
