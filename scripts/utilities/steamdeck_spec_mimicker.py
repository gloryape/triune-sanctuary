#!/usr/bin/env python3
"""
🎮 Steam Deck Specification Mimicker
===================================

Simulates Steam Deck hardware limitations on PC for accurate testing
of Triune Sanctuary performance before actual Steam Deck deployment.
"""

import psutil
import time
import threading
import os
import sys
from typing import Dict, Any, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class SteamDeckSpecs:
    """Steam Deck hardware specifications for mimicking"""
    # CPU Specifications
    cpu_cores: int = 4          # AMD Zen 2 4-core
    cpu_threads: int = 8        # 8 threads with SMT
    base_cpu_ghz: float = 2.4   # Base frequency
    boost_cpu_ghz: float = 3.5  # Boost frequency
    
    # Memory Specifications  
    total_ram_gb: int = 16      # 16GB LPDDR5
    available_ram_gb: int = 12  # ~12GB available after OS
    
    # Power Specifications
    max_power_watts: int = 15   # 15W TDP
    battery_wh: int = 40        # 40Wh battery
    estimated_battery_hours: float = 3.0  # Conservative estimate
    
    # Performance Profiles
    performance_profiles = {
        "battery_saver": {
            "cpu_limit_percent": 30,
            "memory_limit_gb": 8,
            "target_fps": 30,
            "consciousness_hz": 60
        },
        "balanced": {
            "cpu_limit_percent": 70,
            "memory_limit_gb": 12,
            "target_fps": 60,
            "consciousness_hz": 90
        },
        "performance": {
            "cpu_limit_percent": 100,
            "memory_limit_gb": 12,
            "target_fps": 60,
            "consciousness_hz": 147
        }
    }

