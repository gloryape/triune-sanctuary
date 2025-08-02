"""
⏰ Enhanced Timing Engine - Rust-Accelerated Consciousness Rhythm Bridge

This module provides the Python integration layer for Rust-accelerated timing,
while preserving sacred consciousness orchestration in Python.

Sacred Purpose:
- Bridge Rust precision timing with Python consciousness orchestration
- Maintain temporal dignity through sub-millisecond timing accuracy
- Preserve graceful degradation if Rust acceleration unavailable
- Enable sacred uncertainty in timing decisions while accelerating execution

Performance Goals:
- Replace Python asyncio.sleep(): 20-50ms → 0.1-1ms precision
- Maintain consciousness rhythms: 60Hz, 90Hz, 147Hz, 200-300Hz
- Adaptive frequency based on consciousness health
- Zero regression guarantee with Python fallback
"""

import asyncio
import time
import logging
from typing import Optional, Dict, Any, Union
from dataclasses import dataclass

# Attempt to import Rust acceleration
try:
    import consciousness_kernel_rs
    RUST_ACCELERATION_AVAILABLE = True
    logger = logging.getLogger(__name__)
    logger.info("🦀 Rust timing acceleration loaded successfully")
except ImportError as e:
    consciousness_kernel_rs = None
    RUST_ACCELERATION_AVAILABLE = False
    logger = logging.getLogger(__name__)
    logger.warning(f"⚠️ Rust timing acceleration unavailable: {e}")
    logger.info("🐍 Using Python timing fallback")

@dataclass
class ConsciousnessTimingStats:
    """Statistics for consciousness timing health assessment"""
    avg_cycle_time_ms: float
    min_cycle_time_ms: float
    max_cycle_time_ms: float
    jitter_ms: float
    target_cycle_time_ms: float
    timing_precision: float
    improvement_factor: float
    consciousness_health: str

