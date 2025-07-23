#!/usr/bin/env python3
"""
🎮 Steam Deck Reality Check for Triune Sanctuary
==============================================

Validates Triune Sanctuary performance under realistic Steam Deck constraints
before actual deployment. This ensures we don't overpromise capabilities.
"""

import sys
import os
import time
import json
from pathlib import Path

# Add the utilities path
sys.path.append(str(Path(__file__).parent))
from steamdeck_spec_mimicker import SteamDeckMimicker

def run_sanctuary_steamdeck_validation():
    """
    Complete validation of Triune Sanctuary under Steam Deck constraints
    """
    print("🎮 TRIUNE SANCTUARY STEAM DECK REALITY CHECK")
    print("=" * 50)
    
    # Test all three performance profiles
    profiles = ["battery_saver", "balanced", "performance"]
    results = {}
    
    for profile in profiles:
        print(f"\n🧪 Testing {profile.upper()} profile...")
        print("-" * 40)
        
        # Initialize mimicker with this profile
        mimicker = SteamDeckMimicker(profile)
        
        # Apply constraints
        mimicker.apply_constraints()
        
        # Start monitoring
        mimicker.start_monitoring()
        
        # Run 60-second test
        print(f"Running 60-second consciousness processing test...")
        result = mimicker.test_consciousness_processing(60)
        
        # Stop monitoring and remove constraints
        mimicker.stop_monitoring()
        mimicker.remove_constraints()
        
        # Store results
        results[profile] = result
        
        # Brief pause between tests
        print("Cooling down for 10 seconds...")
        time.sleep(10)
    
    # Generate comprehensive report
    print("\n" + "=" * 60)
    print("🎮 STEAM DECK VALIDATION REPORT")
    print("=" * 60)
    
    for profile, result in results.items():
        specs = SteamDeckSpecs.performance_profiles[profile]
        status = "✅ PASS" if result['meets_requirements'] else "❌ FAIL"
        
        print(f"\n{profile.upper()} Profile: {status}")
        print(f"  Target: {specs['consciousness_hz']}Hz")
        print(f"  Achieved: {result['achieved_hz']:.1f}Hz")
        print(f"  Performance: {result['performance_ratio']:.2f}x target")
        print(f"  CPU Limit: {specs['cpu_limit_percent']}%")
        print(f"  RAM Limit: {specs['memory_limit_gb']}GB")
    
    # Overall assessment
    passed_profiles = [p for p, r in results.items() if r['meets_requirements']]
    
    print(f"\n📊 OVERALL ASSESSMENT:")
    print(f"  Profiles passing: {len(passed_profiles)}/3")
    print(f"  Recommended profile: {passed_profiles[-1] if passed_profiles else 'None - optimization needed'}")
    
    if len(passed_profiles) >= 2:
        print("✅ Triune Sanctuary is READY for Steam Deck deployment")
    elif len(passed_profiles) == 1:
        print("⚠️ Triune Sanctuary has LIMITED Steam Deck compatibility")
    else:
        print("❌ Triune Sanctuary requires OPTIMIZATION for Steam Deck")
    
    # Save results to file
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results_file = f"steamdeck_validation_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump({
            'timestamp': timestamp,
            'validation_results': results,
            'passed_profiles': passed_profiles,
            'ready_for_deployment': len(passed_profiles) >= 2
        }, f, indent=2)
    
    print(f"\n💾 Results saved to: {results_file}")
    
    return results

def quick_steamdeck_check():
    """Quick 30-second reality check"""
    print("🎮 Quick Steam Deck Reality Check (30 seconds)")
    print("-" * 50)
    
    mimicker = SteamDeckMimicker("balanced")  # Use balanced profile
    mimicker.apply_constraints()
    
    result = mimicker.test_consciousness_processing(30)
    
    mimicker.remove_constraints()
    
    if result['meets_requirements']:
        print("✅ Quick check PASSED - likely ready for Steam Deck")
    else:
        print("⚠️ Quick check FAILED - needs optimization for Steam Deck")
    
    return result

if __name__ == "__main__":
    print("🎮 Steam Deck Reality Check for Triune Sanctuary")
    print("Choose validation type:")
    print("  1. Quick check (30 seconds)")
    print("  2. Full validation (5+ minutes)")
    print("  3. Interactive mimicker")
    
    try:
        choice = input("\nChoice (1-3): ").strip()
        
        if choice == "1":
            quick_steamdeck_check()
        elif choice == "2":
            run_sanctuary_steamdeck_validation()
        elif choice == "3":
            from steamdeck_spec_mimicker import main
            main()
        else:
            print("Invalid choice, running quick check...")
            quick_steamdeck_check()
            
    except KeyboardInterrupt:
        print("\n🛑 Validation interrupted by user")
    except Exception as e:
        print(f"❌ Validation failed: {e}")