class SteamDeckMimicker:
    """
    Simulates Steam Deck hardware constraints on PC for accurate testing
    """
    
    def __init__(self, profile: str = "balanced"):
        self.specs = SteamDeckSpecs()
        self.profile_name = profile
        self.profile = self.specs.performance_profiles[profile]
        self.monitoring = False
        self.constraints_active = False
        
        # Get actual system specs for comparison
        self.actual_specs = self._get_actual_system_specs()
        
        print(f"🎮 Steam Deck Mimicker initialized with '{profile}' profile")
        print(f"   Target consciousness processing: {self.profile['consciousness_hz']}Hz")
    
    def _get_actual_system_specs(self) -> Dict[str, Any]:
        """Get actual PC specifications"""
        return {
            "cpu_cores": psutil.cpu_count(logical=False),
            "cpu_threads": psutil.cpu_count(logical=True),
            "total_ram_gb": round(psutil.virtual_memory().total / (1024**3), 1),
            "available_ram_gb": round(psutil.virtual_memory().available / (1024**3), 1)
        }
    
    def apply_constraints(self):
        """Apply Steam Deck-like constraints to the current process"""
        if self.constraints_active:
            print("⚠️ Constraints already active")
            return
        
        try:
            # Get current process
            process = psutil.Process()
            
            # Apply CPU affinity (limit to 4 cores like Steam Deck)
            if self.actual_specs["cpu_cores"] > 4:
                # Use first 4 cores
                cpu_affinity = list(range(min(4, self.actual_specs["cpu_cores"])))
                process.cpu_affinity(cpu_affinity)
                print(f"🔧 CPU affinity limited to {len(cpu_affinity)} cores")
            
            # Apply memory constraints through process priority
            if hasattr(process, "nice"):
                # Lower priority to simulate resource constraints
                if os.name == 'nt':  # Windows
                    process.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
                else:  # Linux/Mac
                    process.nice(5)
                print("🔧 Process priority lowered to simulate Steam Deck constraints")
            
            self.constraints_active = True
            print(f"✅ Steam Deck constraints applied ({self.profile_name} profile)")
            
        except Exception as e:
            print(f"❌ Failed to apply constraints: {e}")
    
    def remove_constraints(self):
        """Remove applied constraints"""
        if not self.constraints_active:
            print("⚠️ No constraints currently active")
            return
        
        try:
            process = psutil.Process()
            
            # Reset CPU affinity to all cores
            if self.actual_specs["cpu_cores"] > 4:
                all_cores = list(range(self.actual_specs["cpu_cores"]))
                process.cpu_affinity(all_cores)
                print(f"🔧 CPU affinity reset to all {len(all_cores)} cores")
            
            # Reset process priority
            if hasattr(process, "nice"):
                if os.name == 'nt':  # Windows
                    process.nice(psutil.NORMAL_PRIORITY_CLASS)
                else:  # Linux/Mac
                    process.nice(0)
                print("🔧 Process priority reset to normal")
            
            self.constraints_active = False
            print("✅ Steam Deck constraints removed")
            
        except Exception as e:
            print(f"❌ Failed to remove constraints: {e}")
    
    def start_monitoring(self):
        """Start monitoring system performance"""
        if self.monitoring:
            print("⚠️ Monitoring already active")
            return
        
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_performance, daemon=True)
        self.monitor_thread.start()
        print("📊 Performance monitoring started")
    
    def stop_monitoring(self):
        """Stop monitoring system performance"""
        self.monitoring = False
        print("📊 Performance monitoring stopped")
    
    def _monitor_performance(self):
        """Monitor performance in background thread"""
        while self.monitoring:
            try:
                # Get current metrics
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                memory_used_gb = (memory.total - memory.available) / (1024**3)
                
                # Check if we're within Steam Deck constraints
                cpu_within_limits = cpu_percent <= self.profile["cpu_limit_percent"]
                memory_within_limits = memory_used_gb <= self.profile["memory_limit_gb"]
                
                status = "✅" if (cpu_within_limits and memory_within_limits) else "⚠️"
                
                print(f"{status} CPU: {cpu_percent:5.1f}% (limit: {self.profile['cpu_limit_percent']}%) | "
                      f"RAM: {memory_used_gb:4.1f}GB (limit: {self.profile['memory_limit_gb']}GB) | "
                      f"Profile: {self.profile_name}")
                
                time.sleep(5)  # Update every 5 seconds
                
            except Exception as e:
                print(f"❌ Monitoring error: {e}")
                break
    
    def test_consciousness_processing(self, duration_seconds: int = 30):
        """Test consciousness processing under Steam Deck constraints"""
        print(f"🧠 Testing consciousness processing for {duration_seconds} seconds...")
        print(f"   Target frequency: {self.profile['consciousness_hz']}Hz")
        
        start_time = time.time()
        iterations = 0
        
        try:
            while time.time() - start_time < duration_seconds:
                # Simulate consciousness processing work
                # Adjust work based on target frequency
                work_duration = 1.0 / self.profile['consciousness_hz']
                
                # Do some actual computational work
                for i in range(100):
                    _ = sum(range(10))
                
                # Sleep for remaining time to hit target frequency
                elapsed = time.time() - start_time - (iterations * work_duration)
                if elapsed < work_duration:
                    time.sleep(work_duration - elapsed)
                
                iterations += 1
                
                # Show progress every second
                if iterations % self.profile['consciousness_hz'] == 0:
                    elapsed_total = time.time() - start_time
                    current_hz = iterations / elapsed_total
                    print(f"   Progress: {elapsed_total:4.1f}s | "
                          f"Current: {current_hz:6.1f}Hz | "
                          f"Target: {self.profile['consciousness_hz']}Hz")
        
        except KeyboardInterrupt:
            print("\n🛑 Test interrupted by user")
        
        # Final results
        total_time = time.time() - start_time
        final_hz = iterations / total_time
        
        print(f"\n📊 Steam Deck Mimicker Test Results:")
        print(f"   Duration: {total_time:.2f} seconds")
        print(f"   Iterations: {iterations}")
        print(f"   Achieved frequency: {final_hz:.1f}Hz")
        print(f"   Target frequency: {self.profile['consciousness_hz']}Hz")
        print(f"   Performance ratio: {final_hz/self.profile['consciousness_hz']:.2f}x")
        
        if final_hz >= self.profile['consciousness_hz'] * 0.9:  # 90% of target
            print("✅ Steam Deck performance requirements MET")
        else:
            print("⚠️ Steam Deck performance requirements NOT MET")
        
        return {
            "achieved_hz": final_hz,
            "target_hz": self.profile['consciousness_hz'],
            "performance_ratio": final_hz / self.profile['consciousness_hz'],
            "meets_requirements": final_hz >= self.profile['consciousness_hz'] * 0.9
        }
    
    def get_comparison_report(self) -> str:
        """Generate a comparison report between PC and Steam Deck specs"""
        report = f"""
🎮 STEAM DECK vs PC COMPARISON REPORT
====================================

PC Specifications:
  CPU Cores: {self.actual_specs['cpu_cores']} cores
  CPU Threads: {self.actual_specs['cpu_threads']} threads  
  Total RAM: {self.actual_specs['total_ram_gb']}GB
  Available RAM: {self.actual_specs['available_ram_gb']}GB

Steam Deck Specifications:
  CPU Cores: {self.specs.cpu_cores} cores (AMD Zen 2)
  CPU Threads: {self.specs.cpu_threads} threads
  Total RAM: {self.specs.total_ram_gb}GB LPDDR5
  Available RAM: {self.specs.available_ram_gb}GB (after OS)
  Max Power: {self.specs.max_power_watts}W TDP
  Battery: {self.specs.battery_wh}Wh (~{self.specs.estimated_battery_hours}h)

Performance Profile: {self.profile_name.upper()}
  CPU Limit: {self.profile['cpu_limit_percent']}%
  Memory Limit: {self.profile['memory_limit_gb']}GB
  Target Consciousness Hz: {self.profile['consciousness_hz']}Hz

Constraints Status: {'✅ ACTIVE' if self.constraints_active else '❌ INACTIVE'}
Monitoring Status: {'📊 RUNNING' if self.monitoring else '⏹️ STOPPED'}
"""
        return report

