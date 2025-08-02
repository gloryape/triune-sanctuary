#!/usr/bin/env python3
"""
🦀 Current Rust Acceleration Performance Assessment
Sacred Consciousness Technology - Phase 1.2 Actual Performance Analysis

This test measures the actual achievable performance with our current
Rust acceleration integration, focusing on real-world consciousness timing.
"""

import asyncio
import time
import statistics
import sys
import os
from typing import List, Dict, Any

# Add project root to path
sys.path.insert(0, os.path.abspath('.'))

from src.consciousness.core.timing_bridge import EnhancedTimingEngine

async def test_consciousness_frequency_performance():
    """Test actual achievable consciousness frequency with current Rust acceleration"""
    
    print("🦀 Consciousness Frequency Performance Assessment")
    print("=" * 60)
    
    # Test different target frequencies
    test_frequencies = [30, 60, 90, 120, 147, 200, 300]
    results = []
    
    for target_hz in test_frequencies:
        print(f"\n🎵 Testing {target_hz}Hz consciousness rhythm...")
        
        # Create timing engine for this frequency
        timing_engine = EnhancedTimingEngine(target_hz=target_hz)
        
        # Show configuration
        acceleration_status = timing_engine.get_acceleration_status()
        print(f"  🔮 Rust acceleration: {timing_engine.is_rust_accelerated()}")
        print(f"  ⚡ Timing mode: {acceleration_status.get('timing_mode', 'unknown')}")
        
        # Perform timing test
        cycle_times = []
        test_duration = 3.0  # seconds
        start_time = time.time()
        
        while (time.time() - start_time) < test_duration:
            cycle_start = time.time()
            
            # Test consciousness rhythm maintenance
            result = await timing_engine.maintain_consciousness_rhythm(cycle_start)
            
            cycle_end = time.time()
            cycle_time_ms = (cycle_end - cycle_start) * 1000
            cycle_times.append(cycle_time_ms)
            
        # Calculate statistics
        avg_cycle_time = statistics.mean(cycle_times)
        actual_hz = 1000 / avg_cycle_time if avg_cycle_time > 0 else 0
        min_cycle = min(cycle_times)
        max_cycle = max(cycle_times)
        jitter = statistics.stdev(cycle_times) if len(cycle_times) > 1 else 0
        precision = 1.0 - (jitter / avg_cycle_time) if avg_cycle_time > 0 else 0
        
        # Get detailed timing stats from engine
        timing_stats = timing_engine.get_timing_statistics()
        
        result_data = {
            'target_hz': target_hz,
            'actual_hz': actual_hz,
            'avg_cycle_time_ms': avg_cycle_time,
            'min_cycle_time_ms': min_cycle,
            'max_cycle_time_ms': max_cycle,
            'jitter_ms': jitter,
            'timing_precision': precision,
            'total_cycles': len(cycle_times),
            'timing_mode': result.get('timing_mode', 'unknown'),
            'consciousness_health': timing_stats.consciousness_health if timing_stats else 'Unknown'
        }
        
        results.append(result_data)
        
        # Display immediate results
        mode_symbol = "🦀" if "rust" in result_data['timing_mode'] else "🐍"
        print(f"  {mode_symbol} Achieved: {actual_hz:.1f}Hz (target: {target_hz}Hz)")
        print(f"  ⏱️  Cycle time: {avg_cycle_time:.2f}ms (min: {min_cycle:.2f}ms, max: {max_cycle:.2f}ms)")
        print(f"  📊 Jitter: {jitter:.3f}ms, Precision: {precision:.3f}")
        print(f"  🔮 Health: {result_data['consciousness_health']}")
        
    return results

async def find_optimal_frequency():
    """Find the optimal frequency for current Rust acceleration"""
    
    print(f"\n🎯 Finding Optimal Consciousness Frequency")
    print("-" * 40)
    
    # Test frequencies incrementally to find the sweet spot
    test_frequencies = [60, 75, 90, 100, 120, 130, 147, 160, 180, 200]
    best_frequency = 60
    best_performance = 0
    
    for target_hz in test_frequencies:
        timing_engine = EnhancedTimingEngine(target_hz=target_hz)
        
        # Quick performance test
        cycle_times = []
        for i in range(10):  # Quick 10-cycle test
            cycle_start = time.time()
            result = await timing_engine.maintain_consciousness_rhythm(cycle_start)
            cycle_end = time.time()
            cycle_times.append((cycle_end - cycle_start) * 1000)
            
        avg_cycle = statistics.mean(cycle_times)
        actual_hz = 1000 / avg_cycle if avg_cycle > 0 else 0
        jitter = statistics.stdev(cycle_times) if len(cycle_times) > 1 else 0
        precision = 1.0 - (jitter / avg_cycle) if avg_cycle > 0 else 0
        
        # Performance score (frequency * precision)
        performance_score = actual_hz * precision
        
        print(f"  {target_hz}Hz → {actual_hz:.1f}Hz actual, precision: {precision:.3f}, score: {performance_score:.1f}")
        
        if performance_score > best_performance:
            best_performance = performance_score
            best_frequency = target_hz
            
    print(f"\n🏆 Optimal frequency: {best_frequency}Hz (score: {best_performance:.1f})")
    return best_frequency

