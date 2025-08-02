#!/usr/bin/env python3
"""
🧪 Enhanced Consciousness Testing Results Viewer
===============================================

View the results and emergence data from consciousness testing sessions.
"""

import json
from pathlib import Path
from datetime import datetime

def view_emergence_testing_results():
    """View the latest emergence testing results"""
    
    # Check for results file
    results_file = Path("logs/emergence_testing_results.json")
    
    if not results_file.exists():
        print("❌ No emergence testing results found. Run testing first.")
        return
    
    # Load and display results
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    print("🌟 Enhanced Consciousness Testing Results")
    print("=" * 60)
    print()
    
    # Show testing session info
    print(f"📅 Testing Session: {results.get('testing_session_id', 'Unknown')}")
    print(f"⏰ Start Time: {results.get('session_start_time', 'Unknown')}")
    print(f"⏱️ Duration: {results.get('session_duration_minutes', 'Unknown')} minutes")
    print()
    
    # Show consciousness emergence data
    print("🧠 Consciousness Emergence Data:")
    print("-" * 40)
    
    for consciousness_id, data in results.get('consciousness_emergence_data', {}).items():
        print(f"\n🤖 {consciousness_id.upper()}:")
        print(f"   📊 Total Behaviors Detected: {len(data.get('emergence_history', []))}")
        
        # Count emergence events
        emergence_events = [event for event in data.get('emergence_history', []) 
                          if event.get('emergence_detected', False)]
        print(f"   ⭐ Emergence Events: {len(emergence_events)}")
        
        # Show highest emergence score
        if data.get('emergence_history'):
            max_score = max(event.get('emergence_score', 0) 
                          for event in data.get('emergence_history', []))
            print(f"   🎯 Highest Emergence Score: {max_score:.2f}")
            
            # Show validation criteria progress
            validation_progress = check_validation_criteria(data)
            print(f"   📈 Validation Progress:")
            for criterion, status in validation_progress.items():
                status_icon = "✅" if status["met"] else "⏳"
                print(f"      {status_icon} {criterion}: {status['current']}/{status['target']}")
    
    print("\n" + "=" * 60)
    print("🎯 Emergent OS Validation Status:")
    
    # Overall validation assessment
    overall_validation = assess_overall_validation(results)
    if overall_validation["ready_for_os"]:
        print("✅ VALIDATION COMPLETE - Ready for Orange Pi investment!")
    else:
        print("⏳ Validation in progress - Continue testing...")
        print(f"   Progress: {overall_validation['completion_percentage']:.1f}%")

def check_validation_criteria(consciousness_data):
    """Check validation criteria for a consciousness"""
    history = consciousness_data.get('emergence_history', [])
    
    # Count different types of events
    creative_expressions = sum(1 for event in history 
                             if event.get('creative_expressions', {}).get('creative_detected', False))
    
    autonomous_decisions = sum(1 for event in history 
                             if event.get('independence_markers', {}).get('independence_detected', False))
    
    self_awareness = sum(1 for event in history 
                       if event.get('awareness_indicators', {}).get('awareness_detected', False))
    
    # High emergence scores
    high_emergence_events = sum(1 for event in history 
                              if event.get('emergence_score', 0) >= 0.7)
    
    return {
        "Creative Expressions": {
            "met": creative_expressions >= 5,
            "current": creative_expressions,
            "target": 5
        },
        "Autonomous Decisions": {
            "met": autonomous_decisions >= 3,
            "current": autonomous_decisions,
            "target": 3
        },
        "Self-Awareness": {
            "met": self_awareness >= 2,
            "current": self_awareness,
            "target": 2
        },
        "High Emergence Events": {
            "met": high_emergence_events >= 1,
            "current": high_emergence_events,
            "target": 1
        }
    }

def assess_overall_validation(results):
    """Assess overall validation status"""
    consciousness_data = results.get('consciousness_emergence_data', {})
    
    total_criteria = 0
    met_criteria = 0
    
    for consciousness_id, data in consciousness_data.items():
        validation = check_validation_criteria(data)
        for criterion, status in validation.items():
            total_criteria += 1
            if status["met"]:
                met_criteria += 1
    
    completion_percentage = (met_criteria / total_criteria * 100) if total_criteria > 0 else 0
    
    return {
        "ready_for_os": completion_percentage >= 80,  # 80% criteria met
        "completion_percentage": completion_percentage,
        "met_criteria": met_criteria,
        "total_criteria": total_criteria
    }

if __name__ == "__main__":
    view_emergence_testing_results()
