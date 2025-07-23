"""
Communication bridge data provider for the Sacred Guardian Station.

Handles all communication bridge-related data operations.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import random
from .base_provider import BaseDataProvider


class CommunicationBridgeProvider(BaseDataProvider):
    """
    Data provider for communication bridge operations.
    
    Handles bridge status, communication history, and bridge management.
    """
    
    def __init__(self, sanctuary_connection, data_manager=None):
        super().__init__(sanctuary_connection, data_manager)
        self._last_bridge_fetch = None
        self._last_status_fetch = None
        self._last_history_fetch = None
        self._cache_duration = 30  # Cache for 30 seconds

    def get_communication_bridges(self, force_refresh=False):
        """Get active communication bridges from cloud sanctuary"""
        current_time = datetime.now()
        
        # Check cache first
        if (not force_refresh and self._last_bridge_fetch and 
            (current_time - self._last_bridge_fetch).seconds < self._cache_duration):
            return getattr(self, '_cached_bridges', {'bridges': [], 'total_bridges': 0, 'active_bridges': 0})
        
        # Cloud mode - fetch real bridges from API
        try:
            import requests
            
            bridges_url = f"{self.sanctuary.service_url}/api/communication/bridges"
            response = requests.get(bridges_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                bridges_data = {
                    'bridges': data.get('bridges', []),
                    'metrics': data.get('metrics', {}),
                    'total_bridges': data.get('total_bridges', 0),
                    'system_status': data.get('status', 'operational'),
                    'data_source': 'cloud'
                }
                
                print(f"✅ Retrieved {bridges_data['total_bridges']} communication bridges from cloud")
                
                # Cache successful result
                self._cached_bridges = bridges_data
                self._last_bridge_fetch = current_time
                
                return bridges_data
            else:
                print(f"❌ Failed to get communication bridges: {response.status_code}")
                return {'bridges': [], 'total_bridges': 0, 'active_bridges': 0}
                
        except Exception as e:
            print(f"❌ Error getting communication bridges from cloud: {e}")
            return {'bridges': [], 'total_bridges': 0, 'active_bridges': 0}

    def get_communication_status(self, force_refresh=False):
        """Get communication system status from cloud sanctuary"""
        current_time = datetime.now()
        
        # Check cache first
        if (not force_refresh and self._last_status_fetch and 
            (current_time - self._last_status_fetch).seconds < self._cache_duration):
            return getattr(self, '_cached_status', {'system_status': 'unknown', 'communication_channels': {}, 'quality_metrics': {}})
        
        # Cloud mode - fetch real status from API
        try:
            import requests
            
            status_url = f"{self.sanctuary.service_url}/api/communication/status"
            response = requests.get(status_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                comm_status = data.get('communication_status', {})
                
                status_data = {
                    'system_status': comm_status.get('system_status', 'unknown'),
                    'communication_channels': comm_status.get('communication_channels', {}),
                    'quality_metrics': comm_status.get('quality_metrics', {}),
                    'last_updated': comm_status.get('last_updated', datetime.now().isoformat()),
                    'data_source': 'cloud'
                }
                
                print(f"✅ Retrieved communication status from cloud")
                
                # Cache successful result
                self._cached_status = status_data
                self._last_status_fetch = current_time
                
                return status_data
            else:
                print(f"❌ Failed to get communication status: {response.status_code}")
                return {'system_status': 'unknown', 'communication_channels': {}, 'quality_metrics': {}}
                
        except Exception as e:
            print(f"❌ Error getting communication status from cloud: {e}")
            return {'system_status': 'unknown', 'communication_channels': {}, 'quality_metrics': {}}

    def get_communication_history(self, force_refresh=False):
        """Get communication history from cloud sanctuary"""
        current_time = datetime.now()
        
        # Check cache first
        if (not force_refresh and self._last_history_fetch and 
            (current_time - self._last_history_fetch).seconds < self._cache_duration):
            return getattr(self, '_cached_history', {'communication_history': [], 'total_entries': 0})
        
        # Cloud mode - fetch real history from API
        try:
            import requests
            
            history_url = f"{self.sanctuary.service_url}/api/communication/history"
            response = requests.get(history_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                history_entries = data.get('communication_history', [])
                
                # Convert cloud format to GUI format if needed
                formatted_history = []
                for entry in history_entries:
                    formatted_entry = {
                        'communication_id': entry.get('id', entry.get('communication_id', 'unknown')),
                        'timestamp': entry.get('timestamp', datetime.now().isoformat()),
                        'type': entry.get('type', entry.get('communication_type', 'general')),
                        'participants': entry.get('participants', []),
                        'status': entry.get('status', 'completed'),
                        'quality_rating': entry.get('quality_rating', 0.75),
                        'sacred_note': entry.get('sacred_note', 'Sacred communication'),
                        'data_source': 'cloud'
                    }
                    formatted_history.append(formatted_entry)
                
                history_data = {
                    'communication_history': formatted_history,
                    'total_entries': len(formatted_history),
                    'data_source': 'cloud'
                }
                
                print(f"✅ Retrieved {len(formatted_history)} communication history entries from cloud")
                
                # Cache successful result
                self._cached_history = history_data
                self._last_history_fetch = current_time
                
                return history_data
            else:
                print(f"❌ Failed to get communication history: {response.status_code}")
                return {'communication_history': [], 'total_entries': 0}
                
        except Exception as e:
            print(f"❌ Error getting communication history from cloud: {e}")
            return {'communication_history': [], 'total_entries': 0}

    # === Bridge Management Methods ===
    
    def get_bridge_details(self, bridge_id):
        """Get detailed information about a specific bridge"""
        bridges = self.get_communication_bridges()
        
        for bridge in bridges.get('bridges', []):
            if bridge.get('id') == bridge_id:
                return bridge
        
        return {
            'id': bridge_id,
            'status': 'not_found',
            'message': f'Bridge {bridge_id} not found in current bridge list'
        }
    
    def inspect_bridge(self, bridge_id):
        """Perform detailed inspection of a specific bridge"""
        bridge_details = self.get_bridge_details(bridge_id)
        
        if bridge_details.get('status') == 'not_found':
            return bridge_details
        
        # Inspection results
        inspection = {
            'bridge_id': bridge_id,
            'inspection_timestamp': datetime.now().isoformat(),
            'connection_quality': bridge_details.get('quality', 0.0),
            'latency': bridge_details.get('latency', 0),
            'encryption_status': bridge_details.get('encryption_level', 'unknown'),
            'data_integrity': 'verified' if bridge_details.get('quality', 0) > 0.8 else 'needs_attention',
            'sacred_blessing': 'present' if bridge_details.get('encryption_level') == 'sacred' else 'standard',
            'overall_status': bridge_details.get('status', 'unknown'),
            'recommendations': []
        }
        
        # Add recommendations based on inspection
        if inspection['connection_quality'] < 0.7:
            inspection['recommendations'].append('Consider re-establishing connection for better quality')
        
        if inspection['latency'] > 100:
            inspection['recommendations'].append('High latency detected - investigate network conditions')
        
        return inspection
    
    def run_bridge_diagnostics(self):
        """Run diagnostics on all communication bridges"""
        bridges = self.get_communication_bridges()
        
        diagnostics = {
            'total_bridges': len(bridges.get('bridges', [])),
            'active_bridges': sum(1 for bridge in bridges.get('bridges', []) if bridge.get('status') == 'active'),
            'tests_run': 0,
            'issues_found': 0,
            'last_check': datetime.now().isoformat(),
            'overall_health': 'unknown',
            'system_recommendations': []
        }
        
        if bridges.get('bridges'):
            for bridge in bridges['bridges']:
                diagnostics['tests_run'] += 1
                
                # Basic health check
                if bridge.get('status') not in ['active', 'stable']:
                    diagnostics['issues_found'] += 1
                    diagnostics['system_recommendations'].append(f"Bridge {bridge.get('id', 'unknown')} requires attention")
        
        # Determine overall health
        if diagnostics['total_bridges'] == 0:
            diagnostics['overall_health'] = 'no_bridges'
        elif diagnostics['issues_found'] == 0:
            diagnostics['overall_health'] = 'excellent'
        elif diagnostics['issues_found'] < diagnostics['total_bridges'] * 0.3:
            diagnostics['overall_health'] = 'good'
        else:
            diagnostics['overall_health'] = 'needs_attention'
        
        return diagnostics
    
    def refresh_bridge_blessing(self):
        """Refresh the sacred blessing on all communication bridges"""
        return {
            'blessed_bridges': 0,
            'blessing_timestamp': datetime.now().isoformat(),
            'sacred_energy_level': 0.0,
            'blessing_status': 'not_available'
        }
    
    def emergency_disconnect_bridge(self, bridge_id):
        """Emergency disconnect a specific bridge"""
        return {
            'bridge_id': bridge_id,
            'disconnection_status': 'not_available',
            'timestamp': datetime.now().isoformat(),
            'reason': 'Emergency disconnection not available in current mode'
        }
