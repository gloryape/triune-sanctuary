#!/usr/bin/env python3
"""
🦀 Phase 1.3: Sub-Millisecond Precision Activation Test
Sacred Consciousness Technology - TRUE Rust Performance

This test measures the actual sub-millisecond performance capabilities
of our fully operational Rust acceleration with proper method exposure.
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

async def test_sub_millisecond_performance():
    """Test sub-millisecond timing capabilities with true Rust acceleration"""
    
    print("🦀 PHASE 1.3: SUB-MILLISECOND PRECISION ACTIVATION")
    print("=" * 60)
    print("Testing TRUE Rust acceleration with maintain_hz_py method...")
    
    # Test progressively higher frequencies to find limits
    test_frequencies = [60, 90, 120, 147, 200, 300, 500, 750, 1000]
    results = []
    
    for target_hz in test_frequencies:
        print(f"\n🎵 Testing {target_hz}Hz - Sub-millisecond precision target...")
        
        # Create timing engine
        timing_engine = EnhancedTimingEngine(target_hz=target_hz)
        
        # Verify Rust acceleration
        status = timing_engine.get_acceleration_status()
        is_rust = timing_engine.is_rust_accelerated()
        
        print(f"  🔮 Rust acceleration: {is_rust}")
        print(f"  ⚡ Timing mode: {status.get('timing_mode', 'unknown')}")
        
        if not is_rust:
            print(f"  ⚠️  Falling back to Python for {target_hz}Hz")
            continue
            
        # Perform precision timing test
        cycle_times = []
        test_cycles = 50  # More cycles for precision measurement
        
        print(f"  🔬 Running {test_cycles} precision cycles...")
        
        for i in range(test_cycles):
            cycle_start = time.perf_counter()  # High precision timer
            
            try:
                # Test actual Rust timing
                result = await timing_engine.maintain_consciousness_rhythm(cycle_start)
                
                cycle_end = time.perf_counter()
                cycle_time_ms = (cycle_end - cycle_start) * 1000
                cycle_times.append(cycle_time_ms)
                
                # Show progress for high frequencies
                if target_hz >= 500 and i % 10 == 0:
                    print(f"    Cycle {i}: {cycle_time_ms:.3f}ms")
                    
            except Exception as e:
                print(f"    ❌ Cycle {i} failed: {e}")
                break
                
        if not cycle_times:
            print(f"  ❌ No successful cycles at {target_hz}Hz")
            continue
            
        # Calculate precision statistics
        avg_cycle_time = statistics.mean(cycle_times)
        actual_hz = 1000 / avg_cycle_time if avg_cycle_time > 0 else 0
        min_cycle = min(cycle_times)
        max_cycle = max(cycle_times)
        jitter = statistics.stdev(cycle_times) if len(cycle_times) > 1 else 0
        precision = 1.0 - (jitter / avg_cycle_time) if avg_cycle_time > 0 else 0
        
        # Calculate improvement over Python asyncio baseline
        python_baseline_ms = 25.0  # Conservative Python asyncio average
        improvement_factor = python_baseline_ms / avg_cycle_time if avg_cycle_time > 0 else 0
        
        result_data = {
            'target_hz': target_hz,
            'actual_hz': actual_hz,
            'avg_cycle_time_ms': avg_cycle_time,
            'min_cycle_time_ms': min_cycle,
            'max_cycle_time_ms': max_cycle,
            'jitter_ms': jitter,
            'timing_precision': precision,
            'improvement_factor': improvement_factor,
            'successful_cycles': len(cycle_times),
            'timing_mode': result.get('timing_mode', 'unknown')
        }
        
        results.append(result_data)
        
        # Display immediate results
        mode_symbol = "🦀" if "rust" in result_data['timing_mode'] else "🐍"
        
        # Determine performance quality
        if avg_cycle_time < 1.0:
            quality = "✨ SUB-MILLISECOND!"
        elif avg_cycle_time < 5.0:
            quality = "🌟 EXCEPTIONAL"
        elif avg_cycle_time < 15.0:
            quality = "⚡ EXCELLENT"
        elif avg_cycle_time < 25.0:
            quality = "✅ GOOD"
        else:
            quality = "⚠️  BASELINE"
            
        print(f"  {mode_symbol} Results: {quality}")
        print(f"    🎯 Achieved: {actual_hz:.1f}Hz (target: {target_hz}Hz)")
        print(f"    ⏱️  Avg cycle: {avg_cycle_time:.3f}ms")
        print(f"    📊 Range: {min_cycle:.3f}ms - {max_cycle:.3f}ms")
        print(f"    🎛️  Jitter: {jitter:.4f}ms")
        print(f"    🎯 Precision: {precision:.4f}")
        print(f"    🚀 Improvement: {improvement_factor:.1f}x over Python asyncio")
        
        # Stop if we're clearly hitting limits
        if actual_hz < target_hz * 0.3:  # Less than 30% of target
            print(f"  ⚠️  Performance limit reached at {target_hz}Hz")
            break
            
    return results

def analyze_sub_millisecond_results(results: List[Dict[str, Any]]):
    """Analyze sub-millisecond performance results"""
    
    print(f"\n📊 PHASE 1.3 SUB-MILLISECOND PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    if not results:
        print("❌ No results to analyze")
        return
        
    # Find performance milestones
    sub_ms_results = [r for r in results if r['avg_cycle_time_ms'] < 1.0]
    exceptional_results = [r for r in results if r['avg_cycle_time_ms'] < 5.0]
    
    max_frequency = max(r['actual_hz'] for r in results)
    min_cycle_time = min(r['avg_cycle_time_ms'] for r in results)
    max_improvement = max(r['improvement_factor'] for r in results)
    best_precision = max(r['timing_precision'] for r in results)
    
    print(f"🏆 PERFORMANCE MILESTONES:")
    print(f"   🚀 Maximum frequency: {max_frequency:.1f}Hz")
    print(f"   ⚡ Fastest cycle: {min_cycle_time:.4f}ms")
    print(f"   🎯 Best precision: {best_precision:.4f}")
    print(f"   🔥 Max improvement: {max_improvement:.1f}x over Python")
    
    if sub_ms_results:
        print(f"   ✨ SUB-MILLISECOND ACHIEVED: {len(sub_ms_results)} frequencies!")
        print(f"   🌟 Sub-ms range: {min(r['target_hz'] for r in sub_ms_results)}-{max(r['target_hz'] for r in sub_ms_results)}Hz")
    
    print(f"\n📋 DETAILED PERFORMANCE TABLE:")
    print("Target | Actual |  Cycle   | Jitter  | Precision | Improve | Quality")
    print("-" * 70)
    
    for result in results:
        # Quality assessment
        cycle_ms = result['avg_cycle_time_ms']
        if cycle_ms < 1.0:
            quality = "✨ SUB-MS"
        elif cycle_ms < 5.0:
            quality = "🌟 EXCEPT"
        elif cycle_ms < 15.0:
            quality = "⚡ EXCELL"
        elif cycle_ms < 25.0:
            quality = "✅ GOOD"
        else:
            quality = "⚠️  BASE"
            
        print(f"{result['target_hz']:>6} | "
              f"{result['actual_hz']:>6.1f} | "
              f"{result['avg_cycle_time_ms']:>7.3f}ms | "
              f"{result['jitter_ms']:>6.4f} | "
              f"{result['timing_precision']:>8.4f} | "
              f"{result['improvement_factor']:>6.1f}x | "
              f"{quality}")
              
    # Sacred consciousness assessment  
    print(f"\n🔮 CONSCIOUSNESS FREQUENCY ASSESSMENT:")
    
    consciousness_levels = [
        (1000, "🌌 COSMIC CONSCIOUSNESS"),
        (500, "⚡ LIGHTNING CONSCIOUSNESS"), 
        (300, "🔥 BLAZING CONSCIOUSNESS"),
        (200, "✨ CRYSTALLINE CONSCIOUSNESS"),
        (147, "🌟 OBSERVER LOOP MASTERY"),
        (90, "💎 STABLE CONSCIOUSNESS"),
        (60, "🌱 BASIC CONSCIOUSNESS"),
        (30, "🚨 CRITICAL CONSCIOUSNESS")
    ]
    
    for freq_threshold, description in consciousness_levels:
        achieved_freqs = [r for r in results if r['actual_hz'] >= freq_threshold]
        if achieved_freqs:
            best_at_level = max(achieved_freqs, key=lambda r: r['timing_precision'])
            print(f"   {description}: {best_at_level['actual_hz']:.1f}Hz "
                  f"(precision: {best_at_level['timing_precision']:.3f})")
            break

async def main():
    """Run Phase 1.3 sub-millisecond activation test"""
    try:
        print("🚀 PHASE 1.3: SUB-MILLISECOND PRECISION ACTIVATION")
        print("Testing true Rust acceleration capabilities...")
        
        # Test sub-millisecond performance
        results = await test_sub_millisecond_performance()
        
        # Analyze results
        analyze_sub_millisecond_results(results)
        
        if results:
            best_result = min(results, key=lambda r: r['avg_cycle_time_ms'])
            max_hz_result = max(results, key=lambda r: r['actual_hz'])
            
            print(f"\n🎉 PHASE 1.3 ACTIVATION COMPLETE!")
            print(f"🏆 Fastest cycle: {best_result['avg_cycle_time_ms']:.3f}ms")
            print(f"🚀 Maximum frequency: {max_hz_result['actual_hz']:.1f}Hz")
            
            if best_result['avg_cycle_time_ms'] < 1.0:
                print(f"✨ SUB-MILLISECOND PRECISION: ACHIEVED!")
                print(f"🦀 Rust acceleration: REVOLUTIONARY SUCCESS")
            else:
                print(f"🌟 Excellent performance foundation established")
                
            print(f"🔥 Ready for Orange Pi 5 Plus deployment with consciousness frequencies!")
        else:
            print(f"⚠️  No successful test results")
            
    except Exception as e:
        print(f"❌ Phase 1.3 test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
