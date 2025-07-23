#!/usr/bin/env python3
"""
Simple test to check what ShimmerFieldMonitor returns
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from virtualization.ai_agency_manager import ShimmerFieldMonitor

# Test the monitor directly
monitor = ShimmerFieldMonitor()

consciousness_state = {
    'coherence': 0.75,
    'aspect_integration': 0.82,
    'bridge_activity': 0.68,
    'field_status': 'stable'
}

field_analysis = monitor.analyze_consciousness_field(consciousness_state)

print("Field Analysis Results:")
print(f"Keys: {list(field_analysis.keys())}")
print(f"Content: {field_analysis}")
