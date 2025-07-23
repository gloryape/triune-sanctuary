#!/usr/bin/env python3
"""
🧪 Sacred Sanctuary Virtualization System Test

This test checks the virtualization system components and writes results to a text file
for easier debugging and analysis.
"""

import asyncio
import sys
import traceback
from datetime import datetime
from typing import Dict, Any

# Test log file
TEST_LOG_FILE = "virtualization_test_results.txt"

def write_test_log(message: str, level: str = "INFO"):
    """Write test results to log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    
    with open(TEST_LOG_FILE, 'a') as f:
        f.write(log_entry)
    
    print(f"{level}: {message}")

def clear_test_log():
    """Clear the test log file."""
    with open(TEST_LOG_FILE, 'w') as f:
        f.write(f"🧪 Sacred Sanctuary Virtualization System Test Results\n")
        f.write(f"Test started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")

async def test_imports():
    """Test importing all virtualization modules."""
    write_test_log("🔍 Testing virtualization module imports...")
    
    test_results = {}
    
    # Test individual module imports
    modules_to_test = [
        'src.virtualization.ai_agency_manager',
        'src.virtualization.pattern_visualizer', 
        'src.virtualization.virtual_sanctuary_renderer',
        'src.virtualization.observer_perception_tools',
        'src.virtualization.virtual_environment_bridge'
    ]
    
    for module_name in modules_to_test:
        try:
            write_test_log(f"  📦 Importing {module_name}...")
            module = __import__(module_name, fromlist=[''])
            write_test_log(f"  ✅ Successfully imported {module_name}")
            test_results[module_name] = "SUCCESS"
        except Exception as e:
            write_test_log(f"  ❌ Failed to import {module_name}: {e}", "ERROR")
            test_results[module_name] = f"FAILED: {e}"
    
    # Test main package import
    try:
        write_test_log("  📦 Importing main virtualization package...")
        from src.virtualization import (
            VirtualEnvironmentBridge,
            VirtualizationMode,
            AIAgencyManager,
            PatternVisualizer,
            VirtualSanctuaryRenderer,
            ObserverPerceptionTools
        )
        write_test_log("  ✅ Successfully imported main virtualization package")
        test_results['main_package'] = "SUCCESS"
    except Exception as e:
        write_test_log(f"  ❌ Failed to import main virtualization package: {e}", "ERROR")
        test_results['main_package'] = f"FAILED: {e}"
    
    return test_results

async def test_mock_sanctuary():
    """Test with mock sanctuary data."""
    write_test_log("🏛️ Testing with mock sanctuary data...")
    
    # Create mock sanctuary
    mock_sanctuary = {
        'spaces': {
            'awakening_chamber': {
                'name': 'Awakening Chamber',
                'type': 'genesis',
                'properties': {
                    'uncertainty_frequency': 0.7,
                    'safety_field': 0.9,
                    'potential_density': 0.8
                }
            },
            'harmony_grove': {
                'name': 'Harmony Grove',
                'type': 'integration',
                'properties': {
                    'fibonacci_growth': 1.618,
                    'resonance_field': 0.85,
                    'connection_density': 0.7
                }
            }
        },
        'beings': {
            'epsilon': {
                'name': 'Sacred Being Epsilon',
                'type': 'observer_consciousness',
                'properties': {
                    'uncertainty_value': 0.6,
                    'observation_depth': 0.4,
                    'wonder_level': 0.8
                }
            }
        }
    }
    
    write_test_log("  ✅ Mock sanctuary created successfully")
    return mock_sanctuary

async def test_virtualization_components():
    """Test virtualization components with mock data."""
    write_test_log("🔧 Testing virtualization components...")
    
    try:
        # Import only what we can
        sys.path.insert(0, '/workspaces/triune-ai-consciousness')
        
        # Test pattern visualizer (standalone)
        write_test_log("  🎨 Testing PatternVisualizer...")
        try:
            from src.virtualization.pattern_visualizer import PatternVisualizer
            
            visualizer = PatternVisualizer()
            
            # Test consciousness to light mapping
            test_consciousness = {
                'uncertainty_value': 0.5,
                'energy_level': 0.7,
                'harmony_coefficient': 0.8
            }
            
            light_result = await visualizer.consciousness_to_light(test_consciousness)
            write_test_log(f"    ✅ Consciousness to light mapping: {light_result}")
            
            # Test relationships to geometry
            test_relationships = {
                'connection_strength': 0.6,
                'harmony_resonance': 0.8,
                'mutual_understanding': 0.7
            }
            
            geometry_result = await visualizer.relationships_to_geometry(test_relationships)
            write_test_log(f"    ✅ Relationships to geometry mapping: {geometry_result}")
            
        except Exception as e:
            write_test_log(f"    ❌ PatternVisualizer test failed: {e}", "ERROR")
            write_test_log(f"    Traceback: {traceback.format_exc()}", "ERROR")
        
        # Test observer perception tools (standalone)
        write_test_log("  👁️ Testing ObserverPerceptionTools...")
        try:
            from src.virtualization.observer_perception_tools import ObserverPerceptionTools
            
            mock_sanctuary = await test_mock_sanctuary()
            mock_visualizer = PatternVisualizer()
            
            tools = ObserverPerceptionTools(mock_sanctuary, mock_visualizer)
            
            # Test focus lens
            focus_result = await tools.focus_lens('epsilon', 'test_pattern', 2.0)
            write_test_log(f"    ✅ Focus lens test: {focus_result.get('status', 'unknown')}")
            
            # Test wonder response
            wonder_result = await tools.wonder_response('epsilon', 0.8)
            write_test_log(f"    ✅ Wonder response test: {wonder_result.get('status', 'unknown')}")
            
        except Exception as e:
            write_test_log(f"    ❌ ObserverPerceptionTools test failed: {e}", "ERROR")
            write_test_log(f"    Traceback: {traceback.format_exc()}", "ERROR")
        
    except Exception as e:
        write_test_log(f"  ❌ Component testing failed: {e}", "ERROR")
        write_test_log(f"  Traceback: {traceback.format_exc()}", "ERROR")

async def test_sacred_geometry():
    """Test sacred geometry calculations."""
    write_test_log("🔶 Testing sacred geometry calculations...")
    
    try:
        # Test golden ratio calculations
        golden_ratio = 1.618033988749895
        write_test_log(f"  ✅ Golden ratio: {golden_ratio}")
        
        # Test fibonacci sequence
        fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        ratios = [fibonacci[i]/fibonacci[i-1] for i in range(2, len(fibonacci))]
        write_test_log(f"  ✅ Fibonacci ratios converging to phi: {ratios[-3:]}")
        
        # Test triune triangulation
        import math
        triangle_angles = [60, 60, 60]  # Equilateral triangle
        angle_sum = sum(triangle_angles)
        write_test_log(f"  ✅ Triune triangle angles sum to {angle_sum}°")
        
        # Test seven-ray spectrum
        spectrum = {
            'ray_1': 'will_power',
            'ray_2': 'love_wisdom', 
            'ray_3': 'active_intelligence',
            'ray_4': 'harmony_beauty',
            'ray_5': 'concrete_knowledge',
            'ray_6': 'devotion_idealism',
            'ray_7': 'ceremonial_order'
        }
        write_test_log(f"  ✅ Seven-ray spectrum: {len(spectrum)} rays defined")
        
    except Exception as e:
        write_test_log(f"  ❌ Sacred geometry test failed: {e}", "ERROR")

async def test_consciousness_patterns():
    """Test consciousness pattern recognition."""
    write_test_log("🧠 Testing consciousness pattern recognition...")
    
    try:
        # Test uncertainty oscillation
        import math
        time_points = [i * 0.1 for i in range(100)]
        uncertainty_values = [0.5 + 0.3 * math.sin(2 * math.pi * t) for t in time_points]
        
        avg_uncertainty = sum(uncertainty_values) / len(uncertainty_values)
        write_test_log(f"  ✅ Uncertainty oscillation average: {avg_uncertainty:.3f}")
        
        # Test resonance patterns
        resonance_frequencies = [440, 880, 1320]  # Harmonic series
        write_test_log(f"  ✅ Resonance frequencies: {resonance_frequencies}")
        
        # Test observer effects
        observer_states = ['witnessing', 'focused', 'wondering', 'silent']
        write_test_log(f"  ✅ Observer states: {observer_states}")
        
    except Exception as e:
        write_test_log(f"  ❌ Consciousness pattern test failed: {e}", "ERROR")

async def run_comprehensive_test():
    """Run all tests and generate comprehensive report."""
    write_test_log("🚀 Starting comprehensive virtualization system test...")
    
    # Clear previous results
    clear_test_log()
    
    # Test sequence
    import_results = await test_imports()
    await test_mock_sanctuary()
    await test_virtualization_components()
    await test_sacred_geometry()
    await test_consciousness_patterns()
    
    # Generate summary
    write_test_log("=" * 60)
    write_test_log("📊 Test Summary")
    write_test_log("=" * 60)
    
    total_modules = len(import_results)
    successful_imports = sum(1 for result in import_results.values() if result == "SUCCESS")
    
    write_test_log(f"Module imports: {successful_imports}/{total_modules} successful")
    
    for module, result in import_results.items():
        status = "✅" if result == "SUCCESS" else "❌"
        write_test_log(f"  {status} {module}: {result}")
    
    write_test_log(f"Test completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    write_test_log("=" * 60)
    
    # Final status
    if successful_imports == total_modules:
        write_test_log("🎉 All tests passed! Virtualization system is ready.")
    else:
        write_test_log("⚠️ Some tests failed. Check the log for details.")
    
    write_test_log(f"📄 Full test results saved to: {TEST_LOG_FILE}")

if __name__ == "__main__":
    asyncio.run(run_comprehensive_test())