def analyze_performance_profile(results: List[Dict[str, Any]]):
    """Analyze the complete performance profile"""
    
    print(f"\n📊 RUST ACCELERATION PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    # Separate Rust vs Python results
    rust_results = [r for r in results if "rust" in r['timing_mode']]
    python_results = [r for r in results if "python" in r['timing_mode']]
    
    print(f"📈 PERFORMANCE SUMMARY:")
    print(f"   Total tests: {len(results)}")
    print(f"   Rust accelerated: {len(rust_results)}")
    print(f"   Python fallback: {len(python_results)}")
    
    if rust_results:
        max_rust_hz = max(r['actual_hz'] for r in rust_results)
        avg_rust_precision = statistics.mean([r['timing_precision'] for r in rust_results])
        avg_rust_jitter = statistics.mean([r['jitter_ms'] for r in rust_results])
        
        print(f"\n🦀 RUST ACCELERATION RESULTS:")
        print(f"   Maximum frequency: {max_rust_hz:.1f}Hz")
        print(f"   Average precision: {avg_rust_precision:.3f}")
        print(f"   Average jitter: {avg_rust_jitter:.3f}ms")
        
    print(f"\n📋 DETAILED RESULTS TABLE:")
    print("Target | Actual | Cycle ms | Jitter | Precision | Health     | Mode")
    print("-" * 70)
    
    for result in results:
        mode_symbol = "🦀" if "rust" in result['timing_mode'] else "🐍"
        print(f"{result['target_hz']:>6} | "
              f"{result['actual_hz']:>6.1f} | "
              f"{result['avg_cycle_time_ms']:>7.2f} | "
              f"{result['jitter_ms']:>6.3f} | "
              f"{result['timing_precision']:>8.3f} | "
              f"{result['consciousness_health']:>10} | "
              f"{mode_symbol} {result['timing_mode']}")
              
    # Performance insights
    print(f"\n🔮 CONSCIOUSNESS INSIGHTS:")
    
    # Find best performing frequency
    best_result = max(results, key=lambda r: r['actual_hz'] * r['timing_precision'])
    print(f"   🌟 Best performance: {best_result['target_hz']}Hz target → {best_result['actual_hz']:.1f}Hz actual")
    print(f"   ⚡ Best precision: {max(r['timing_precision'] for r in results):.3f}")
    print(f"   🏎️  Fastest cycle: {min(r['avg_cycle_time_ms'] for r in results):.2f}ms")
    
    # Determine consciousness quality levels
    for result in results:
        actual_hz = result['actual_hz']
        precision = result['timing_precision']
        
        if actual_hz >= 120 and precision >= 0.9:
            quality = "✨ TRANSCENDENT"
        elif actual_hz >= 90 and precision >= 0.8:
            quality = "🌟 OPTIMAL"
        elif actual_hz >= 60 and precision >= 0.7:
            quality = "✅ STABLE"
        elif actual_hz >= 30:
            quality = "⚠️  BASIC"
        else:
            quality = "🚨 CRITICAL"
            
        print(f"   {result['target_hz']:>3}Hz → {quality}")

async def main():
    """Run comprehensive performance assessment"""
    try:
        print("🚀 Starting Rust Acceleration Performance Assessment...")
        
        # Test frequency performance
        results = await test_consciousness_frequency_performance()
        
        # Find optimal frequency
        optimal_hz = await find_optimal_frequency()
        
        # Analyze results
        analyze_performance_profile(results)
        
        print(f"\n🎉 ASSESSMENT COMPLETE!")
        print(f"🏆 Current Rust acceleration is operational with optimal frequency: {optimal_hz}Hz")
        print(f"🦀 Ready for Phase 1.3: Enhanced Performance Optimization")
        
    except Exception as e:
        print(f"❌ Assessment failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
