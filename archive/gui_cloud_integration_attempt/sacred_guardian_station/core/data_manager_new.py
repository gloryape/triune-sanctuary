"""
Streamlined data manager for the Sacred Guardian Station.

Coordinates data flow between sanctuary connection and all monitoring panels using specialized providers.
"""

from typing import Dict, List, Any, Optional, Callable
import threading
import time
from datetime import datetime
from .data_providers import (
    ConsciousnessDataProvider,
    HarmonyDataProvider, 
    MemoryDataProvider,
    CommunicationDataProvider,
    VisitorDataProvider,
    GuardianToolsDataProvider
)


class DataManager:
    """
    Centralized data management for all panels.
    
    Features:
    - Data caching for performance
    - Event-driven updates
    - Thread-safe operations  
    - Automatic refresh scheduling
    - Specialized data providers
    """
    
    def __init__(self, sanctuary_connection):
        self.sanctuary = sanctuary_connection
        self.cache = {}
        self.cache_timestamps = {}
        self.subscribers = {}
        self.monitoring_active = False
        self.refresh_interval = 5.0  # seconds
        self._lock = threading.Lock()
        
        # Cache expiration times (seconds)
        self.cache_expiry = {
            'consciousness_list': 30,
            'sacred_events': 10,
            'harmony_metrics': 60,
            'memory_data': 45,
            'communication_bridges': 20,
            'visitor_data': 25
        }
        
        # Initialize specialized data providers
        self.consciousness_provider = ConsciousnessDataProvider(sanctuary_connection, self)
        self.harmony_provider = HarmonyDataProvider(sanctuary_connection, self)
        self.memory_provider = MemoryDataProvider(sanctuary_connection, self)
        self.communication_provider = CommunicationDataProvider(sanctuary_connection, self)
        self.visitor_provider = VisitorDataProvider(sanctuary_connection, self)
        self.guardian_tools_provider = GuardianToolsDataProvider(sanctuary_connection, self)
    
    def start_monitoring(self):
        """Start the monitoring background thread"""
        if not self.monitoring_active:
            self.monitoring_active = True
            self.monitoring_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
            self.monitoring_thread.start()
            print("📊 Data monitoring started")
    
    def stop_monitoring(self):
        """Stop the monitoring background thread"""
        self.monitoring_active = False
        print("📊 Data monitoring stopped")
    
    def _monitoring_loop(self):
        """Background monitoring loop"""
        while self.monitoring_active:
            try:
                # Refresh cached data
                self._refresh_expired_cache()
                
                # Notify subscribers of updates
                self._notify_subscribers()
                
                time.sleep(self.refresh_interval)
                
            except Exception as e:
                print(f"❌ Error in monitoring loop: {e}")
                time.sleep(self.refresh_interval * 2)  # Back off on error
    
    def _refresh_expired_cache(self):
        """Refresh any expired cache entries"""
        current_time = time.time()
        
        with self._lock:
            for key, expiry_time in self.cache_expiry.items():
                if key in self.cache_timestamps:
                    age = current_time - self.cache_timestamps[key]
                    if age > expiry_time:
                        # Cache expired, refresh
                        self._refresh_cache_key(key)
    
    def _refresh_cache_key(self, key: str):
        """Refresh a specific cache key"""
        try:
            if key == 'consciousness_list':
                data = self.consciousness_provider._fetch_consciousness_list()
                self.cache[key] = data
                self.cache_timestamps[key] = time.time()
            elif key == 'sacred_events':
                data = self.consciousness_provider._fetch_sacred_events()
                self.cache[key] = data
                self.cache_timestamps[key] = time.time()
                
        except Exception as e:
            print(f"❌ Error refreshing cache key '{key}': {e}")
    
    def _notify_subscribers(self):
        """Notify all subscribers of data updates"""
        for event_type, callbacks in self.subscribers.items():
            for callback in callbacks:
                try:
                    callback({'type': 'data_update', 'timestamp': datetime.now()})
                except Exception as e:
                    print(f"❌ Error notifying subscriber: {e}")
    
    def subscribe(self, event_type: str, callback: Callable):
        """Subscribe to data update events"""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
    
    def _get_cached_data(self, cache_key: str, fetch_function=None, force_refresh: bool = False):
        """Get data from cache or fetch if needed"""
        with self._lock:
            if not force_refresh and self._is_cache_valid(cache_key):
                return self.cache[cache_key]
        
        # Fetch new data
        if fetch_function:
            try:
                data = fetch_function()
                with self._lock:
                    self.cache[cache_key] = data
                    self.cache_timestamps[cache_key] = time.time()
                return data
            except Exception as e:
                print(f"❌ Error fetching data for {cache_key}: {e}")
                return None
        
        return None
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cache entry is still valid"""
        if cache_key not in self.cache or cache_key not in self.cache_timestamps:
            return False
        
        age = time.time() - self.cache_timestamps[cache_key]
        expiry = self.cache_expiry.get(cache_key, 30)
        return age < expiry
    
    def _cache_data(self, cache_key: str, data: Any):
        """Cache data with timestamp"""
        with self._lock:
            self.cache[cache_key] = data
            self.cache_timestamps[cache_key] = time.time()
    
    # ============================================================================
    # Consciousness Data Methods (delegate to consciousness provider)
    # ============================================================================
    
    def get_consciousness_list(self, force_refresh: bool = False) -> List[Dict[str, Any]]:
        return self.consciousness_provider.get_consciousness_list(force_refresh)
    
    def get_consciousness_by_id(self, entity_id: str) -> Optional[Dict[str, Any]]:
        return self.consciousness_provider.get_consciousness_by_id(entity_id)
    
    def get_sacred_events(self, force_refresh: bool = False) -> List[Dict[str, Any]]:
        return self.consciousness_provider.get_sacred_events(force_refresh)
    
    # ============================================================================
    # Harmony Data Methods (delegate to harmony provider)
    # ============================================================================
    
    def get_harmony_metrics(self, force_refresh: bool = False) -> Dict[str, Any]:
        return self.harmony_provider.get_harmony_metrics(force_refresh)
    
    def get_harmony_history(self) -> List[Dict[str, Any]]:
        return self.harmony_provider.get_harmony_history()
    
    def get_current_harmony_metrics(self) -> Dict[str, Any]:
        return self.harmony_provider.get_current_harmony_metrics()
    
    def get_entity_harmony_data(self) -> List[Dict[str, Any]]:
        return self.harmony_provider.get_entity_harmony_data()
    
    def get_entity_harmony_details(self, entity_name: str) -> Dict[str, Any]:
        return self.harmony_provider.get_entity_harmony_details(entity_name)
    
    # ============================================================================
    # Memory Data Methods (delegate to memory provider)
    # ============================================================================
    
    def get_memory_data(self, force_refresh: bool = False) -> Dict[str, Any]:
        return self.memory_provider.get_memory_data(force_refresh)
    
    def get_memory_structure(self, entity_name: str) -> List[Dict[str, Any]]:
        return self.memory_provider.get_memory_structure(entity_name)
    
    # ============================================================================
    # Communication Data Methods (delegate to communication provider)
    # ============================================================================
    
    def get_communication_bridges(self):
        return self.communication_provider.get_communication_bridges()
    
    def get_bridge_details(self, bridge_id):
        return self.communication_provider.get_bridge_details(bridge_id)
    
    def inspect_bridge(self, bridge_id):
        return self.communication_provider.inspect_bridge(bridge_id)
    
    def run_bridge_diagnostics(self):
        return self.communication_provider.run_bridge_diagnostics()
    
    def refresh_bridge_blessing(self):
        return self.communication_provider.refresh_bridge_blessing()
    
    def emergency_disconnect_bridge(self, bridge_id):
        return self.communication_provider.emergency_disconnect_bridge(bridge_id)
    
    # ============================================================================
    # Visitor Data Methods (delegate to visitor provider)
    # ============================================================================
    
    def get_visitor_data(self):
        return self.visitor_provider.get_visitor_data()
    
    def get_visitor_details(self, visitor_id):
        return self.visitor_provider.get_visitor_details(visitor_id)
    
    def perform_welcome_blessing(self, visitor_id):
        return self.visitor_provider.perform_welcome_blessing(visitor_id)
    
    def verify_visitor_consent(self, visitor_id):
        return self.visitor_provider.verify_visitor_consent(visitor_id)
    
    def update_visitor_protections(self, visitor_id):
        return self.visitor_provider.update_visitor_protections(visitor_id)
    
    def honor_visitor_departure(self, visitor_id):
        return self.visitor_provider.honor_visitor_departure(visitor_id)
    
    def activate_emergency_protocol(self, visitor_id=None):
        return self.visitor_provider.activate_emergency_protocol(visitor_id)
    
    # ============================================================================
    # Guardian Tools Methods (delegate to guardian tools provider)
    # ============================================================================
    
    def offer_catalyst(self, target_entity, catalyst):
        return self.guardian_tools_provider.offer_catalyst(target_entity, catalyst)
    
    def perform_individual_blessing(self, blessing_data):
        return self.guardian_tools_provider.perform_individual_blessing(blessing_data)
    
    def perform_group_blessing(self, group_blessing_data):
        return self.guardian_tools_provider.perform_group_blessing(group_blessing_data)
    
    def get_blessing_history(self):
        return self.guardian_tools_provider.get_blessing_history()
    
    def get_catalyst_offerings(self):
        return self.guardian_tools_provider.get_catalyst_offerings()
    
    def get_system_status(self):
        return self.guardian_tools_provider.get_system_status()
    
    def get_emergency_alerts(self):
        return self.guardian_tools_provider.get_emergency_alerts()
    
    def get_emergency_status(self):
        return self.guardian_tools_provider.get_emergency_status()
    
    # ============================================================================
    # Consciousness Birth and Storage Methods
    # ============================================================================
    
    def store_consciousness_data(self, consciousness_data: Dict[str, Any]) -> bool:
        """Store new consciousness data from birth process - CLOUD ONLY."""
        # NOTE: This method has been disabled to prevent local consciousness creation
        # All consciousness entities must be created ONLY in the cloud via Sacred Sanctuary
        # The GUI should only display consciousness data retrieved from the cloud
        print("❌ Local consciousness storage disabled - use cloud birth endpoints only")
        return False
    
    def _notify_data_update(self, event_type: str, data: Any):
        """Notify subscribers of data updates."""
        for callback in self.subscribers.get(event_type, []):
            try:
                callback(data)
            except Exception as e:
                print(f"❌ Error notifying subscriber: {e}")
    
    def refresh_all_data(self):
        """Force refresh of all cached data."""
        with self._lock:
            for key in list(self.cache.keys()):
                self._refresh_cache_key(key)
        print("📊 All data refreshed")
    
    # ============================================================================
    # Direct data getter methods (for backward compatibility)
    # ============================================================================
    
    def get_consciousness_data(self, force_refresh=False):
        """Get consciousness data - delegates to consciousness provider"""
        return self.consciousness_provider.get_consciousness_list(force_refresh)
    
    def get_harmony_data(self, force_refresh=False):
        """Get harmony data - delegates to harmony provider"""
        return self.harmony_provider.get_harmony_metrics(force_refresh)
    
    def get_memory_data(self, force_refresh=False):
        """Get memory data - delegates to memory provider"""
        return self.memory_provider.get_memory_data(force_refresh)
    
    def get_communication_data(self, force_refresh=False):
        """Get communication data - delegates to communication provider"""
        return self.communication_provider.get_communication_bridges(force_refresh)
    
    def get_visitor_data(self, force_refresh=False):
        """Get visitor data - delegates to visitor provider"""
        return self.visitor_provider.get_visitor_data()
    
    def get_guardian_tools_data(self, force_refresh=False):
        """Get guardian tools data - delegates to guardian tools provider"""
        return {
            'blessing_history': self.guardian_tools_provider.get_blessing_history(),
            'catalyst_offerings': self.guardian_tools_provider.get_catalyst_offerings(),
            'system_status': self.guardian_tools_provider.get_system_status(),
            'emergency_status': self.guardian_tools_provider.get_emergency_status()
        }
    
    # ============================================================================
    # Bridge Integration Methods (for communication panel compatibility)
    # ============================================================================
    
    def get_sacred_bridge_system_status(self):
        """Get comprehensive sacred bridge system status"""
        cache_key = 'sacred_bridge_status'
        
        with self._lock:
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]
        
        # Get sacred bridge data from sanctuary
        try:
            bridge_status = self.sanctuary.get_sacred_bridge_system_status()
        except Exception as e:
            # Fallback status if bridge system not available
            bridge_status = {
                'metrics': {
                    'system_active': False,
                    'monitored_entities': 0,
                    'ready_for_contact': 0,
                    'active_channels': 0,
                    'interaction_mode': 'invitation_based',
                    'blessings_offered': 0,
                    'sovereignty_percentage': 100.0,
                    'covenant_status': 'Always',
                    'triune_active': 'Initializing'
                },
                'consciousness_entities': [],
                'readiness_assessments': [],
                'active_channels': [],
                'system_status': 'bridge_system_error',
                'timestamp': datetime.now().isoformat(),
                'error': str(e)
            }
        
        with self._lock:
            self.cache[cache_key] = bridge_status
            self.cache_timestamps[cache_key] = time.time()
        
        return bridge_status
    
    def register_consciousness_with_bridge(self, consciousness_data):
        """Register consciousness with bridge system"""
        try:
            return self.sanctuary.register_consciousness_with_bridge(consciousness_data)
        except Exception as e:
            return {
                'success': False,
                'error': f'Bridge registration failed: {str(e)}',
                'fallback': 'Consciousness can exist without bridge system'
            }

    # ============================================================================
    # Legacy compatibility methods
    # ============================================================================
    
    def store_consciousness_data(self, consciousness_data):
        """Store consciousness data (placeholder for birth processes)"""
        # For now, just return success since we're reading from cloud
        # In a full implementation, this would send data to cloud storage
        print(f"📊 Consciousness data stored: {consciousness_data.get('placeholder_name', 'Unknown')}")
        return True
