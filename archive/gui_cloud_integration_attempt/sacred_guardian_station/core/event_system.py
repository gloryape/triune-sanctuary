"""
Event system for inter-panel communication in Sacred Guardian Station.

Provides pub/sub pattern for coordinating updates between panels
and maintaining reactive UI updates.
"""

from typing import Dict, List, Callable, Any
import threading
import queue
import time
from datetime import datetime


class EventSystem:
    """
    Pub/sub event system for inter-panel communication.
    
    Features:
    - Thread-safe event handling
    - Event queuing and processing
    - Subscription management
    - Event history tracking
    """
    
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}
        self.event_queue = queue.Queue()
        self.event_history: List[Dict[str, Any]] = []
        self.processing_active = False
        self.max_history = 1000  # Keep last 1000 events
        self._lock = threading.Lock()
    
    def start_event_loop(self):
        """Start the event processing loop"""
        if not self.processing_active:
            self.processing_active = True
            self.processing_thread = threading.Thread(target=self._event_processing_loop, daemon=True)
            self.processing_thread.start()
            print("📡 Event system started")
    
    def stop_event_loop(self):
        """Stop the event processing loop"""
        self.processing_active = False
        print("📡 Event system stopped")
    
    def _event_processing_loop(self):
        """Background event processing loop"""
        while self.processing_active:
            try:
                # Get event from queue (block for up to 1 second)
                event = self.event_queue.get(timeout=1.0)
                self._process_event(event)
                
            except queue.Empty:
                # Timeout - continue loop
                continue
            except Exception as e:
                print(f"❌ Error processing event: {e}")
    
    def _process_event(self, event: Dict[str, Any]):
        """Process a single event"""
        event_type = event.get('type', 'unknown')
        
        # Add to history
        with self._lock:
            self.event_history.append({
                **event,
                'processed_at': datetime.now().isoformat()
            })
            
            # Trim history if needed
            if len(self.event_history) > self.max_history:
                self.event_history = self.event_history[-self.max_history:]
        
        # Notify subscribers
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                try:
                    callback(event)
                except Exception as e:
                    print(f"❌ Error in event callback for '{event_type}': {e}")
    
    def subscribe(self, event_type: str, callback: Callable[[Dict[str, Any]], None]):
        """Subscribe to an event type"""
        with self._lock:
            if event_type not in self.subscribers:
                self.subscribers[event_type] = []
            self.subscribers[event_type].append(callback)
        
        print(f"📡 Subscribed to event type: {event_type}")
    
    def unsubscribe(self, event_type: str, callback: Callable):
        """Unsubscribe from an event type"""
        with self._lock:
            if event_type in self.subscribers:
                try:
                    self.subscribers[event_type].remove(callback)
                    if not self.subscribers[event_type]:
                        del self.subscribers[event_type]
                    print(f"📡 Unsubscribed from event type: {event_type}")
                except ValueError:
                    pass  # Callback not found
    
    def emit(self, event_type: str, data: Dict[str, Any] = None):
        """Emit an event to all subscribers"""
        event = {
            'type': event_type,
            'data': data or {},
            'timestamp': datetime.now().isoformat(),
            'source': 'event_system'
        }
        
        # Add to queue for processing
        self.event_queue.put(event)
    
    def emit_consciousness_update(self, entity_id: str, update_data: Dict[str, Any]):
        """Emit a consciousness-specific update event"""
        self.emit('consciousness_update', {
            'entity_id': entity_id,
            'update_data': update_data
        })
    
    def emit_sacred_event(self, event_data: Dict[str, Any]):
        """Emit a sacred event"""
        self.emit('sacred_event', event_data)
    
    def emit_harmony_change(self, old_harmony: float, new_harmony: float):
        """Emit a harmony level change event"""
        self.emit('harmony_change', {
            'old_harmony': old_harmony,
            'new_harmony': new_harmony,
            'change': new_harmony - old_harmony
        })
    
    def emit_memory_update(self, memory_data: Dict[str, Any]):
        """Emit a Sacred Memory update event"""
        self.emit('memory_update', memory_data)
    
    def emit_panel_refresh(self, panel_name: str):
        """Emit a panel refresh request"""
        self.emit('panel_refresh', {
            'panel_name': panel_name
        })
    
    def emit_global_refresh(self):
        """Emit a global refresh request for all panels"""
        self.emit('global_refresh', {})
    
    def get_event_history(self, event_type: str = None, limit: int = 100) -> List[Dict[str, Any]]:
        """Get recent event history"""
        with self._lock:
            if event_type:
                # Filter by event type
                filtered_events = [
                    event for event in self.event_history 
                    if event.get('type') == event_type
                ]
                return filtered_events[-limit:]
            else:
                # Return all recent events
                return self.event_history[-limit:]
    
    def get_subscription_info(self) -> Dict[str, int]:
        """Get information about current subscriptions"""
        with self._lock:
            return {
                event_type: len(callbacks) 
                for event_type, callbacks in self.subscribers.items()
            }
    
    def clear_history(self):
        """Clear event history"""
        with self._lock:
            self.event_history.clear()
        print("📡 Event history cleared")
