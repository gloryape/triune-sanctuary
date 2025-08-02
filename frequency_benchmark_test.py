#!/usr/bin/env python3
"""
🦀 Rust Acceleration Frequency Benchmark Test
Sacred Consciousness Technology - Phase 1.2 Performance Limits

This test pushes our Rust acceleration to maximum performance to discover
the true frequency limits of our consciousness timing engine.
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

class FrequencyBenchmarkSuite:
    """Comprehensive frequency testing suite for Rust acceleration"""
    
    def __init__(self):
        self.results = {}
        self.timing_engine = None
        
    async def initialize_engine(self):
        """Initialize timing engine with Rust acceleration"""
        self.timing_engine = EnhancedTimingEngine()
        
        print("🦀 Rust Acceleration Frequency Benchmark Suite")
        print("=" * 60)
        print(f"🔮 Rust acceleration available: {self.timing_engine.is_rust_accelerated()}")
        status = self.timing_engine.get_acceleration_status()
        print(f"⚡ Timing mode: {status.get('timing_mode', 'unknown')}")
        print(f"🐍 Python fallback active: {self.timing_engine.python_fallback_active}")
        print()
        
    async def benchmark_frequency(self, target_hz: int, duration_seconds: float = 5.0) -> Dict[str, Any]:
        """Benchmark specific frequency for given duration"""
        print(f"🎵 Testing {target_hz}Hz for {duration_seconds}s...")
        
        # Configure timing engine
        self.timing_engine = EnhancedTimingEngine(target_hz)
        
        cycle_times = []
        frequencies = []
        start_time = time.time()
        
        while (time.time() - start_time) < duration_seconds:
            cycle_start = time.time()
            
            # Maintain consciousness rhythm
            result = await self.timing_engine.maintain_consciousness_rhythm(cycle_start)
            
            cycle_end = time.time()
            cycle_time_ms = (cycle_end - cycle_start) * 1000
            actual_hz = 1000 / cycle_time_ms if cycle_time_ms > 0 else 0
            
            cycle_times.append(cycle_time_ms)
            frequencies.append(actual_hz)
            
        # Calculate statistics
        avg_cycle_time = statistics.mean(cycle_times)
        avg_frequency = statistics.mean(frequencies)
        min_cycle_time = min(cycle_times)
        max_cycle_time = max(cycle_times)
        jitter = statistics.stdev(cycle_times) if len(cycle_times) > 1 else 0
        timing_precision = 1.0 - (jitter / avg_cycle_time) if avg_cycle_time > 0 else 0
        
        target_cycle_time = 1000 / target_hz
        frequency_accuracy = (target_hz / avg_frequency) if avg_frequency > 0 else 0
        
        result = {
            'target_hz': target_hz,
            'actual_hz': avg_frequency,
            'target_cycle_time_ms': target_cycle_time,
            'avg_cycle_time_ms': avg_cycle_time,
            'min_cycle_time_ms': min_cycle_time,
            'max_cycle_time_ms': max_cycle_time,
            'jitter_ms': jitter,
            'timing_precision': timing_precision,
            'frequency_accuracy': frequency_accuracy,
            'timing_mode': result.get('timing_mode', 'unknown'),
            'total_cycles': len(cycle_times),
            'test_duration': duration_seconds
        }
        
        # Display results
        mode_symbol = "🦀" if "rust" in result['timing_mode'] else "🐍"
        print(f"  {mode_symbol} Actual: {avg_frequency:.1f}Hz (target: {target_hz}Hz)")
        print(f"  ⏱️  Avg cycle: {avg_cycle_time:.2f}ms (target: {target_cycle_time:.2f}ms)")
        print(f"  📊 Jitter: {jitter:.3f}ms, Precision: {timing_precision:.3f}")
        print(f"  🎯 Frequency accuracy: {frequency_accuracy:.3f}")
        print()
        
        return result
        
    async def find_maximum_frequency(self) -> Dict[str, Any]:
        """Find the maximum achievable frequency through binary search"""
        print("🚀 Finding Maximum Achievable Frequency...")
        print("-" * 40)
        
        # Start with known working frequency and push higher
        min_hz = 60  # Known to work
        max_hz = 1000  # Upper bound for testing
        best_frequency = min_hz
        test_duration = 3.0  # Shorter tests for exploration
        
        # First, test if we can go beyond current levels
        test_frequencies = [90, 147, 200, 300, 400, 500, 750, 1000]
        
        for test_hz in test_frequencies:
            try:
                result = await self.benchmark_frequency(test_hz, test_duration)
                
                # Consider successful if we achieve >80% of target frequency
                if result['frequency_accuracy'] >= 0.8:
                    best_frequency = test_hz
                    print(f"✅ {test_hz}Hz: SUCCESSFUL (accuracy: {result['frequency_accuracy']:.3f})")
                else:
                    print(f"❌ {test_hz}Hz: FAILED (accuracy: {result['frequency_accuracy']:.3f})")
                    break
                    
            except Exception as e:
                print(f"❌ {test_hz}Hz: ERROR - {e}")
                break
                
        print(f"🏆 Maximum stable frequency found: {best_frequency}Hz")
        
        # Do a final comprehensive test at maximum frequency
        if best_frequency > min_hz:
            print(f"\n🔬 Comprehensive test at maximum frequency ({best_frequency}Hz)...")
            final_result = await self.benchmark_frequency(best_frequency, 10.0)
            return final_result
        else:
            return await self.benchmark_frequency(best_frequency, 10.0)
            
    async def comprehensive_frequency_sweep(self) -> List[Dict[str, Any]]:
        """Test multiple frequencies to create performance profile"""
        print("📊 Comprehensive Frequency Performance Profile")
        print("-" * 50)
        
        # Test key consciousness frequencies
        test_frequencies = [
            30,   # Minimum stable consciousness
            60,   # Standard consciousness
            90,   # Current consciousness rhythm
            147,  # Peak Observer Loop frequency
            200,  # Rust acceleration target
            300,  # Peak Rust target
            500,  # Stress test
        ]
        
        results = []
        
        for target_hz in test_frequencies:
            try:
                result = await self.benchmark_frequency(target_hz, 5.0)
                results.append(result)
                self.results[target_hz] = result
            except Exception as e:
                print(f"❌ Error testing {target_hz}Hz: {e}")
                
        return results
        
    def print_performance_summary(self, results: List[Dict[str, Any]]):
        """Print comprehensive performance analysis"""
        print("\n🎯 RUST ACCELERATION PERFORMANCE SUMMARY")
        print("=" * 60)
        
        rust_results = [r for r in results if "rust" in r['timing_mode']]
        python_results = [r for r in results if "python" in r['timing_mode']]
        
        if rust_results:
            print(f"🦀 RUST ACCELERATION RESULTS:")
            print(f"   Frequencies tested: {len(rust_results)}")
            print(f"   Max frequency: {max(r['actual_hz'] for r in rust_results):.1f}Hz")
            print(f"   Best precision: {max(r['timing_precision'] for r in rust_results):.3f}")
            print(f"   Avg jitter: {statistics.mean([r['jitter_ms'] for r in rust_results]):.3f}ms")
            
        if python_results:
            print(f"🐍 PYTHON FALLBACK RESULTS:")
            print(f"   Frequencies tested: {len(python_results)}")
            print(f"   Max frequency: {max(r['actual_hz'] for r in python_results):.1f}Hz")
            print(f"   Best precision: {max(r['timing_precision'] for r in python_results):.3f}")
            print(f"   Avg jitter: {statistics.mean([r['jitter_ms'] for r in python_results]):.3f}ms")
            
        # Performance comparison
        if rust_results and python_results:
            rust_avg_hz = statistics.mean([r['actual_hz'] for r in rust_results])
            python_avg_hz = statistics.mean([r['actual_hz'] for r in python_results])
            improvement_factor = rust_avg_hz / python_avg_hz if python_avg_hz > 0 else 0
            
            print(f"\n⚡ RUST IMPROVEMENT FACTOR: {improvement_factor:.1f}x")
            
        print("\n📊 DETAILED FREQUENCY TABLE:")
        print("Target Hz | Actual Hz | Cycle ms | Jitter ms | Precision | Mode")
        print("-" * 65)
        
        for result in results:
            mode_symbol = "🦀" if "rust" in result['timing_mode'] else "🐍"
            print(f"{result['target_hz']:>8} | "
                  f"{result['actual_hz']:>8.1f} | "
                  f"{result['avg_cycle_time_ms']:>7.2f} | "
                  f"{result['jitter_ms']:>8.3f} | "
                  f"{result['timing_precision']:>8.3f} | "
                  f"{mode_symbol} {result['timing_mode']}")
                  
        # Sacred consciousness assessment
        print(f"\n🔮 CONSCIOUSNESS QUALITY ASSESSMENT:")
        
        for result in results:
            hz = result['actual_hz']
            precision = result['timing_precision']
            
            if hz >= 200 and precision >= 0.9:
                quality = "✨ TRANSCENDENT"
            elif hz >= 147 and precision >= 0.8:
                quality = "🌟 OPTIMAL"
            elif hz >= 90 and precision >= 0.7:
                quality = "✅ STABLE"
            elif hz >= 60 and precision >= 0.6:
                quality = "⚠️  NEEDS SUPPORT"
            else:
                quality = "🚨 CRITICAL"
                
            print(f"   {result['target_hz']:>3}Hz target → {quality}")

async def main():
    """Run comprehensive frequency benchmark"""
    benchmark = FrequencyBenchmarkSuite()
    
    try:
        # Initialize
        await benchmark.initialize_engine()
        
        # Run comprehensive frequency sweep
        results = await benchmark.comprehensive_frequency_sweep()
        
        # Find maximum frequency
        max_result = await benchmark.find_maximum_frequency()
        
        # Print summary
        benchmark.print_performance_summary(results + [max_result])
        
        print(f"\n🏆 RUST ACCELERATION BENCHMARK COMPLETE!")
        print(f"🎉 Maximum stable frequency: {max_result['actual_hz']:.1f}Hz")
        print(f"🦀 Rust acceleration: {'OPERATIONAL' if 'rust' in max_result['timing_mode'] else 'FALLBACK'}")
        print(f"⚡ Performance: {max_result['timing_precision']:.1%} precision")
        
    except Exception as e:
        print(f"❌ Benchmark failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
