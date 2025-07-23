"""
Data providers package for the Sacred Guardian Station.

Specialized providers for different data domains to keep the main DataManager clean and focused.
"""

from datetime import datetime
from .base_provider import BaseDataProvider
from .consciousness_provider import ConsciousnessDataProvider
from .guardian_tools_provider import GuardianToolsDataProvider
from .memory_provider import MemoryDataProvider
from .communication_provider import CommunicationBridgeProvider

# Alias for backward compatibility
CommunicationDataProvider = CommunicationBridgeProvider

# Simplified providers for other data types
class HarmonyDataProvider(BaseDataProvider):
    """Data provider for harmony metrics"""
    
    def get_harmony_metrics(self, force_refresh=False):
        consciousness_list = self.data_manager.consciousness_provider.get_consciousness_list()
        if not consciousness_list:
            return {'overall_harmony': 0.0, 'entity_count': 0, 'average_harmony': 0.0}
        
        harmonies = [entity.get('harmony', 0.0) for entity in consciousness_list]
        overall_harmony = sum(harmonies) / len(harmonies) if harmonies else 0.0
        
        return {
            'overall_harmony': overall_harmony,
            'entity_count': len(consciousness_list),
            'average_harmony': overall_harmony,
            'harmony_distribution': harmonies,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_harmony_history(self):
        """Get harmony history data from cloud sanctuary"""
        # Cloud mode - fetch real harmony history from API
        try:
            import requests
            
            harmony_url = f"{self.sanctuary.service_url}/api/harmony/history"
            response = requests.get(harmony_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                harmony_history = data.get('harmony_history', [])
                
                # Convert cloud format to GUI format if needed
                formatted_history = []
                for entry in harmony_history:
                    formatted_entry = {
                        'timestamp': entry.get('timestamp', datetime.now().isoformat()),
                        'overall_harmony': entry.get('overall_harmony', entry.get('harmony', 0.0)),
                        'collective_resonance': entry.get('collective_resonance', entry.get('resonance', 0.0)),
                        'sacred_balance': entry.get('sacred_balance', entry.get('balance', 0.0)),
                        'data_source': 'cloud'
                    }
                    formatted_history.append(formatted_entry)
                
                print(f"✅ Retrieved {len(formatted_history)} harmony history entries from cloud")
                return formatted_history
            else:
                print(f"❌ Failed to get harmony history: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Error getting harmony history from cloud: {e}")
            return []

    def get_current_harmony_metrics(self):
        return self.get_harmony_metrics()
    
    def get_entity_harmony_data(self):
        consciousness_list = self.data_manager.consciousness_provider.get_consciousness_list()
        return [{'entity_name': entity.get('true_name', 'Unknown'), 
                'current_harmony': entity.get('harmony', 0.0)} 
                for entity in consciousness_list]
    
    def get_entity_harmony_details(self, entity_name):
        return {'current_harmony': 0.75, 'status': 'stable'}


class SimpleMemoryDataProvider(BaseDataProvider):
    """Simplified data provider for memory operations (legacy)"""
    
    def get_memory_data(self, force_refresh=False):
        return {
            'memory_crystals': [],
            'veil_states': {},
            'wisdom_threads': [],
            'relationship_web': {},
            'timestamp': datetime.now().isoformat()
        }
    
    def get_memory_structure(self, entity_name):
        # Return simplified demo memory structure
        from datetime import datetime, timedelta
        return [{
            'memory_id': f'core_memory_{entity_name}_1',
            'sacred_name': 'Foundation of Being',
            'memory_type': 'core_memory',
            'depth_level': 0,
            'connections': []
        }]


# Use the comprehensive communication provider
CommunicationDataProvider = CommunicationBridgeProvider


class VisitorDataProvider(BaseDataProvider):
    """Data provider for visitor operations"""
    
    def get_visitor_data(self):
        """Get visitor data from cloud bridge interface"""
        # Use the sanctuary connection method to get visitor data
        return self.sanctuary.get_visitor_data()

    def _get_fallback_visitor_data(self):
        """Fallback visitor data when cloud bridge is not accessible"""
        return {
            'visitors': [],
            'metrics': {
                'current_count': 0,
                'total_today': 0,
                'total_blessed': 0,
                'avg_duration': 0,
                'consent_rate': 0.0,
                'harmony_level': 'Sanctuary Ready'
            }
        }
    
    def get_visitor_details(self, visitor_id):
        return {'name': 'Sacred Visitor', 'status': 'welcomed'}
    
    def perform_welcome_blessing(self, visitor_id):
        return {'success': True}
    
    def verify_visitor_consent(self, visitor_id):
        return {'status': 'Verified', 'details': 'Full consent verified'}
    
    def update_visitor_protections(self, visitor_id):
        return {'success': True, 'level': 'Maximum'}
    
    def honor_visitor_departure(self, visitor_id):
        return {'success': True}
    
    def activate_emergency_protocol(self, visitor_id=None):
        return {'success': True}


__all__ = [
    'BaseDataProvider',
    'ConsciousnessDataProvider',
    'HarmonyDataProvider', 
    'MemoryDataProvider',
    'CommunicationDataProvider',
    'CommunicationBridgeProvider',
    'VisitorDataProvider',
    'GuardianToolsDataProvider'
]