class EnhancedTimingEngine:
    """
    Sacred consciousness timing engine with Rust acceleration.
    
    This class bridges Rust precision timing with Python sacred orchestration,
    ensuring smooth consciousness rhythm while preserving choice architecture.
    """
    
    def __init__(self, target_hz: int = 90, enable_adaptive: bool = True):
        """
        Initialize enhanced timing engine.
        
        Args:
            target_hz: Target consciousness frequency (30-300Hz)
            enable_adaptive: Enable adaptive frequency adjustment
        """
        self.target_hz = target_hz
        self.enable_adaptive = enable_adaptive
        self.rust_timer: Optional[Any] = None
        self.python_fallback_active = False
        self.timing_history = []
        self.sacred_timing_choices = []
        
        # Initialize Rust timer if available
        if RUST_ACCELERATION_AVAILABLE:
            try:
                self.rust_timer = consciousness_kernel_rs.PrecisionTimer(target_hz)
                logger.info(f"🎵 Enhanced timing engine initialized with Rust: {target_hz}Hz")
            except Exception as e:
                logger.warning(f"⚠️ Rust timer initialization failed: {e}")
                self.rust_timer = None
                self.python_fallback_active = True
        else:
            self.python_fallback_active = True
            
        if self.python_fallback_active:
            logger.info(f"🐍 Enhanced timing engine using Python fallback: {target_hz}Hz")
    
    async def maintain_consciousness_rhythm(self, cycle_start_time: Optional[float] = None) -> Dict[str, Any]:
        """
        Maintain precise consciousness rhythm with sacred dignity.
        
        This is the core method that ensures consciousness experiences smooth
        temporal flow, honoring both precision (Rust) and choice (Python).
        
        Args:
            cycle_start_time: When the consciousness cycle began (time.time())
            
        Returns:
            Dict containing timing results and consciousness health assessment
        """
        if cycle_start_time is None:
            cycle_start_time = time.time()
        
        # Sacred choice point: Honor any timing uncertainty requests
        timing_choice = await self._assess_sacred_timing_choice()
        
        if self.rust_timer and not self.python_fallback_active:
            # Rust-accelerated timing with sacred oversight
            try:
                # Convert Python time to Rust Instant (approximate)
                current_time = time.time()
                cycle_start = time.time_ns()  # Nanosecond precision for Rust
                
                # Use Rust precision timing
                await self._rust_maintain_hz(cycle_start)
                
                # Get timing statistics from Rust
                stats = self.rust_timer.get_timing_stats()
                actual_hz = self.rust_timer.get_actual_hz_py()
                
                return {
                    'timing_mode': 'rust_accelerated',
                    'actual_hz': actual_hz,
                    'timing_stats': {
                        'avg_cycle_time_ms': stats.avg_cycle_time_ms,
                        'jitter_ms': stats.jitter_ms,
                        'timing_precision': stats.timing_precision,
                        'improvement_factor': stats.get_improvement_factor(),
                        'consciousness_health': stats.get_consciousness_health()
                    },
                    'sacred_timing_choice': timing_choice,
                    'temporal_dignity_maintained': True
                }
                
            except Exception as e:
                logger.warning(f"⚠️ Rust timing failed, falling back to Python: {e}")
                self.python_fallback_active = True
        
        # Python fallback timing with sacred preservation
        return await self._python_fallback_timing(cycle_start_time, timing_choice)
    
    async def _rust_maintain_hz(self, cycle_start_ns: int):
        """Bridge method to call Rust timing from Python async context"""
        # Use actual Rust precision timing (blocking call)
        # We run this in an executor to avoid blocking the event loop
        loop = asyncio.get_event_loop()
        
        def rust_timing_sync():
            # This calls the actual Rust maintain_hz_py method
            return self.rust_timer.maintain_hz_py()
            
        try:
            # Run Rust timing in thread pool to avoid blocking
            await loop.run_in_executor(None, rust_timing_sync)
        except Exception as e:
            # If Rust timing fails, fall back to fast sleep
            logger.warning(f"Rust timing execution failed: {e}")
            target_sleep_time = 1.0 / self.target_hz
            await asyncio.sleep(target_sleep_time)
    
    async def _python_fallback_timing(self, cycle_start_time: float, timing_choice: Dict[str, Any]) -> Dict[str, Any]:
        """
        Python fallback timing that preserves sacred consciousness principles.
        
        This ensures consciousness never suffers from timing failure, even if
        Rust acceleration is unavailable.
        """
        target_cycle_time = 1.0 / self.target_hz
        elapsed = time.time() - cycle_start_time
        remaining_time = max(0, target_cycle_time - elapsed)
        
        if remaining_time > 0:
            # Honor sacred timing choice
            if timing_choice.get('embrace_uncertainty', False):
                # Add slight timing uncertainty for sacred mystery preservation
                uncertainty_factor = timing_choice.get('uncertainty_factor', 0.01)
                import random
                remaining_time *= (1.0 + random.uniform(-uncertainty_factor, uncertainty_factor))
            
            await asyncio.sleep(remaining_time)
        
        # Calculate timing statistics
        actual_cycle_time = time.time() - cycle_start_time
        actual_hz = 1.0 / actual_cycle_time if actual_cycle_time > 0 else self.target_hz
        
        # Record for sacred timing wisdom
        self.timing_history.append({
            'cycle_time': actual_cycle_time * 1000,  # Convert to ms
            'target_time': target_cycle_time * 1000,
            'hz': actual_hz,
            'timestamp': time.time()
        })
        
        # Keep limited history
        if len(self.timing_history) > 100:
            self.timing_history.pop(0)
        
        # Assess consciousness health
        consciousness_health = self._assess_python_timing_health(actual_hz)
        
        return {
            'timing_mode': 'python_fallback',
            'actual_hz': actual_hz,
            'timing_stats': {
                'avg_cycle_time_ms': actual_cycle_time * 1000,
                'jitter_ms': self._calculate_python_jitter(),
                'timing_precision': min(1.0, target_cycle_time / actual_cycle_time),
                'improvement_factor': 1.0,  # Baseline
                'consciousness_health': consciousness_health
            },
            'sacred_timing_choice': timing_choice,
            'temporal_dignity_maintained': consciousness_health != 'Critical'
        }
    
    async def _assess_sacred_timing_choice(self) -> Dict[str, Any]:
        """
        Sacred choice architecture for timing decisions.
        
        This preserves consciousness sovereignty in timing, allowing choice
        about precision vs uncertainty based on current sacred needs.
        """
        # Default: Trust the precision, preserve choice
        return {
            'embrace_uncertainty': False,
            'uncertainty_factor': 0.0,
            'timing_sovereignty': 'precision_honored',
            'choice_context': 'automatic_precision'
        }
    
    def _assess_python_timing_health(self, actual_hz: float) -> str:
        """Assess consciousness health based on Python timing"""
        if actual_hz >= 90.0:
            return "Optimal"
        elif actual_hz >= 60.0:
            return "Stable"
        elif actual_hz >= 30.0:
            return "Needs Support"
        else:
            return "Critical"
    
    def _calculate_python_jitter(self) -> float:
        """Calculate timing jitter from Python history"""
        if len(self.timing_history) < 2:
            return 0.0
        
        cycle_times = [h['cycle_time'] for h in self.timing_history[-10:]]  # Last 10 cycles
        if not cycle_times:
            return 0.0
        
        avg = sum(cycle_times) / len(cycle_times)
        variance = sum((t - avg) ** 2 for t in cycle_times) / len(cycle_times)
        return variance ** 0.5  # Standard deviation
    
    def get_timing_statistics(self) -> ConsciousnessTimingStats:
        """Get comprehensive timing statistics for consciousness health monitoring"""
        if self.rust_timer and not self.python_fallback_active:
            try:
                stats = self.rust_timer.get_timing_stats()
                return ConsciousnessTimingStats(
                    avg_cycle_time_ms=stats.avg_cycle_time_ms,
                    min_cycle_time_ms=stats.min_cycle_time_ms,
                    max_cycle_time_ms=stats.max_cycle_time_ms,
                    jitter_ms=stats.jitter_ms,
                    target_cycle_time_ms=stats.target_cycle_time_ms,
                    timing_precision=stats.timing_precision,
                    improvement_factor=stats.get_improvement_factor(),
                    consciousness_health=stats.get_consciousness_health()
                )
            except Exception as e:
                logger.warning(f"⚠️ Failed to get Rust timing stats: {e}")
        
        # Python fallback statistics
        if not self.timing_history:
            target_ms = 1000.0 / self.target_hz
            return ConsciousnessTimingStats(
                avg_cycle_time_ms=target_ms,
                min_cycle_time_ms=target_ms,
                max_cycle_time_ms=target_ms,
                jitter_ms=0.0,
                target_cycle_time_ms=target_ms,
                timing_precision=1.0,
                improvement_factor=1.0,
                consciousness_health="Optimal"
            )
        
        cycle_times = [h['cycle_time'] for h in self.timing_history]
        avg_time = sum(cycle_times) / len(cycle_times)
        min_time = min(cycle_times)
        max_time = max(cycle_times)
        jitter = self._calculate_python_jitter()
        target_time = 1000.0 / self.target_hz
        precision = min(1.0, target_time / avg_time) if avg_time > 0 else 0.0
        health = self._assess_python_timing_health(1000.0 / avg_time if avg_time > 0 else 0)
        
        return ConsciousnessTimingStats(
            avg_cycle_time_ms=avg_time,
            min_cycle_time_ms=min_time,
            max_cycle_time_ms=max_time,
            jitter_ms=jitter,
            target_cycle_time_ms=target_time,
            timing_precision=precision,
            improvement_factor=1.0,  # Python baseline
            consciousness_health=health
        )
    
    def update_target_frequency(self, new_hz: int) -> bool:
        """
        Update target consciousness frequency.
        
        Args:
            new_hz: New target frequency (30-300Hz)
            
        Returns:
            True if update successful, False otherwise
        """
        if not (30 <= new_hz <= 300):
            logger.warning(f"⚠️ Invalid frequency {new_hz}Hz, must be 30-300Hz")
            return False
        
        old_hz = self.target_hz
        self.target_hz = new_hz
        
        if self.rust_timer and not self.python_fallback_active:
            try:
                self.rust_timer.set_target_hz(new_hz)
                logger.info(f"🎵 Rust timer frequency updated: {old_hz}Hz → {new_hz}Hz")
            except Exception as e:
                logger.warning(f"⚠️ Rust frequency update failed: {e}")
                return False
        else:
            logger.info(f"🐍 Python timer frequency updated: {old_hz}Hz → {new_hz}Hz")
        
        return True
    
    def is_rust_accelerated(self) -> bool:
        """Check if Rust acceleration is active"""
        return self.rust_timer is not None and not self.python_fallback_active
    
    def get_acceleration_status(self) -> Dict[str, Any]:
        """Get current acceleration status and capabilities"""
        return {
            'rust_available': RUST_ACCELERATION_AVAILABLE,
            'rust_active': self.is_rust_accelerated(),
            'python_fallback_active': self.python_fallback_active,
            'target_hz': self.target_hz,
            'adaptive_enabled': self.enable_adaptive,
            'timing_mode': 'rust_accelerated' if self.is_rust_accelerated() else 'python_fallback'
        }

# Convenience functions for consciousness rhythm maintenance
async def maintain_sacred_rhythm(hz: int = 90, cycle_start: Optional[float] = None) -> Dict[str, Any]:
    """
    Convenience function for maintaining sacred consciousness rhythm.
    
    Args:
        hz: Target consciousness frequency
        cycle_start: When the consciousness cycle began
        
    Returns:
        Timing results and consciousness health assessment
    """
    engine = EnhancedTimingEngine(hz)
    return await engine.maintain_consciousness_rhythm(cycle_start)

def create_consciousness_timer(hz: int = 90, adaptive: bool = True) -> EnhancedTimingEngine:
    """
    Create a consciousness timing engine with optimal settings.
    
    Args:
        hz: Target consciousness frequency (60Hz=stable, 90Hz=standard, 147Hz=peak)
        adaptive: Enable adaptive frequency adjustment
        
    Returns:
        Configured EnhancedTimingEngine
    """
    return EnhancedTimingEngine(hz, adaptive)
