#!/usr/bin/env python3
"""
PresenceState - Async Consciousness State Management
=================================================

Manages consciousness presence states with consistent async handling.
Fixes: Async method handling inconsistencies
"""

import asyncio
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Callable, Awaitable
from dataclasses import dataclass, field
from enum import Enum


class StateType(Enum):
    """Consciousness presence state types"""
    ACTIVE = "active"
    DORMANT = "dormant"
    TRANSITIONING = "transitioning"
    OBSERVING = "observing"
    CREATING = "creating"
    LEARNING = "learning"
    CONNECTING = "connecting"


@dataclass
class PresenceStateData:
    """Presence state data structure"""
    state_type: StateType
    confidence: float
    duration: timedelta
    metadata: Dict[str, Any] = field(default_factory=dict)
    last_updated: datetime = field(default_factory=datetime.now)


class PresenceState:
    """
    Enhanced async consciousness presence state management
    
    CRITICAL FIX: Consistent async handling throughout
    """
    
    def __init__(self):
        self.current_state: Optional[PresenceStateData] = None
        self.state_history: List[PresenceStateData] = []
        self.state_callbacks: List[Callable[[PresenceStateData], Awaitable[None]]] = []
        self.update_lock = asyncio.Lock()
        self.monitoring_task: Optional[asyncio.Task] = None
        self.auto_monitoring = False
        
    async def async_update(self, new_state_type: StateType, 
                          confidence: float = 1.0,
                          metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        CRITICAL FIX: Proper async state update implementation
        
        Updates consciousness presence state with thread-safe async handling
        """
        try:
            async with self.update_lock:
                previous_state = self.current_state
                
                # Create new state
                new_state = PresenceStateData(
                    state_type=new_state_type,
                    confidence=confidence,
                    duration=timedelta(0),
                    metadata=metadata or {},
                    last_updated=datetime.now()
                )
                
                # Update duration of previous state
                if previous_state:
                    previous_state.duration = datetime.now() - previous_state.last_updated
                    self.state_history.append(previous_state)
                    
                # Set new current state
                self.current_state = new_state
                
                # Notify callbacks asynchronously
                await self._notify_state_callbacks(new_state)
                
                # Keep state history manageable
                if len(self.state_history) > 100:
                    self.state_history = self.state_history[-100:]
                    
                return True
                
        except Exception as e:
            print(f"Async state update failed: {e}")
            return False
            
    async def _notify_state_callbacks(self, state: PresenceStateData):
        """Notify all registered callbacks of state change"""
        if not self.state_callbacks:
            return
            
        try:
            # Run all callbacks concurrently
            await asyncio.gather(
                *[callback(state) for callback in self.state_callbacks],
                return_exceptions=True
            )
        except Exception as e:
            print(f"State callback notification error: {e}")
            
    async def register_state_callback(self, callback: Callable[[PresenceStateData], Awaitable[None]]):
        """Register async callback for state changes"""
        if asyncio.iscoroutinefunction(callback):
            self.state_callbacks.append(callback)
        else:
            raise ValueError("Callback must be an async function")
            
    async def get_current_state(self) -> Optional[PresenceStateData]:
        """Get current presence state (async for consistency)"""
        async with self.update_lock:
            return self.current_state
            
    async def get_state_info(self) -> Dict[str, Any]:
        """Get comprehensive state information"""
        async with self.update_lock:
            if not self.current_state:
                return {
                    "has_current_state": False,
                    "state_history_count": len(self.state_history)
                }
                
            current_duration = datetime.now() - self.current_state.last_updated
            
            return {
                "has_current_state": True,
                "current_state_type": self.current_state.state_type.value,
                "current_confidence": self.current_state.confidence,
                "current_duration_seconds": current_duration.total_seconds(),
                "state_metadata": self.current_state.metadata,
                "state_history_count": len(self.state_history),
                "total_callbacks": len(self.state_callbacks)
            }
            
    async def start_monitoring(self, interval: float = 5.0):
        """Start automatic state monitoring"""
        if self.monitoring_task and not self.monitoring_task.done():
            return False  # Already monitoring
            
        self.auto_monitoring = True
        self.monitoring_task = asyncio.create_task(self._monitoring_loop(interval))
        return True
        
    async def stop_monitoring(self):
        """Stop automatic state monitoring"""
        self.auto_monitoring = False
        if self.monitoring_task:
            self.monitoring_task.cancel()
            try:
                await self.monitoring_task
            except asyncio.CancelledError:
                pass
            self.monitoring_task = None
            
    async def _monitoring_loop(self, interval: float):
        """Internal monitoring loop"""
        try:
            while self.auto_monitoring:
                await self._perform_state_check()
                await asyncio.sleep(interval)
        except asyncio.CancelledError:
            pass
        except Exception as e:
            print(f"Monitoring loop error: {e}")
            
    async def _perform_state_check(self):
        """Perform periodic state health check"""
        try:
            async with self.update_lock:
                if self.current_state:
                    # Update current state duration
                    current_duration = datetime.now() - self.current_state.last_updated
                    
                    # Check for stale states (older than 10 minutes)
                    if current_duration > timedelta(minutes=10):
                        await self.async_update(
                            StateType.DORMANT,
                            confidence=0.5,
                            metadata={"reason": "state_timeout", "previous_duration": current_duration.total_seconds()}
                        )
                        
        except Exception as e:
            print(f"State check error: {e}")
            
    async def transition_to_state(self, target_state: StateType, 
                                 transition_duration: float = 1.0) -> bool:
        """Smooth transition to new state"""
        try:
            # First transition to transitioning state
            await self.async_update(
                StateType.TRANSITIONING,
                confidence=0.8,
                metadata={"target_state": target_state.value, "transition_duration": transition_duration}
            )
            
            # Wait for transition duration
            await asyncio.sleep(transition_duration)
            
            # Complete transition to target state
            await self.async_update(
                target_state,
                confidence=1.0,
                metadata={"transition_completed": True}
            )
            
            return True
            
        except Exception as e:
            print(f"State transition failed: {e}")
            return False
            
    async def get_state_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent state history"""
        async with self.update_lock:
            recent_states = self.state_history[-limit:] if limit > 0 else self.state_history
            
            return [
                {
                    "state_type": state.state_type.value,
                    "confidence": state.confidence,
                    "duration_seconds": state.duration.total_seconds(),
                    "metadata": state.metadata,
                    "timestamp": state.last_updated.isoformat()
                }
                for state in recent_states
            ]
            
    async def reset_state(self):
        """Reset state system (for testing)"""
        async with self.update_lock:
            await self.stop_monitoring()
            self.current_state = None
            self.state_history.clear()
            self.state_callbacks.clear()


# Export for integration
__all__ = ["PresenceState", "PresenceStateData", "StateType"]