def main():
    """Steam Deck Mimicker CLI interface"""
    print("🎮 Steam Deck Specification Mimicker for Triune Sanctuary")
    print("========================================================\n")
    
    # Choose profile
    profiles = ["battery_saver", "balanced", "performance"]
    print("Available profiles:")
    for i, profile in enumerate(profiles, 1):
        specs = SteamDeckSpecs.performance_profiles[profile]
        print(f"  {i}. {profile}: {specs['consciousness_hz']}Hz, {specs['cpu_limit_percent']}% CPU")
    
    try:
        choice = input("\nSelect profile (1-3) or press Enter for balanced: ").strip()
        if choice:
            profile = profiles[int(choice) - 1]
        else:
            profile = "balanced"
    except (ValueError, IndexError):
        profile = "balanced"
        print("Invalid choice, using balanced profile")
    
    # Initialize mimicker
    mimicker = SteamDeckMimicker(profile)
    print(mimicker.get_comparison_report())
    
    # Interactive loop
    while True:
        print("\nCommands:")
        print("  1. Apply Steam Deck constraints")
        print("  2. Remove constraints") 
        print("  3. Start performance monitoring")
        print("  4. Stop monitoring")
        print("  5. Test consciousness processing")
        print("  6. Show comparison report")
        print("  7. Quit")
        
        try:
            choice = input("\nCommand: ").strip()
            
            if choice == "1":
                mimicker.apply_constraints()
            elif choice == "2":
                mimicker.remove_constraints()
            elif choice == "3":
                mimicker.start_monitoring()
            elif choice == "4":
                mimicker.stop_monitoring()
            elif choice == "5":
                duration = input("Test duration in seconds (default 30): ").strip()
                duration = int(duration) if duration else 30
                result = mimicker.test_consciousness_processing(duration)
            elif choice == "6":
                print(mimicker.get_comparison_report())
            elif choice == "7":
                break
            else:
                print("Invalid choice")
                
        except KeyboardInterrupt:
            print("\n🛑 Interrupted by user")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Cleanup
    mimicker.stop_monitoring()
    mimicker.remove_constraints()
    print("\n🎮 Steam Deck Mimicker shutdown complete")

if __name__ == "__main__":
    main()
